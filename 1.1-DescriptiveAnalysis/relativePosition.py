import pandas as pd
import statistics
import matplotlib.pyplot as plt

def quantil():
    input_file = '0-Datasets/echocardiogramClear.data'
    names = ['survival','still-alive','age-at-heart-attack','pericardial-effusion','fractional-shortening', 'epss', 'lvdd', 'wall-motion-score', 'wall-motion-index', 'alive-at-1']

    df = pd.read_csv(input_file, names = names)  

    age = df['age-at-heart-attack'].tolist()

    age = df['age-at-heart-attack']
    ageDescription = age.describe()

    q1 = ageDescription['25%']
    median = ageDescription['50%']
    q2 = ageDescription['75%']

    s_q1 = "{0:.2f}".format(q1)
    s_median = "{0:.2f}".format(median)
    s_q2 = "{0:.2f}".format(q2)

    plt.boxplot(age)
    plt.title("Boxplot da idade de pessoas que sofreram de ataques cardíacos")
    plt.text(1, q1, s_q1)
    plt.text(1, median, s_median)
    plt.text(1, q2, s_q2)
    plt.ylabel('Idade')
    plt.show()

def zscore():
    input_file = '0-Datasets/echocardiogramClear.data'
    names = ['survival','still-alive','age-at-heart-attack','pericardial-effusion','fractional-shortening', 'epss', 'lvdd', 'wall-motion-score', 'wall-motion-index', 'alive-at-1']

    df = pd.read_csv(input_file, names = names)  

    age = df['age-at-heart-attack'].tolist()
    meanAge = df['age-at-heart-attack'].mean()
    stdDeviationAge = statistics.pstdev(age)

    zscoreAge = []
    for i in range(len(age)):
        zscoreAge.append((age[i] - meanAge)/stdDeviationAge)

    print("\nZ-score da idade de pessoas que sofreram de ataques cardíacos")
    print(zscoreAge)

def main():
    quantil()
    zscore()

if __name__ == "__main__":
    main()