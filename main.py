from lib.mineiro import Mineiro
from lib.analista import Analista


if __name__ == '__main__':
    mineiro = Mineiro("youtube", 1000)
    analista = Analista()
    #mineiro.alvo = "facebook"
    #mineiro.quantidade = 1000
    mineiro.arquivar_csv()
    mineiro.arquivo_treino()
    analista.analise_csv()
    print(mineiro.contador)

