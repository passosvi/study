from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.declarative import declarative_base

# Define base class
Base = declarative_base()

# Initialize SQLite engine
try:
    engine = create_engine('sqlite:///C:/Users/vitor/workspace/study/17_class_/desafio.db', echo=True)
    print("Conexão com SQLite estabelecida.")
except Exception as e:
    print(f"Não conectou: {e}")

# Define Usuario class
class Usuario(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True)
    nome = Column(String)
    idade = Column(Integer)

# Define Fornecedor class
class Fornecedor(Base):
    __tablename__ = 'fornecedor'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String)
    telefone = Column(Integer)
    email = Column(String)
    endereco = Column(String)

# Create tables in the database
Base.metadata.create_all(engine)

# Create session factory
Session = sessionmaker(bind=engine)

# Insert records into the Fornecedor table
session = Session()
try:
    fornecedores = [
        Fornecedor(nome='Maria', telefone=97546854, email='zzz.@gmail', endereco='rua A'),
        Fornecedor(nome='Jose', telefone=97546854, email='jjj.@gmail', endereco='rua B'),
        Fornecedor(nome='Tadeu', telefone=97546854, email='ttt.@gmail', endereco='rua C')
    ]
    session.add_all(fornecedores)
    session.commit()
    print("Fornecedores inseridos com sucesso.")
except SQLAlchemyError as e:
    session.rollback()
    print(f"Erro ao inserir fornecedores: {e}")
finally:
    session.close()
