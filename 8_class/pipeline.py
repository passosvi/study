from etl import pipeline_calculo_kpi_vendas 

pasta_argumento = 'data'
saida: list = ["parquet"]
pipeline_calculo_kpi_vendas(pasta_argumento,saida)
