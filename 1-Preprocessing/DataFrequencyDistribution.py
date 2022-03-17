from math import ceil
import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

def main():
    # Faz a leitura do arquivo
    input_file = '0-Datasets/echocardiogramClear.data'
    names = ['survival','still-alive','age-at-heart-attack','pericardial-effusion','fractional-shortening', 'epss', 'lvdd', 'wall-motion-score', 'wall-motion-index', 'mult', 'group', 'alive-at-1']
    df = pd.read_csv(input_file,    # Nome do arquivo com dados
                     names = names) # Nome das colunas                      
    # ShowInformationDataFrame(df,"Dataframe original")

    ##Passos a serem implementados##

    #Imprimir todos os atributos idade de pessoas que tem um ataque cardíaco
    df_age = (df['age-at-heart-attack'])
    #df_age.sort_values(ascending=True)

    #Idade Mínima e Máxima que as pessoas que tem um ataque cardíaco
    age_min = int(df.min()[['age-at-heart-attack']])
    age_max = int(df.max()[['age-at-heart-attack']])

    #Definir o número de classes
    number_classes =  6

    #Calcular a amplitude de classe
    range = ceil((age_max - age_min)/number_classes)
    print(range)



    #Definir os limites inferiores e superiores das classes
    frequencias = []
    valor = age_min
    while valor < age_max:
        frequencias.append('{} - {}'.format(round(valor,1),round(valor+range,1)))
        valor += range

    print(frequencias)

    #Rotular os valores dos atributos de acordo com sua classe
  
    freq_abs = pd.qcut(df_age,len(frequencias),labels=frequencias) # Discretização dos valores em k faixas, rotuladas pela lista criada anteriormente
    print(pd.value_counts(freq_abs))
    print(freq_abs)


def ShowInformationDataFrame(df, message=""):
    print(message+"\n")
    print(df.info())
    print(df.describe())
    print(df.head(10))
    print("\n")
    
if __name__ == "__main__":
    main()