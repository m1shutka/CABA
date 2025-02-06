from flask import Flask
from flask import render_template, request, redirect, flash, session, send_from_directory
from stages import stages, progress
from email_manager import send_ya_mail
from farm import farm
from stack import Stack
from dotenv import load_dotenv
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from UserLogin import UserLogin
from db_api import DBApi
from pdf_writer import PDFWirter
from datetime import timedelta, datetime
from ua_parser import user_agent_parser
import os
from werkzeug.exceptions import HTTPException

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
app.config['PERMANENT_SESSION_LIFETIME'] =  timedelta(hours=2)
app.config['UPLOAD_FOLDER'] = os.getenv("UPLOAD_FOLDER")
login_manager = LoginManager(app)

login_manager.login_view = 'login'
login_manager.login_message = 'Необходимо авторизоваться'
login_manager.login_message_category = "alert alert-danger alert-dismissible fade show text-center"

stk = Stack()


@login_manager.user_loader
def load_user(user_id):

    user = UserLogin().fromDB(user_id)

    return user


def progress_output():
    
    print(f"Current stage: {session['stage']}")
    print(f"Current flags: {session['local_flags']}")
    print(f"Current stack: {session['stk']}")
    #print(f"Current changes: {session['local_changes']}")
    for i in range(1, len(session['local_progress'])):
        print(f"{session['timing'][i]} stage: {i}, template: {session['local_stages'][i][0]}, Current progress {session['local_progress'][i]}")


def body_params():

    for i in session['local_progress'][2].keys():
        if session['local_progress'][2][i] == True:
            return i

    return None


@app.errorhandler(404)
def pageNotFount(error):

    if current_user.is_authenticated:
        menu = DBApi().getMenu(True, current_user.is_admin())
    else:
        menu = DBApi().getMenu(False, False)

    for i in menu:
        i.append('nav-link')

    return render_template('error_page.html', menu=menu, error='Страница не найдена!'), 404


#@app.errorhandler(Exception)
def handle_exception(e):

    if isinstance(e, HTTPException):
        return e

    return render_template("error_page.html", menu=[], error='Ошибка приложения!'), 500


@app.route("/download_protocol", methods = ['GET', 'POST'])
@login_required
def download_protocol():

    pdfw = PDFWirter(app.config['UPLOAD_FOLDER'], current_user.get_login())
    pdfw.write_file(session['local_stages'], session['local_progress'], session['timing'])

    return send_from_directory(app.config['UPLOAD_FOLDER'], pdfw.filename + '.pdf', as_attachment=True)


@app.route('/protocol', methods = ['GET', 'POST'])
@login_required
def protocol():

    if current_user.is_authenticated:
        menu = DBApi().getMenu(True, current_user.is_admin())
    else:
        menu = DBApi().getMenu(False, False)

    for i in menu:
        i.append('nav-link')

    return render_template("protocol.html", menu=menu)


@app.route("/registration", methods = ['GET', 'POST'])
@login_required
def registration():

    if current_user.is_admin():

        if request.method == "POST":

            if len(request.form['phone']) != 11:
                flash('Неверный формат ввода телефона (89997774545)!', "alert alert-danger alert-dismissible fade show text-center")
            elif '@' not in request.form['email']:
                flash('Неверный формат ввода почты (mail@example.org)!', "alert alert-danger alert-dismissible fade show text-center")
            elif request.form['time'] not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '24', '36']:
                flash('Неверный формат ввода кол-ва месяцев (1, 2, ... 12, 24, 36)!', "alert alert-danger alert-dismissible fade show text-center")
            else:
                login, password, msg = DBApi().user_registration(request.form['name'], request.form['email'], request.form['phone'], request.form['time'])
                if msg == '':
                    msg = send_ya_mail(msg_info={'to':request.form['email'], 'header': 'Данные учетной записи САВА', 'text':f'Логин: {login}\nПароль: {password}'})
                    if msg == "Success":
                        flash(f'Зарегестрировано, login: {login}, password: {password}', "alert alert-success alert-dismissible fade show text-center")
                    else:
                        flash(msg, "alert alert-success alert-dismissible fade show text-center")
                else:
                        flash(msg, "alert alert-success alert-dismissible fade show text-center")

        if current_user.is_authenticated:
            menu = DBApi().getMenu(True, current_user.is_admin())
        else:
            menu = DBApi().getMenu(False, False)

        for i in menu:
            i.append('nav-link active') if i[0] == 'Регистрация' else i.append('nav-link')
        
        return render_template("registration.html", menu=menu)
    
    else: 
        return redirect('/main', 301)


@app.route("/login", methods = ['GET', 'POST'])
def login():

    if request.method == "POST":
        
        ua = user_agent_parser.Parse(request.user_agent.string)
        ua['addr'] = request.headers.get('X-Real-IP', request.remote_addr)
        msg = DBApi().user_autorization(request.form['login'], request.form['password'], ua)

        if type(msg) != str:

            userlogin = UserLogin().create(msg)
            login_user(userlogin, remember=False, fresh=False, duration=None, force=False)
            session.permanent = True
            return redirect('/main', 301)

        else:
            flash(f'{msg}', "alert alert-danger alert-dismissible fade show text-center")

    if current_user.is_authenticated:
        menu = DBApi().getMenu(True, current_user.is_admin())
    else:
        menu = DBApi().getMenu(False, False)

    for i in menu:
        i.append('nav-link active') if i[0] == 'Войти' else i.append('nav-link')

    return render_template('sign_in.html', menu=menu)


@app.route('/info')
def info():

    if current_user.is_authenticated:
        menu = DBApi().getMenu(True, current_user.is_admin())
    else:
        menu = DBApi().getMenu(False, False)

    for i in menu:
        i.append('nav-link active') if i[0] == 'Справка' else i.append('nav-link')

    return render_template('info.html', menu=menu)


@app.route('/profile')
@login_required
def profile():

    if current_user.is_authenticated:
        menu = DBApi().getMenu(True, current_user.is_admin())
        user_login = current_user.get_login()
        sessions = current_user.get_user_sessions()
    else:
        menu = DBApi().getMenu(False, False)
        user_login = ''

    for i in menu:
        i.append('nav-link active') if i[0] == 'Учетная запись' else i.append('nav-link')

    return render_template('profile.html', menu=menu, user_login=user_login, sessions=sessions)


@app.route('/logout')
@login_required
def logout():

    ua = user_agent_parser.Parse(request.user_agent.string)
    ua['addr'] = request.remote_addr
    DBApi().user_logout(current_user.get_id(), ua)
    logout_user()

    return redirect('/login', 301)


@app.route("/main")
@app.route("/")
def main():

    session['stage'] = 0
    session['local_stages'] = [['aa0', {'prev': stages['aa0']['prev'], 'next': stages['aa0']['next']}]]
    session['local_progress'] = [{'1': False}]
    session['local_flags'] = {'flag_changes': False}
    session['local_changes'] = []
    session['stk'] = []
    session['timing'] = [datetime.now().strftime("%H:%M:%S")]

    if current_user.is_authenticated:
        menu = DBApi().getMenu(True, current_user.is_admin())
    else:
        menu = DBApi().getMenu(False, False)

    for i in menu:
        i.append('nav-link active') if i[0] == 'Главная' else i.append('nav-link')
        
    return render_template("index.html", menu=menu)

@app.route("/next_stage")
@login_required
def next_stage():

    next_atr = session['local_stages'][session['stage']][1]['next']

    print( session['local_flags']['flag_changes'])
    

    if session['local_stages'][session['stage']][0] == 'fb13':
        stk.push(session['stk'], 'fa23')
    elif session['local_stages'][session['stage']][0] == 'ga13':
        stk.push(session['stk'], 'ga23')
    elif session['local_stages'][session['stage']][0] == 'ca8' and next_atr == 'fb3.2':
        stk.push(session['stk'],'ca24.3')
    elif session['local_stages'][session['stage']][0] == 'cb8' and next_atr == 'fb3.2':
        stk.push(session['stk'],'ca13.3')
    elif session['local_stages'][session['stage']][0] == 'da8' and next_atr == 'fb3.2':
        stk.push(session['stk'],'da13.3')
    elif session['local_stages'][session['stage']][0] == 'db8' and next_atr == 'fb3.2':
        stk.push(session['stk'], 'da24.6')
    elif session['local_stages'][session['stage']][0] == 'eh13.1' and next_atr == 'ga3.2':
        stk.push(session['stk'],'ea16')
    elif session['local_stages'][session['stage']][0] == 'eb8' and next_atr == 'ga3.2':
        stk.push(session['stk'], 'ea16')
    elif session['local_stages'][session['stage']][0] == 'fa4' and next_atr == 'ca5':
        stk.push(session['stk'],'fb24.9')
    elif session['local_stages'][session['stage']][0] == 'ga4' and next_atr == 'ca5':
        stk.push(session['stk'],'ga18')

    if next_atr == 'ba3.2' and stk.get(session['stk']) == 'fa23':
        next_atr, session['stk'] = stk.pop(session['stk'])
    elif next_atr == 'ba3.2' and stk.get(session['stk']) == 'ga23':
        next_atr, session['stk'] = stk.pop(session['stk'])
    elif next_atr[2:] == '12' and not stk.is_empty(session['stk']):
        next_atr, session['stk'] = stk.pop(session['stk'])

    if session['stage'] + 1 == len(session['local_progress']):
        #print('1')
        session['local_stages'].append([next_atr, {'prev': stages[next_atr]['prev'], 'next': stages[next_atr]['next']}])
        session['local_progress'].append(progress[next_atr[2:]].copy())
        session['timing'].append(datetime.now().strftime("%H:%M:%S"))
        session['stage'] += 1

        session['local_stages'][session['stage']][1]['prev'] = session['local_stages'][session['stage'] - 1][0]
        session['local_flags']['flag_changes'] = False

    elif session['local_flags']['flag_changes']:
        #print('2')
        session['local_stages'] = session['local_stages'][:session['stage'] + 1]
        session['local_progress'] = session['local_progress'][:session['stage'] + 1]
        session['timing'] = session['timing'][:session['stage'] + 1]

        session['local_stages'].append([next_atr, {'prev': stages[next_atr]['prev'], 'next': stages[next_atr]['next']}])
        session['local_progress'].append(progress[next_atr[2:]].copy())
        session['timing'].append(datetime.now().strftime("%H:%M:%S"))
        session['stage'] += 1

        session['local_stages'][session['stage']][1]['prev'] = session['local_stages'][session['stage'] - 1][0]
        session['local_flags']['flag_changes'] = False

    elif not session['local_flags']['flag_changes'] and session['stage'] < len(session['local_progress']):
        #print('3')
        session['stage'] += 1

    progress_output()

    session['local_changes'].clear()

    if session['local_stages'][session['stage']][1]['prev'][2:] == '12':
        return redirect('/protocol', 301)
    else:
        return redirect(stages[session['local_stages'][session['stage']][0]]['attr']['base_url'], 301)


@app.route("/prev_stage")
@login_required
def prev_stage():

    if session['local_stages'][session['stage']][0] == 'fa23':
        stk.push(session['stk'], 'fa23')
    elif session['local_stages'][session['stage']][0] == 'ga23':
        stk.push(session['stk'], 'ga23')
    if (session['local_stages'][session['stage']][0] == 'aa9.1' and stk.get(session['stk']) == 'fa23') or (session['local_stages'][session['stage']][0] == 'aa9.1' and stk.get(session['stk']) == 'ga23'):
        _, session['stk'] = stk.pop(session['stk'])

    if session['local_flags']['flag_changes']:
        session['local_stages'] = session['local_stages'][:session['stage'] + 1]
        session['local_progress'] = session['local_progress'][:session['stage'] + 1]
        session['timing'] = session['timing'][:session['stage'] + 1]
        session['local_flags']['flag_changes'] = False

    if session['stage'] > 1:
        session['stage'] -= 1
    else:
        return redirect('/main', 301)
    session['local_changes'].clear()

    progress_output()

    return redirect(stages[session['local_stages'][session['stage']][0]]['attr']['base_url'], 301)


