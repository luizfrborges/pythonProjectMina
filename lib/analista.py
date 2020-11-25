import csv
import sys

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import AgglomerativeClustering
from sklearn.preprocessing import StandardScaler
import numpy as np


class Analista:
    def __init__(self, alvo: str = "arquivo_treino.csv", clusters: int = 4, /):
        if clusters > 10:
            print('Selecione um valor de clusters menor que 10')
            sys.exit()
        self.__alvo: str = alvo
        self.__clusters: int = clusters
        self.__contador: int = 0

    @property
    def alvo(self):
        return str(self.__alvo)

    @property
    def clusters(self):
        return int(self.__clusters)

    @alvo.setter
    def alvo(self, novo_alvo):
        self.__alvo = novo_alvo

    @clusters.setter
    def clusters(self, novo_clusters):
        if novo_clusters > 10:
            print('Selecione um valor de clusters menor que 10')
            sys.exit()
        self.__clusters = novo_clusters

    def carregar_dados(self):
        base = pd.read_csv(self.alvo, header=1)
        return base

    def equalizar_dados(self):
        dados = self.carregar_dados().iloc[:, [7, 8, 3,  5, 9, 13, 14, 15]].values
        scaler = StandardScaler()
        dados = scaler.fit_transform(dados)
        return dados

    def hierarquico(self):
        eixo = self.equalizar_dados()
        hc = AgglomerativeClustering(n_clusters=self.clusters, affinity='euclidean', linkage='ward')
        previsoes = hc.fit_predict(eixo)
        lista_resultado = np.column_stack((self.carregar_dados(), previsoes))
        for item in range(self.clusters):
            cores = ['red', 'blue', 'green', 'orange', 'purple', 'brown', 'pink', 'gray', 'olive', 'cyan']
            plt.scatter(eixo[previsoes == item, 1], eixo[previsoes == item, 0], s=30, c=cores[item],
                        label=f'Cluster{item}')
        plt.xlabel('número segindo')
        plt.ylabel('número de seguidores')
        plt.title('Analise')
        plt.legend()
        plt.savefig(f'grafico_{self.alvo}.png')
        return lista_resultado

    def analise_csv(self):
        with open(f'analise.csv', 'w') as arquivo:
            escrever = csv.writer(arquivo)
            escrever.writerow(
                ['busca', 'usuario_nome', 'usuario_nome_exibido', 'usuario_id', 'usuario_data', 'usuario_data_timestamp'
                    , 'usuario_local', 'usuario_seguidores', 'usuario_seguindo', 'usuario_favoritos', 'texto_data'
                    , 'texto_data_timestamp', 'texto', 'texto_retweet', 'texto_favorito', 'texto_tamanho', 'grupo'])
            for item in self.hierarquico():
                escrever.writerow(item)
