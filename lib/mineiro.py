import tweepy
import csv
from datetime import datetime
import time


class Mineiro:

    def __init__(self, alvo: str = "pyhton", quantidade: int = 100, /):
        self.__alvo: str = alvo
        self.__quantidade: int = quantidade
        self.__contador: int = 0

    @property
    def alvo(self):
        return str(self.__alvo)

    @property
    def quantidade(self):
        return self.__quantidade

    @property
    def contador(self):
        return self.__contador

    @alvo.setter
    def alvo(self, novo_alvo):
        self.__alvo = novo_alvo

    @quantidade.setter
    def quantidade(self, novo_quantidade):
        self.__quantidade = novo_quantidade

    @contador.setter
    def contador(self, novo_contador):
        self.__contador = novo_contador

    @staticmethod
    def conectar():
        with open('keys.txt') as keys:
            #    CONSUMER_KEY;CONSUMER_SECRET;ACCESS_TOKEN;ACCESS_TOKEN_SECRET no arquivo keys.txt
            key = keys.read()
            CONSUMER_KEY: str = key.split(';')[0]
            CONSUMER_SECRET: str = key.split(';')[1]
            ACCESS_TOKEN: str = key.split(';')[2]
            ACCESS_TOKEN_SECRET: str = key.split(';')[3]
        # Authenticador
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
        api = tweepy.API(auth)
        return api

    def minerar(self):
        try:
            self.conectar().verify_credentials()
            print("Authenticacao OK")
        except:
            print("Erro durante autenticacao")
        query_busca = self.alvo + " -filter:retweets"
        tweets = tweepy.Cursor(self.conectar().search, q=query_busca).items(self.quantidade)
        return tweets

    def arquivar_csv(self):
        with open(f'coleta_{self.alvo}_{datetime.now().strftime("%Y-%m-%d-%H-%M-%S")}_para_{self.quantidade}.csv', 'w') as arquivo:
            escrever = csv.writer(arquivo)
            escrever.writerow(
                ['busca', 'usuario_nome', 'usuario_nome_exibido', 'usuario_id', 'usuario_data','usuario_data_timestamp'
                    , 'usuario_local', 'usuario_seguidores', 'usuario_seguindo', 'texto_data','texto_data_timestamp'
                    , 'texto', 'texto_tamanho'])
            for tweet in self.minerar():
                self.contador = self.contador + 1
                print(f'Garimpando {self.alvo} - {self.contador} de {self.quantidade}')
                # print(tweet.created_at)
                #print(tweet.text)
                # print(tweet.user)
                # print(tweet._json)
                # print(tweet._json['created_at'])
                # print(tweet._json['user'])
                #print(tweet._json['user']['name'])
                # print(tweet._json['user']['screen_name'])
                # print(tweet._json['user']['id'])
                # print(tweet._json['user']['location'])
                #print(tweet._json['user']['created_at'])
                # print(tweet._json['user']['followers_count'])
                # print(tweet._json['user']['friends_count'])
                # print(tweet._json['text'])
                # print(tweet._json.keys())
                usuario = tweet._json['user']
                usuario_nome = tweet._json['user']['name']
                usuario_nome_exibido = tweet._json['user']['screen_name']
                usuario_id = tweet._json['user']['id']
                usuario_local = tweet._json['user']['location']
                usuario_data = tweet._json['user']['created_at']
                usuario_seguidores = tweet._json['user']['followers_count']
                usuario_seguindo = tweet._json['user']['friends_count']
                texto = tweet._json['text']
                texto_data = tweet._json['created_at']
                texto_tamanho = len(texto)
                usuario_data_convert = datetime.strftime(datetime.strptime(usuario_data, '%a %b %d %H:%M:%S +0000 %Y'),
                                                         '%Y-%m-%d %H:%M:%S')
                texto_data_convert = datetime.strftime(datetime.strptime(texto_data, '%a %b %d %H:%M:%S +0000 %Y'),
                                                       '%Y-%m-%d %H:%M:%S')
                usuario_data_timestamp = time.mktime(datetime.strptime(usuario_data, '%a %b %d %H:%M:%S +0000 %Y')
                                                     .timetuple())
                texto_data_timestamp = time.mktime(datetime.strptime(texto_data, '%a %b %d %H:%M:%S +0000 %Y')
                                                   .timetuple())

                escrever.writerow(
                    [self.__alvo, usuario_nome, usuario_nome_exibido, usuario_id, usuario_data_convert,
                     usuario_data_timestamp, usuario_local, usuario_seguidores, usuario_seguindo, texto_data_convert,
                     texto_data_timestamp, texto, texto_tamanho])
        print('Fim do Garimpo')

    def arquivo_treino(self):
        with open(f'arquivo_de_treino.csv', 'w') as arquivo:
            escrever = csv.writer(arquivo)
            escrever.writerow(
                ['busca', 'usuario_nome', 'usuario_nome_exibido', 'usuario_id', 'usuario_data','usuario_data_timestamp'
                    , 'usuario_local', 'usuario_seguidores', 'usuario_seguindo', 'texto_data','texto_data_timestamp'
                    , 'texto', 'texto_tamanho'])
            for tweet in self.minerar():
                self.contador = self.contador + 1
                print(f'Arquivando {self.alvo} - {self.contador} de {self.quantidade}')
                usuario = tweet._json['user']
                usuario_nome = tweet._json['user']['name']
                usuario_nome_exibido = tweet._json['user']['screen_name']
                usuario_id = tweet._json['user']['id']
                usuario_local = tweet._json['user']['location']
                usuario_data = tweet._json['user']['created_at']
                usuario_seguidores = tweet._json['user']['followers_count']
                usuario_seguindo = tweet._json['user']['friends_count']
                texto = tweet._json['text']
                texto_data = tweet._json['created_at']
                texto_tamanho = len(texto)
                usuario_data_convert = datetime.strftime(datetime.strptime(usuario_data, '%a %b %d %H:%M:%S +0000 %Y'),
                                                         '%Y-%m-%d %H:%M:%S')
                texto_data_convert = datetime.strftime(datetime.strptime(texto_data, '%a %b %d %H:%M:%S +0000 %Y'),
                                                       '%Y-%m-%d %H:%M:%S')
                usuario_data_timestamp = time.mktime(datetime.strptime(usuario_data, '%a %b %d %H:%M:%S +0000 %Y')
                                                     .timetuple())
                texto_data_timestamp = time.mktime(datetime.strptime(texto_data, '%a %b %d %H:%M:%S +0000 %Y')
                                                   .timetuple())

                escrever.writerow(
                    [self.__alvo, usuario_nome, usuario_nome_exibido, usuario_id, usuario_data_convert,
                     usuario_data_timestamp, usuario_local, usuario_seguidores, usuario_seguindo, texto_data_convert,
                     texto_data_timestamp, texto, texto_tamanho])
        print('Fim do Garimpo')