@app.route("/to_beginning")
@login_required
def to_beginning():

    if body_params() != None:
        session['stage'] = 2
    else:
        session['stage'] = 1

    session['local_stages'] = session['local_stages'][:session['stage'] + 1]
    session['local_progress'] = session['local_progress'][:session['stage'] + 1]
    session['timing'] = session['timing'][:session['stage'] + 1]
    session['local_flags'] = {'flag_changes': False}

    return redirect('/next_stage')


@app.route("/test_first", methods = ['GET', 'POST'])
@login_required
def test_first():
    
    if stages[session['local_stages'][session['stage']][0]]['attr']['base_url'] != "test_first":
        return redirect('/prev_stage')

    if request.is_json:
        button_number = request.args.get('button_number')
        session['local_progress'][session['stage']][button_number] = not session['local_progress'][session['stage']][button_number]

    if session['local_stages'][session['stage']][0] != 'aa1':
        body_p = body_params()

        if body_p == None:
            return redirect('/to_beginning', 301)
        
    info_text = stages[session['local_stages'][session['stage']][0]]['attr']['info']['text'].copy()
    info_styles = stages[session['local_stages'][session['stage']][0]]['attr']['info']['styles'].copy()

    if session['local_stages'][session['stage']][0][2:] == '10.1':
        info_text[1] = f'Оценивайте дыхание, пульс и SpO2 непрерывно, измеряйте АД не реже раза в 5 минут). При нарушениях дыхания, снижения SpO2 ниже 92% При АД выше {farm["ads"][body_p][1]} или ниже {farm["ads"][body_p][0]} мм.рт.ст., развитии судорог нажмите «В начало»'
    elif session['local_stages'][session['stage']][0][2:] == '17':
        info_text[0] = f'Установите воздуховод #{farm["air_duct"][body_p]} или ларингеальную маску #{farm["i-gel"][body_p]}'
    elif session['local_stages'][session['stage']][0][2:] == '20':
        info_text[0] = f'Поместите сахар/конфету за щёку пациента (не за зубы). При наличии доступа в вену – внутривенно {farm["glucose"][body_p]} мл 20% раствора глюкозы (ампулы 40% глюкозы развести пополам 0,9% раствором NaCl)'
    elif session['local_stages'][session['stage']][0][2:] == '21':
        info_text[0] = f'При наличии сосудистого доступа – введите внутривенно вальпроевую кислоту (детям старше 3 лет) {farm["valpro"][body_p]} мл за 5 минут либо мидазолам {farm["midazolam"][body_p]} мл, либо диазепам {farm["diazepam"][body_p]} мл'
        info_text[1] = f'При отсутствии сосудистого доступа внутримышечно ввести мидазолам {farm["midazolam"][body_p]} мл, либо диазепам {farm["diazepam"][body_p]} мл'
    elif session['local_stages'][session['stage']][0][2:] == '24.3':
        info_text[0] = f'Введите внутривенно/внутрикостно или (при отсутствии сосудистого доступа – внутримышечно) 1. Эпинефрин (адреналин) {farm["adrenalin_v"][body_p]} мл'
        info_text[1] = f'2. Дексаметазон {farm["dexamethasone"][body_p]} мл или Преднизолон {farm["prednisolone"][body_p]} мл или Метилпреднизолон {farm["methylprednisolone"][body_p]} мг или Гидрокортизон {farm["hydrocortisone"][body_p]} мл (только внутримышечно)'
    elif session['local_stages'][session['stage']][0][2:] == '24.3.2':
        info_text[0] = f'Вводите внутривенно капельно или (при отсутствии сосудистого доступа – внутримышечно) Атропин {farm["atropin"][body_p]} мл в 10 мл (5 мл при внутримышечном введении) 0,9% раствора NaCl. Максимальное количество введений - два. Целевое ЧСС не менее {farm["css"][body_p][0]} в мин (при внутримышечном введении интервал 1 раз в 5 минут)'
    elif session['local_stages'][session['stage']][0][2:] == '24.3.3':
        info_text[0] = f'Вводите внутривенно капельно Допамин (дофамин) 100 мг в 200 мл 5 % раствора глюкозы или 0,9 % раствора NaCl. До достижения артериального давления не менее 90/60 мм.рт.ст., ЧСС не менее {farm["css"][body_p][0]} в мин'
    elif session['local_stages'][session['stage']][0][2:] == '24.3.4':
        info_text[0] = f'Введите внутривенно болюс интралипида 20% {farm["intralipid_b"][body_p]} мл (1,5 мл/кг) в течение 1 минуты. Немедленно начните инфузию со скоростью {farm["intralipid_k"][body_p]} кап/мин (15 мл/кг/час) (взрослому пациенту - 1 л/час, 300 капель в минуту)'
    elif session['local_stages'][session['stage']][0][2:] == '24.3.5':
        info_text[0] = f'Введите струйно внутривенно/внутрикостно или (при отсутствии сосудистого доступа – внутримышечно под язык) Эпинефрин (адреналин) {farm["adrenalin_v"][body_p]} мл'
    elif session['local_stages'][session['stage']][0][2:] == '24.4':
        info_text[0] = f'Введите ингаляционно через небулайзер 1. Будесонид {farm["budesonid"][body_p]} мл + NaCl 0,9% 3,0 мл'
        info_text[1] = f'2. Адреналин {farm["adrenalin_n"][body_p]} мл + NaCl 0,9% 5,0 мл'
    elif session['local_stages'][session['stage']][0][2:] == '24.5':
        info_text[0] = f'Введите ингаляционно через небулайзер 1. Сальбутамол {farm["salbutamol"][body_p]} доз'
    elif session['local_stages'][session['stage']][0][2:] == '24.6':
        info_text[0] = f'Введите внутривенно/внутрикостно или (при отсутствии сосудистого доступа – внутримышечно) 1.Аминофиллин (эуфиллин) {farm["eufillin"][body_p]} мл'
        info_text[1] = f'2. Дексаметазон {farm["dexamethasone"][body_p]} мл или Преднизолон {farm["prednisolone"][body_p]} мл или Метилпреднизолон {farm["methylprednisolone"][body_p]} мг или Гидрокортизон {farm["hydrocortisone"][body_p]} мл (только внутримышечно)'
    elif session['local_stages'][session['stage']][0][2:] == '24.7.1':
        info_text[0] = f'Введите внутривенно или (при отсутствии сосудистого доступа – внутримышечно) Фуросемид {farm["furosemide"][body_p]} мл'
    elif session['local_stages'][session['stage']][0][2:] == '24.8':
        info_text[0] = f'Введите внутривенно/внутрикостно Урапидил 25 мг в/в медленно, далее капельно (у пациентов старше 18 лет)'
        info_text[1] = f'Сульфат магнезии 25% {farm["magnesia_sulfate"][body_p]} мл в/в медленно'
        info_text[2] = f'Фуросемид {farm["furosemide"][body_p]} мл внутривенно'
    elif session['local_stages'][session['stage']][0][2:] == '24.8.1':
        info_text[0] = f'Введите внутривенно Урапидил 25 мг в/в медленно, далее капельно (у пациентов старше 18 лет)'
        info_text[1] = f'Сульфат магнезии 25% {farm["magnesia_sulfate"][body_p]} мл в/в медленно'
        info_text[2] = f'Фуросемид {farm["furosemide"][body_p]} мл внутривенно'
    elif session['local_stages'][session['stage']][0][2:] == '24.9':
        info_text[0] = f'Важно! Только при ДаД выше 120 мм.рт.ст. АД снижать на 10-15% Введите внутривенно/внутрикостно Урапидил 12, 5 мг в/в медленно, далее капельно (у пациентов старше 18 лет)'
        info_text['text'][1] = f'Сульфат магнезии 25% {farm["magnesia_sulfate"][body_p]} мл в/в медленно'
    elif session['local_stages'][session['stage']][0][2:] == '28.5':
        info_text[0] = f'Присоедините к лицевой маске (размер #{farm["face_mask"][body_p]}) или установленной ларингеальной маске ( размер #{farm["i-gel"][body_p]}) дыхательный мешок'
    elif session['local_stages'][session['stage']][0][2:] == '28.7':
        info_text[2] = f'С третьего разряда дефибрилляции введите амиодарон {farm["amiodaron"][body_p]} мг при отсутствии – лидокаин {farm["lidocaine"][body_p]} мг (пациентам старше 1 года)'
    elif session['local_stages'][session['stage']][0][2:] == '33.1':
        info_text[0] = f'Присоедините к лицевой маске (размер  #{farm["face_mask"][body_p]}) или установленной ларингеальной маске (размер #{farm["i-gel"][body_p]}) дыхательный мешок'

    buttons_text = stages[session['local_stages'][session['stage']][0]]['attr']['buttons']['text'].copy()
    buttons_styles = stages[session['local_stages'][session['stage']][0]]['attr']['buttons']['styles'].copy()

    true_count = 0
    for i in session['local_progress'][session['stage']].keys():
        if session['local_progress'][session['stage']][i] == True:
            buttons_text[int(i) - 1] = 'Выполнено'
            buttons_styles[int(i) - 1] = f'btn btn-lg btn-success btn{i} w-100'
            true_count += 1
        else:
            buttons_text[int(i) - 1] = 'Выполнить'
            buttons_styles[int(i) - 1] = f'btn btn-lg btn-outline-success btn{i} w-100'

    navigation = []
    navigation_text = stages[session['local_stages'][session['stage']][0]]['attr']['navigation']['text'].copy()
    navigation_styles = stages[session['local_stages'][session['stage']][0]]['attr']['navigation']['styles'].copy()
    navigation_links = stages[session['local_stages'][session['stage']][0]]['attr']['navigation']['links'].copy()

    if true_count == len(session['local_progress'][session['stage']].keys()):
        if session['local_stages'][session['stage']][0] == 'aa1':
            navigation_styles[0] = 'btn btn-lg btn-success w-100 btn-next'
            navigation.append((navigation_styles[0], navigation_text[0], navigation_links[0]))
        else: 
            navigation_styles[2] = 'btn btn-lg btn-success w-100 btn-next'
            navigation.append((navigation_styles[0], navigation_text[0], navigation_links[0]))
            navigation.append((navigation_styles[1], navigation_text[1], navigation_links[1]))
            navigation.append((navigation_styles[2], navigation_text[2], navigation_links[2]))
    else:
        if session['local_stages'][session['stage']][0] == 'aa1':
            navigation_styles[0] = 'btn btn-lg btn-outline-danger w-100 btn-next disabled'
            navigation.append((navigation_styles[0], navigation_text[0], navigation_links[0]))
        else:
            navigation_styles[2] = 'btn btn-lg btn-outline-danger w-100 btn-next disabled'
            navigation.append((navigation_styles[0], navigation_text[0], navigation_links[0]))
            navigation.append((navigation_styles[1], navigation_text[1], navigation_links[1]))
            navigation.append((navigation_styles[2], navigation_text[2], navigation_links[2]))

    data = []
    for i in zip(buttons_text, buttons_styles, info_text, info_styles):
        data.append(i)

    if current_user.is_authenticated:
        menu = DBApi().getMenu(True, current_user.is_admin())
    else:
        menu = DBApi().getMenu(False, False)

    for i in menu:
        i.append('nav-link active') if i[0] == 'Главная' else i.append('nav-link')
    
    return render_template("test1.html", data=data, navigation=navigation, len=len, str=str, menu=menu)


