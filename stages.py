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
            '3.2': {'1': False, '2': False},
            '4': {'1': False, '2': False, '3': False, '4': False},
            '5': {'1': False, '2': False, '3': False},
            '6': {'1': False, '2': False},
            '7': {'1': False, '2': False},
            '8': {'1': False, '2': False, '3': False, '4': False},
            '9': {'1': False, '2': False},
            '9.1': {'1': False, '2': False},
            '10': {'1': False},
            '10.1': {'1': False},
            '11': {'1': False, '2': False, '3': False, '4': False},
            '12': {'1': False, '2': False},
            '13': {'1': False, '2': False},
            '13.1': {'1': False},
            '13.2': {'1': False},
            '13.3': {'1': False},
            '13.4': {'1': False},
            '14': {'1': False, '2': False, '3': False},
            '15': {'1': False, '2': False, '3': False, '4': False},
            '16': {'1': False},
            '17': {'1': False},
            '18': {'1': False},
            '18.1': {'1': False, '2': False},
            '18.2': {'1': False},
            '19': {'1': False, '2': False},
            '20': {'1': False, '2': False},
            '21': {'1': False, '2': False},
            '22': {'1': False, '2': False},
            '23': {'1': False, '2': False},
            '23.1': {'1': False, '2': False, '3': False, '4': False},
            '23.2': {'1': False, '2': False},
            '24': {'1': False, '2': False},
            '24.3': {'1': False},
            '24.4': {'1': False},
            '24.5': {'1': False},
            '24.6': {'1': False},
            '24.7': {'1': False},
            '24.8': {'1': False},
            '24.9': {'1': False},
            '24.10': {'1': False},
            '24.11': {'1': False},
            '24.12': {'1': False},
            '24.13': {'1': False},
            '25': {'1': False, '2': False},
            '26.1': {'1': False, '2': False},
            '26.2': {'1': False, '2': False},
            '26.3': {'1': False, '2': False},
            '26.4': {'1': False, '2': False},
            }


