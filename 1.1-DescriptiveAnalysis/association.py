import pandas as pd
import matplotlib.pyplot as plt

def covariance():
    print("Covariância")
    input_file = '0-Datasets/echocardiogramClear.data'
    names = ['survival','still-alive','age-at-heart-attack','pericardial-effusion','fractional-shortening', 'epss', 'lvdd', 'wall-motion-score', 'wall-motion-index', 'alive-at-1']

    df = pd.read_csv(input_file, names = names)
    
    covariance = df['alive-at-1'].cov(df['age-at-heart-attack'])
    print("Covariância entre a variável survival e a variável still-alive = " + str(covariance))

def correlation():
    print("Correlação")
    input_file = '0-Datasets/echocardiogramClear.data'
    names = ['survival','still-alive','age-at-heart-attack','pericardial-effusion','fractional-shortening', 'epss', 'lvdd', 'wall-motion-score', 'wall-motion-index', 'alive-at-1']

    df = pd.read_csv(input_file, names = names)
    
    correlation = df['alive-at-1'].corr(df['age-at-heart-attack'])
    print("Correlação entre a variável survival e a variável still-alive = " + str(correlation))

# Scatter Plot age-at-heart-attack vs alive-at-1
def scatterPlot():
    input_file = '0-Datasets/echocardiogramClear.data'
    names = ['survival','still-alive','age-at-heart-attack','pericardial-effusion','fractional-shortening', 'epss', 'lvdd', 'wall-motion-score', 'wall-motion-index', 'alive-at-1']
    df = pd.read_csv(input_file, names = names)
    df_age = (df['age-at-heart-attack'])
    df_alive = (df['alive-at-1'])
    plt.scatter(df_alive, df_age)
    plt.savefig('1.1-DescriptiveAnalysis/dispersionChart.png', format='png')
    plt.show()

def main():
    covariance()
    correlation()
    scatterPlot()

if __name__ == "__main__":
    main()