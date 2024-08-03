from dotenv import load_dotenv
from sqlalchemy import create_engine, Column, Integer, String, LargeBinary, BOOLEAN
from sqlalchemy.orm import DeclarativeBase, Session
import os

class Base(DeclarativeBase): pass

class User(Base):
    __tablename__ = "users"
    record_id = Column(Integer, primary_key=True, index=True)
    login = Column(String(30))
    password = Column(String(30))
    solt = Column(LargeBinary)
    isAdmin = Column(BOOLEAN)
    isPrime = Column(BOOLEAN)
    fdevice = Column(String(30))
    sdevice = Column(String(30))


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



