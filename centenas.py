class Centenas:
    def valores(x, digitos, dicionario_numerico):
        centena = ''
        dezena = ''
        unidade = ''
        if x == 3 and digitos[1] != '0' and digitos[2] != '0':
            for k, v in dicionario_numerico['cemAteNoventaenove'].items():
                valor = str(v)
                if digitos[0] == valor[0]:
                    centena = k
    

            if (int(digitos[1])) > 0 and (int(digitos[1])) < 2:
                for k1, v1 in dicionario_numerico['onzeAodezenove'].items():
                    valor = str(v1)
                    if digitos[1] == valor[0] and digitos[2] == valor[1]:
                        dezena = k1

            else:
                for k1, v1 in dicionario_numerico['vinteanoventa'].items():
                    valor = str(v1)
                    if digitos[1] == valor[0]:
                        dezena = k1

                for k2, v2 in dicionario_numerico['unidade'].items():
                    valor = str(v2)
                    if digitos[2] == valor:
                        unidade = k2
            print('-'*10)
            print(centena, 'e', dezena, unidade)
            print('-'*10)

        elif x == 3 and digitos[1] == '0' and digitos[2] == '0':
            for k, v in dicionario_numerico['cemAteNoventaenove'].items():
                valor = str(v)
                if digitos[0] == valor[0]:
                    print('-' * 10)
                    print(k)
                    print('-' * 10)
        elif x == 3 and digitos[1] != '0' and digitos[2] == '0':
            for k, v in dicionario_numerico['cemAteNoventaenove'].items():
                valor = str(v)
                if digitos[0] == valor[0]:
                    centena = k
            for k1, v1 in dicionario_numerico['vinteanoventa'].items():
                valor = str(v1)
                if digitos[1] == valor[0]:
                    dezena = k1
            print('-' * 10)
            print(centena, 'e', dezena)
            print('-' * 10)
        elif x == 3 and digitos[1] == '0' and digitos[2] != '0':
            for k, v in dicionario_numerico['cemAteNoventaenove'].items():
                valor = str(v)
                if digitos[0] == valor[0]:
                    centena = k
            for k2, v2 in dicionario_numerico['unidade'].items():
                valor = str(v2)
                if digitos[2] == valor:
                    unidade = k2
            print('-' * 10)
            print(centena, 'e', unidade)
            print('-' * 10)
