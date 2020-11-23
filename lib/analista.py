import csv

import matplotlib.pyplot as plt
import pandas as pd
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.cluster import AgglomerativeClustering
from sklearn.preprocessing import StandardScaler
import numpy as np


class Analista:
    def __init__(self, alvo: str = "arquivo_de_treino.csv", clusters: int = 3, /):
        self.__alvo: str = alvo
        self.__clusters: int = clusters
        self.__contador: int = 0

    @property
    def alvo(self):
        return str(self.__alvo)

    @property
    def clusters(self):
        return self.__clusters

    @alvo.setter
    def alvo(self, novo_alvo):
        self.__alvo = novo_alvo

    @clusters.setter
    def quantidade(self, novo_quantidade):
        self.__clusters = novo_quantidade

    def carregar_dados(self):
        base = pd.read_csv(self.alvo, header=1)
        return base

    def equalizar_dados(self):
        dados = self.carregar_dados().iloc[:, [3, 5, 7, 8, 12]].values
        scaler = StandardScaler()
        dados = scaler.fit_transform(dados)
        return dados

    def hierarquico(self):
        eixo = self.equalizar_dados()
        hc = AgglomerativeClustering(n_clusters=self.clusters, affinity='euclidean', linkage='ward')
        previsoes = hc.fit_predict(eixo)
        lista_resultado = np.column_stack((self.carregar_dados(), previsoes))
        plt.scatter(eixo[previsoes == 0, 3], eixo[previsoes == 0, 2], s=30, c='red', label='Cluster 0')
        plt.scatter(eixo[previsoes == 1, 3], eixo[previsoes == 1, 2], s=30, c='blue', label='Cluster 1')
        plt.scatter(eixo[previsoes == 2, 3], eixo[previsoes == 2, 2], s=30, c='green', label='Cluster 2')
        plt.xlabel('número segindo')
        plt.ylabel('número de seguidores')
        plt.title('Analise')
        plt.legend()
        plt.savefig(f'grafico_{self.alvo}.png')
        return lista_resultado

    def analise_csv(self):
        with open(f'previsoes_{self.alvo}.csv', 'w') as arquivo:
            escrever = csv.writer(arquivo)
            escrever.writerow(
                ['busca', 'usuario_nome', 'usuario_nome_exibido', 'usuario_id', 'usuario_data', 'usuario_data_timestamp'
                    , 'usuario_local', 'usuario_seguidores', 'usuario_seguindo', 'texto_data', 'texto_data_timestamp'
                    , 'texto', 'texto_tamanho', 'grupo'])
            for item in self.hierarquico():
                escrever.writerow(item)
