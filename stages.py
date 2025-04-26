progress = {'1': {'1': False, '2': False, '3': False, '4': False}, 
            '2': {'1': False, '2': False, '3': False, '4': False, '5': False, '6': False, '7': False},
            '3': {'1': False, '2': False, '3': False, '4': False},
            '3.2': {'1': False, '2': False},
            '3.3': {'1': False, '2': False, '3': False, '4': False},
            '4': {'1': False, '2': False, '3': False, '4': False},
            '5': {'1': False, '2': False, '3': False},
            '6': {'1': False, '2': False},
            '7': {'1': False},
            '7.1': {'1': False},
            '7.3': {'1': False},
            '8': {'1': False, '2': False, '3': False, '4': False},
            '8.2': {'1': False, '2': False, '3': False, '4': False},
            '9': {'1': False, '2': False},
            '9.1': {'1': False, '2': False},
            '9.2': {'1': False, '2': False},
            '10': {'1': False},
            '10.1': {'1': False, '2': False},
            '11': {'1': False, '2': False, '3': False, '4': False},
            '12': {'1': False, '2': False},
            '13': {'1': False, '2': False},
            '13.1': {'1': False},
            '13.2': {'1': False},
            '13.3': {'1': False},
            '13.4': {'1': False},
            '14': {'1': False, '2': False, '3': False},
            '15': {'1': False, '2': False},
            '15.1': {'1': False, '2': False},
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
            '23.3': {'1': False, '2': False},
            '24': {'1': False, '2': False},
            '24.3': {'1': False, '2': False},
            '24.3.1': {'1': False},
            '24.3.2': {'1': False},
            '24.3.3': {'1': False},
            '24.3.4': {'1': False},
            '24.3.5': {'1': False},
            '24.4': {'1': False, '2': False},
            '24.5': {'1': False},
            '24.6': {'1': False, '2': False},
            '24.7': {'1': False, '2': False},
            '24.7.1': {'1': False},
            '24.8': {'1': False, '2': False, '3': False},
            '24.8.1': {'1': False, '2': False, '3': False},
            '24.9': {'1': False, '2': False},
            '24.10': {'1': False, '2': False, '3': False},
            '24.11': {'1': False},
            '24.12': {'1': False, '2': False, '3': False},
            '24.12.1': {'1': False, '2': False},
            '24.13': {'1': False, '2': False},
            '25': {'1': False, '2': False},
            '26.1': {'1': False, '2': False},
            '26.2': {'1': False, '2': False},
            '26.3': {'1': False, '2': False},
            '26.4': {'1': False, '2': False},
            '26.5': {'1': False, '2': False},
            '27.1': {'1': False, '2': False},
            '27.2': {'1': False},
            '27.2A': {'1': False},
            '27.2.1': {'1': False, '2': False},
            '27.2.2': {'1': False, '2': False},
            '27.2.3': {'1': False},
            '27.2.4': {'1': False},
            '27.3': {'1': False},
            '27.3.1': {'1': False},
            '27.3.2': {'1': False},
            '27.4': {'1': False, '2': False},
            '27.6': {'1': False, '2': False},
            '28.1': {'1': False, '2': False},
            '28.2': {'1': False, '2': False},
            '28.4': {'1': False, '2': False, '3': False, '4': False},
            '28.4.1': {'1': False, '2': False, '3': False},
            '28.5': {'1': False, '2': False, '3': False, '4': False},
            '28.5.1': {'1': False, '2': False, '3': False, '4': False},
            '28.5.2': {'1': False, '2': False, '3': False, '4': False},
            '28.6': {'1': False},
            '28.7': {'1': False, '2': False, '3': False},
            '29': {'1': False, '2': False},
            '30': {'1': False, '2': False},
            '31': {'1': False, '2': False},
            '32': {'1': False, '2': False},
            '33.1': {'1': False, '2': False, '3': False},
            }


