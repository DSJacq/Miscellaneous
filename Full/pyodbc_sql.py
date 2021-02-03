import schedule
import time
import os
import pyodbc
import pandas as pd
from datetime import datetime
import subprocess

def job():

        print('Connecting to SQL Server...')
        server = '10.128.223.38' 
        database = 'WFM' 
        username = 'MACKSEN' 
        password = 'Vivo#2019' 
        cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
        cursor = cnxn.cursor()
        print('Connection successful!')

        def tratarData(data):
            saida = datetime.strftime(data,'%Y-%m-%d %H:%M:%S.%f')
            saida = saida[:-3]
            return saida

        script = "SELECT ACIONAMENTO, (TQI_CODI + 3000000) AS TQI_CODI_OUT, SITUAÇÃO, Dt_Rec, TIE_ENDERECO, TIE_ENDERECO_TIPO, TIE_ENDERECO_NUM, TIE_ENDERECO_COMPL, TIE_BAIRRO, TIE_ESTADO_CODIGO, TIE_ESTADO_NOME, TIE_MUNICIPIO_NOME, TIE_PONTA, TIE_LOCALIDADE_CODIGO, TIE_LOCALIDADE_NOME, TIE_AREA_CODIGO, TIE_AREA_NOME, TECNICO, tni_nome, TIE_ESCRITORIO_CODIGO, TIE_ESCRITORIO_NOME, TIS_CLIENTE_SEGMENTO, ACI_DATA_CRIACAO, tis_lp, poi_nome, EMPRESA, produto, TECNOLOGIA, COD_ACIO_ANTERIOR, TQI_TIPO_ABERTURA, TQI_RESPONSAVELPOR_GRUPO, tis_cliente_titular, TQI_DATA_PREVISAO, TIS_SERVICO_CPCC, TIPO_RECLAMAÇÃO, QUANTIDADE_PARES, NATUREZA_ATIVIDADE, re_tecnico, descricao, telefone, tis_velocidade, CASE WHEN NATUREZA_ATIVIDADE = 'REPARO' THEN -1 ELSE 'OSX' END, CASE WHEN NATUREZA_ATIVIDADE = 'REPARO' THEN -1 ELSE 'TRE' END FROM dbo.TBL_MAKSEN_ON_LINE"

        df = pd.read_sql_query(script, cnxn)
        df.Dt_Rec = pd.to_datetime(df.Dt_Rec)
        df.Dt_Rec = df.Dt_Rec.apply(tratarData)
        df.ACI_DATA_CRIACAO = pd.to_datetime(df.ACI_DATA_CRIACAO)
        df.ACI_DATA_CRIACAO = df.ACI_DATA_CRIACAO.apply(tratarData)
        df.TQI_DATA_PREVISAO = pd.to_datetime(df.TQI_DATA_PREVISAO)
        df.TQI_DATA_PREVISAO = df.TQI_DATA_PREVISAO.apply(tratarData)

        filename = 'B2B_VIVO_' + datetime.now().strftime('%Y%m%d_%H_%M')
        writer = pd.ExcelWriter(filename +'.xlsx')
        df.to_excel(writer, header = False, index=False)
        writer.save()

        subprocess.call('java -jar upload_azure.jar ' + filename + '.xlsx')
        print('Export to Azure successful!')

        if os.path.exists(filename + ".xlsx"):
            os.remove(filename + ".xlsx")
        else:
            print("The file does not exist")

        print('File removed from directory B2B.')
        print('Process finished at ' + datetime.now().strftime('%Y/%m/%d %H:%M:%S'))

schedule.every(1).minutes.do(job)
schedule.every().hour.do(job)
schedule.every().day.at("15:30").do(job)

while 1:
    schedule.run_pending()
    
