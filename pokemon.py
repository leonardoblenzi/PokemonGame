#definir classe com letras maiusculas para manter padrão
class Pokemon:
    #construtor
    #argumento nome é opcional, se nao for passado nome recebe especie do pokemon
    #argumento level é opcioval se nao for passado vai ser 1
    def __init__(self, especie, level = 1, nome=None):
        self.especie = especie
        self.level = level

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


meu_pokemon = PokemonFogo('charmander')
pokemon_inimigo = PokemonAgua('squirtle')

meu_pokemon.atacar(pokemon_inimigo)
print(meu_pokemon.tipo)