@app.route("/test_second", methods = ['GET', 'POST'])
@login_required
def test_second():

    if stages[session['local_stages'][session['stage']][0]]['attr']['base_url'] != "test_second":
        return redirect('/prev_stage', 301)

    if request.is_json:

        button_number = request.args.get('button_number')

        for i in session['local_progress'][session['stage']].keys():
            if i == button_number:
                session['local_progress'][session['stage']][i] = True
            else:
                session['local_progress'][session['stage']][i] = False

    buttons_text = stages[session['local_stages'][session['stage']][0]]['attr']['buttons']['text'].copy()
    buttons_styles = stages[session['local_stages'][session['stage']][0]]['attr']['buttons']['styles'].copy()
    
    data = []
    next_ability = False
    for i in session['local_progress'][session['stage']].keys():
        if session['local_progress'][session['stage']][i] == True:
            buttons_styles[int(i) - 1] = f'btn btn-lg btn-success btn{i} w-100'
            next_ability = True
        else:
            buttons_styles[int(i) - 1] = f'btn btn-lg btn-outline-success btn{i} w-100'
        data.append((buttons_styles[int(i) - 1], buttons_text[int(i) - 1]))
    
    navigation = []
    navigation_text = stages[session['local_stages'][session['stage']][0]]['attr']['navigation']['text'].copy()
    navigation_styles = stages[session['local_stages'][session['stage']][0]]['attr']['navigation']['styles'].copy()
    navigation_links = stages[session['local_stages'][session['stage']][0]]['attr']['navigation']['links'].copy()

    if next_ability:
        navigation_styles[2] = 'btn btn-lg btn-success w-100 btn-next'
    else:
        navigation_styles[2] = 'btn btn-lg btn-outline-danger w-100 btn-next disabled'
    navigation.append((navigation_styles[0], navigation_text[0], navigation_links[0])) 
    navigation.append((navigation_styles[1], navigation_text[1], navigation_links[1]))
    navigation.append((navigation_styles[2], navigation_text[2], navigation_links[2]))

    if current_user.is_authenticated:
        menu = DBApi().getMenu(True, current_user.is_admin())
    else:
        menu = DBApi().getMenu(False, False)

    for i in menu:
        i.append('nav-link active') if i[0] == 'Главная' else i.append('nav-link')

    return render_template("test2.html", data=data, navigation=navigation, menu=menu)


