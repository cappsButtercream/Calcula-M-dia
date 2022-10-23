from time import sleep
print('-='*20)
print('CALCULA MÉDIA')
print('-='*20)
p1 = 0
while p1 != 6:
    print('''Escolha Uma Matéria:
    (1)Mátematica
    (2)Português
    (3)História
    (4)Geografia
    (5)Ciências
    (6)Sair Do Programa''')
    p1 = int(input('Qual Opção irá Escolher: '))
    if p1 == 1:
        a1 = int(input('1º Média: '))
        a2 = int(input('2º Média: '))
        a3 = int(input('3º Média: '))
        tot = a1+a2+a3-28
        print(f"Para passar em Mátematica você precisa de {tot}")
        s = int(input('Digite {6} para Sair do Programa: '))
        if s != 6:
            print('RENICIANDO PROGRAMA....')
            sleep(2)
            break
        else:
            break
    if p1 == 2:
        a1 = int(input('1º Média: '))
        a2 = int(input('2º Média: '))
        a3 = int(input('3º Média: '))
        tot = a1+a2+a3-286
        print(f"Para passar em Português você precisa de {tot}")
        s = int(input('Digite {6} para Sair do Programa: '))
        if s != 6:
            print('RENICIANDO PROGRAMA....')
            sleep(2)
            break
        else:
            break
    if p1 == 3:
        a1 = int(input('1º Média: '))
        a2 = int(input('2º Média: '))
        a3 = int(input('3º Média: '))
        tot = a1+a2+a3-28
        print(f"Para passar em História você precisa de {tot}")
        s = int(input('Digite {6} para Sair do Programa: '))
        if s != 6:
            print('RENICIANDO PROGRAMA....')
            sleep(2)
            break
        else:
            break
    if p1 == 4:
        a1 = int(input('1º Média: '))
        a2 = int(input('2º Média: '))
        a3 = int(input('3º Média: '))
        tot = a1+a2+a3-28
        print(f"Para passar em Geografia você precisa de {tot}")
        s = int(input('Digite {6} para Sair do Programa: '))
        if s != 6:
            print('RENICIANDO PROGRAMA....')
            sleep(2)
            break
        else:
            break
    if p1 == 5:
        a1 = int(input('1º Média: '))
        a2 = int(input('2º Média: '))
        a3 = int(input('3º Média: '))
        tot = a1+a2+a3-28
        print(f"Para passar em Ciências você precisa de f{tot}")
        s = int(input('Digite {6} para Sair do Programa: '))
        if s != 6:
            print('RENICIANDO PROGRAMA....')
            sleep(2)
            break
        else:
            break
    if p1 == 6:
        break

    else:
        print('tente de novo!')


print('Obrigado por usar o nosso programa!!')