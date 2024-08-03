from flask import Flask
from flask import render_template, request, jsonify, redirect
from stages import stages, progress

app = Flask(__name__)

current_stage = '0'

stage = 0

local_stages = [('0', stages['0'])]
local_progress = [{'1': False}]

def body_params():
    global local_progress
    for i in local_progress[2].keys():
        if local_progress[2][i] == True:
            return i
    return None

@app.route("/registration")
def registration():
    return render_template("registration.html")


@app.route("/sign_in", methods = ['GET', 'POST'])
def sign_in():
    return render_template("sign_in.html")


@app.route("/main")
@app.route("/")
def main():
    global local_stages, local_progress, stage

    stage = 0
    local_stages = [('0', stages['0'])]
    
    return render_template("index.html")


@app.route("/next_stage")
def next_stage():
    
    global local_stages, local_progress, stage

    local_stages.append((local_stages[stage][1].next, stages[local_stages[stage][1].next].copy()))
    local_progress.append(progress[local_stages[stage][1].next].copy())
    stage += 1

    #print(f'move to {stage}')
    print(f'local progress {local_progress}')
    print(f'local stage {local_stages[stage][0]}')
    print(f'local stage {local_stages[stage][1].attr["navigation"]}')
    #print(stage)

    return redirect(local_stages[stage][1].attr['base_url'])


@app.route("/prev_stage")
def prev_stage():

    global stage, local_stages, local_progress

    local_stages = local_stages[:len(local_stages) - 1]
    local_progress = local_progress[:len(local_progress) - 1]

    stage -= 1

    print(f'move to {current_stage}')
    print(f'local progress {local_progress}')

    return redirect(local_stages[stage][1].attr['base_url'])


@app.route("/test_first", methods = ['GET', 'POST'])
def test_first():

    global local_progress, local_stages, current_stage, stage

    if request.is_json:
        button_number = request.args.get('button_number')
        local_progress[stage][button_number] = not local_progress[stage][button_number]
       
    true_count = 0
    for i in local_progress[stage].keys():
        if local_progress[stage][i] == True:
            local_stages[stage][1].attr['buttons']['text'][int(i) - 1] = 'Выполнено'
            local_stages[stage][1].attr['buttons']['styles'][int(i) - 1] = f'btn btn-lg btn-success btn{i} w-100'
            true_count += 1

    navigation = []
    if true_count == len(local_progress[stage].keys()):
        if local_stages[stage][0] == '1':
            local_stages[stage][1].attr['navigation']['styles'][0] = 'btn btn-lg btn-success w-100 btn-next'
            navigation.append((local_stages[stage][1].attr['navigation']['styles'][0], local_stages[stage][1].attr['navigation']['text'][0], local_stages[stage][1].attr['navigation']['links'][0]))
        else: 
            local_stages[stage][1].attr['navigation']['styles'][1] = 'btn btn-lg btn-success w-100 btn-next'
            navigation.append((local_stages[stage][1].attr['navigation']['styles'][0], local_stages[stage][1].attr['navigation']['text'][0], local_stages[stage][1].attr['navigation']['links'][0]))
            navigation.append((local_stages[stage][1].attr['navigation']['styles'][1], local_stages[stage][1].attr['navigation']['text'][1], local_stages[stage][1].attr['navigation']['links'][1]))
    else:
        if local_stages[stage][0] == '1':
            #print(local_stages[stage][1].attr['navigation']['styles'])
            local_stages[stage][1].attr['navigation']['styles'][0] = 'btn btn-lg btn-outline-danger w-100 btn-next disabled'
            navigation.append((local_stages[stage][1].attr['navigation']['styles'][0], local_stages[stage][1].attr['navigation']['text'][0], local_stages[stage][1].attr['navigation']['links'][0]))
        else:
            local_stages[stage][1].attr['navigation']['styles'][1] = 'btn btn-lg btn-outline-danger w-100 btn-next disabled'
            navigation.append((local_stages[stage][1].attr['navigation']['styles'][0], local_stages[stage][1].attr['navigation']['text'][0], local_stages[stage][1].attr['navigation']['links'][0]))
            navigation.append((local_stages[stage][1].attr['navigation']['styles'][1], local_stages[stage][1].attr['navigation']['text'][1], local_stages[stage][1].attr['navigation']['links'][1]))

    if local_stages[stage][0] == '1':
        local_stages[stage][1].next = '2'

    elif local_stages[stage][0] == '7':
        local_stages[stage][1].next = '8'

    elif local_stages[stage][0] == '9':
        local_stages[stage][1].next = '10'

    elif local_stages[stage][0] == '10':
        local_stages[stage][1].next = '11'

    elif local_stages[stage][0] == '13':
        local_stages[stage][1].next = '4'

    elif local_stages[stage][0] == '13.1':
        local_stages[stage][1].next = '4'

    elif local_stages[stage][0] == '18':
        local_stages[stage][1].next = '21'
        ################################

    elif local_stages[stage][0] == '17':
        local_stages[stage][1].attr['info']['text'] = [f'Установите воздуховод №test{body_params()} или ларингеальную маску №test{body_params()}']

    elif local_stages[stage][0] == '20':
        local_stages[stage][1].attr['info']['text'][0] = f'Поместите сахар/конфету за щёку пациента (не за зубы).При наличии доступа в вену – внутривенно test{body_params()} мл 20% раствора глюкозы (ампулы 40% глюкозы развести пополам 0,9 % раствором NaCl)'
        local_stages[stage][1].next = '19'

    elif local_stages[stage][0] == '21':
        local_stages[stage][1].attr['info']['text'][0] = f'При наличии сосудистого доступа – введите внутривенно вальпроевую кислоту test{body_params()} мл (15 мг/кг), либо мидазолам test{body_params()} мл (0,3 мг/кг), либо диазепам test{body_params()} мл (0,3-0,5 мг/кг)'
        local_stages[stage][1].attr['info']['text'][1] = f'При отсутствии сосудистого доступа внутримышечно ввести мидазолам test{body_params()} мл (0,3 мг/кг), либо диазепам test{body_params()} мл (0,3-0,5 мг/кг)'
        local_stages[stage][1].next = '19'

    data = []
    for i in zip(local_stages[stage][1].attr['buttons']['text'], local_stages[stage][1].attr['buttons']['styles'], local_stages[stage][1].attr['info']['text'], local_stages[stage][1].attr['info']['styles']):
        data.append(i)
    
    return render_template("test1.html", data=data, navigation=navigation, len=len, str=str)


