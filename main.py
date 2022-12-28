from pokemon import *
from pessoa import *
import pickle

#função para salvar o jogo
def salvar_jogo(player):
    try:
        #abrindo arquivo no modo write('escrita') b(binario) (wb)
        #vai ser um arquivo binário pois vamos salvar o objeto
        with open('database.db', 'wb') as arquivo:
            #passando objeto em modo binario para arquivo
            pickle.dump(player, arquivo)
            print('Jogo salvo com sucesso!')

    except Exception as erro:
        print('Erro ao salvar o jogo')
        print(erro)

#função para carregar o jogo
def carregar_jogo():
    try:
        #abrindo arquivo somente no modo read b(leitura binario)
        with open('database.db', 'rb') as arquivo:
            #lendo objeto binario e retornando valor do jogador
            player = pickle.load(arquivo)
            print('Loading feito com sucesso')
            return player

    except Exception as erro:
        print('Save não encontrado')
        print(erro)

# metodo para o jogador escolher o pokemon inicial (todos level 1)
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


if __name__ == '__main__':
    print('------------------------------------------')
    print('Bem-vindo ao Pokemon RPG de terminal')
    print('------------------------------------------')

    while True:
        print('1 - Iniciar novo jogo')
        print('2 - Carregar jogo salvo')
        opcao = input('Selecione uma opção: ')

        if opcao == '1':
            player = None
            break
        elif opcao == '2':
            player = carregar_jogo()
            print('Bem vindo de volta {}!'.format(player))
            break
        else:
            print('Opção inválida')



    #se player nao existir vai ser feita a introdução do jogo
    if not player:

        nome = input('Olá, qual é o seu nome? ')
        player = Player(nome)
        print(
            'Olá {} esse é um mundo habitado por pokemons, a partir de algo sua missão é se tornar mestre dos pokemons'.format(
                player))
        print('Capture o máximo de pokemons que conseguir e lute com seus inimigos')
        player.mostrar_dinheiro()

        if player.pokemons:
            print('Já vi que você tem alguns pokemons')
            player.mostrar_pokemon()
        else:
            print('Você não tem nenhum pokemon, portanto precisa escolher um')
            escolher_pokemon_inicial(player)

        # primeiro inimigo do jogo
        print('Pronto, agora que você já possui um pokemon enfrente seu arqui-rival desde o jardim da infancia Gary')
        gary = Inimigo(nome='Gary', pokemons=[PokemonAgua('Squirtle', level=1)])
        player.batalhar(gary)
        #apos concluir primeira batalha vai salvar jogo e passar o player
        salvar_jogo(player)

    #se player existir vai abrir direto no menu


    #menu de escolhas do jogo
    while True:
        print('------------------------------------------')
        print('O que deseja fazer?')
        print('1 - Explorar o mundo')
        print('2 - Lutar com um inimigo')
        print('3 - Mostrar Pokedex')
        print('0 - Sair do jogo')

        escolha = input('Sua escolha: ')
        print('------------------------------------------')

        if escolha == '0':
            print('>>>>>>Saindo do jogo')
            break

        # explorando o mundo
        elif escolha == '1':
            player.explorar()
            # salvando automaticamente
            salvar_jogo(player)

        # lutando contra inimigos aleatorios
        elif escolha == '2':
            inimigo = Inimigo()
            player.batalhar(inimigo)
            # salvando automaticamente
            salvar_jogo(player)

        # mostrando pokedex
        elif escolha == '3':
            player.mostrar_pokemon()

        else:
            print('Escolha inválida')
