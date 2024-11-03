from dotenv import load_dotenv
from models import User, App
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
import os
from Crypto.Cipher import Salsa20
from Crypto.Hash import SHA256


class DBApi():

    def init(self):
        pass

    def user_registration(self, user_login_reg: str, user_pass_reg: str, product_key: str) -> str:

        with Session(autoflush=False, bind=create_engine(f"postgresql://postgres:postgres@localhost:5432/crypto")) as db:

            exist_user = db.query(User).filter(User.login==user_login_reg).first()
            if exist_user == None:


                cipher = Salsa20.new(key=b'\x9eKY\xaaT\xf10u7\xf8\xaf\x19\x8b7\x132E\x86\xb5V\xb3\xd1\x8b\nE\xac\x90\xa7/U\xa6\x81')
                solt = cipher.nonce + cipher.encrypt(bytes(user_login_reg, 'utf-8'))
                h = SHA256.new()
                h.update(solt + bytes(user_pass_reg, 'utf-8'))

                db.add(User(login=user_login_reg, solt=solt, password=h.hexdigest(), isAdmin=False))
                db.commit()

                return 'Зарегестрировано'
                    
            else:      
                return 'Пользователь с таким логином уже существует!'


    def user_autorization(self, user_login_auto: str, user_pass_auto:str) -> str:

        with Session(autoflush=False, bind=create_engine(f'mysql://{os.getenv("ADMIN_NAME")}:{os.getenv("ADMIN_PASSWORD")}@{os.getenv("HOST")}/{os.getenv("DB_NAME")}')) as db:

            user = db.query(User).filter(User.login==user_login_auto).first()
            if user != None:

                h = SHA256.new()
                h.update(user.solt + bytes(user_pass_auto, 'utf-8'))

                if user.password == h.hexdigest():
                    return {'id':user.record_id, 'login':user.login, 'is_admin':user.isAdmin}
                else:
                    return None
                    
            else:
                return None

    def getUserInfo(self, user_id):
        with Session(autoflush=False, bind=create_engine(f'mysql://{os.getenv("ADMIN_NAME")}:{os.getenv("ADMIN_PASSWORD")}@{os.getenv("HOST")}/{os.getenv("DB_NAME")}')) as db:

            user = db.query(User).filter(User.record_id==user_id).first()
            if user != None:
                return {'id':user.record_id, 'login':user.login, 'is_admin':user.isAdmin}
            else:
                return None

    def getMenu(self, login, root):
        print(login, root)
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

        exist_user = db.query(User).filter(User.login=='test_user1').first()
        if exist_user == None:

            cipher = Salsa20.new(key=b'\x9eKY\xaaT\xf10u7\xf8\xaf\x19\x8b7\x132E\x86\xb5V\xb3\xd1\x8b\nE\xac\x90\xa7/U\xa6\x81')
            solt = cipher.nonce + cipher.encrypt(bytes('m_admin', 'utf-8'))
            h = SHA256.new()
            h.update(solt + bytes('password12345', 'utf-8'))

            db.add(User(login='test_user1', solt=solt, password=h.hexdigest(), isAdmin=False, isPrime=True, fdevice='all', sdevice='all'))
            db.commit()
                       
               