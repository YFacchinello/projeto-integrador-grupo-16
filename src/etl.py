import pandas as pd
import numpy as np
import os

def executar_etl():
    caminho_original = "personal_transactions.csv" if os.path.exists("personal_transactions.csv") else "data/personal_transactions.csv"
    caminho_destino = "base_tratada.csv"
    
    if not os.path.exists(caminho_original):
        return

    df = pd.read_csv(caminho_original)
    
    mapeamento_colunas = {
        'Date': 'Data',
        'Category': 'Categoria',
        'Amount': 'Valor'
    }
    df = df.rename(columns=mapeamento_colunas)
    
    df['Data'] = pd.to_datetime(df['Data'], errors='coerce')
    df = df.dropna(subset=['Data', 'Valor'])
    
    df['Tipo'] = np.where(df['Transaction Type'] == 'credit', 'Entrada', 'Saída')
    df['Valor_Absoluto'] = df['Valor'].abs()
    df['Ano'] = df['Data'].dt.year
    
    meses_pt = {
        1: "Janeiro", 2: "Fevereiro", 3: "Março", 4: "Abril",
        5: "Maio", 6: "Junho", 7: "Julho", 8: "Agosto",
        9: "Setembro", 10: "Outubro", 11: "Novembro", 12: "Dezembro"
    }
    df['Mes'] = df['Data'].dt.month.map(meses_pt)
    df['Ano_Mes'] = df['Data'].dt.to_period('M').astype(str)
    
    df.to_csv(caminho_destino, index=False)
    
    if os.path.exists("data"):
        df.to_csv("data/base_tratada.csv", index=False)

if __name__ == "__main__":
    executar_etl()