import pandas as pd
import statistics

def main():
    input_file = '0-Datasets/echocardiogramClear.data'
    names = ['survival','still-alive','age-at-heart-attack','pericardial-effusion','fractional-shortening', 'epss', 'lvdd', 'wall-motion-score', 'wall-motion-index', 'alive-at-1']

    df = pd.read_csv(input_file, names = names)  

    age = df['age-at-heart-attack'].tolist()
    sortedAge = sorted(df['age-at-heart-attack'].tolist())

    meanAge = df['age-at-heart-attack'].mean()

    amplitudeAge = sortedAge[len(sortedAge)-1] - sortedAge[0]
    stdDeviationAge = statistics.pstdev(age)
    varianceAge = statistics.pvariance(age)
    coefVariationAge = (stdDeviationAge/meanAge)*100

    print("\nMedidas de dispersão da idade de pessoas que sofreram de ataques cardíacos")
    print("Amplitude = " + str(amplitudeAge))
    print("Desvio Padrão = " + str(stdDeviationAge))
    print("Variância = " + str(varianceAge))
    print("Coeficiente de Variação = " + str(round(coefVariationAge, 2)) + "%\n")

if __name__ == "__main__":
    main()