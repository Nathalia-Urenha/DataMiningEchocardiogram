import pandas as pd
import statistics

def main():
    input_file = '0-Datasets/echocardiogramClear.data'
    names = ['survival','still-alive','age-at-heart-attack','pericardial-effusion','fractional-shortening', 'epss', 'lvdd', 'wall-motion-score', 'wall-motion-index', 'alive-at-1']

    df = pd.read_csv(input_file, names = names)  

    age = df['age-at-heart-attack'].tolist()
    sortedAge = sorted(df['age-at-heart-attack'].tolist())

    meanAge = df['age-at-heart-attack'].mean()
    modeAge = df['age-at-heart-attack'].mode()
    medianAge = statistics.median(age)
    mediumPointAge = (sortedAge[0] + sortedAge[len(sortedAge)-1])/2

    print("Média de pessoas que sofreram de ataques cardíacos")
    print("Média = " + str(meanAge))
    print("Moda = " + str(modeAge[0]))
    print("Mediana = " + str(medianAge))
    print("Ponto Médio = " + str(mediumPointAge))

if __name__ == "__main__":
    main()