@app.route("/test_third", methods = ['GET', 'POST'])
@login_required
def test_third():

    if stages[session['local_stages'][session['stage']][0]]['attr']['base_url'] != "test_third":
        return redirect('/prev_stage', 301)

    data, navigation = [], []

    buttons_left_text = stages[session['local_stages'][session['stage']][0]]['attr']['buttons']['left']['text'].copy()
    buttons_left_styles = stages[session['local_stages'][session['stage']][0]]['attr']['buttons']['left']['styles'].copy()
    buttons_right_text = stages[session['local_stages'][session['stage']][0]]['attr']['buttons']['right']['text'].copy()
    buttons_right_styles = stages[session['local_stages'][session['stage']][0]]['attr']['buttons']['right']['styles'].copy()

    info_text = stages[session['local_stages'][session['stage']][0]]['attr']['info']['text'].copy()
    info_styles = stages[session['local_stages'][session['stage']][0]]['attr']['info']['styles'].copy()

    navigation_text = stages[session['local_stages'][session['stage']][0]]['attr']['navigation']['text'].copy()
    navigation_styles = stages[session['local_stages'][session['stage']][0]]['attr']['navigation']['styles'].copy()
    navigation_links = stages[session['local_stages'][session['stage']][0]]['attr']['navigation']['links'].copy()

    navigation.append((navigation_styles[0], navigation_text[0], navigation_links[0]))

    button_number = None

    if request.is_json:
        button_number = request.args.get('button_number')

        session['local_changes'].append(session['local_progress'][session['stage']])
        changes = session['local_progress'][session['stage']].copy()

        if button_number == '1':
            changes[button_number] = True
            changes['2'] = False
        elif button_number == '2':
            changes[button_number] = True
            changes['1'] = False
        elif button_number == '3':
            changes[button_number] = True
            changes['4'] = False
        else:
            changes[button_number] = True
            changes['3'] = False

        session['local_changes'].append(changes)

        if changes != session['local_changes'][0]:
            session['local_flags']['flag_changes'] = True
        else:
            session['local_flags']['flag_changes'] = False

        session['local_progress'][session['stage']] = changes

    if session['local_stages'][session['stage']][0][2:] == '3':

        if  session['local_progress'][session['stage']]['1'] == True and session['local_progress'][session['stage']]['3'] == True:
            
            buttons_left_styles[0] = f'btn btn-lg btn-success btn31 w-100'
            buttons_left_styles[1] = f'btn btn-lg btn-danger btn33 w-100'
            buttons_right_styles[0] = f'btn btn-lg btn-outline-danger btn32 w-100'
            buttons_right_styles[1] = f'btn btn-lg btn-outline-success btn34 w-100'
            navigation_styles[2] = 'btn btn-lg btn-warning w-100 btn-next'
            navigation_text[2] = 'SOS. Судороги'

        elif session['local_progress'][session['stage']]['2'] == True and session['local_progress'][session['stage']]['3'] == True:
            buttons_left_styles[0] = f'btn btn-lg btn-outline-success btn31 w-100'
            buttons_left_styles[1] = f'btn btn-lg btn-danger btn33 w-100'
            buttons_right_styles[0] = f'btn btn-lg btn-danger btn32 w-100'
            buttons_right_styles[1] = f'btn btn-lg btn-outline-success btn34 w-100'
            navigation_styles[2] = 'btn btn-lg btn-danger w-100 btn-next'
            navigation_text[2] = 'SOS. Оценить дыхание!'

        elif session['local_progress'][session['stage']]['1'] == True and session['local_progress'][session['stage']]['4'] == True:
            buttons_left_styles[0] = f'btn btn-lg btn-success btn31 w-100'
            buttons_left_styles[1] = f'btn btn-lg btn-outline-danger btn33 w-100'
            buttons_right_styles[0] = f'btn btn-lg btn-outline-danger btn32 w-100'
            buttons_right_styles[1] = f'btn btn-lg btn-success btn34 w-100'
            navigation_styles[2] = 'btn btn-lg btn-success w-100 btn-next'
            navigation_text[2] = 'Далее'

        elif session['local_progress'][session['stage']]['2'] == True and session['local_progress'][session['stage']]['4'] == True:
            buttons_left_styles[0] = f'btn btn-lg btn-outline-success btn31 w-100'
            buttons_left_styles[1] = f'btn btn-lg btn-outline-danger btn33 w-100'
            buttons_right_styles[0] = f'btn btn-lg btn-danger btn32 w-100'
            buttons_right_styles[1] = f'btn btn-lg btn-success btn34 w-100'
            navigation_styles[2] = 'btn btn-lg btn-success w-100 btn-next'
            navigation_text[2] = 'Далее'

        if session['local_stages'][session['stage']][0] == 'aa3':
            if session['local_progress'][session['stage']]['1'] == True and session['local_progress'][session['stage']]['3'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'aa13'
                session['local_flags'][str(session['stage'])] = '3.1'
            elif session['local_progress'][session['stage']]['2'] == True and session['local_progress'][session['stage']]['3'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'aa13'
                session['local_flags'][str(session['stage'])] = '3.3'
            elif session['local_progress'][session['stage']]['1'] == True and session['local_progress'][session['stage']]['4'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'ja30'
                session['local_flags'][str(session['stage'])] = '3.1'
            elif session['local_progress'][session['stage']]['2'] == True and session['local_progress'][session['stage']]['4'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'aa13.1'
                session['local_flags'][str(session['stage'])] = '3.2'               

    elif session['local_stages'][session['stage']][0][2:] == '3.3':

        if  session['local_progress'][session['stage']]['1'] == True and session['local_progress'][session['stage']]['3'] == True:
            buttons_left_styles[0] = f'btn btn-lg btn-danger btn111 w-100'
            buttons_left_styles[1] = f'btn btn-lg btn-danger btn113 w-100'
            buttons_right_styles[0] = f'btn btn-lg btn-outline-success btn112 w-100'
            buttons_right_styles[1] = f'btn btn-lg btn-outline-success btn114 w-100'
            navigation_styles[2] = 'btn btn-lg btn-warning w-100 btn-next'
            navigation_text[2] = 'Далее'

        elif session['local_progress'][session['stage']]['2'] == True and session['local_progress'][session['stage']]['3'] == True:
            buttons_left_styles[0] = f'btn btn-lg btn-outline-danger btn111 w-100'
            buttons_left_styles[1] = f'btn btn-lg btn-danger btn113 w-100'
            buttons_right_styles[0] = f'btn btn-lg btn-success btn112 w-100'
            buttons_right_styles[1] = f'btn btn-lg btn-outline-success btn114 w-100'
            navigation_styles[2] = 'btn btn-lg btn-warning w-100 btn-next'
            navigation_text[2] = 'Далее'           

        elif session['local_progress'][session['stage']]['1'] == True and session['local_progress'][session['stage']]['4'] == True:
            buttons_left_styles[0] = f'btn btn-lg btn-danger btn111 w-100'
            buttons_left_styles[1] = f'btn btn-lg btn-outline-danger btn113 w-100'
            buttons_right_styles[0] = f'btn btn-lg btn-outline-success btn112 w-100'
            buttons_right_styles[1] = f'btn btn-lg btn-success btn114 w-100'
            navigation_styles[2] = 'btn btn-lg btn-warning w-100 btn-next'
            navigation_text[2] = 'Далее'

        elif session['local_progress'][session['stage']]['2'] == True and session['local_progress'][session['stage']]['4'] == True:
            buttons_left_styles[0] = f'btn btn-lg btn-outline-danger btn111 w-100'
            buttons_left_styles[1] = f'btn btn-lg btn-outline-danger btn113 w-100'
            buttons_right_styles[0] = f'btn btn-lg btn-success btn112 w-100'
            buttons_right_styles[1] = f'btn btn-lg btn-success btn114 w-100'
            navigation_styles[2] = 'btn btn-lg btn-success w-100 btn-next'
            navigation_text[2] = 'Далее'

        if session['local_stages'][session['stage']][0] == 'ga3.3':
            if  session['local_progress'][session['stage']]['1'] == True and session['local_progress'][session['stage']]['3'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'gb24.3'
            elif session['local_progress'][session['stage']]['2'] == True and session['local_progress'][session['stage']]['3'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'gb24.3'           
            elif session['local_progress'][session['stage']]['1'] == True and session['local_progress'][session['stage']]['4'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'ga24.3'
            elif session['local_progress'][session['stage']]['2'] == True and session['local_progress'][session['stage']]['4'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'ga23.3'

    elif session['local_stages'][session['stage']][0][2:] == '8.2':

        body_p = body_params()

        if body_p == None:
            return redirect('/to_beginning', 301)

        info_text[0] = f'ЧСС более {farm["css"][body_p][1]} в мин'
        info_text[1] = f'ЧСС менее {farm["css"][body_p][0]} в мин'

        if  session['local_progress'][session['stage']]['1'] == True and session['local_progress'][session['stage']]['3'] == True:
            buttons_left_styles[0] = f'btn btn-lg btn-danger btn111 w-100'
            buttons_left_styles[1] = f'btn btn-lg btn-danger btn113 w-100'
            buttons_right_styles[0] = f'btn btn-lg btn-outline-success btn112 w-100'
            buttons_right_styles[1] = f'btn btn-lg btn-outline-success btn114 w-100'
            navigation_styles[2] = 'btn btn-lg btn-warning w-100 btn-next'
            navigation_text[2] = 'Далее'

        elif session['local_progress'][session['stage']]['2'] == True and session['local_progress'][session['stage']]['3'] == True:
            buttons_left_styles[0] = f'btn btn-lg btn-outline-danger btn111 w-100'
            buttons_left_styles[1] = f'btn btn-lg btn-danger btn113 w-100'
            buttons_right_styles[0] = f'btn btn-lg btn-success btn112 w-100'
            buttons_right_styles[1] = f'btn btn-lg btn-outline-success btn114 w-100'
            navigation_styles[2] = 'btn btn-lg btn-warning w-100 btn-next'
            navigation_text[2] = 'Далее'       

        elif session['local_progress'][session['stage']]['1'] == True and session['local_progress'][session['stage']]['4'] == True:
            buttons_left_styles[0] = f'btn btn-lg btn-danger btn111 w-100'
            buttons_left_styles[1] = f'btn btn-lg btn-outline-danger btn113 w-100'
            buttons_right_styles[0] = f'btn btn-lg btn-outline-success btn112 w-100'
            buttons_right_styles[1] = f'btn btn-lg btn-success btn114 w-100'
            navigation_styles[2] = 'btn btn-lg btn-warning w-100 btn-next'
            navigation_text[2] = 'Далее'

        elif session['local_progress'][session['stage']]['2'] == True and session['local_progress'][session['stage']]['4'] == True:
            buttons_left_styles[0] = f'btn btn-lg btn-outline-danger btn111 w-100'
            buttons_left_styles[1] = f'btn btn-lg btn-outline-danger btn113 w-100'
            buttons_right_styles[0] = f'btn btn-lg btn-success btn112 w-100'
            buttons_right_styles[1] = f'btn btn-lg btn-success btn114 w-100'
            navigation_styles[2] = 'btn btn-lg btn-success w-100 btn-next'
            navigation_text[2] = 'Далее'

        if session['local_stages'][session['stage']][0] == 'ga8.2':
            if  session['local_progress'][session['stage']]['1'] == True and session['local_progress'][session['stage']]['3'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'ga7.1'
            elif session['local_progress'][session['stage']]['2'] == True and session['local_progress'][session['stage']]['3'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'ga24.3.2'           
            elif session['local_progress'][session['stage']]['1'] == True and session['local_progress'][session['stage']]['4'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'ga7.1'
            elif session['local_progress'][session['stage']]['2'] == True and session['local_progress'][session['stage']]['4'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'ga24.3.1'

        elif session['local_stages'][session['stage']][0] == 'ia8.2':
            if  session['local_progress'][session['stage']]['1'] == True and session['local_progress'][session['stage']]['3'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'ia7.1'
            elif session['local_progress'][session['stage']]['2'] == True and session['local_progress'][session['stage']]['3'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'ia24.3.2'          
            elif session['local_progress'][session['stage']]['1'] == True and session['local_progress'][session['stage']]['4'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'ia7.1'
            elif session['local_progress'][session['stage']]['2'] == True and session['local_progress'][session['stage']]['4'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'ia24.3.1'

    elif session['local_stages'][session['stage']][0][2:] == '11':

        if  session['local_progress'][session['stage']]['1'] == True and session['local_progress'][session['stage']]['3'] == True:
            buttons_left_styles[0] = f'btn btn-lg btn-danger btn111 w-100'
            buttons_left_styles[1] = f'btn btn-lg btn-danger btn113 w-100'
            buttons_right_styles[0] = f'btn btn-lg btn-outline-success btn112 w-100'
            buttons_right_styles[1] = f'btn btn-lg btn-outline-success btn114 w-100'
            navigation_styles[2] = 'btn btn-lg btn-warning w-100 btn-next'
            navigation_text[2] = 'Далее'

        elif session['local_progress'][session['stage']]['2'] == True and session['local_progress'][session['stage']]['3'] == True:
            buttons_left_styles[0] = f'btn btn-lg btn-outline-danger btn111 w-100'
            buttons_left_styles[1] = f'btn btn-lg btn-danger btn113 w-100'
            buttons_right_styles[0] = f'btn btn-lg btn-success btn112 w-100'
            buttons_right_styles[1] = f'btn btn-lg btn-outline-success btn114 w-100'
            navigation_styles[2] = 'btn btn-lg btn-warning w-100 btn-next'
            navigation_text[2] = 'Далее'

        elif session['local_progress'][session['stage']]['1'] == True and session['local_progress'][session['stage']]['4'] == True:
            buttons_left_styles[0] = f'btn btn-lg btn-danger btn111 w-100'
            buttons_left_styles[1] = f'btn btn-lg btn-outline-danger btn113 w-100'
            buttons_right_styles[0] = f'btn btn-lg btn-outline-success btn112 w-100'
            buttons_right_styles[1] = f'btn btn-lg btn-success btn114 w-100'
            navigation_styles[2] = 'btn btn-lg btn-warning w-100 btn-next'
            navigation_text[2] = 'Далее'

        elif session['local_progress'][session['stage']]['2'] == True and session['local_progress'][session['stage']]['4'] == True:
            buttons_left_styles[0] = f'btn btn-lg btn-outline-danger btn111 w-100'
            buttons_left_styles[1] = f'btn btn-lg btn-outline-danger btn113 w-100'
            buttons_right_styles[0] = f'btn btn-lg btn-success btn112 w-100'
            buttons_right_styles[1] = f'btn btn-lg btn-success btn114 w-100'
            navigation_styles[2] = 'btn btn-lg btn-success w-100 btn-next'
            navigation_text[2] = 'Далее'

        if session['local_stages'][session['stage']][0] == 'ca11':
            if  session['local_progress'][session['stage']]['1'] == True and session['local_progress'][session['stage']]['3'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'fa6'
            elif session['local_progress'][session['stage']]['2'] == True and session['local_progress'][session['stage']]['3'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'fa6'           
            elif session['local_progress'][session['stage']]['1'] == True and session['local_progress'][session['stage']]['4'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'ba3.2'
            elif session['local_progress'][session['stage']]['2'] == True and session['local_progress'][session['stage']]['4'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'cb23'

        elif session['local_stages'][session['stage']][0] == 'da11':
            if  session['local_progress'][session['stage']]['1'] == True and session['local_progress'][session['stage']]['3'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'fa6'
            elif session['local_progress'][session['stage']]['2'] == True and session['local_progress'][session['stage']]['3'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'fa6'           
            elif session['local_progress'][session['stage']]['1'] == True and session['local_progress'][session['stage']]['4'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'ba3.2'
            elif session['local_progress'][session['stage']]['2'] == True and session['local_progress'][session['stage']]['4'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'db23'

        elif session['local_stages'][session['stage']][0] == 'ea11':
            if  session['local_progress'][session['stage']]['1'] == True and session['local_progress'][session['stage']]['3'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'fa6'
            elif session['local_progress'][session['stage']]['2'] == True and session['local_progress'][session['stage']]['3'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'fa6'           
            elif session['local_progress'][session['stage']]['1'] == True and session['local_progress'][session['stage']]['4'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'ba3.2'
            elif session['local_progress'][session['stage']]['2'] == True and session['local_progress'][session['stage']]['4'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'eb23'

        elif session['local_stages'][session['stage']][0] == 'fa11':
            if  session['local_progress'][session['stage']]['1'] == True and session['local_progress'][session['stage']]['3'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'fa6'
            elif session['local_progress'][session['stage']]['2'] == True and session['local_progress'][session['stage']]['3'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'fa6'           
            elif session['local_progress'][session['stage']]['1'] == True and session['local_progress'][session['stage']]['4'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'ba3.2'
            elif session['local_progress'][session['stage']]['2'] == True and session['local_progress'][session['stage']]['4'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'fe10.1'

        elif session['local_stages'][session['stage']][0] == 'ia11':
            if  session['local_progress'][session['stage']]['1'] == True and session['local_progress'][session['stage']]['3'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'fa6'
            elif session['local_progress'][session['stage']]['2'] == True and session['local_progress'][session['stage']]['3'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'fa6'           
            elif session['local_progress'][session['stage']]['1'] == True and session['local_progress'][session['stage']]['4'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'ba3.2'
            elif session['local_progress'][session['stage']]['2'] == True and session['local_progress'][session['stage']]['4'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'ib10.1'

        elif session['local_stages'][session['stage']][0] == 'ib11':
            if  session['local_progress'][session['stage']]['1'] == True and session['local_progress'][session['stage']]['3'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'fa6'
            elif session['local_progress'][session['stage']]['2'] == True and session['local_progress'][session['stage']]['3'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'fa6'           
            elif session['local_progress'][session['stage']]['1'] == True and session['local_progress'][session['stage']]['4'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'ba3.2'
            elif session['local_progress'][session['stage']]['2'] == True and session['local_progress'][session['stage']]['4'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'id10.1'

    elif session['local_stages'][session['stage']][0][2:] == '15':

        if  session['local_progress'][session['stage']]['1'] == True and session['local_progress'][session['stage']]['3'] == True:
            buttons_left_styles[0] = f'btn btn-lg btn-success btn151 w-100'
            buttons_left_styles[1] = f'btn btn-lg btn-success btn153 w-100'
            buttons_right_styles[0] = f'btn btn-lg btn-outline-danger btn152 w-100'
            buttons_right_styles[1] = f'btn btn-lg btn-outline-danger btn154 w-100'
            navigation_styles[2] = 'btn btn-lg btn-success w-100 btn-next'
            navigation_text[2] = 'Далее'

        elif session['local_progress'][session['stage']]['2'] == True and session['local_progress'][session['stage']]['3'] == True:
            buttons_left_styles[0] = f'btn btn-lg btn-outline-success btn151 w-100'
            buttons_left_styles[1] = f'btn btn-lg btn-success btn153 w-100'
            buttons_right_styles[0] = f'btn btn-lg btn-danger btn152 w-100'
            buttons_right_styles[1] = f'btn btn-lg btn-outline-danger btn154 w-100'
            navigation_styles[2] = 'btn btn-lg btn-warning w-100 btn-next'
            navigation_text[2] = 'Далее'

        elif session['local_progress'][session['stage']]['1'] == True and session['local_progress'][session['stage']]['4'] == True:
            buttons_left_styles[0] = f'btn btn-lg btn-success btn151 w-100'
            buttons_left_styles[1] = f'btn btn-lg btn-outline-success btn153 w-100'
            buttons_right_styles[0] = f'btn btn-lg btn-outline-danger btn152 w-100'
            buttons_right_styles[1] = f'btn btn-lg btn-danger btn154 w-100'
            navigation_styles[2] = 'btn btn-lg btn-success w-100 btn-next'
            navigation_text[2] = 'Далее'

        elif session['local_progress'][session['stage']]['2'] == True and session['local_progress'][session['stage']]['4'] == True:
            buttons_left_styles[0] = f'btn btn-lg btn-outline-success btn151 w-100'
            buttons_left_styles[1] = f'btn btn-lg btn-outline-success btn153 w-100'
            buttons_right_styles[0] = f'btn btn-lg btn-danger btn152 w-100'
            buttons_right_styles[1] = f'btn btn-lg btn-danger btn154 w-100'
            navigation_styles[2] = 'btn btn-lg btn-warning w-100 btn-next'
            navigation_text[2] = 'Далее'

        if session['local_stages'][session['stage']][0] == 'ba15':
            if  session['local_progress'][session['stage']]['1'] == True and session['local_progress'][session['stage']]['3'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'fa6'
                session['local_flags']['15'] = '15.1'
            elif session['local_progress'][session['stage']]['2'] == True and session['local_progress'][session['stage']]['3'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'bb17'
                session['local_flags']['15'] = '15.3'
            elif session['local_progress'][session['stage']]['1'] == True and session['local_progress'][session['stage']]['4'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'bb16'
                session['local_flags']['15'] = '15.2'
            elif session['local_progress'][session['stage']]['2'] == True and session['local_progress'][session['stage']]['4'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'ba17'
                session['local_flags']['15'] = '15.4'

        elif session['local_stages'][session['stage']][0] == 'fa15':
            if  session['local_progress'][session['stage']]['1'] == True and session['local_progress'][session['stage']]['3'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'fb18'
                session['local_flags']['15'] = '15.1'
            elif session['local_progress'][session['stage']]['2'] == True and session['local_progress'][session['stage']]['3'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'fa14'
                session['local_flags']['15'] = '15.3'
            elif session['local_progress'][session['stage']]['1'] == True and session['local_progress'][session['stage']]['4'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'fa16'
                session['local_flags']['15'] = '15.2'
            elif session['local_progress'][session['stage']]['2'] == True and session['local_progress'][session['stage']]['4'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'fa14'
                session['local_flags']['15'] = '15.4'

        elif session['local_stages'][session['stage']][0] == 'fb15':
            if  session['local_progress'][session['stage']]['1'] == True and session['local_progress'][session['stage']]['3'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'fd18'
                session['local_flags']['15'] = '15.1'
            elif session['local_progress'][session['stage']]['2'] == True and session['local_progress'][session['stage']]['3'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'fa17'
                session['local_flags']['15'] = '15.3'
            elif session['local_progress'][session['stage']]['1'] == True and session['local_progress'][session['stage']]['4'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'fc16'
                session['local_flags']['15'] = '15.2'
            elif session['local_progress'][session['stage']]['2'] == True and session['local_progress'][session['stage']]['4'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'fb17'
                session['local_flags']['15'] = '15.4'

        elif session['local_stages'][session['stage']][0] == 'ga15':
            if  session['local_progress'][session['stage']]['1'] == True and session['local_progress'][session['stage']]['3'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'ga18'
                session['local_flags']['15'] = '15.1'
            elif session['local_progress'][session['stage']]['2'] == True and session['local_progress'][session['stage']]['3'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'gb17'
                session['local_flags']['15'] = '15.3'
            elif session['local_progress'][session['stage']]['1'] == True and session['local_progress'][session['stage']]['4'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'gb16'
                session['local_flags']['15'] = '15.2'
            elif session['local_progress'][session['stage']]['2'] == True and session['local_progress'][session['stage']]['4'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'ga17'
                session['local_flags']['15'] = '15.4'

    elif session['local_stages'][session['stage']][0][2:] == '23.1':

        if  session['local_progress'][session['stage']]['1'] == True and session['local_progress'][session['stage']]['3'] == True:
            buttons_left_styles[0] = f'btn btn-lg btn-danger btn2311 w-100'
            buttons_left_styles[1] = f'btn btn-lg btn-danger btn2313 w-100'
            buttons_right_styles[0] = f'btn btn-lg btn-outline-success btn2312 w-100'
            buttons_right_styles[1] = f'btn btn-lg btn-outline-success btn2314 w-100'
            navigation_styles[2] = 'btn btn-lg btn-success w-100 btn-next'
            navigation_text[2] = 'Далее'

        elif session['local_progress'][session['stage']]['2'] == True and session['local_progress'][session['stage']]['3'] == True:
            buttons_left_styles[0] = f'btn btn-lg btn-outline-danger btn2311 w-100'
            buttons_left_styles[1] = f'btn btn-lg btn-danger btn2313 w-100'
            buttons_right_styles[0] = f'btn btn-lg btn-success btn2312 w-100'
            buttons_right_styles[1] = f'btn btn-lg btn-outline-success btn2314 w-100'
            navigation_styles[2] = 'btn btn-lg btn-success w-100 btn-next'
            navigation_text[2] = 'Далее'

        elif session['local_progress'][session['stage']]['1'] == True and session['local_progress'][session['stage']]['4'] == True:
            buttons_left_styles[0] = f'btn btn-lg btn-danger btn2311 w-100'
            buttons_left_styles[1] = f'btn btn-lg btn-outline-danger btn2313 w-100'
            buttons_right_styles[0] = f'btn btn-lg btn-outline-success btn2312 w-100'
            buttons_right_styles[1] = f'btn btn-lg btn-success btn2314 w-100'
            navigation_styles[2] = 'btn btn-lg btn-success w-100 btn-next'
            navigation_text[2] = 'Далее'

        elif session['local_progress'][session['stage']]['2'] == True and session['local_progress'][session['stage']]['4'] == True:
            buttons_left_styles[0] = f'btn btn-lg btn-outline-danger btn2311 w-100'
            buttons_left_styles[1] = f'btn btn-lg btn-outline-danger btn2313 w-100'
            buttons_right_styles[0] = f'btn btn-lg btn-success btn2312 w-100'
            buttons_right_styles[1] = f'btn btn-lg btn-success btn2314 w-100'
            navigation_styles[2] = 'btn btn-lg btn-success w-100 btn-next'
            navigation_text[2] = 'Далее'

        if session['local_stages'][session['stage']][0] == 'fa23.1':
            if  session['local_progress'][session['stage']]['1'] == True and session['local_progress'][session['stage']]['3'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'fb13.4'
            elif session['local_progress'][session['stage']]['2'] == True and session['local_progress'][session['stage']]['3'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'fa23.2'
            elif session['local_progress'][session['stage']]['1'] == True and session['local_progress'][session['stage']]['4'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'fb13.4'
            elif session['local_progress'][session['stage']]['2'] == True and session['local_progress'][session['stage']]['4'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'fc13.4'

    navigation.append((navigation_styles[1], navigation_text[1], navigation_links[1]))
    navigation.append((navigation_styles[2], navigation_text[2], navigation_links[2]))



    for i in range(int(len(session['local_progress'][session['stage']].keys())//2)):
        data.append((info_styles[i], info_text[i], buttons_left_styles[i], buttons_left_text[i], buttons_right_styles[i], buttons_right_text[i]))

    if current_user.is_authenticated:
        menu = DBApi().getMenu(True, current_user.is_admin())
    else:
        menu = DBApi().getMenu(False, False)

    for i in menu:
        i.append('nav-link active') if i[0] == 'Главная' else i.append('nav-link')

    return render_template("test3.html", data=data, navigation=navigation, menu=menu)


@app.route("/test_fourth", methods = ['GET', 'POST'])
@login_required
def test_fourth():

    if stages[session['local_stages'][session['stage']][0]]['attr']['base_url'] != "test_fourth":
        return redirect('/prev_stage', 301)

    info, data, navigation = [], [], []

    buttons_text = stages[session['local_stages'][session['stage']][0]]['attr']['buttons']['text'].copy()
    buttons_styles = stages[session['local_stages'][session['stage']][0]]['attr']['buttons']['styles'].copy()

    info_text = stages[session['local_stages'][session['stage']][0]]['attr']['info']['text'].copy()
    info_styles = stages[session['local_stages'][session['stage']][0]]['attr']['info']['styles'].copy()

    navigation_text = stages[session['local_stages'][session['stage']][0]]['attr']['navigation']['text'].copy()
    navigation_styles = stages[session['local_stages'][session['stage']][0]]['attr']['navigation']['styles'].copy()
    navigation_links = stages[session['local_stages'][session['stage']][0]]['attr']['navigation']['links'].copy()

    navigation.append((navigation_styles[0], navigation_text[0], navigation_links[0]))

    button_number = None

    if request.is_json:
        button_number = request.args.get('button_number')

        session['local_changes'].append(session['local_progress'][session['stage']].copy())
        changes = session['local_progress'][session['stage']].copy()

        for i in changes.keys():
            if i == button_number:
                changes[i] = True
            else:
                changes[i] = False
        
        session['local_changes'].append(changes)

        if changes != session['local_changes'][0]:
            session['local_flags']['flag_changes'] = True
        else:
            session['local_flags']['flag_changes'] = False

        session['local_progress'][session['stage']] = changes

    if session['local_stages'][session['stage']][0][2:] == '3.2':

        if session['local_progress'][session['stage']]['1'] == True:
            buttons_styles[0] = f'btn btn-lg btn-danger btn3321 w-100'
            buttons_styles[1] = f'btn btn-lg btn-outline-success btn3322 w-100'
            navigation_styles[2] = 'btn btn-lg btn-danger w-100 btn-next'
            navigation_text[2] = 'SOS. Оценить дыхание!'
            session['local_flags']['3.2'] = '3.4'

        elif session['local_progress'][session['stage']]['2'] == True:
            buttons_styles[0] = f'btn btn-lg btn-outline-danger btn3321 w-100'
            buttons_styles[1] = f'btn btn-lg btn-success btn3322 w-100'
            navigation_styles[2] = 'btn btn-lg btn-success w-100 btn-next'
            navigation_text[2] = 'Далее'
            session['local_flags']['3.2'] = '3.5'

        if session['local_stages'][session['stage']][0] == 'ba3.2':
            if session['local_progress'][session['stage']]['1'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'ba4'
            elif session['local_progress'][session['stage']]['2'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'bb4'

        elif session['local_stages'][session['stage']][0] == 'fa3.2':
            if session['local_progress'][session['stage']]['1'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'fa13'
            elif session['local_progress'][session['stage']]['2'] == True:
                navigation_text[2] = 'Далее'
                session['local_stages'][session['stage']][1]['next'] = 'aa9'

        elif session['local_stages'][session['stage']][0] == 'fb3.2':
            if session['local_progress'][session['stage']]['1'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'fb13'
            elif session['local_progress'][session['stage']]['2'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'fa23'

        elif session['local_stages'][session['stage']][0] == 'ga3.2':
            if session['local_progress'][session['stage']]['1'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'ga13'
            elif session['local_progress'][session['stage']]['2'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'ga13.4'

    elif session['local_stages'][session['stage']][0][2:] == '4':

        if session['local_progress'][session['stage']]['1'] == True:
            buttons_styles[0] = f'btn btn-lg btn-success btn41 w-100'
            buttons_styles[1] = f'btn btn-lg btn-outline-warning btn42 w-100'
            buttons_styles[2] = f'btn btn-lg btn-outline-warning btn43 w-100'
            buttons_styles[3] = f'btn btn-lg btn-outline-danger btn44 w-100'
            navigation_styles[2] = 'btn btn-lg btn-success w-100 btn-next'
            navigation_text[2] = 'Далее'
            session['local_flags']['4'] = '4.1'

        elif session['local_progress'][session['stage']]['2'] == True:
            buttons_styles[0] = f'btn btn-lg btn-outline-success btn41 w-100'
            buttons_styles[1] = f'btn btn-lg btn-warning btn42 w-100'
            buttons_styles[2] = f'btn btn-lg btn-outline-warning btn43 w-100'
            buttons_styles[3] = f'btn btn-lg btn-outline-danger btn44 w-100'
            navigation_styles[2] = 'btn btn-lg btn-warning w-100 btn-next'
            navigation_text[2] = 'SOS. Обеспечение проходимости дыхательных путей'
            session['local_flags']['4'] = '4.2'

        elif session['local_progress'][session['stage']]['3'] == True:
            buttons_styles[0] = f'btn btn-lg btn-outline-success btn41 w-100'
            buttons_styles[1] = f'btn btn-lg btn-outline-warning btn42 w-100'
            buttons_styles[2] = f'btn btn-lg btn-warning btn43 w-100'
            buttons_styles[3] = f'btn btn-lg btn-outline-danger btn44 w-100'
            navigation_styles[2] = 'btn btn-lg btn-warning w-100 btn-next'
            navigation_text[2] = 'SOS. Дыхательная недостаточность'
            session['local_flags']['4'] = '4.3'

        elif session['local_progress'][session['stage']]['4'] == True:
            buttons_styles[0] = f'btn btn-lg btn-outline-success btn41 w-100'
            buttons_styles[1] = f'btn btn-lg btn-outline-warning btn42 w-100'
            buttons_styles[2] = f'btn btn-lg btn-outline-warning btn43 w-100'
            buttons_styles[3] = f'btn btn-lg btn-danger btn44 w-100'
            navigation_styles[2] = 'btn btn-lg btn-danger w-100 btn-next'
            navigation_text[2] = 'SOS. Реанимация!!!'
            session['local_flags']['4'] = '4.4'

        if session['local_stages'][session['stage']][0] == 'ba4':
            if session['local_progress'][session['stage']]['1'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'fa6'
            elif session['local_progress'][session['stage']]['2'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'ba13.2'
            elif session['local_progress'][session['stage']]['3'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'fa6'
            elif session['local_progress'][session['stage']]['4'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'ha13.2'

        elif session['local_stages'][session['stage']][0] == 'bb4':
            if session['local_progress'][session['stage']]['1'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'fa6'
            elif session['local_progress'][session['stage']]['2'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'ba13.2'
            elif session['local_progress'][session['stage']]['3'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'ca5'
            elif session['local_progress'][session['stage']]['4'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'ha13.2'

        elif session['local_stages'][session['stage']][0] == 'bc4':
            if session['local_progress'][session['stage']]['1'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'fa6'
            elif session['local_progress'][session['stage']]['2'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'ba13.2'
            elif session['local_progress'][session['stage']]['3'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'ca5'
            elif session['local_progress'][session['stage']]['4'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'ha13.2'

        elif session['local_stages'][session['stage']][0] == 'fa4':
            if session['local_progress'][session['stage']]['1'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'fd18'
            elif session['local_progress'][session['stage']]['2'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'ba13.2'
            elif session['local_progress'][session['stage']]['3'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'ca5'
            elif session['local_progress'][session['stage']]['4'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'ha13.2'

        elif session['local_stages'][session['stage']][0] == 'ga4':
            if session['local_progress'][session['stage']]['1'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'ga18'
            elif session['local_progress'][session['stage']]['2'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'ba13.2'
            elif session['local_progress'][session['stage']]['3'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'ca5'
            elif session['local_progress'][session['stage']]['4'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'ha13.2'

    elif session['local_stages'][session['stage']][0][2:] == '5':

        if session['local_progress'][session['stage']]['1'] == True:
            buttons_styles[0] = f'btn btn-lg btn-warning btn51 w-100'
            buttons_styles[1] = f'btn btn-lg btn-outline-warning btn52 w-100'
            buttons_styles[2] = f'btn btn-lg btn-outline-warning btn53 w-100'
            navigation_styles[2] = 'btn btn-lg btn-warning w-100 btn-next'
            navigation_text[2] = 'SOS. Отёк гортани'
            session['local_flags']['5'] = '5.1'

        elif session['local_progress'][session['stage']]['2'] == True:
            buttons_styles[0] = f'btn btn-lg btn-outline-warning btn51 w-100'
            buttons_styles[1] = f'btn btn-lg btn-warning btn52 w-100'
            buttons_styles[2] = f'btn btn-lg btn-outline-warning btn53 w-100'
            navigation_styles[2] = 'btn btn-lg btn-warning w-100 btn-next'
            navigation_text[2] = 'SOS. Бронхообструкция'
            session['local_flags']['5'] = '5.2'

        elif session['local_progress'][session['stage']]['3'] == True:
            buttons_styles[0] = f'btn btn-lg btn-outline-warning btn51 w-100'
            buttons_styles[1] = f'btn btn-lg btn-outline-warning btn52 w-100'
            buttons_styles[2] = f'btn btn-lg btn-warning btn53 w-100'
            navigation_styles[2] = 'btn btn-lg btn-warning w-100 btn-next'
            navigation_text[2] = 'SOS. Отёк лёгких'
            session['local_flags']['5'] = '5.3'

        if session['local_stages'][session['stage']][0] == 'ca5':
            if session['local_progress'][session['stage']]['1'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'ca23'
            elif session['local_progress'][session['stage']]['2'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'da23'
            elif session['local_progress'][session['stage']]['3'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'ea23'

    elif session['local_stages'][session['stage']][0][2:] == '6':

        if session['local_progress'][session['stage']]['1'] == True:
            buttons_styles[0] = f'btn btn-lg btn-success btn61 w-100'
            buttons_styles[1] = f'btn btn-lg btn-outline-danger btn62 w-100'
            navigation_styles[2] = 'btn btn-lg btn-success w-100 btn-next'
            navigation_text[2] = 'Далее'
            session['local_flags']['6'] = '6.1'

        elif session['local_progress'][session['stage']]['2'] == True:
            buttons_styles[0] = f'btn btn-lg btn-outline-success btn61 w-100'
            buttons_styles[1] = f'btn btn-lg btn-danger btn62 w-100'
            navigation_styles[2] = 'btn btn-lg btn-danger w-100 btn-next'
            navigation_text[2] = 'SOS. Реанимация!!!'
            session['local_flags']['6'] = '6.2'

        if session['local_stages'][session['stage']][0] == 'fa6':
            if session['local_progress'][session['stage']]['1'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'fa7'
            elif session['local_progress'][session['stage']]['2'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'ha13.2'

    elif session['local_stages'][session['stage']][0][2:] == '8':

        body_p = body_params()

        if body_p == None:
            return redirect('/to_beginning', 301)

        buttons_text[0] = f'Систолическое {farm["ads"][body_p][0]}-{farm["ads"][body_p][1]} Диастолическое {farm["add"][body_p][0]}-{farm["add"][body_p][1]} мм.рт.ст.'
        buttons_text[1] = f'Выше 180/120 мм.рт.ст.'
        buttons_text[2] = f'Ниже {farm["ads"][body_p][0]}/{farm["add"][body_p][0]} мм.рт.ст.'
        buttons_text[3] = f'Не определяется'

        if session['local_progress'][session['stage']]['1'] == True:
            buttons_styles[0] = f'btn btn-lg btn-success btn81 w-100'
            buttons_styles[1] = f'btn btn-lg btn-outline-warning btn82 w-100'
            buttons_styles[2] = f'btn btn-lg btn-outline-warning btn83 w-100'
            buttons_styles[3] = f'btn btn-lg btn-outline-danger btn84 w-100'
            navigation_styles[2] = 'btn btn-lg btn-success w-100 btn-next'
            navigation_text[2] = 'Далее'

        elif session['local_progress'][session['stage']]['2'] == True:
            buttons_styles[0] = f'btn btn-lg btn-outline-success btn81 w-100'
            buttons_styles[1] = f'btn btn-lg btn-warning btn82 w-100'
            buttons_styles[2] = f'btn btn-lg btn-outline-warning btn83 w-100'
            buttons_styles[3] = f'btn btn-lg btn-outline-danger btn84 w-100'
            navigation_styles[2] = 'btn btn-lg btn-warning w-100 btn-next'
            navigation_text[2] = 'SOS. Гипертонический криз'   

        elif session['local_progress'][session['stage']]['3'] == True:
            buttons_styles[0] = f'btn btn-lg btn-outline-success btn81 w-100'
            buttons_styles[1] = f'btn btn-lg btn-outline-warning btn82 w-100'
            buttons_styles[2] = f'btn btn-lg btn-warning btn83 w-100'
            buttons_styles[3] = f'btn btn-lg btn-outline-danger btn84 w-100'
            navigation_styles[2] = 'btn btn-lg btn-warning w-100 btn-next'
            navigation_text[2] = 'SOS. Артериальная гипотония'

        elif session['local_progress'][session['stage']]['4'] == True:
            buttons_styles[0] = f'btn btn-lg btn-outline-success btn81 w-100'
            buttons_styles[1] = f'btn btn-lg btn-outline-warning btn82 w-100'
            buttons_styles[2] = f'btn btn-lg btn-outline-warning btn83 w-100'
            buttons_styles[3] = f'btn btn-lg btn-danger btn84 w-100'
            navigation_styles[2] = 'btn btn-lg btn-danger w-100 btn-next'
            navigation_text[2] = 'SOS. Реанимация!!!'

        if session['local_stages'][session['stage']][0] == 'ca8':
            if session['local_progress'][session['stage']]['1'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'ca18'
            elif session['local_progress'][session['stage']]['2'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'fb3.2'
            elif session['local_progress'][session['stage']]['3'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'ca18'
            elif session['local_progress'][session['stage']]['4'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'ha13.2'

        elif session['local_stages'][session['stage']][0] == 'cb8':
            if session['local_progress'][session['stage']]['1'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'ca13.3'
            elif session['local_progress'][session['stage']]['2'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'fb3.2'
            elif session['local_progress'][session['stage']]['3'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'cb13.1'
            elif session['local_progress'][session['stage']]['4'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'ha13.2'

        elif session['local_stages'][session['stage']][0] == 'da8':
            if session['local_progress'][session['stage']]['1'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'da13.3'
            elif session['local_progress'][session['stage']]['2'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'fb3.2'
            elif session['local_progress'][session['stage']]['3'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'db13.1'
            elif session['local_progress'][session['stage']]['4'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'ha13.2'

        elif session['local_stages'][session['stage']][0] == 'db8':
            if session['local_progress'][session['stage']]['1'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'da18'
            elif session['local_progress'][session['stage']]['2'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'fb3.2'
            elif session['local_progress'][session['stage']]['3'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'da18'
            elif session['local_progress'][session['stage']]['4'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'ha13.2'

        elif session['local_stages'][session['stage']][0] == 'ea8':
            if session['local_progress'][session['stage']]['1'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'ea13.3'
            elif session['local_progress'][session['stage']]['2'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'ea13.3'
            elif session['local_progress'][session['stage']]['3'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'eb13.1'
            elif session['local_progress'][session['stage']]['4'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'ha13.2'

        elif session['local_stages'][session['stage']][0] == 'eb8':
            if session['local_progress'][session['stage']]['1'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'ea18'
            elif session['local_progress'][session['stage']]['2'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'ea18'
            elif session['local_progress'][session['stage']]['3'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'ga3.2'
            elif session['local_progress'][session['stage']]['4'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'ha13.2'

        elif session['local_stages'][session['stage']][0] == 'fa8':
            if session['local_progress'][session['stage']]['1'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'fa3.2'
            elif session['local_progress'][session['stage']]['2'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'fb3.2'
            elif session['local_progress'][session['stage']]['3'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'ga3.2'
            elif session['local_progress'][session['stage']]['4'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'ha13.2'

        elif session['local_stages'][session['stage']][0] == 'ga8':
            if session['local_progress'][session['stage']]['1'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'ga10.1'
            elif session['local_progress'][session['stage']]['2'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'fb3.2'
            elif session['local_progress'][session['stage']]['3'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'gb24.3.1'
            elif session['local_progress'][session['stage']]['4'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'ha13.2'

        elif session['local_stages'][session['stage']][0] == 'ia8':
            if session['local_progress'][session['stage']]['1'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'ia23.2'
            elif session['local_progress'][session['stage']]['2'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'fb3.2'
            elif session['local_progress'][session['stage']]['3'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'ia13.4'
            elif session['local_progress'][session['stage']]['4'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'ha13.2'

    elif session['local_stages'][session['stage']][0][2:] == '18.1':

        if session['local_progress'][session['stage']]['1'] == True:
            buttons_styles[0] = f'btn btn-lg btn-success btn181 w-100'
            buttons_styles[1] = f'btn btn-lg btn-outline-danger btn182 w-100'
            navigation_styles[2] = 'btn btn-lg btn-success w-100 btn-next'
            navigation_text[2] = 'Далее'

        elif session['local_progress'][session['stage']]['2'] == True:
            buttons_styles[0] = f'btn btn-lg btn-outline-success btn181 w-100'
            buttons_styles[1] = f'btn btn-lg btn-danger btn182 w-100'
            navigation_styles[2] = 'btn btn-lg btn-success w-100 btn-next'
            navigation_text[2] = 'Далее'

        if session['local_stages'][session['stage']][0] == 'fa18.1':
            if session['local_progress'][session['stage']]['1'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'fa24.8.1'
            elif session['local_progress'][session['stage']]['2'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'fa24.13'

    elif session['local_stages'][session['stage']][0][2:] == '19':

        if session['local_progress'][session['stage']]['1'] == True:
            buttons_styles[0] = f'btn btn-lg btn-success btn181 w-100'
            buttons_styles[1] = f'btn btn-lg btn-outline-danger btn182 w-100'
            navigation_styles[2] = 'btn btn-lg btn-success w-100 btn-next'
            navigation_text[2] = 'Далее'

        elif session['local_progress'][session['stage']]['2'] == True:
            buttons_styles[0] = f'btn btn-lg btn-outline-success btn181 w-100'
            buttons_styles[1] = f'btn btn-lg btn-danger btn182 w-100'
            navigation_styles[2] = 'btn btn-lg btn-success w-100 btn-next'
            navigation_text[2] = 'Далее'

        if session['local_stages'][session['stage']][0] == 'aa19':
            if session['local_progress'][session['stage']]['1'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'aa10.1'
            elif session['local_progress'][session['stage']]['2'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'aa18'

        elif session['local_stages'][session['stage']][0] == 'ab19':
            if session['local_progress'][session['stage']]['1'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'aa10.1'
            elif session['local_progress'][session['stage']]['2'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'ad20'

        elif session['local_stages'][session['stage']][0] == 'ac19':
            if session['local_progress'][session['stage']]['1'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'aa22'
            elif session['local_progress'][session['stage']]['2'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'ab20'

        elif session['local_stages'][session['stage']][0] == 'ad19':
            if session['local_progress'][session['stage']]['1'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'aa22'
            elif session['local_progress'][session['stage']]['2'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'ac20'

    elif session['local_stages'][session['stage']][0][2:] == '22':

        if session['local_progress'][session['stage']]['1'] == True:
            buttons_styles[0] = f'btn btn-lg btn-success btn181 w-100'
            buttons_styles[1] = f'btn btn-lg btn-outline-danger btn182 w-100'
            navigation_styles[2] = 'btn btn-lg btn-success w-100 btn-next'
            navigation_text[2] = 'Далее'

        elif session['local_progress'][session['stage']]['2'] == True:
            buttons_styles[0] = f'btn btn-lg btn-outline-success btn181 w-100'
            buttons_styles[1] = f'btn btn-lg btn-danger btn182 w-100'
            navigation_styles[2] = 'btn btn-lg btn-success w-100 btn-next'
            navigation_text[2] = 'Далее'

        if session['local_stages'][session['stage']][0] == 'aa22':
            if session['local_progress'][session['stage']]['1'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'ba3.2'
            elif session['local_progress'][session['stage']]['2'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'ab21'

    elif session['local_stages'][session['stage']][0][2:] == '23':

        if session['local_progress'][session['stage']]['1'] == True:
            buttons_styles[0] = f'btn btn-lg btn-success btn181 w-100'
            buttons_styles[1] = f'btn btn-lg btn-outline-danger btn182 w-100'
            navigation_styles[2] = 'btn btn-lg btn-success w-100 btn-next'
            navigation_text[2] = 'Далее'
            session['local_flags']['23'] = '23.1'

        elif session['local_progress'][session['stage']]['2'] == True:
            buttons_styles[0] = f'btn btn-lg btn-outline-success btn181 w-100'
            buttons_styles[1] = f'btn btn-lg btn-danger btn182 w-100'
            navigation_styles[2] = 'btn btn-lg btn-success w-100 btn-next'
            navigation_text[2] = 'Далее'
            session['local_flags']['23'] = '23.2'

        if session['local_stages'][session['stage']][0] == 'ca23':
            if session['local_progress'][session['stage']]['1'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'cb7'
            elif session['local_progress'][session['stage']]['2'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'ca13.1'

        elif session['local_stages'][session['stage']][0] == 'da23':
            if session['local_progress'][session['stage']]['1'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'da7'
            elif session['local_progress'][session['stage']]['2'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'da13.1'

        elif session['local_stages'][session['stage']][0] == 'ea23':
            if session['local_progress'][session['stage']]['1'] == True:   
                session['local_stages'][session['stage']][1]['next'] = 'ea7'
            elif session['local_progress'][session['stage']]['2'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'ea13.1'

        elif session['local_stages'][session['stage']][0] == 'db23':
            if session['local_progress'][session['stage']]['1'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'da10.1'
            elif session['local_progress'][session['stage']]['2'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'da9'

        elif session['local_stages'][session['stage']][0] == 'eb23':
            if session['local_progress'][session['stage']]['1'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'ea10.1'
            elif session['local_progress'][session['stage']]['2'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'ea9'

        elif session['local_stages'][session['stage']][0] == 'cb23':
            if session['local_progress'][session['stage']]['1'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'ca10.1'
            elif session['local_progress'][session['stage']]['2'] == True:  
                session['local_stages'][session['stage']][1]['next'] = 'ca9'

        elif session['local_stages'][session['stage']][0] == 'fa23':
            if session['local_progress'][session['stage']]['1'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'fa23.1'
            elif session['local_progress'][session['stage']]['2'] == True:   
                session['local_stages'][session['stage']][1]['next'] = 'fa13.4'

        elif session['local_stages'][session['stage']][0] == 'fb23':
            if session['local_progress'][session['stage']]['1'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'fa12' 
            elif session['local_progress'][session['stage']]['2'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'fa9'

        elif session['local_stages'][session['stage']][0] == 'fc23':
            if session['local_progress'][session['stage']]['1'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'fb12'
            elif session['local_progress'][session['stage']]['2'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'fb9'

        elif session['local_stages'][session['stage']][0] == 'fd23':
            if session['local_progress'][session['stage']]['1'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'fc12'
            elif session['local_progress'][session['stage']]['2'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'fc9'

        elif session['local_stages'][session['stage']][0] == 'fe23':
            if session['local_progress'][session['stage']]['1'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'fe12'
            elif session['local_progress'][session['stage']]['2'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'fd9'

        elif session['local_stages'][session['stage']][0] == 'ff23':
            if session['local_progress'][session['stage']]['1'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'ff12'
            elif session['local_progress'][session['stage']]['2'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'fe9'

        elif session['local_stages'][session['stage']][0] == 'ga23':
            if session['local_progress'][session['stage']]['1'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'ga18'
            elif session['local_progress'][session['stage']]['2'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'ga9.1'

        elif session['local_stages'][session['stage']][0] == 'gb23':
            if session['local_progress'][session['stage']]['1'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'ga12'
            elif session['local_progress'][session['stage']]['2'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'ga9'

    elif session['local_stages'][session['stage']][0][2:] == '23.2':

        if session['local_progress'][session['stage']]['1'] == True:
            buttons_styles[0] = f'btn btn-lg btn-success btn2321 w-100'
            buttons_styles[1] = f'btn btn-lg btn-outline-danger btn2322 w-100'
            navigation_styles[2] = 'btn btn-lg btn-success w-100 btn-next'
            navigation_text[2] = 'Далее'

        elif session['local_progress'][session['stage']]['2'] == True:
            buttons_styles[0] = f'btn btn-lg btn-outline-success btn2321 w-100'
            buttons_styles[1] = f'btn btn-lg btn-danger btn2322 w-100'
            navigation_styles[2] = 'btn btn-lg btn-success w-100 btn-next'
            navigation_text[2] = 'Далее'

        if session['local_stages'][session['stage']][0] == 'fa23.2':
            if session['local_progress'][session['stage']]['1'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'fa13.3'
            elif session['local_progress'][session['stage']]['2'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'fd13.4'

        elif session['local_stages'][session['stage']][0] == 'ia23.2':
            if session['local_progress'][session['stage']]['1'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'ia13.3'
            elif session['local_progress'][session['stage']]['2'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'ib13.4'

        elif session['local_stages'][session['stage']][0] == 'ib23.2':
            if session['local_progress'][session['stage']]['1'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'ib16'
            elif session['local_progress'][session['stage']]['2'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'ic24.10'

    elif session['local_stages'][session['stage']][0][2:] == '23.3':

        if session['local_progress'][session['stage']]['1'] == True:
            buttons_styles[0] = f'btn btn-lg btn-danger btn2321 w-100'
            buttons_styles[1] = f'btn btn-lg btn-outline-success btn2322 w-100'
            navigation_styles[2] = 'btn btn-lg btn-danger w-100 btn-next'
            navigation_text[2] = 'Далее'

        elif session['local_progress'][session['stage']]['2'] == True:
            buttons_styles[0] = f'btn btn-lg btn-outline-danger btn2321 w-100'
            buttons_styles[1] = f'btn btn-lg btn-success btn2322 w-100'
            navigation_styles[2] = 'btn btn-lg btn-success w-100 btn-next'
            navigation_text[2] = 'Далее'

        if session['local_stages'][session['stage']][0] == 'ga23.3':
            if session['local_progress'][session['stage']]['1'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'ia7'
            elif session['local_progress'][session['stage']]['2'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'ga8.2'

    elif session['local_stages'][session['stage']][0][2:] == '24':

        if session['local_progress'][session['stage']]['1'] == True:
            buttons_styles[0] = f'btn btn-lg btn-success btn181 w-100'
            buttons_styles[1] = f'btn btn-lg btn-outline-danger btn182 w-100'
            navigation_styles[2] = 'btn btn-lg btn-success w-100 btn-next'
            navigation_text[2] = 'Далее'
            session['local_flags']['24'] = '24.1'

        elif session['local_progress'][session['stage']]['2'] == True:
            buttons_styles[0] = f'btn btn-lg btn-outline-success btn181 w-100'
            buttons_styles[1] = f'btn btn-lg btn-danger btn182 w-100'
            navigation_styles[2] = 'btn btn-lg btn-success w-100 btn-next'
            navigation_text[2] = 'Далее' 
            session['local_flags']['24'] = '24.2'

        if session['local_stages'][session['stage']][0] == 'ca24':
            if session['local_progress'][session['stage']]['1'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'ca24.4' 
            elif session['local_progress'][session['stage']]['2'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'ca18'    

        elif session['local_stages'][session['stage']][0] == 'da24':
            if session['local_progress'][session['stage']]['1'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'da24.5' 
            elif session['local_progress'][session['stage']]['2'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'da18'    

    elif session['local_stages'][session['stage']][0][2:] == '25':

        if session['local_progress'][session['stage']]['1'] == True:
            buttons_styles[0] = f'btn btn-lg btn-success btn181 w-100'
            buttons_styles[1] = f'btn btn-lg btn-outline-danger btn182 w-100'
            navigation_styles[2] = 'btn btn-lg btn-success w-100 btn-next'
            navigation_text[2] = 'Далее'
            session['local_flags']['25'] = '25.1'

        elif session['local_progress'][session['stage']]['2'] == True:
            buttons_styles[0] = f'btn btn-lg btn-outline-success btn181 w-100'
            buttons_styles[1] = f'btn btn-lg btn-danger btn182 w-100'
            navigation_styles[2] = 'btn btn-lg btn-success w-100 btn-next'
            navigation_text[2] = 'Далее'
            session['local_flags']['25'] = '25.2'

        if session['local_stages'][session['stage']][0] == 'ca25':
            if session['local_progress'][session['stage']]['1'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'ca10'
            elif session['local_progress'][session['stage']]['2'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'ca16'

        elif session['local_stages'][session['stage']][0] == 'cb25':
            if session['local_progress'][session['stage']]['1'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'ca10'
            elif session['local_progress'][session['stage']]['2'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'cb16'

        elif session['local_stages'][session['stage']][0] == 'da25':
            if session['local_progress'][session['stage']]['1'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'da10'
            elif session['local_progress'][session['stage']]['2'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'da16'

        elif session['local_stages'][session['stage']][0] == 'db25':
            if session['local_progress'][session['stage']]['1'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'da10'
            elif session['local_progress'][session['stage']]['2'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'db16'

    elif session['local_stages'][session['stage']][0][2:] == '26.1':

        if session['local_progress'][session['stage']]['1'] == True:
            buttons_styles[0] = f'btn btn-lg btn-success btn181 w-100'
            buttons_styles[1] = f'btn btn-lg btn-outline-danger btn182 w-100'
            navigation_styles[2] = 'btn btn-lg btn-success w-100 btn-next'
            navigation_text[2] = 'Далее'

        elif session['local_progress'][session['stage']]['2'] == True:
            buttons_styles[0] = f'btn btn-lg btn-outline-success btn181 w-100'
            buttons_styles[1] = f'btn btn-lg btn-danger btn182 w-100'
            navigation_styles[2] = 'btn btn-lg btn-success w-100 btn-next'
            navigation_text[2] = 'Далее'

        if session['local_stages'][session['stage']][0] == 'fa26.1':
            if session['local_progress'][session['stage']]['1'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'fc10.1'
            elif session['local_progress'][session['stage']]['2'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'fa18.2'

        elif session['local_stages'][session['stage']][0] == 'fb26.1':
            if session['local_progress'][session['stage']]['1'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'fz10.1'
            elif session['local_progress'][session['stage']]['2'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'fa18.2'

    elif session['local_stages'][session['stage']][0][2:] == '26.2':

        if session['local_progress'][session['stage']]['1'] == True:
            buttons_styles[0] = f'btn btn-lg btn-success btn181 w-100'
            buttons_styles[1] = f'btn btn-lg btn-outline-danger btn182 w-100'
            navigation_styles[2] = 'btn btn-lg btn-success w-100 btn-next'
            navigation_text[2] = 'Далее'

        elif session['local_progress'][session['stage']]['2'] == True:
            buttons_styles[0] = f'btn btn-lg btn-outline-success btn181 w-100'
            buttons_styles[1] = f'btn btn-lg btn-danger btn182 w-100'
            navigation_styles[2] = 'btn btn-lg btn-success w-100 btn-next'
            navigation_text[2] = 'Далее'

        if session['local_stages'][session['stage']][0] == 'fa26.2':
            if session['local_progress'][session['stage']]['1'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'fa10.1'
            elif session['local_progress'][session['stage']]['2'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'fa24.9'

        elif session['local_stages'][session['stage']][0] == 'fb26.2':
            if session['local_progress'][session['stage']]['1'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'ff10.1'
            elif session['local_progress'][session['stage']]['2'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'fb24.9'

    elif session['local_stages'][session['stage']][0][2:] == '26.3':

        if session['local_progress'][session['stage']]['1'] == True:
            buttons_styles[0] = f'btn btn-lg btn-success btn181 w-100'
            buttons_styles[1] = f'btn btn-lg btn-outline-danger btn182 w-100'
            navigation_styles[2] = 'btn btn-lg btn-success w-100 btn-next'
            navigation_text[2] = 'Далее'

        elif session['local_progress'][session['stage']]['2'] == True:
            buttons_styles[0] = f'btn btn-lg btn-outline-success btn181 w-100'
            buttons_styles[1] = f'btn btn-lg btn-danger btn182 w-100'
            navigation_styles[2] = 'btn btn-lg btn-success w-100 btn-next'
            navigation_text[2] = 'Далее'

        if session['local_stages'][session['stage']][0] == 'fa26.3':
            if session['local_progress'][session['stage']]['1'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'fb10.1'
            elif session['local_progress'][session['stage']]['2'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'fa24.11'

    elif session['local_stages'][session['stage']][0][2:] == '26.4':

        body_p = body_params()

        if body_p == None:
            return redirect('/to_beginning', 301)

        info_text[0] = f'ЧСС выше {farm["css"][body_p][1]} в мин?'

        if session['local_progress'][session['stage']]['1'] == True:
            buttons_styles[0] = f'btn btn-lg btn-success btn2641 w-100'
            buttons_styles[1] = f'btn btn-lg btn-outline-success btn2642 w-100'
            navigation_styles[2] = 'btn btn-lg btn-success w-100 btn-next'
            navigation_text[2] = 'Далее'

        elif session['local_progress'][session['stage']]['2'] == True:
            buttons_styles[0] = f'btn btn-lg btn-outline-success btn2641 w-100'
            buttons_styles[1] = f'btn btn-lg btn-success btn2642 w-100'
            navigation_styles[2] = 'btn btn-lg btn-success w-100 btn-next'
            navigation_text[2] = 'Далее'

        if session['local_stages'][session['stage']][0] == 'fa26.4':
            if session['local_progress'][session['stage']]['1'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'fa24.12'
            elif session['local_progress'][session['stage']]['2'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'fa24.12.1'

    elif session['local_stages'][session['stage']][0][2:] == '26.5':

        if session['local_progress'][session['stage']]['1'] == True:
            buttons_styles[0] = f'btn btn-lg btn-success btn181 w-100'
            buttons_styles[1] = f'btn btn-lg btn-outline-danger btn182 w-100'
            navigation_styles[2] = 'btn btn-lg btn-success w-100 btn-next'
            navigation_text[2] = 'Далее'

        elif session['local_progress'][session['stage']]['2'] == True:
            buttons_styles[0] = f'btn btn-lg btn-outline-success btn181 w-100'
            buttons_styles[1] = f'btn btn-lg btn-danger btn182 w-100'
            navigation_styles[2] = 'btn btn-lg btn-success w-100 btn-next'
            navigation_text[2] = 'Далее'

        if session['local_stages'][session['stage']][0] == 'ia26.5':
            if session['local_progress'][session['stage']]['1'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'ia10.1'
            elif session['local_progress'][session['stage']]['2'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'ib18'

    elif session['local_stages'][session['stage']][0][2:] == '27.4':

        if session['local_progress'][session['stage']]['1'] == True:
            buttons_styles[0] = f'btn btn-lg btn-success btn181 w-100'
            buttons_styles[1] = f'btn btn-lg btn-outline-danger btn182 w-100'
            navigation_styles[2] = 'btn btn-lg btn-success w-100 btn-next'
            navigation_text[2] = 'Далее'

        elif session['local_progress'][session['stage']]['2'] == True:
            buttons_styles[0] = f'btn btn-lg btn-outline-success btn181 w-100'
            buttons_styles[1] = f'btn btn-lg btn-danger btn182 w-100'
            navigation_styles[2] = 'btn btn-lg btn-success w-100 btn-next'
            navigation_text[2] = 'Далее'

        if session['local_stages'][session['stage']][0] == 'ha27.4':
            if session['local_progress'][session['stage']]['1'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'ha27.6'
            elif session['local_progress'][session['stage']]['2'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'ha27.2.1'

        elif session['local_stages'][session['stage']][0] == 'hb27.4':
            if session['local_progress'][session['stage']]['1'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'hb27.6'
            elif session['local_progress'][session['stage']]['2'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'ha27.2.2'

        elif session['local_stages'][session['stage']][0] == 'hc27.4':
            if session['local_progress'][session['stage']]['1'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'ha7'
            elif session['local_progress'][session['stage']]['2'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'ha28.7'

        elif session['local_stages'][session['stage']][0] == 'hd27.4':
            if session['local_progress'][session['stage']]['1'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'hb7'
            elif session['local_progress'][session['stage']]['2'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'hc28.6'

        elif session['local_stages'][session['stage']][0] == 'he27.4':
            if session['local_progress'][session['stage']]['1'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'hb7'
            elif session['local_progress'][session['stage']]['2'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'hb27.2.2'

        elif session['local_stages'][session['stage']][0] == 'hf27.4':
            if session['local_progress'][session['stage']]['1'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'he27.6'
            elif session['local_progress'][session['stage']]['2'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'hc27.2.2'

    elif session['local_stages'][session['stage']][0][2:] == '28.1':

        if session['local_progress'][session['stage']]['1'] == True:
            buttons_styles[0] = f'btn btn-lg btn-success btn181 w-100'
            buttons_styles[1] = f'btn btn-lg btn-outline-danger btn182 w-100'
            navigation_styles[2] = 'btn btn-lg btn-success w-100 btn-next'
            navigation_text[2] = 'Далее'

        elif session['local_progress'][session['stage']]['2'] == True:
            buttons_styles[0] = f'btn btn-lg btn-outline-success btn181 w-100'
            buttons_styles[1] = f'btn btn-lg btn-danger btn182 w-100'
            navigation_styles[2] = 'btn btn-lg btn-success w-100 btn-next'
            navigation_text[2] = 'Далее'

        if session['local_stages'][session['stage']][0] == 'ha28.1':
            if session['local_progress'][session['stage']]['1'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'ha28.4'
            elif session['local_progress'][session['stage']]['2'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'ha27.2'

        if session['local_stages'][session['stage']][0] == 'hb28.1':
            if session['local_progress'][session['stage']]['1'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'hd14'
            elif session['local_progress'][session['stage']]['2'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'hb28.2'

    elif session['local_stages'][session['stage']][0][2:] == '28.2':

        if session['local_progress'][session['stage']]['1'] == True:
            buttons_styles[0] = f'btn btn-lg btn-success btn181 w-100'
            buttons_styles[1] = f'btn btn-lg btn-outline-danger btn182 w-100'
            navigation_styles[2] = 'btn btn-lg btn-success w-100 btn-next'
            navigation_text[2] = 'Далее'

        elif session['local_progress'][session['stage']]['2'] == True:
            buttons_styles[0] = f'btn btn-lg btn-outline-success btn181 w-100'
            buttons_styles[1] = f'btn btn-lg btn-danger btn182 w-100'
            navigation_styles[2] = 'btn btn-lg btn-success w-100 btn-next'
            navigation_text[2] = 'Далее'

        if session['local_stages'][session['stage']][0] == 'ha28.2':
            if session['local_progress'][session['stage']]['1'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'ha14'
            elif session['local_progress'][session['stage']]['2'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'hb27.2'

        if session['local_stages'][session['stage']][0] == 'hb28.2':
            if session['local_progress'][session['stage']]['1'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'hc14'
            elif session['local_progress'][session['stage']]['2'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'hb27.1'

    elif session['local_stages'][session['stage']][0][2:] == '29':

        if session['local_progress'][session['stage']]['1'] == True:
            buttons_styles[0] = f'btn btn-lg btn-danger btn191 w-100'
            buttons_styles[1] = f'btn btn-lg btn-outline-success btn192 w-100'
            navigation_styles[2] = 'btn btn-lg btn-success w-100 btn-next'
            navigation_text[2] = 'Далее'

        elif session['local_progress'][session['stage']]['2'] == True:
            buttons_styles[0] = f'btn btn-lg btn-outline-danger btn191 w-100'
            buttons_styles[1] = f'btn btn-lg btn-success btn192 w-100'
            navigation_styles[2] = 'btn btn-lg btn-success w-100 btn-next'
            navigation_text[2] = 'Далее'

        if session['local_stages'][session['stage']][0] == 'ja29':
            if session['local_progress'][session['stage']]['1'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'ia7'
            elif session['local_progress'][session['stage']]['2'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'ja31'

        elif session['local_stages'][session['stage']][0] == 'jb29':
            if session['local_progress'][session['stage']]['1'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'ia7'
            elif session['local_progress'][session['stage']]['2'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'ja31'

    elif session['local_stages'][session['stage']][0][2:] == '30':

        if session['local_progress'][session['stage']]['1'] == True:
            buttons_styles[0] = f'btn btn-lg btn-danger btn191 w-100'
            buttons_styles[1] = f'btn btn-lg btn-outline-success btn192 w-100'
            navigation_styles[2] = 'btn btn-lg btn-success w-100 btn-next'
            navigation_text[2] = 'Далее'

        elif session['local_progress'][session['stage']]['2'] == True:
            buttons_styles[0] = f'btn btn-lg btn-outline-danger btn191 w-100'
            buttons_styles[1] = f'btn btn-lg btn-success btn192 w-100'
            navigation_styles[2] = 'btn btn-lg btn-success w-100 btn-next'
            navigation_text[2] = 'Далее'

        if session['local_stages'][session['stage']][0] == 'ja30':
            if session['local_progress'][session['stage']]['1'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'ja29'
            elif session['local_progress'][session['stage']]['2'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'jb29'

    elif session['local_stages'][session['stage']][0][2:] == '31':

        if session['local_progress'][session['stage']]['1'] == True:
            buttons_styles[0] = f'btn btn-lg btn-danger btn191 w-100'
            buttons_styles[1] = f'btn btn-lg btn-outline-success btn192 w-100'
            navigation_styles[2] = 'btn btn-lg btn-success w-100 btn-next'
            navigation_text[2] = 'Далее'

        elif session['local_progress'][session['stage']]['2'] == True:
            buttons_styles[0] = f'btn btn-lg btn-outline-danger btn191 w-100'
            buttons_styles[1] = f'btn btn-lg btn-success btn192 w-100'
            navigation_styles[2] = 'btn btn-lg btn-success w-100 btn-next'
            navigation_text[2] = 'Далее'

        if session['local_stages'][session['stage']][0] == 'ja31':
            if session['local_progress'][session['stage']]['1'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'ja9.2'
            elif session['local_progress'][session['stage']]['2'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'ba3.2'

    elif session['local_stages'][session['stage']][0][2:] == '32':

        if session['local_progress'][session['stage']]['1'] == True:
            buttons_styles[0] = f'btn btn-lg btn-success btn181 w-100'
            buttons_styles[1] = f'btn btn-lg btn-outline-danger btn182 w-100'
            navigation_styles[2] = 'btn btn-lg btn-success w-100 btn-next'
            navigation_text[2] = 'Далее'

        elif session['local_progress'][session['stage']]['2'] == True:
            buttons_styles[0] = f'btn btn-lg btn-outline-success btn181 w-100'
            buttons_styles[1] = f'btn btn-lg btn-danger btn182 w-100'
            navigation_styles[2] = 'btn btn-lg btn-success w-100 btn-next'
            navigation_text[2] = 'Далее'

        if session['local_stages'][session['stage']][0] == 'ha32':
            if session['local_progress'][session['stage']]['1'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'ha27.1'
            elif session['local_progress'][session['stage']]['2'] == True:
                session['local_stages'][session['stage']][1]['next'] = 'hb28.1'

    info.append((info_styles[0], info_text[0]))
    for i in session['local_progress'][session['stage']].keys():
        data.append((buttons_styles[int(i) - 1], buttons_text[int(i) - 1]))
    navigation.append((navigation_styles[1], navigation_text[1], navigation_links[1]))
    navigation.append((navigation_styles[2], navigation_text[2], navigation_links[2]))

    if current_user.is_authenticated:
        menu = DBApi().getMenu(True, current_user.is_admin())
    else:
        menu = DBApi().getMenu(False, False)

    for i in menu:
        i.append('nav-link active') if i[0] == 'Главная' else i.append('nav-link')

    return render_template("test4.html", info=info, data=data, navigation=navigation, menu=menu)


def run_app():
    app.run(debug=True)


if __name__ == "__main__":
    app.run(debug=True)