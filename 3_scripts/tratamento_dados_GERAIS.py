import os
import pandas as pd
import numpy as np
import missingno as msno
import plotly.express as px
from datetime import datetime

#PASTA BASE COM OS ARQUIVOS CSV
pasta_arquivos_csv = "../0_bases_originais_CSV/"

# CRIANDO O DATAFRAME COM LISTA DOS MESES PARA FAZER O LOOPING PRA FICAR MAIS FÁCIL DE LER E CONCATENAR
dfs = [pd.read_csv(os.path.join(pasta_arquivos_csv, arquivo), sep=';', encoding='utf-8')
for arquivo in os.listdir(pasta_arquivos_csv)
if arquivo.endswith(".csv")]

# CONCATENANDO TUDO E CRIANDO UM ÚNICO ARQUIVO CSV
dados_geral = pd.concat(dfs, ignore_index=True)

# EXIBE TODAS AS COLUNAS INDEPENDENTE DA QUANTIDADE
pd.set_option('display.max_columns', None)

# DEIXA O NOME DAS COLUNAS EM MINUSCULO
dados_geral.columns = dados_geral.columns.str.lower()

dados_geral['modelo_veic'] = dados_geral['descr_marca_veiculo'].str.split('/').str[1]
dados_geral['marca_veic'] = dados_geral['descr_marca_veiculo'].str.split('/').str[0]

dados_geral['dataocorrencia'] = dados_geral['dataocorrencia'].astype(str)
dados_geral['mes'] = dados_geral['dataocorrencia'].str[3:4]
dados_geral['ano'] = dados_geral['dataocorrencia'].str[4:10]
dados_geral['mes_ocorrencia'] = dados_geral['mes'] + dados_geral['ano']

#
dados_geral['ano_modelo']=dados_geral.ano_modelo.astype(str)
dados_geral['ano_modelo']=dados_geral.ano_modelo.str[:4]

dados_geral = dados_geral.drop(columns=['ano_bo','num_bo','numero_boletim','bo_iniciado','bo_emitido','dataocorrencia','horaocorrencia','datacomunicacao',
'dataelaboracao','bo_autoria','flagrante','numero_boletim_principal','logradouro','numero','bairro','uf','latitude','longitude','exame','solucao',
'delegacia_nome','delegacia_circunscricao','especie','desdobramento','status','tipopessoa','vitimafatal','sexo','datanascimento','idade',
'estadocivil','profissao','grauinstrucao','naturezavinculada','tipovinculo','relacionamento', 'parentesco','placa_veiculo','uf_veiculo',
'descr_marca_veiculo','ano_fabricacao','naturalidade','nacionalidade','corcutis', 'quant_celular','marca_celular','mes','ano'])


# SALVANDO OS ARQUIVOS COMPILADOS E CRIANDO UM NOVO ARQUIVO DENTRO DA PASTA BASE TRATADAS
salvar_pasta = '../1_bases_tratadas/dados_GERAL.csv'
dados_geral.to_csv(salvar_pasta, index=False)