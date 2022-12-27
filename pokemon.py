#definir classe com letras maiusculas para manter padrão
import random
class Pokemon:
    #construtor
    #argumento nome é opcional, se nao for passado nome recebe especie do pokemon
    #se argumento level não for definido vai ser aleatorio
    def __init__(self, especie, level = None, nome=None):
        self.especie = especie
        if level:
            self.level = level
        else:
            self.level = random.randint(1,100)

        #se tiver nome recebe o nome, senão o nome vai ser a especie do pokemon
        if nome:
            self.nome = nome
        else:
            self.nome = especie
    #metodo str, retorna esse texto ao printar objeto
    def __str__(self):
        return '{} ({})'.format(self.especie, self.level)
    #metodo de ataque
    def atacar(self, alvo):
        print('{} atacou {}!'.format(self, alvo))

#classe PokemonEletrico é filha de classe Pokemon
class PokemonEletrico(Pokemon):
    tipo = 'eletrico'

    def atacar(self, alvo):
        print('{} lançou um raio do trovão em {}!'.format(self, alvo))

class PokemonFogo(Pokemon):
    tipo = 'fogo'

    def atacar(self, alvo):
        print('{} lançou uma bola de fogo na cabeça de {}!'.format(self,alvo))

class PokemonAgua(Pokemon):
    tipo = 'agua'

    def atacar(self, alvo):
        print('{} lançou um jato de agua em {}!'.format(self, alvo))