@app.route("/test_second", methods = ['GET', 'POST'])
def test_second():

    global local_progress, local_stages, stage

    if request.is_json:
        button_number = request.args.get('button_number')

        for i in local_progress[stage].keys():
            if i == button_number:
                local_progress[stage][i] = True
            else:
                local_progress[stage][i] = False

        print(f'button_number {button_number}')
        print(f'local progress {local_progress}')
    
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
        local_stages[stage][1].attr['navigation']['styles'][1] = 'btn btn-lg btn-success w-100 btn-next'
    else:
        local_stages[stage][1].attr['navigation']['styles'][1] = 'btn btn-lg btn-outline-danger w-100 btn-next disabled'
    navigation.append((local_stages[stage][1].attr['navigation']['styles'][0], local_stages[stage][1].attr['navigation']['text'][0], local_stages[stage][1].attr['navigation']['links'][0])) 
    navigation.append((local_stages[stage][1].attr['navigation']['styles'][1], local_stages[stage][1].attr['navigation']['text'][1], local_stages[stage][1].attr['navigation']['links'][1]))
    local_stages[stage][1].next = '3'

    return render_template("test2.html", data=data, navigation=navigation)


@app.route("/test_third", methods = ['GET', 'POST'])
def test_third():

    global local_progress, local_stages, current_stage, stage
    data, navigation = [], []
    navigation.append((local_stages[stage][1].attr['navigation']['styles'][0], local_stages[stage][1].attr['navigation']['text'][0], local_stages[stage][1].attr['navigation']['links'][0]))

    if local_stages[stage][0] == '3':

        if request.is_json:
            button_number = request.args.get('button_number')
            if button_number == '1':
                local_progress[stage][button_number] = True
                local_progress[stage]['2'] = False
            elif button_number == '2':
                local_progress[stage][button_number] = True
                local_progress[stage]['1'] = False
            elif button_number == '3':
                local_progress[stage][button_number] = True
                local_progress[stage]['4'] = False
            else:
                local_progress[stage][button_number] = True
                local_progress[stage]['3'] = False
            print(f'button_number {button_number}')
            print(f'local progress {local_progress}')

        if  local_progress[stage]['1'] == True and local_progress[stage]['3'] == True:
            local_stages[stage][1].attr['buttons']['left']['styles'][0] = f'btn btn-lg btn-success btn31 w-100'
            local_stages[stage][1].attr['buttons']['left']['styles'][1] = f'btn btn-lg btn-danger btn33 w-100'
            local_stages[stage][1].attr['buttons']['right']['styles'][0] = f'btn btn-lg btn-outline-danger btn32 w-100'
            local_stages[stage][1].attr['buttons']['right']['styles'][1] = f'btn btn-lg btn-outline-success btn34 w-100'
            local_stages[stage][1].attr['navigation']['styles'][1] = 'btn btn-lg btn-warning w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][1] = 'SOS. Судороги'
            local_stages[stage][1].next = '4'

        elif local_progress[stage]['2'] == True and local_progress[stage]['3'] == True:
            local_stages[stage][1].attr['buttons']['left']['styles'][0] = f'btn btn-lg btn-outline-success btn31 w-100'
            local_stages[stage][1].attr['buttons']['left']['styles'][1] = f'btn btn-lg btn-danger btn33 w-100'
            local_stages[stage][1].attr['buttons']['right']['styles'][0] = f'btn btn-lg btn-danger btn32 w-100'
            local_stages[stage][1].attr['buttons']['right']['styles'][1] = f'btn btn-lg btn-outline-success btn34 w-100'
            local_stages[stage][1].attr['navigation']['styles'][1] = 'btn btn-lg btn-danger w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][1] = 'SOS. Оценить дыхание!'
            local_stages[stage][1].next = '13'

        elif local_progress[stage]['1'] == True and local_progress[stage]['4'] == True:
            local_stages[stage][1].attr['buttons']['left']['styles'][0] = f'btn btn-lg btn-success btn31 w-100'
            local_stages[stage][1].attr['buttons']['left']['styles'][1] = f'btn btn-lg btn-outline-danger btn33 w-100'
            local_stages[stage][1].attr['buttons']['right']['styles'][0] = f'btn btn-lg btn-outline-danger btn32 w-100'
            local_stages[stage][1].attr['buttons']['right']['styles'][1] = f'btn btn-lg btn-success btn34 w-100'
            local_stages[stage][1].attr['navigation']['styles'][1] = 'btn btn-lg btn-success w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][1] = 'Далее'
            local_stages[stage][1].next = '4'

        elif local_progress[stage]['2'] == True and local_progress[stage]['4'] == True:
            local_stages[stage][1].attr['buttons']['left']['styles'][0] = f'btn btn-lg btn-outline-success btn31 w-100'
            local_stages[stage][1].attr['buttons']['left']['styles'][1] = f'btn btn-lg btn-outline-danger btn33 w-100'
            local_stages[stage][1].attr['buttons']['right']['styles'][0] = f'btn btn-lg btn-danger btn32 w-100'
            local_stages[stage][1].attr['buttons']['right']['styles'][1] = f'btn btn-lg btn-success btn34 w-100'
            local_stages[stage][1].attr['navigation']['styles'][1] = 'btn btn-lg btn-danger w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][1] = 'SOS. Оценить дыхание!'
            local_stages[stage][1].next = '13.1'

    if local_stages[stage][0] == '11':

        if request.is_json:

            button_number = request.args.get('button_number')
            if button_number == '1':
                local_progress[stage][button_number] = True
                local_progress[stage]['2'] = False
            elif button_number == '2':
                local_progress[stage][button_number] = True
                local_progress[stage]['1'] = False
            elif button_number == '3':
                local_progress[stage][button_number] = True
                local_progress[stage]['4'] = False
            else:
                local_progress[stage][button_number] = True
                local_progress[stage]['3'] = False
            print(f'button_number {button_number}')
            print(f'local progress {local_progress}')

        if  local_progress[stage]['1'] == True and local_progress[stage]['3'] == True:
            local_stages[stage][1].attr['buttons']['left']['styles'][0] = f'btn btn-lg btn-danger btn111 w-100'
            local_stages[stage][1].attr['buttons']['left']['styles'][1] = f'btn btn-lg btn-danger btn113 w-100'
            local_stages[stage][1].attr['buttons']['right']['styles'][0] = f'btn btn-lg btn-outline-success btn112 w-100'
            local_stages[stage][1].attr['buttons']['right']['styles'][1] = f'btn btn-lg btn-outline-success btn114 w-100'
            local_stages[stage][1].attr['navigation']['styles'][1] = 'btn btn-lg btn-warning w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][1] = 'Далее'
            local_stages[stage][1].next = '18'

        elif local_progress[stage]['2'] == True and local_progress[stage]['3'] == True:
            local_stages[stage][1].attr['buttons']['left']['styles'][0] = f'btn btn-lg btn-outline-danger btn111 w-100'
            local_stages[stage][1].attr['buttons']['left']['styles'][1] = f'btn btn-lg btn-danger btn113 w-100'
            local_stages[stage][1].attr['buttons']['right']['styles'][0] = f'btn btn-lg btn-success btn112 w-100'
            local_stages[stage][1].attr['buttons']['right']['styles'][1] = f'btn btn-lg btn-outline-success btn114 w-100'
            local_stages[stage][1].attr['navigation']['styles'][1] = 'btn btn-lg btn-warning w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][1] = 'Далее'
            local_stages[stage][1].next = '18'

        elif local_progress[stage]['1'] == True and local_progress[stage]['4'] == True:
            local_stages[stage][1].attr['buttons']['left']['styles'][0] = f'btn btn-lg btn-danger btn111 w-100'
            local_stages[stage][1].attr['buttons']['left']['styles'][1] = f'btn btn-lg btn-outline-danger btn113 w-100'
            local_stages[stage][1].attr['buttons']['right']['styles'][0] = f'btn btn-lg btn-outline-success btn112 w-100'
            local_stages[stage][1].attr['buttons']['right']['styles'][1] = f'btn btn-lg btn-success btn114 w-100'
            local_stages[stage][1].attr['navigation']['styles'][1] = 'btn btn-lg btn-warning w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][1] = 'Далее'
            local_stages[stage][1].next = '18'

        elif local_progress[stage]['2'] == True and local_progress[stage]['4'] == True:
            local_stages[stage][1].attr['buttons']['left']['styles'][0] = f'btn btn-lg btn-outline-danger btn111 w-100'
            local_stages[stage][1].attr['buttons']['left']['styles'][1] = f'btn btn-lg btn-outline-danger btn113 w-100'
            local_stages[stage][1].attr['buttons']['right']['styles'][0] = f'btn btn-lg btn-success btn112 w-100'
            local_stages[stage][1].attr['buttons']['right']['styles'][1] = f'btn btn-lg btn-success btn114 w-100'
            local_stages[stage][1].attr['navigation']['styles'][1] = 'btn btn-lg btn-success w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][1] = 'Далее'
            local_stages[stage][1].next = '12'

    if local_stages[stage][0] == '15':

        if request.is_json:

            button_number = request.args.get('button_number')
            if button_number == '1':
                local_progress[stage][button_number] = True
                local_progress[stage]['2'] = False
            elif button_number == '2':
                local_progress[stage][button_number] = True
                local_progress[stage]['1'] = False
            elif button_number == '3':
                local_progress[stage][button_number] = True
                local_progress[stage]['4'] = False
            else:
                local_progress[stage][button_number] = True
                local_progress[stage]['3'] = False
            print(f'button_number {button_number}')
            print(f'local progress {local_progress}')

        if  local_progress[stage]['1'] == True and local_progress[stage]['3'] == True:
            local_stages[stage][1].attr['buttons']['left']['styles'][0] = f'btn btn-lg btn-success btn151 w-100'
            local_stages[stage][1].attr['buttons']['left']['styles'][1] = f'btn btn-lg btn-success btn153 w-100'
            local_stages[stage][1].attr['buttons']['right']['styles'][0] = f'btn btn-lg btn-outline-danger btn152 w-100'
            local_stages[stage][1].attr['buttons']['right']['styles'][1] = f'btn btn-lg btn-outline-danger btn154 w-100'
            local_stages[stage][1].attr['navigation']['styles'][1] = 'btn btn-lg btn-success w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][1] = 'Далее'
            local_stages[stage][1].next = '16'

        elif local_progress[stage]['2'] == True and local_progress[stage]['3'] == True:
            local_stages[stage][1].attr['buttons']['left']['styles'][0] = f'btn btn-lg btn-outline-success btn151 w-100'
            local_stages[stage][1].attr['buttons']['left']['styles'][1] = f'btn btn-lg btn-success btn153 w-100'
            local_stages[stage][1].attr['buttons']['right']['styles'][0] = f'btn btn-lg btn-danger btn152 w-100'
            local_stages[stage][1].attr['buttons']['right']['styles'][1] = f'btn btn-lg btn-outline-danger btn154 w-100'
            local_stages[stage][1].attr['navigation']['styles'][1] = 'btn btn-lg btn-warning w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][1] = 'Далее'
            local_stages[stage][1].next = '16'

        elif local_progress[stage]['1'] == True and local_progress[stage]['4'] == True:
            local_stages[stage][1].attr['buttons']['left']['styles'][0] = f'btn btn-lg btn-success btn151 w-100'
            local_stages[stage][1].attr['buttons']['left']['styles'][1] = f'btn btn-lg btn-outline-success btn153 w-100'
            local_stages[stage][1].attr['buttons']['right']['styles'][0] = f'btn btn-lg btn-outline-danger btn152 w-100'
            local_stages[stage][1].attr['buttons']['right']['styles'][1] = f'btn btn-lg btn-danger btn154 w-100'
            local_stages[stage][1].attr['navigation']['styles'][1] = 'btn btn-lg btn-success w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][1] = 'Далее'
            local_stages[stage][1].next = '16'

        elif local_progress[stage]['2'] == True and local_progress[stage]['4'] == True:
            local_stages[stage][1].attr['buttons']['left']['styles'][0] = f'btn btn-lg btn-outline-success btn151 w-100'
            local_stages[stage][1].attr['buttons']['left']['styles'][1] = f'btn btn-lg btn-outline-success btn153 w-100'
            local_stages[stage][1].attr['buttons']['right']['styles'][0] = f'btn btn-lg btn-danger btn152 w-100'
            local_stages[stage][1].attr['buttons']['right']['styles'][1] = f'btn btn-lg btn-danger btn154 w-100'
            local_stages[stage][1].attr['navigation']['styles'][1] = 'btn btn-lg btn-warning w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][1] = 'Далее'
            local_stages[stage][1].next = '16'

    navigation.append((local_stages[stage][1].attr['navigation']['styles'][1], local_stages[stage][1].attr['navigation']['text'][1], local_stages[stage][1].attr['navigation']['links'][1]))

    for i in range(int(len(local_progress[stage].keys())//2)):
        data.append((local_stages[stage][1].attr['info']['styles'][i], local_stages[stage][1].attr['info']['text'][i], local_stages[stage][1].attr['buttons']['left']['styles'][i], local_stages[stage][1].attr['buttons']['left']['text'][i], local_stages[stage][1].attr['buttons']['right']['styles'][i], local_stages[stage][1].attr['buttons']['right']['text'][i]))
    
    return render_template("test3.html", data=data, length=len(data), navigation=navigation)


@app.route("/test_fourth", methods = ['GET', 'POST'])
def test_fourth():

    global local_progress, local_stages, current_stage, stage
    info, data, navigation = [], [], []
    navigation.append((local_stages[stage][1].attr['navigation']['styles'][0], local_stages[stage][1].attr['navigation']['text'][0], local_stages[stage][1].attr['navigation']['links'][0]))

    if local_stages[stage][0] == '4':

        if request.is_json:
            button_number = request.args.get('button_number')

            for i in local_progress[stage].keys():
                if i == button_number:
                    local_progress[stage][i] = True
                else:
                    local_progress[stage][i] = False

            print(f'button_number {button_number}')
            print(f'local progress {local_progress}')

        if local_progress[stage]['1'] == True:
            local_stages[stage][1].attr['buttons']['styles'][0] = f'btn btn-lg btn-success btn41 w-100'
            local_stages[stage][1].attr['buttons']['styles'][1] = f'btn btn-lg btn-outline-warning btn42 w-100'
            local_stages[stage][1].attr['buttons']['styles'][2] = f'btn btn-lg btn-outline-warning btn43 w-100'
            local_stages[stage][1].attr['buttons']['styles'][3] = f'btn btn-lg btn-outline-danger btn44 w-100'
            local_stages[stage][1].attr['navigation']['styles'][1] = 'btn btn-lg btn-success w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][1] = 'Далее'
            local_stages[stage][1].next = '7'
   
        elif local_progress[stage]['2'] == True:
            local_stages[stage][1].attr['buttons']['styles'][0] = f'btn btn-lg btn-outline-success btn41 w-100'
            local_stages[stage][1].attr['buttons']['styles'][1] = f'btn btn-lg btn-warning btn42 w-100'
            local_stages[stage][1].attr['buttons']['styles'][2] = f'btn btn-lg btn-outline-warning btn43 w-100'
            local_stages[stage][1].attr['buttons']['styles'][3] = f'btn btn-lg btn-outline-danger btn44 w-100'
            local_stages[stage][1].attr['navigation']['styles'][1] = 'btn btn-lg btn-warning w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][1] = 'SOS. Обеспечение проходимости дыхательных путей'
            local_stages[stage][1].next = '7'

        elif local_progress[stage]['3'] == True:
            local_stages[stage][1].attr['buttons']['styles'][0] = f'btn btn-lg btn-outline-success btn41 w-100'
            local_stages[stage][1].attr['buttons']['styles'][1] = f'btn btn-lg btn-outline-warning btn42 w-100'
            local_stages[stage][1].attr['buttons']['styles'][2] = f'btn btn-lg btn-warning btn43 w-100'
            local_stages[stage][1].attr['buttons']['styles'][3] = f'btn btn-lg btn-outline-danger btn44 w-100'
            local_stages[stage][1].attr['navigation']['styles'][1] = 'btn btn-lg btn-warning w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][1] = 'SOS. Дыхательная недостаточность'
            local_stages[stage][1].next = '7'

        elif local_progress[stage]['4'] == True:
            local_stages[stage][1].attr['buttons']['styles'][0] = f'btn btn-lg btn-outline-success btn41 w-100'
            local_stages[stage][1].attr['buttons']['styles'][1] = f'btn btn-lg btn-outline-warning btn42 w-100'
            local_stages[stage][1].attr['buttons']['styles'][2] = f'btn btn-lg btn-outline-warning btn43 w-100'
            local_stages[stage][1].attr['buttons']['styles'][3] = f'btn btn-lg btn-danger btn44 w-100'
            local_stages[stage][1].attr['navigation']['styles'][1] = 'btn btn-lg btn-danger w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][1] = 'SOS. Реанимация!!!'
            local_stages[stage][1].next = '7'

        info.append((local_stages[stage][1].attr['info']['styles'][0], local_stages[stage][1].attr['info']['text'][0]))
        for i in local_progress[stage].keys():
            data.append((local_stages[stage][1].attr['buttons']['styles'][int(i) - 1], local_stages[stage][1].attr['buttons']['text'][int(i) - 1]))
        navigation.append((local_stages[stage][1].attr['navigation']['styles'][1], local_stages[stage][1].attr['navigation']['text'][1], local_stages[stage][1].attr['navigation']['links'][1]))


    elif local_stages[stage][0] == '5':

        if request.is_json:
            button_number = request.args.get('button_number')

            for i in local_progress[stage].keys():
                if i == button_number:
                    local_progress[stage][i] = True
                else:
                    local_progress[stage][i] = False

            print(f'button_number {button_number}')
            print(f'local progress {local_progress}')

        if local_progress[stage]['1'] == True:
            local_stages[stage][1].attr['buttons']['styles'][0] = f'btn btn-lg btn-warning btn51 w-100'
            local_stages[stage][1].attr['buttons']['styles'][1] = f'btn btn-lg btn-outline-warning btn52 w-100'
            local_stages[stage][1].attr['buttons']['styles'][2] = f'btn btn-lg btn-outline-warning btn53 w-100'
            local_stages[stage][1].attr['navigation']['styles'][1] = 'btn btn-lg btn-warning w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][1] = 'SOS. Отёк гортани'
   
        elif local_progress[stage]['2'] == True:
            local_stages[stage][1].attr['buttons']['styles'][0] = f'btn btn-lg btn-outline-warning btn51 w-100'
            local_stages[stage][1].attr['buttons']['styles'][1] = f'btn btn-lg btn-warning btn52 w-100'
            local_stages[stage][1].attr['buttons']['styles'][2] = f'btn btn-lg btn-outline-warning btn53 w-100'
            local_stages[stage][1].attr['navigation']['styles'][1] = 'btn btn-lg btn-warning w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][1] = 'SOS. Бронхообструкция'

        elif local_progress[stage]['3'] == True:
            local_stages[stage][1].attr['buttons']['styles'][0] = f'btn btn-lg btn-outline-warning btn51 w-100'
            local_stages[stage][1].attr['buttons']['styles'][1] = f'btn btn-lg btn-outline-warning btn52 w-100'
            local_stages[stage][1].attr['buttons']['styles'][2] = f'btn btn-lg btn-warning btn53 w-100'
            local_stages[stage][1].attr['navigation']['styles'][1] = 'btn btn-lg btn-warning w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][1] = 'SOS. Отёк лёгких'

        info.append((local_stages[stage][1].attr['info']['styles'][0], local_stages[stage][1].attr['info']['text'][0]))
        for i in local_progress[stage].keys():
            data.append((local_stages[stage][1].attr['buttons']['styles'][int(i) - 1], local_stages[stage][1].attr['buttons']['text'][int(i) - 1]))
        navigation.append((local_stages[stage][1].attr['navigation']['styles'][1], local_stages[stage][1].attr['navigation']['text'][1], local_stages[stage][1].attr['navigation']['links'][1]))
    

    elif local_stages[stage][0] == '6':

        if request.is_json:
            button_number = request.args.get('button_number')

            for i in local_progress[stage].keys():
                if i == button_number:
                    local_progress[stage][i] = True
                else:
                    local_progress[stage][i] = False

            print(f'button_number {button_number}')
            print(f'local progress {local_progress}')

        if local_progress[stage]['1'] == True:
            local_stages[stage][1].attr['buttons']['styles'][0] = f'btn btn-lg btn-success btn61 w-100'
            local_stages[stage][1].attr['buttons']['styles'][1] = f'btn btn-lg btn-outline-danger btn62 w-100'
            local_stages[stage][1].attr['navigation']['styles'][1] = 'btn btn-lg btn-success w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][1] = 'Далее'
   
        elif local_progress[stage]['2'] == True:
            local_stages[stage][1].attr['buttons']['styles'][0] = f'btn btn-lg btn-outline-success btn61 w-100'
            local_stages[stage][1].attr['buttons']['styles'][1] = f'btn btn-lg btn-danger btn62 w-100'
            local_stages[stage][1].attr['navigation']['styles'][1] = 'btn btn-lg btn-danger w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][1] = 'SOS. Реанимация!!!'


        info.append((local_stages[stage][1].attr['info']['styles'][0], local_stages[stage][1].attr['info']['text'][0]))
        for i in local_progress[stage].keys():
            data.append((local_stages[stage][1].attr['buttons']['styles'][int(i) - 1], local_stages[stage][1].attr['buttons']['text'][int(i) - 1]))
        navigation.append((local_stages[stage][1].attr['navigation']['styles'][1], local_stages[stage][1].attr['navigation']['text'][1], local_stages[stage][1].attr['navigation']['links'][1]))

    if local_stages[stage][0] == '8':

        if request.is_json:
            button_number = request.args.get('button_number')

            for i in local_progress[stage].keys():
                if i == button_number:
                    local_progress[stage][i] = True
                else:
                    local_progress[stage][i] = False

            print(f'button_number {button_number}')
            print(f'local progress {local_progress}')

        #local_stages[current_stage].attr['navigation']['styles'][1] = 'btn btn-lg btn-outline-danger w-100 btn-next'
        #local_stages[current_stage].attr['navigation']['text'][1] = 'Далее'
   
        if local_progress[stage]['1'] == True:
            local_stages[stage][1].attr['buttons']['styles'][0] = f'btn btn-lg btn-success btn81 w-100'
            local_stages[stage][1].attr['buttons']['styles'][1] = f'btn btn-lg btn-outline-warning btn82 w-100'
            local_stages[stage][1].attr['buttons']['styles'][2] = f'btn btn-lg btn-outline-warning btn83 w-100'
            local_stages[stage][1].attr['buttons']['styles'][3] = f'btn btn-lg btn-outline-danger btn84 w-100'
            local_stages[stage][1].attr['navigation']['styles'][1] = 'btn btn-lg btn-success w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][1] = 'Далее'
            local_stages[stage][1].next = '9'
   
        elif local_progress[stage]['2'] == True:
            local_stages[stage][1].attr['buttons']['styles'][0] = f'btn btn-lg btn-outline-success btn81 w-100'
            local_stages[stage][1].attr['buttons']['styles'][1] = f'btn btn-lg btn-warning btn82 w-100'
            local_stages[stage][1].attr['buttons']['styles'][2] = f'btn btn-lg btn-outline-warning btn83 w-100'
            local_stages[stage][1].attr['buttons']['styles'][3] = f'btn btn-lg btn-outline-danger btn84 w-100'
            local_stages[stage][1].attr['navigation']['styles'][1] = 'btn btn-lg btn-warning w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][1] = 'SOS. Гипертонический криз'
            local_stages[stage][1].next = '9'

        elif local_progress[stage]['3'] == True:
            local_stages[stage][1].attr['buttons']['styles'][0] = f'btn btn-lg btn-outline-success btn81 w-100'
            local_stages[stage][1].attr['buttons']['styles'][1] = f'btn btn-lg btn-outline-warning btn82 w-100'
            local_stages[stage][1].attr['buttons']['styles'][2] = f'btn btn-lg btn-warning btn83 w-100'
            local_stages[stage][1].attr['buttons']['styles'][3] = f'btn btn-lg btn-outline-danger btn84 w-100'
            local_stages[stage][1].attr['navigation']['styles'][1] = 'btn btn-lg btn-warning w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][1] = 'SOS. Артериальная гипотония'
            local_stages[stage][1].next = '9'

        elif local_progress[stage]['4'] == True:
            local_stages[stage][1].attr['buttons']['styles'][0] = f'btn btn-lg btn-outline-success btn81 w-100'
            local_stages[stage][1].attr['buttons']['styles'][1] = f'btn btn-lg btn-outline-warning btn82 w-100'
            local_stages[stage][1].attr['buttons']['styles'][2] = f'btn btn-lg btn-outline-warning btn83 w-100'
            local_stages[stage][1].attr['buttons']['styles'][3] = f'btn btn-lg btn-danger btn84 w-100'
            local_stages[stage][1].attr['navigation']['styles'][1] = 'btn btn-lg btn-danger w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][1] = 'SOS. Реанимация!!!'
            local_stages[stage][1].next = '9'

        info.append((local_stages[stage][1].attr['info']['styles'][0], local_stages[stage][1].attr['info']['text'][0]))
        for i in local_progress[stage].keys():
            data.append((local_stages[stage][1].attr['buttons']['styles'][int(i) - 1], local_stages[stage][1].attr['buttons']['text'][int(i) - 1]))
        navigation.append((local_stages[stage][1].attr['navigation']['styles'][1], local_stages[stage][1].attr['navigation']['text'][1], local_stages[stage][1].attr['navigation']['links'][1]))


    elif local_stages[stage][0] == '18.1':

        if request.is_json:
            button_number = request.args.get('button_number')

            for i in local_progress[stage].keys():
                if i == button_number:
                    local_progress[stage][i] = True
                else:
                    local_progress[stage][i] = False

            print(f'button_number {button_number}')
            print(f'local progress {local_progress}')

        if local_progress[stage]['1'] == True:
            local_stages[stage][1].attr['buttons']['styles'][0] = f'btn btn-lg btn-success btn181 w-100'
            local_stages[stage][1].attr['buttons']['styles'][1] = f'btn btn-lg btn-outline-danger btn182 w-100'
            local_stages[stage][1].attr['navigation']['styles'][1] = 'btn btn-lg btn-success w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][1] = 'Далее'
   
        elif local_progress[stage]['2'] == True:
            local_stages[stage][1].attr['buttons']['styles'][0] = f'btn btn-lg btn-outline-success btn181 w-100'
            local_stages[stage][1].attr['buttons']['styles'][1] = f'btn btn-lg btn-danger btn182 w-100'
            local_stages[stage][1].attr['navigation']['styles'][1] = 'btn btn-lg btn-success w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][1] = 'Далее'


        info.append((local_stages[stage][1].attr['info']['styles'][0], local_stages[stage][1].attr['info']['text'][0]))
        for i in local_progress[stage].keys():
            data.append((local_stages[stage][1].attr['buttons']['styles'][int(i) - 1], local_stages[stage][1].attr['buttons']['text'][int(i) - 1]))
        navigation.append((local_stages[stage][1].attr['navigation']['styles'][1], local_stages[stage][1].attr['navigation']['text'][1], local_stages[stage][1].attr['navigation']['links'][1]))
    

    elif local_stages[stage][0] == '19':

        if request.is_json:
            button_number = request.args.get('button_number')

            for i in local_progress[stage].keys():
                if i == button_number:
                    local_progress[stage][i] = True
                else:
                    local_progress[stage][i] = False

            print(f'button_number {button_number}')
            print(f'local progress {local_progress}')

        if local_progress[stage]['1'] == True:
            local_stages[stage][1].attr['buttons']['styles'][0] = f'btn btn-lg btn-success btn191 w-100'
            local_stages[stage][1].attr['buttons']['styles'][1] = f'btn btn-lg btn-outline-danger btn192 w-100'
            local_stages[stage][1].attr['navigation']['styles'][1] = 'btn btn-lg btn-success w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][1] = 'Далее'
            local_stages[stage][1].next = '22'
   
        elif local_progress[stage]['2'] == True:
            local_stages[stage][1].attr['buttons']['styles'][0] = f'btn btn-lg btn-outline-success btn191 w-100'
            local_stages[stage][1].attr['buttons']['styles'][1] = f'btn btn-lg btn-danger btn192 w-100'
            local_stages[stage][1].attr['navigation']['styles'][1] = 'btn btn-lg btn-success w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][1] = 'Далее'
            local_stages[stage][1].next = '20'


        info.append((local_stages[stage][1].attr['info']['styles'][0], local_stages[stage][1].attr['info']['text'][0]))
        for i in local_progress[stage].keys():
            data.append((local_stages[stage][1].attr['buttons']['styles'][int(i) - 1], local_stages[stage][1].attr['buttons']['text'][int(i) - 1]))
        navigation.append((local_stages[stage][1].attr['navigation']['styles'][1], local_stages[stage][1].attr['navigation']['text'][1], local_stages[stage][1].attr['navigation']['links'][1]))


    elif local_stages[stage][0] == '22':

        if request.is_json:
            button_number = request.args.get('button_number')

            for i in local_progress[stage].keys():
                if i == button_number:
                    local_progress[stage][i] = True
                else:
                    local_progress[stage][i] = False

            print(f'button_number {button_number}')
            print(f'local progress {local_progress}')

        if local_progress[stage]['1'] == True:
            local_stages[stage][1].attr['buttons']['styles'][0] = f'btn btn-lg btn-success btn221 w-100'
            local_stages[stage][1].attr['buttons']['styles'][1] = f'btn btn-lg btn-outline-danger btn222 w-100'
            local_stages[stage][1].attr['navigation']['styles'][1] = 'btn btn-lg btn-success w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][1] = 'Далее'
            local_stages[stage][1].next = '10'
   
        elif local_progress[stage]['2'] == True:
            local_stages[stage][1].attr['buttons']['styles'][0] = f'btn btn-lg btn-outline-success btn221 w-100'
            local_stages[stage][1].attr['buttons']['styles'][1] = f'btn btn-lg btn-danger btn222 w-100'
            local_stages[stage][1].attr['navigation']['styles'][1] = 'btn btn-lg btn-success w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][1] = 'Далее'
            local_stages[stage][1].next = '21'


        info.append((local_stages[stage][1].attr['info']['styles'][0], local_stages[stage][1].attr['info']['text'][0]))
        for i in local_progress[stage].keys():
            data.append((local_stages[stage][1].attr['buttons']['styles'][int(i) - 1], local_stages[stage][1].attr['buttons']['text'][int(i) - 1]))
        navigation.append((local_stages[stage][1].attr['navigation']['styles'][1], local_stages[stage][1].attr['navigation']['text'][1], local_stages[stage][1].attr['navigation']['links'][1]))


    return render_template("test4.html", info=info, data=data, navigation=navigation)


def run_app():
    app.run(debug=True)


if __name__ == "__main__":
    app.run(debug=True)