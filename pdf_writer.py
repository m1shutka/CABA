from stages import stages
from Crypto.Hash import SHA256
from Crypto.Random import get_random_bytes
from fpdf import FPDF

class PDFWirter():

    def __init__(self, folder, filename):

        h = SHA256.new()
        h.update(get_random_bytes(1) + bytes(filename, 'utf-8'))

        self.folder = folder
        self.filename = h.hexdigest()

    def write_file(self, session_stages, session_progress, session_timing):

        pdf = FPDF('P', 'mm', 'Letter')  
        pdf.add_page()
        pdf.add_font('DejaVu', '', 'fonts/dejavu-sans-condensed.ttf', uni=True)
        pdf.set_font('DejaVu', size=9)

        for i in range(1, len(session_stages)):

            if stages[session_stages[i][0]]['attr']['base_url'] == 'test_first':

                info = stages[session_stages[i][0]]['attr']['info']['text']

                for j in range(len(info)):
                    if session_progress[i][str(j + 1)]:
                        pdf.cell(40, 10, session_timing[i] + ' -- ' + info[j] + ' -> ' + 'Выполнено', new_x='LMARGIN', new_y='NEXT')

            elif stages[session_stages[i][0]]['attr']['base_url'] == 'test_second':
                
                buttons = stages[session_stages[i][0]]['attr']['buttons']['text']

                for j in range(len(buttons)):
                    if session_progress[i][str(j + 1)]:
                        pdf.cell(40, 10, session_timing[i] + ' -- ' + 'Определение веса и возраста: ' + buttons[j], new_x='LMARGIN', new_y='NEXT')

            elif stages[session_stages[i][0]]['attr']['base_url'] == 'test_third':

                info = stages[session_stages[i][0]]['attr']['info']['text']

                for j in range(len(info)):
                    if session_progress[i][str(2 * j + 1)]:
                        pdf.cell(40, 10, session_timing[i] + ' -- ' + info[j] + ' -> ' + 'Да', new_x='LMARGIN', new_y='NEXT')
                    else:
                        pdf.cell(40, 10, session_timing[i] + ' -- ' + info[j] + ' -> ' + 'Нет', new_x='LMARGIN', new_y='NEXT')

            elif stages[session_stages[i][0]]['attr']['base_url'] == 'test_fourth':
                
                info = stages[session_stages[i][0]]['attr']['info']['text']
                buttons = stages[session_stages[i][0]]['attr']['buttons']['text']

                for j in range(len(buttons)):
                    if session_progress[i][str(j + 1)]:
                        pdf.cell(40, 10, session_timing[i] + ' -- ' + info[0] + ' -> ' + buttons[j], new_x='LMARGIN', new_y='NEXT')

        pdf.output(f'reports/{self.filename}.pdf')
