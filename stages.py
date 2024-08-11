import copy

class stage():
    def __init__(self, attr: dict, prev: str = None, next: str = None):
        self.prev = prev
        self.next = next
        self.attr = {'base_url': attr['base_url'],
                     'info': attr['info'],
                     'buttons': attr['buttons'],
                     'navigation': attr['navigation']}

    def copy(self):
        return copy.deepcopy(self)

progress = {'1': {'1': False, '2': False, '3': False, '4': False}, 
                  '2': {'1': False, '2': False, '3': False, '4': False, '5': False, '6': False, '7': False},
                  '3': {'1': False, '2': False, '3': False, '4': False},
                  '4': {'1': False, '2': False, '3': False, '4': False},
                  '5': {'1': False, '2': False, '3': False},
                  '6': {'1': False, '2': False},
                  '7': {'1': False, '2': False},
                  '8': {'1': False, '2': False, '3': False, '4': False},
                  '9': {'1': False, '2': False},
                  '10': {'1': False},
                  '11': {'1': False, '2': False, '3': False, '4': False},
                  '12': {'1': False, '2': False},
                  '13': {'1': False, '2': False},
                  '13.1': {'1': False},
                  '14': {'1': False, '2': False, '3': False},
                  '15': {'1': False, '2': False, '3': False, '4': False},
                  '16': {'1': False},
                  '17': {'1': False},
                  '18': {'1': False},
                  '18.1': {'1': False, '2': False},
                  '19': {'1': False, '2': False},
                  '20': {'1': False, '2': False},
                  '21': {'1': False, '2': False},
                  '22': {'1': False, '2': False},
                  }


