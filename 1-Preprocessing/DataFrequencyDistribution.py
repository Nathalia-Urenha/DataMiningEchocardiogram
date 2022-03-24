from math import ceil
import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
plt.style.use('ggplot')

def main():
    # Faz a leitura do arquivo
    input_file = '0-Datasets/echocardiogramClear.data'
    names = ['survival','still-alive','age-at-heart-attack','pericardial-effusion','fractional-shortening', 'epss', 'lvdd', 'wall-motion-score', 'wall-motion-index', 'alive-at-1']
    
    df = pd.read_csv(input_file, names = names)                     

    #Atributos idade de pessoas que tem um ataque cardíaco
    df_age = (df['age-at-heart-attack'])
    array_age = df_age.tolist()
    print(array_age)
    

    #Idade Mínima e Máxima que as pessoas que tem um ataque cardíaco
    age_min = int(df.min()[['age-at-heart-attack']])
    age_max = int(df.max()[['age-at-heart-attack']])

    #Definir o número de classes
    number_classes =  6

    #Calcular a amplitude de classe
    range = ceil((age_max - age_min)/number_classes)



    #Definir os limites inferiores e superiores das classes
    frequencias = []
    valor = age_min
    while valor < age_max:
        frequencias.append('{} - {}'.format(round(valor,1),round(valor+range,1)))
        valor += range

    print('frequencias', frequencias)

    #Rotular os valores dos atributos de acordo com sua classe
    freq_abs = pd.qcut(df_age,len(frequencias),labels=frequencias) # Discretização dos valores em k faixas, rotuladas pela lista criada anteriormente
    print(freq_abs)
    
    #quantidade de atributos idade que tem em cada classe
    qtd_atr = (pd.value_counts(freq_abs)) 
    print('Quantidade de atributos em cada classe', qtd_atr)

    #Histograma do atributo idade
    bin = []
    for number in frequencias:
        bin.append(int(number[0:3]))

    last_range = frequencias.pop()

    bin.append(int(last_range[5:7]))

    
    plt.xlabel("Idade")
    plt.ylabel("Distribuição da idade")
    plt.title("Histograma de Distribuição de idade")
    plt.xlim(35, 89)
    plt.xticks(bin)
    plt.hist(array_age, bins=bin, edgecolor='black')
    plt.savefig('1-Preprocessing/histogram.png', format='png')
    plt.show()
    

def ShowInformationDataFrame(df, message=""):
    print(message+"\n")
    print(df.info())
    print(df.describe())
    print(df.head(10))
    print("\n")
    
if __name__ == "__main__":
    main()