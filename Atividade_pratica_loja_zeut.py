import datetime
import time
import sys


#funcao 1 cadstrar cliente e obter limite de gasto
def cadastro() -> object:
    agora = datetime.datetime.now()
    #hoje = datetime.date.today()
    #atual = hoje.strftime("%Y")
    print('\nBem vindo(a) a Loja Zeut, meu nome é Vinicius Farineli Freire ')
    print('Gostariamos de saber mais sobre você\n')
    nome = str(input('Qual seu nome:\t'))
    tamanho_nome = len(nome)
    cargo = str(input('Qual seu cargo atual?\t'))
    salario = float(input('Qual seu salario?\t'))
    if salario > 0:
        print('\n\nAgora queremos saber data de seu nascimento\n')
        dia = int(input('Dia : '))
        #VERIFICANDO ENTRADAS DO USUARIO
        if dia <= 31 and dia > 0:
            mes = int(input('Agora o mes: '))
        else:
            print('----------- ERRO RECOMECE O CADASTRO ----------------')
            time.sleep(1)
            sys.exit()
        if mes <= 12 and mes > 0:
            ano = int(input('Digite o ano de seu nascimento com 4 digitos:\t'))
        else:
            print('----------- ERRO RECOMECE O CADASTRO ----------------')
            time.sleep(1)
            sys.exit()
        if (ano > 1900) and (ano < agora.year):
                idade = (agora.year) - ano
        else:
            print('----------- ERRO RECOMECE O CADASTRO ----------------')
            time.sleep(1)
            sys.exit()
    else:
        print('----------- ERRO RECOMECE O CADASTRO ----------------')
        time.sleep(1)
        sys.exit()
    print('\nConferindo dados')
    time.sleep(2)
    print(f'Seu cargo e {cargo}\nSeu salario é de R${salario}\nSua data de nascimento é: {dia}/{mes}/{ano}')
    print(f'Sua idade é aproximadamente {idade} anos')
    gasto = (salario * (idade / 1000)) + 100
    print(f'Maximo de gasto recomendado {gasto}')
    confirma = input('Confirma dados (s/n)? ')
    if confirma == 's':
        print('----------- CADASTRO OK ----------------')
    else:
        print('----------- ERRO RECOMECE O CADASTRO ----------------')
        time.sleep(1)
        sys.exit()



    return gasto, nome, idade




#funçao 2 solicitar quantos deseja cadastrar e se o produto cadastrado esta dentro do limite de gasto

def verifica(gasto, nome, idade):
    novo = 0
    pdesconto = 0
    tamanhonome = len(nome) - nome.count(' ')# verificar tamanho do nome completo excluindo espaços
    soma = 0
    # print(tamanhonome) verificando se ta contando a quantidade certa
    desconto = nome.find(' ')
    # print(desconto) verificar primeiro nome
    soma = 0
    produto = dict()
    qtdprodutos = int(input('Quantos produtos deseja cadastrar? '))
    for n in range(0, qtdprodutos): #REPETIÇÃO ATE A QUANTIDADE  INFORMADA
        produto['Nome do produto'] = str(input('Qual nome do produto: '))
        produto['Valor'] = float(input(f'Qual valor do {produto["Nome do produto"]}:  '))
        diferenca60 = gasto * 0.60
        diferenca90 = gasto * 0.90
        dife100 = gasto * 1  # 150 é igual a gasto
        soma = soma + produto['Valor']  # soma o valor de cada produto digitado
        menos = 0
        if produto['Valor'] <= gasto:  # verifica individualmente como pede no passo 3 usuario digita e verifica quanto do limite usa
            if produto['Valor'] <= diferenca60:
                print('---------------------------------------------------------------|')
                print('   Este produto que acabou de cadastrar  está Liberado         |')
                print('---------------------------------------------------------------|')
            if produto['Valor'] >= diferenca60 and produto['Valor'] <= diferenca90:
                print('---------------------------------------------------------------------|')
                print('  Este produto que acabou de cadastrar está Liberado parcelar em 2x  |')
                print('---------------------------------------------------------------------|')
            if produto['Valor'] == dife100:
                print('---------------------------------------------------------------------|')
                print("  Este produto que acabou de cadastrar está Liberado 3x ou mais      |")
                print('---------------------------------------------------------------------|')
        else:
            print('*******************************************************')
            print(' Bloqueado produto excede limite de gasto')
            print('*******************************************************')
            print('_______________________________________________________')
        for k, v in produto.items():
            print(f' - {k} : {v} \n ')
            menos = gasto - soma
        if menos >= 0:
            print(f'O valor que você  ainda tem do limite  para gastar é R${menos}\n')

        if produto['Valor'] > desconto and produto['Valor'] < idade:  # verifica a condiçao do valor do produto estar entre a quantidade de letras do nome e a idade
            print(f'Parabéns você possui um desconto de {desconto}% ')
            pdesconto = desconto / 100
            novo = produto['Valor'] * pdesconto
            novo = produto['Valor'] - novo
            print(f'O novo valor do seu  produto é {novo}')

    if soma > gasto:  # gasto = limite
        print(f'A soma dos produtos ficou em R${soma}, é acima do seu limite de gasto recomendado,que é {gasto}.\n')
        print(f'O total  de produtos cadastrado é de  R${soma}')
    else:  # gasto = limite
        print(f'A soma dos produtos deu R${soma} e tambem esta liberado\n\n')

    print('___________________________________________________________________________________________________________')






#BSAKJDASJKBDJSABD



gasto, nome, idade = cadastro()




#JASDJBASJDBSAJKDB



soma = verifica(gasto, nome, idade)





















