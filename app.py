from flask import Flask
from flask import render_template, request, redirect, flash, session
from stages import stages, progress
from farm import farm
from stack import Stack
from dotenv import load_dotenv
from flask_login import LoginManager, login_user, login_required, logout_user, current_user, fresh_login_required
from UserLogin import UserLogin
from db_api import DBApi
import os
from datetime import timedelta

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
app.config['PERMANENT_SESSION_LIFETIME'] =  timedelta(hours=2)
login_manager = LoginManager(app)

login_manager.login_view = 'login'
login_manager.login_message = 'Необходимо авторизоваться'
login_manager.login_message_category = "alert alert-danger alert-dismissible fade show text-center"

login_manager.refresh_view = 'login'
login_manager.needs_refresh_message = 'Необходимо авторизоваться r'
login_manager.needs_refresh_message_category = "alert alert-danger alert-dismissible fade show text-center"

stage = 0
local_stages = [('aa0', stages['aa0'])]
local_progress = [{'1': False}]
local_flags = {'flag_changes': False}
local_changes = []
stk = Stack()


@login_manager.user_loader
def load_user(user_id):

    user = UserLogin().fromDB(user_id)

    return user


def progress_output():
    global local_progress, local_stages, stage
    print(f'Current stage: {stage}')
    print(f'Current flags: {local_flags}')
    print(f'Current stack: {stk.get_elems()}')
    for i in range(1, len(local_progress)):
        print(f'stage: {i}, template: {local_stages[i][0]}, Current progress {local_progress[i]}')


def body_params():
    global local_progress

    for i in local_progress[2].keys():
        if local_progress[2][i] == True:
            return i

    return None


@app.route("/registration", methods = ['GET', 'POST'])
def registration():

    if request.method == "POST":
        result = DBApi().user_registration(request.form['name'], request.form['email'], request.form['phone'], request.form['time'])
        flash(result, "alert alert-success alert-dismissible fade show text-center")

    if current_user.is_authenticated:
        menu = DBApi().getMenu(True, current_user.is_admin())
    else:
        menu = DBApi().getMenu(False, False)

    for i in menu:
        i.append('nav-link active') if i[0] == 'Регистрация' else i.append('nav-link')
         
    return render_template("registration.html", menu=menu)


@app.route("/login", methods = ['GET', 'POST'])
def login():

    if request.method == "POST":
        msg = DBApi().user_autorization(request.form['login'], request.form['password'], request.user_agent.string)

        if type(msg) != str:

            userlogin = UserLogin().create(msg)
            login_user(userlogin, remember=False, fresh=False, duration=None, force=False)
            session.permanent = True
            return redirect('/main')

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
def profile():

    if current_user.is_authenticated:
        menu = DBApi().getMenu(True, current_user.is_admin())
    else:
        menu = DBApi().getMenu(False, False)

    for i in menu:
        i.append('nav-link active') if i[0] == 'Учетная запись' else i.append('nav-link')

    return render_template('profile.html', menu=menu)


@app.route('/logout')
@login_required
def logout():

    logout_user()

    return redirect('/login')


@app.route("/main")
@app.route("/")
def main():

    global local_stages, local_progress, stage, local_flags

    stage = 0
    local_stages = [('aa0', stages['aa0'])]
    local_progress = [{'1': False}]
    local_flags = {'flag_changes': False}

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
    
    global local_stages, local_progress, stage, local_flags, local_changes

    next_atr = local_stages[stage][1].next

    if local_stages[stage][0] == 'fb13':
        stk.push('fa23')
    elif local_stages[stage][0] == 'ga13':
        stk.push('ga23')

    if next_atr == 'ba3.2' and stk.get() == 'fa23':
        next_atr = stk.pop()
    elif next_atr == 'ba3.2' and stk.get() == 'ga23':
        next_atr = stk.pop()

    if stage + 1 == len(local_progress):
        print("\n" + f'var1')
        local_stages.append((next_atr, stages[next_atr].copy()))
        local_progress.append(progress[next_atr[2:]].copy())
        stage += 1
        local_stages[stage][1].prev = local_stages[stage - 1][0]
        local_flags['flag_changes'] = False

    elif local_flags['flag_changes']:
        print("\n" + f'var2')
        local_stages = local_stages[:stage + 1]
        local_progress = local_progress[:stage + 1]
        local_stages.append((next_atr, stages[next_atr].copy()))
        local_progress.append(progress[next_atr[2:]].copy())
        stage += 1
        local_stages[stage][1].prev = local_stages[stage - 1][0]
        local_flags['flag_changes'] = False

    elif not local_flags['flag_changes'] and stage < len(local_progress):
        print("\n" + f'var3')
        stage += 1

    progress_output()

    local_changes.clear()

    if local_stages[stage][1].prev[2:] == '12':
        return redirect('/main')
    else:
        return redirect(local_stages[stage][1].attr['base_url'])


@app.route("/prev_stage")
@login_required
def prev_stage():

    global stage, local_stages, local_progress, local_flags, local_changes

    if local_stages[stage][0] == 'fa23':
        stk.push('fa23')
    elif local_stages[stage][0] == 'ga23':
        stk.push('ga23')
    if (local_stages[stage][0] == 'aa9.1' and stk.get() == 'fa23') or (local_stages[stage][0] == 'aa9.1' and stk.get() == 'ga23'):
        stk.pop()

    if local_flags['flag_changes']:
        local_stages = local_stages[:stage + 1]
        local_progress = local_progress[:stage + 1]
        local_flags['flag_changes'] = False

    if stage > 1:
        stage -= 1
    else:
        return redirect('/main')
    local_changes.clear()

    progress_output()

    return redirect(local_stages[stage][1].attr['base_url'])


@app.route("/to_beginning")
@login_required
def to_beginning():
    global local_stages, local_progress, stage, local_flags

    if body_params() != None:
        stage = 2
    else:
        stage = 1

    local_stages = local_stages[:stage + 1]
    local_progress = local_progress[:stage + 1]
    local_flags = {'flag_changes': False}

    return redirect('/next_stage')


