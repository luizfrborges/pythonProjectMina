# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
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


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
