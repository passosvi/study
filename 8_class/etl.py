import pandas as pd
import os
import glob

#uma funcao de extract que lê e consolida o json
def extract_concat_json(path:str) -> pd.DataFrame:
    arquivo_json =glob.glob(os.path.join(path,'*.json'))
    df_list =[pd.read_json(arquivo) for arquivo in arquivo_json]
    df_total = pd.concat(df_list, ignore_index =True)
    return df_total

#criando uma nova coluna a partir da multiplicação de outras duas colunas já existentes
def calculate_kpi_total_de_vendas(df: pd.DataFrame) -> pd.DataFrame:
    df["Total"] = df["Quantidade"] * df["Venda"]
    return df

#carregando dados, LOAD
def carregar_dados(df: pd.DataFrame, format_output: list):
    for format in format_output:
        if format == 'csv':
            df.to_csv("dados.csv")
        elif format == 'parquet':
            df.to_csv("dados.parquet")
        else:
            print("Nenhum formato condiz com o esperado")


def pipeline_calculo_kpi_vendas(pasta_argumento: str, saida: list):
    data_frame =extract_concat_json(pasta_argumento)
    data_frame_cal = calculate_kpi_total_de_vendas(data_frame)
    carregar_dados(data_frame_cal,saida)
