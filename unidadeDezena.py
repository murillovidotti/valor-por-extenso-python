from unicodedata import digit


class Unidade_Dezena:
    def valores(x, digitos, dicionario_numerico):
        if x == 1:#-verifica se o usuario digitou um unico numero
            for k, v in dicionario_numerico['unidade'].items():
                if int(digitos) == v:
                    print('-' * 10)
                    print(k)
                    print('-' * 10)

        if x == 2 and digitos[0] == '1' and digitos[1] == '0':
            print('-' * 10)
            print(list(dicionario_numerico['unidade'])[9])
            print('-' * 10)

        if x == 2 and digitos[0] == '1':
            for k, v in dicionario_numerico['onzeAodezenove'].items():
                valor = str(v)
                if digitos[1] == valor[1]:
                    print('-' * 10)
                    print(k)
                    print('-' * 10)



        if x == 2 and digitos[0] != '1':
            for k, v in dicionario_numerico['vinteanoventa'].items():
                valor = str(v)
                if digitos[0] == valor[0]:
                    saveK = k
                    for k, v in dicionario_numerico['unidade'].items():
                        if digitos[1] == str(v):
                            print('-' * 10)
                            print(saveK, 'e', k)
                            print('-' * 10)

        if x == 2 and digitos[1] == '0':
            for k, v in dicionario_numerico['vinteanoventa'].items():
                valor = str(v)
                if digitos[0] == valor[0]:
                    print('-' * 10)
                    print(k)
                    print('-' * 10)

