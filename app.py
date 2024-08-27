from flask import Flask
from flask import render_template, request, redirect, session
from stages import stages, progress


app = Flask(__name__)
app.config['SECRET_KEY'] = '9bf43c3a13544daaff33ffa122e8c8a54275d280'

stage = 0
local_stages = [('a0', stages['a0'])]
local_progress = [{'a1': False}]
local_flags = {'flag_changes': False}
local_changes = []

def progress_output():
    global local_progress, local_stages, stage
    print(f'Current stage: {stage}')
    print(f'Current flags: {local_flags}')
    for i in range(1, len(local_progress)):
        print(f'stage: {i}, template: {local_stages[i][0]}, Current progress {local_progress[i]}')

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

    global local_stages, local_progress, stage, local_flags

    stage = 0
    local_stages = [('a0', stages['a0'])]
    local_progress = [{'a1': False}]
    local_flags = {'flag_changes': False}
    print(request.user_agent_class)
    
    return render_template("index.html")


@app.route("/next_stage")
def next_stage():
    
    global local_stages, local_progress, stage, local_flags, local_changes

    if stage + 1 == len(local_progress):
        print("\n" + f'var1')
        local_stages.append((local_stages[stage][1].next, stages[local_stages[stage][1].next].copy()))
        local_progress.append(progress[local_stages[stage][1].next[1:]].copy())
        stage += 1
        local_stages[stage][1].prev = local_stages[stage - 1][0]
        local_flags['flag_changes'] = False

    elif local_flags['flag_changes']:
        print("\n" + f'var2')
        local_stages = local_stages[:stage + 1]
        local_progress = local_progress[:stage + 1]
        local_stages.append((local_stages[stage][1].next, stages[local_stages[stage][1].next].copy()))
        local_progress.append(progress[local_stages[stage][1].next[1:]].copy())
        stage += 1
        local_stages[stage][1].prev = local_stages[stage - 1][0]
        local_flags['flag_changes'] = False

    elif not local_flags['flag_changes'] and stage < len(local_progress):
        print("\n" + f'var3')
        stage += 1

    progress_output()

    local_changes.clear()

    if local_stages[stage][1].prev[1:] == '12':
        return redirect('/main')
    else:
        return redirect(local_stages[stage][1].attr['base_url'])


@app.route("/prev_stage")
def prev_stage():

    global stage, local_stages, local_progress, local_flags, local_changes

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
def to_beginning():
    global local_stages, local_progress, stage, local_flags
    stage = 0
    local_stages = [('0', stages['0'])]
    local_progress = [{'1': False}]
    local_flags = {'flag_changes': False}

    return redirect('/next_stage')


@app.route("/test_first", methods = ['GET', 'POST'])
def test_first():

    global local_progress, local_stages, stage, local_flags

    if local_stages[stage][1].attr['base_url'] != "test_first":
        return redirect('/prev_stage')

    if request.is_json:
        #print(request.path)

        button_number = request.args.get('button_number')
        local_progress[stage][button_number] = not local_progress[stage][button_number]
       
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
        if local_stages[stage][0] == 'a1':
            local_stages[stage][1].attr['navigation']['styles'][0] = 'btn btn-lg btn-success w-100 btn-next'
            navigation.append((local_stages[stage][1].attr['navigation']['styles'][0], local_stages[stage][1].attr['navigation']['text'][0], local_stages[stage][1].attr['navigation']['links'][0]))
        else: 
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-success w-100 btn-next'
            navigation.append((local_stages[stage][1].attr['navigation']['styles'][0], local_stages[stage][1].attr['navigation']['text'][0], local_stages[stage][1].attr['navigation']['links'][0]))
            navigation.append((local_stages[stage][1].attr['navigation']['styles'][1], local_stages[stage][1].attr['navigation']['text'][1], local_stages[stage][1].attr['navigation']['links'][1]))
            navigation.append((local_stages[stage][1].attr['navigation']['styles'][2], local_stages[stage][1].attr['navigation']['text'][2], local_stages[stage][1].attr['navigation']['links'][2]))
    else:
        if local_stages[stage][0] == 'a1':
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
    
    return render_template("test1.html", data=data, navigation=navigation, len=len, str=str)


@app.route("/test_second", methods = ['GET', 'POST'])
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

    return render_template("test2.html", data=data, navigation=navigation)
   

