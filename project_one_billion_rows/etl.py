import csv
from typing import List

path_file = "vendas.csv"

def ler_csv(nome: str) -> list[dict]:
    """Fução para ler o arquivo
    """
    lista =[]
    with open(nome, mode='r', encoding ='utf-8') as arquivo:
        leitor = csv.DictReader(arquivo)
        for item in leitor:
            lista.append(item)
    return lista

def filtrar_true(lista: List[dict]) -> list[dict]:
    """Fução para filtrar produtos onde o entregue seja True
    """
    lista_produtos_filtrados =[]
    for produto in lista:
        if produto.get("entregue") == "True":
            lista_produtos_filtrados.append(produto)
    return lista_produtos_filtrados

def somar(lista: List[dict]) -> int:
    """Soma produtos onde o entregue seja True
    """
    soma = 0
    for produto in lista:
        soma += int(produto.get("preco"))
    return soma

leitura = ler_csv(path_file)
entregues = filtrar_true(leitura)
print(somar(entregues))