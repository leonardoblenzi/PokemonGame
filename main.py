from pokemon import *
from pessoa import *

#metodo para o jogador escolher o pokemon inicial (todos level 1)
def escolher_pokemon_inicial(player):
    print('Olá {}, você poderá escolher agora o Pokemon que irá lhe acompanhar nessa jornada!'.format(player))
    pikachu = PokemonEletrico('Pikachu', level=1)
    charmander = PokemonFogo('Charmander', level=1)
    squirtle = PokemonAgua('Squirtle', level=1)

    print('Você possui 3 escolhas: ')
    print('1 - Pikachu')
    print('2 - Charmander')
    print('3 - Squirtle')

    while True:
        escolha = input('Escolha seu Pokemon: ')
        if escolha == '1':
            player.capturar(pikachu)
            break
        elif escolha == '2':
            player.capturar(charmander)
            break
        elif escolha == '3':
            player.capturar(squirtle)
            break
        else:
            print('Escolha inválida')

player = Player()
player.capturar(PokemonEletrico('Pikachu',level=1))
#definindo inimigo
#inimigo1 = Inimigo(nome='Gary', pokemons=[PokemonAgua('Squirtle', level=1)])

player.explorar()
