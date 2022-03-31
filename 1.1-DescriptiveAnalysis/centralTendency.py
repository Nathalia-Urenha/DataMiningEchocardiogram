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
    avgPointAge = (sortedAge[0] + sortedAge[len(sortedAge)-1])/2
    weightedAverageAge = (df['age-at-heart-attack'].sum())/len(age)
    geometricMeanAge = statistics.geometric_mean(age)
    harmonicMeanAge = statistics.harmonic_mean(age)

    print("Média de pessoas que sofreram de ataques cardíacos")
    print("Média = " + str(meanAge))
    print("Moda = " + str(modeAge[0]))
    print("Mediana = " + str(medianAge))
    print("Ponto Médio = " + str(avgPointAge))
    print("Média Ponderada = " + str(weightedAverageAge))
    print("Média Geométrica = " + str(geometricMeanAge))
    print("Média Harmônica = " + str(harmonicMeanAge))

if __name__ == "__main__":
    main()