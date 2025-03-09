from dotenv import load_dotenv
import os
import smtplib
from email.mime.text import MIMEText
from email.header import Header

load_dotenv()

def send_ya_mail(msg_info: dict):

    password = os.getenv("YA_PASS")
    login = os.getenv("YA_LOGIN")

    msg = MIMEText(f'{msg_info["text"]}', 'plain', 'utf-8')
    msg['Subject'] = Header(f'{msg_info["header"]}', 'utf-8')
    msg['From'] = login
    msg['To'] = msg_info["to"]

    s = smtplib.SMTP('smtp.yandex.ru', 587, timeout=10)
    error = 'Success'

    try:
        s.starttls()
        s.login(login, password)
        s.sendmail(msg['From'], msg_info["to"], msg.as_string())
        s.sendmail(msg['From'], msg['From'], msg.as_string())
    except Exception as ex:
        error = ex
    finally:
        s.quit()

    return error


if __name__ == '__main__':
    print(send_ya_mail(msg_info={'to':'maihailovsky18@mail.ru', 'header': 'Данные учетной записи САВА', 'text':f'Логин: login\nПароль: password'}))