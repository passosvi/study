from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base,sessionmaker

# Conectar ao SQLite em memória
try:
    engine = create_engine('sqlite:///C:/Users/vitor/sqlite.db', echo=True)
    print("Conexão com SQLite estabelecida.")
except Exception as e:
    print(f"Não conectou: {e}")

# Define the base class for declarative models
Base = declarative_base()

# Define the Usuario table
class Usuario(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True)
    nome = Column(String)
    idade = Column(Integer)

# Create the table in the database
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

novo_usuario = Usuario(nome='João', idade=28)
session.add(novo_usuario)
session.commit()

print("Usuário inserido com sucesso.")