stages = {'aa0': {'prev':'', 'next':'aa1', 'attr':{'base_url': '',
                                                   'info': '',
                                                   'buttons': '',
                                                   'navigation': ''
                                                  }},

          'aa1': {'prev': 'aa0', 'next': 'aa2', 'attr':{'base_url': 'test_first', 
                                                        'info': {'text': ['Человеку плохо, Вы в безопасности', 'Громко оповестить, вывести лишних', 'Вызвать СМП (телефон 103), назвать адрес, не класть трубку', 'Доставить укладку, дефибриллятор'], 
                                                                 'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                        'buttons': {'text': ['Выполнить', 'Выполнить', 'Выполнить', 'Выполнить'], 
                                                                    'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn2 w-100', 'btn btn-lg btn-outline-success btn3 w-100', 'btn btn-lg btn-outline-success btn4 w-100']}, 
                                                        'navigation': {'text': ['Далее'],
                                                                       'styles': ['btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                       'links': ['/next_stage']}
                                                       }},

          'aa2': {'prev':'aa1', 'next':'aa3', 'attr':{'base_url': 'test_second', 
                                                      'info': {}, 
                                                      'buttons': {'text': ['Примерный возраст до 1 года Примерный вес до 10 кг', 'Примерный возраст 1-3 года Примерный вес 10-15 кг', 'Примерный возраст 3-7 лет Примерный вес 15-20 кг', 'Примерный возраст 7-10 лет Примерный вес 20-30 кг', 'Примерный возраст старше 10 лет Примерный вес 30-50 кг', 'Примерный возраст старше 10 лет Примерный вес 50-90 кг', 'Примерный возраст старше 10 лет Примерный вес более 90 кг'], 
                                                                  'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn2 w-100', 'btn btn-lg btn-outline-success btn3 w-100', 'btn btn-lg btn-outline-success btn4 w-100', 'btn btn-lg btn-outline-success btn5 w-100', 'btn btn-lg btn-outline-success btn6 w-100', 'btn btn-lg btn-outline-success btn7 w-100']}, 
                                                      'navigation': {'text': ['В начало', 'Назад', 'Далее'], 
                                                                     'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                    'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                     }},

          'aa3': {'prev':'aa2', 'next':'', 'attr':{'base_url': 'test_third', 
                                                     'info': {'text': ['В сознании. Ответил на вопрос "Что беспокоит" или отреагировал на мягкое "потрясывание" за плечи', 'Судороги'], 
                                                              'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                     'buttons':{'left': {'text': ['Да', 'Да'], 
                                                                'styles': ['btn btn-lg btn-outline-success btn31 w-100', 'btn btn-lg btn-outline-danger btn33 w-100']}, 
                                                                'right': {'text': ['Нет', 'Нет'], 
                                                                'styles': ['btn btn-lg btn-outline-danger btn32 w-100', 'btn btn-lg btn-outline-success btn34 w-100']}}, 
                                                     'navigation': {'text': ['В начало', 'Назад', 'Далее'], 
                                                                'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                    }},

          'ba3.2': {'prev':'', 'next':'', 'attr':{'base_url': 'test_fourth', 
                                                 'info': {'text': ['Генерализированные судороги'], 
                                                          'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                 'buttons': {'text': ["Да", "Нет"], 
                                                             'styles': ['btn btn-lg btn-outline-danger btn3321 w-100', 'btn btn-lg btn-outline-success btn3322 w-100']}, 
                                                 'navigation': {'text': ['В начало', 'Назад', 'Далее'], 
                                                                'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                 }},

          'fa3.2': {'prev':'fa8', 'next':'', 'attr':{'base_url': 'test_fourth', 
                                                 'info': {'text': ['Генерализированные судороги'], 
                                                          'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                 'buttons': {'text': ["Да", "Нет"], 
                                                             'styles': ['btn btn-lg btn-outline-danger btn3321 w-100', 'btn btn-lg btn-outline-success btn3322 w-100']}, 
                                                 'navigation': {'text': ['В начало', 'Назад', 'Далее'], 
                                                                'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                 }},

          'fb3.2': {'prev':'', 'next': '', 'attr':{'base_url': 'test_fourth', 
                                                 'info': {'text': ['Генерализированные судороги'], 
                                                          'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                 'buttons': {'text': ["Да", "Нет"], 
                                                             'styles': ['btn btn-lg btn-outline-danger btn3321 w-100', 'btn btn-lg btn-outline-success btn3322 w-100']}, 
                                                 'navigation': {'text': ['В начало', 'Назад', 'Далее'], 
                                                                'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                 }},

          'ga3.2': {'prev':'', 'next': '', 'attr':{'base_url': 'test_fourth', 
                                                 'info': {'text': ['Генерализированные судороги'], 
                                                          'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                 'buttons': {'text': ["Да", "Нет"], 
                                                             'styles': ['btn btn-lg btn-outline-danger btn3321 w-100', 'btn btn-lg btn-outline-success btn3322 w-100']}, 
                                                 'navigation': {'text': ['В начало', 'Назад', 'Далее'], 
                                                                'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                 }},

          'ga3.3': {'prev':'ga18', 'next': '', 'attr':{'base_url': 'test_third', 
                                                 'info': {'text': ['Внезапное начало. Покраснение кожи. Затруднения дыхания', 'Введена потенциально токсическая доза местного анестетика (максимальная разовая доза). Реакция через некоторое время после инъекции'], 
                                                          'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                 'buttons':{'left': {'text': ['Да', 'Да'], 
                                                                     'styles': ['btn btn-lg btn-outline-danger btn111 w-100', 'btn btn-lg btn-outline-danger btn113 w-100']}, 
                                                            'right': {'text': ['Нет', 'Нет'], 
                                                                      'styles': ['btn btn-lg btn-outline-success btn112 w-100', 'btn btn-lg btn-outline-success btn114 w-100']}}, 
                                                 'navigation': {'text': ['В начало', 'Назад', 'Далее'], 
                                                                'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                 }},
          
          'ba4': {'prev':'ba3.2', 'next': '', 'attr':{'base_url': 'test_fourth', 
                                                 'info': {'text': ['Характер дыхания'], 
                                                          'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                 'buttons': {'text': ["Нормальное", "Нарушена проходимость", "Одышка", "Агональное или отсутствует"], 
                                                             'styles': ['btn btn-lg btn-outline-success btn41 w-100', 'btn btn-lg btn-outline-warning btn42 w-100', 'btn btn-lg btn-outline-warning btn43 w-100', 'btn btn-lg btn-outline-danger btn44 w-100']}, 
                                                 'navigation': {'text': ['В начало', 'Назад', 'Далее'], 
                                                                'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining align-middle', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                 }},

          'bb4': {'prev':'ba3.2', 'next': '', 'attr':{'base_url': 'test_fourth', 
                                                 'info': {'text': ['Характер дыхания'], 
                                                          'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                 'buttons': {'text': ["Нормальное", "Нарушена проходимость", "Одышка", "Агональное или отсутствует"], 
                                                             'styles': ['btn btn-lg btn-outline-success btn41 w-100', 'btn btn-lg btn-outline-warning btn42 w-100', 'btn btn-lg btn-outline-warning btn43 w-100', 'btn btn-lg btn-outline-danger btn44 w-100']}, 
                                                 'navigation': {'text': ['В начало', 'Назад', 'Далее'], 
                                                                'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining align-middle', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                 }},

          'bc4': {'prev':'', 'next': '', 'attr':{'base_url': 'test_fourth', 
                                                 'info': {'text': ['Характер дыхания'], 
                                                          'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                 'buttons': {'text': ["Нормальное", "Нарушена проходимость", "Одышка", "Агональное или отсутствует"], 
                                                             'styles': ['btn btn-lg btn-outline-success btn41 w-100', 'btn btn-lg btn-outline-warning btn42 w-100', 'btn btn-lg btn-outline-warning btn43 w-100', 'btn btn-lg btn-outline-danger btn44 w-100']}, 
                                                 'navigation': {'text': ['В начало', 'Назад', 'Далее'], 
                                                                'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining align-middle', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                 }},

            # вырезано
          'fa4': {'prev':'', 'next': '', 'attr':{'base_url': 'test_fourth', 
                                                 'info': {'text': ['Характер дыхания'], 
                                                          'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                 'buttons': {'text': ["Нормальное", "Нарушена проходимость", "Одышка", "Агональное или отсутствует"], 
                                                             'styles': ['btn btn-lg btn-outline-success btn41 w-100', 'btn btn-lg btn-outline-warning btn42 w-100', 'btn btn-lg btn-outline-warning btn43 w-100', 'btn btn-lg btn-outline-danger btn44 w-100']}, 
                                                 'navigation': {'text': ['В начало', 'Назад', 'Далее'], 
                                                                'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining align-middle', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                 }},

            # вырезано
          'ga4': {'prev':'', 'next': '', 'attr':{'base_url': 'test_fourth', 
                                                 'info': {'text': ['Характер дыхания'], 
                                                          'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                 'buttons': {'text': ["Нормальное", "Нарушена проходимость", "Одышка", "Агональное или отсутствует"], 
                                                             'styles': ['btn btn-lg btn-outline-success btn41 w-100', 'btn btn-lg btn-outline-warning btn42 w-100', 'btn btn-lg btn-outline-warning btn43 w-100', 'btn btn-lg btn-outline-danger btn44 w-100']}, 
                                                 'navigation': {'text': ['В начало', 'Назад', 'Далее'], 
                                                                'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining align-middle', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                 }},

          'ca5': {'prev':'bb4', 'next': '', 'attr':{'base_url': 'test_fourth', 
                                                 'info': {'text': ['Что затруднено, характер хрипов?'], 
                                                          'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                 'buttons': {'text': ["Затруднен вдох,свистящие хрипы, осиплость голоса", "Затруднен выдох,  свистящие хрипы", "Затруднены вдох и выдох, влажные хрипы"], 
                                                             'styles': ['btn btn-lg btn-outline-warning btn51 w-100', 'btn btn-lg btn-outline-warning btn52 w-100', 'btn btn-lg btn-outline-warning btn53 w-100']}, 
                                                 'navigation': {'text': ['В начало', 'Назад', 'Далее'], 
                                                                'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                 }},

          'fa6': {'prev':'', 'next': '', 'attr':{'base_url': 'test_fourth', 
                                                 'info': {'text': ['Пульс на сонной артерии'], 
                                                          'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                 'buttons': {'text': ["Отчетливый", "Резко ослаблен или отсутствует"], 
                                                             'styles': ['btn btn-lg btn-outline-success btn61 w-100', 'btn btn-lg btn-outline-danger btn62 w-100']}, 
                                                 'navigation': {'text': ['В начало', 'Назад', 'Далее'], 
                                                                'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                 }},

          'ba7': {'prev':'ba14', 'next': 'ba15', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Подсоедините тонометр, пульсоксиметр, измерьте артериальное давление'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'ca7': {'prev':'ca13.4', 'next': 'ca8', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Подсоедините тонометр, пульсоксиметр, измерьте артериальное давление'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'da7': {'prev':'da23', 'next': 'da8', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Подсоедините тонометр, пульсоксиметр, измерьте артериальное давление'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'ea7': {'prev':'ea23', 'next': 'ea8', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Подсоедините тонометр, пульсоксиметр, измерьте артериальное давление'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'db7': {'prev':'da13.1', 'next': 'db8', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Подсоедините тонометр, пульсоксиметр, измерьте артериальное давление'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'cb7': {'prev':'ca23', 'next': 'cb8', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Подсоедините тонометр, пульсоксиметр, измерьте артериальное давление'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'eb7': {'prev':'ea13.1', 'next': 'eb8', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Подсоедините тонометр, пульсоксиметр, измерьте артериальное давление'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'fa7': {'prev':'fa6', 'next': 'fa8', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Подсоедините тонометр, пульсоксиметр, измерьте артериальное давление'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'ha7': {'prev':'hc27.4', 'next': 'hc27.6', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Подсоедините тонометр, пульсоксиметр, измерьте артериальное давление'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'hb7': {'prev':'', 'next': 'hd27.6', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Подсоедините тонометр, пульсоксиметр, измерьте артериальное давление'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'ia7': {'prev':'', 'next': 'ia8', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Подсоедините тонометр, пульсоксиметр, измерьте артериальное давление'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'ga7.1': {'prev':'ga8.2', 'next': 'ga24.3.1', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Присоедините к пациенту автоматический наружный дефибриллятор (АНД), выполните оценку сердечного ритма, следуйте инструкциям дефибриллятора'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          #вырезано
          'ha7.1': {'prev':'ha7', 'next': 'hc27.6', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Присоедините к пациенту автоматический наружный дефибриллятор (АНД), выполните оценку сердечного ритма, следуйте инструкциям дефибриллятора'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},
          #вырезано
          'hb7.1': {'prev':'hb7', 'next': 'hd27.6', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Присоедините к пациенту автоматический наружный дефибриллятор (АНД), выполните оценку сердечного ритма, следуйте инструкциям дефибриллятора'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'ia7.1': {'prev':'ia8.2', 'next': 'ia24.3.1', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Присоедините к пациенту автоматический наружный дефибриллятор (АНД), выполните оценку сердечного ритма, следуйте инструкциям дефибриллятора'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'ba7.3': {'prev': 'ba13', 'next': 'ba15.1', 'attr':{'base_url': 'test_first', 
                                        'info': {'text': ['Подключите к пациенту пульсоксиметр'], 
                                                'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                        'buttons': {'text': ['Выполнить'], 
                                                    'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                        'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                        'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                        'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                        }},

          'bb7.3': {'prev': '', 'next': '', 'attr':{'base_url': 'test_first', 
                                        'info': {'text': ['Подключите к пациенту пульсоксиметр'], 
                                                 'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                        'buttons': {'text': ['Выполнить'], 
                                                    'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                        'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                       'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                       'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                        }},

          'bc7.3': {'prev': 'bb4', 'next': 'bc15.1', 'attr':{'base_url': 'test_first', 
                                        'info': {'text': ['Подключите к пациенту пульсоксиметр'], 
                                                'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                        'buttons': {'text': ['Выполнить'], 
                                                    'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                        'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                       'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                       'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                        }},

          'bd7.3': {'prev': 'bb4', 'next': 'bd15.1', 'attr':{'base_url': 'test_first', 
                                        'info': {'text': ['Подключите к пациенту пульсоксиметр'], 
                                                'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                        'buttons': {'text': ['Выполнить'], 
                                                    'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                        'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                       'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                       'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                        }},

          'ca8': {'prev':'ca7', 'next': '', 'attr':{'base_url': 'test_fourth', 
                                                 'info': {'text': ['Артериальное давление'], 
                                                          'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                 'buttons': {'text': ["Нормальное", "Выше 180/120 мм.рт.ст", "Ниже 90/60 мм.рт.ст. у взрослого", "Не определяется"], 
                                                             'styles': ['btn btn-lg btn-outline-success btn81 w-100', 'btn btn-lg btn-outline-warning btn82 w-100', 'btn btn-lg btn-outline-warning btn83 w-100', 'btn btn-lg btn-outline-danger btn84 w-100']}, 
                                                 'navigation': {'text': ['В начало', 'Назад', 'Далее'], 
                                                                'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                 }},

          'da8': {'prev':'da7', 'next': '', 'attr':{'base_url': 'test_fourth', 
                                                 'info': {'text': ['Артериальное давление'], 
                                                          'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                 'buttons': {'text': ["Нормальное", "Выше 180/120 мм.рт.ст", "Ниже 90/60 мм.рт.ст. у взрослого", "Не определяется"], 
                                                             'styles': ['btn btn-lg btn-outline-success btn81 w-100', 'btn btn-lg btn-outline-warning btn82 w-100', 'btn btn-lg btn-outline-warning btn83 w-100', 'btn btn-lg btn-outline-danger btn84 w-100']}, 
                                                 'navigation': {'text': ['В начало', 'Назад', 'Далее'], 
                                                                'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                 }},

          'db8': {'prev':'db7', 'next': '', 'attr':{'base_url': 'test_fourth', 
                                                 'info': {'text': ['Артериальное давление'], 
                                                          'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                 'buttons': {'text': ["Нормальное", "Выше 180/120 мм.рт.ст", "Ниже 90/60 мм.рт.ст. у взрослого", "Не определяется"], 
                                                             'styles': ['btn btn-lg btn-outline-success btn81 w-100', 'btn btn-lg btn-outline-warning btn82 w-100', 'btn btn-lg btn-outline-warning btn83 w-100', 'btn btn-lg btn-outline-danger btn84 w-100']}, 
                                                 'navigation': {'text': ['В начало', 'Назад', 'Далее'], 
                                                                'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                 }},

          'ea8': {'prev':'da7', 'next': '', 'attr':{'base_url': 'test_fourth', 
                                                 'info': {'text': ['Артериальное давление'], 
                                                          'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                 'buttons': {'text': ["Нормальное", "Выше 180/120 мм.рт.ст", "Ниже 90/60 мм.рт.ст. у взрослого", "Не определяется"], 
                                                             'styles': ['btn btn-lg btn-outline-success btn81 w-100', 'btn btn-lg btn-outline-warning btn82 w-100', 'btn btn-lg btn-outline-warning btn83 w-100', 'btn btn-lg btn-outline-danger btn84 w-100']}, 
                                                 'navigation': {'text': ['В начало', 'Назад', 'Далее'], 
                                                                'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                 }},

          'eb8': {'prev':'db7', 'next': '', 'attr':{'base_url': 'test_fourth', 
                                                 'info': {'text': ['Артериальное давление'], 
                                                          'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                 'buttons': {'text': ["Нормальное", "Выше 180/120 мм.рт.ст", "Ниже 90/60 мм.рт.ст. у взрослого", "Не определяется"], 
                                                             'styles': ['btn btn-lg btn-outline-success btn81 w-100', 'btn btn-lg btn-outline-warning btn82 w-100', 'btn btn-lg btn-outline-warning btn83 w-100', 'btn btn-lg btn-outline-danger btn84 w-100']}, 
                                                 'navigation': {'text': ['В начало', 'Назад', 'Далее'], 
                                                                'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                 }},

          'cb8': {'prev':'cb7', 'next': '', 'attr':{'base_url': 'test_fourth', 
                                                 'info': {'text': ['Артериальное давление'], 
                                                          'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                 'buttons': {'text': ["Нормальное", "Выше 180/120 мм.рт.ст", "Ниже 90/60 мм.рт.ст. у взрослого", "Не определяется"], 
                                                             'styles': ['btn btn-lg btn-outline-success btn81 w-100', 'btn btn-lg btn-outline-warning btn82 w-100', 'btn btn-lg btn-outline-warning btn83 w-100', 'btn btn-lg btn-outline-danger btn84 w-100']}, 
                                                 'navigation': {'text': ['В начало', 'Назад', 'Далее'], 
                                                                'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                 }},

          'fa8': {'prev':'fa7', 'next': '', 'attr':{'base_url': 'test_fourth', 
                                                 'info': {'text': ['Артериальное давление'], 
                                                          'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                 'buttons': {'text': ["Нормальное", "Выше 180/120 мм.рт.ст", "Ниже 90/60 мм.рт.ст. у взрослого", "Не определяется"], 
                                                             'styles': ['btn btn-lg btn-outline-success btn81 w-100', 'btn btn-lg btn-outline-warning btn82 w-100', 'btn btn-lg btn-outline-warning btn83 w-100', 'btn btn-lg btn-outline-danger btn84 w-100']}, 
                                                 'navigation': {'text': ['В начало', 'Назад', 'Далее'], 
                                                                'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                 }},

          'ga8': {'prev':'ga10', 'next': '', 'attr':{'base_url': 'test_fourth', 
                                                 'info': {'text': ['Артериальное давление'], 
                                                          'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                 'buttons': {'text': ["Нормальное", "Выше 180/120 мм.рт.ст", "Ниже 90/60 мм.рт.ст. у взрослого", "Не определяется"], 
                                                             'styles': ['btn btn-lg btn-outline-success btn81 w-100', 'btn btn-lg btn-outline-warning btn82 w-100', 'btn btn-lg btn-outline-warning btn83 w-100', 'btn btn-lg btn-outline-danger btn84 w-100']}, 
                                                 'navigation': {'text': ['В начало', 'Назад', 'Далее'], 
                                                                'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                 }},

          'ia8': {'prev':'ia7', 'next': '', 'attr':{'base_url': 'test_fourth', 
                                                 'info': {'text': ['Артериальное давление'], 
                                                          'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                 'buttons': {'text': ["Нормальное", "Выше 180/120 мм.рт.ст", "Ниже 90/60 мм.рт.ст. у взрослого", "Не определяется"], 
                                                             'styles': ['btn btn-lg btn-outline-success btn81 w-100', 'btn btn-lg btn-outline-warning btn82 w-100', 'btn btn-lg btn-outline-warning btn83 w-100', 'btn btn-lg btn-outline-danger btn84 w-100']}, 
                                                 'navigation': {'text': ['В начало', 'Назад', 'Далее'], 
                                                                'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                 }},

          'ga8.2': {'prev':'ga23.3', 'next': '', 'attr':{'base_url': 'test_third', 
                                                 'info': {'text': ['ЧСС более в мин', 'ЧСС менее в мин'], 
                                                          'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                 'buttons':{'left': {'text': ['Да', 'Да'], 
                                                                     'styles': ['btn btn-lg btn-outline-danger btn111 w-100', 'btn btn-lg btn-outline-danger btn113 w-100']}, 
                                                            'right': {'text': ['Нет', 'Нет'], 
                                                                      'styles': ['btn btn-lg btn-outline-success btn112 w-100', 'btn btn-lg btn-outline-success btn114 w-100']}}, 
                                                 'navigation': {'text': ['В начало', 'Назад', 'Далее'], 
                                                                'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                 }},

          'ia8.2': {'prev':'ia18', 'next': '', 'attr':{'base_url': 'test_third', 
                                                 'info': {'text': ['ЧСС более в мин', 'ЧСС менее в мин'], 
                                                          'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                 'buttons':{'left': {'text': ['Да', 'Да'], 
                                                                     'styles': ['btn btn-lg btn-outline-danger btn111 w-100', 'btn btn-lg btn-outline-danger btn113 w-100']}, 
                                                            'right': {'text': ['Нет', 'Нет'], 
                                                                      'styles': ['btn btn-lg btn-outline-success btn112 w-100', 'btn btn-lg btn-outline-success btn114 w-100']}}, 
                                                 'navigation': {'text': ['В начало', 'Назад', 'Далее'], 
                                                                'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                 }},

          'aa9': {'prev':'', 'next': 'aa19', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Не помещайте пальцы в рот (за зубы) пациента', 'Ничего не давайте через рот/под язык до полного восстановления сознания! Не используйте нашатырный спирт!'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить', 'Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn2 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

            # вырезано
          'ca9': {'prev':'cb23', 'next': 'aa19', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Не помещайте пальцы в рот (за зубы) пациента', 'Ничего не давайте через рот/под язык до полного восстановления сознания! Не используйте нашатырный спирт!'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить', 'Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn2 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},
            # вырезано
          'da9': {'prev':'da23', 'next': 'aa19', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Не помещайте пальцы в рот (за зубы) пациента', 'Ничего не давайте через рот/под язык до полного восстановления сознания! Не используйте нашатырный спирт!'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить', 'Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn2 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

            # вырезано
          'ea9': {'prev':'ea23', 'next': 'aa19', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Не помещайте пальцы в рот (за зубы) пациента', 'Ничего не давайте через рот/под язык до полного восстановления сознания! Не используйте нашатырный спирт!'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить', 'Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn2 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'fa9': {'prev':'fb23', 'next': 'aa19', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Не помещайте пальцы в рот (за зубы) пациента', 'Ничего не давайте через рот/под язык до полного восстановления сознания! Не используйте нашатырный спирт!'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить', 'Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn2 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'fb9': {'prev':'fc23', 'next': 'aa19', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Не помещайте пальцы в рот (за зубы) пациента', 'Ничего не давайте через рот/под язык до полного восстановления сознания! Не используйте нашатырный спирт!'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить', 'Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn2 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'fc9': {'prev':'fd23', 'next': 'aa19', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Не помещайте пальцы в рот (за зубы) пациента', 'Ничего не давайте через рот/под язык до полного восстановления сознания! Не используйте нашатырный спирт!'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить', 'Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn2 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

            # вырезано
          'fd9': {'prev':'fe23', 'next': 'aa19', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Не помещайте пальцы в рот (за зубы) пациента', 'Ничего не давайте через рот/под язык до полного восстановления сознания! Не используйте нашатырный спирт!'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить', 'Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn2 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'fe9': {'prev':'ff23', 'next': 'aa19', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Не помещайте пальцы в рот (за зубы) пациента', 'Ничего не давайте через рот/под язык до полного восстановления сознания! Не используйте нашатырный спирт!'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить', 'Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn2 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'ff9': {'prev':'fg23', 'next': 'aa19', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Не помещайте пальцы в рот (за зубы) пациента', 'Ничего не давайте через рот/под язык до полного восстановления сознания! Не используйте нашатырный спирт!'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить', 'Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn2 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'ga9': {'prev':'gb23', 'next': 'aa19', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Не помещайте пальцы в рот (за зубы) пациента', 'Ничего не давайте через рот/под язык до полного восстановления сознания! Не используйте нашатырный спирт!'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить', 'Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn2 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'aa9.1': {'prev':'', 'next': 'ab18', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Не помещайте пальцы в рот (за зубы) пациента', 'Ничего не давайте через рот/под язык!'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить', 'Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn2 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'ba9.1': {'prev':'ba13.2', 'next': 'ba14', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Не помещайте пальцы в рот (за зубы) пациента', 'Ничего не давайте через рот/под язык!'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить', 'Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn2 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

            # вырезано
          'fa9.1': {'prev':'fa13.4', 'next': 'fa15', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Не помещайте пальцы в рот (за зубы) пациента', 'Ничего не давайте через рот/под язык!'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить', 'Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn2 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'ga9.1': {'prev':'ga23', 'next': 'gb13.4', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Не помещайте пальцы в рот (за зубы) пациента', 'Ничего не давайте через рот/под язык!'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить', 'Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn2 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'ja9.2': {'prev':'ja31', 'next':'ba3.2', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Ничего не давайте через рот/под язык, не давайте спазмолитики, не обезболивайте пациента'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить', 'Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn2 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

            # вырезано
          'ca10': {'prev':'', 'next': 'ca11', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Оценивайте дыхание, пульс и SpO2 непрерывно, измеряйте АД не реже раза в 5 минут'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

            # вырезано
          'da10': {'prev':'', 'next': 'da11', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Оценивайте дыхание, пульс и SpO2 непрерывно, измеряйте АД не реже раза в 5 минут'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

            # вырезано
          'ea10': {'prev':'ea24.7', 'next': 'ea11', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Оценивайте дыхание, пульс и SpO2 непрерывно, измеряйте АД не реже раза в 5 минут'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

            # вырезано
          'fa10': {'prev':'fa24.7', 'next': 'fa11', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Оценивайте дыхание, пульс и SpO2 непрерывно, измеряйте АД не реже раза в 5 минут'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'ga10': {'prev':'', 'next': 'ga8', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Оценивайте дыхание, пульс и SpO2 непрерывно, измеряйте АД не реже раза в 5 минут'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},
            
          'aa10.1': {'prev':'', 'next': 'aa12', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Оценивайте дыхание, пульс и SpO2 непрерывно, измеряйте АД не реже раза в 5 минут.', 'При нарушениях, развитии судорог нажмите «В начало»'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить', 'Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn2 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'ab10.1': {'prev':'ab20', 'next': 'aa12', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Оценивайте дыхание, пульс и SpO2 непрерывно, измеряйте АД не реже раза в 5 минут.', 'При нарушениях, развитии судорог нажмите «В начало»'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить', 'Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn2 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

            # вырезано
          'ca10.1': {'prev':'cb23', 'next': 'ca12', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Оценивайте дыхание, пульс и SpO2 непрерывно, измеряйте АД не реже раза в 5 минут.', 'При нарушениях, развитии судорог нажмите «В начало»'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить', 'Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn2 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},
            # вырезано
          'da10.1': {'prev':'cb23', 'next': 'da12', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Оценивайте дыхание, пульс и SpO2 непрерывно, измеряйте АД не реже раза в 5 минут.', 'При нарушениях, развитии судорог нажмите «В начало»'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить', 'Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn2 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

            # вырезано
          'ea10.1': {'prev':'eb23', 'next': 'ea12', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Оценивайте дыхание, пульс и SpO2 непрерывно, измеряйте АД не реже раза в 5 минут.', 'При нарушениях, развитии судорог нажмите «В начало»'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить', 'Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn2 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'fa10.1': {'prev':'', 'next': 'fb23', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Оценивайте дыхание, пульс и SpO2 непрерывно, измеряйте АД не реже раза в 5 минут.', 'При нарушениях, развитии судорог нажмите «В начало»'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить', 'Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn2 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'fb10.1': {'prev':'', 'next': 'fb23', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Оценивайте дыхание, пульс и SpO2 непрерывно, измеряйте АД не реже раза в 5 минут.', 'При нарушениях, развитии судорог нажмите «В начало»'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить', 'Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn2 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'fc10.1': {'prev':'fa26.1', 'next': 'fc12', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Оценивайте дыхание, пульс и SpO2 непрерывно, измеряйте АД не реже раза в 5 минут.', 'При нарушениях, развитии судорог нажмите «В начало»'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить', 'Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn2 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'fd10.1': {'prev':'', 'next': 'fd23', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Оценивайте дыхание, пульс и SpO2 непрерывно, измеряйте АД не реже раза в 5 минут.', 'При нарушениях, развитии судорог нажмите «В начало»'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить', 'Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn2 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},
            # вырезано
          'fe10.1': {'prev':'fa11', 'next': 'fe23', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Оценивайте дыхание, пульс и SpO2 непрерывно, измеряйте АД не реже раза в 5 минут.', 'При нарушениях, развитии судорог нажмите «В начало»'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить', 'Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn2 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

            # вырезано
          'ff10.1': {'prev':'', 'next': 'ff23', 'attr':{'base_url': 'test_first', 
                                                 'info': {'text': ['Оценивайте дыхание, пульс и SpO2 непрерывно, измеряйте АД не реже раза в 5 минут.', 'При нарушениях, развитии судорог нажмите «В начало»'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить', 'Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn2 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'ga10.1': {'prev':'', 'next': 'gb23', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Оценивайте дыхание, пульс и SpO2 непрерывно, измеряйте АД не реже раза в 5 минут.', 'При нарушениях, развитии судорог нажмите «В начало»'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить', 'Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn2 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'ia10.1': {'prev':'', 'next': 'ia11', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Оценивайте дыхание, пульс и SpO2 непрерывно, измеряйте АД не реже раза в 5 минут.', 'При нарушениях, развитии судорог нажмите «В начало»'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить', 'Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn2 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'ib10.1': {'prev':'ia11', 'next': 'ia12', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Оценивайте дыхание, пульс и SpO2 непрерывно, измеряйте АД не реже раза в 5 минут.', 'При нарушениях, развитии судорог нажмите «В начало»'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить', 'Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn2 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'ic10.1': {'prev':'', 'next': 'ib11', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Оценивайте дыхание, пульс и SpO2 непрерывно, измеряйте АД не реже раза в 5 минут.', 'При нарушениях, развитии судорог нажмите «В начало»'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить', 'Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn2 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'id10.1': {'prev':'', 'next': 'ib12', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Оценивайте дыхание, пульс и SpO2 непрерывно, измеряйте АД не реже раза в 5 минут.', 'При нарушениях, развитии судорог нажмите «В начало»'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить', 'Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn2 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'fx10.1': {'prev':'fa3.2', 'next': 'fg23', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Оценивайте дыхание, пульс и SpO2 непрерывно, измеряйте АД не реже раза в 5 минут.', 'При нарушениях, развитии судорог нажмите «В начало»'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить', 'Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn2 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'fy10.1': {'prev':'fb26.1', 'next': 'fg12', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Оценивайте дыхание, пульс и SpO2 непрерывно, измеряйте АД не реже раза в 5 минут.', 'При нарушениях, развитии судорог нажмите «В начало»'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить', 'Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn2 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'fz10.1': {'prev':'fb26.1', 'next': 'fc23', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Оценивайте дыхание, пульс и SpO2 непрерывно, измеряйте АД не реже раза в 5 минут.', 'При нарушениях, развитии судорог нажмите «В начало»'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить', 'Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn2 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

            # вырезано 
          'ca11': {'prev':'ca10', 'next': '', 'attr':{'base_url': 'test_third', 
                                                 'info': {'text': ['Нарушено дыхание?', 'Нарушены пульс, давление?'], 
                                                          'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                 'buttons':{'left': {'text': ['Да', 'Да'], 
                                                                     'styles': ['btn btn-lg btn-outline-danger btn111 w-100', 'btn btn-lg btn-outline-danger btn113 w-100']}, 
                                                            'right': {'text': ['Нет', 'Нет'], 
                                                                      'styles': ['btn btn-lg btn-outline-success btn112 w-100', 'btn btn-lg btn-outline-success btn114 w-100']}}, 
                                                 'navigation': {'text': ['В начало', 'Назад', 'Далее'], 
                                                                'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-warning w-100 btn-next disabled'],
                                                                'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                 }},
            # вырезано
          'da11': {'prev':'da10', 'next': '', 'attr':{'base_url': 'test_third', 
                                                 'info': {'text': ['Нарушено дыхание?', 'Нарушены пульс, давление?'], 
                                                          'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                 'buttons':{'left': {'text': ['Да', 'Да'], 
                                                                     'styles': ['btn btn-lg btn-outline-danger btn111 w-100', 'btn btn-lg btn-outline-danger btn113 w-100']}, 
                                                            'right': {'text': ['Нет', 'Нет'], 
                                                                      'styles': ['btn btn-lg btn-outline-success btn112 w-100', 'btn btn-lg btn-outline-success btn114 w-100']}}, 
                                                 'navigation': {'text': ['В начало', 'Назад', 'Далее'], 
                                                                'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-warning w-100 btn-next disabled'],
                                                                'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                 }},

            # вырезано
          'ea11': {'prev':'ea10', 'next': '', 'attr':{'base_url': 'test_third', 
                                                 'info': {'text': ['Нарушено дыхание?', 'Нарушены пульс, давление?'], 
                                                          'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                 'buttons':{'left': {'text': ['Да', 'Да'], 
                                                                     'styles': ['btn btn-lg btn-outline-danger btn111 w-100', 'btn btn-lg btn-outline-danger btn113 w-100']}, 
                                                            'right': {'text': ['Нет', 'Нет'], 
                                                                      'styles': ['btn btn-lg btn-outline-success btn112 w-100', 'btn btn-lg btn-outline-success btn114 w-100']}}, 
                                                 'navigation': {'text': ['В начало', 'Назад', 'Далее'], 
                                                                'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-warning w-100 btn-next disabled'],
                                                                'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                 }},

            # вырезано
          'fa11': {'prev':'fa10', 'next': '', 'attr':{'base_url': 'test_third', 
                                                 'info': {'text': ['Нарушено дыхание?', 'Нарушены пульс, давление?'], 
                                                          'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                 'buttons':{'left': {'text': ['Да', 'Да'], 
                                                                     'styles': ['btn btn-lg btn-outline-danger btn111 w-100', 'btn btn-lg btn-outline-danger btn113 w-100']}, 
                                                            'right': {'text': ['Нет', 'Нет'], 
                                                                      'styles': ['btn btn-lg btn-outline-success btn112 w-100', 'btn btn-lg btn-outline-success btn114 w-100']}}, 
                                                 'navigation': {'text': ['В начало', 'Назад', 'Далее'], 
                                                                'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-warning w-100 btn-next disabled'],
                                                                'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                 }},

          'ia11': {'prev':'ia10.1', 'next': '', 'attr':{'base_url': 'test_third', 
                                                 'info': {'text': ['Нарушено дыхание?', 'Нарушены пульс, давление?'], 
                                                          'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                 'buttons':{'left': {'text': ['Да', 'Да'], 
                                                                     'styles': ['btn btn-lg btn-outline-danger btn111 w-100', 'btn btn-lg btn-outline-danger btn113 w-100']}, 
                                                            'right': {'text': ['Нет', 'Нет'], 
                                                                      'styles': ['btn btn-lg btn-outline-success btn112 w-100', 'btn btn-lg btn-outline-success btn114 w-100']}}, 
                                                 'navigation': {'text': ['В начало', 'Назад', 'Далее'], 
                                                                'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-warning w-100 btn-next disabled'],
                                                                'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                 }},

          'aa12': {'prev':'', 'next': 'aa13', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Откройте пути для эвакуации пациента. Передайте пациента бригаде скорой медицинской помощи, опишите детали произошедшего', 'Заполните медицинскую документацию'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить', 'Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn2 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

            # вырезано
          'ca12': {'prev':'ca10.1', 'next': 'aa13', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Откройте пути для эвакуации пациента. Передайте пациента бригаде скорой медицинской помощи, опишите детали произошедшего', 'Заполните медицинскую документацию'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить', 'Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn2 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},
            # вырезано
          'da12': {'prev':'da10.1', 'next': 'aa13', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Откройте пути для эвакуации пациента. Передайте пациента бригаде скорой медицинской помощи, опишите детали произошедшего', 'Заполните медицинскую документацию'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить', 'Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn2 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

            # вырезано
          'ea12': {'prev':'ea10.1', 'next': 'aa13', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Откройте пути для эвакуации пациента. Передайте пациента бригаде скорой медицинской помощи, опишите детали произошедшего', 'Заполните медицинскую документацию'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить', 'Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn2 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'fa12': {'prev':'fb23', 'next': 'aa13', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Откройте пути для эвакуации пациента. Передайте пациента бригаде скорой медицинской помощи, опишите детали произошедшего', 'Заполните медицинскую документацию'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить', 'Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn2 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'fb12': {'prev':'fc23', 'next': 'aa13', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Откройте пути для эвакуации пациента. Передайте пациента бригаде скорой медицинской помощи, опишите детали произошедшего', 'Заполните медицинскую документацию'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить', 'Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn2 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},


          'fc12': {'prev':'fc10.1', 'next': 'aa13', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Откройте пути для эвакуации пациента. Передайте пациента бригаде скорой медицинской помощи, опишите детали произошедшего', 'Заполните медицинскую документацию'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить', 'Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn2 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

            # вырезано
          'fd12': {'prev':'fd23', 'next': 'aa13', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Откройте пути для эвакуации пациента. Передайте пациента бригаде скорой медицинской помощи, опишите детали произошедшего', 'Заполните медицинскую документацию'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить', 'Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn2 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},
            # вырезано
          'fe12': {'prev':'fe23', 'next': 'aa13', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Откройте пути для эвакуации пациента. Передайте пациента бригаде скорой медицинской помощи, опишите детали произошедшего', 'Заполните медицинскую документацию'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить', 'Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn2 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'ff12': {'prev':'ff23', 'next': 'aa13', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Откройте пути для эвакуации пациента. Передайте пациента бригаде скорой медицинской помощи, опишите детали произошедшего', 'Заполните медицинскую документацию'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить', 'Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn2 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'fg12': {'prev':'fy10.1', 'next': 'aa13', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Откройте пути для эвакуации пациента. Передайте пациента бригаде скорой медицинской помощи, опишите детали произошедшего', 'Заполните медицинскую документацию'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить', 'Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn2 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'fh12': {'prev':'fg23', 'next': 'aa13', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Откройте пути для эвакуации пациента. Передайте пациента бригаде скорой медицинской помощи, опишите детали произошедшего', 'Заполните медицинскую документацию'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить', 'Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn2 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'ga12': {'prev':'gb23', 'next': 'aa13', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Откройте пути для эвакуации пациента. Передайте пациента бригаде скорой медицинской помощи, опишите детали произошедшего', 'Заполните медицинскую документацию'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить', 'Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn2 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'ha12': {'prev':'', 'next': 'aa13', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Откройте пути для эвакуации пациента. Передайте пациента бригаде скорой медицинской помощи, опишите детали произошедшего', 'Заполните медицинскую документацию'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить', 'Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn2 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'hb12': {'prev':'ha27.2.2', 'next': 'aa13', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Откройте пути для эвакуации пациента. Передайте пациента бригаде скорой медицинской помощи, опишите детали произошедшего', 'Заполните медицинскую документацию'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить', 'Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn2 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'hc12': {'prev':'hb27.6', 'next': 'aa13', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Откройте пути для эвакуации пациента. Передайте пациента бригаде скорой медицинской помощи, опишите детали произошедшего', 'Заполните медицинскую документацию'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить', 'Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn2 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'hd12': {'prev':'hc27.6', 'next': 'aa13', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Откройте пути для эвакуации пациента. Передайте пациента бригаде скорой медицинской помощи, опишите детали произошедшего', 'Заполните медицинскую документацию'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить', 'Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn2 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'he12': {'prev':'hb27.2.2', 'next': 'aa13', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Откройте пути для эвакуации пациента. Передайте пациента бригаде скорой медицинской помощи, опишите детали произошедшего', 'Заполните медицинскую документацию'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить', 'Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn2 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'ia12': {'prev':'ib10.1', 'next': 'aa13', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Откройте пути для эвакуации пациента. Передайте пациента бригаде скорой медицинской помощи, опишите детали произошедшего', 'Заполните медицинскую документацию'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить', 'Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn2 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'ib12': {'prev':'id10.1', 'next': 'aa13', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Откройте пути для эвакуации пациента. Передайте пациента бригаде скорой медицинской помощи, опишите детали произошедшего', 'Заполните медицинскую документацию'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить', 'Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn2 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'aa13': {'prev':'aa3', 'next': 'ba3.2', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Уложите пациента на пол на спину', 'Удалите от пациента опасные предметы (пациента от предметов). Насильно не удерживайте пациента!!!'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить', 'Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn2 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

           'ba13': {'prev':'bab4', 'next': 'ba7.3', 'attr':{'base_url': 'test_first', 
                                    'info': {'text': ['Уложите пациента на пол на спину', 'Удалите от пациента опасные предметы (пациента от предметов). Насильно не удерживайте пациента!!!'], 
                                            'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                    'buttons': {'text': ['Выполнить', 'Выполнить'], 
                                                'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn2 w-100']}, 
                                    'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                    'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                    'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                    }},

          'fa13': {'prev':'fa3.2', 'next': 'aa9.1', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Уложите пациента на пол на спину', 'Удалите от пациента опасные предметы (пациента от предметов). Насильно не удерживайте пациента!!!'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить', 'Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn2 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'fb13': {'prev':'fa3.2', 'next': 'aa9.1', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Уложите пациента на пол на спину', 'Удалите от пациента опасные предметы (пациента от предметов). Насильно не удерживайте пациента!!!'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить', 'Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn2 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'ga13': {'prev':'ga3.2', 'next': 'aa9.1', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Уложите пациента на пол на спину', 'Удалите от пациента опасные предметы (пациента от предметов). Насильно не удерживайте пациента!!!'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить', 'Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn2 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'aa13.1': {'prev':'aa3', 'next': 'ba3.2', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Уложите пациента на пол на спину с приподнятыми ногами'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          # вырезано
          'ca13.1': {'prev':'ca23', 'next': 'ca7', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Уложите пациента на пол на спину с приподнятыми ногами'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'da13.1': {'prev':'da23', 'next': 'db7', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Уложите пациента на пол на спину с приподнятыми ногами'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'db13.1': {'prev':'da8', 'next': 'da18', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Уложите пациента на пол на спину с приподнятыми ногами'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'ea13.1': {'prev':'ea23', 'next': 'eb7', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Уложите пациента на пол на спину с приподнятыми ногами'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

            # вырезано
          'eb13.1': {'prev':'ea8', 'next': 'ga3.2', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Уложите пациента на пол на спину с приподнятыми ногами'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'cb13.1': {'prev':'cb8', 'next': 'ca18', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Уложите пациента на пол на спину с приподнятыми ногами'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'ba13.2': {'prev':'bb4', 'next': 'ba9.1', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Уложите пациента на пол на спину на твёрдую поверхность'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'ha13.2': {'prev':'', 'next': 'ha32', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Уложите пациента на пол на спину на твёрдую поверхность'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'ca13.3': {'prev':'cb8', 'next': 'ca24', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Усадите пациента'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'da13.3': {'prev':'da8', 'next': 'da24', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Усадите пациента'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'ea13.3': {'prev':'ea8', 'next': 'ea18', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Усадите пациента'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'fa13.3': {'prev':'fa23.2', 'next': 'fb16', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Усадите пациента'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'ia13.3': {'prev':'ia23.2', 'next': 'ia16', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Усадите пациента'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'ca13.4': {'prev':'сa23', 'next': 'ca7', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Уложите пациента на кушетку'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

            # вырезано
          'fa13.4': {'prev':'fa23', 'next': 'fa9.1', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Уложите пациента на кушетку'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'fb13.4': {'prev':'fa23.1', 'next': 'fb18', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Уложите пациента на кушетку'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'fc13.4': {'prev':'fa23.1', 'next': 'fa26.4', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Уложите пациента на кушетку'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'fd13.4': {'prev':'fa23.2', 'next': 'fb24.13', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Уложите пациента на кушетку'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'ga13.4': {'prev':'ga3.2', 'next': 'ga23', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Уложите пациента на кушетку'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'gb13.4': {'prev':'ga9.1', 'next': 'ga18', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Уложите пациента на кушетку'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'ia13.4': {'prev':'ia8', 'next': 'ia18', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Уложите пациента на кушетку'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'ib13.4': {'prev':'ia23.2', 'next': 'ia24.13', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Уложите пациента на кушетку'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'ba14': {'prev':'ba9.1', 'next': 'ba7', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Запрокиньте назад голову (разогните в шейном отделе)', 'Откройте рот пациента', 'Выдвиньте нижнюю челюсть и удалите все видимые инородные тела'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить', 'Выполнить', 'Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn2 w-100', 'btn btn-lg btn-outline-success btn3 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

            # вырезано
          'fa14': {'prev':'fa15', 'next': 'fb15', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Запрокиньте назад голову (разогните в шейном отделе)', 'Откройте рот пациента', 'Выдвиньте нижнюю челюсть и удалите все видимые инородные тела'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить', 'Выполнить', 'Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn2 w-100', 'btn btn-lg btn-outline-success btn3 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'ha14': {'prev':'ha28.2', 'next': 'ha28.5.1', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Запрокиньте назад голову (разогните в шейном отделе)', 'Откройте рот пациента', 'Выдвиньте нижнюю челюсть и удалите все видимые инородные тела'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить', 'Выполнить', 'Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn2 w-100', 'btn btn-lg btn-outline-success btn3 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'hb14': {'prev':'ha27.2.3', 'next': 'ha17', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Запрокиньте назад голову (разогните в шейном отделе)', 'Откройте рот пациента', 'Выдвиньте нижнюю челюсть и удалите все видимые инородные тела'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить', 'Выполнить', 'Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn2 w-100', 'btn btn-lg btn-outline-success btn3 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'hc14': {'prev':'hb28.2', 'next':'ha28.5.2', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Запрокиньте назад голову (разогните в шейном отделе)', 'Откройте рот пациента', 'Выдвиньте нижнюю челюсть и удалите все видимые инородные тела'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить', 'Выполнить', 'Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn2 w-100', 'btn btn-lg btn-outline-success btn3 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'hd14': {'prev':'hb28.1', 'next':'hb17', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Запрокиньте назад голову (разогните в шейном отделе)', 'Откройте рот пациента', 'Выдвиньте нижнюю челюсть и удалите все видимые инородные тела'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить', 'Выполнить', 'Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn2 w-100', 'btn btn-lg btn-outline-success btn3 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},
            # вырезано
          'ba15': {'prev':'bb16', 'next': '', 'attr':{'base_url': 'test_fourth', 
                                                 'info': {'text': ['Проходимость дыхательных путей  нормальная?'], 
                                                          'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                 'buttons': {'text': ["Да", "Нет"], 
                                                             'styles': ['btn btn-lg btn-outline-success btn181 w-100', 'btn btn-lg btn-outline-danger btn182 w-100']}, 
                                                 'navigation': {'text': ['В начало', 'Назад', 'Далее'], 
                                                                'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                 }},

            # вырезано
          'fa15': {'prev':'fa9.1', 'next': '', 'attr':{'base_url': 'test_fourth', 
                                                 'info': {'text': ['Проходимость дыхательных путей  нормальная?'], 
                                                          'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                 'buttons': {'text': ["Да", "Нет"], 
                                                             'styles': ['btn btn-lg btn-outline-success btn181 w-100', 'btn btn-lg btn-outline-danger btn182 w-100']}, 
                                                 'navigation': {'text': ['В начало', 'Назад', 'Далее'], 
                                                                'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                 }},

            # вырезано
          'fb15': {'prev':'fa14', 'next': '', 'attr':{'base_url': 'test_fourth', 
                                                 'info': {'text': ['Проходимость дыхательных путей  нормальная?'], 
                                                          'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                 'buttons': {'text': ["Да", "Нет"], 
                                                             'styles': ['btn btn-lg btn-outline-success btn181 w-100', 'btn btn-lg btn-outline-danger btn182 w-100']}, 
                                                 'navigation': {'text': ['В начало', 'Назад', 'Далее'], 
                                                                'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                 }},

          'ga15': {'prev':'gb13.4', 'next': '', 'attr':{'base_url': 'test_fourth', 
                                                 'info': {'text': ['Проходимость дыхательных путей  нормальная?'], 
                                                          'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                 'buttons': {'text': ["Да", "Нет"], 
                                                             'styles': ['btn btn-lg btn-outline-success btn181 w-100', 'btn btn-lg btn-outline-danger btn182 w-100']}, 
                                                 'navigation': {'text': ['В начало', 'Назад', 'Далее'], 
                                                                'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                 }},
            # вырезано
          'ba15.1': {'prev':'ba7.3', 'next': '', 'attr':{'base_url': 'test_fourth', 
                                        'info': {'text': ['SpO2 более 92%?'], 
                                                'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                        'buttons': {'text': ["Да", "Нет"], 
                                                    'styles': ['btn btn-lg btn-outline-success btn181 w-100', 'btn btn-lg btn-outline-danger btn182 w-100']}, 
                                        'navigation': {'text': ['В начало', 'Назад', 'Далее'], 
                                                    'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                    'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                        }},
            
          'bb15.1': {'prev':'bb7.3', 'next': '', 'attr':{'base_url': 'test_fourth', 
                                                    'info': {'text': ['SpO2 более 92%?'], 
                                                            'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                    'buttons': {'text': ["Да", "Нет"], 
                                                                'styles': ['btn btn-lg btn-outline-success btn181 w-100', 'btn btn-lg btn-outline-danger btn182 w-100']}, 
                                                    'navigation': {'text': ['В начало', 'Назад', 'Далее'], 
                                                                'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                    }},

          'bc15.1': {'prev':'bc7.3', 'next': '', 'attr':{'base_url': 'test_fourth', 
                                                    'info': {'text': ['SpO2 более 92%?'], 
                                                            'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                    'buttons': {'text': ["Да", "Нет"], 
                                                                'styles': ['btn btn-lg btn-outline-success btn181 w-100', 'btn btn-lg btn-outline-danger btn182 w-100']}, 
                                                    'navigation': {'text': ['В начало', 'Назад', 'Далее'], 
                                                                'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                    }},

          'bd15.1': {'prev':'bd7.3', 'next': '', 'attr':{'base_url': 'test_fourth', 
                                                    'info': {'text': ['SpO2 более 92%?'], 
                                                            'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                    'buttons': {'text': ["Да", "Нет"], 
                                                                'styles': ['btn btn-lg btn-outline-success btn181 w-100', 'btn btn-lg btn-outline-danger btn182 w-100']}, 
                                                    'navigation': {'text': ['В начало', 'Назад', 'Далее'], 
                                                                'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                    }},
          
          'ba16': {'prev':'ba15.1', 'next': 'fa6', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Подключите к пациенту кислород (при наличии возможности)'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'bb16': {'prev':'bb15.1', 'next': 'ba15', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Подключите к пациенту кислород (при наличии возможности)'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'bc16': {'prev':'bc15.1', 'next': 'fa6', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Подключите к пациенту кислород (при наличии возможности)'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'bd16': {'prev':'bd15.1', 'next': 'ca5', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Подключите к пациенту кислород (при наличии возможности)'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},
          
          # вырезано
          'fa16': {'prev':'fa15', 'next': 'fb18', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Подключите к пациенту кислород (при наличии возможности)'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'fb16': {'prev':'fa13.3', 'next': 'fc18', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Подключите к пациенту кислород (при наличии возможности)'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

            # вырезано
          'fc16': {'prev':'fb15', 'next': 'fa4', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Подключите к пациенту кислород (при наличии возможности)'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

            # вырезано
          'fd16': {'prev':'fb17', 'next': 'fa4', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Подключите к пациенту кислород (при наличии возможности)'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'ca16': {'prev':'ca25', 'next': 'ca18', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Подключите к пациенту кислород (при наличии возможности)'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'da16': {'prev':'da25', 'next': 'da18', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Подключите к пациенту кислород (при наличии возможности)'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'db16': {'prev':'db25', 'next': 'db24.6', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Подключите к пациенту кислород (при наличии возможности)'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'cb16': {'prev':'cb25', 'next': 'cb24.3', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Подключите к пациенту кислород (при наличии возможности)'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'ea16': {'prev':'ea18', 'next': 'ea24.7', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Подключите к пациенту кислород (при наличии возможности)'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

            # вырезано
          'gb16': {'prev':'ga15', 'next': 'ga4', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Подключите к пациенту кислород (при наличии возможности)'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

            # вырезано
          'ga16': {'prev':'ga17', 'next': 'ga4', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Подключите к пациенту кислород (при наличии возможности)'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

            'ha16': {'prev':'ha17', 'next': 'ha28.5', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Подключите к пациенту кислород (при наличии возможности)'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

            'hb16': {'prev':'hb17', 'next': 'ha33.1', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Подключите к пациенту кислород (при наличии возможности)'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'ia16': {'prev':'ia13.3', 'next': 'ic18', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Подключите к пациенту кислород (при наличии возможности)'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'ib16': {'prev':'ia23.2', 'next': 'ib24.10', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Подключите к пациенту кислород (при наличии возможности)'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'ba17': {'prev':'ba15', 'next': 'ba3.2', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Установите воздуховод № или ларингеальную маску № '], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'bb17': {'prev':'ba15', 'next': 'bc4', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Установите воздуховод № или ларингеальную маску № '], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

            # вырезано
          'fa17': {'prev':'fb15', 'next': 'fa4', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Установите воздуховод № или ларингеальную маску № '], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

            # вырезано
          'fb17': {'prev':'fb15', 'next': 'fd16', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Установите воздуховод № или ларингеальную маску № '], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

            # вырезано
          'ga17': {'prev':'ga15', 'next': 'ga16', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Установите воздуховод № или ларингеальную маску № '], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

            # вырезано
          'gb17': {'prev':'ga15', 'next': 'ga4', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Установите воздуховод № или ларингеальную маску № '], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'ha17': {'prev':'hb14', 'next': 'ha16', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Установите воздуховод № или ларингеальную маску № '], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'hb17': {'prev':'hb14', 'next': 'hb16', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Установите воздуховод № или ларингеальную маску № '], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'aa18': {'prev':'aa19', 'next': 'aa20', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Обеспечьте внутривенный/внутрикостный сосудистый доступ'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'ab18': {'prev':'aa9.1', 'next': 'aa21', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Обеспечьте внутривенный/внутрикостный сосудистый доступ'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'ca18': {'prev':'', 'next': 'ca24.3', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Обеспечьте внутривенный/внутрикостный сосудистый доступ'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'da18': {'prev':'', 'next': 'da24.6', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Обеспечьте внутривенный/внутрикостный сосудистый доступ'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'ea18': {'prev':'ea13.3', 'next': 'ea16', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Обеспечьте внутривенный/внутрикостный сосудистый доступ'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'fb18': {'prev':'fb13.4', 'next': 'fa24.9', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Обеспечьте внутривенный/внутрикостный сосудистый доступ'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'fa18': {'prev':'fa13.4', 'next': 'fa24.10', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Обеспечьте внутривенный/внутрикостный сосудистый доступ'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'fc18': {'prev':'fb16', 'next': 'fa24.7', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Обеспечьте внутривенный/внутрикостный сосудистый доступ'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

            # вырезано
          'fd18': {'prev':'', 'next': 'fb24.9', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Обеспечьте внутривенный/внутрикостный сосудистый доступ'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'ga18': {'prev':'', 'next': 'ga3.3', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Обеспечьте внутривенный/внутрикостный сосудистый доступ'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'ha18': {'prev':'hb28.6', 'next': 'ha24.3.5', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Обеспечьте внутривенный/внутрикостный сосудистый доступ'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'hb18': {'prev':'ha27.2A', 'next': 'hc24.3.5', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Обеспечьте внутривенный/внутрикостный сосудистый доступ'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'ia18': {'prev':'ia13.4', 'next': 'ia8.2', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Обеспечьте внутривенный/внутрикостный сосудистый доступ'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'ib18': {'prev':'ia26.5', 'next': 'ib24.10', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Обеспечьте внутривенный/внутрикостный сосудистый доступ'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'ic18': {'prev':'ia16', 'next': 'ia24.10', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Обеспечьте внутривенный/внутрикостный сосудистый доступ'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'fa18.1': {'prev':'fa18.2', 'next': '', 'attr':{'base_url': 'test_fourth', 
                                                 'info': {'text': ['Сосудистый доступ установлен?'], 
                                                          'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                 'buttons': {'text': ["Да", "Нет"], 
                                                             'styles': ['btn btn-lg btn-outline-success btn181 w-100', 'btn btn-lg btn-outline-danger btn182 w-100']}, 
                                                 'navigation': {'text': ['В начало', 'Назад', 'Далее'], 
                                                                'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                 }},

          'fa18.2': {'prev':'fa26.1', 'next': 'fa18.1', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Обеспечьте внутривенный сосудистый доступ'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'aa19': {'prev':'', 'next': '', 'attr':{'base_url': 'test_fourth', 
                                                 'info': {'text': ['Сахар крови'], 
                                                          'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                 'buttons': {'text': ["Выше 3 ммоль/л", "Ниже 3 ммоль/л "], 
                                                             'styles': ['btn btn-lg btn-outline-success btn181 w-100', 'btn btn-lg btn-outline-danger btn182 w-100']}, 
                                                 'navigation': {'text': ['В начало', 'Назад', 'Далее'], 
                                                                'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                 }},

          'ab19': {'prev':'aa20', 'next': '', 'attr':{'base_url': 'test_fourth', 
                                                 'info': {'text': ['Сахар крови'], 
                                                          'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                 'buttons': {'text': ["Выше 3 ммоль/л", "Ниже 3 ммоль/л "], 
                                                             'styles': ['btn btn-lg btn-outline-success btn181 w-100', 'btn btn-lg btn-outline-danger btn182 w-100']}, 
                                                 'navigation': {'text': ['В начало', 'Назад', 'Далее'], 
                                                                'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                 }},

          'ac19': {'prev':'aa21', 'next': '', 'attr':{'base_url': 'test_fourth', 
                                                 'info': {'text': ['Сахар крови'], 
                                                          'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                 'buttons': {'text': ["Выше 3 ммоль/л", "Ниже 3 ммоль/л "], 
                                                             'styles': ['btn btn-lg btn-outline-success btn181 w-100', 'btn btn-lg btn-outline-danger btn182 w-100']}, 
                                                 'navigation': {'text': ['В начало', 'Назад', 'Далее'], 
                                                                'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                 }},

          'ad19': {'prev':'ab20', 'next': '', 'attr':{'base_url': 'test_fourth', 
                                                 'info': {'text': ['Сахар крови'], 
                                                          'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                 'buttons': {'text': ["Выше 3 ммоль/л", "Ниже 3 ммоль/л "], 
                                                             'styles': ['btn btn-lg btn-outline-success btn181 w-100', 'btn btn-lg btn-outline-danger btn182 w-100']}, 
                                                 'navigation': {'text': ['В начало', 'Назад', 'Далее'], 
                                                                'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                 }},

          'aa20': {'prev':'aa18', 'next': 'ab19', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Поместите сахар/конфету за щёку пациента (не за зубы).При наличии доступа в вену – внутривенно мл 20% раствора глюкозы (ампулы 40% глюкозы развести пополам 0,9 % раствором NaCl)', 'Определите уровень сахара повторно через 5 минут'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить', 'Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn2 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'ab20': {'prev':'ac19', 'next': 'ad19', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Поместите сахар/конфету за щёку пациента (не за зубы).При наличии доступа в вену – внутривенно мл 20% раствора глюкозы (ампулы 40% глюкозы развести пополам 0,9 % раствором NaCl)', 'Определите уровень сахара повторно через 5 минут'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить', 'Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn2 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'ac20': {'prev':'ad19', 'next': 'aa22', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Поместите сахар/конфету за щёку пациента (не за зубы).При наличии доступа в вену – внутривенно мл 20% раствора глюкозы (ампулы 40% глюкозы развести пополам 0,9 % раствором NaCl)', 'Определите уровень сахара повторно через 5 минут'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить', 'Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn2 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'ad20': {'prev':'ab19', 'next': 'ab10.1', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Поместите сахар/конфету за щёку пациента (не за зубы).При наличии доступа в вену – внутривенно мл 20% раствора глюкозы (ампулы 40% глюкозы развести пополам 0,9 % раствором NaCl)', 'Определите уровень сахара повторно через 5 минут'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить', 'Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn2 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'aa21': {'prev':'ab18', 'next': 'ac19', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['При наличии сосудистого доступа – введите внутривенно вальпроевую кислоту мл (15 мг/кг), либо мидазолам мл (0,3 мг/кг), либо диазепам мл (0,3-0,5 мг/кг)', 'При отсутствии сосудистого доступа внутримышечно ввести мидазолам мл (0,3 мг/кг), либо диазепам мл (0,3-0,5 мг/кг)'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить', 'Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn2 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'ab21': {'prev':'aa22', 'next': 'ba3.2', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['При наличии сосудистого доступа – введите внутривенно вальпроевую кислоту мл (15 мг/кг), либо мидазолам мл (0,3 мг/кг), либо диазепам мл (0,3-0,5 мг/кг)', 'При отсутствии сосудистого доступа внутримышечно ввести мидазолам мл (0,3 мг/кг), либо диазепам мл (0,3-0,5 мг/кг)'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить', 'Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn2 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'aa22': {'prev':'', 'next': '', 'attr':{'base_url': 'test_fourth', 
                                                 'info': {'text': ['Судороги купированы?'], 
                                                          'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                 'buttons': {'text': ["Да", "Нет"], 
                                                             'styles': ['btn btn-lg btn-outline-success btn181 w-100', 'btn btn-lg btn-outline-danger btn182 w-100']}, 
                                                 'navigation': {'text': ['В начало', 'Назад', 'Далее'], 
                                                                'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                 }},

          'ca23': {'prev':'ca5', 'next': '', 'attr':{'base_url': 'test_fourth', 
                                                 'info': {'text': ['Пациент может выполнять команды?'], 
                                                          'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                 'buttons': {'text': ["Да", "Нет"], 
                                                             'styles': ['btn btn-lg btn-outline-success btn181 w-100', 'btn btn-lg btn-outline-danger btn182 w-100']}, 
                                                 'navigation': {'text': ['В начало', 'Назад', 'Далее'], 
                                                                'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                 }},

            # вырезано
          'da23': {'prev':'ca5', 'next': '', 'attr':{'base_url': 'test_fourth', 
                                                 'info': {'text': ['Пациент может выполнять команды?'], 
                                                          'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                 'buttons': {'text': ["Да", "Нет"], 
                                                             'styles': ['btn btn-lg btn-outline-success btn181 w-100', 'btn btn-lg btn-outline-danger btn182 w-100']}, 
                                                 'navigation': {'text': ['В начало', 'Назад', 'Далее'], 
                                                                'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                 }},
            
          'ea23': {'prev':'ca5', 'next': '', 'attr':{'base_url': 'test_fourth', 
                                                 'info': {'text': ['Пациент может выполнять команды?'], 
                                                          'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                 'buttons': {'text': ["Да", "Нет"], 
                                                             'styles': ['btn btn-lg btn-outline-success btn181 w-100', 'btn btn-lg btn-outline-danger btn182 w-100']}, 
                                                 'navigation': {'text': ['В начало', 'Назад', 'Далее'], 
                                                                'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                 }},
            # вырезано
          'eb23': {'prev':'ea11', 'next': '', 'attr':{'base_url': 'test_fourth', 
                                                 'info': {'text': ['Пациент может выполнять команды?'], 
                                                          'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                 'buttons': {'text': ["Да", "Нет"], 
                                                             'styles': ['btn btn-lg btn-outline-success btn181 w-100', 'btn btn-lg btn-outline-danger btn182 w-100']}, 
                                                 'navigation': {'text': ['В начало', 'Назад', 'Далее'], 
                                                                'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                 }},

          'db23': {'prev':'da11', 'next': '', 'attr':{'base_url': 'test_fourth', 
                                                 'info': {'text': ['Пациент может выполнять команды?'], 
                                                          'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                 'buttons': {'text': ["Да", "Нет"], 
                                                             'styles': ['btn btn-lg btn-outline-success btn181 w-100', 'btn btn-lg btn-outline-danger btn182 w-100']}, 
                                                 'navigation': {'text': ['В начало', 'Назад', 'Далее'], 
                                                                'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                 }},

            # вырезано
          'cb23': {'prev':'ca11', 'next': '', 'attr':{'base_url': 'test_fourth', 
                                                 'info': {'text': ['Пациент может выполнять команды?'], 
                                                          'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                 'buttons': {'text': ["Да", "Нет"], 
                                                             'styles': ['btn btn-lg btn-outline-success btn181 w-100', 'btn btn-lg btn-outline-danger btn182 w-100']}, 
                                                 'navigation': {'text': ['В начало', 'Назад', 'Далее'], 
                                                                'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                 }},

          'fa23': {'prev':'', 'next': '', 'attr':{'base_url': 'test_fourth', 
                                                 'info': {'text': ['Пациент может выполнять команды?'], 
                                                          'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                 'buttons': {'text': ["Да", "Нет"], 
                                                             'styles': ['btn btn-lg btn-outline-success btn181 w-100', 'btn btn-lg btn-outline-danger btn182 w-100']}, 
                                                 'navigation': {'text': ['В начало', 'Назад', 'Далее'], 
                                                                'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                 }},

          'fb23': {'prev':'', 'next': '', 'attr':{'base_url': 'test_fourth', 
                                                 'info': {'text': ['Пациент может выполнять команды?'], 
                                                          'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                 'buttons': {'text': ["Да", "Нет"], 
                                                             'styles': ['btn btn-lg btn-outline-success btn181 w-100', 'btn btn-lg btn-outline-danger btn182 w-100']}, 
                                                 'navigation': {'text': ['В начало', 'Назад', 'Далее'], 
                                                                'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                 }},

          'fc23': {'prev':'fz10.1', 'next': '', 'attr':{'base_url': 'test_fourth', 
                                                 'info': {'text': ['Пациент может выполнять команды?'], 
                                                          'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                 'buttons': {'text': ["Да", "Нет"], 
                                                             'styles': ['btn btn-lg btn-outline-success btn181 w-100', 'btn btn-lg btn-outline-danger btn182 w-100']}, 
                                                 'navigation': {'text': ['В начало', 'Назад', 'Далее'], 
                                                                'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                 }},

          'fd23': {'prev':'fd10.1', 'next': '', 'attr':{'base_url': 'test_fourth', 
                                                 'info': {'text': ['Пациент может выполнять команды?'], 
                                                          'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                 'buttons': {'text': ["Да", "Нет"], 
                                                             'styles': ['btn btn-lg btn-outline-success btn181 w-100', 'btn btn-lg btn-outline-danger btn182 w-100']}, 
                                                 'navigation': {'text': ['В начало', 'Назад', 'Далее'], 
                                                                'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                 }},

            # вырезано
          'fe23': {'prev':'fe10.1', 'next': '', 'attr':{'base_url': 'test_fourth', 
                                                 'info': {'text': ['Пациент может выполнять команды?'], 
                                                          'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                 'buttons': {'text': ["Да", "Нет"], 
                                                             'styles': ['btn btn-lg btn-outline-success btn181 w-100', 'btn btn-lg btn-outline-danger btn182 w-100']}, 
                                                 'navigation': {'text': ['В начало', 'Назад', 'Далее'], 
                                                                'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                 }},

            # вырезано
          'ff23': {'prev':'ff10.1', 'next': '', 'attr':{'base_url': 'test_fourth', 
                                                 'info': {'text': ['Пациент может выполнять команды?'], 
                                                          'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                 'buttons': {'text': ["Да", "Нет"], 
                                                             'styles': ['btn btn-lg btn-outline-success btn181 w-100', 'btn btn-lg btn-outline-danger btn182 w-100']},  
                                                 'navigation': {'text': ['В начало', 'Назад', 'Далее'], 
                                                                'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                 }},

          'fg23': {'prev':'fx.10.1', 'next': '', 'attr':{'base_url': 'test_fourth', 
                                                 'info': {'text': ['Пациент может выполнять команды?'], 
                                                          'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                 'buttons': {'text': ["Да", "Нет"], 
                                                             'styles': ['btn btn-lg btn-outline-success btn181 w-100', 'btn btn-lg btn-outline-danger btn182 w-100']},  
                                                 'navigation': {'text': ['В начало', 'Назад', 'Далее'], 
                                                                'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                 }},

          'ga23': {'prev':'', 'next': '', 'attr':{'base_url': 'test_fourth', 
                                                 'info': {'text': ['Пациент может выполнять команды?'], 
                                                          'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                 'buttons': {'text': ["Да", "Нет"], 
                                                             'styles': ['btn btn-lg btn-outline-success btn181 w-100', 'btn btn-lg btn-outline-danger btn182 w-100']}, 
                                                 'navigation': {'text': ['В начало', 'Назад', 'Далее'], 
                                                                'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                 }},

          'gb23': {'prev':'ga10.1', 'next': '', 'attr':{'base_url': 'test_fourth', 
                                                 'info': {'text': ['Пациент может выполнять команды?'], 
                                                          'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                 'buttons': {'text': ["Да", "Нет"], 
                                                             'styles': ['btn btn-lg btn-outline-success btn181 w-100', 'btn btn-lg btn-outline-danger btn182 w-100']}, 
                                                 'navigation': {'text': ['В начало', 'Назад', 'Далее'], 
                                                                'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                 }},

          'fa23.1': {'prev':'fa23', 'next': '', 'attr':{'base_url': 'test_third', 
                                                 'info': {'text': ['Рвота, расстройства зрения, речи, параличи есть?', 'Боли в груди/«жжение» за грудиной, нехватка воздуха, цианоз есть ?'], 
                                                          'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                 'buttons':{'left': {'text': ['Да', 'Да'], 
                                                                     'styles': ['btn btn-lg btn-outline-danger btn2311 w-100', 'btn btn-lg btn-outline-danger btn2313 w-100']}, 
                                                            'right': {'text': ['Нет', 'Нет'], 
                                                                      'styles': ['btn btn-lg btn-outline-success btn2312 w-100', 'btn btn-lg btn-outline-success btn2314 w-100']}}, 
                                                 'navigation': {'text': ['В начало', 'Назад', 'Далее'], 
                                                                'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-warning w-100 btn-next disabled'],
                                                                'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                 }},

          'fa23.2': {'prev':'fa23.1', 'next': '', 'attr':{'base_url': 'test_fourth', 
                                                 'info': {'text': ['Нехватка воздуха, хрипы, цианоз есть?'], 
                                                          'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                 'buttons': {'text': ["Да", "Нет"], 
                                                             'styles': ['btn btn-lg btn-outline-danger btn191 w-100', 'btn btn-lg btn-outline-success btn192 w-100']}, 
                                                 'navigation': {'text': ['В начало', 'Назад', 'Далее'], 
                                                                'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                 }},

          'ia23.2': {'prev':'ia8', 'next': '', 'attr':{'base_url': 'test_fourth', 
                                                 'info': {'text': ['Нехватка воздуха, хрипы, цианоз есть?'], 
                                                          'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                 'buttons': {'text': ["Да", "Нет"], 
                                                             'styles': ['btn btn-lg btn-outline-danger btn191 w-100', 'btn btn-lg btn-outline-success btn192 w-100']},
                                                 'navigation': {'text': ['В начало', 'Назад', 'Далее'], 
                                                                'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                 }},

          'ib23.2': {'prev':'', 'next': '', 'attr':{'base_url': 'test_fourth', 
                                                 'info': {'text': ['Нехватка воздуха, хрипы, цианоз есть?'], 
                                                          'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                 'buttons': {'text': ["Да", "Нет"], 
                                                             'styles': ['btn btn-lg btn-outline-danger btn191 w-100', 'btn btn-lg btn-outline-success btn192 w-100']},
                                                 'navigation': {'text': ['В начало', 'Назад', 'Далее'], 
                                                                'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                 }},

          'ga23.3': {'prev':'ga3.3', 'next': '', 'attr':{'base_url': 'test_fourth', 
                                                 'info': {'text': ['Боли в груди/ «жжение» за грудиной, нехватка воздуха есть?'], 
                                                          'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                 'buttons': {'text': ["Да", "Нет"], 
                                                             'styles': ['btn btn-lg btn-outline-danger btn191 w-100', 'btn btn-lg btn-outline-success btn192 w-100']},
                                                 'navigation': {'text': ['В начало', 'Назад', 'Далее'], 
                                                                'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                 }},

          'ca24': {'prev':'ca13.3', 'next': '', 'attr':{'base_url': 'test_fourth', 
                                                 'info': {'text': ['Небулайзер доступен?'], 
                                                          'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                 'buttons': {'text': ["Да", "Нет"], 
                                                             'styles': ['btn btn-lg btn-outline-success btn181 w-100', 'btn btn-lg btn-outline-danger btn182 w-100']}, 
                                                 'navigation': {'text': ['В начало', 'Назад', 'Далее'], 
                                                                'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                 }},

          'da24': {'prev':'ca13.3', 'next': '', 'attr':{'base_url': 'test_fourth', 
                                                 'info': {'text': ['Небулайзер доступен?'], 
                                                          'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                 'buttons': {'text': ["Да", "Нет"], 
                                                             'styles': ['btn btn-lg btn-outline-success btn181 w-100', 'btn btn-lg btn-outline-danger btn182 w-100']}, 
                                                 'navigation': {'text': ['В начало', 'Назад', 'Далее'], 
                                                                'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                 }},
          #цифры в начале блока
          'ca24.3': {'prev':'', 'next': 'cb25', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Введите внутривенно или (при отсутствии сосудистого доступа – внутримышечно) 1. Эпинефрин (адреналин)мл', '2. Дексаметазон мл или Преднизолон мл или Метилпреднизолон мл или Гидрокортизон мл'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить', 'Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn2 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'cb24.3': {'prev':'', 'next': 'cb25', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Введите внутривенно или (при отсутствии сосудистого доступа – внутримышечно) 1. Эпинефрин (адреналин)мл', '2. Дексаметазон мл или Преднизолон мл или Метилпреднизолон мл или Гидрокортизон мл'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить', 'Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn2 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'ga24.3': {'prev':'ga3.3', 'next': 'ga10', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Введите внутривенно или (при отсутствии сосудистого доступа – внутримышечно) 1. Эпинефрин (адреналин)мл', 'Введите внутривенно/внутрикостно или (при отсутствии сосудистого доступа – внутримышечно) 2. Дексаметазон мл или Преднизолон мл или Метилпреднизолон мл или Гидрокортизон мл'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить', 'Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn2 w-100']},
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'gb24.3': {'prev':'ga3.3', 'next': 'ga24.3.4', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Введите внутривенно или (при отсутствии сосудистого доступа – внутримышечно) 1. Эпинефрин (адреналин)мл', 'Введите внутривенно/внутрикостно или (при отсутствии сосудистого доступа – внутримышечно) 2. Дексаметазон мл или Преднизолон мл или Метилпреднизолон мл или Гидрокортизон мл'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить', 'Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn2 w-100']},
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},


          'ga24.3.1': {'prev':'ga8.2', 'next': 'ga10', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Вводите внутривенно капельно или (при отсутствии сосудистого доступа – внутримышечно) Эпинефрин (адреналин) 1,0 мл в 200 мл 5% раствора глюкозы или 0,9% раствора NaCl. До достижения артериального давления не менее 90/60 мм.рт.ст (при внутримышечном введении 1 раз в 5 минут)'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'gb24.3.1': {'prev':'ga8', 'next': 'ga10.1', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Вводите внутривенно капельно или (при отсутствии сосудистого доступа – внутримышечно) Эпинефрин (адреналин) мл в 200 мл 5 % раствора глюкозы или 0,9 % раствора NaCl. До достижения артериального давления не менее 90/60 мм.рт.ст (при внутримышечном введении 1 раз в 5 минут)'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'ia24.3.1': {'prev':'', 'next': 'ia23.2', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Вводите внутривенно капельно или (при отсутствии сосудистого доступа – внутримышечно) Эпинефрин (адреналин) мл в 200 мл 5 % раствора глюкозы или 0,9 % раствора NaCl. До достижения артериального давления не менее 90/60 мм.рт.ст (при внутримышечном введении 1 раз в 5 минут)'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'ga24.3.2': {'prev':'ga8.2', 'next': 'ga24.3.3', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Вводите внутривенно капельно или (при отсутствии сосудистого доступа – внутримышечно). Атропин мл в 10 мл (5 мл при внутримышечном введении) 0,9 % раствора NaCl Максимальное количество введений - два. Целевое ЧСС не менее в мин (при внутримышечном введении интервал 1 раз в 5 минут)'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'ia24.3.2': {'prev':'ia8.2', 'next': 'ia24.3.3', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Вводите внутривенно капельно или (при отсутствии сосудистого доступа – внутримышечно). Атропин мл в 10 мл (5 мл при внутримышечном введении) 0,9 % раствора NaCl Максимальное количество введений - два. Целевое ЧСС не менее в мин (при внутримышечном введении интервал 1 раз в 5 минут)'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'ga24.3.3': {'prev':'ga24.3.2', 'next': 'ga10', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Вводите внутривенно капельно Допамин (дофамин) 100 мг в 200 мл 5% раствора глюкозы или 0,9% раствора NaCl. До достижения артериального давления не менее 90/60 мм.рт.ст, ЧСС не менее'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'ia24.3.3': {'prev':'ia24.3.2', 'next': 'ia23.2', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Вводите внутривенно капельно Допамин (дофамин) 100 мг в 200 мл 5% раствора глюкозы или 0,9% раствора NaCl. До достижения артериального давления не менее 90/60 мм.рт.ст, ЧСС не менее'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'ga24.3.4': {'prev':'gb24.3', 'next': 'ga10', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Введите внутривенно болюс интралипида 20% мл (1,5 мл/кг) в течение 1 минуты. Немедленно начните инфузию со скоростью мл/час (15 мл/кг/час) (взрослому пациенту - 1 л/час, 300 капель в минуту)'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'ha24.3.5': {'prev':'ha18', 'next': 'hc27.3', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Введите струйно внутривенно/внутрикостно или (при отсутствии сосудистого доступа – внутримышечно под язык) Эпинефрин (адреналин) мл'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'hb24.3.5': {'prev':'hc28.6', 'next': 'hb28.7', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Введите струйно внутривенно/внутрикостно или (при отсутствии сосудистого доступа – внутримышечно под язык) Эпинефрин (адреналин) мл'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'hc24.3.5': {'prev':'hb18', 'next': 'hb27.2A', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Введите струйно внутривенно/внутрикостно или (при отсутствии сосудистого доступа – внутримышечно под язык) Эпинефрин (адреналин) мл'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          #цифры в начале блока
          'ca24.4': {'prev':'ca24', 'next': 'ca25', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Введите ингаляционно через небулайзер 1. Будесонид мг + NaCl 0,9% 3 мл', ' 2. Адреналин мл + NaCl 0,9% 3 мл'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить', 'Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn2 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'da24.5': {'prev':'da24', 'next': 'da25', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Введите ингаляционно Сальбутамол доз'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},
          #цифры в начале блока
          'da24.6': {'prev':'da18', 'next': 'db25', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Введите внутривенно или (при отсутствии сосудистого доступа – внутримышечно) 1. Аминофиллин (эуфиллин) мл', 'Введите внутривенно/внутрикостно или (при отсутствии сосудистого доступа – внутримышечно) 2. Дексаметазон мл или Преднизолон мл или Метилпреднизолон мл или Гидрокортизон мл'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить', 'Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn2 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'db24.6': {'prev':'db16', 'next': 'db25', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Введите внутривенно или (при отсутствии сосудистого доступа – внутримышечно) 1. Аминофиллин (эуфиллин) мл', 'Введите внутривенно/внутрикостно или (при отсутствии сосудистого доступа – внутримышечно) 2. Дексаметазон мл или Преднизолон мл или Метилпреднизолон мл или Гидрокортизон мл'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить', 'Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn2 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'ea24.7': {'prev':'ea16', 'next': 'ba3.2', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Введите внутривенно  Нитроглицерин 10 мг в/в капельно При отсутствии сосудистого доступа дайте пациенту Нитроглицерин 0,4 мг под язык', 'Введите внутривенно или (при отсутствии сосудистого доступа – внутримышечно) Морфин 1 % - 1 мл (при наличии) Фуросемид 40 мг (4 мл)'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить', 'Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'fa24.7': {'prev':'fc18', 'next': 'ba3.2', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Введите внутривенно  Нитроглицерин 10 мг в/в капельно При отсутствии сосудистого доступа дайте пациенту Нитроглицерин 0,4 мг под язык', 'Введите внутривенно или (при отсутствии сосудистого доступа – внутримышечно) Морфин 1 % - 1 мл (при наличии) Фуросемид 40 мг (4 мл)'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить', 'Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'ia24.7.1': {'prev':'ia24.10', 'next': 'ia10.1', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Введите внутривенно или (при отсутствии сосудистого доступа – внутримышечно) Фуросемид 4 мл '], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'ib24.7.1': {'prev':'id24.10', 'next': 'ic10.1', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Введите внутривенно или (при отсутствии сосудистого доступа – внутримышечно) Фуросемид 4 мл '], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'a24.8': {'prev':'b3.2', 'next': 'a26.1', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Введите внутривенно/внутрикостно Урапидил 25 мг в/в медленно, далее капельно (у пациентов старше 18 лет)', 'Сульфат магнезии 25% мл (25-50 мг\кг) в/в медленно', 'Фуросемид мл (1-2 мг/кг) внутривенно'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить', 'Выполнить', 'Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn2 w-100', 'btn btn-lg btn-outline-success btn3 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'fa24.8.1': {'prev':'fa18.1', 'next': 'fd10.1', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Введите внутривенно Урапидил 25 мг в/в медленно, далее капельно (у пациентов старше 18 лет)', 'Сульфат магнезии 25% мл (25-50 мг\кг) в/в медленно', 'Фуросемид мл (1-2 мг/кг) внутривенно'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить', 'Выполнить', 'Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn2 w-100', 'btn btn-lg btn-outline-success btn3 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'fa24.9': {'prev':'fb18', 'next': 'fa26.2', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Важно! Только при ДаД выше 120 мм.рт.ст. АД снижать на 10-15% Введите внутривенно/внутрикостно Урапидил 12, 5 мг в/в медленно, далее капельно (у пациентов старше 18 лет)', 'Сульфат магнезии 25% мл (25-50 мг\кг) в/в медленно'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить', 'Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn2 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

            # вырезано
          'fb24.9': {'prev':'', 'next': 'fa26.2', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Важно! Только при ДаД выше 120 мм.рт.ст. АД снижать на 10-15% Введите внутривенно/внутрикостно Урапидил 12, 5 мг в/в медленно, далее капельно (у пациентов старше 18 лет)', 'Сульфат магнезии 25% мл (25-50 мг\кг) в/в медленно'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить', 'Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn2 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'fa24.10': {'prev':'fa18', 'next': 'fa26.3', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Введите внутривенно Нитроглицерин 10 мг в/в капельно. При отсутствии сосудистого доступа дайте пациенту Нитроглицерин 0,4 мг под язык (если прием возможен)', 'Ацетилсалициловая кислоту внутрь 150-300 мг (если прием возможен)', 'Введите внутривенно или (при отсутствии сосудистого доступа – внутримышечно) Морфин 1% - 1 мл (при наличии) или Кетопрофен - 2 мл'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить', 'Выполнить', 'Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn2 w-100', 'btn btn-lg btn-outline-success btn3 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'ia24.10': {'prev':'ic18', 'next': 'ia24.7.1', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Введите внутривенно Нитроглицерин 10 мг в/в капельно. При отсутствии сосудистого доступа дайте пациенту Нитроглицерин 0,4 мг под язык (если прием возможен)', 'Ацетилсалициловая кислоту внутрь 150-300 мг (если прием возможен)', 'Введите внутривенно или (при отсутствии сосудистого доступа – внутримышечно) Морфин 1% - 1 мл (при наличии) или Кетопрофен - 2 мл'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить', 'Выполнить', 'Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn2 w-100', 'btn btn-lg btn-outline-success btn3 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'ib24.10': {'prev':'ib18', 'next': 'ia10.1', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Введите внутривенно Нитроглицерин 10 мг в/в капельно. При отсутствии сосудистого доступа дайте пациенту Нитроглицерин 0,4 мг под язык (если прием возможен)', 'Ацетилсалициловая кислоту внутрь 150-300 мг (если прием возможен)', 'Введите внутривенно или (при отсутствии сосудистого доступа – внутримышечно) Морфин 1% - 1 мл (при наличии) или Кетопрофен - 2 мл'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить', 'Выполнить', 'Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn2 w-100', 'btn btn-lg btn-outline-success btn3 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'ic24.10': {'prev':'ia23.2', 'next': 'ic10.1', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Введите внутривенно Нитроглицерин 10 мг в/в капельно. При отсутствии сосудистого доступа дайте пациенту Нитроглицерин 0,4 мг под язык (если прием возможен)', 'Ацетилсалициловая кислоту внутрь 150-300 мг (если прием возможен)', 'Введите внутривенно или (при отсутствии сосудистого доступа – внутримышечно) Морфин 1% - 1 мл (при наличии) или Кетопрофен - 2 мл'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить', 'Выполнить', 'Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn2 w-100', 'btn btn-lg btn-outline-success btn3 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'id24.10': {'prev':'ib16', 'next': 'ib24.7.1', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Введите внутривенно Нитроглицерин 10 мг в/в капельно. При отсутствии сосудистого доступа дайте пациенту Нитроглицерин 0,4 мг под язык (если прием возможен)', 'Ацетилсалициловая кислоту внутрь 150-300 мг (если прием возможен)', 'Введите внутривенно или (при отсутствии сосудистого доступа – внутримышечно) Морфин 1% - 1 мл (при наличии) или Кетопрофен - 2 мл'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить', 'Выполнить', 'Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn2 w-100', 'btn btn-lg btn-outline-success btn3 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'fa24.11': {'prev':'fa26.3', 'next': 'fb10.1', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Введите внутривенно  Нитроглицерин 10 мг в/в капельно. При отсутствии сосудистого доступа дайте пациенту Нитроглицерин 0,4 мг под язык (если прием возможен)'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'fa24.12': {'prev':'fa26.4', 'next': 'fa26.1', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Пациентам старше 18 лет: моксонидин 0,4 мг внутрь или под язык', 'Нифедипин 10 мг внутрь или под язык', 'Фуросемид 20 мг (2 мл) внутримышечно (внутривенно при наличии венозного доступа)'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить', 'Выполнить', 'Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn2 w-100', 'btn btn-lg btn-outline-success btn3 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'fa24.12.1': {'prev':'fa26.4', 'next': 'fb26.1', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Пациентам старше 18 лет: моксонидин 0,4 мг внутрь или под язык', 'Нифедипин 10 мг внутрь или под язык', 'Фуросемид 20 мг (2 мл) внутримышечно (внутривенно при наличии венозного доступа)'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить', 'Выполнить', 'Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn2 w-100', 'btn btn-lg btn-outline-success btn3 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'fa24.13': {'prev':'fa18.1', 'next': 'fd10.1', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Дайте пациенту Нитроглицерин 0,4 мг под язык', 'Ацетилсалициловую кислоту внутрь 150-300 мг, если прием внутрь возможен'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить', 'Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn2 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'fb24.13': {'prev':'fd13.4', 'next': 'fb26.3', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Дайте пациенту Нитроглицерин 0,4 мг под язык', 'Ацетилсалициловую кислоту внутрь 150-300 мг, если прием внутрь возможен'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить', 'Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn2 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'ia24.13': {'prev':'ib13.4', 'next': 'ia26.5', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Дайте пациенту Нитроглицерин 0,4 мг под язык', 'Ацетилсалициловую кислоту внутрь 150-300 мг, если прием внутрь возможен'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить', 'Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn2 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'ca25': {'prev':'ca24.4', 'next': '', 'attr':{'base_url': 'test_fourth', 
                                                 'info': {'text': ['Дыхание, SpO2 нормализовались?'], 
                                                          'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                 'buttons': {'text': ["Да", "Нет"], 
                                                             'styles': ['btn btn-lg btn-outline-success btn181 w-100', 'btn btn-lg btn-outline-danger btn182 w-100']}, 
                                                 'navigation': {'text': ['В начало', 'Назад', 'Далее'], 
                                                                'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                 }},

          'da25': {'prev':'da24.5', 'next': '', 'attr':{'base_url': 'test_fourth', 
                                                 'info': {'text': ['Дыхание, SpO2 нормализовались?'], 
                                                          'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                 'buttons': {'text': ["Да", "Нет"], 
                                                             'styles': ['btn btn-lg btn-outline-success btn181 w-100', 'btn btn-lg btn-outline-danger btn182 w-100']}, 
                                                 'navigation': {'text': ['В начало', 'Назад', 'Далее'], 
                                                                'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                 }},

          'cb25': {'prev':'ca24.3', 'next': '', 'attr':{'base_url': 'test_fourth', 
                                                 'info': {'text': ['Дыхание, SpO2 нормализовались?'], 
                                                          'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                 'buttons': {'text': ["Да", "Нет"], 
                                                             'styles': ['btn btn-lg btn-outline-success btn181 w-100', 'btn btn-lg btn-outline-danger btn182 w-100']}, 
                                                 'navigation': {'text': ['В начало', 'Назад', 'Далее'], 
                                                                'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                 }},

          'db25': {'prev':'ca24.6', 'next': '', 'attr':{'base_url': 'test_fourth', 
                                                 'info': {'text': ['Дыхание, SpO2 нормализовались?'], 
                                                          'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                 'buttons': {'text': ["Да", "Нет"], 
                                                             'styles': ['btn btn-lg btn-outline-success btn181 w-100', 'btn btn-lg btn-outline-danger btn182 w-100']},  
                                                 'navigation': {'text': ['В начало', 'Назад', 'Далее'], 
                                                                'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                 }},

          'fa26.1': {'prev':'fa24.12', 'next': '', 'attr':{'base_url': 'test_fourth', 
                                                 'info': {'text': ['Артериальное давление снизилось на 25% от исходных величин?'], 
                                                          'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                 'buttons': {'text': ["Да", "Нет"], 
                                                             'styles': ['btn btn-lg btn-outline-success btn181 w-100', 'btn btn-lg btn-outline-danger btn182 w-100']}, 
                                                 'navigation': {'text': ['В начало', 'Назад', 'Далее'], 
                                                                'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                 }},

          'fb26.1': {'prev':'fa24.12.1', 'next': '', 'attr':{'base_url': 'test_fourth', 
                                                 'info': {'text': ['Артериальное давление снизилось на 25% от исходных величин?'], 
                                                          'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                 'buttons': {'text': ["Да", "Нет"], 
                                                             'styles': ['btn btn-lg btn-outline-success btn181 w-100', 'btn btn-lg btn-outline-danger btn182 w-100']}, 
                                                 'navigation': {'text': ['В начало', 'Назад', 'Далее'], 
                                                                'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                 }},

            # вырезано
          'fa26.2': {'prev':'fa24.9', 'next':'', 'attr':{'base_url': 'test_fourth', 
                                                 'info': {'text': ['Артериальное давление снизилось на 15% от исходных величин?'], 
                                                          'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                 'buttons': {'text': ["Да", "Нет"], 
                                                             'styles': ['btn btn-lg btn-outline-success btn181 w-100', 'btn btn-lg btn-outline-danger btn182 w-100']}, 
                                                 'navigation': {'text': ['В начало', 'Назад', 'Далее'], 
                                                                'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                 }},

          'fa26.3': {'prev':'fa24.10', 'next':'', 'attr':{'base_url': 'test_fourth', 
                                                 'info': {'text': ['Артериальное давление снизилось на 25% от исходных величин, болевой синдром купирован?'], 
                                                          'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                 'buttons': {'text': ["Да", "Нет"], 
                                                             'styles': ['btn btn-lg btn-outline-success btn181 w-100', 'btn btn-lg btn-outline-danger btn182 w-100']}, 
                                                 'navigation': {'text': ['В начало', 'Назад', 'Далее'], 
                                                                'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                 }},

          'fb26.3': {'prev':'fa24.10', 'next':'', 'attr':{'base_url': 'test_fourth', 
                                                 'info': {'text': ['Артериальное давление снизилось на 25% от исходных величин, болевой синдром купирован?'], 
                                                          'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                 'buttons': {'text': ["Да", "Нет"], 
                                                             'styles': ['btn btn-lg btn-outline-success btn181 w-100', 'btn btn-lg btn-outline-danger btn182 w-100']}, 
                                                 'navigation': {'text': ['В начало', 'Назад', 'Далее'], 
                                                                'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                 }},

          'fa26.4': {'prev':'fc13.4', 'next':'', 'attr':{'base_url': 'test_fourth', 
                                                 'info': {'text': ['ЧСС выше в мин?'], 
                                                          'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                 'buttons': {'text': ["Да", "Нет"], 
                                                             'styles': ['btn btn-lg btn-outline-success btn2641 w-100', 'btn btn-lg btn-outline-success btn2642 w-100']}, 
                                                 'navigation': {'text': ['В начало', 'Назад', 'Далее'], 
                                                                'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                 }},

          'ia26.5': {'prev':'ia24.13', 'next': '', 'attr':{'base_url': 'test_fourth', 
                                                 'info': {'text': ['Болевой синдром купирован?'], 
                                                          'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                 'buttons': {'text': ["Да", "Нет"], 
                                                             'styles': ['btn btn-lg btn-outline-success btn181 w-100', 'btn btn-lg btn-outline-danger btn182 w-100']}, 
                                                 'navigation': {'text': ['В начало', 'Назад', 'Далее'], 
                                                                'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                 }},

          'ha27.1': {'prev':'ha13.2', 'next':'ha28.1', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Встаньте на колени сбоку от пациента','Начните компрессии грудной клетки (ориентир – середина грудины): частота компрессий 100-120 в мин., глубина компрессий у взрослых – 5-6 см. глубина компрессий у детей – 1/3 расстояния между грудиной и позвоночником паузы между компрессиями не более 10 сек.'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить', 'Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn2 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'hb27.1': {'prev':'hb28.2', 'next':'hb27.2', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Встаньте на колени сбоку от пациента','Начните компрессии грудной клетки (ориентир – середина грудины): частота компрессий 100-120 в мин., глубина компрессий у взрослых – 5-6 см. глубина компрессий у детей – 1/3 расстояния между грудиной и позвоночником паузы между компрессиями не более 10 сек.'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить', 'Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn2 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'hc27.1': {'prev':'ha33.1', 'next':'hb27.2.4', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Встаньте на колени сбоку от пациента','Начните компрессии грудной клетки (ориентир – середина грудины): частота компрессий 100-120 в мин., глубина компрессий у взрослых – 5-6 см. глубина компрессий у детей – 1/3 расстояния между грудиной и позвоночником паузы между компрессиями не более 10 сек.'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить', 'Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn2 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'ha27.2': {'prev':'ha28.1', 'next':'ha28.2', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Продолжайте компрессии грудной клетки'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'hb27.2': {'prev':'ha28.2', 'next':'ha27.3', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Продолжайте компрессии грудной клетки'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'ha27.2A': {'prev':'hb28.4', 'next':'hb18', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Продолжайте компрессии грудной клетки и исскусьвенные вдохи в соотношении 15/2 (30/2, если один реаниматор) в течение 2 минут'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'hb27.2A': {'prev':'hc24.3.5', 'next':'hc27.3', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Продолжайте компрессии грудной клетки и исскусьвенные вдохи в соотношении 15/2 (30/2, если один реаниматор) в течение 2 минут'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'ha27.2.1': {'prev':'ha27.4', 'next':'ha27.3.1', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Продолжайте компрессии грудной клетки до восстановления дыхания и кровообращения / появления признаков биологической смерти либо до прибытия бригады скорой медицинской помощи', 'При восстановлении дыхания и кровообращения уложите пациента в стабильное боковое положение, обеспечьте непрерывный мониторинг'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить', 'Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn2 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'hb27.2.1': {'prev':'ha27.3.1', 'next':'ha12', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Продолжайте компрессии грудной клетки до восстановления дыхания и кровообращения / появления признаков биологической смерти либо до прибытия бригады скорой медицинской помощи', 'При восстановлении дыхания и кровообращения уложите пациента в стабильное боковое положение, обеспечьте непрерывный мониторинг'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить', 'Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn2 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'ha27.2.2': {'prev':'hb27.4', 'next':'hb12', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Продолжайте реанимационные мероприятия до восстановления дыхания и кровообращения / появления признаков биологической смерти либо до прибытия бригады скорой медицинской помощи', 'При восстановлении дыхания и кровообращения уложите пациента в стабильное боковое положение, обеспечьте непрерывный мониторинг'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить', 'Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn2 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'hb27.2.2': {'prev':'he27.4', 'next':'he12', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Продолжайте реанимационные мероприятия до восстановления дыхания и кровообращения / появления признаков биологической смерти либо до прибытия бригады скорой медицинской помощи', 'При восстановлении дыхания и кровообращения уложите пациента в стабильное боковое положение, обеспечьте непрерывный мониторинг'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить', 'Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn2 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'hc27.2.2': {'prev':'hf27.4', 'next':'ha12', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Продолжайте реанимационные мероприятия до восстановления дыхания и кровообращения / появления признаков биологической смерти либо до прибытия бригады скорой медицинской помощи', 'При восстановлении дыхания и кровообращения уложите пациента в стабильное боковое положение, обеспечьте непрерывный мониторинг'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить', 'Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn2 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'ha27.2.3': {'prev':'ha28.4', 'next':'hb14', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Выполните 30 компрессий грудной клетки'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'hb27.2.3': {'prev':'ha28.5', 'next':'hb28.6', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Выполните 30 компрессий грудной клетки'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'ha27.2.4': {'prev':'ha28.5.2', 'next':'hd28.6', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Выполните 30 (15 у детей) компрессий грудной клетки'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'hb27.2.4': {'prev':'hc27.1', 'next':'hb28.4', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Выполните 30 (15 у детей) компрессий грудной клетки'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'ha27.3': {'prev':'hb27.2', 'next':'ha27.4', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Через 2 минуты выполните оценку пульсации на сонной артерии и дыхания (не более 10 секунд)'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'hb27.3': {'prev':'ha27.3.2', 'next':'hb27.4', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Через 2 минуты выполните оценку пульсации на сонной артерии и дыхания (не более 10 секунд)'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'hc27.3': {'prev':'ha24.3.5', 'next':'ha28.4.1', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Через 2 минуты выполните оценку пульсации на сонной артерии и дыхания (не более 10 секунд)'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'hd27.3': {'prev':'hb28.7', 'next':'he27.4', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Через 2 минуты выполните оценку пульсации на сонной артерии и дыхания (не более 10 секунд)'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'he27.3': {'prev':'hd28.6', 'next':'hf27.4', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Через 2 минуты выполните оценку пульсации на сонной артерии и дыхания (не более 10 секунд)'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'ha27.3.1': {'prev':'ha27.2.1', 'next':'hb27.2.1', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Каждые 2-3 минуты при проведении компрессий меняйтесь местами'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'ha27.3.2': {'prev':'ha28.6', 'next':'hb27.3', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Каждые 2-3 минуты при проведении компрессий и искусственных вдохов меняйтесь местами'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'ha27.4': {'prev':'ha27.3', 'next':'', 'attr':{'base_url': 'test_fourth', 
                                                 'info': {'text': ['Отчетливый пульс на сонной артерии, самостоятельное дыхание восстановились?'], 
                                                          'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                 'buttons': {'text': ["Да", "Нет"], 
                                                             'styles': ['btn btn-lg btn-outline-success btn181 w-100', 'btn btn-lg btn-outline-danger btn182 w-100']}, 
                                                 'navigation': {'text': ['В начало', 'Назад', 'Далее'], 
                                                                'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                 }},

          'hb27.4': {'prev':'hb27.3', 'next':'', 'attr':{'base_url': 'test_fourth', 
                                                 'info': {'text': ['Отчетливый пульс на сонной артерии, самостоятельное дыхание восстановились?'], 
                                                          'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                 'buttons': {'text': ["Да", "Нет"], 
                                                             'styles': ['btn btn-lg btn-outline-success btn181 w-100', 'btn btn-lg btn-outline-danger btn182 w-100']}, 
                                                 'navigation': {'text': ['В начало', 'Назад', 'Далее'], 
                                                                'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                 }},

          'hc27.4': {'prev':'hb28.4.1', 'next':'', 'attr':{'base_url': 'test_fourth', 
                                                 'info': {'text': ['Отчетливый пульс на сонной артерии, самостоятельное дыхание восстановились?'], 
                                                          'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                 'buttons': {'text': ["Да", "Нет"], 
                                                             'styles': ['btn btn-lg btn-outline-success btn181 w-100', 'btn btn-lg btn-outline-danger btn182 w-100']}, 
                                                 'navigation': {'text': ['В начало', 'Назад', 'Далее'], 
                                                                'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                 }},

          'hd27.4': {'prev':'hb28.4.1', 'next':'', 'attr':{'base_url': 'test_fourth', 
                                                 'info': {'text': ['Отчетливый пульс на сонной артерии, самостоятельное дыхание восстановились?'], 
                                                          'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                 'buttons': {'text': ["Да", "Нет"], 
                                                             'styles': ['btn btn-lg btn-outline-success btn181 w-100', 'btn btn-lg btn-outline-danger btn182 w-100']}, 
                                                 'navigation': {'text': ['В начало', 'Назад', 'Далее'], 
                                                                'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                 }},

          'he27.4': {'prev':'hd27.3', 'next':'', 'attr':{'base_url': 'test_fourth', 
                                                 'info': {'text': ['Отчетливый пульс на сонной артерии, самостоятельное дыхание восстановились?'], 
                                                          'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                 'buttons': {'text': ["Да", "Нет"], 
                                                             'styles': ['btn btn-lg btn-outline-success btn181 w-100', 'btn btn-lg btn-outline-danger btn182 w-100']}, 
                                                 'navigation': {'text': ['В начало', 'Назад', 'Далее'], 
                                                                'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                 }},

          'hf27.4': {'prev':'he27.3', 'next':'', 'attr':{'base_url': 'test_fourth', 
                                                 'info': {'text': ['Отчетливый пульс на сонной артерии, самостоятельное дыхание восстановились?'], 
                                                          'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                 'buttons': {'text': ["Да", "Нет"], 
                                                             'styles': ['btn btn-lg btn-outline-success btn181 w-100', 'btn btn-lg btn-outline-danger btn182 w-100']}, 
                                                 'navigation': {'text': ['В начало', 'Назад', 'Далее'], 
                                                                'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                 }},

          'ha27.6': {'prev':'ha27.4', 'next':'ha12', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Уложите пациента в стабильное боковое положения', 'Не оставляйте пациента без присмотра. Непрерывно оценивайте дыхание, пульс на сонной артерии. Будьте готовы к возобновлению СЛР'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить', 'Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn2 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'hb27.6': {'prev':'hb27.4', 'next':'hc12', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Уложите пациента в стабильное боковое положения', 'Не оставляйте пациента без присмотра. Непрерывно оценивайте дыхание, пульс на сонной артерии. Будьте готовы к возобновлению СЛР'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить', 'Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn2 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'hc27.6': {'prev':'ha7.2', 'next':'hd12', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Уложите пациента в стабильное боковое положения', 'Не оставляйте пациента без присмотра. Непрерывно оценивайте дыхание, пульс на сонной артерии. Будьте готовы к возобновлению СЛР'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить', 'Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn2 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'hd27.6': {'prev':'hb7.2', 'next':'hd12', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Уложите пациента в стабильное боковое положения', 'Не оставляйте пациента без присмотра. Непрерывно оценивайте дыхание, пульс на сонной артерии. Будьте готовы к возобновлению СЛР'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить', 'Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn2 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'he27.6': {'prev':'hf27.4', 'next':'ha12', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Уложите пациента в стабильное боковое положения', 'Не оставляйте пациента без присмотра. Непрерывно оценивайте дыхание, пульс на сонной артерии. Будьте готовы к возобновлению СЛР'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить', 'Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn2 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'ha28.1': {'prev':'ha27.1', 'next': '', 'attr':{'base_url': 'test_fourth', 
                                                 'info': {'text': ['Укладка с расходными материалами, вспомогательными устройствами, препаратами, дефибриллятор доступны?'], 
                                                          'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                 'buttons': {'text': ["Да", "Нет"], 
                                                             'styles': ['btn btn-lg btn-outline-success btn181 w-100', 'btn btn-lg btn-outline-danger btn182 w-100']}, 
                                                 'navigation': {'text': ['В начало', 'Назад', 'Далее'], 
                                                                'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                 }},

          'hb28.1': {'prev':'ha32', 'next': '', 'attr':{'base_url': 'test_fourth', 
                                                 'info': {'text': ['Укладка с расходными материалами, вспомогательными устройствами, препаратами, дефибриллятор доступны?'], 
                                                          'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                 'buttons': {'text': ["Да", "Нет"], 
                                                             'styles': ['btn btn-lg btn-outline-success btn181 w-100', 'btn btn-lg btn-outline-danger btn182 w-100']}, 
                                                 'navigation': {'text': ['В начало', 'Назад', 'Далее'], 
                                                                'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                 }},

          'ha28.2': {'prev':'ha27.2', 'next': '', 'attr':{'base_url': 'test_fourth', 
                                                 'info': {'text': ['Средства защиты дыхательных путей реаниматора доступны ? (устройство-маска полиэтиленовая с обратным клапаном)'], 
                                                          'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                 'buttons': {'text': ["Да", "Нет"], 
                                                             'styles': ['btn btn-lg btn-outline-success btn181 w-100', 'btn btn-lg btn-outline-danger btn182 w-100']}, 
                                                 'navigation': {'text': ['В начало', 'Назад', 'Далее'], 
                                                                'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                 }},

          'hb28.2': {'prev':'hb28.1', 'next': '', 'attr':{'base_url': 'test_fourth', 
                                                 'info': {'text': ['Средства защиты дыхательных путей реаниматора доступны ? (устройство-маска полиэтиленовая с обратным клапаном)'], 
                                                          'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                 'buttons': {'text': ["Да", "Нет"], 
                                                             'styles': ['btn btn-lg btn-outline-success btn181 w-100', 'btn btn-lg btn-outline-danger btn182 w-100']}, 
                                                 'navigation': {'text': ['В начало', 'Назад', 'Далее'], 
                                                                'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                 }},

          'ha28.4': {'prev':'ha28.1', 'next':'ha27.2.3', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Как можно скорее подключите к пациенту автоматический наружный дефибриллятор (АНД), оцените ритм', 'Следуйте инструкциям АНД', 'Во время анализа ритма прекратите компрессии грудной клетки (пауза не более 5 секунд)', 'При наличии фибрилляции желудочков/желудочковой тахикардии без пульса выполните одну попытку дефибрилляции'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить', 'Выполнить', 'Выполнить', 'Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn2 w-100', 'btn btn-lg btn-outline-success btn3 w-100', 'btn btn-lg btn-outline-success btn4 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'hb28.4': {'prev':'hb27.2.4', 'next':'ha27.2A', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Как можно скорее подключите к пациенту автоматический наружный дефибриллятор (АНД), оцените ритм', 'Следуйте инструкциям АНД', 'Во время анализа ритма прекратите компрессии грудной клетки (пауза не более 5 секунд)', 'При наличии фибрилляции желудочков/желудочковой тахикардии без пульса выполните одну попытку дефибрилляции'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить', 'Выполнить', 'Выполнить', 'Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn2 w-100', 'btn btn-lg btn-outline-success btn3 w-100', 'btn btn-lg btn-outline-success btn4 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'ha28.4.1': {'prev':'hc27.3', 'next':'hc27.4', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Повторно оцените ритм при помощи АНД', 'Во время анализа ритма прекратите компрессии грудной клетки (пауза не более 5 секунд)', 'При наличии фибрилляции желудочков/желудочковой тахикардии без пульса выполните одну попытку дефибрилляции'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить', 'Выполнить', 'Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn2 w-100', 'btn btn-lg btn-outline-success btn3 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'hb28.4.1': {'prev':'ha28.7', 'next':'hd27.4', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Повторно оцените ритм при помощи АНД', 'Во время анализа ритма прекратите компрессии грудной клетки (пауза не более 5 секунд)', 'При наличии фибрилляции желудочков/желудочковой тахикардии без пульса выполните одну попытку дефибрилляции'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить', 'Выполнить', 'Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn2 w-100', 'btn btn-lg btn-outline-success btn3 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'ha28.5': {'prev':'ha16', 'next':'hb27.2.3', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Присоедините к лицевой маске  (размер       ) или установленной ларингеальной маске ( размер          )    дыхательный мешок', 'Выполните 2 искусственных вдоха при помощи дыхательного мешка', 'Делайте каждый вдох в течение 1 секунды, чтобы грудь заметно приподнималась', 'Пауза в компрессиях грудной клетки для двух вдохов – 5 секунд'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить', 'Выполнить', 'Выполнить', 'Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn2 w-100', 'btn btn-lg btn-outline-success btn3 w-100', 'btn btn-lg btn-outline-success btn4 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'ha28.5.1': {'prev':'ha14', 'next':'ha28.6', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Приложите маску с обратным клапаном к лицу пациента согласно инструкции', 'Выполните 2 искусственных вдоха', 'Делайте каждый вдох в течение 1 секунды, чтобы грудь заметно приподнималась', 'Пауза в компрессиях грудной клетки для двух вдохов – 5 секунд'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить', 'Выполнить', 'Выполнить', 'Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn2 w-100', 'btn btn-lg btn-outline-success btn3 w-100', 'btn btn-lg btn-outline-success btn4 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'ha28.5.2': {'prev':'hc14', 'next':'ha27.2.4', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Приложите маску с обратным клапаном к лицу пациента согласно инструкции', 'Выполните 5 искусственных вдоха', 'Делайте каждый вдох в течение 1 секунды, чтобы грудь заметно приподнималась', 'Пауза в компрессиях грудной клетки для двух вдохов – 5 секунд'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить', 'Выполнить', 'Выполнить', 'Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn2 w-100', 'btn btn-lg btn-outline-success btn3 w-100', 'btn btn-lg btn-outline-success btn4 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'ha28.6': {'prev':'ha28.5.1', 'next':'ha27.3.2', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Продолжайте компрессии грудной клетки и искусственные вдохи в соотношении 30:2 (15/2 у детей до 8 лет) в течение 2 минут'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'hb28.6': {'prev':'hb27.2.3', 'next':'ha18', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Продолжайте компрессии грудной клетки и искусственные вдохи в соотношении 30:2 (15/2 у детей до 8 лет) в течение 2 минут'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'hc28.6': {'prev':'hd27.4', 'next':'hb24.3.5', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Продолжайте компрессии грудной клетки и искусственные вдохи в соотношении 30:2 (15/2 у детей до 8 лет) в течение 2 минут'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'hd28.6': {'prev':'ha27.2.4', 'next':'he27.3', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Продолжайте компрессии грудной клетки и искусственные вдохи в соотношении 30:2 (15/2 у детей до 8 лет) в течение 2 минут'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'ha28.7': {'prev':'27.4', 'next':'hb28.4.1', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Продолжайте компрессии грудной клетки и искусственные вдохи 30/2 (15/2 у детей до 8 лет), меняйте реаниматоров каждые 2-3 минуты', 'Каждые 3-5 минут повторяйте введение адреналина, следуйте командам АНД', 'С третьего разряда дефибрилляции введите амиодарон мг при отсутствии – лидокаин мг (пациентам старше 1 года)'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить', 'Выполнить', 'Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn2 w-100', 'btn btn-lg btn-outline-success btn3 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'hb28.7': {'prev':'hb24.3.5', 'next':'hd27.3', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Продолжайте компрессии грудной клетки и искусственные вдохи 30/2 (15/2 у детей до 8 лет), меняйте реаниматоров каждые 2-3 минуты', 'Каждые 3-5 минут повторяйте введение адреналина, следуйте командам АНД', 'С третьего разряда дефибрилляции введите амиодарон мг при отсутствии – лидокаин мг (пациентам старше 1 года)'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить', 'Выполнить', 'Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn2 w-100', 'btn btn-lg btn-outline-success btn3 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          'ja29': {'prev':'ja30', 'next': '', 'attr':{'base_url': 'test_fourth', 
                                                 'info': {'text': ['Боли в груди/ «жжение» за грудиной есть?'], 
                                                          'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                 'buttons': {'text': ["Да", "Нет"], 
                                                             'styles': ['btn btn-lg btn-outline-danger btn191 w-100', 'btn btn-lg btn-outline-success btn192 w-100']},
                                                 'navigation': {'text': ['В начало', 'Назад', 'Далее'], 
                                                                'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                 }},

          'jb29': {'prev':'ja30', 'next': '', 'attr':{'base_url': 'test_fourth', 
                                                 'info': {'text': ['Боли в груди/ «жжение» за грудиной есть?'], 
                                                          'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                 'buttons': {'text': ["Да", "Нет"], 
                                                             'styles': ['btn btn-lg btn-outline-danger btn191 w-100', 'btn btn-lg btn-outline-success btn192 w-100']}, 
                                                 'navigation': {'text': ['В начало', 'Назад', 'Далее'], 
                                                                'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                 }},

          'ja30': {'prev':'', 'next': '', 'attr':{'base_url': 'test_fourth', 
                                                 'info': {'text': ['Чувство нехватки воздуха, затруднения дыхания есть?'], 
                                                          'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                 'buttons': {'text': ["Да", "Нет"], 
                                                             'styles': ['btn btn-lg btn-outline-danger btn191 w-100', 'btn btn-lg btn-outline-success btn192 w-100']},
                                                 'navigation': {'text': ['В начало', 'Назад', 'Далее'], 
                                                                'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                 }},

          'ja31': {'prev':'', 'next': '', 'attr':{'base_url': 'test_fourth', 
                                                 'info': {'text': ['Боли в животе, рвота есть?'], 
                                                          'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                 'buttons': {'text': ["Да", "Нет"], 
                                                             'styles': ['btn btn-lg btn-outline-danger btn191 w-100', 'btn btn-lg btn-outline-success btn192 w-100']},
                                                 'navigation': {'text': ['В начало', 'Назад', 'Далее'], 
                                                                'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                 }},

          'ha32': {'prev':'ha13.2', 'next': '', 'attr':{'base_url': 'test_fourth', 
                                                 'info': {'text': ['Пациент старше 8 лет?'], 
                                                          'styles': ['alert alert-primary alert-dismissible fade show text-center']}, 
                                                 'buttons': {'text': ["Да", "Нет"], 
                                                             'styles': ['btn btn-lg btn-outline-success btn181 w-100', 'btn btn-lg btn-outline-danger btn182 w-100']},
                                                 'navigation': {'text': ['В начало', 'Назад', 'Далее'], 
                                                                'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                 }},

          'ha33.1': {'prev':'hb16', 'next':'hc27.1', 'attr':{'base_url': 'test_first', 
                                                  'info': {'text': ['Присоедините к лицевой маске (размер) или установленной ларингеальной маске (размер) дыхательный мешок', 'Выполните 5 искусственных вдохов при помощи дыхательного мешка', 'Делайте каждый вдох в течение 1 секунды, чтобы грудь заметно приподнималась'], 
                                                           'styles': ['alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center', 'alert alert-primary alert-dismissible fade show text-center']}, 
                                                  'buttons': {'text': ['Выполнить', 'Выполнить', 'Выполнить'], 
                                                              'styles': ['btn btn-lg btn-outline-success btn1 w-100', 'btn btn-lg btn-outline-success btn2 w-100', 'btn btn-lg btn-outline-success btn3 w-100']}, 
                                                  'navigation': {'text': ['В начало', 'Назад', 'Далее'],
                                                                 'styles': ['btn btn-lg btn-outline-primary w-100 btn-begining', 'btn btn-lg btn-secondary w-100 btn-back', 'btn btn-lg btn-outline-danger w-100 btn-next disabled'],
                                                                 'links': ['/to_beginning', '/prev_stage', '/next_stage']}
                                                  }},

          }