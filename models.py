from dotenv import load_dotenv
from sqlalchemy import create_engine, Column, Integer, String, LargeBinary, BOOLEAN
from sqlalchemy.orm import DeclarativeBase, Session
import os

class Base(DeclarativeBase): pass

class User(Base):
    __tablename__ = "users"
    record_id = Column(Integer, primary_key=True, index=True)
    login = Column(String(30))
    password = Column(String(100))
    solt = Column(LargeBinary)
    isAdmin = Column(BOOLEAN)
    isPrime = Column(BOOLEAN)
    fdevice = Column(String(30))
    sdevice = Column(String(30))

class App(Base):
    __tablename__ = 'app'
    record_id = Column(Integer, primary_key=True, index=True)
    frame_name = Column(String(30))
    frame_url = Column(String(30))
    root = Column(BOOLEAN)
    login = Column(BOOLEAN)


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

    Base.metadata.create_all(bind=engine)

    with Session(autoflush=False, bind=create_engine(f'mysql://{name}:{password}@{host}/{db}')) as db:

        db.add(App(frame_name='Главная', frame_url='/main', root = False, login = False))
        db.add(App(frame_name='Справка', frame_url='/info', root = False, login = False))
        db.add(App(frame_name='Войти', frame_url='/login', root = False, login = False))

        db.add(App(frame_name='Главная', frame_url='/main', root = False, login = True))
        db.add(App(frame_name='Справка', frame_url='/info', root = False, login = True))
        db.add(App(frame_name='Учетная запись', frame_url='/profile', root = False, login = True))

        db.add(App(frame_name='Главная', frame_url='/main', root = True, login = True))
        db.add(App(frame_name='Справка', frame_url='/info', root = True, login = True))
        db.add(App(frame_name='Учетная запись', frame_url='/profile', root = True, login = True))
        db.add(App(frame_name='Регистрация', frame_url='/registration', root = True, login = True))
        db.commit()



