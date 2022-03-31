import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import plotly.express as px

def main():
    # Faz a leitura do arquivo
    input_file = '0-Datasets/echocardiogramClear.data'
    names = ['survival','still-alive','age-at-heart-attack','pericardial-effusion','fractional-shortening', 'epss', 'lvdd', 'wall-motion-score', 'wall-motion-index', 'alive-at-1']
    features = ['survival','still-alive','age-at-heart-attack','pericardial-effusion','fractional-shortening', 'epss', 'lvdd', 'wall-motion-score', 'wall-motion-index']
    target = 'alive-at-1'
    df = pd.read_csv(input_file,    # Nome do arquivo com dados
                     names = names) # Nome das colunas                      
    ShowInformationDataFrame(df,"Dataframe original")

    # Separating out the features
    x = df.loc[:, features].values

    # Separating out the target
    y = df.loc[:,[target]].values

    # Standardizing the features
    x = StandardScaler().fit_transform(x)
    normalizedDf = pd.DataFrame(data = x, columns = features)
    normalizedDf = pd.concat([normalizedDf, df[[target]]], axis = 1)
    ShowInformationDataFrame(normalizedDf,"Dataframe Normalized")

    # PCA projection
    pca = PCA()    
    principalComponents = pca.fit_transform(x)
    print("Explained variance per component:")
    print(pca.explained_variance_ratio_.tolist())
    print("\n\n")

    principalDf = pd.DataFrame(data = principalComponents[:,0:2], 
                               columns = ['principal component 1', 
                                          'principal component 2'])
    finalDf = pd.concat([principalDf, df[[target]]], axis = 1)    
    ShowInformationDataFrame(finalDf,"Dataframe PCA")
    
    VisualizePcaProjection(finalDf, target)
    plot3DPCA(normalizedDf, features)


def ShowInformationDataFrame(df, message=""):
    print(message+"\n")
    print(df.info())
    print(df.describe())
    print(df.head(10))
    print("\n")
    
           
def VisualizePcaProjection(finalDf, targetColumn):
    fig = plt.figure(figsize = (8,8))
    ax = fig.add_subplot(1,1,1) 
    ax.set_xlabel('Principal Component 1', fontsize = 15)
    ax.set_ylabel('Principal Component 2', fontsize = 15)
    ax.set_title('2 component PCA', fontsize = 20)
    targets = [0, 1, ]
    colors = ['r', 'g']
    for target, color in zip(targets,colors):
        indicesToKeep = finalDf[targetColumn] == target
        ax.scatter(finalDf.loc[indicesToKeep, 'principal component 1'],
                   finalDf.loc[indicesToKeep, 'principal component 2'],
                   c = color, s = 50)
    ax.legend(targets)
    ax.grid()
    plt.savefig('1-Preprocessing/PCAProjection.png', format='png')
    plt.show()

def plot3DPCA(df, features):
    X=df[features]

    pca = PCA(n_components=3)
    components = pca.fit_transform(X)

    total_var = pca.explained_variance_ratio_.sum() * 100

    group_color = ['black', 'lightsalmon']

    fig = px.scatter_3d(
        components, x=0, y=1, z=2, color=df['alive-at-1'].apply(str),
        title=f'Total Explained Variance: {total_var:.2f}%',
        labels={'0': 'PC 1', '1': 'PC 2', '2': 'PC 3'},
        color_discrete_sequence = group_color
    )
    fig.show()


if __name__ == "__main__":
    main()