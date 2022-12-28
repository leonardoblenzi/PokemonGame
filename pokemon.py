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
        #valores de ataque e vida são baseados no level no pokemon
        #ataque
        self.ataque = self.level * 5
        #vida
        self.vida = self.level * 10

    #metodo str, retorna esse texto ao printar objeto
    def __str__(self):
        return '{} ({})'.format(self.especie, self.level)

    #metodo de ataque pai
    def atacar(self, alvo):
        #vida do alvo - poder de ataque do atacante
        #ataque vai ser aleatorio
        dano_efetivo = int(self.ataque * random.random() * 1.3)
        alvo.vida -= dano_efetivo

        print('{} perdeu {} pontos de vida!'.format(alvo, dano_efetivo))

        #retorna true se alvo tiver morrido
        if alvo.vida<=0:
            print('{} foi derrotado!'.format(alvo))
            return True
        #retorna false se alvo estiver vivo
        else:
            return False

#classe PokemonEletrico é filha de classe Pokemon
class PokemonEletrico(Pokemon):
    tipo = 'eletrico'

    def atacar(self, alvo):

        print('{} lançou um raio do trovão em {}!'.format(self, alvo))
        # chamando metodo atacar classe pai, passar return para pegar true ou false da classe pai
        return super().atacar(alvo)

class PokemonFogo(Pokemon):
    tipo = 'fogo'

    def atacar(self, alvo):

        print('{} lançou uma bola de fogo na cabeça de {}!'.format(self,alvo))
        # chamando metodo atacar classe pai, passar return para pegar true ou false da classe pai
        return super().atacar(alvo)

class PokemonAgua(Pokemon):
    tipo = 'agua'

    def atacar(self, alvo):

        print('{} lançou um jato de agua em {}!'.format(self, alvo))
        # chamando metodo atacar classe pai, passar return para pegar true ou false da classe pai
        return super().atacar(alvo)


