#framework para produzir API de forma mais simples possivel

#API são rotas que dão acessos para algum servico(CreateReadUpdateDelete)
from fastapi import FastAPI
# gera numero, nomes aleatorios fake
from faker import Faker
import pandas as pd
import random

app = FastAPI(debug = True)
fake = Faker()

file_name = '.csv'

#assincrono, ela nao é sincronizada.

@app.get("/")
async def primeira():
    return 'Olha só'


print(fake.name())