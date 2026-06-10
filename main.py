from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
import os

# Força a criação do ficheiro exatamente na raiz da pasta do projeto
BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
DB_PATH = os.path.join(BASE_DIR, "hospital.db")

# A configuração 'check_same_thread=False' é vital para o SQLite funcionar com GUIs
engine = create_engine(
    f"sqlite:///{DB_PATH}", 
    connect_args={"check_same_thread": False},
    echo=False
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def obter_sessao():
    sessao = SessionLocal()
    try:
        yield sessao
    finally:
        sessao.close()