# Vamos revisar funções adicionando type hints e Pydantic
from typing import List
# 1. Calcular Média de Valores em uma Lista

lista : List[int] = [1, 4, 8, 9 , 15, 18]
def meanlist(a:List[int]) -> float:
    return f"{sum(a)/len(a):.2f}"
print(meanlist(lista))

# 2. Filtrar Dados Acima de um Limite
def filter(a:List[int]) -> int:
    lista_filtrada =[]
    for i in a:
        if i > 6:
             lista_filtrada.append(i)
        else:
             pass
    return lista_filtrada

listinha =[7,1,2,3,9,8,5,4,7,12,4]
print(filter(listinha))
            
    
# 3. Contar Valores Únicos em uma Lista ---> function set ordered unique values
def uniquevalues(parameter:List[int]) -> int:
    return(len(set(parameter)))
listinha = [1,2,2,4,65,7,1,1,57,57,3,2]
print(uniquevalues(listinha))

# 4. Converter Celsius para Fahrenheit em uma Lista
def conversor(parameter : List[float]) -> List[float]:
     return [f"{(9/5) * temp + 32:.2f}" for temp in parameter]
lista=[29.6,28.1,30]
print(conversor(lista))
# 5. Calcular Desvio Padrão de uma Lista
def calcular_desvio_padrao(valores: List[float]) -> float:
    media = sum(valores) / len(valores)
    variancia = sum((x - media) ** 2 for x in valores) / len(valores)
    return variancia ** 0.5
# 6. Encontrar Valores Ausentes em uma Sequência
def encontrar_valores_ausentes(sequencia: List[int]) -> List[int]:
     completo = set(range(min(sequencia), max(sequencia) + 1))
     return list(completo - set(sequencia))