@app.route("/test_third", methods = ['GET', 'POST'])
def test_third():

    global local_progress, local_stages, stage, local_flags, local_changes

    if local_stages[stage][1].attr['base_url'] != "test_third":
        return redirect('/prev_stage')

    data, navigation = [], []
    navigation.append((local_stages[stage][1].attr['navigation']['styles'][0], local_stages[stage][1].attr['navigation']['text'][0], local_stages[stage][1].attr['navigation']['links'][0]))

    if local_stages[stage][0] == 'a3':

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

        if  local_progress[stage]['1'] == True and local_progress[stage]['3'] == True:
            local_stages[stage][1].attr['buttons']['left']['styles'][0] = f'btn btn-lg btn-success btn31 w-100'
            local_stages[stage][1].attr['buttons']['left']['styles'][1] = f'btn btn-lg btn-danger btn33 w-100'
            local_stages[stage][1].attr['buttons']['right']['styles'][0] = f'btn btn-lg btn-outline-danger btn32 w-100'
            local_stages[stage][1].attr['buttons']['right']['styles'][1] = f'btn btn-lg btn-outline-success btn34 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-warning w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'SOS. Судороги'
            local_stages[stage][1].next = 'a3.2'
            local_flags[stage] = '3.1'


        elif local_progress[stage]['2'] == True and local_progress[stage]['3'] == True:
            local_stages[stage][1].attr['buttons']['left']['styles'][0] = f'btn btn-lg btn-outline-success btn31 w-100'
            local_stages[stage][1].attr['buttons']['left']['styles'][1] = f'btn btn-lg btn-danger btn33 w-100'
            local_stages[stage][1].attr['buttons']['right']['styles'][0] = f'btn btn-lg btn-danger btn32 w-100'
            local_stages[stage][1].attr['buttons']['right']['styles'][1] = f'btn btn-lg btn-outline-success btn34 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-danger w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'SOS. Оценить дыхание!'
            local_stages[stage][1].next = 'a13'
            local_flags[stage] = '3.3'

        elif local_progress[stage]['1'] == True and local_progress[stage]['4'] == True:
            local_stages[stage][1].attr['buttons']['left']['styles'][0] = f'btn btn-lg btn-success btn31 w-100'
            local_stages[stage][1].attr['buttons']['left']['styles'][1] = f'btn btn-lg btn-outline-danger btn33 w-100'
            local_stages[stage][1].attr['buttons']['right']['styles'][0] = f'btn btn-lg btn-outline-danger btn32 w-100'
            local_stages[stage][1].attr['buttons']['right']['styles'][1] = f'btn btn-lg btn-success btn34 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-success w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'Далее'
            local_stages[stage][1].next = 'a3.2'
            local_flags[stage] = '3.1'

        elif local_progress[stage]['2'] == True and local_progress[stage]['4'] == True:
            local_stages[stage][1].attr['buttons']['left']['styles'][0] = f'btn btn-lg btn-outline-success btn31 w-100'
            local_stages[stage][1].attr['buttons']['left']['styles'][1] = f'btn btn-lg btn-outline-danger btn33 w-100'
            local_stages[stage][1].attr['buttons']['right']['styles'][0] = f'btn btn-lg btn-danger btn32 w-100'
            local_stages[stage][1].attr['buttons']['right']['styles'][1] = f'btn btn-lg btn-success btn34 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-danger w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'SOS. Оценить дыхание!'
            local_stages[stage][1].next = 'a13.1'
            local_flags[stage] = '3.2'

    if local_stages[stage][0] == 'a11':

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

        if  local_progress[stage]['1'] == True and local_progress[stage]['3'] == True:
            local_stages[stage][1].attr['buttons']['left']['styles'][0] = f'btn btn-lg btn-danger btn111 w-100'
            local_stages[stage][1].attr['buttons']['left']['styles'][1] = f'btn btn-lg btn-danger btn113 w-100'
            local_stages[stage][1].attr['buttons']['right']['styles'][0] = f'btn btn-lg btn-outline-success btn112 w-100'
            local_stages[stage][1].attr['buttons']['right']['styles'][1] = f'btn btn-lg btn-outline-success btn114 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-warning w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'Далее'

            if local_flags[3] == '3.2':
                local_stages[stage][1].next = 'a9'
            elif local_flags[3] == '3.3':
                local_stages[stage][1].next = 'a9.1'

        elif local_progress[stage]['2'] == True and local_progress[stage]['3'] == True:
            local_stages[stage][1].attr['buttons']['left']['styles'][0] = f'btn btn-lg btn-outline-danger btn111 w-100'
            local_stages[stage][1].attr['buttons']['left']['styles'][1] = f'btn btn-lg btn-danger btn113 w-100'
            local_stages[stage][1].attr['buttons']['right']['styles'][0] = f'btn btn-lg btn-success btn112 w-100'
            local_stages[stage][1].attr['buttons']['right']['styles'][1] = f'btn btn-lg btn-outline-success btn114 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-warning w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'Далее'

            if local_flags[3] == '3.2':
                local_stages[stage][1].next = 'a9'
            elif local_flags[3] == '3.3':
                local_stages[stage][1].next = 'a9.1'            


        elif local_progress[stage]['1'] == True and local_progress[stage]['4'] == True:
            local_stages[stage][1].attr['buttons']['left']['styles'][0] = f'btn btn-lg btn-danger btn111 w-100'
            local_stages[stage][1].attr['buttons']['left']['styles'][1] = f'btn btn-lg btn-outline-danger btn113 w-100'
            local_stages[stage][1].attr['buttons']['right']['styles'][0] = f'btn btn-lg btn-outline-success btn112 w-100'
            local_stages[stage][1].attr['buttons']['right']['styles'][1] = f'btn btn-lg btn-success btn114 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-warning w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'Далее'
            local_stages[stage][1].next = 'a3.2'

        elif local_progress[stage]['2'] == True and local_progress[stage]['4'] == True:
            local_stages[stage][1].attr['buttons']['left']['styles'][0] = f'btn btn-lg btn-outline-danger btn111 w-100'
            local_stages[stage][1].attr['buttons']['left']['styles'][1] = f'btn btn-lg btn-outline-danger btn113 w-100'
            local_stages[stage][1].attr['buttons']['right']['styles'][0] = f'btn btn-lg btn-success btn112 w-100'
            local_stages[stage][1].attr['buttons']['right']['styles'][1] = f'btn btn-lg btn-success btn114 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-success w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'Далее'
            local_stages[stage][1].next = 'd10.1'

    if local_stages[stage][0] == 'b11':

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

        if  local_progress[stage]['1'] == True and local_progress[stage]['3'] == True:
            local_stages[stage][1].attr['buttons']['left']['styles'][0] = f'btn btn-lg btn-danger btn111 w-100'
            local_stages[stage][1].attr['buttons']['left']['styles'][1] = f'btn btn-lg btn-danger btn113 w-100'
            local_stages[stage][1].attr['buttons']['right']['styles'][0] = f'btn btn-lg btn-outline-success btn112 w-100'
            local_stages[stage][1].attr['buttons']['right']['styles'][1] = f'btn btn-lg btn-outline-success btn114 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-warning w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'Далее'

            if local_flags[3] == '3.2':
                local_stages[stage][1].next = 'a9'
            elif local_flags[3] == '3.3':
                local_stages[stage][1].next = 'a9.1'

        elif local_progress[stage]['2'] == True and local_progress[stage]['3'] == True:
            local_stages[stage][1].attr['buttons']['left']['styles'][0] = f'btn btn-lg btn-outline-danger btn111 w-100'
            local_stages[stage][1].attr['buttons']['left']['styles'][1] = f'btn btn-lg btn-danger btn113 w-100'
            local_stages[stage][1].attr['buttons']['right']['styles'][0] = f'btn btn-lg btn-success btn112 w-100'
            local_stages[stage][1].attr['buttons']['right']['styles'][1] = f'btn btn-lg btn-outline-success btn114 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-warning w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'Далее'

            if local_flags[3] == '3.2':
                local_stages[stage][1].next = 'a9'
            elif local_flags[3] == '3.3':
                local_stages[stage][1].next = 'a9.1'            


        elif local_progress[stage]['1'] == True and local_progress[stage]['4'] == True:
            local_stages[stage][1].attr['buttons']['left']['styles'][0] = f'btn btn-lg btn-danger btn111 w-100'
            local_stages[stage][1].attr['buttons']['left']['styles'][1] = f'btn btn-lg btn-outline-danger btn113 w-100'
            local_stages[stage][1].attr['buttons']['right']['styles'][0] = f'btn btn-lg btn-outline-success btn112 w-100'
            local_stages[stage][1].attr['buttons']['right']['styles'][1] = f'btn btn-lg btn-success btn114 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-warning w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'Далее'
            local_stages[stage][1].next = 'a3.2'

        elif local_progress[stage]['2'] == True and local_progress[stage]['4'] == True:
            local_stages[stage][1].attr['buttons']['left']['styles'][0] = f'btn btn-lg btn-outline-danger btn111 w-100'
            local_stages[stage][1].attr['buttons']['left']['styles'][1] = f'btn btn-lg btn-outline-danger btn113 w-100'
            local_stages[stage][1].attr['buttons']['right']['styles'][0] = f'btn btn-lg btn-success btn112 w-100'
            local_stages[stage][1].attr['buttons']['right']['styles'][1] = f'btn btn-lg btn-success btn114 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-success w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'Далее'
            local_stages[stage][1].next = 'e10.1'

    if local_stages[stage][0] == 'a15':

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

        if  local_progress[stage]['1'] == True and local_progress[stage]['3'] == True:
            local_stages[stage][1].attr['buttons']['left']['styles'][0] = f'btn btn-lg btn-success btn151 w-100'
            local_stages[stage][1].attr['buttons']['left']['styles'][1] = f'btn btn-lg btn-success btn153 w-100'
            local_stages[stage][1].attr['buttons']['right']['styles'][0] = f'btn btn-lg btn-outline-danger btn152 w-100'
            local_stages[stage][1].attr['buttons']['right']['styles'][1] = f'btn btn-lg btn-outline-danger btn154 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-success w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'Далее'

            ###
            if local_flags[3] == '3.2':
                local_stages[stage][1].next = 'a9'
            elif local_flags[3] == '3.3':
                local_stages[stage][1].next = 'a9.1'
            ###

            local_flags[15] = '15.1'

        elif local_progress[stage]['2'] == True and local_progress[stage]['3'] == True:
            local_stages[stage][1].attr['buttons']['left']['styles'][0] = f'btn btn-lg btn-outline-success btn151 w-100'
            local_stages[stage][1].attr['buttons']['left']['styles'][1] = f'btn btn-lg btn-success btn153 w-100'
            local_stages[stage][1].attr['buttons']['right']['styles'][0] = f'btn btn-lg btn-danger btn152 w-100'
            local_stages[stage][1].attr['buttons']['right']['styles'][1] = f'btn btn-lg btn-outline-danger btn154 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-warning w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'Далее'
            local_stages[stage][1].next = 'a16'
            local_flags[15] = '15.3'

        elif local_progress[stage]['1'] == True and local_progress[stage]['4'] == True:
            local_stages[stage][1].attr['buttons']['left']['styles'][0] = f'btn btn-lg btn-success btn151 w-100'
            local_stages[stage][1].attr['buttons']['left']['styles'][1] = f'btn btn-lg btn-outline-success btn153 w-100'
            local_stages[stage][1].attr['buttons']['right']['styles'][0] = f'btn btn-lg btn-outline-danger btn152 w-100'
            local_stages[stage][1].attr['buttons']['right']['styles'][1] = f'btn btn-lg btn-danger btn154 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-success w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'Далее'
            local_stages[stage][1].next = 'a17'
            local_flags[15] = '15.2'

        elif local_progress[stage]['2'] == True and local_progress[stage]['4'] == True:
            local_stages[stage][1].attr['buttons']['left']['styles'][0] = f'btn btn-lg btn-outline-success btn151 w-100'
            local_stages[stage][1].attr['buttons']['left']['styles'][1] = f'btn btn-lg btn-outline-success btn153 w-100'
            local_stages[stage][1].attr['buttons']['right']['styles'][0] = f'btn btn-lg btn-danger btn152 w-100'
            local_stages[stage][1].attr['buttons']['right']['styles'][1] = f'btn btn-lg btn-danger btn154 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-warning w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'Далее'
            local_stages[stage][1].next = 'b17'
            local_flags[15] = '15.4'

    navigation.append((local_stages[stage][1].attr['navigation']['styles'][1], local_stages[stage][1].attr['navigation']['text'][1], local_stages[stage][1].attr['navigation']['links'][1]))
    navigation.append((local_stages[stage][1].attr['navigation']['styles'][2], local_stages[stage][1].attr['navigation']['text'][2], local_stages[stage][1].attr['navigation']['links'][2]))

    for i in range(int(len(local_progress[stage].keys())//2)):
        data.append((local_stages[stage][1].attr['info']['styles'][i], local_stages[stage][1].attr['info']['text'][i], local_stages[stage][1].attr['buttons']['left']['styles'][i], local_stages[stage][1].attr['buttons']['left']['text'][i], local_stages[stage][1].attr['buttons']['right']['styles'][i], local_stages[stage][1].attr['buttons']['right']['text'][i]))

    return render_template("test3.html", data=data, navigation=navigation)


@app.route("/test_fourth", methods = ['GET', 'POST'])
def test_fourth():

    global local_progress, local_stages, stage, local_flags

    if local_stages[stage][1].attr['base_url'] != "test_fourth":
        return redirect('/prev_stage')

    info, data, navigation = [], [], []
    navigation.append((local_stages[stage][1].attr['navigation']['styles'][0], local_stages[stage][1].attr['navigation']['text'][0], local_stages[stage][1].attr['navigation']['links'][0]))

    if local_stages[stage][0] == 'a3.2':

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

        if local_progress[stage]['1'] == True:
            local_stages[stage][1].attr['buttons']['styles'][0] = f'btn btn-lg btn-danger btn3321 w-100'
            local_stages[stage][1].attr['buttons']['styles'][1] = f'btn btn-lg btn-outline-success btn3322 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-danger w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'SOS. Оценить дыхание!'
            local_stages[stage][1].next = 'a4'
            local_flags[3.2] = '3.4'
   
        elif local_progress[stage]['2'] == True:
            local_stages[stage][1].attr['buttons']['styles'][0] = f'btn btn-lg btn-outline-danger btn3321 w-100'
            local_stages[stage][1].attr['buttons']['styles'][1] = f'btn btn-lg btn-success btn3322 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-success w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'Далее'
            local_stages[stage][1].next = 'a4'
            local_flags[3.2] = '3.5'

    elif local_stages[stage][0] == 'a4':

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

        if local_progress[stage]['1'] == True:
            local_stages[stage][1].attr['buttons']['styles'][0] = f'btn btn-lg btn-success btn41 w-100'
            local_stages[stage][1].attr['buttons']['styles'][1] = f'btn btn-lg btn-outline-warning btn42 w-100'
            local_stages[stage][1].attr['buttons']['styles'][2] = f'btn btn-lg btn-outline-warning btn43 w-100'
            local_stages[stage][1].attr['buttons']['styles'][3] = f'btn btn-lg btn-outline-danger btn44 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-success w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'Далее'

            print(local_stages[stage][1].next)
            if local_flags[3] == '3.2':
                local_stages[stage][1].next = 'a9'###
            elif local_flags[3] == '3.3':
                local_stages[stage][1].next = 'a9.1'###
            print(local_stages[stage][1].next)

            local_flags[4] = '4.1'
   
        elif local_progress[stage]['2'] == True:
            local_stages[stage][1].attr['buttons']['styles'][0] = f'btn btn-lg btn-outline-success btn41 w-100'
            local_stages[stage][1].attr['buttons']['styles'][1] = f'btn btn-lg btn-warning btn42 w-100'
            local_stages[stage][1].attr['buttons']['styles'][2] = f'btn btn-lg btn-outline-warning btn43 w-100'
            local_stages[stage][1].attr['buttons']['styles'][3] = f'btn btn-lg btn-outline-danger btn44 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-warning w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'SOS. Обеспечение проходимости дыхательных путей'
            local_stages[stage][1].next = 'a13.2'
            local_flags[4] = '4.2'

        elif local_progress[stage]['3'] == True:
            local_stages[stage][1].attr['buttons']['styles'][0] = f'btn btn-lg btn-outline-success btn41 w-100'
            local_stages[stage][1].attr['buttons']['styles'][1] = f'btn btn-lg btn-outline-warning btn42 w-100'
            local_stages[stage][1].attr['buttons']['styles'][2] = f'btn btn-lg btn-warning btn43 w-100'
            local_stages[stage][1].attr['buttons']['styles'][3] = f'btn btn-lg btn-outline-danger btn44 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-warning w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'SOS. Дыхательная недостаточность'
            local_stages[stage][1].next = 'a5'
            local_flags[4] = '4.3'

        elif local_progress[stage]['4'] == True:
            local_stages[stage][1].attr['buttons']['styles'][0] = f'btn btn-lg btn-outline-success btn41 w-100'
            local_stages[stage][1].attr['buttons']['styles'][1] = f'btn btn-lg btn-outline-warning btn42 w-100'
            local_stages[stage][1].attr['buttons']['styles'][2] = f'btn btn-lg btn-outline-warning btn43 w-100'
            local_stages[stage][1].attr['buttons']['styles'][3] = f'btn btn-lg btn-danger btn44 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-danger w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'SOS. Реанимация!!!'

            ###
            local_stages[stage][1].next = 'a12'
            ###

            local_flags[4] = '4.4'

    elif local_stages[stage][0] == 'b4':

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

        if local_progress[stage]['1'] == True:
            local_stages[stage][1].attr['buttons']['styles'][0] = f'btn btn-lg btn-success btn41 w-100'
            local_stages[stage][1].attr['buttons']['styles'][1] = f'btn btn-lg btn-outline-warning btn42 w-100'
            local_stages[stage][1].attr['buttons']['styles'][2] = f'btn btn-lg btn-outline-warning btn43 w-100'
            local_stages[stage][1].attr['buttons']['styles'][3] = f'btn btn-lg btn-outline-danger btn44 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-success w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'Далее'

            ###
            if local_flags[3] == '3.2':
                local_stages[stage][1].next = 'a9'
            elif local_flags[3] == '3.3':
                local_stages[stage][1].next = 'a9.1'
            ###

            local_flags[4] = '4.1'
   
        elif local_progress[stage]['2'] == True:
            local_stages[stage][1].attr['buttons']['styles'][0] = f'btn btn-lg btn-outline-success btn41 w-100'
            local_stages[stage][1].attr['buttons']['styles'][1] = f'btn btn-lg btn-warning btn42 w-100'
            local_stages[stage][1].attr['buttons']['styles'][2] = f'btn btn-lg btn-outline-warning btn43 w-100'
            local_stages[stage][1].attr['buttons']['styles'][3] = f'btn btn-lg btn-outline-danger btn44 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-warning w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'SOS. Обеспечение проходимости дыхательных путей'
            local_stages[stage][1].next = 'a13.2'
            local_flags[4] = '4.2'

        elif local_progress[stage]['3'] == True:
            local_stages[stage][1].attr['buttons']['styles'][0] = f'btn btn-lg btn-outline-success btn41 w-100'
            local_stages[stage][1].attr['buttons']['styles'][1] = f'btn btn-lg btn-outline-warning btn42 w-100'
            local_stages[stage][1].attr['buttons']['styles'][2] = f'btn btn-lg btn-warning btn43 w-100'
            local_stages[stage][1].attr['buttons']['styles'][3] = f'btn btn-lg btn-outline-danger btn44 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-warning w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'SOS. Дыхательная недостаточность'
            
            ###
            if local_flags[3] == '3.2':
                local_stages[stage][1].next = 'a9'
            elif local_flags[3] == '3.3':
                local_stages[stage][1].next = 'a9.1'
            ###

            local_flags[4] = '4.3'

        elif local_progress[stage]['4'] == True:
            local_stages[stage][1].attr['buttons']['styles'][0] = f'btn btn-lg btn-outline-success btn41 w-100'
            local_stages[stage][1].attr['buttons']['styles'][1] = f'btn btn-lg btn-outline-warning btn42 w-100'
            local_stages[stage][1].attr['buttons']['styles'][2] = f'btn btn-lg btn-outline-warning btn43 w-100'
            local_stages[stage][1].attr['buttons']['styles'][3] = f'btn btn-lg btn-danger btn44 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-danger w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'SOS. Реанимация!!!'
            local_stages[stage][1].next = 'a12'
            local_flags[4] = '4.4'

    elif local_stages[stage][0] == 'c4':

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

        if local_progress[stage]['1'] == True:
            local_stages[stage][1].attr['buttons']['styles'][0] = f'btn btn-lg btn-success btn41 w-100'
            local_stages[stage][1].attr['buttons']['styles'][1] = f'btn btn-lg btn-outline-warning btn42 w-100'
            local_stages[stage][1].attr['buttons']['styles'][2] = f'btn btn-lg btn-outline-warning btn43 w-100'
            local_stages[stage][1].attr['buttons']['styles'][3] = f'btn btn-lg btn-outline-danger btn44 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-success w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'Далее'

            ###
            if local_flags[3] == '3.2':
                local_stages[stage][1].next = 'a9'
            elif local_flags[3] == '3.3':
                local_stages[stage][1].next = 'a9.1'
            ###

            local_flags[4] = '4.1'
   
        elif local_progress[stage]['2'] == True:
            local_stages[stage][1].attr['buttons']['styles'][0] = f'btn btn-lg btn-outline-success btn41 w-100'
            local_stages[stage][1].attr['buttons']['styles'][1] = f'btn btn-lg btn-warning btn42 w-100'
            local_stages[stage][1].attr['buttons']['styles'][2] = f'btn btn-lg btn-outline-warning btn43 w-100'
            local_stages[stage][1].attr['buttons']['styles'][3] = f'btn btn-lg btn-outline-danger btn44 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-warning w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'SOS. Обеспечение проходимости дыхательных путей'

            ###
            local_stages[stage][1].next = 'a13.2'
            ###

            local_flags[4] = '4.2'

        elif local_progress[stage]['3'] == True:
            local_stages[stage][1].attr['buttons']['styles'][0] = f'btn btn-lg btn-outline-success btn41 w-100'
            local_stages[stage][1].attr['buttons']['styles'][1] = f'btn btn-lg btn-outline-warning btn42 w-100'
            local_stages[stage][1].attr['buttons']['styles'][2] = f'btn btn-lg btn-warning btn43 w-100'
            local_stages[stage][1].attr['buttons']['styles'][3] = f'btn btn-lg btn-outline-danger btn44 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-warning w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'SOS. Дыхательная недостаточность'
            local_stages[stage][1].next = 'a5'
            local_flags[4] = '4.3'

        elif local_progress[stage]['4'] == True:
            local_stages[stage][1].attr['buttons']['styles'][0] = f'btn btn-lg btn-outline-success btn41 w-100'
            local_stages[stage][1].attr['buttons']['styles'][1] = f'btn btn-lg btn-outline-warning btn42 w-100'
            local_stages[stage][1].attr['buttons']['styles'][2] = f'btn btn-lg btn-outline-warning btn43 w-100'
            local_stages[stage][1].attr['buttons']['styles'][3] = f'btn btn-lg btn-danger btn44 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-danger w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'SOS. Реанимация!!!'
            local_stages[stage][1].next = 'a12'
            local_flags[4] = '4.4'

    elif local_stages[stage][0] == 'a5':

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

        if local_progress[stage]['1'] == True:
            local_stages[stage][1].attr['buttons']['styles'][0] = f'btn btn-lg btn-warning btn51 w-100'
            local_stages[stage][1].attr['buttons']['styles'][1] = f'btn btn-lg btn-outline-warning btn52 w-100'
            local_stages[stage][1].attr['buttons']['styles'][2] = f'btn btn-lg btn-outline-warning btn53 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-warning w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'SOS. Отёк гортани'
            local_stages[stage][1].next = 'a23'
            local_flags[5] = '5.1'
   
        elif local_progress[stage]['2'] == True:
            local_stages[stage][1].attr['buttons']['styles'][0] = f'btn btn-lg btn-outline-warning btn51 w-100'
            local_stages[stage][1].attr['buttons']['styles'][1] = f'btn btn-lg btn-warning btn52 w-100'
            local_stages[stage][1].attr['buttons']['styles'][2] = f'btn btn-lg btn-outline-warning btn53 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-warning w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'SOS. Бронхообструкция'
            local_stages[stage][1].next = 'b23'
            local_flags[5] = '5.2'

        elif local_progress[stage]['3'] == True:
            local_stages[stage][1].attr['buttons']['styles'][0] = f'btn btn-lg btn-outline-warning btn51 w-100'
            local_stages[stage][1].attr['buttons']['styles'][1] = f'btn btn-lg btn-outline-warning btn52 w-100'
            local_stages[stage][1].attr['buttons']['styles'][2] = f'btn btn-lg btn-warning btn53 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-warning w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'SOS. Отёк лёгких'
            local_stages[stage][1].next = 'c23'
            local_flags[5] = '5.3'

    elif local_stages[stage][0] == '6':

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

        if local_progress[stage]['1'] == True:
            local_stages[stage][1].attr['buttons']['styles'][0] = f'btn btn-lg btn-success btn61 w-100'
            local_stages[stage][1].attr['buttons']['styles'][1] = f'btn btn-lg btn-outline-danger btn62 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-success w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'Далее'
   
        elif local_progress[stage]['2'] == True:
            local_stages[stage][1].attr['buttons']['styles'][0] = f'btn btn-lg btn-outline-success btn61 w-100'
            local_stages[stage][1].attr['buttons']['styles'][1] = f'btn btn-lg btn-danger btn62 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-danger w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'SOS. Реанимация!!!'

    if local_stages[stage][0] == 'a8':

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

        #local_stages[current_stage].attr['navigation']['styles'][1] = 'btn btn-lg btn-outline-danger w-100 btn-next'
        #local_stages[current_stage].attr['navigation']['text'][1] = 'Далее'

        for i in range(len(local_stages[stage][1].attr['buttons']['text'])):
            local_stages[stage][1].attr['buttons']['text'][i] += f'test {body_params()}'

        if local_progress[stage]['1'] == True:
            local_stages[stage][1].attr['buttons']['styles'][0] = f'btn btn-lg btn-success btn81 w-100'
            local_stages[stage][1].attr['buttons']['styles'][1] = f'btn btn-lg btn-outline-warning btn82 w-100'
            local_stages[stage][1].attr['buttons']['styles'][2] = f'btn btn-lg btn-outline-warning btn83 w-100'
            local_stages[stage][1].attr['buttons']['styles'][3] = f'btn btn-lg btn-outline-danger btn84 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-success w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'Далее'
            local_stages[stage][1].next = 'a13.3'
 
   
        elif local_progress[stage]['2'] == True:
            local_stages[stage][1].attr['buttons']['styles'][0] = f'btn btn-lg btn-outline-success btn81 w-100'
            local_stages[stage][1].attr['buttons']['styles'][1] = f'btn btn-lg btn-warning btn82 w-100'
            local_stages[stage][1].attr['buttons']['styles'][2] = f'btn btn-lg btn-outline-warning btn83 w-100'
            local_stages[stage][1].attr['buttons']['styles'][3] = f'btn btn-lg btn-outline-danger btn84 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-warning w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'SOS. Гипертонический криз'
            local_stages[stage][1].next = 'a13.3'###
            

        elif local_progress[stage]['3'] == True:
            local_stages[stage][1].attr['buttons']['styles'][0] = f'btn btn-lg btn-outline-success btn81 w-100'
            local_stages[stage][1].attr['buttons']['styles'][1] = f'btn btn-lg btn-outline-warning btn82 w-100'
            local_stages[stage][1].attr['buttons']['styles'][2] = f'btn btn-lg btn-warning btn83 w-100'
            local_stages[stage][1].attr['buttons']['styles'][3] = f'btn btn-lg btn-outline-danger btn84 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-warning w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'SOS. Артериальная гипотония'
            local_stages[stage][1].next = 'c13.1'


        elif local_progress[stage]['4'] == True:
            local_stages[stage][1].attr['buttons']['styles'][0] = f'btn btn-lg btn-outline-success btn81 w-100'
            local_stages[stage][1].attr['buttons']['styles'][1] = f'btn btn-lg btn-outline-warning btn82 w-100'
            local_stages[stage][1].attr['buttons']['styles'][2] = f'btn btn-lg btn-outline-warning btn83 w-100'
            local_stages[stage][1].attr['buttons']['styles'][3] = f'btn btn-lg btn-danger btn84 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-danger w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'SOS. Реанимация!!!'
            local_stages[stage][1].next = 'c13.1'###


    if local_stages[stage][0] == 'b8':

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

        #local_stages[current_stage].attr['navigation']['styles'][1] = 'btn btn-lg btn-outline-danger w-100 btn-next'
        #local_stages[current_stage].attr['navigation']['text'][1] = 'Далее'

        for i in range(len(local_stages[stage][1].attr['buttons']['text'])):
            local_stages[stage][1].attr['buttons']['text'][i] += f'test {body_params()}'

        if local_progress[stage]['1'] == True:
            local_stages[stage][1].attr['buttons']['styles'][0] = f'btn btn-lg btn-success btn81 w-100'
            local_stages[stage][1].attr['buttons']['styles'][1] = f'btn btn-lg btn-outline-warning btn82 w-100'
            local_stages[stage][1].attr['buttons']['styles'][2] = f'btn btn-lg btn-outline-warning btn83 w-100'
            local_stages[stage][1].attr['buttons']['styles'][3] = f'btn btn-lg btn-outline-danger btn84 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-success w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'Далее'
            local_stages[stage][1].next = 'c18'
 
   
        elif local_progress[stage]['2'] == True:
            local_stages[stage][1].attr['buttons']['styles'][0] = f'btn btn-lg btn-outline-success btn81 w-100'
            local_stages[stage][1].attr['buttons']['styles'][1] = f'btn btn-lg btn-warning btn82 w-100'
            local_stages[stage][1].attr['buttons']['styles'][2] = f'btn btn-lg btn-outline-warning btn83 w-100'
            local_stages[stage][1].attr['buttons']['styles'][3] = f'btn btn-lg btn-outline-danger btn84 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-warning w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'SOS. Гипертонический криз'
            local_stages[stage][1].next = 'a24.3'###
            

        elif local_progress[stage]['3'] == True:
            local_stages[stage][1].attr['buttons']['styles'][0] = f'btn btn-lg btn-outline-success btn81 w-100'
            local_stages[stage][1].attr['buttons']['styles'][1] = f'btn btn-lg btn-outline-warning btn82 w-100'
            local_stages[stage][1].attr['buttons']['styles'][2] = f'btn btn-lg btn-warning btn83 w-100'
            local_stages[stage][1].attr['buttons']['styles'][3] = f'btn btn-lg btn-outline-danger btn84 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-warning w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'SOS. Артериальная гипотония'
            local_stages[stage][1].next = 'c18'


        elif local_progress[stage]['4'] == True:
            local_stages[stage][1].attr['buttons']['styles'][0] = f'btn btn-lg btn-outline-success btn81 w-100'
            local_stages[stage][1].attr['buttons']['styles'][1] = f'btn btn-lg btn-outline-warning btn82 w-100'
            local_stages[stage][1].attr['buttons']['styles'][2] = f'btn btn-lg btn-outline-warning btn83 w-100'
            local_stages[stage][1].attr['buttons']['styles'][3] = f'btn btn-lg btn-danger btn84 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-danger w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'SOS. Реанимация!!!'
            local_stages[stage][1].next = 'a24.3'###

    if local_stages[stage][0] == 'c8':

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

        #local_stages[current_stage].attr['navigation']['styles'][1] = 'btn btn-lg btn-outline-danger w-100 btn-next'
        #local_stages[current_stage].attr['navigation']['text'][1] = 'Далее'

        for i in range(len(local_stages[stage][1].attr['buttons']['text'])):
            local_stages[stage][1].attr['buttons']['text'][i] += f'test {body_params()}'

        if local_progress[stage]['1'] == True:
            local_stages[stage][1].attr['buttons']['styles'][0] = f'btn btn-lg btn-success btn81 w-100'
            local_stages[stage][1].attr['buttons']['styles'][1] = f'btn btn-lg btn-outline-warning btn82 w-100'
            local_stages[stage][1].attr['buttons']['styles'][2] = f'btn btn-lg btn-outline-warning btn83 w-100'
            local_stages[stage][1].attr['buttons']['styles'][3] = f'btn btn-lg btn-outline-danger btn84 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-success w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'Далее'
            local_stages[stage][1].next = 'b13.3'
 
   
        elif local_progress[stage]['2'] == True:
            local_stages[stage][1].attr['buttons']['styles'][0] = f'btn btn-lg btn-outline-success btn81 w-100'
            local_stages[stage][1].attr['buttons']['styles'][1] = f'btn btn-lg btn-warning btn82 w-100'
            local_stages[stage][1].attr['buttons']['styles'][2] = f'btn btn-lg btn-outline-warning btn83 w-100'
            local_stages[stage][1].attr['buttons']['styles'][3] = f'btn btn-lg btn-outline-danger btn84 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-warning w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'SOS. Гипертонический криз'
            local_stages[stage][1].next = 'b13.3'###
            

        elif local_progress[stage]['3'] == True:
            local_stages[stage][1].attr['buttons']['styles'][0] = f'btn btn-lg btn-outline-success btn81 w-100'
            local_stages[stage][1].attr['buttons']['styles'][1] = f'btn btn-lg btn-outline-warning btn82 w-100'
            local_stages[stage][1].attr['buttons']['styles'][2] = f'btn btn-lg btn-warning btn83 w-100'
            local_stages[stage][1].attr['buttons']['styles'][3] = f'btn btn-lg btn-outline-danger btn84 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-warning w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'SOS. Артериальная гипотония'
            local_stages[stage][1].next = 'e13.1'


        elif local_progress[stage]['4'] == True:
            local_stages[stage][1].attr['buttons']['styles'][0] = f'btn btn-lg btn-outline-success btn81 w-100'
            local_stages[stage][1].attr['buttons']['styles'][1] = f'btn btn-lg btn-outline-warning btn82 w-100'
            local_stages[stage][1].attr['buttons']['styles'][2] = f'btn btn-lg btn-outline-warning btn83 w-100'
            local_stages[stage][1].attr['buttons']['styles'][3] = f'btn btn-lg btn-danger btn84 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-danger w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'SOS. Реанимация!!!'
            local_stages[stage][1].next = 'e13.1'###

    if local_stages[stage][0] == 'd8':

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

        #local_stages[current_stage].attr['navigation']['styles'][1] = 'btn btn-lg btn-outline-danger w-100 btn-next'
        #local_stages[current_stage].attr['navigation']['text'][1] = 'Далее'

        for i in range(len(local_stages[stage][1].attr['buttons']['text'])):
            local_stages[stage][1].attr['buttons']['text'][i] += f'test {body_params()}'

        if local_progress[stage]['1'] == True:
            local_stages[stage][1].attr['buttons']['styles'][0] = f'btn btn-lg btn-success btn81 w-100'
            local_stages[stage][1].attr['buttons']['styles'][1] = f'btn btn-lg btn-outline-warning btn82 w-100'
            local_stages[stage][1].attr['buttons']['styles'][2] = f'btn btn-lg btn-outline-warning btn83 w-100'
            local_stages[stage][1].attr['buttons']['styles'][3] = f'btn btn-lg btn-outline-danger btn84 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-success w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'Далее'
            local_stages[stage][1].next = 'd18'
 
   
        elif local_progress[stage]['2'] == True:
            local_stages[stage][1].attr['buttons']['styles'][0] = f'btn btn-lg btn-outline-success btn81 w-100'
            local_stages[stage][1].attr['buttons']['styles'][1] = f'btn btn-lg btn-warning btn82 w-100'
            local_stages[stage][1].attr['buttons']['styles'][2] = f'btn btn-lg btn-outline-warning btn83 w-100'
            local_stages[stage][1].attr['buttons']['styles'][3] = f'btn btn-lg btn-outline-danger btn84 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-warning w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'SOS. Гипертонический криз'
            local_stages[stage][1].next = 'a24.6'###
            

        elif local_progress[stage]['3'] == True:
            local_stages[stage][1].attr['buttons']['styles'][0] = f'btn btn-lg btn-outline-success btn81 w-100'
            local_stages[stage][1].attr['buttons']['styles'][1] = f'btn btn-lg btn-outline-warning btn82 w-100'
            local_stages[stage][1].attr['buttons']['styles'][2] = f'btn btn-lg btn-warning btn83 w-100'
            local_stages[stage][1].attr['buttons']['styles'][3] = f'btn btn-lg btn-outline-danger btn84 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-warning w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'SOS. Артериальная гипотония'
            local_stages[stage][1].next = 'd18'


        elif local_progress[stage]['4'] == True:
            local_stages[stage][1].attr['buttons']['styles'][0] = f'btn btn-lg btn-outline-success btn81 w-100'
            local_stages[stage][1].attr['buttons']['styles'][1] = f'btn btn-lg btn-outline-warning btn82 w-100'
            local_stages[stage][1].attr['buttons']['styles'][2] = f'btn btn-lg btn-outline-warning btn83 w-100'
            local_stages[stage][1].attr['buttons']['styles'][3] = f'btn btn-lg btn-danger btn84 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-danger w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'SOS. Реанимация!!!'
            local_stages[stage][1].next = 'a24.6'###


    elif local_stages[stage][0] == '18.1':

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

    elif local_stages[stage][0] == 'a19':

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

        if local_progress[stage]['1'] == True:
            local_stages[stage][1].attr['buttons']['styles'][0] = f'btn btn-lg btn-success btn191 w-100'
            local_stages[stage][1].attr['buttons']['styles'][1] = f'btn btn-lg btn-outline-danger btn192 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-success w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'Далее'
            local_stages[stage][1].next = 'a10.1'
   
        elif local_progress[stage]['2'] == True:
            local_stages[stage][1].attr['buttons']['styles'][0] = f'btn btn-lg btn-outline-success btn191 w-100'
            local_stages[stage][1].attr['buttons']['styles'][1] = f'btn btn-lg btn-danger btn192 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-success w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'Далее'
            local_stages[stage][1].next = 'a18'

    elif local_stages[stage][0] == 'b19':

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

        if local_progress[stage]['1'] == True:
            local_stages[stage][1].attr['buttons']['styles'][0] = f'btn btn-lg btn-success btn191 w-100'
            local_stages[stage][1].attr['buttons']['styles'][1] = f'btn btn-lg btn-outline-danger btn192 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-success w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'Далее'
            local_stages[stage][1].next = 'a10.1'
   
        elif local_progress[stage]['2'] == True:
            local_stages[stage][1].attr['buttons']['styles'][0] = f'btn btn-lg btn-outline-success btn191 w-100'
            local_stages[stage][1].attr['buttons']['styles'][1] = f'btn btn-lg btn-danger btn192 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-success w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'Далее'
            local_stages[stage][1].next = 'b20'

    elif local_stages[stage][0] == 'c19':

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

        if local_progress[stage]['1'] == True:
            local_stages[stage][1].attr['buttons']['styles'][0] = f'btn btn-lg btn-success btn191 w-100'
            local_stages[stage][1].attr['buttons']['styles'][1] = f'btn btn-lg btn-outline-danger btn192 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-success w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'Далее'
            local_stages[stage][1].next = 'a22'
   
        elif local_progress[stage]['2'] == True:
            local_stages[stage][1].attr['buttons']['styles'][0] = f'btn btn-lg btn-outline-success btn191 w-100'
            local_stages[stage][1].attr['buttons']['styles'][1] = f'btn btn-lg btn-danger btn192 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-success w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'Далее'
            local_stages[stage][1].next = 'c20'

    elif local_stages[stage][0] == 'd19':

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

        if local_progress[stage]['1'] == True:
            local_stages[stage][1].attr['buttons']['styles'][0] = f'btn btn-lg btn-success btn191 w-100'
            local_stages[stage][1].attr['buttons']['styles'][1] = f'btn btn-lg btn-outline-danger btn192 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-success w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'Далее'
            local_stages[stage][1].next = 'a22'
   
        elif local_progress[stage]['2'] == True:
            local_stages[stage][1].attr['buttons']['styles'][0] = f'btn btn-lg btn-outline-success btn191 w-100'
            local_stages[stage][1].attr['buttons']['styles'][1] = f'btn btn-lg btn-danger btn192 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-success w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'Далее'
            local_stages[stage][1].next = 'd20'

    elif local_stages[stage][0] == 'a22':

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

        if local_progress[stage]['1'] == True:
            local_stages[stage][1].attr['buttons']['styles'][0] = f'btn btn-lg btn-success btn221 w-100'
            local_stages[stage][1].attr['buttons']['styles'][1] = f'btn btn-lg btn-outline-danger btn222 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-success w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'Далее'
            local_stages[stage][1].next = 'b10.1'
   
        elif local_progress[stage]['2'] == True:
            local_stages[stage][1].attr['buttons']['styles'][0] = f'btn btn-lg btn-outline-success btn221 w-100'
            local_stages[stage][1].attr['buttons']['styles'][1] = f'btn btn-lg btn-danger btn222 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-success w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'Далее'
            local_stages[stage][1].next = 'b21'

    elif local_stages[stage][0] == 'b22':

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

        if local_progress[stage]['1'] == True:
            local_stages[stage][1].attr['buttons']['styles'][0] = f'btn btn-lg btn-success btn221 w-100'
            local_stages[stage][1].attr['buttons']['styles'][1] = f'btn btn-lg btn-outline-danger btn222 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-success w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'Далее'
            local_stages[stage][1].next = 'b10.1'
   
        elif local_progress[stage]['2'] == True:
            local_stages[stage][1].attr['buttons']['styles'][0] = f'btn btn-lg btn-outline-success btn221 w-100'
            local_stages[stage][1].attr['buttons']['styles'][1] = f'btn btn-lg btn-danger btn222 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-success w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'Далее'
            local_stages[stage][1].next = 'b21'

    elif local_stages[stage][0] == 'a23':

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

        if local_progress[stage]['1'] == True:
            local_stages[stage][1].attr['buttons']['styles'][0] = f'btn btn-lg btn-success btn231 w-100'
            local_stages[stage][1].attr['buttons']['styles'][1] = f'btn btn-lg btn-outline-danger btn232 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-success w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'Далее'
            local_stages[stage][1].next = 'b7'
            local_flags[23] = '23.1'
   
        elif local_progress[stage]['2'] == True:
            local_stages[stage][1].attr['buttons']['styles'][0] = f'btn btn-lg btn-outline-success btn231 w-100'
            local_stages[stage][1].attr['buttons']['styles'][1] = f'btn btn-lg btn-danger btn232 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-success w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'Далее'
            local_stages[stage][1].next = 'b13.1'
            local_flags[23] = '23.2'

    elif local_stages[stage][0] == 'b23':

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

        if local_progress[stage]['1'] == True:
            local_stages[stage][1].attr['buttons']['styles'][0] = f'btn btn-lg btn-success btn231 w-100'
            local_stages[stage][1].attr['buttons']['styles'][1] = f'btn btn-lg btn-outline-danger btn232 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-success w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'Далее'
            local_stages[stage][1].next = 'd7'
            local_flags[23] = '23.1'
   
        elif local_progress[stage]['2'] == True:
            local_stages[stage][1].attr['buttons']['styles'][0] = f'btn btn-lg btn-outline-success btn231 w-100'
            local_stages[stage][1].attr['buttons']['styles'][1] = f'btn btn-lg btn-danger btn232 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-success w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'Далее'
            local_stages[stage][1].next = 'd13.1'
            local_flags[23] = '23.2'

    elif local_stages[stage][0] == 'c23':

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

        if local_progress[stage]['1'] == True:
            local_stages[stage][1].attr['buttons']['styles'][0] = f'btn btn-lg btn-success btn231 w-100'
            local_stages[stage][1].attr['buttons']['styles'][1] = f'btn btn-lg btn-outline-danger btn232 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-success w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'Далее'
            local_stages[stage][1].next = 'f7'
            local_flags[23] = '23.1'
   
        elif local_progress[stage]['2'] == True:
            local_stages[stage][1].attr['buttons']['styles'][0] = f'btn btn-lg btn-outline-success btn231 w-100'
            local_stages[stage][1].attr['buttons']['styles'][1] = f'btn btn-lg btn-danger btn232 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-success w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'Далее'
            local_stages[stage][1].next = 'c13.1'
            local_flags[23] = '23.2'

    elif local_stages[stage][0] == 'a24':

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

        if local_progress[stage]['1'] == True:
            local_stages[stage][1].attr['buttons']['styles'][0] = f'btn btn-lg btn-success btn241 w-100'
            local_stages[stage][1].attr['buttons']['styles'][1] = f'btn btn-lg btn-outline-danger btn242 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-success w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'Далее'
            local_stages[stage][1].next = 'a24.4' 
            local_flags[24] = '24.1'
   
        elif local_progress[stage]['2'] == True:
            local_stages[stage][1].attr['buttons']['styles'][0] = f'btn btn-lg btn-outline-success btn241 w-100'
            local_stages[stage][1].attr['buttons']['styles'][1] = f'btn btn-lg btn-danger btn242 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-success w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'Далее'
            local_stages[stage][1].next = 'c18'    
            local_flags[24] = '24.2'

    elif local_stages[stage][0] == 'b24':

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

        if local_progress[stage]['1'] == True:
            local_stages[stage][1].attr['buttons']['styles'][0] = f'btn btn-lg btn-success btn241 w-100'
            local_stages[stage][1].attr['buttons']['styles'][1] = f'btn btn-lg btn-outline-danger btn242 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-success w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'Далее'
            local_stages[stage][1].next = 'a24.5' 
            local_flags[24] = '24.1'
   
        elif local_progress[stage]['2'] == True:
            local_stages[stage][1].attr['buttons']['styles'][0] = f'btn btn-lg btn-outline-success btn241 w-100'
            local_stages[stage][1].attr['buttons']['styles'][1] = f'btn btn-lg btn-danger btn242 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-success w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'Далее'
            local_stages[stage][1].next = 'd18'    
            local_flags[24] = '24.2'

    elif local_stages[stage][0] == 'a25':

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

        if local_progress[stage]['1'] == True:
            local_stages[stage][1].attr['buttons']['styles'][0] = f'btn btn-lg btn-success btn251 w-100'
            local_stages[stage][1].attr['buttons']['styles'][1] = f'btn btn-lg btn-outline-danger btn252 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-success w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'Далее'
            local_stages[stage][1].next = 'a10'
            local_flags[25] = '25.1'
   
        elif local_progress[stage]['2'] == True:
            local_stages[stage][1].attr['buttons']['styles'][0] = f'btn btn-lg btn-outline-success btn251 w-100'
            local_stages[stage][1].attr['buttons']['styles'][1] = f'btn btn-lg btn-danger btn252 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-success w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'Далее'
            local_stages[stage][1].next = 'c16'
            local_flags[25] = '25.2'

    elif local_stages[stage][0] == 'b25':

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

        if local_progress[stage]['1'] == True:
            local_stages[stage][1].attr['buttons']['styles'][0] = f'btn btn-lg btn-success btn251 w-100'
            local_stages[stage][1].attr['buttons']['styles'][1] = f'btn btn-lg btn-outline-danger btn252 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-success w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'Далее'
            local_stages[stage][1].next = 'a10'
            local_flags[25] = '25.1'
   
        elif local_progress[stage]['2'] == True:
            local_stages[stage][1].attr['buttons']['styles'][0] = f'btn btn-lg btn-outline-success btn251 w-100'
            local_stages[stage][1].attr['buttons']['styles'][1] = f'btn btn-lg btn-danger btn252 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-success w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'Далее'
            local_stages[stage][1].next = 'd16'
            local_flags[25] = '25.2'

    elif local_stages[stage][0] == 'c25':

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

        if local_progress[stage]['1'] == True:
            local_stages[stage][1].attr['buttons']['styles'][0] = f'btn btn-lg btn-success btn251 w-100'
            local_stages[stage][1].attr['buttons']['styles'][1] = f'btn btn-lg btn-outline-danger btn252 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-success w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'Далее'
            local_stages[stage][1].next = 'b10'
            local_flags[25] = '25.1'
   
        elif local_progress[stage]['2'] == True:
            local_stages[stage][1].attr['buttons']['styles'][0] = f'btn btn-lg btn-outline-success btn251 w-100'
            local_stages[stage][1].attr['buttons']['styles'][1] = f'btn btn-lg btn-danger btn252 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-success w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'Далее'
            local_stages[stage][1].next = 'e16'
            local_flags[25] = '25.2'

    elif local_stages[stage][0] == 'd25':

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

        if local_progress[stage]['1'] == True:
            local_stages[stage][1].attr['buttons']['styles'][0] = f'btn btn-lg btn-success btn251 w-100'
            local_stages[stage][1].attr['buttons']['styles'][1] = f'btn btn-lg btn-outline-danger btn252 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-success w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'Далее'
            local_stages[stage][1].next = 'b10'
            local_flags[25] = '25.1'
   
        elif local_progress[stage]['2'] == True:
            local_stages[stage][1].attr['buttons']['styles'][0] = f'btn btn-lg btn-outline-success btn251 w-100'
            local_stages[stage][1].attr['buttons']['styles'][1] = f'btn btn-lg btn-danger btn252 w-100'
            local_stages[stage][1].attr['navigation']['styles'][2] = 'btn btn-lg btn-success w-100 btn-next'
            local_stages[stage][1].attr['navigation']['text'][2] = 'Далее'
            local_stages[stage][1].next = 'f16'
            local_flags[25] = '25.2'

    info.append((local_stages[stage][1].attr['info']['styles'][0], local_stages[stage][1].attr['info']['text'][0]))
    for i in local_progress[stage].keys():
        data.append((local_stages[stage][1].attr['buttons']['styles'][int(i) - 1], local_stages[stage][1].attr['buttons']['text'][int(i) - 1]))
    navigation.append((local_stages[stage][1].attr['navigation']['styles'][1], local_stages[stage][1].attr['navigation']['text'][1], local_stages[stage][1].attr['navigation']['links'][1]))
    navigation.append((local_stages[stage][1].attr['navigation']['styles'][2], local_stages[stage][1].attr['navigation']['text'][2], local_stages[stage][1].attr['navigation']['links'][2]))

    return render_template("test4.html", info=info, data=data, navigation=navigation)


def run_app():
    app.run(debug=True)


if __name__ == "__main__":
    app.run(debug=True)