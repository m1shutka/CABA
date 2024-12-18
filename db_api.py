from dotenv import load_dotenv
from models import User, App
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
import os
from Crypto.Cipher import Salsa20
from Crypto.Hash import SHA256
from datetime import datetime, timedelta
from math import ceil
import string
import random


class DBApi():

    def generate_password(self, n = 12):
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(n))
        return password

    def user_registration(self, user_name_reg: str, user_email_reg: str, user_phone_reg: str, months: str):

        with Session(autoflush=False, bind=create_engine(f'mysql://{os.getenv("ADMIN_NAME")}:{os.getenv("ADMIN_PASSWORD")}@{os.getenv("HOST")}/{os.getenv("DB_NAME")}')) as db:

            exist_user = db.query(User).filter(User.email==user_email_reg).first()
            if exist_user == None:
                
                login = user_email_reg[:user_email_reg.index('@')]
                password = self.generate_password()

                cipher = Salsa20.new(key=os.getenv("PSWRD_KEY").encode("utf-8"))
                solt = cipher.nonce + cipher.encrypt(bytes(login, 'utf-8'))
                h = SHA256.new()
                h.update(solt + bytes(password, 'utf-8'))

                date = datetime.now()
                total_date=(date + timedelta(days=ceil(365/12*int(months))))

                db.add(User(name=user_name_reg, phone_number=user_phone_reg, email=user_email_reg, login=login, solt=solt, password=h.hexdigest(), isAdmin=False, device='', registration_time=date.strftime('%Y-%m-%d %H:%M:%S'), subscribe_time=total_date.strftime('%Y-%m-%d %H:%M:%S')))
                db.commit()

                return f'Зарегестрировано, login: {login}, password: {password}'
                    
            else:      
                
                date = datetime.strptime(exist_user.subscribe_time, '%Y-%m-%d %H:%M:%S')
                total_date=(date + timedelta(days=ceil(365/12*int(months))))
                exist_user.subscribe_time = total_date.strftime('%Y-%m-%d %H:%M:%S')
                db.commit()

                return 'Пользователь продлен'


    def user_autorization(self, user_login_auto: str, user_pass_auto: str, user_agent: str):

        with Session(autoflush=False, bind=create_engine(f'mysql://{os.getenv("ADMIN_NAME")}:{os.getenv("ADMIN_PASSWORD")}@{os.getenv("HOST")}/{os.getenv("DB_NAME")}')) as db:

            user = db.query(User).filter(User.login==user_login_auto).first()
            if user != None:

                h = SHA256.new()
                h.update(user.solt + bytes(user_pass_auto, 'utf-8'))

                if user.password == h.hexdigest():

                    if datetime.strptime(user.subscribe_time, '%Y-%m-%d %H:%M:%S') > datetime.now():

                        #print(user_agent in user.device.split('%') )
                        print(user.device.split('%'))
                        new_addr = user_agent['string'] + '$' + user_agent['addr']
                        print(new_addr)
                        if user.device == 'all':
                            return {'id':user.record_id, 'login':user.login, 'is_admin':user.isAdmin}

                        elif len(user.device.split('%')) == 0:
                            user.device = new_addr
                            db.commit()
                            return {'id':user.record_id, 'login':user.login, 'is_admin':user.isAdmin}

                        elif new_addr in user.device.split('%') and len(user.device.split('%')) == 1:
                            return {'id':user.record_id, 'login':user.login, 'is_admin':user.isAdmin}

                        elif new_addr in user.device.split('%') and len(user.device.split('%')) == 2:
                            return {'id':user.record_id, 'login':user.login, 'is_admin':user.isAdmin}

                        elif new_addr not in user.device.split('%') and len(user.device.split('%')) == 1:
                            user.device += '%' + new_addr
                            db.commit()
                            return {'id':user.record_id, 'login':user.login, 'is_admin':user.isAdmin}

                        elif user_agent not in user.device.split('%') and len(user.device.split('%')) == 2:
                            return 'Превышено число подключенных устройств!'

                        else:
                            return 'Ошибка!'

                    else:
                         return 'Необходимо продлить подписку!'

                else:
                    return 'Неверный логин/пароль!'
                    
            else:
                return 'Пользователя с таким логином не существует!'

    def getUserInfo(self, user_id):

        with Session(autoflush=False, bind=create_engine(f'mysql://{os.getenv("ADMIN_NAME")}:{os.getenv("ADMIN_PASSWORD")}@{os.getenv("HOST")}/{os.getenv("DB_NAME")}')) as db:

            user = db.query(User).filter(User.record_id==user_id).first()
            if user != None:
                return {'id':user.record_id, 'login':user.login, 'is_admin':user.isAdmin}
            else:
                return None

    def getMenu(self, login, root):
 
        menu_list = []

        with Session(autoflush=False, bind=create_engine(f'mysql://{os.getenv("ADMIN_NAME")}:{os.getenv("ADMIN_PASSWORD")}@{os.getenv("HOST")}/{os.getenv("DB_NAME")}')) as db:

            menu = db.query(App).filter(App.login==login, App.root==root).all()
            for i in menu:
                menu_list.append([i.frame_name, i.frame_url])

            return menu_list



if __name__ == '__main__':
    load_dotenv()

    name = os.getenv("ADMIN_NAME")
    password = os.getenv("ADMIN_PASSWORD")
    host = os.getenv("HOST")
    db = os.getenv("DB_NAME")

    print(name)
    print(password)
    print(host)
    print(db)

    with Session(autoflush=False, bind=create_engine(f'mysql://{name}:{password}@{host}/{db}')) as db:

        exist_user = db.query(User).filter(User.login=='m_admin').first()
        if exist_user == None:
            cipher = Salsa20.new(key=os.getenv("PSWRD_KEY").encode("utf-8"))
            solt = cipher.nonce + cipher.encrypt(bytes('m_admin', 'utf-8'))
            h = SHA256.new()
            h.update(solt + bytes('mikel112358', 'utf-8'))

            db.add(User(name='m_admin',phone_number='88005553535', email='admin@mail.ru', login='m_admin', solt=solt, password=h.hexdigest(), isAdmin=False, device='all', registration_time=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), subscribe_time=(datetime.now() + timedelta(weeks=100)).strftime('%Y-%m-%d %H:%M:%S')))
            db.commit()
                       
               