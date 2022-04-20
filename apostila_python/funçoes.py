def velocidade(espaco, tempo):
    v = espaco/tempo
    print('velocidade: {} m/s'.format(v))

velocidade(100, 20)

#funçao sem parametro :dizer 'oi'

def diz_oi():
    print('oi')
diz_oi()

#funçao com retorno

def velocidade(espaco, tempo):
    v = espaco/tempo
    return v
print(velocidade(100, 20))

#atribuindo a funçao a uma  variavel

resultado = velocidade(100, 20))
print(resultado)

#utilizando no calculo aceleraçao
aceleracao = velocidade(100, 20)/20
print(aceleracao)

#retornando 2comandos return

def dados(nome, idade=None):
    if(idade is not None):
        return ('nome : {} \nidade {}'.format(nome, idade))
    else:return ('nome: {} \nidade: nao informada'.format(nome))

#retornando multiplos valores

def calculadora(x, y):
    return x+y, x - y
print(calculadora(1, 2))

#retornando um dicionario utilizando um for

def calculadora(x, y):
    return {'soma' :x+y, 'subtracao': x-y}
resultados = calculadora(1, 2)
for key in resultados:
    print('{}: {}'.format(key, resultados[key]))