stages = {'a0': stage(prev='', next = 'a1', attr={'base_url': '',
                                                  'info': '',
                                                  'buttons': '',
                                                  'navigation': ''
                                                  }),

          'a1': stage(prev='a0', next = 'a2', attr={'base_url': 'test_first', 
                                                  'info': {'text': ['Человеку плохо, Вы в безопасности', 'Громко оповестить, вывести лишних', 'Вызвать СМП (телефон 103), назвать адрес, не класть трубку', 'Доставить укладку, дефибриллятор'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить', 'Выполнить', 'Выполнить', 'Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn2 w-100', 'btn btn-lg btn-outline-success btn3 w-100', 'btn btn-lg btn-outline-success btn4 w-100']}, 
                                                  'navigation': {'text': ['Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/next_stage']}
                                                  }),

          'a2': stage(prev='a1', next = 'a3', attr={'base_url': 'test_second', 
                                                 'info': {}, 
                                                 'buttons': {'text': ['Примерный возраст до 1 года Примерный вес до 10 кг', 'Примерный возраст 1-3 года Примерный вес 10-15 кг', 'Примерный возраст 3-7 лет Примерный вес 15-20 кг', 'Примерный возраст 7-10 лет Примерный вес 20-30 кг', 'Примерный возраст старше 10 лет Примерный вес 30-50 кг', 'Примерный возраст старше 10 лет Примерный вес 50-90 кг', 'Примерный возраст старше 10 лет Примерный вес более 90 кг'], 
                                                             'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn2 w-100', 'btn btn-lg btn-outline-success btn3 w-100', 'btn btn-lg btn-outline-success btn4 w-100', 'btn btn-lg btn-outline-success btn5 w-100', 'btn btn-lg btn-outline-success btn6 w-100', 'btn btn-lg btn-outline-success btn7 w-100']}, 
                                                 'navigation': {'text': ['В начало', 'Назад', 'Далее'], 
                                                                'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                 }),

          'a3': stage(prev='a2', next = None, attr={'base_url': 'test_third', 
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

          'a3.2': stage(prev='a3', next = None, attr={'base_url': 'test_fourth', 
                                                 'info': {'text': ['Генерализированные судороги'], 
                                                          'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                 'buttons': {'text': ["Да", "Нет"], 
                                                             'styles': ['btn btn-lg btn-outline-danger btn3321 w-100', 'btn btn-lg btn-outline-success btn3322 w-100']}, 
                                                 'navigation': {'text': ['В начало', 'Назад', 'Далее'], 
                                                                'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                 }),
          
          'a4': stage(prev='a3', next = None, attr={'base_url': 'test_fourth', 
                                                 'info': {'text': ['Характер дыхания'], 
                                                          'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                 'buttons': {'text': ["Нормальное", "Нарушена проходимость", "Одышка", "Агональное или отсутствует"], 
                                                             'styles': ['btn btn-lg btn-outline-success btn41 w-100', 'btn btn-lg btn-outline-warning btn42 w-100', 'btn btn-lg btn-outline-warning btn43 w-100', 'btn btn-lg btn-outline-danger btn44 w-100']}, 
                                                 'navigation': {'text': ['В начало', 'Назад', 'Далее'], 
                                                                'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining align-middle', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                 }),

          'b4': stage(prev='a3', next = None, attr={'base_url': 'test_fourth', 
                                                 'info': {'text': ['Характер дыхания'], 
                                                          'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                 'buttons': {'text': ["Нормальное", "Нарушена проходимость", "Одышка", "Агональное или отсутствует"], 
                                                             'styles': ['btn btn-lg btn-outline-success btn41 w-100', 'btn btn-lg btn-outline-warning btn42 w-100', 'btn btn-lg btn-outline-warning btn43 w-100', 'btn btn-lg btn-outline-danger btn44 w-100']}, 
                                                 'navigation': {'text': ['В начало', 'Назад', 'Далее'], 
                                                                'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining align-middle', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                 }),

          'c4': stage(prev='a3', next = None, attr={'base_url': 'test_fourth', 
                                                 'info': {'text': ['Характер дыхания'], 
                                                          'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                 'buttons': {'text': ["Нормальное", "Нарушена проходимость", "Одышка", "Агональное или отсутствует"], 
                                                             'styles': ['btn btn-lg btn-outline-success btn41 w-100', 'btn btn-lg btn-outline-warning btn42 w-100', 'btn btn-lg btn-outline-warning btn43 w-100', 'btn btn-lg btn-outline-danger btn44 w-100']}, 
                                                 'navigation': {'text': ['В начало', 'Назад', 'Далее'], 
                                                                'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining align-middle', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                 }),

          'a5': stage(prev='a4', next = None, attr={'base_url': 'test_fourth', 
                                                 'info': {'text': ['Что затруднено, характер хрипов?'], 
                                                          'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                 'buttons': {'text': ["Затруднен вдох,свистящие хрипы, осиплость голоса", "Затруднен выдох,  свистящие хрипы", "Затруднены вдох и выдох, влажные хрипы"], 
                                                             'styles': ['btn btn-lg btn-outline-warning btn51 w-100', 'btn btn-lg btn-outline-warning btn52 w-100', 'btn btn-lg btn-outline-warning btn53 w-100']}, 
                                                 'navigation': {'text': ['В начало', 'Назад', 'Далее'], 
                                                                'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                 }),

          '6': stage(prev='5', next = None, attr={'base_url': 'test_fourth', 
                                                 'info': {'text': ['Пульс на сонной артерии'], 
                                                          'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                 'buttons': {'text': ["Отчетливый", "Резко ослаблен или отсутствует"], 
                                                             'styles': ['btn btn-lg btn-outline-success btn61 w-100', 'btn btn-lg btn-outline-danger btn62 w-100']}, 
                                                 'navigation': {'text': ['В начало', 'Назад', 'Далее'], 
                                                                'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                 }),

          'a7': stage(prev='a14', next = 'a15', attr={'base_url': 'test_first', 
                                                  'info': {'text': ['Подключите к пациенту пульсоксиметр', 'Подсоедините тонометр, измерьте артериальное давление'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить', 'Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn2 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }),

          'b7': stage(prev='a23', next = 'a8', attr={'base_url': 'test_first', 
                                                  'info': {'text': ['Подключите к пациенту пульсоксиметр', 'Подсоедините тонометр, измерьте артериальное давление'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить', 'Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn2 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }),

          'c7': stage(prev='b13.1', next = 'b8', attr={'base_url': 'test_first', 
                                                  'info': {'text': ['Подключите к пациенту пульсоксиметр', 'Подсоедините тонометр, измерьте артериальное давление'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить', 'Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn2 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }),

          'd7': stage(prev='b23', next = 'c8', attr={'base_url': 'test_first', 
                                                  'info': {'text': ['Подключите к пациенту пульсоксиметр', 'Подсоедините тонометр, измерьте артериальное давление'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить', 'Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn2 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }),

          'e7': stage(prev='d13.1', next = 'd8', attr={'base_url': 'test_first', 
                                                  'info': {'text': ['Подключите к пациенту пульсоксиметр', 'Подсоедините тонометр, измерьте артериальное давление'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить', 'Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn2 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }),

          'f7': stage(prev='c23', next = 'e8', attr={'base_url': 'test_first', 
                                                  'info': {'text': ['Подключите к пациенту пульсоксиметр', 'Подсоедините тонометр, измерьте артериальное давление'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить', 'Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn2 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }),

          'g7': stage(prev='f13.1', next = 'f8', attr={'base_url': 'test_first', 
                                                  'info': {'text': ['Подключите к пациенту пульсоксиметр', 'Подсоедините тонометр, измерьте артериальное давление'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить', 'Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn2 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }),

          'a8': stage(prev='b7', next = None, attr={'base_url': 'test_fourth', 
                                                 'info': {'text': ['Артериальное давление'], 
                                                          'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                 'buttons': {'text': ["Нормальное", "Выше 180/120 мм.рт.ст", "Ниже 90/60 мм.рт.ст. у взрослого", "Не определяется"], 
                                                             'styles': ['btn btn-lg btn-outline-success btn81 w-100', 'btn btn-lg btn-outline-warning btn82 w-100', 'btn btn-lg btn-outline-warning btn83 w-100', 'btn btn-lg btn-outline-danger btn84 w-100']}, 
                                                 'navigation': {'text': ['В начало', 'Назад', 'Далее'], 
                                                                'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                 }),

          'b8': stage(prev='c7', next = None, attr={'base_url': 'test_fourth', 
                                                 'info': {'text': ['Артериальное давление'], 
                                                          'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                 'buttons': {'text': ["Нормальное", "Выше 180/120 мм.рт.ст", "Ниже 90/60 мм.рт.ст. у взрослого", "Не определяется"], 
                                                             'styles': ['btn btn-lg btn-outline-success btn81 w-100', 'btn btn-lg btn-outline-warning btn82 w-100', 'btn btn-lg btn-outline-warning btn83 w-100', 'btn btn-lg btn-outline-danger btn84 w-100']}, 
                                                 'navigation': {'text': ['В начало', 'Назад', 'Далее'], 
                                                                'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                 }),

          'c8': stage(prev='d7', next = None, attr={'base_url': 'test_fourth', 
                                                 'info': {'text': ['Артериальное давление'], 
                                                          'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                 'buttons': {'text': ["Нормальное", "Выше 180/120 мм.рт.ст", "Ниже 90/60 мм.рт.ст. у взрослого", "Не определяется"], 
                                                             'styles': ['btn btn-lg btn-outline-success btn81 w-100', 'btn btn-lg btn-outline-warning btn82 w-100', 'btn btn-lg btn-outline-warning btn83 w-100', 'btn btn-lg btn-outline-danger btn84 w-100']}, 
                                                 'navigation': {'text': ['В начало', 'Назад', 'Далее'], 
                                                                'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                 }),

          'd8': stage(prev='e7', next = None, attr={'base_url': 'test_fourth', 
                                                 'info': {'text': ['Артериальное давление'], 
                                                          'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                 'buttons': {'text': ["Нормальное", "Выше 180/120 мм.рт.ст", "Ниже 90/60 мм.рт.ст. у взрослого", "Не определяется"], 
                                                             'styles': ['btn btn-lg btn-outline-success btn81 w-100', 'btn btn-lg btn-outline-warning btn82 w-100', 'btn btn-lg btn-outline-warning btn83 w-100', 'btn btn-lg btn-outline-danger btn84 w-100']}, 
                                                 'navigation': {'text': ['В начало', 'Назад', 'Далее'], 
                                                                'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                 }),

          'e8': stage(prev='f7', next = None, attr={'base_url': 'test_fourth', 
                                                 'info': {'text': ['Артериальное давление'], 
                                                          'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                 'buttons': {'text': ["Нормальное", "Выше 180/120 мм.рт.ст", "Ниже 90/60 мм.рт.ст. у взрослого", "Не определяется"], 
                                                             'styles': ['btn btn-lg btn-outline-success btn81 w-100', 'btn btn-lg btn-outline-warning btn82 w-100', 'btn btn-lg btn-outline-warning btn83 w-100', 'btn btn-lg btn-outline-danger btn84 w-100']}, 
                                                 'navigation': {'text': ['В начало', 'Назад', 'Далее'], 
                                                                'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                 }),

          'f8': stage(prev='f7', next = None, attr={'base_url': 'test_fourth', 
                                                 'info': {'text': ['Артериальное давление'], 
                                                          'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                 'buttons': {'text': ["Нормальное", "Выше 180/120 мм.рт.ст", "Ниже 90/60 мм.рт.ст. у взрослого", "Не определяется"], 
                                                             'styles': ['btn btn-lg btn-outline-success btn81 w-100', 'btn btn-lg btn-outline-warning btn82 w-100', 'btn btn-lg btn-outline-warning btn83 w-100', 'btn btn-lg btn-outline-danger btn84 w-100']}, 
                                                 'navigation': {'text': ['В начало', 'Назад', 'Далее'], 
                                                                'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                 }),

          'a9': stage(prev='8', next = 'a19', attr={'base_url': 'test_first', 
                                                  'info': {'text': ['Не помещайте пальцы в рот (за зубы) пациента', 'Ничего не давайте через рот/под язык до полного восстановления сознания! Не используйте нашатырный спирт!'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить', 'Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn2 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }),

          'a9.1': stage(prev='a13.2', next = 'b18', attr={'base_url': 'test_first', 
                                                  'info': {'text': ['Не помещайте пальцы в рот (за зубы) пациента', 'Ничего не давайте через рот/под язык!'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить', 'Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn2 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }),

          'b9.1': stage(prev='a13.2', next = 'a14', attr={'base_url': 'test_first', 
                                                  'info': {'text': ['Не помещайте пальцы в рот (за зубы) пациента', 'Ничего не давайте через рот/под язык!'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить', 'Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn2 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }),

          'a10': stage(prev='9', next = 'a11', attr={'base_url': 'test_first', 
                                                  'info': {'text': ['Оценивайте дыхание, пульс и SpO2 непрерывно, измеряйте АД не реже раза в 5 минут'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }),

          'b10': stage(prev='9', next = 'b11', attr={'base_url': 'test_first', 
                                                  'info': {'text': ['Оценивайте дыхание, пульс и SpO2 непрерывно, измеряйте АД не реже раза в 5 минут'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }),

          'c10': stage(prev='a24.7', next = 'c11', attr={'base_url': 'test_first', 
                                                  'info': {'text': ['Оценивайте дыхание, пульс и SpO2 непрерывно, измеряйте АД не реже раза в 5 минут'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }),
            
          'a10.1': stage(prev='b20', next = 'a12', attr={'base_url': 'test_first', 
                                                  'info': {'text': ['Оценивайте дыхание, пульс и SpO2 непрерывно, измеряйте АД не реже раза в 5 минут). При нарушениях, развитии судорог нажмите «В начало»'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }),

          'b10.1': stage(prev='b19', next = 'a12', attr={'base_url': 'test_first', 
                                                  'info': {'text': ['Оценивайте дыхание, пульс и SpO2 непрерывно, измеряйте АД не реже раза в 5 минут). При нарушениях, развитии судорог нажмите «В начало»'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }),

          'c10.1': stage(prev='b19', next = 'a12', attr={'base_url': 'test_first', 
                                                  'info': {'text': ['Оценивайте дыхание, пульс и SpO2 непрерывно, измеряйте АД не реже раза в 5 минут). При нарушениях, развитии судорог нажмите «В начало»'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }),

          'd10.1': stage(prev='a11', next = 'b12', attr={'base_url': 'test_first', 
                                                  'info': {'text': ['Оценивайте дыхание, пульс и SpO2 непрерывно, измеряйте АД не реже раза в 5 минут). При нарушениях, развитии судорог нажмите «В начало»'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }),

          'e10.1': stage(prev='b11', next = 'c12', attr={'base_url': 'test_first', 
                                                  'info': {'text': ['Оценивайте дыхание, пульс и SpO2 непрерывно, измеряйте АД не реже раза в 5 минут). При нарушениях, развитии судорог нажмите «В начало»'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }),

          'f10.1': stage(prev='c11', next = 'd12', attr={'base_url': 'test_first', 
                                                  'info': {'text': ['Оценивайте дыхание, пульс и SpO2 непрерывно, измеряйте АД не реже раза в 5 минут). При нарушениях, развитии судорог нажмите «В начало»'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }),

          'a11': stage(prev='a10', next = None, attr={'base_url': 'test_third', 
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

          'b11': stage(prev='b10', next = None, attr={'base_url': 'test_third', 
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

          'c11': stage(prev='c10', next = None, attr={'base_url': 'test_third', 
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

          'a12': stage(prev='11', next = 'a13', attr={'base_url': 'test_first', 
                                                  'info': {'text': ['Откройте пути для эвакуации пациента. Передайте пациента бригаде скорой медицинской помощи, опишите детали произошедшего', 'Заполните медицинскую документацию'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить', 'Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn2 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }),

          'b12': stage(prev='d10.1', next = 'a13', attr={'base_url': 'test_first', 
                                                  'info': {'text': ['Откройте пути для эвакуации пациента. Передайте пациента бригаде скорой медицинской помощи, опишите детали произошедшего', 'Заполните медицинскую документацию'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить', 'Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn2 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }),

          'c12': stage(prev='e10.1', next = 'a13', attr={'base_url': 'test_first', 
                                                  'info': {'text': ['Откройте пути для эвакуации пациента. Передайте пациента бригаде скорой медицинской помощи, опишите детали произошедшего', 'Заполните медицинскую документацию'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить', 'Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn2 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }),

          'd12': stage(prev='f10.1', next = 'a13', attr={'base_url': 'test_first', 
                                                  'info': {'text': ['Откройте пути для эвакуации пациента. Передайте пациента бригаде скорой медицинской помощи, опишите детали произошедшего', 'Заполните медицинскую документацию'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить', 'Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn2 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }),

          'a13': stage(prev='a3', next = 'a3.2', attr={'base_url': 'test_first', 
                                                  'info': {'text': ['Уложите пациента на пол на спину', 'Удалите от пациента опасные предметы (пациента от предметов). Насильно не удерживайте пациента!!!'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить', 'Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn2 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }),

          'a13.1': stage(prev='a3', next = 'a3.2', attr={'base_url': 'test_first', 
                                                  'info': {'text': ['Уложите пациента на пол на спину с приподнятыми ногами'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }),

          'b13.1': stage(prev='a23', next = 'c7', attr={'base_url': 'test_first', 
                                                  'info': {'text': ['Уложите пациента на пол на спину с приподнятыми ногами'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }),

          'c13.1': stage(prev='a8', next = 'c18', attr={'base_url': 'test_first', 
                                                  'info': {'text': ['Уложите пациента на пол на спину с приподнятыми ногами'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }),

          'd13.1': stage(prev='b23', next = 'e7', attr={'base_url': 'test_first', 
                                                  'info': {'text': ['Уложите пациента на пол на спину с приподнятыми ногами'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }),

          'e13.1': stage(prev='c8', next = 'd18', attr={'base_url': 'test_first', 
                                                  'info': {'text': ['Уложите пациента на пол на спину с приподнятыми ногами'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }),

          'f13.1': stage(prev='c23', next = 'g7', attr={'base_url': 'test_first', 
                                                  'info': {'text': ['Уложите пациента на пол на спину с приподнятыми ногами'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }),

          'g13.1': stage(prev='e8', next = 'g16', attr={'base_url': 'test_first', 
                                                  'info': {'text': ['Уложите пациента на пол на спину с приподнятыми ногами'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }),

          'a13.2': stage(prev='a4', next = 'b9.1', attr={'base_url': 'test_first', 
                                                  'info': {'text': ['Уложите пациента на пол на спину'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }),

          'a13.3': stage(prev='a8', next = 'a24', attr={'base_url': 'test_first', 
                                                  'info': {'text': ['Усадите пациента'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }),

          'b13.3': stage(prev='c8', next = 'b24', attr={'base_url': 'test_first', 
                                                  'info': {'text': ['Усадите пациента'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }),

          'c13.3': stage(prev='e8', next = 'e18', attr={'base_url': 'test_first', 
                                                  'info': {'text': ['Усадите пациента'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }),

          '13.4': stage(prev='13.3', next = '14', attr={'base_url': 'test_first', 
                                                  'info': {'text': ['Уложите пациента на кушетку'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }),

          'a14': stage(prev='a9.1', next = 'a7', attr={'base_url': 'test_first', 
                                                  'info': {'text': ['Запрокиньте назад голову (разогните в шейном отделе)', 'Откройте рот пациента', 'Выдвиньте нижнюю челюсть и удалите все видимые инородные тела'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить', 'Выполнить', 'Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn2 w-100', 'btn btn-lg btn-outline-success btn3 w-100', 'btn btn-lg btn-outline-success btn4 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }),

          'a15': stage(prev='a7', next = None, attr={'base_url': 'test_third', 
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
          
          'a16': stage(prev='a15', next = 'c4', attr={'base_url': 'test_first', 
                                                  'info': {'text': ['Подключите к пациенту кислород'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }),

          'b16': stage(prev='b17', next = 'c4', attr={'base_url': 'test_first', 
                                                  'info': {'text': ['Подключите к пациенту кислород'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }),

          'c16': stage(prev='a25', next = 'c18', attr={'base_url': 'test_first', 
                                                  'info': {'text': ['Подключите к пациенту кислород'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }),

          'd16': stage(prev='b25', next = 'b24.3', attr={'base_url': 'test_first', 
                                                  'info': {'text': ['Подключите к пациенту кислород'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }),

          'e16': stage(prev='c25', next = 'd18', attr={'base_url': 'test_first', 
                                                  'info': {'text': ['Подключите к пациенту кислород'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }),

          'f16': stage(prev='d25', next = 'b24.6', attr={'base_url': 'test_first', 
                                                  'info': {'text': ['Подключите к пациенту кислород'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }),

          'g16': stage(prev=None , next = 'a24.7', attr={'base_url': 'test_first', 
                                                  'info': {'text': ['Подключите к пациенту кислород'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }),

          'a17': stage(prev='a15', next = 'c4', attr={'base_url': 'test_first', 
                                                  'info': {'text': ['Установите воздуховод № или ларингеальную маску № '], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }),

          'b17': stage(prev='a15', next = 'b16', attr={'base_url': 'test_first', 
                                                  'info': {'text': ['Установите воздуховод № или ларингеальную маску № '], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }),

          'a18': stage(prev='17', next = 'a20', attr={'base_url': 'test_first', 
                                                  'info': {'text': ['Обеспечьте внутривенный/внутрикостный сосудистый доступ'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }),

          'b18': stage(prev='a9.1', next = 'a21', attr={'base_url': 'test_first', 
                                                  'info': {'text': ['Обеспечьте внутривенный/внутрикостный сосудистый доступ'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }),

          'c18': stage(prev='b8', next = 'a24.3', attr={'base_url': 'test_first', 
                                                  'info': {'text': ['Обеспечьте внутривенный/внутрикостный сосудистый доступ'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }),

          'd18': stage(prev='d8', next = 'a24.6', attr={'base_url': 'test_first', 
                                                  'info': {'text': ['Обеспечьте внутривенный/внутрикостный сосудистый доступ'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }),

          'e18': stage(prev=None, next = 'g16', attr={'base_url': 'test_first', 
                                                  'info': {'text': ['Обеспечьте внутривенный/внутрикостный сосудистый доступ'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }),

          '18.1': stage(prev='18', next = None, attr={'base_url': 'test_fourth', 
                                                 'info': {'text': ['Сосудистый доступ установлен?'], 
                                                          'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                 'buttons': {'text': ["Да", "Нет"], 
                                                             'styles': ['btn btn-lg btn-outline-success btn181 w-100', 'btn btn-lg btn-outline-danger btn182 w-100']}, 
                                                 'navigation': {'text': ['В начало', 'Назад', 'Далее'], 
                                                                'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                 }),

          '18.2': stage(prev='17', next = '18.1', attr={'base_url': 'test_first', 
                                                  'info': {'text': ['Обеспечьте внутривенный сосудистый доступ'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }),

          'a19': stage(prev='a9', next = None, attr={'base_url': 'test_fourth', 
                                                 'info': {'text': ['Сахар крови'], 
                                                          'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                 'buttons': {'text': ["Выше 3 ммоль/л", "Ниже 3 ммоль/л "], 
                                                             'styles': ['btn btn-lg btn-outline-success btn191 w-100', 'btn btn-lg btn-outline-danger btn192 w-100']}, 
                                                 'navigation': {'text': ['В начало', 'Назад', 'Далее'], 
                                                                'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                 }),

          'b19': stage(prev='a20', next = None, attr={'base_url': 'test_fourth', 
                                                 'info': {'text': ['Сахар крови'], 
                                                          'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                 'buttons': {'text': ["Выше 3 ммоль/л", "Ниже 3 ммоль/л "], 
                                                             'styles': ['btn btn-lg btn-outline-success btn191 w-100', 'btn btn-lg btn-outline-danger btn192 w-100']}, 
                                                 'navigation': {'text': ['В начало', 'Назад', 'Далее'], 
                                                                'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                 }),

          'c19': stage(prev='a21', next = None, attr={'base_url': 'test_fourth', 
                                                 'info': {'text': ['Сахар крови'], 
                                                          'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                 'buttons': {'text': ["Выше 3 ммоль/л", "Ниже 3 ммоль/л "], 
                                                             'styles': ['btn btn-lg btn-outline-success btn191 w-100', 'btn btn-lg btn-outline-danger btn192 w-100']}, 
                                                 'navigation': {'text': ['В начало', 'Назад', 'Далее'], 
                                                                'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                 }),

          'd19': stage(prev='c20', next = None, attr={'base_url': 'test_fourth', 
                                                 'info': {'text': ['Сахар крови'], 
                                                          'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                 'buttons': {'text': ["Выше 3 ммоль/л", "Ниже 3 ммоль/л "], 
                                                             'styles': ['btn btn-lg btn-outline-success btn191 w-100', 'btn btn-lg btn-outline-danger btn192 w-100']}, 
                                                 'navigation': {'text': ['В начало', 'Назад', 'Далее'], 
                                                                'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                 }),

          'a20': stage(prev='a18', next = 'b19', attr={'base_url': 'test_first', 
                                                  'info': {'text': ['Поместите сахар/конфету за щёку пациента (не за зубы).При наличии доступа в вену – внутривенно мл 20% раствора глюкозы (ампулы 40% глюкозы развести пополам 0,9 % раствором NaCl)', 'Определите уровень сахара повторно через 5 минут'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить', 'Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn2 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }),

          'b20': stage(prev='a18', next = 'a10.1', attr={'base_url': 'test_first', 
                                                  'info': {'text': ['Поместите сахар/конфету за щёку пациента (не за зубы).При наличии доступа в вену – внутривенно мл 20% раствора глюкозы (ампулы 40% глюкозы развести пополам 0,9 % раствором NaCl)', 'Определите уровень сахара повторно через 5 минут'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить', 'Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn2 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }),

          'c20': stage(prev='c19', next = 'd19', attr={'base_url': 'test_first', 
                                                  'info': {'text': ['Поместите сахар/конфету за щёку пациента (не за зубы).При наличии доступа в вену – внутривенно мл 20% раствора глюкозы (ампулы 40% глюкозы развести пополам 0,9 % раствором NaCl)', 'Определите уровень сахара повторно через 5 минут'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить', 'Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn2 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }),

          'd20': stage(prev='c19', next = 'b22', attr={'base_url': 'test_first', 
                                                  'info': {'text': ['Поместите сахар/конфету за щёку пациента (не за зубы).При наличии доступа в вену – внутривенно мл 20% раствора глюкозы (ампулы 40% глюкозы развести пополам 0,9 % раствором NaCl)', 'Определите уровень сахара повторно через 5 минут'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить', 'Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn2 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }),

          'a21': stage(prev='b18', next = 'c19', attr={'base_url': 'test_first', 
                                                  'info': {'text': ['При наличии сосудистого доступа – введите внутривенно вальпроевую кислоту мл (15 мг/кг), либо мидазолам мл (0,3 мг/кг), либо диазепам мл (0,3-0,5 мг/кг)', 'При отсутствии сосудистого доступа внутримышечно ввести мидазолам мл (0,3 мг/кг), либо диазепам мл (0,3-0,5 мг/кг)'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить', 'Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn2 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }),

          'b21': stage(prev='a22', next = 'b10.1', attr={'base_url': 'test_first', 
                                                  'info': {'text': ['При наличии сосудистого доступа – введите внутривенно вальпроевую кислоту мл (15 мг/кг), либо мидазолам мл (0,3 мг/кг), либо диазепам мл (0,3-0,5 мг/кг)', 'При отсутствии сосудистого доступа внутримышечно ввести мидазолам мл (0,3 мг/кг), либо диазепам мл (0,3-0,5 мг/кг)'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить', 'Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn2 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }),

          'a22': stage(prev='21', next = None, attr={'base_url': 'test_fourth', 
                                                 'info': {'text': ['Судороги купированы?'], 
                                                          'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                 'buttons': {'text': ["Да", "Нет"], 
                                                             'styles': ['btn btn-lg btn-outline-success btn221 w-100', 'btn btn-lg btn-outline-danger btn222 w-100']}, 
                                                 'navigation': {'text': ['В начало', 'Назад', 'Далее'], 
                                                                'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                 }),

          'b22': stage(prev='d20', next = None, attr={'base_url': 'test_fourth', 
                                                 'info': {'text': ['Судороги купированы?'], 
                                                          'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                 'buttons': {'text': ["Да", "Нет"], 
                                                             'styles': ['btn btn-lg btn-outline-success btn221 w-100', 'btn btn-lg btn-outline-danger btn222 w-100']}, 
                                                 'navigation': {'text': ['В начало', 'Назад', 'Далее'], 
                                                                'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                 }),

          'a23': stage(prev='a5', next = None, attr={'base_url': 'test_fourth', 
                                                 'info': {'text': ['Пациент может выполнять команды?'], 
                                                          'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                 'buttons': {'text': ["Да", "Нет"], 
                                                             'styles': ['btn btn-lg btn-outline-success btn231 w-100', 'btn btn-lg btn-outline-danger btn232 w-100']}, 
                                                 'navigation': {'text': ['В начало', 'Назад', 'Далее'], 
                                                                'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                 }),

          'b23': stage(prev='a5', next = None, attr={'base_url': 'test_fourth', 
                                                 'info': {'text': ['Пациент может выполнять команды?'], 
                                                          'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                 'buttons': {'text': ["Да", "Нет"], 
                                                             'styles': ['btn btn-lg btn-outline-success btn231 w-100', 'btn btn-lg btn-outline-danger btn232 w-100']}, 
                                                 'navigation': {'text': ['В начало', 'Назад', 'Далее'], 
                                                                'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                 }),

          'c23': stage(prev='a5', next = None, attr={'base_url': 'test_fourth', 
                                                 'info': {'text': ['Пациент может выполнять команды?'], 
                                                          'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                 'buttons': {'text': ["Да", "Нет"], 
                                                             'styles': ['btn btn-lg btn-outline-success btn231 w-100', 'btn btn-lg btn-outline-danger btn232 w-100']}, 
                                                 'navigation': {'text': ['В начало', 'Назад', 'Далее'], 
                                                                'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                 }),

          '23.1': stage(prev='23', next = None, attr={'base_url': 'test_third', 
                                                 'info': {'text': ['Рвота, расстройства зрения, речи, параличи есть?', 'Боли в груди/«жжение» за грудиной, нехватка воздуха, цианоз есть ?'], 
                                                          'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                 'buttons':{'left': {'text': ['Да', 'Да'], 
                                                                     'styles': ['btn btn-lg btn-outline-danger btn2311 w-100', 'btn btn-lg btn-outline-danger btn2313 w-100']}, 
                                                            'right': {'text': ['Нет', 'Нет'], 
                                                                      'styles': ['btn btn-lg btn-outline-success btn2312 w-100', 'btn btn-lg btn-outline-success btn2314 w-100']}}, 
                                                 'navigation': {'text': ['В начало', 'Назад', 'Далее'], 
                                                                'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-warning w-100 btn-next disabled'],
                                                                'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                 }),

          '23.2': stage(prev='23.1', next = None, attr={'base_url': 'test_fourth', 
                                                 'info': {'text': ['Нехватка воздуха, хрипы, цианоз есть?'], 
                                                          'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                 'buttons': {'text': ["Да", "Нет"], 
                                                             'styles': ['btn btn-lg btn-outline-danger btn2321 w-100', 'btn btn-lg btn-outline-success btn2322 w-100']}, 
                                                 'navigation': {'text': ['В начало', 'Назад', 'Далее'], 
                                                                'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                 }),

          'a24': stage(prev='a13.3', next = None, attr={'base_url': 'test_fourth', 
                                                 'info': {'text': ['Небулайзер доступен?'], 
                                                          'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                 'buttons': {'text': ["Да", "Нет"], 
                                                             'styles': ['btn btn-lg btn-outline-success btn241 w-100', 'btn btn-lg btn-outline-danger btn242 w-100']}, 
                                                 'navigation': {'text': ['В начало', 'Назад', 'Далее'], 
                                                                'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                 }),

          'b24': stage(prev='b13.3', next = None, attr={'base_url': 'test_fourth', 
                                                 'info': {'text': ['Небулайзер доступен?'], 
                                                          'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                 'buttons': {'text': ["Да", "Нет"], 
                                                             'styles': ['btn btn-lg btn-outline-success btn241 w-100', 'btn btn-lg btn-outline-danger btn242 w-100']}, 
                                                 'navigation': {'text': ['В начало', 'Назад', 'Далее'], 
                                                                'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                 }),

          'a24.3': stage(prev='24', next = 'b25', attr={'base_url': 'test_first', 
                                                  'info': {'text': ['Введите внутривенно или (при отсутствии сосудистого доступа – внутримышечно)' + '\n' + '1. Эпинефрин (адреналин)мл' + '\n' + '2. Дексаметазон мл или Преднизолон мл или Метилпреднизолон мл или Гидрокортизон мл'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }),

          'b24.3': stage(prev='d16', next = 'a10', attr={'base_url': 'test_first', 
                                                  'info': {'text': ['Введите внутривенно или (при отсутствии сосудистого доступа – внутримышечно)' + '\n' + '1. Эпинефрин (адреналин)мл' + '\n' + '2. Дексаметазон мл или Преднизолон мл или Метилпреднизолон мл или Гидрокортизон мл'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }),

          'a24.4': stage(prev='a24', next = 'a25', attr={'base_url': 'test_first', 
                                                  'info': {'text': ['Введите ингаляционно через небулайзер' + '\n' + '1. Будесонид мг + NaCl 0,9% 3 мл' + '\n' + '2. Адреналин мл + NaCl 0,9% 3 мл'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }),

          'a24.5': stage(prev='a24.4', next = 'c25', attr={'base_url': 'test_first', 
                                                  'info': {'text': ['Введите ингаляционно' + '\n' + '1. Сальбутамол доз'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }),

          'a24.6': stage(prev='24.5', next = 'd25', attr={'base_url': 'test_first', 
                                                  'info': {'text': ['Введите внутривенно или (при отсутствии сосудистого доступа – внутримышечно)' + '\n' + '1. Аминофиллин (эуфиллин) мл' + '\n' + '2. Дексаметазон мл или Преднизолон мл или Метилпреднизолон мл или Гидрокортизон мл'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }),

          'b24.6': stage(prev='f16', next = 'b10', attr={'base_url': 'test_first', 
                                                  'info': {'text': ['Введите внутривенно или (при отсутствии сосудистого доступа – внутримышечно)' + '\n' + '1. Аминофиллин (эуфиллин) мл' + '\n' + '2. Дексаметазон мл или Преднизолон мл или Метилпреднизолон мл или Гидрокортизон мл'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }),

          'a24.7': stage(prev='g16', next = 'c10', attr={'base_url': 'test_first', 
                                                  'info': {'text': ['1. Введите внутривенно  Нитроглицерин 10 мг в/в капельно При отсутствии сосудистого доступа дайте пациенту Нитроглицерин 0,4 мг под язык' + '\n' + '2. Введите внутривенно или (при отсутствии сосудистого доступа – внутримышечно) Морфин 1 % - 1 мл (при наличии) Фуросемид 40 мг (4 мл)'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }),

          '24.8': stage(prev='24.7', next = '24.8.1', attr={'base_url': 'test_first', 
                                                  'info': {'text': ['Введите внутривенно/внутрикостно Урапидил 25 мг в/в медленно, далее капельно (у пациентов старше 18 лет) или Сульфат магнезии 25% мл (25-50 мг\кг) в/в медленно Фуросемид мл (1-2 мг/кг) внутривенно'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }),

          '24.8.1': stage(prev='24.8', next = '24.9', attr={'base_url': 'test_first', 
                                                  'info': {'text': ['Введите внутривенно Урапидил 25 мг в/в медленно, далее капельно (у пациентов старше 18 лет) или Сульфат магнезии 25% мл (25-50 мг\кг) в/в медленно Фуросемид мл (1-2 мг/кг) внутривенно'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }),

          '24.9': stage(prev='24.8.1', next = '24.10', attr={'base_url': 'test_first', 
                                                  'info': {'text': ['Важно! Только при ДаД выше 120 мм.рт.ст. АД снижать на 10-15% Введите внутривенно/внутрикостно Урапидил 12, 5 мг в/в медленно, далее капельно (у пациентов старше 18 лет) или Сульфат магнезии 25% мл (25-50 мг\кг) в/в медленно'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }),

          '24.10': stage(prev='24.9', next = '24.10', attr={'base_url': 'test_first', 
                                                  'info': {'text': ['1. Введите внутривенно Нитроглицерин 10 мг в/в капельно. При отсутствии сосудистого доступа дайте пациенту Нитроглицерин 0,4 мг под язык (если прием возможен) 2. Ацетилсалициловая кислоту внутрь 150-300 мг (если прием возможен) 3. Введите внутривенно или (при отсутствии сосудистого доступа – внутримышечно) Морфин 1% - 1 мл (при наличии) или Кетопрофен - 2 мл'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }),

          '24.11': stage(prev='24.10', next = '24.12', attr={'base_url': 'test_first', 
                                                  'info': {'text': ['1. Введите внутривенно  Нитроглицерин 10 мг в/в капельно. При отсутствии сосудистого доступа дайте пациенту Нитроглицерин 0,4 мг под язык (если прием возможен)'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }),

          '24.12': stage(prev='24.11', next = '24.13', attr={'base_url': 'test_first', 
                                                  'info': {'text': ['Пациентам старше 18 лет: 1. моксонидин 0,4 мг внутрь или под язык 2. нифедипин 10 мг внутрь или под язык 3. фуросемид 20 мг (2 мл) внутримышечно (внутривенно при наличии венозного доступа)'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }),

          '24.13': stage(prev='24.12', next = '25', attr={'base_url': 'test_first', 
                                                  'info': {'text': ['Дайте пациенту Нитроглицерин 0,4 мг под язык'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }),

          'a25': stage(prev='a24.4', next = None, attr={'base_url': 'test_fourth', 
                                                 'info': {'text': ['Дыхание, SpO2 нормализовались?'], 
                                                          'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                 'buttons': {'text': ["Да", "Нет"], 
                                                             'styles': ['btn btn-lg btn-outline-success btn251 w-100', 'btn btn-lg btn-outline-danger btn252 w-100']}, 
                                                 'navigation': {'text': ['В начало', 'Назад', 'Далее'], 
                                                                'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                 }),

          'b25': stage(prev='a24.3', next = None, attr={'base_url': 'test_fourth', 
                                                 'info': {'text': ['Дыхание, SpO2 нормализовались?'], 
                                                          'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                 'buttons': {'text': ["Да", "Нет"], 
                                                             'styles': ['btn btn-lg btn-outline-success btn251 w-100', 'btn btn-lg btn-outline-danger btn252 w-100']}, 
                                                 'navigation': {'text': ['В начало', 'Назад', 'Далее'], 
                                                                'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                 }),

          'c25': stage(prev='a24.5', next = None, attr={'base_url': 'test_fourth', 
                                                 'info': {'text': ['Дыхание, SpO2 нормализовались?'], 
                                                          'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                 'buttons': {'text': ["Да", "Нет"], 
                                                             'styles': ['btn btn-lg btn-outline-success btn251 w-100', 'btn btn-lg btn-outline-danger btn252 w-100']}, 
                                                 'navigation': {'text': ['В начало', 'Назад', 'Далее'], 
                                                                'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                 }),

          'd25': stage(prev='a24.6', next = None, attr={'base_url': 'test_fourth', 
                                                 'info': {'text': ['Дыхание, SpO2 нормализовались?'], 
                                                          'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                 'buttons': {'text': ["Да", "Нет"], 
                                                             'styles': ['btn btn-lg btn-outline-success btn251 w-100', 'btn btn-lg btn-outline-danger btn252 w-100']}, 
                                                 'navigation': {'text': ['В начало', 'Назад', 'Далее'], 
                                                                'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                 }),

          '26.1': stage(prev='25', next = None, attr={'base_url': 'test_fourth', 
                                                 'info': {'text': ['Артериальное давление снизилось на 25% от исходных величин?'], 
                                                          'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                 'buttons': {'text': ["Да", "Нет"], 
                                                             'styles': ['btn btn-lg btn-outline-success btn261 w-100', 'btn btn-lg btn-outline-danger btn262 w-100']}, 
                                                 'navigation': {'text': ['В начало', 'Назад', 'Далее'], 
                                                                'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                 }),

          '26.2': stage(prev='26.1', next = None, attr={'base_url': 'test_fourth', 
                                                 'info': {'text': ['Артериальное давление снизилось на 15% от исходных величин?'], 
                                                          'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                 'buttons': {'text': ["Да", "Нет"], 
                                                             'styles': ['btn btn-lg btn-outline-success btn2621 w-100', 'btn btn-lg btn-outline-danger btn2622 w-100']}, 
                                                 'navigation': {'text': ['В начало', 'Назад', 'Далее'], 
                                                                'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                 }),

          '26.3': stage(prev='26.2', next = None, attr={'base_url': 'test_fourth', 
                                                 'info': {'text': ['Артериальное давление снизилось на 25% от исходных величин, болевой синдром купирован?'], 
                                                          'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                 'buttons': {'text': ["Да", "Нет"], 
                                                             'styles': ['btn btn-lg btn-outline-success btn2631 w-100', 'btn btn-lg btn-outline-danger btn2632 w-100']}, 
                                                 'navigation': {'text': ['В начало', 'Назад', 'Далее'], 
                                                                'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                 }),

          '26.4': stage(prev='26.3', next = None, attr={'base_url': 'test_fourth', 
                                                 'info': {'text': ['ЧСС выше в мин?'], 
                                                          'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                 'buttons': {'text': ["Да", "Нет"], 
                                                             'styles': ['btn btn-lg btn-outline-success btn2641 w-100', 'btn btn-lg btn-outline-danger btn2642 w-100']}, 
                                                 'navigation': {'text': ['В начало', 'Назад', 'Далее'], 
                                                                'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                 }),

          }