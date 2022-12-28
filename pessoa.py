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
    #dinheiro é opcional, se não for passando vai ser 100
    def __init__(self, nome = None, pokemons = [], dinheiro = 100):
        if nome:
            self.nome = nome
        else:
            self.nome = random.choice(NOMES)

        self.pokemons = pokemons

        self.dinheiro = dinheiro

    def __str__(self):
        return self.nome

    #metodo para mostrar pokemons da pessoa
    def mostrar_pokemon(self):
        if self.pokemons:
            print('Pokemons de {}:'.format(self))
            #usando metodo enumerate para printar o indice da lista junto com os valores
            for index, pokemon in enumerate(self.pokemons):
                print('{} - {}'.format(index, pokemon))
        else:
            print('{} não tem nenhum pokemon!'.format(self))

    #metodo para ganhar dinheiro apos batalhas
    def ganhar_dinheiro(self, quantidade):
        self.dinheiro += quantidade
        print('Você ganhou $ {}!'.format(quantidade))
        self.mostrar_dinheiro()
    #metodo para mostrar quanto dinheiro personagem possui
    def mostrar_dinheiro(self):
        print('Você possui $ {}!'.format(self.dinheiro))

    #metodo batalha, necessario passar o inimigo/pessoa/alvo
    def batalhar(self, pessoa):
        print('{} iniciou uma batalha com {}!'.format(self, pessoa))
        inimigo = pessoa
        #mostrando pokemons do inimigo
        pessoa.mostrar_pokemon()
        #inimigo escolhe pokemon primeiro
        pokemon_inimigo = pessoa.escolher_pokemon()

        #player escolhe pokemon
        meu_pokemon = self.escolher_pokemon()

        #verificando se os dois tem pokemons para iniciar a luta
        if meu_pokemon and pokemon_inimigo:
            while True:
                #começo da batalha
                #se vitoria retornar true vai parar
                vitoria = meu_pokemon.atacar(pokemon_inimigo)
                if vitoria:
                    print('{} ganhou a batalha com {}!'.format(self, meu_pokemon))
                    self.ganhar_dinheiro(pokemon_inimigo.level * 15)
                    break

                vitoria_inimiga = pokemon_inimigo.atacar(meu_pokemon)
                if vitoria_inimiga:
                    print('{} ganhou a batalha com {}!'.format(inimigo, pokemon_inimigo))
                    break

        else:
            print('Essa batalha não pode ocorrer!')


    def escolher_pokemon(self):
        #verificando se tem pokemon na lista, se tiver vai escolher um aleatorio entre os valores
        if self.pokemons:
            pokemon_escolhido = random.choice(self.pokemons)
            print('{}: escolheu {}!'.format(self, pokemon_escolhido))
            return pokemon_escolhido
        else:
            print('Erro: Esse jogador não possui nenhum Pokemon para ser escolhido')

#classe player, filho de pessoa
class Player(Pessoa):
    tipo = 'Player'
    #funcao capturar pokemon, adiciona pokemon à lista de pokemons do player
    def capturar(self, pokemon):
        self.pokemons.append(pokemon)
        print('{} capturou {}!'.format(self, pokemon))

    #metodo para escolher pokemon na batalha
    def escolher_pokemon(self):
        self.mostrar_pokemon()
        #verficando se tem pokemons na lista
        if self.pokemons:
            #enquanto nao escolher pokemon valido nao sai dessa função
            while True:
                escolha = input('Escolha seu Pokemon: ')
                try:
                    #convertendo string para int
                    escolha = int(escolha)
                    #passando valor do indice escolhido para a variavel
                    pokemon_escolhido = self.pokemons[escolha]
                    #ao dar o return o while é finalizado
                    print('{}: {} eu escolho você!'.format(self, pokemon_escolhido))
                    return pokemon_escolhido
                except:
                    print('Escolha inválida')
        else:
            print('Erro: Esse jogador não possui nenhum Pokemon para ser escolhido')

    #função explorar
    def explorar(self):
        #chance de enconcontrar pokemons pelo caminho (30% de chances)
        if random.random() <= 0.3:
            #gerando pokemon aleatorio
            pokemon = random.choice(POKEMONS)
            print('Um pokemon selvagem apareceu: {}' .format(pokemon))
            #podemos capturar o pokemon
            escolha = input('Deseja capturar pokemon ? (s/n): ')
            if escolha == 's':
                #definindo chance aleatoria de capturar o pokemon(50% de chance)
                if random.random() >= 0.5:
                    self.capturar(pokemon)
                else:
                    print('{} fugiu!'.format(pokemon))
            else:
                print('Ok, boa viagem!')

        else:
            print('Essa exploração não deu em nada')



#classe inimigo, filho de pessoa
class Inimigo(Pessoa):
    tipo = 'Inimigo'
    #passando nome e pokemons vazios para caso precise criar um inimigo especifico
    #se não forem definidos os valores serão nome e pokemons aleatorios
    def __init__(self, nome = None, pokemons = None):
        #se pokemons não tiver valor definido vão ser passados pokemons aleatorios
        if not pokemons:
            pokemons_aleatorios = []
            #vai adicionar pokemons aleatorios para o inimigo (de 1 à 6)
            #inimigo vai ter no minimo 1 e no maximo 6 pokemons
            for i in range(random.randint(1, 6)):
                pokemons_aleatorios.append(random.choice(POKEMONS))

            #chamando construtor da classe pai ao final para instanciar os valores
            super().__init__(nome=nome, pokemons=pokemons_aleatorios)


        #se tiver sido passado os pokemons vai instanciar normalmente
        else:
            super().__init__(nome=nome, pokemons=pokemons)









