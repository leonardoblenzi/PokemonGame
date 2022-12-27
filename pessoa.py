from pokemon import *
import random

# lista de nomes
NOMES = ['Ferbald', 'Menu', 'Loccla', 'Sogar', 'Robber', 'Ron', 'Chelldas', 'Regin', 'Sonne', 'Trisyl', 'Ard-ham',
         'Wynleofu', 'Heesc', 'Gejo', 'Samga', 'Egelni', 'Betlen', 'Swithcar', 'Pherdoc', 'Kentim']
#lista com objetos pokemon
POKEMONS = [
    PokemonFogo('Charmander'),
    PokemonFogo('Charmeleon'),
    PokemonFogo('Charizard'),
    PokemonAgua('Squirtle'),
    PokemonAgua('Wartortle'),
    PokemonAgua('Blastoise'),
    PokemonEletrico('Pikachu'),
    PokemonEletrico('Raichu'),
    PokemonEletrico('Zapdos'),
]
class Pessoa:
    #construtor
    #nome é opcional, se não for passado vai ser um nome aleatorio
    #pokemons vao ser uma lista
    def __init__(self, nome = None, pokemons = []):
        if nome:
            self.nome = nome
        else:
            self.nome = random.choice(NOMES)

        self.pokemons = pokemons

    def __str__(self):
        return self.nome

    #metodo para mostrar pokemons da pessoa
    def mostrar_pokemon(self):
        if self.pokemons:
            print('Pokemons de {}:'.format(self))
            for pokemon in self.pokemons:
                print(pokemon)
        else:
            print('{} não tem nenhum pokemon!'.format(self))

#classe player, filho de pessoa
class Player(Pessoa):
    tipo = 'Player'
    #funcao capturar pokemon, adiciona pokemon à lista de pokemons do player
    def capturar(self, pokemon):
        self.pokemons.append(pokemon)
        print('{} capturou {}'.format(self, pokemon))


#classe inimigo, filho de pessoa
class Inimigo(Pessoa):
    tipo = 'Inimigo'
    #passando nome e pokemons vazios para caso precise criar um inimigo especifico
    #se não forem definidos os valores serão nome e pokemons aleatorios
    def __init__(self, nome = None, pokemons = []):
        #se pokemons não tiver valor definido vão ser passados pokemons aleatorios
        if not pokemons:
            #vai adicionar pokemons aleatorios para o inimigo (de 1 à 6)
            #inimigo vai ter no minimo 1 e no maximo 6 pokemons
            for i in range(random.randint(1, 6)):
                pokemons.append(random.choice(POKEMONS))

        #chamando construtor da classe pai ao final para instanciar os valores
        super().__init__(nome=nome, pokemons=pokemons)






