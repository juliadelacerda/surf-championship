from campeonato import Campeonato
from patrocinador import Patrocinador
from amador import Amador
from profissional import Profissional
from lenda import Lenda

patrocinadorx = Patrocinador(' ', 0)
campeonatoX = Campeonato(' ', ' ', ' ', 0)
amadorx = Amador(' ', 0, 0)
profissionalX = Profissional(' ', 0, 0)
lendaX = Lenda(' ', 0, 0)


def cadastraCampeonato ():
    print('\n---=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=---')
    campeonatoX._nome = input('\nNome do campeonato: ')
    campeonatoX._local = input('Local onde ocorrerá o campeonato: ')
    campeonatoX._premiacao = input('Premiação: ')
    campeonatoX._categoria = int(input('Categoria do campeonato (Digite 1 para "Amador", 2 para "Profissional" e 3 para "Lenda"): '))

    print('\n\nCampeonato cadastrado com sucesso!\n')



def cadastraAtleta ():
    print('\n---=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=---')
    categoria = int(input('\nCategoria do atleta (Digite 1 para "Amador", 2 para "Profissional" e 3 para "Lenda"): '))

    if campeonatoX._categoria <= categoria:
        if categoria == 1:
            amadorx._nome = input('Nome: ')
            amadorx._idade = int(input('Idade: '))
            amadorx._pontuacao = float(input('Pontuação: '))


            if amadorx.vencedor() == True:
                print('\nAtleta vencedor cadastrado com sucesso!\n')

            else:
                print('\nAtleta cadastrado com sucesso! ')



        elif categoria == 2:
            profissionalX._nome = input('Nome: ')
            profissionalX.idade = int(input('Idade: '))
            profissionalX._pontuacao = float(input('Pontuação: '))


            if profissionalX.vencedor() == True:
                print('\nAtleta vencedor cadastrado com sucesso!\n')

            else:
                print('\nAtleta cadastrado com sucesso! ')  



        elif categoria == 3:
            lendaX._nome = input('Nome: ')
            lendaX.idade = int(input('Idade: '))
            lendaX._pontuacao = float(input('Pontuação: '))


            if lendaX.vencedor() == True:
                print('\nAtleta vencedor cadastrado com sucesso!\n')

            else:
                print('\nAtleta cadastrado com sucesso!\n')


        else:
            print('\nCategoria inválida!\n')

    else:
        print('\nO atleta não pode participar de um campeonato desta categoria!')
        cadastraAtleta()


def cadastraPatrocinador ():
    print('\n---=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=---')
    patrocinadorx._nome = input('\nNome do patrocinador: ')
    patrocinadorx._valor = input('Valor do contrato: ')

    print('Patrocinador cadastrado com sucesso!')




print('\n--------------------------------------------------------------------------------------------')
start = ' '

while start != '.':
    start = input('\nEscolha o que irá cadastrar:\n- 1 -- Campeonato\n- 2 -- Atletas\n- 3 -- Patrocinador\n- 4 -- Sair:\n ')
    
    if start == '1':
        cadastraCampeonato()
    
    
    elif start == '2':
        qtd_atletas = int(input('Quantidade de atletas que você deseja cadastrar: '))
        
        cont = 0
        while cont < qtd_atletas:
            cadastraAtleta()
            cont += 1
    

    elif start == '3':
        qtd_patrocinadores = int(input('Quantidade de patrocinadores que você deseja cadastrar: '))

        cont = 0
        while cont < qtd_patrocinadores:
            cadastraPatrocinador()
            cont += 1
        

    elif start == '.':
        'Saindo do sistema...'


print('--------------------------------------------------------------------------------------------')