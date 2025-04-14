import requests
import json
import pprint
from pydantic import BaseModel
#requests.get #select
#requests.post #insert/create
#requests.put #update
#requests.delete #delete
#pydantic faz validação dos dados e desceralizada, transformando o json em um objeto python

class PokemonSchema(BaseModel): #contrato de dados, schema de recebimento padrão
    bunting:bool
    data:str
    notes: str

    #class Config:
     #   orm_mode = True


def pegar_pokemon(dates:str):
    url = 'https://www.gov.uk/bank-holidays.json?ref=public_apis&utm_medium=website'
    response = requests.get(url)
    data = response.json()
    listin =[]
    for i in data.items():
        if i == dates:
            listin.append(data['date,notes,title'])
    return i[0]

x = '2020-05-25'

print(pegar_pokemon(x))


#pydantic faz uma validação do schema e tipo de dados, para isso precisa instalar e criar uma classe