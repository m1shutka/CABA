from dotenv import load_dotenv
from models import User
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

                #validate_key = db.query(Keys).filter(Keys.key==product_key).first()
                #if validate_key != None and validate_key.isActivated != True:

                    #validate_key.isActivated = True

                    cipher = Salsa20.new(key=b'\x9eKY\xaaT\xf10u7\xf8\xaf\x19\x8b7\x132E\x86\xb5V\xb3\xd1\x8b\nE\xac\x90\xa7/U\xa6\x81')
                    solt = cipher.nonce + cipher.encrypt(bytes(user_login_reg, 'utf-8'))
                    h = SHA256.new()
                    h.update(solt + bytes(user_pass_reg, 'utf-8'))

                    db.add(User(login=user_login_reg, solt=solt, password=h.hexdigest(), isAdmin=False))
                    db.commit()

                    return 'Зарегестрировано'

                #else:
                    #return 'Неверный ключ продукта!'
                    
            else:      
                return 'Пользователь с таким логином уже существует!'


    def user_autorization(self, user_login_auto: str, user_pass_auto:str) -> str:

        with Session(autoflush=False, bind=create_engine(f"postgresql://postgres:postgres@localhost:5432/crypto")) as db:

            user = db.query(User).filter(User.login==user_login_auto).first()
            if user != None:

                h = SHA256.new()
                h.update(user.solt + bytes(user_pass_auto, 'utf-8'))

                if user.password == h.hexdigest():
                    
                    self.__user_login = user.login

                    if user.isAdmin:
                        self.__isAdmin = True

                    else:
                        self.__isAdmin = False

                    return 'Вход успешен'
                else:
                    return 'Неверный логин или пароль!'
                    
            else:
                return 'Пользователя с таким логином не существует!'



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

    
    engine = create_engine(f'mysql://{name}:{password}@{host}/{db}')