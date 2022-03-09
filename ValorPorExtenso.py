from centenas import Centenas
from unidadeDezena import Unidade_Dezena
from dicionarioNumerio import Dicionario_numerico

#Código principal
dic_numeros = Dicionario_numerico.dic_numerico_valores()


valor = input('Digite um numero entre 1 e 999: ')
while valor != 1000 or valor != 'sair':
    if valor.isnumeric():
        valor = valor.lstrip('0')
        tamanho_Valor = len(valor)
    else:
        break
    Unidade_Dezena.valores(tamanho_Valor,valor, dic_numeros)
    Centenas.valores(tamanho_Valor,valor, dic_numeros)


    valor = input('Digite um numero entre 1 e 999:')
   
    

   


