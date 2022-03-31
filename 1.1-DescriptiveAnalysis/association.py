import pandas as pd

def covariance():
    print("Covariância")
    input_file = '0-Datasets/echocardiogramClear.data'
    names = ['survival','still-alive','age-at-heart-attack','pericardial-effusion','fractional-shortening', 'epss', 'lvdd', 'wall-motion-score', 'wall-motion-index', 'alive-at-1']

    df = pd.read_csv(input_file, names = names)
    
    covariance = df['survival'].cov(df['still-alive'])
    print("Covariância entre a variável survival e a variável still-alive = " + str(covariance))

def correlation():
    print("Correlação")
    input_file = '0-Datasets/echocardiogramClear.data'
    names = ['survival','still-alive','age-at-heart-attack','pericardial-effusion','fractional-shortening', 'epss', 'lvdd', 'wall-motion-score', 'wall-motion-index', 'alive-at-1']

    df = pd.read_csv(input_file, names = names)
    
    correlation = df['survival'].corr(df['still-alive'])
    print("Correlação entre a variável survival e a variável still-alive = " + str(correlation))


def main():
    covariance()
    correlation()

if __name__ == "__main__":
    main()