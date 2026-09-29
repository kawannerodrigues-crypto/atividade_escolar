import pandas as pd

#1 carrega a planilha para dentro de uma estrutura chamada DataFrame(df)

#se o seu arquivo for .csv, mude para: pd.read_csv("dados.csv")

df = pd.read_csv("kaka.csv")

#print(df)

#print(df.info()) #MOstra informações sobre o Datafame, como número de linhas,colunas e tipos de dados

#print(df.describe()) #mostra estatíticas descritivas das colunas númerica do DataFrome

print(df.drop_duplicates()) #Remove linhas duplicadas da Dataframe e exibe o resultado