@app.route("/test_first", methods = ['GET', 'POST'])
@login_required
def test_first():

    global local_progress, local_stages, stage, local_flags

    if local_stages[stage][1].attr['base_url'] != "test_first":
        return redirect('/prev_stage')

    if request.is_json:
        #print(request.path)
        button_number = request.args.get('button_number')
        local_progress[stage][button_number] = not local_progress[stage][button_number]

    if local_stages[stage][0] != 'aa1':
        body_p = body_params()

        if body_p == None:
            return redirect('/to_beginning')

    if local_stages[stage][0][2:] == '10.1':
        local_stages[stage][1].attr['info']['text'][1] = f'Оценивайте дыхание, пульс и SpO2 непрерывно, измеряйте АД не реже раза в 5 минут). При нарушениях дыхания, снижения SpO2 ниже 92% При АД выше {farm["ads"][body_p][1]} или ниже {farm["ads"][body_p][0]} мм.рт.ст., развитии судорог нажмите «В начало»'
    elif local_stages[stage][0][2:] == '17':
        local_stages[stage][1].attr['info']['text'][0] = f'Установите воздуховод #{farm["air_duct"][body_p]} или ларингеальную маску #{farm["i-gel"][body_p]}'
    elif local_stages[stage][0][2:] == '20':
        local_stages[stage][1].attr['info']['text'][0] = f'Поместите сахар/конфету за щёку пациента (не за зубы). При наличии доступа в вену – внутривенно {farm["glucose"][body_p]} мл 20% раствора глюкозы (ампулы 40% глюкозы развести пополам 0,9% раствором NaCl)'
    elif local_stages[stage][0][2:] == '21':
        local_stages[stage][1].attr['info']['text'][0] = f'При наличии сосудистого доступа – введите внутривенно вальпроевую кислоту (детям старше 3 лет) {farm["valpro"][body_p]} мл за 5 минут либо мидазолам {farm["midazolam"][body_p]} мл, либо диазепам {farm["diazepam"][body_p]} мл'
        local_stages[stage][1].attr['info']['text'][1] = f'При отсутствии сосудистого доступа внутримышечно ввести мидазолам {farm["midazolam"][body_p]} мл, либо диазепам {farm["diazepam"][body_p]} мл'
    elif local_stages[stage][0][2:] == '24.3':
        local_stages[stage][1].attr['info']['text'][0] = f'Введите внутривенно/внутрикостно или (при отсутствии сосудистого доступа – внутримышечно) 1. Эпинефрин (адреналин) {farm["adrenalin_v"][body_p]} мл'
        local_stages[stage][1].attr['info']['text'][1] = f'2. Дексаметазон {farm["dexamethasone"][body_p]} мл или Преднизолон {farm["prednisolone"][body_p]} мл или Метилпреднизолон {farm["methylprednisolone"][body_p]} мг или Гидрокортизон {farm["hydrocortisone"][body_p]} мл (только внутримышечно)'
    elif local_stages[stage][0][2:] == '24.3.2':
        local_stages[stage][1].attr['info']['text'][0] = f'Вводите внутривенно капельно или (при отсутствии сосудистого доступа – внутримышечно) Атропин {farm["atropin"][body_p]} мл в 10 мл (5 мл при внутримышечном введении) 0,9% раствора NaCl. Максимальное количество введений - два. Целевое ЧСС не менее {farm["css"][body_p][0]} в мин (при внутримышечном введении интервал 1 раз в 5 минут)'
    elif local_stages[stage][0][2:] == '24.3.3':
        local_stages[stage][1].attr['info']['text'][0] = f'Вводите внутривенно капельно Допамин (дофамин) 100 мг в 200 мл 5 % раствора глюкозы или 0,9 % раствора NaCl. До достижения артериального давления не менее 90/60 мм.рт.ст., ЧСС не менее {farm["css"][body_p][0]} в мин'
    elif local_stages[stage][0][2:] == '24.3.4':
        local_stages[stage][1].attr['info']['text'][0] = f'Введите внутривенно болюс интралипида 20% {farm["intralipid_b"][body_p]} мл (1,5 мл/кг) в течение 1 минуты. Немедленно начните инфузию со скоростью {farm["intralipid_k"][body_p]} кап/мин (15 мл/кг/час) (взрослому пациенту - 1 л/час, 300 капель в минуту)'
    elif local_stages[stage][0][2:] == '24.3.5':
        local_stages[stage][1].attr['info']['text'][0] = f'Введите струйно внутривенно/внутрикостно или (при отсутствии сосудистого доступа – внутримышечно под язык) Эпинефрин (адреналин) {farm["adrenalin_v"][body_p]} мл'
    elif local_stages[stage][0][2:] == '24.4':
        local_stages[stage][1].attr['info']['text'][0] = f'Введите ингаляционно через небулайзер 1. Будесонид {farm["budesonid"][body_p]} мл + NaCl 0,9% 3,0 мл'
        local_stages[stage][1].attr['info']['text'][1] = f'2. Адреналин {farm["adrenalin_n"][body_p]} мл + NaCl 0,9% 5,0 мл'
    elif local_stages[stage][0][2:] == '24.5':
        local_stages[stage][1].attr['info']['text'][0] = f'Введите ингаляционно через небулайзер 1. Сальбутамол {farm["salbutamol"][body_p]} доз'
    elif local_stages[stage][0][2:] == '24.6':
        local_stages[stage][1].attr['info']['text'][0] = f'Введите внутривенно/внутрикостно или (при отсутствии сосудистого доступа – внутримышечно) 1.Аминофиллин (эуфиллин) {farm["eufillin"][body_p]} мл'
        local_stages[stage][1].attr['info']['text'][1] = f'2. Дексаметазон {farm["dexamethasone"][body_p]} мл или Преднизолон {farm["prednisolone"][body_p]} мл или Метилпреднизолон {farm["methylprednisolone"][body_p]} мг или Гидрокортизон {farm["hydrocortisone"][body_p]} мл (только внутримышечно)'
    elif local_stages[stage][0][2:] == '24.7.1':
        local_stages[stage][1].attr['info']['text'][0] = f'Введите внутривенно или (при отсутствии сосудистого доступа – внутримышечно) Фуросемид {farm["furosemide"][body_p]} мл'
    elif local_stages[stage][0][2:] == '24.8':
        local_stages[stage][1].attr['info']['text'][0] = f'Введите внутривенно/внутрикостно Урапидил 25 мг в/в медленно, далее капельно (у пациентов старше 18 лет)'
        local_stages[stage][1].attr['info']['text'][1] = f'Сульфат магнезии 25% {farm["magnesia_sulfate"][body_p]} мл в/в медленно'
        local_stages[stage][1].attr['info']['text'][2] = f'Фуросемид {farm["furosemide"][body_p]} мл внутривенно'
    elif local_stages[stage][0][2:] == '24.8.1':
        local_stages[stage][1].attr['info']['text'][0] = f'Введите внутривенно Урапидил 25 мг в/в медленно, далее капельно (у пациентов старше 18 лет)'
        local_stages[stage][1].attr['info']['text'][1] = f'Сульфат магнезии 25% {farm["magnesia_sulfate"][body_p]} мл в/в медленно'
        local_stages[stage][1].attr['info']['text'][2] = f'Фуросемид {farm["furosemide"][body_p]} мл внутривенно'
    elif local_stages[stage][0][2:] == '24.9':
        local_stages[stage][1].attr['info']['text'][0] = f'Важно! Только при ДаД выше 120 мм.рт.ст. АД снижать на 10-15% Введите внутривенно/внутрикостно Урапидил 12, 5 мг в/в медленно, далее капельно (у пациентов старше 18 лет)'
        local_stages[stage][1].attr['info']['text'][1] = f'Сульфат магнезии 25% {farm["magnesia_sulfate"][body_p]} мл в/в медленно'
    elif local_stages[stage][0][2:] == '28.5':
        local_stages[stage][1].attr['info']['text'][0] = f'1. Присоедините к лицевой маске (размер #{farm["face_mask"][body_p]}) или установленной ларингеальной маске ( размер #{farm["i-gel"][body_p]}) дыхательный мешок'
    elif local_stages[stage][0][2:] == '28.7':
        local_stages[stage][1].attr['info']['text'][2] = f'С третьего разряда дефибрилляции введите амиодарон {farm["amiodaron"][body_p]} мг при отсутствии – лидокаин {farm["lidocaine"][body_p]} мг (пациентам старше 1 года)'

    true_count = 0
    for i in local_progress[stage].keys():
        if local_progress[stage][i] == True:
            local_stages[stage][1].attr['buttons']['text'][int(i) - 1] = 'Выполнено'
            local_stages[stage][1].attr['buttons']['styles'][int(i) - 1] = f'btn btn-lg btn-success btn{i} w-100'
            true_count += 1
        else:
            local_stages[stage][1].attr['buttons']['text'][int(i) - 1] = 'Выполнить'
            local_stages[stage][1].attr['buttons']['styles'][int(i) - 1] = f'btn btn-lg btn-outline-success btn{i} w-100'

    navigation = []

    if true_count == len(local_progress[stage].keys()):
        if local_stages[stage][0] == 'aa1':
            local_stages[stage][1].attr['navigation']['styles'][0] = 'btn btn-lg btn-success w-100 btn-next'
            navigation.append((local_stages[stage][1].attr['navigation']['styles'][0], local_stages[stage][1].attr['navigation']['text'][0], local_stages[stage][1].attr['navigation']['links'][0]))
        else: 
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-success w-100 btn-next'
            navigation.append((local_stages[stage][1].attr['navigation']['styles'][0], local_stages[stage][1].attr['navigation']['text'][0], local_stages[stage][1].attr['navigation']['links'][0]))
            navigation.append((local_stages[stage][1].attr['navigation']['styles'][1], local_stages[stage][1].attr['navigation']['text'][1], local_stages[stage][1].attr['navigation']['links'][1]))
            navigation.append((local_stages[stage][1].attr['navigation']['styles'][2], local_stages[stage][1].attr['navigation']['text'][2], local_stages[stage][1].attr['navigation']['links'][2]))
    else:
        if local_stages[stage][0] == 'aa1':
            local_stages[stage][1].attr['navigation']['styles'][0] = 'btn btn-lg btn-outline-danger w-100 btn-next disabled'
            navigation.append((local_stages[stage][1].attr['navigation']['styles'][0], local_stages[stage][1].attr['navigation']['text'][0], local_stages[stage][1].attr['navigation']['links'][0]))
        else:
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-outline-danger w-100 btn-next disabled'
            navigation.append((local_stages[stage][1].attr['navigation']['styles'][0], local_stages[stage][1].attr['navigation']['text'][0], local_stages[stage][1].attr['navigation']['links'][0]))
            navigation.append((local_stages[stage][1].attr['navigation']['styles'][1], local_stages[stage][1].attr['navigation']['text'][1], local_stages[stage][1].attr['navigation']['links'][1]))
            navigation.append((local_stages[stage][1].attr['navigation']['styles'][2], local_stages[stage][1].attr['navigation']['text'][2], local_stages[stage][1].attr['navigation']['links'][2]))

    data = []
    for i in zip(local_stages[stage][1].attr['buttons']['text'], local_stages[stage][1].attr['buttons']['styles'], local_stages[stage][1].attr['info']['text'], local_stages[stage][1].attr['info']['styles']):
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

    global local_progress, local_stages, stage

    if local_stages[stage][1].attr['base_url'] != "test_second":
        return redirect('/prev_stage')

    if request.is_json:

        #print(request.path)

        button_number = request.args.get('button_number')

        for i in local_progress[stage].keys():
            if i == button_number:
                local_progress[stage][i] = True
            else:
                local_progress[stage][i] = False
    
    data = []
    next_ability = False
    for i in local_progress[stage].keys():
        if local_progress[stage][i] == True:
            local_stages[stage][1].attr['buttons']['styles'][int(i) - 1] = f'btn btn-lg btn-success btn{i} w-100'
            next_ability = True
        else:
            local_stages[stage][1].attr['buttons']['styles'][int(i) - 1] = f'btn btn-lg btn-outline-success btn{i} w-100'
        data.append((local_stages[stage][1].attr['buttons']['styles'][int(i) - 1], local_stages[stage][1].attr['buttons']['text'][int(i) - 1]))
    
    navigation = []
    if next_ability:
        local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-success w-100 btn-next'
    else:
        local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-outline-danger w-100 btn-next disabled'
    navigation.append((local_stages[stage][1].attr['navigation']['styles'][0], local_stages[stage][1].attr['navigation']['text'][0], local_stages[stage][1].attr['navigation']['links'][0])) 
    navigation.append((local_stages[stage][1].attr['navigation']['styles'][1], local_stages[stage][1].attr['navigation']['text'][1], local_stages[stage][1].attr['navigation']['links'][1]))
    navigation.append((local_stages[stage][1].attr['navigation']['styles'][2], local_stages[stage][1].attr['navigation']['text'][2], local_stages[stage][1].attr['navigation']['links'][2]))

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

    global local_progress, local_stages, stage, local_flags, local_changes

    if local_stages[stage][1].attr['base_url'] != "test_third":
        return redirect('/prev_stage')

    data, navigation = [], []
    navigation.append((local_stages[stage][1].attr['navigation']['styles'][0], local_stages[stage][1].attr['navigation']['text'][0], local_stages[stage][1].attr['navigation']['links'][0]))

    button_number = None

    if request.is_json:
        button_number = request.args.get('button_number')

        local_changes.append(local_progress[stage].copy())
        changes = local_progress[stage].copy()
            
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

        local_changes.append(changes)

        if changes != local_changes[0]:
            local_flags['flag_changes'] = True
        else:
            local_flags['flag_changes'] = False

        local_progress[stage] = changes

    if local_stages[stage][0][2:] == '3':

        if  local_progress[stage]['1'] == True and local_progress[stage]['3'] == True:
            local_stages[stage][1].attr['buttons']['left']['styles'][0] = f'btn btn-lg btn-success btn31 w-100'
            local_stages[stage][1].attr['buttons']['left']['styles'][1] = f'btn btn-lg btn-danger btn33 w-100'
            local_stages[stage][1].attr['buttons']['right']['styles'][0] = f'btn btn-lg btn-outline-danger btn32 w-100'
            local_stages[stage][1].attr['buttons']['right']['styles'][1] = f'btn btn-lg btn-outline-success btn34 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-warning w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'SOS. Судороги'

        elif local_progress[stage]['2'] == True and local_progress[stage]['3'] == True:
            local_stages[stage][1].attr['buttons']['left']['styles'][0] = f'btn btn-lg btn-outline-success btn31 w-100'
            local_stages[stage][1].attr['buttons']['left']['styles'][1] = f'btn btn-lg btn-danger btn33 w-100'
            local_stages[stage][1].attr['buttons']['right']['styles'][0] = f'btn btn-lg btn-danger btn32 w-100'
            local_stages[stage][1].attr['buttons']['right']['styles'][1] = f'btn btn-lg btn-outline-success btn34 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-danger w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'SOS. Оценить дыхание!'

        elif local_progress[stage]['1'] == True and local_progress[stage]['4'] == True:
            local_stages[stage][1].attr['buttons']['left']['styles'][0] = f'btn btn-lg btn-success btn31 w-100'
            local_stages[stage][1].attr['buttons']['left']['styles'][1] = f'btn btn-lg btn-outline-danger btn33 w-100'
            local_stages[stage][1].attr['buttons']['right']['styles'][0] = f'btn btn-lg btn-outline-danger btn32 w-100'
            local_stages[stage][1].attr['buttons']['right']['styles'][1] = f'btn btn-lg btn-success btn34 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-success w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'Далее'

        elif local_progress[stage]['2'] == True and local_progress[stage]['4'] == True:
            local_stages[stage][1].attr['buttons']['left']['styles'][0] = f'btn btn-lg btn-outline-success btn31 w-100'
            local_stages[stage][1].attr['buttons']['left']['styles'][1] = f'btn btn-lg btn-outline-danger btn33 w-100'
            local_stages[stage][1].attr['buttons']['right']['styles'][0] = f'btn btn-lg btn-danger btn32 w-100'
            local_stages[stage][1].attr['buttons']['right']['styles'][1] = f'btn btn-lg btn-success btn34 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-success w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'Далее'

        if local_stages[stage][0] == 'aa3':
            if  local_progress[stage]['1'] == True and local_progress[stage]['3'] == True:
                local_stages[stage][1].next = 'aa13'
                local_flags[stage] = '3.1'
            elif local_progress[stage]['2'] == True and local_progress[stage]['3'] == True:
                local_stages[stage][1].next = 'aa13'
                local_flags[stage] = '3.3'
            elif local_progress[stage]['1'] == True and local_progress[stage]['4'] == True:
                local_stages[stage][1].next = 'ja30'
                local_flags[stage] = '3.1'
            elif local_progress[stage]['2'] == True and local_progress[stage]['4'] == True:
                local_stages[stage][1].next = 'aa13.1'
                local_flags[stage] = '3.2'

    elif local_stages[stage][0][2:] == '3.3':

        if  local_progress[stage]['1'] == True and local_progress[stage]['3'] == True:
            local_stages[stage][1].attr['buttons']['left']['styles'][0] = f'btn btn-lg btn-danger btn111 w-100'
            local_stages[stage][1].attr['buttons']['left']['styles'][1] = f'btn btn-lg btn-danger btn113 w-100'
            local_stages[stage][1].attr['buttons']['right']['styles'][0] = f'btn btn-lg btn-outline-success btn112 w-100'
            local_stages[stage][1].attr['buttons']['right']['styles'][1] = f'btn btn-lg btn-outline-success btn114 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-warning w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'Далее'

        elif local_progress[stage]['2'] == True and local_progress[stage]['3'] == True:
            local_stages[stage][1].attr['buttons']['left']['styles'][0] = f'btn btn-lg btn-outline-danger btn111 w-100'
            local_stages[stage][1].attr['buttons']['left']['styles'][1] = f'btn btn-lg btn-danger btn113 w-100'
            local_stages[stage][1].attr['buttons']['right']['styles'][0] = f'btn btn-lg btn-success btn112 w-100'
            local_stages[stage][1].attr['buttons']['right']['styles'][1] = f'btn btn-lg btn-outline-success btn114 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-warning w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'Далее'           

        elif local_progress[stage]['1'] == True and local_progress[stage]['4'] == True:
            local_stages[stage][1].attr['buttons']['left']['styles'][0] = f'btn btn-lg btn-danger btn111 w-100'
            local_stages[stage][1].attr['buttons']['left']['styles'][1] = f'btn btn-lg btn-outline-danger btn113 w-100'
            local_stages[stage][1].attr['buttons']['right']['styles'][0] = f'btn btn-lg btn-outline-success btn112 w-100'
            local_stages[stage][1].attr['buttons']['right']['styles'][1] = f'btn btn-lg btn-success btn114 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-warning w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'Далее'

        elif local_progress[stage]['2'] == True and local_progress[stage]['4'] == True:
            local_stages[stage][1].attr['buttons']['left']['styles'][0] = f'btn btn-lg btn-outline-danger btn111 w-100'
            local_stages[stage][1].attr['buttons']['left']['styles'][1] = f'btn btn-lg btn-outline-danger btn113 w-100'
            local_stages[stage][1].attr['buttons']['right']['styles'][0] = f'btn btn-lg btn-success btn112 w-100'
            local_stages[stage][1].attr['buttons']['right']['styles'][1] = f'btn btn-lg btn-success btn114 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-success w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'Далее'

        if local_stages[stage][0] == 'ga3.3':
            if  local_progress[stage]['1'] == True and local_progress[stage]['3'] == True:
                local_stages[stage][1].next = 'gb24.3'
            elif local_progress[stage]['2'] == True and local_progress[stage]['3'] == True:
                local_stages[stage][1].next = 'gb24.3'           
            elif local_progress[stage]['1'] == True and local_progress[stage]['4'] == True:
                local_stages[stage][1].next = 'ga24.3'
            elif local_progress[stage]['2'] == True and local_progress[stage]['4'] == True:
                local_stages[stage][1].next = 'ga23.3'

    elif local_stages[stage][0][2:] == '8.2':

        body_p = body_params()

        if body_p == None:
            return redirect('/to_beginning')

        local_stages[stage][1].attr['info']['text'][0] = f'ЧСС более {farm["css"][body_p][1]} в мин'
        local_stages[stage][1].attr['info']['text'][1] = f'ЧСС менее {farm["css"][body_p][0]} в мин'

        if  local_progress[stage]['1'] == True and local_progress[stage]['3'] == True:
            local_stages[stage][1].attr['buttons']['left']['styles'][0] = f'btn btn-lg btn-danger btn111 w-100'
            local_stages[stage][1].attr['buttons']['left']['styles'][1] = f'btn btn-lg btn-danger btn113 w-100'
            local_stages[stage][1].attr['buttons']['right']['styles'][0] = f'btn btn-lg btn-outline-success btn112 w-100'
            local_stages[stage][1].attr['buttons']['right']['styles'][1] = f'btn btn-lg btn-outline-success btn114 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-warning w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'Далее'

        elif local_progress[stage]['2'] == True and local_progress[stage]['3'] == True:
            local_stages[stage][1].attr['buttons']['left']['styles'][0] = f'btn btn-lg btn-outline-danger btn111 w-100'
            local_stages[stage][1].attr['buttons']['left']['styles'][1] = f'btn btn-lg btn-danger btn113 w-100'
            local_stages[stage][1].attr['buttons']['right']['styles'][0] = f'btn btn-lg btn-success btn112 w-100'
            local_stages[stage][1].attr['buttons']['right']['styles'][1] = f'btn btn-lg btn-outline-success btn114 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-warning w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'Далее'       

        elif local_progress[stage]['1'] == True and local_progress[stage]['4'] == True:
            local_stages[stage][1].attr['buttons']['left']['styles'][0] = f'btn btn-lg btn-danger btn111 w-100'
            local_stages[stage][1].attr['buttons']['left']['styles'][1] = f'btn btn-lg btn-outline-danger btn113 w-100'
            local_stages[stage][1].attr['buttons']['right']['styles'][0] = f'btn btn-lg btn-outline-success btn112 w-100'
            local_stages[stage][1].attr['buttons']['right']['styles'][1] = f'btn btn-lg btn-success btn114 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-warning w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'Далее'

        elif local_progress[stage]['2'] == True and local_progress[stage]['4'] == True:
            local_stages[stage][1].attr['buttons']['left']['styles'][0] = f'btn btn-lg btn-outline-danger btn111 w-100'
            local_stages[stage][1].attr['buttons']['left']['styles'][1] = f'btn btn-lg btn-outline-danger btn113 w-100'
            local_stages[stage][1].attr['buttons']['right']['styles'][0] = f'btn btn-lg btn-success btn112 w-100'
            local_stages[stage][1].attr['buttons']['right']['styles'][1] = f'btn btn-lg btn-success btn114 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-success w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'Далее'

        if local_stages[stage][0] == 'ga8.2':
            if  local_progress[stage]['1'] == True and local_progress[stage]['3'] == True:
                local_stages[stage][1].next = 'ga7.1'
            elif local_progress[stage]['2'] == True and local_progress[stage]['3'] == True:
                local_stages[stage][1].next = 'ga24.3.2'           
            elif local_progress[stage]['1'] == True and local_progress[stage]['4'] == True:
                local_stages[stage][1].next = 'ga7.1'
            elif local_progress[stage]['2'] == True and local_progress[stage]['4'] == True:
                local_stages[stage][1].next = 'ga24.3.1'

        elif local_stages[stage][0] == 'ia8.2':
            if  local_progress[stage]['1'] == True and local_progress[stage]['3'] == True:
                local_stages[stage][1].next = 'ia7.1'
            elif local_progress[stage]['2'] == True and local_progress[stage]['3'] == True:
                local_stages[stage][1].next = 'ia24.3.2'          
            elif local_progress[stage]['1'] == True and local_progress[stage]['4'] == True:
                local_stages[stage][1].next = 'ia7.1'
            elif local_progress[stage]['2'] == True and local_progress[stage]['4'] == True:
                local_stages[stage][1].next = 'ia24.3.1'

    elif local_stages[stage][0][2:] == '11':

        if  local_progress[stage]['1'] == True and local_progress[stage]['3'] == True:
            local_stages[stage][1].attr['buttons']['left']['styles'][0] = f'btn btn-lg btn-danger btn111 w-100'
            local_stages[stage][1].attr['buttons']['left']['styles'][1] = f'btn btn-lg btn-danger btn113 w-100'
            local_stages[stage][1].attr['buttons']['right']['styles'][0] = f'btn btn-lg btn-outline-success btn112 w-100'
            local_stages[stage][1].attr['buttons']['right']['styles'][1] = f'btn btn-lg btn-outline-success btn114 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-warning w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'Далее'

        elif local_progress[stage]['2'] == True and local_progress[stage]['3'] == True:
            local_stages[stage][1].attr['buttons']['left']['styles'][0] = f'btn btn-lg btn-outline-danger btn111 w-100'
            local_stages[stage][1].attr['buttons']['left']['styles'][1] = f'btn btn-lg btn-danger btn113 w-100'
            local_stages[stage][1].attr['buttons']['right']['styles'][0] = f'btn btn-lg btn-success btn112 w-100'
            local_stages[stage][1].attr['buttons']['right']['styles'][1] = f'btn btn-lg btn-outline-success btn114 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-warning w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'Далее'

        elif local_progress[stage]['1'] == True and local_progress[stage]['4'] == True:
            local_stages[stage][1].attr['buttons']['left']['styles'][0] = f'btn btn-lg btn-danger btn111 w-100'
            local_stages[stage][1].attr['buttons']['left']['styles'][1] = f'btn btn-lg btn-outline-danger btn113 w-100'
            local_stages[stage][1].attr['buttons']['right']['styles'][0] = f'btn btn-lg btn-outline-success btn112 w-100'
            local_stages[stage][1].attr['buttons']['right']['styles'][1] = f'btn btn-lg btn-success btn114 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-warning w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'Далее'

        elif local_progress[stage]['2'] == True and local_progress[stage]['4'] == True:
            local_stages[stage][1].attr['buttons']['left']['styles'][0] = f'btn btn-lg btn-outline-danger btn111 w-100'
            local_stages[stage][1].attr['buttons']['left']['styles'][1] = f'btn btn-lg btn-outline-danger btn113 w-100'
            local_stages[stage][1].attr['buttons']['right']['styles'][0] = f'btn btn-lg btn-success btn112 w-100'
            local_stages[stage][1].attr['buttons']['right']['styles'][1] = f'btn btn-lg btn-success btn114 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-success w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'Далее'

        if local_stages[stage][0] == 'ca11':
            if  local_progress[stage]['1'] == True and local_progress[stage]['3'] == True:
                local_stages[stage][1].next = 'fa6'
            elif local_progress[stage]['2'] == True and local_progress[stage]['3'] == True:
                local_stages[stage][1].next = 'fa6'           
            elif local_progress[stage]['1'] == True and local_progress[stage]['4'] == True:
                local_stages[stage][1].next = 'ba3.2'
            elif local_progress[stage]['2'] == True and local_progress[stage]['4'] == True:
                local_stages[stage][1].next = 'cb23'

        elif local_stages[stage][0] == 'da11':
            if  local_progress[stage]['1'] == True and local_progress[stage]['3'] == True:
                local_stages[stage][1].next = 'fa6'
            elif local_progress[stage]['2'] == True and local_progress[stage]['3'] == True:
                local_stages[stage][1].next = 'fa6'           
            elif local_progress[stage]['1'] == True and local_progress[stage]['4'] == True:
                local_stages[stage][1].next = 'ba3.2'
            elif local_progress[stage]['2'] == True and local_progress[stage]['4'] == True:
                local_stages[stage][1].next = 'db23'

        elif local_stages[stage][0] == 'ea11':
            if  local_progress[stage]['1'] == True and local_progress[stage]['3'] == True:
                local_stages[stage][1].next = 'fa6'
            elif local_progress[stage]['2'] == True and local_progress[stage]['3'] == True:
                local_stages[stage][1].next = 'fa6'           
            elif local_progress[stage]['1'] == True and local_progress[stage]['4'] == True:
                local_stages[stage][1].next = 'ba3.2'
            elif local_progress[stage]['2'] == True and local_progress[stage]['4'] == True:
                local_stages[stage][1].next = 'eb23'

        elif local_stages[stage][0] == 'fa11':
            if  local_progress[stage]['1'] == True and local_progress[stage]['3'] == True:
                local_stages[stage][1].next = 'fa6'
            elif local_progress[stage]['2'] == True and local_progress[stage]['3'] == True:
                local_stages[stage][1].next = 'fa6'           
            elif local_progress[stage]['1'] == True and local_progress[stage]['4'] == True:
                local_stages[stage][1].next = 'ba3.2'
            elif local_progress[stage]['2'] == True and local_progress[stage]['4'] == True:
                local_stages[stage][1].next = 'fe10.1'

        elif local_stages[stage][0] == 'ia11':
            if  local_progress[stage]['1'] == True and local_progress[stage]['3'] == True:
                local_stages[stage][1].next = 'fa6'
            elif local_progress[stage]['2'] == True and local_progress[stage]['3'] == True:
                local_stages[stage][1].next = 'fa6'           
            elif local_progress[stage]['1'] == True and local_progress[stage]['4'] == True:
                local_stages[stage][1].next = 'ba3.2'
            elif local_progress[stage]['2'] == True and local_progress[stage]['4'] == True:
                local_stages[stage][1].next = 'ib10.1'

        elif local_stages[stage][0] == 'ib11':
            if  local_progress[stage]['1'] == True and local_progress[stage]['3'] == True:
                local_stages[stage][1].next = 'fa6'
            elif local_progress[stage]['2'] == True and local_progress[stage]['3'] == True:
                local_stages[stage][1].next = 'fa6'           
            elif local_progress[stage]['1'] == True and local_progress[stage]['4'] == True:
                local_stages[stage][1].next = 'ba3.2'
            elif local_progress[stage]['2'] == True and local_progress[stage]['4'] == True:
                local_stages[stage][1].next = 'id10.1'

    elif local_stages[stage][0][2:] == '15':

        if  local_progress[stage]['1'] == True and local_progress[stage]['3'] == True:
            local_stages[stage][1].attr['buttons']['left']['styles'][0] = f'btn btn-lg btn-success btn151 w-100'
            local_stages[stage][1].attr['buttons']['left']['styles'][1] = f'btn btn-lg btn-success btn153 w-100'
            local_stages[stage][1].attr['buttons']['right']['styles'][0] = f'btn btn-lg btn-outline-danger btn152 w-100'
            local_stages[stage][1].attr['buttons']['right']['styles'][1] = f'btn btn-lg btn-outline-danger btn154 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-success w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'Далее'

        elif local_progress[stage]['2'] == True and local_progress[stage]['3'] == True:
            local_stages[stage][1].attr['buttons']['left']['styles'][0] = f'btn btn-lg btn-outline-success btn151 w-100'
            local_stages[stage][1].attr['buttons']['left']['styles'][1] = f'btn btn-lg btn-success btn153 w-100'
            local_stages[stage][1].attr['buttons']['right']['styles'][0] = f'btn btn-lg btn-danger btn152 w-100'
            local_stages[stage][1].attr['buttons']['right']['styles'][1] = f'btn btn-lg btn-outline-danger btn154 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-warning w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'Далее'

        elif local_progress[stage]['1'] == True and local_progress[stage]['4'] == True:
            local_stages[stage][1].attr['buttons']['left']['styles'][0] = f'btn btn-lg btn-success btn151 w-100'
            local_stages[stage][1].attr['buttons']['left']['styles'][1] = f'btn btn-lg btn-outline-success btn153 w-100'
            local_stages[stage][1].attr['buttons']['right']['styles'][0] = f'btn btn-lg btn-outline-danger btn152 w-100'
            local_stages[stage][1].attr['buttons']['right']['styles'][1] = f'btn btn-lg btn-danger btn154 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-success w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'Далее'

        elif local_progress[stage]['2'] == True and local_progress[stage]['4'] == True:
            local_stages[stage][1].attr['buttons']['left']['styles'][0] = f'btn btn-lg btn-outline-success btn151 w-100'
            local_stages[stage][1].attr['buttons']['left']['styles'][1] = f'btn btn-lg btn-outline-success btn153 w-100'
            local_stages[stage][1].attr['buttons']['right']['styles'][0] = f'btn btn-lg btn-danger btn152 w-100'
            local_stages[stage][1].attr['buttons']['right']['styles'][1] = f'btn btn-lg btn-danger btn154 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-warning w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'Далее'

        if local_stages[stage][0] == 'ba15':
            if  local_progress[stage]['1'] == True and local_progress[stage]['3'] == True:
                local_stages[stage][1].next = 'fa6'
                local_flags[15] = '15.1'
            elif local_progress[stage]['2'] == True and local_progress[stage]['3'] == True:
                local_stages[stage][1].next = 'bb17'
                local_flags[15] = '15.3'
            elif local_progress[stage]['1'] == True and local_progress[stage]['4'] == True:
                local_stages[stage][1].next = 'bb16'
                local_flags[15] = '15.2'
            elif local_progress[stage]['2'] == True and local_progress[stage]['4'] == True:
                local_stages[stage][1].next = 'ba17'
                local_flags[15] = '15.4'

        elif local_stages[stage][0] == 'fa15':
            if  local_progress[stage]['1'] == True and local_progress[stage]['3'] == True:
                local_stages[stage][1].next = 'fb18'
                local_flags[15] = '15.1'
            elif local_progress[stage]['2'] == True and local_progress[stage]['3'] == True:
                local_stages[stage][1].next = 'fa14'
                local_flags[15] = '15.3'
            elif local_progress[stage]['1'] == True and local_progress[stage]['4'] == True:
                local_stages[stage][1].next = 'fa16'
                local_flags[15] = '15.2'
            elif local_progress[stage]['2'] == True and local_progress[stage]['4'] == True:
                local_stages[stage][1].next = 'fa14'
                local_flags[15] = '15.4'

        elif local_stages[stage][0] == 'fb15':
            if  local_progress[stage]['1'] == True and local_progress[stage]['3'] == True:
                local_stages[stage][1].next = 'fd18'
                local_flags[15] = '15.1'
            elif local_progress[stage]['2'] == True and local_progress[stage]['3'] == True:
                local_stages[stage][1].next = 'fa17'
                local_flags[15] = '15.3'
            elif local_progress[stage]['1'] == True and local_progress[stage]['4'] == True:
                local_stages[stage][1].next = 'fc16'
                local_flags[15] = '15.2'
            elif local_progress[stage]['2'] == True and local_progress[stage]['4'] == True:
                local_stages[stage][1].next = 'fb17'
                local_flags[15] = '15.4'

        elif local_stages[stage][0] == 'ga15':
            if  local_progress[stage]['1'] == True and local_progress[stage]['3'] == True:
                local_stages[stage][1].next = 'ga18'
                local_flags[15] = '15.1'
            elif local_progress[stage]['2'] == True and local_progress[stage]['3'] == True:
                local_stages[stage][1].next = 'gb17'
                local_flags[15] = '15.3'
            elif local_progress[stage]['1'] == True and local_progress[stage]['4'] == True:
                local_stages[stage][1].next = 'gb16'
                local_flags[15] = '15.2'
            elif local_progress[stage]['2'] == True and local_progress[stage]['4'] == True:
                local_stages[stage][1].next = 'ga17'
                local_flags[15] = '15.4'

    elif local_stages[stage][0][2:] == '23.1':

        if  local_progress[stage]['1'] == True and local_progress[stage]['3'] == True:
            local_stages[stage][1].attr['buttons']['left']['styles'][0] = f'btn btn-lg btn-danger btn2311 w-100'
            local_stages[stage][1].attr['buttons']['left']['styles'][1] = f'btn btn-lg btn-danger btn2313 w-100'
            local_stages[stage][1].attr['buttons']['right']['styles'][0] = f'btn btn-lg btn-outline-success btn2312 w-100'
            local_stages[stage][1].attr['buttons']['right']['styles'][1] = f'btn btn-lg btn-outline-success btn2314 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-success w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'Далее'

        elif local_progress[stage]['2'] == True and local_progress[stage]['3'] == True:
            local_stages[stage][1].attr['buttons']['left']['styles'][0] = f'btn btn-lg btn-outline-danger btn2311 w-100'
            local_stages[stage][1].attr['buttons']['left']['styles'][1] = f'btn btn-lg btn-danger btn2313 w-100'
            local_stages[stage][1].attr['buttons']['right']['styles'][0] = f'btn btn-lg btn-success btn2312 w-100'
            local_stages[stage][1].attr['buttons']['right']['styles'][1] = f'btn btn-lg btn-outline-success btn2314 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-success w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'Далее'

        elif local_progress[stage]['1'] == True and local_progress[stage]['4'] == True:
            local_stages[stage][1].attr['buttons']['left']['styles'][0] = f'btn btn-lg btn-danger btn2311 w-100'
            local_stages[stage][1].attr['buttons']['left']['styles'][1] = f'btn btn-lg btn-outline-danger btn2313 w-100'
            local_stages[stage][1].attr['buttons']['right']['styles'][0] = f'btn btn-lg btn-outline-success btn2312 w-100'
            local_stages[stage][1].attr['buttons']['right']['styles'][1] = f'btn btn-lg btn-success btn2314 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-success w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'Далее'

        elif local_progress[stage]['2'] == True and local_progress[stage]['4'] == True:
            local_stages[stage][1].attr['buttons']['left']['styles'][0] = f'btn btn-lg btn-outline-danger btn2311 w-100'
            local_stages[stage][1].attr['buttons']['left']['styles'][1] = f'btn btn-lg btn-outline-danger btn2313 w-100'
            local_stages[stage][1].attr['buttons']['right']['styles'][0] = f'btn btn-lg btn-success btn2312 w-100'
            local_stages[stage][1].attr['buttons']['right']['styles'][1] = f'btn btn-lg btn-success btn2314 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-success w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'Далее'

        if local_stages[stage][0] == 'fa23.1':
            if  local_progress[stage]['1'] == True and local_progress[stage]['3'] == True:
                local_stages[stage][1].next = 'fb13.4'
            elif local_progress[stage]['2'] == True and local_progress[stage]['3'] == True:
                local_stages[stage][1].next = 'fa23.2'
            elif local_progress[stage]['1'] == True and local_progress[stage]['4'] == True:
                local_stages[stage][1].next = 'fb13.4'
            elif local_progress[stage]['2'] == True and local_progress[stage]['4'] == True:
                local_stages[stage][1].next = 'fc13.4'

    navigation.append((local_stages[stage][1].attr['navigation']['styles'][1], local_stages[stage][1].attr['navigation']['text'][1], local_stages[stage][1].attr['navigation']['links'][1]))
    navigation.append((local_stages[stage][1].attr['navigation']['styles'][2], local_stages[stage][1].attr['navigation']['text'][2], local_stages[stage][1].attr['navigation']['links'][2]))

    for i in range(int(len(local_progress[stage].keys())//2)):
        data.append((local_stages[stage][1].attr['info']['styles'][i], local_stages[stage][1].attr['info']['text'][i], local_stages[stage][1].attr['buttons']['left']['styles'][i], local_stages[stage][1].attr['buttons']['left']['text'][i], local_stages[stage][1].attr['buttons']['right']['styles'][i], local_stages[stage][1].attr['buttons']['right']['text'][i]))

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

    global local_progress, local_stages, stage, local_flags

    if local_stages[stage][1].attr['base_url'] != "test_fourth":
        return redirect('/prev_stage')

    info, data, navigation = [], [], []
    navigation.append((local_stages[stage][1].attr['navigation']['styles'][0], local_stages[stage][1].attr['navigation']['text'][0], local_stages[stage][1].attr['navigation']['links'][0]))

    button_number = None

    if request.is_json:
        button_number = request.args.get('button_number')

        local_changes.append(local_progress[stage].copy())
        changes = local_progress[stage].copy()

        for i in changes.keys():
            if i == button_number:
                changes[i] = True
            else:
                changes[i] = False
        
        local_changes.append(changes)

        if changes != local_changes[0]:
            local_flags['flag_changes'] = True
        else:
            local_flags['flag_changes'] = False

        local_progress[stage] = changes

    if local_stages[stage][0][2:] == '3.2':

        if local_progress[stage]['1'] == True:
            local_stages[stage][1].attr['buttons']['styles'][0] = f'btn btn-lg btn-danger btn3321 w-100'
            local_stages[stage][1].attr['buttons']['styles'][1] = f'btn btn-lg btn-outline-success btn3322 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-danger w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'SOS. Оценить дыхание!'
            local_flags[3.2] = '3.4'
   
        elif local_progress[stage]['2'] == True:
            local_stages[stage][1].attr['buttons']['styles'][0] = f'btn btn-lg btn-outline-danger btn3321 w-100'
            local_stages[stage][1].attr['buttons']['styles'][1] = f'btn btn-lg btn-success btn3322 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-success w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'Далее'
            local_flags[3.2] = '3.5'

        if local_stages[stage][0] == 'ba3.2':
            if local_progress[stage]['1'] == True:
                local_stages[stage][1].next = 'ba4'
            elif local_progress[stage]['2'] == True:
                local_stages[stage][1].next = 'bb4'

        elif local_stages[stage][0] == 'fa3.2':
            if local_progress[stage]['1'] == True:
                local_stages[stage][1].next = 'fa13'
            elif local_progress[stage]['2'] == True:
                local_stages[stage][1].attr['navigation']['text'][2] = 'Далее'
                local_stages[stage][1].next = 'aa9'

        elif local_stages[stage][0] == 'fb3.2':
            if local_progress[stage]['1'] == True:
                local_stages[stage][1].next = 'fb13'
            elif local_progress[stage]['2'] == True:
                local_stages[stage][1].next = 'fa23'

        elif local_stages[stage][0] == 'ga3.2':
            if local_progress[stage]['1'] == True:
                local_stages[stage][1].next = 'ga13'
            elif local_progress[stage]['2'] == True:
                local_stages[stage][1].next = 'ga13.4'

    elif local_stages[stage][0][2:] == '4':

        if local_progress[stage]['1'] == True:
            local_stages[stage][1].attr['buttons']['styles'][0] = f'btn btn-lg btn-success btn41 w-100'
            local_stages[stage][1].attr['buttons']['styles'][1] = f'btn btn-lg btn-outline-warning btn42 w-100'
            local_stages[stage][1].attr['buttons']['styles'][2] = f'btn btn-lg btn-outline-warning btn43 w-100'
            local_stages[stage][1].attr['buttons']['styles'][3] = f'btn btn-lg btn-outline-danger btn44 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-success w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'Далее'
            local_flags[4] = '4.1'
   
        elif local_progress[stage]['2'] == True:
            local_stages[stage][1].attr['buttons']['styles'][0] = f'btn btn-lg btn-outline-success btn41 w-100'
            local_stages[stage][1].attr['buttons']['styles'][1] = f'btn btn-lg btn-warning btn42 w-100'
            local_stages[stage][1].attr['buttons']['styles'][2] = f'btn btn-lg btn-outline-warning btn43 w-100'
            local_stages[stage][1].attr['buttons']['styles'][3] = f'btn btn-lg btn-outline-danger btn44 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-warning w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'SOS. Обеспечение проходимости дыхательных путей'
            local_flags[4] = '4.2'

        elif local_progress[stage]['3'] == True:
            local_stages[stage][1].attr['buttons']['styles'][0] = f'btn btn-lg btn-outline-success btn41 w-100'
            local_stages[stage][1].attr['buttons']['styles'][1] = f'btn btn-lg btn-outline-warning btn42 w-100'
            local_stages[stage][1].attr['buttons']['styles'][2] = f'btn btn-lg btn-warning btn43 w-100'
            local_stages[stage][1].attr['buttons']['styles'][3] = f'btn btn-lg btn-outline-danger btn44 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-warning w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'SOS. Дыхательная недостаточность'
            local_flags[4] = '4.3'

        elif local_progress[stage]['4'] == True:
            local_stages[stage][1].attr['buttons']['styles'][0] = f'btn btn-lg btn-outline-success btn41 w-100'
            local_stages[stage][1].attr['buttons']['styles'][1] = f'btn btn-lg btn-outline-warning btn42 w-100'
            local_stages[stage][1].attr['buttons']['styles'][2] = f'btn btn-lg btn-outline-warning btn43 w-100'
            local_stages[stage][1].attr['buttons']['styles'][3] = f'btn btn-lg btn-danger btn44 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-danger w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'SOS. Реанимация!!!'
            local_flags[4] = '4.4'

        if local_stages[stage][0] == 'ba4':
            if local_progress[stage]['1'] == True:
                local_stages[stage][1].next = 'fa6'
            elif local_progress[stage]['2'] == True:
                local_stages[stage][1].next = 'ba13.2'
            elif local_progress[stage]['3'] == True:
                local_stages[stage][1].next = 'fa6'
            elif local_progress[stage]['4'] == True:
                local_stages[stage][1].next = 'ha13.2'

        elif local_stages[stage][0] == 'bb4':
            if local_progress[stage]['1'] == True:
                local_stages[stage][1].next = 'fa6'
            elif local_progress[stage]['2'] == True:
                local_stages[stage][1].next = 'ba13.2'
            elif local_progress[stage]['3'] == True:
                local_stages[stage][1].next = 'ca5'
            elif local_progress[stage]['4'] == True:
                local_stages[stage][1].next = 'ha13.2'

        elif local_stages[stage][0] == 'bc4':
            if local_progress[stage]['1'] == True:
                local_stages[stage][1].next = 'fa6'
            elif local_progress[stage]['2'] == True:
                local_stages[stage][1].next = 'ba13.2'
            elif local_progress[stage]['3'] == True:
                local_stages[stage][1].next = 'ca5'
            elif local_progress[stage]['4'] == True:
                local_stages[stage][1].next = 'ha13.2'

        elif local_stages[stage][0] == 'fa4':
            if local_progress[stage]['1'] == True:
                local_stages[stage][1].next = 'fd18'
            elif local_progress[stage]['2'] == True:
                local_stages[stage][1].next = 'ba13.2'
            elif local_progress[stage]['3'] == True:
                local_stages[stage][1].next = 'ca5'
            elif local_progress[stage]['4'] == True:
                local_stages[stage][1].next = 'ha13.2'

        elif local_stages[stage][0] == 'ga4':
            if local_progress[stage]['1'] == True:
                local_stages[stage][1].next = 'ga18'
            elif local_progress[stage]['2'] == True:
                local_stages[stage][1].next = 'ba13.2'
            elif local_progress[stage]['3'] == True:
                local_stages[stage][1].next = 'ca5'
            elif local_progress[stage]['4'] == True:
                local_stages[stage][1].next = 'ha13.2'

    elif local_stages[stage][0][2:] == '5':

        if local_progress[stage]['1'] == True:
            local_stages[stage][1].attr['buttons']['styles'][0] = f'btn btn-lg btn-warning btn51 w-100'
            local_stages[stage][1].attr['buttons']['styles'][1] = f'btn btn-lg btn-outline-warning btn52 w-100'
            local_stages[stage][1].attr['buttons']['styles'][2] = f'btn btn-lg btn-outline-warning btn53 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-warning w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'SOS. Отёк гортани'
            local_flags[5] = '5.1'
   
        elif local_progress[stage]['2'] == True:
            local_stages[stage][1].attr['buttons']['styles'][0] = f'btn btn-lg btn-outline-warning btn51 w-100'
            local_stages[stage][1].attr['buttons']['styles'][1] = f'btn btn-lg btn-warning btn52 w-100'
            local_stages[stage][1].attr['buttons']['styles'][2] = f'btn btn-lg btn-outline-warning btn53 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-warning w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'SOS. Бронхообструкция'
            local_flags[5] = '5.2'

        elif local_progress[stage]['3'] == True:
            local_stages[stage][1].attr['buttons']['styles'][0] = f'btn btn-lg btn-outline-warning btn51 w-100'
            local_stages[stage][1].attr['buttons']['styles'][1] = f'btn btn-lg btn-outline-warning btn52 w-100'
            local_stages[stage][1].attr['buttons']['styles'][2] = f'btn btn-lg btn-warning btn53 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-warning w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'SOS. Отёк лёгких'
            local_flags[5] = '5.3'

        if local_stages[stage][0] == 'ca5':
            if local_progress[stage]['1'] == True:
                local_stages[stage][1].next = 'ca23'
            elif local_progress[stage]['2'] == True:
                local_stages[stage][1].next = 'da23'
            elif local_progress[stage]['3'] == True:
                local_stages[stage][1].next = 'ea23'

    elif local_stages[stage][0][2:] == '6':

        if local_progress[stage]['1'] == True:
            local_stages[stage][1].attr['buttons']['styles'][0] = f'btn btn-lg btn-success btn61 w-100'
            local_stages[stage][1].attr['buttons']['styles'][1] = f'btn btn-lg btn-outline-danger btn62 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-success w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'Далее'
            local_flags[6] = '6.1'
   
        elif local_progress[stage]['2'] == True:
            local_stages[stage][1].attr['buttons']['styles'][0] = f'btn btn-lg btn-outline-success btn61 w-100'
            local_stages[stage][1].attr['buttons']['styles'][1] = f'btn btn-lg btn-danger btn62 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-danger w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'SOS. Реанимация!!!'
            local_flags[6] = '6.2'

        if local_stages[stage][0] == 'fa6':
            if local_progress[stage]['1'] == True:
                local_stages[stage][1].next = 'fa7'
            elif local_progress[stage]['2'] == True:
                local_stages[stage][1].next = 'ha13.2'

    elif local_stages[stage][0][2:] == '8':

        body_p = body_params()

        if body_p == None:
            return redirect('/to_beginning')

        local_stages[stage][1].attr['buttons']['text'][0] = f'Систолическое {farm["ads"][body_p][0]}-{farm["ads"][body_p][1]} Диастолическое {farm["add"][body_p][0]}-{farm["add"][body_p][1]} мм.рт.ст.'
        local_stages[stage][1].attr['buttons']['text'][1] = f'Выше 180/120 мм.рт.ст.'
        local_stages[stage][1].attr['buttons']['text'][2] = f'Ниже {farm["ads"][body_p][0]}/{farm["add"][body_p][0]} мм.рт.ст.'
        local_stages[stage][1].attr['buttons']['text'][3] = f'Не определяется'

        if local_progress[stage]['1'] == True:
            local_stages[stage][1].attr['buttons']['styles'][0] = f'btn btn-lg btn-success btn81 w-100'
            local_stages[stage][1].attr['buttons']['styles'][1] = f'btn btn-lg btn-outline-warning btn82 w-100'
            local_stages[stage][1].attr['buttons']['styles'][2] = f'btn btn-lg btn-outline-warning btn83 w-100'
            local_stages[stage][1].attr['buttons']['styles'][3] = f'btn btn-lg btn-outline-danger btn84 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-success w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'Далее'

        elif local_progress[stage]['2'] == True:
            local_stages[stage][1].attr['buttons']['styles'][0] = f'btn btn-lg btn-outline-success btn81 w-100'
            local_stages[stage][1].attr['buttons']['styles'][1] = f'btn btn-lg btn-warning btn82 w-100'
            local_stages[stage][1].attr['buttons']['styles'][2] = f'btn btn-lg btn-outline-warning btn83 w-100'
            local_stages[stage][1].attr['buttons']['styles'][3] = f'btn btn-lg btn-outline-danger btn84 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-warning w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'SOS. Гипертонический криз'   

        elif local_progress[stage]['3'] == True:
            local_stages[stage][1].attr['buttons']['styles'][0] = f'btn btn-lg btn-outline-success btn81 w-100'
            local_stages[stage][1].attr['buttons']['styles'][1] = f'btn btn-lg btn-outline-warning btn82 w-100'
            local_stages[stage][1].attr['buttons']['styles'][2] = f'btn btn-lg btn-warning btn83 w-100'
            local_stages[stage][1].attr['buttons']['styles'][3] = f'btn btn-lg btn-outline-danger btn84 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-warning w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'SOS. Артериальная гипотония'

        elif local_progress[stage]['4'] == True:
            local_stages[stage][1].attr['buttons']['styles'][0] = f'btn btn-lg btn-outline-success btn81 w-100'
            local_stages[stage][1].attr['buttons']['styles'][1] = f'btn btn-lg btn-outline-warning btn82 w-100'
            local_stages[stage][1].attr['buttons']['styles'][2] = f'btn btn-lg btn-outline-warning btn83 w-100'
            local_stages[stage][1].attr['buttons']['styles'][3] = f'btn btn-lg btn-danger btn84 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-danger w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'SOS. Реанимация!!!'

        if local_stages[stage][0] == 'ca8':
            if local_progress[stage]['1'] == True:
                local_stages[stage][1].next = 'ca18'
            elif local_progress[stage]['2'] == True:
                local_stages[stage][1].next = 'fb3.2'
            elif local_progress[stage]['3'] == True:
                local_stages[stage][1].next = 'ca18'
            elif local_progress[stage]['4'] == True:
                local_stages[stage][1].next = 'ha13.2'

        elif local_stages[stage][0] == 'cb8':
            if local_progress[stage]['1'] == True:
                local_stages[stage][1].next = 'ca13.3'
            elif local_progress[stage]['2'] == True:
                local_stages[stage][1].next = 'fb3.2'
            elif local_progress[stage]['3'] == True:
                local_stages[stage][1].next = 'cb13.1'
            elif local_progress[stage]['4'] == True:
                local_stages[stage][1].next = 'ha13.2'

        elif local_stages[stage][0] == 'da8':
            if local_progress[stage]['1'] == True:
                local_stages[stage][1].next = 'da13.3'
            elif local_progress[stage]['2'] == True:
                local_stages[stage][1].next = 'fb3.2'
            elif local_progress[stage]['3'] == True:
                local_stages[stage][1].next = 'db13.1'
            elif local_progress[stage]['4'] == True:
                local_stages[stage][1].next = 'ha13.2'

        elif local_stages[stage][0] == 'db8':
            if local_progress[stage]['1'] == True:
                local_stages[stage][1].next = 'da18'
            elif local_progress[stage]['2'] == True:
                local_stages[stage][1].next = 'fb3.2'
            elif local_progress[stage]['3'] == True:
                local_stages[stage][1].next = 'da18'
            elif local_progress[stage]['4'] == True:
                local_stages[stage][1].next = 'ha13.2'

        elif local_stages[stage][0] == 'ea8':
            if local_progress[stage]['1'] == True:
                local_stages[stage][1].next = 'ea13.3'
            elif local_progress[stage]['2'] == True:
                local_stages[stage][1].next = 'ea13.3'
            elif local_progress[stage]['3'] == True:
                local_stages[stage][1].next = 'eb13.1'
            elif local_progress[stage]['4'] == True:
                local_stages[stage][1].next = 'ha13.2'

        elif local_stages[stage][0] == 'eb8':
            if local_progress[stage]['1'] == True:
                local_stages[stage][1].next = 'ea18'
            elif local_progress[stage]['2'] == True:
                local_stages[stage][1].next = 'ea18'
            elif local_progress[stage]['3'] == True:
                local_stages[stage][1].next = 'ga3.2'
            elif local_progress[stage]['4'] == True:
                local_stages[stage][1].next = 'ha13.2'

        elif local_stages[stage][0] == 'fa8':
            if local_progress[stage]['1'] == True:
                local_stages[stage][1].next = 'fa3.2'
            elif local_progress[stage]['2'] == True:
                local_stages[stage][1].next = 'fb3.2'
            elif local_progress[stage]['3'] == True:
                local_stages[stage][1].next = 'ga3.2'
            elif local_progress[stage]['4'] == True:
                local_stages[stage][1].next = 'ha13.2'

        elif local_stages[stage][0] == 'ga8':
            if local_progress[stage]['1'] == True:
                local_stages[stage][1].next = 'ga10.1'
            elif local_progress[stage]['2'] == True:
                local_stages[stage][1].next = 'fb3.2'
            elif local_progress[stage]['3'] == True:
                local_stages[stage][1].next = 'gb24.3.1'
            elif local_progress[stage]['4'] == True:
                local_stages[stage][1].next = 'ha13.2'

        elif local_stages[stage][0] == 'ia8':
            if local_progress[stage]['1'] == True:
                local_stages[stage][1].next = 'ia23.2'
            elif local_progress[stage]['2'] == True:
                local_stages[stage][1].next = 'fb3.2'
            elif local_progress[stage]['3'] == True:
                local_stages[stage][1].next = 'ia13.4'
            elif local_progress[stage]['4'] == True:
                local_stages[stage][1].next = 'ha13.2'

    elif local_stages[stage][0][2:] == '18.1':

        if local_progress[stage]['1'] == True:
            local_stages[stage][1].attr['buttons']['styles'][0] = f'btn btn-lg btn-success btn181 w-100'
            local_stages[stage][1].attr['buttons']['styles'][1] = f'btn btn-lg btn-outline-danger btn182 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-success w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'Далее'
   
        elif local_progress[stage]['2'] == True:
            local_stages[stage][1].attr['buttons']['styles'][0] = f'btn btn-lg btn-outline-success btn181 w-100'
            local_stages[stage][1].attr['buttons']['styles'][1] = f'btn btn-lg btn-danger btn182 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-success w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'Далее'

        if local_stages[stage][0] == 'fa18.1':
            if local_progress[stage]['1'] == True:
                local_stages[stage][1].next = 'fa24.8.1'
            elif local_progress[stage]['2'] == True:
                local_stages[stage][1].next = 'fa24.13'

    elif local_stages[stage][0][2:] == '19':

        if local_progress[stage]['1'] == True:
            local_stages[stage][1].attr['buttons']['styles'][0] = f'btn btn-lg btn-success btn181 w-100'
            local_stages[stage][1].attr['buttons']['styles'][1] = f'btn btn-lg btn-outline-danger btn182 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-success w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'Далее'
   
        elif local_progress[stage]['2'] == True:
            local_stages[stage][1].attr['buttons']['styles'][0] = f'btn btn-lg btn-outline-success btn181 w-100'
            local_stages[stage][1].attr['buttons']['styles'][1] = f'btn btn-lg btn-danger btn182 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-success w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'Далее'

        if local_stages[stage][0] == 'aa19':
            if local_progress[stage]['1'] == True:
                local_stages[stage][1].next = 'aa10.1'
            elif local_progress[stage]['2'] == True:
                local_stages[stage][1].next = 'aa18'

        elif local_stages[stage][0] == 'ab19':
            if local_progress[stage]['1'] == True:
                local_stages[stage][1].next = 'aa10.1'
            elif local_progress[stage]['2'] == True:
                local_stages[stage][1].next = 'ad20'

        elif local_stages[stage][0] == 'ac19':
            if local_progress[stage]['1'] == True:
                local_stages[stage][1].next = 'aa22'
            elif local_progress[stage]['2'] == True:
                local_stages[stage][1].next = 'ab20'

        elif local_stages[stage][0] == 'ad19':
            if local_progress[stage]['1'] == True:
                local_stages[stage][1].next = 'aa22'
            elif local_progress[stage]['2'] == True:
                local_stages[stage][1].next = 'ac20'

    elif local_stages[stage][0][2:] == '22':

        if local_progress[stage]['1'] == True:
            local_stages[stage][1].attr['buttons']['styles'][0] = f'btn btn-lg btn-success btn181 w-100'
            local_stages[stage][1].attr['buttons']['styles'][1] = f'btn btn-lg btn-outline-danger btn182 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-success w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'Далее'
   
        elif local_progress[stage]['2'] == True:
            local_stages[stage][1].attr['buttons']['styles'][0] = f'btn btn-lg btn-outline-success btn181 w-100'
            local_stages[stage][1].attr['buttons']['styles'][1] = f'btn btn-lg btn-danger btn182 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-success w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'Далее'

        if local_stages[stage][0] == 'aa22':
            if local_progress[stage]['1'] == True:
                local_stages[stage][1].next = 'ba3.2'
            elif local_progress[stage]['2'] == True:
                local_stages[stage][1].next = 'ab21'

    elif local_stages[stage][0][2:] == '23':

        if local_progress[stage]['1'] == True:
            local_stages[stage][1].attr['buttons']['styles'][0] = f'btn btn-lg btn-success btn181 w-100'
            local_stages[stage][1].attr['buttons']['styles'][1] = f'btn btn-lg btn-outline-danger btn182 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-success w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'Далее'
            local_flags[23] = '23.1'
   
        elif local_progress[stage]['2'] == True:
            local_stages[stage][1].attr['buttons']['styles'][0] = f'btn btn-lg btn-outline-success btn181 w-100'
            local_stages[stage][1].attr['buttons']['styles'][1] = f'btn btn-lg btn-danger btn182 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-success w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'Далее'
            local_flags[23] = '23.2'

        if local_stages[stage][0] == 'ca23':
            if local_progress[stage]['1'] == True:
                local_stages[stage][1].next = 'cb7'
            elif local_progress[stage]['2'] == True:
                local_stages[stage][1].next = 'ca13.1'

        elif local_stages[stage][0] == 'da23':
            if local_progress[stage]['1'] == True:
                local_stages[stage][1].next = 'da7'
            elif local_progress[stage]['2'] == True:
                local_stages[stage][1].next = 'da13.1'

        elif local_stages[stage][0] == 'ea23':
            if local_progress[stage]['1'] == True:   
                local_stages[stage][1].next = 'ea7'
            elif local_progress[stage]['2'] == True:
                local_stages[stage][1].next = 'ea13.1'

        elif local_stages[stage][0] == 'db23':
            if local_progress[stage]['1'] == True:
                local_stages[stage][1].next = 'da10.1'
            elif local_progress[stage]['2'] == True:
                local_stages[stage][1].next = 'da9'

        elif local_stages[stage][0] == 'eb23':
            if local_progress[stage]['1'] == True:
                local_stages[stage][1].next = 'ea10.1'
            elif local_progress[stage]['2'] == True:
                local_stages[stage][1].next = 'ea9'

        elif local_stages[stage][0] == 'cb23':
            if local_progress[stage]['1'] == True:
                local_stages[stage][1].next = 'ca10.1'
            elif local_progress[stage]['2'] == True:  
                local_stages[stage][1].next = 'ca9'

        elif local_stages[stage][0] == 'fa23':
            if local_progress[stage]['1'] == True:
                local_stages[stage][1].next = 'fa23.1'
            elif local_progress[stage]['2'] == True:   
                local_stages[stage][1].next = 'fa13.4'

        elif local_stages[stage][0] == 'fb23':
            if local_progress[stage]['1'] == True:
                local_stages[stage][1].next = 'fa12' 
            elif local_progress[stage]['2'] == True:
                local_stages[stage][1].next = 'fa9'

        elif local_stages[stage][0] == 'fc23':
            if local_progress[stage]['1'] == True:
                local_stages[stage][1].next = 'fb12'
            elif local_progress[stage]['2'] == True:
                local_stages[stage][1].next = 'fb9'

        elif local_stages[stage][0] == 'fd23':
            if local_progress[stage]['1'] == True:
                local_stages[stage][1].next = 'fc12'
            elif local_progress[stage]['2'] == True:
                local_stages[stage][1].next = 'fc9'

        elif local_stages[stage][0] == 'fe23':
            if local_progress[stage]['1'] == True:
                local_stages[stage][1].next = 'fe12'
            elif local_progress[stage]['2'] == True:
                local_stages[stage][1].next = 'fd9'

        elif local_stages[stage][0] == 'ff23':
            if local_progress[stage]['1'] == True:
                local_stages[stage][1].next = 'ff12'
            elif local_progress[stage]['2'] == True:
                local_stages[stage][1].next = 'fe9'

        elif local_stages[stage][0] == 'ga23':
            if local_progress[stage]['1'] == True:
                local_stages[stage][1].next = 'ga18'
            elif local_progress[stage]['2'] == True:
                local_stages[stage][1].next = 'ga9.1'

        elif local_stages[stage][0] == 'gb23':
            if local_progress[stage]['1'] == True:
                local_stages[stage][1].next = 'ga12'
            elif local_progress[stage]['2'] == True:
                local_stages[stage][1].next = 'ga9'

    elif local_stages[stage][0][2:] == '23.2':

        if local_progress[stage]['1'] == True:
            local_stages[stage][1].attr['buttons']['styles'][0] = f'btn btn-lg btn-success btn2321 w-100'
            local_stages[stage][1].attr['buttons']['styles'][1] = f'btn btn-lg btn-outline-danger btn2322 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-success w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'Далее'
   
        elif local_progress[stage]['2'] == True:
            local_stages[stage][1].attr['buttons']['styles'][0] = f'btn btn-lg btn-outline-success btn2321 w-100'
            local_stages[stage][1].attr['buttons']['styles'][1] = f'btn btn-lg btn-danger btn2322 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-success w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'Далее'

        if local_stages[stage][0] == 'fa23.2':
            if local_progress[stage]['1'] == True:
                local_stages[stage][1].next = 'fa13.3'
            elif local_progress[stage]['2'] == True:
                local_stages[stage][1].next = 'fd13.4'

        elif local_stages[stage][0] == 'ia23.2':
            if local_progress[stage]['1'] == True:
                local_stages[stage][1].next = 'ia13.3'
            elif local_progress[stage]['2'] == True:
                local_stages[stage][1].next = 'ib13.4'

        elif local_stages[stage][0] == 'ib23.2':
            if local_progress[stage]['1'] == True:
                local_stages[stage][1].next = 'ib16'
            elif local_progress[stage]['2'] == True:
                local_stages[stage][1].next = 'ic24.10'

    elif local_stages[stage][0][2:] == '23.3':

        if local_progress[stage]['1'] == True:
            local_stages[stage][1].attr['buttons']['styles'][0] = f'btn btn-lg btn-danger btn2321 w-100'
            local_stages[stage][1].attr['buttons']['styles'][1] = f'btn btn-lg btn-outline-success btn2322 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-danger w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'Далее'
   
        elif local_progress[stage]['2'] == True:
            local_stages[stage][1].attr['buttons']['styles'][0] = f'btn btn-lg btn-outline-danger btn2321 w-100'
            local_stages[stage][1].attr['buttons']['styles'][1] = f'btn btn-lg btn-success btn2322 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-success w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'Далее'

        if local_stages[stage][0] == 'ga23.3':
            if local_progress[stage]['1'] == True:
                local_stages[stage][1].next = 'ia7'
            elif local_progress[stage]['2'] == True:
                local_stages[stage][1].next = 'ga8.2'

    elif local_stages[stage][0][2:] == '24':

        if local_progress[stage]['1'] == True:
            local_stages[stage][1].attr['buttons']['styles'][0] = f'btn btn-lg btn-success btn181 w-100'
            local_stages[stage][1].attr['buttons']['styles'][1] = f'btn btn-lg btn-outline-danger btn182 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-success w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'Далее'
            local_flags[24] = '24.1'
   
        elif local_progress[stage]['2'] == True:
            local_stages[stage][1].attr['buttons']['styles'][0] = f'btn btn-lg btn-outline-success btn181 w-100'
            local_stages[stage][1].attr['buttons']['styles'][1] = f'btn btn-lg btn-danger btn182 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-success w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'Далее' 
            local_flags[24] = '24.2'

        if local_stages[stage][0] == 'ca24':
            if local_progress[stage]['1'] == True:
                local_stages[stage][1].next = 'ca24.4' 
            elif local_progress[stage]['2'] == True:
                local_stages[stage][1].next = 'ca18'    

        elif local_stages[stage][0] == 'da24':
            if local_progress[stage]['1'] == True:
                local_stages[stage][1].next = 'da24.5' 
            elif local_progress[stage]['2'] == True:
                local_stages[stage][1].next = 'da18'    

    elif local_stages[stage][0][2:] == '25':

        if local_progress[stage]['1'] == True:
            local_stages[stage][1].attr['buttons']['styles'][0] = f'btn btn-lg btn-success btn181 w-100'
            local_stages[stage][1].attr['buttons']['styles'][1] = f'btn btn-lg btn-outline-danger btn182 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-success w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'Далее'
            local_flags[25] = '25.1'
   
        elif local_progress[stage]['2'] == True:
            local_stages[stage][1].attr['buttons']['styles'][0] = f'btn btn-lg btn-outline-success btn181 w-100'
            local_stages[stage][1].attr['buttons']['styles'][1] = f'btn btn-lg btn-danger btn182 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-success w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'Далее'
            local_flags[25] = '25.2'

        if local_stages[stage][0] == 'ca25':
            if local_progress[stage]['1'] == True:
                local_stages[stage][1].next = 'ca10'
            elif local_progress[stage]['2'] == True:
                local_stages[stage][1].next = 'ca16'

        elif local_stages[stage][0] == 'cb25':
            if local_progress[stage]['1'] == True:
                local_stages[stage][1].next = 'ca10'
            elif local_progress[stage]['2'] == True:
                local_stages[stage][1].next = 'cb16'

        elif local_stages[stage][0] == 'da25':
            if local_progress[stage]['1'] == True:
                local_stages[stage][1].next = 'da10'
            elif local_progress[stage]['2'] == True:
                local_stages[stage][1].next = 'da16'

        elif local_stages[stage][0] == 'db25':
            if local_progress[stage]['1'] == True:
                local_stages[stage][1].next = 'da10'
            elif local_progress[stage]['2'] == True:
                local_stages[stage][1].next = 'db16'

    elif local_stages[stage][0][2:] == '26.1':

        if local_progress[stage]['1'] == True:
            local_stages[stage][1].attr['buttons']['styles'][0] = f'btn btn-lg btn-success btn181 w-100'
            local_stages[stage][1].attr['buttons']['styles'][1] = f'btn btn-lg btn-outline-danger btn182 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-success w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'Далее'
   
        elif local_progress[stage]['2'] == True:
            local_stages[stage][1].attr['buttons']['styles'][0] = f'btn btn-lg btn-outline-success btn181 w-100'
            local_stages[stage][1].attr['buttons']['styles'][1] = f'btn btn-lg btn-danger btn182 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-success w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'Далее'

        if local_stages[stage][0] == 'fa26.1':
            if local_progress[stage]['1'] == True:
                local_stages[stage][1].next = 'fc10.1'
            elif local_progress[stage]['2'] == True:
                local_stages[stage][1].next = 'fa18.2'

        elif local_stages[stage][0] == 'fb26.1':
            if local_progress[stage]['1'] == True:
                local_stages[stage][1].next = 'fz10.1'
            elif local_progress[stage]['2'] == True:
                local_stages[stage][1].next = 'fa18.2'

    elif local_stages[stage][0][2:] == '26.2':

        if local_progress[stage]['1'] == True:
            local_stages[stage][1].attr['buttons']['styles'][0] = f'btn btn-lg btn-success btn181 w-100'
            local_stages[stage][1].attr['buttons']['styles'][1] = f'btn btn-lg btn-outline-danger btn182 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-success w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'Далее'
   
        elif local_progress[stage]['2'] == True:
            local_stages[stage][1].attr['buttons']['styles'][0] = f'btn btn-lg btn-outline-success btn181 w-100'
            local_stages[stage][1].attr['buttons']['styles'][1] = f'btn btn-lg btn-danger btn182 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-success w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'Далее'

        if local_stages[stage][0] == 'fa26.2':
            if local_progress[stage]['1'] == True:
                local_stages[stage][1].next = 'fa10.1'
            elif local_progress[stage]['2'] == True:
                local_stages[stage][1].next = 'fa24.9'

        elif local_stages[stage][0] == 'fb26.2':
            if local_progress[stage]['1'] == True:
                local_stages[stage][1].next = 'ff10.1'
            elif local_progress[stage]['2'] == True:
                local_stages[stage][1].next = 'fb24.9'

    elif local_stages[stage][0][2:] == '26.3':

        if local_progress[stage]['1'] == True:
            local_stages[stage][1].attr['buttons']['styles'][0] = f'btn btn-lg btn-success btn181 w-100'
            local_stages[stage][1].attr['buttons']['styles'][1] = f'btn btn-lg btn-outline-danger btn182 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-success w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'Далее'
   
        elif local_progress[stage]['2'] == True:
            local_stages[stage][1].attr['buttons']['styles'][0] = f'btn btn-lg btn-outline-success btn181 w-100'
            local_stages[stage][1].attr['buttons']['styles'][1] = f'btn btn-lg btn-danger btn182 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-success w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'Далее'

        if local_stages[stage][0] == 'fa26.3':
            if local_progress[stage]['1'] == True:
                local_stages[stage][1].next = 'fb10.1'
            elif local_progress[stage]['2'] == True:
                local_stages[stage][1].next = 'fa24.11'

    elif local_stages[stage][0][2:] == '26.4':

        body_p = body_params()

        if body_p == None:
            return redirect('/to_beginning')

        local_stages[stage][1].attr['info']['text'][0] = f'ЧСС выше {farm["css"][body_p][1]} в мин?'

        if local_progress[stage]['1'] == True:
            local_stages[stage][1].attr['buttons']['styles'][0] = f'btn btn-lg btn-success btn2641 w-100'
            local_stages[stage][1].attr['buttons']['styles'][1] = f'btn btn-lg btn-outline-success btn2642 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-success w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'Далее'
   
        elif local_progress[stage]['2'] == True:
            local_stages[stage][1].attr['buttons']['styles'][0] = f'btn btn-lg btn-outline-success btn2641 w-100'
            local_stages[stage][1].attr['buttons']['styles'][1] = f'btn btn-lg btn-success btn2642 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-success w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'Далее'

        if local_stages[stage][0] == 'fa26.4':
            if local_progress[stage]['1'] == True:
                local_stages[stage][1].next = 'fa24.12'
            elif local_progress[stage]['2'] == True:
                local_stages[stage][1].next = 'fa24.12.1'

    elif local_stages[stage][0][2:] == '26.5':

        if local_progress[stage]['1'] == True:
            local_stages[stage][1].attr['buttons']['styles'][0] = f'btn btn-lg btn-success btn181 w-100'
            local_stages[stage][1].attr['buttons']['styles'][1] = f'btn btn-lg btn-outline-danger btn182 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-success w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'Далее'
   
        elif local_progress[stage]['2'] == True:
            local_stages[stage][1].attr['buttons']['styles'][0] = f'btn btn-lg btn-outline-success btn181 w-100'
            local_stages[stage][1].attr['buttons']['styles'][1] = f'btn btn-lg btn-danger btn182 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-success w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'Далее'

        if local_stages[stage][0] == 'ia26.5':
            if local_progress[stage]['1'] == True:
                local_stages[stage][1].next = 'ia10.1'
            elif local_progress[stage]['2'] == True:
                local_stages[stage][1].next = 'ib18'

    elif local_stages[stage][0][2:] == '27.4':

        if local_progress[stage]['1'] == True:
            local_stages[stage][1].attr['buttons']['styles'][0] = f'btn btn-lg btn-success btn181 w-100'
            local_stages[stage][1].attr['buttons']['styles'][1] = f'btn btn-lg btn-outline-danger btn182 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-success w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'Далее'
   
        elif local_progress[stage]['2'] == True:
            local_stages[stage][1].attr['buttons']['styles'][0] = f'btn btn-lg btn-outline-success btn181 w-100'
            local_stages[stage][1].attr['buttons']['styles'][1] = f'btn btn-lg btn-danger btn182 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-success w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'Далее'

        if local_stages[stage][0] == 'ha27.4':
            if local_progress[stage]['1'] == True:
                local_stages[stage][1].next = 'ha27.6'
            elif local_progress[stage]['2'] == True:
                local_stages[stage][1].next = 'ha27.2.1'

        elif local_stages[stage][0] == 'hb27.4':
            if local_progress[stage]['1'] == True:
                local_stages[stage][1].next = 'hb27.6'
            elif local_progress[stage]['2'] == True:
                local_stages[stage][1].next = 'ha27.2.2'

        elif local_stages[stage][0] == 'hc27.4':
            if local_progress[stage]['1'] == True:
                local_stages[stage][1].next = 'ha7'
            elif local_progress[stage]['2'] == True:
                local_stages[stage][1].next = 'ha28.7'

        elif local_stages[stage][0] == 'hd27.4':
            if local_progress[stage]['1'] == True:
                local_stages[stage][1].next = 'hb7'
            elif local_progress[stage]['2'] == True:
                local_stages[stage][1].next = 'hc28.6'

        elif local_stages[stage][0] == 'he27.4':
            if local_progress[stage]['1'] == True:
                local_stages[stage][1].next = 'hb7'
            elif local_progress[stage]['2'] == True:
                local_stages[stage][1].next = 'hb27.2.2'

    elif local_stages[stage][0][2:] == '28.1':

        if local_progress[stage]['1'] == True:
            local_stages[stage][1].attr['buttons']['styles'][0] = f'btn btn-lg btn-success btn181 w-100'
            local_stages[stage][1].attr['buttons']['styles'][1] = f'btn btn-lg btn-outline-danger btn182 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-success w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'Далее'
   
        elif local_progress[stage]['2'] == True:
            local_stages[stage][1].attr['buttons']['styles'][0] = f'btn btn-lg btn-outline-success btn181 w-100'
            local_stages[stage][1].attr['buttons']['styles'][1] = f'btn btn-lg btn-danger btn182 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-success w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'Далее'

        if local_stages[stage][0] == 'ha28.1':
            if local_progress[stage]['1'] == True:
                local_stages[stage][1].next = 'ha28.4'
            elif local_progress[stage]['2'] == True:
                local_stages[stage][1].next = 'ha27.2'

    elif local_stages[stage][0][2:] == '28.2':

        if local_progress[stage]['1'] == True:
            local_stages[stage][1].attr['buttons']['styles'][0] = f'btn btn-lg btn-success btn181 w-100'
            local_stages[stage][1].attr['buttons']['styles'][1] = f'btn btn-lg btn-outline-danger btn182 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-success w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'Далее'
   
        elif local_progress[stage]['2'] == True:
            local_stages[stage][1].attr['buttons']['styles'][0] = f'btn btn-lg btn-outline-success btn181 w-100'
            local_stages[stage][1].attr['buttons']['styles'][1] = f'btn btn-lg btn-danger btn182 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-success w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'Далее'

        if local_stages[stage][0] == 'ha28.2':
            if local_progress[stage]['1'] == True:
                local_stages[stage][1].next = 'ha14'
            elif local_progress[stage]['2'] == True:
                local_stages[stage][1].next = 'hb27.2'

    elif local_stages[stage][0][2:] == '29':

        if local_progress[stage]['1'] == True:
            local_stages[stage][1].attr['buttons']['styles'][0] = f'btn btn-lg btn-danger btn191 w-100'
            local_stages[stage][1].attr['buttons']['styles'][1] = f'btn btn-lg btn-outline-success btn192 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-success w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'Далее'
   
        elif local_progress[stage]['2'] == True:
            local_stages[stage][1].attr['buttons']['styles'][0] = f'btn btn-lg btn-outline-danger btn191 w-100'
            local_stages[stage][1].attr['buttons']['styles'][1] = f'btn btn-lg btn-success btn192 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-success w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'Далее'

        if local_stages[stage][0] == 'ja29':
            if local_progress[stage]['1'] == True:
                local_stages[stage][1].next = 'ia7'
            elif local_progress[stage]['2'] == True:
                local_stages[stage][1].next = 'ja31'

        elif local_stages[stage][0] == 'jb29':
            if local_progress[stage]['1'] == True:
                local_stages[stage][1].next = 'ia7'
            elif local_progress[stage]['2'] == True:
                local_stages[stage][1].next = 'ja31'

    elif local_stages[stage][0][2:] == '30':

        if local_progress[stage]['1'] == True:
            local_stages[stage][1].attr['buttons']['styles'][0] = f'btn btn-lg btn-danger btn191 w-100'
            local_stages[stage][1].attr['buttons']['styles'][1] = f'btn btn-lg btn-outline-success btn192 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-success w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'Далее'
   
        elif local_progress[stage]['2'] == True:
            local_stages[stage][1].attr['buttons']['styles'][0] = f'btn btn-lg btn-outline-danger btn191 w-100'
            local_stages[stage][1].attr['buttons']['styles'][1] = f'btn btn-lg btn-success btn192 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-success w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'Далее'

        if local_stages[stage][0] == 'ja30':
            if local_progress[stage]['1'] == True:
                local_stages[stage][1].next = 'ja29'
            elif local_progress[stage]['2'] == True:
                local_stages[stage][1].next = 'jb29'

    elif local_stages[stage][0][2:] == '31':

        if local_progress[stage]['1'] == True:
            local_stages[stage][1].attr['buttons']['styles'][0] = f'btn btn-lg btn-danger btn191 w-100'
            local_stages[stage][1].attr['buttons']['styles'][1] = f'btn btn-lg btn-outline-success btn192 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-success w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'Далее'
   
        elif local_progress[stage]['2'] == True:
            local_stages[stage][1].attr['buttons']['styles'][0] = f'btn btn-lg btn-outline-danger btn191 w-100'
            local_stages[stage][1].attr['buttons']['styles'][1] = f'btn btn-lg btn-success btn192 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-success w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'Далее'

        if local_stages[stage][0] == 'ja31':
            if local_progress[stage]['1'] == True:
                local_stages[stage][1].next = 'ja9.2'
            elif local_progress[stage]['2'] == True:
                local_stages[stage][1].next = 'ba3.2'

    info.append((local_stages[stage][1].attr['info']['styles'][0], local_stages[stage][1].attr['info']['text'][0]))
    for i in local_progress[stage].keys():
        data.append((local_stages[stage][1].attr['buttons']['styles'][int(i) - 1], local_stages[stage][1].attr['buttons']['text'][int(i) - 1]))
    navigation.append((local_stages[stage][1].attr['navigation']['styles'][1], local_stages[stage][1].attr['navigation']['text'][1], local_stages[stage][1].attr['navigation']['links'][1]))
    navigation.append((local_stages[stage][1].attr['navigation']['styles'][2], local_stages[stage][1].attr['navigation']['text'][2], local_stages[stage][1].attr['navigation']['links'][2]))

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