stages = {'0': stage(prev='', next = '1', attr={'base_url': '',
                                                  'info': '',
                                                  'buttons': '',
                                                  'navigation': ''
                                                  }),

          '1': stage(prev='0', next = '2', attr={'base_url': 'test_first', 
                                                  'info': {'text': ['Человеку плохо, Вы в безопасности', 'Громко оповестить, вывести лишних', 'Вызвать СМП (телефон 103), назвать адрес, не класть трубку', 'Доставить укладку, дефибриллятор'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить', 'Выполнить', 'Выполнить', 'Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn2 w-100', 'btn btn-lg btn-outline-success btn3 w-100', 'btn btn-lg btn-outline-success btn4 w-100']}, 
                                                  'navigation': {'text': ['Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/next_stage']}
                                                  }),

          '2': stage(prev='1', next = '3', attr={'base_url': 'test_second', 
                                                 'info': {}, 
                                                 'buttons': {'text': ['Примерный возраст до 1 года Примерный вес до 10 кг', 'Примерный возраст 1-3 года Примерный вес 10-15 кг', 'Примерный возраст 3-7 лет Примерный вес 15-20 кг', 'Примерный возраст 7-10 лет Примерный вес 20-30 кг', 'Примерный возраст старше 10 лет Примерный вес 30-50 кг', 'Примерный возраст старше 10 лет Примерный вес 50-90 кг', 'Примерный возраст старше 10 лет Примерный вес более 90 кг'], 
                                                             'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn2 w-100', 'btn btn-lg btn-outline-success btn3 w-100', 'btn btn-lg btn-outline-success btn4 w-100', 'btn btn-lg btn-outline-success btn5 w-100', 'btn btn-lg btn-outline-success btn6 w-100', 'btn btn-lg btn-outline-success btn7 w-100']}, 
                                                 'navigation': {'text': ['В начало', 'Назад', 'Далее'], 
                                                                'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                 }),

          '3': stage(prev='2', next = '4', attr={'base_url': 'test_third', 
                                                 'info': {'text': ['Назвал своё имя. Ответил на вопрос: «Что беспокоит?» Отреагировал на мягкое «потрясывание» за плечи', 'Судороги'], 
                                                          'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                 'buttons':{'left': {'text': ['Да', 'Да'], 
                                                                     'styles': ['btn btn-lg btn-outline-success btn31 w-100', 'btn btn-lg btn-outline-danger btn33 w-100']}, 
                                                            'right': {'text': ['Нет', 'Нет'], 
                                                                      'styles': ['btn btn-lg btn-outline-danger btn32 w-100', 'btn btn-lg btn-outline-success btn34 w-100']}}, 
                                                 'navigation': {'text': ['В начало', 'Назад', 'Далее'], 
                                                                'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                 }),
          
          '4': stage(prev='3', next = '5', attr={'base_url': 'test_fourth', 
                                                 'info': {'text': ['Характер дыхания'], 
                                                          'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                 'buttons': {'text': ["Нормальное", "Нарушена проходимость", "Одышка", "Агональное или отсутствует"], 
                                                             'styles': ['btn btn-lg btn-outline-success btn41 w-100', 'btn btn-lg btn-outline-warning btn42 w-100', 'btn btn-lg btn-outline-warning btn43 w-100', 'btn btn-lg btn-outline-danger btn44 w-100']}, 
                                                 'navigation': {'text': ['В начало', 'Назад', 'Далее'], 
                                                                'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining align-middle', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                 }),

          '5': stage(prev='4', next = '6', attr={'base_url': 'test_fourth', 
                                                 'info': {'text': ['Что затруднено, характер хрипов?'], 
                                                          'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                 'buttons': {'text': ["Затруднен вдох,свистящие хрипы, осиплость голоса", "Затруднен выдох,  свистящие хрипы", "Затруднены вдох и выдох, влажные хрипы"], 
                                                             'styles': ['btn btn-lg btn-outline-warning btn51 w-100', 'btn btn-lg btn-outline-warning btn52 w-100', 'btn btn-lg btn-outline-warning btn53 w-100']}, 
                                                 'navigation': {'text': ['В начало', 'Назад', 'Далее'], 
                                                                'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                 }),

          '6': stage(prev='5', next = '7', attr={'base_url': 'test_fourth', 
                                                 'info': {'text': ['Пульс на сонной артерии'], 
                                                          'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                 'buttons': {'text': ["Отчетливый", "Резко ослаблен или отсутствует"], 
                                                             'styles': ['btn btn-lg btn-outline-success btn61 w-100', 'btn btn-lg btn-outline-danger btn62 w-100']}, 
                                                 'navigation': {'text': ['В начало', 'Назад', 'Далее'], 
                                                                'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                 }),

          '7': stage(prev='6', next = '8', attr={'base_url': 'test_first', 
                                                  'info': {'text': ['Подключите к пациенту пульсоксиметр', 'Подсоедините тонометр, измерьте артериальное давление'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить', 'Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn2 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }),

          '8': stage(prev='7', next = '9', attr={'base_url': 'test_fourth', 
                                                 'info': {'text': ['Артериальное давление'], 
                                                          'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                 'buttons': {'text': ["Нормальное", "Выше 180/120 мм.рт.ст", "Ниже 90/60 мм.рт.ст. у взрослого", "Не определяется"], 
                                                             'styles': ['btn btn-lg btn-outline-success btn81 w-100', 'btn btn-lg btn-outline-warning btn82 w-100', 'btn btn-lg btn-outline-warning btn83 w-100', 'btn btn-lg btn-outline-danger btn84 w-100']}, 
                                                 'navigation': {'text': ['В начало', 'Назад', 'Далее'], 
                                                                'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                 }),

          '9': stage(prev='7', next = '10', attr={'base_url': 'test_first', 
                                                  'info': {'text': ['Не помещайте пальцы в рот (за зубы) пациента', 'Ничего не давайте через рот/под язык до полного восстановления сознания! Не используйте нашатырный спирт!'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить', 'Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn2 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }),

          '10': stage(prev='9', next = '11', attr={'base_url': 'test_first', 
                                                  'info': {'text': ['Оценивайте дыхание, пульс и SpO2 непрерывно, измеряйте АД не реже раза в 5 минут'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }),

          '11': stage(prev='10', next = '12', attr={'base_url': 'test_third', 
                                                 'info': {'text': ['Нарушено дыхание?', 'Нарушены пульс, давление?'], 
                                                          'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                 'buttons':{'left': {'text': ['Да', 'Да'], 
                                                                     'styles': ['btn btn-lg btn-outline-danger btn111 w-100', 'btn btn-lg btn-outline-danger btn113 w-100']}, 
                                                            'right': {'text': ['Нет', 'Нет'], 
                                                                      'styles': ['btn btn-lg btn-outline-success btn112 w-100', 'btn btn-lg btn-outline-success btn114 w-100']}}, 
                                                 'navigation': {'text': ['В начало', 'Назад', 'Далее'], 
                                                                'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-warning w-100 btn-next disabled'],
                                                                'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                 }),

          '12': stage(prev='11', next = '13', attr={'base_url': 'test_first', 
                                                  'info': {'text': ['Откройте пути для эвакуации пациента. Передайте пациента бригаде скорой медицинской помощи, опишите детали произошедшего', 'Заполните медицинскую документацию'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить', 'Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn2 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }),

          '13': stage(prev='11', next = '13.1', attr={'base_url': 'test_first', 
                                                  'info': {'text': ['Уложите пациента на пол на спину', 'Удалите от пациента опасные предметы (пациента от предметов). Насильно не удерживайте пациента!!!'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить', 'Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn2 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }),

          '13.1': stage(prev='13', next = '14', attr={'base_url': 'test_first', 
                                                  'info': {'text': ['Уложите пациента на пол на спину с приподнятыми ногами'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }),

          '14': stage(prev='13.1', next = '15', attr={'base_url': 'test_first', 
                                                  'info': {'text': ['Запрокиньте назад голову (разогните в шейном отделе)', 'Откройте рот пациента', 'Выдвиньте нижнюю челюсть и удалите все видимые инородные тела'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить', 'Выполнить', 'Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn2 w-100', 'btn btn-lg btn-outline-success btn3 w-100', 'btn btn-lg btn-outline-success btn4 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }),

          '15': stage(prev='14', next = '16', attr={'base_url': 'test_third', 
                                                 'info': {'text': ['Проходимость дыхательных путей восстановилась, дыхание нормальное?', 'SpO2 более 92%?'], 
                                                          'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                 'buttons':{'left': {'text': ['Да', 'Да'], 
                                                                     'styles': ['btn btn-lg btn-outline-success btn151 w-100', 'btn btn-lg btn-outline-success btn153 w-100']}, 
                                                            'right': {'text': ['Нет', 'Нет'], 
                                                                      'styles': ['btn btn-lg btn-outline-danger btn152 w-100', 'btn btn-lg btn-outline-danger btn154 w-100']}}, 
                                                 'navigation': {'text': ['В начало', 'Назад', 'Далее'], 
                                                                'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-warning w-100 btn-next disabled'],
                                                                'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                 }),
          
          '16': stage(prev='15', next = '17', attr={'base_url': 'test_first', 
                                                  'info': {'text': ['Подключите к пациенту кислород'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }),

          '17': stage(prev='16', next = '18', attr={'base_url': 'test_first', 
                                                  'info': {'text': ['Установите воздуховод № или ларингеальную маску № '], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }),

          '18': stage(prev='17', next = '18.1', attr={'base_url': 'test_first', 
                                                  'info': {'text': ['Обеспечьте внутривенный/внутрикостный сосудистый доступ'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }),

          '18.1': stage(prev='18', next = '19', attr={'base_url': 'test_fourth', 
                                                 'info': {'text': ['Сосудистый доступ установлен?'], 
                                                          'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                 'buttons': {'text': ["Да", "Нет"], 
                                                             'styles': ['btn btn-lg btn-outline-success btn181 w-100', 'btn btn-lg btn-outline-danger btn182 w-100']}, 
                                                 'navigation': {'text': ['В начало', 'Назад', 'Далее'], 
                                                                'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                 }),

          '19': stage(prev='18.1', next = '20', attr={'base_url': 'test_fourth', 
                                                 'info': {'text': ['Сахар крови'], 
                                                          'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                 'buttons': {'text': ["Выше 3 ммоль/л", "Ниже 3 ммоль/л "], 
                                                             'styles': ['btn btn-lg btn-outline-success btn191 w-100', 'btn btn-lg btn-outline-danger btn192 w-100']}, 
                                                 'navigation': {'text': ['В начало', 'Назад', 'Далее'], 
                                                                'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                 }),

          '20': stage(prev='19', next = '21', attr={'base_url': 'test_first', 
                                                  'info': {'text': ['Поместите сахар/конфету за щёку пациента (не за зубы).При наличии доступа в вену – внутривенно мл 20% раствора глюкозы (ампулы 40% глюкозы развести пополам 0,9 % раствором NaCl)', 'Определите уровень сахара повторно через 5 минут'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить', 'Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn2 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }),

          '21': stage(prev='20', next = '22', attr={'base_url': 'test_first', 
                                                  'info': {'text': ['При наличии сосудистого доступа – введите внутривенно вальпроевую кислоту мл (15 мг/кг), либо мидазолам мл (0,3 мг/кг), либо диазепам мл (0,3-0,5 мг/кг)', 'При отсутствии сосудистого доступа внутримышечно ввести мидазолам мл (0,3 мг/кг), либо диазепам мл (0,3-0,5 мг/кг)'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить', 'Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn2 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }),

          '22': stage(prev='21', next = '23', attr={'base_url': 'test_fourth', 
                                                 'info': {'text': ['Судороги купированы?'], 
                                                          'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                 'buttons': {'text': ["Да", "Нет"], 
                                                             'styles': ['btn btn-lg btn-outline-success btn221 w-100', 'btn btn-lg btn-outline-danger btn222 w-100']}, 
                                                 'navigation': {'text': ['В начало', 'Назад', 'Далее'], 
                                                                'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                 }),

          '23': stage(prev='22', next = '24', attr={'base_url': 'test_fourth', 
                                                 'info': {'text': ['Пациент может выполнять команды?'], 
                                                          'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                 'buttons': {'text': ["Да", "Нет"], 
                                                             'styles': ['btn btn-lg btn-outline-success btn231 w-100', 'btn btn-lg btn-outline-danger btn232 w-100']}, 
                                                 'navigation': {'text': ['В начало', 'Назад', 'Далее'], 
                                                                'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                 }),

          '24': stage(prev='23', next = '24.3', attr={'base_url': 'test_fourth', 
                                                 'info': {'text': ['Небулайзер доступен?'], 
                                                          'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                 'buttons': {'text': ["Да", "Нет"], 
                                                             'styles': ['btn btn-lg btn-outline-success btn241 w-100', 'btn btn-lg btn-outline-danger btn242 w-100']}, 
                                                 'navigation': {'text': ['В начало', 'Назад', 'Далее'], 
                                                                'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                 }),

          '24.3': stage(prev='24', next = '24.4', attr={'base_url': 'test_first', 
                                                  'info': {'text': ['Введите внутривенно или (при отсутствии сосудистого доступа – внутримышечно)' + '\n' + '1. Эпинефрин (адреналин)мл' + '\n' + '2. Дексаметазон мл или Преднизолон мл или Метилпреднизолон мл или Гидрокортизон мл'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }),

          '24.4': stage(prev='24.3', next = '24.5', attr={'base_url': 'test_first', 
                                                  'info': {'text': ['Введите ингаляционно через небулайзер' + '\n' + '1. Будесонид мг + NaCl 0,9% 3 мл' + '\n' + '2. Адреналин мл + NaCl 0,9% 3 мл'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }),

          '24.5': stage(prev='24.4', next = '24.6', attr={'base_url': 'test_first', 
                                                  'info': {'text': ['Введите ингаляционно' + '\n' + '1. Сальбутамол доз'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }),

          '24.6': stage(prev='24.5', next = '24.7', attr={'base_url': 'test_first', 
                                                  'info': {'text': ['Введите внутривенно или (при отсутствии сосудистого доступа – внутримышечно)' + '\n' + '1. Аминофиллин (эуфиллин) мл' + '\n' + '2. Дексаметазон мл или Преднизолон мл или Метилпреднизолон мл или Гидрокортизон мл'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }),

          '24.7': stage(prev='24.6', next = '1', attr={'base_url': 'test_first', 
                                                  'info': {'text': ['1. Введите внутривенно  Нитроглицерин 10 мг в/в капельно При отсутствии сосудистого доступа дайте пациенту Нитроглицерин 0,4 мг под язык' + '\n' + '2. Введите внутривенно или (при отсутствии сосудистого доступа – внутримышечно) Морфин 1 % - 1 мл (при наличии) Фуросемид 40 мг (4 мл)'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }),

          '25': stage(prev='24.7', next = '1', attr={'base_url': 'test_fourth', 
                                                 'info': {'text': ['Дыхание, SpO2 нормализовались?'], 
                                                          'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                 'buttons': {'text': ["Да", "Нет"], 
                                                             'styles': ['btn btn-lg btn-outline-success btn251 w-100', 'btn btn-lg btn-outline-danger btn252 w-100']}, 
                                                 'navigation': {'text': ['В начало', 'Назад', 'Далее'], 
                                                                'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                 }),

          }