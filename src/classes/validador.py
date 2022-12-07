from datetime import date

class Validadores:
    def validarInputInt():
        try:
            return int(input())
            #nesse input o programa só recebe valores inteiros. 
            #Portanto, se a conversão do valor inteiro der erro o valor é diferente de int. Então o programa pede para que seja inserido novamente. 
        except ValueError:
            print(" "*2+"***Valor inválido. Por favor insira novamente.***")
            return -330129381023

    def validarTipo(tipo):
        if tipo == 1:
            tipo=(str("Fruta"))    
        else:
            tipo=(str("Bebida"))
        return tipo
    #converte a opção escolhida de inteiro para a string correspondente

    def validarProduto():
        produto = Validadores.validarSair()
        #valida se o valor digitado de produto é 0
        if produto == 0:
            return produto
        #se o valor de produto for 0, o programa cancela o cadastro e retorna para o menu inicial
        produtoLen = len(produto)
        while produtoLen == 0:
            #valida se o valor da variável não é vazio
            print(" "*2+'Valor inválido. Favor inserir um nome válido!')
            produto = Validadores.validarSair()
            if produto == 0:
                return produto
            produtoLen = len(produto)
        return produto

    def validarMedida(medida):
        if medida == 1:
            medida = str('Unidades')
        elif medida == 2:
            medida = str('Litros')
        else:
            medida = str('Kilos')
        return medida 
    #converte a opção escolhida de inteiro para a string correspondente

    def validarData():
        #metodo para validar a data que o usuário inseriu
        valid = False
        data_atual = date.today()
        #importa o dia atual
        while valid == False:
            print(" "*2+'Insira a data de validade do produto:')
            dia = input(" "*2+'Dia: ')
            mes = input(" "*2+'Mês: ')
            ano = input(" "*2+'Ano: ')
            validInteiros = Validadores.validarIntData(dia, mes, ano)
            #metodo valida se o valor nos inputs são inteiros ou são strings
            if validInteiros == False:
                valid = False
                print('Apenas números são aceitos')
                #os valores dos inputs das datas forem str retorna um erro e pede
                #ao usuário para inserir novamente
            else:
                dia = int(dia)
                mes = int(mes)
                ano = int(ano)
                #transforma as variáveis em inteiro

                if dia == 0 or mes == 0 or ano == 0:
                    return False
                #se o valor de alguma variável for 0, o usuário decidiu cancelar o cadastro
                else:
                    if (mes > 12 or mes < 0) or (dia > 31 or dia < 0) or(ano > 2100):
                        valid = False
                        #valida se os valores são aceitáveis nos padrões de data
                    else:
                        if (ano % 4 == 0 and ano % 100 != 0):
                            if mes == 2 and dia > 29:
                                valid = False
                            #valida ano bissexto
                            else: 
                                valid = True
                                if ano < data_atual.year:
                                    print(' Produto vencido!!! Impossível cadastrar!!')
                                    valid = False
                                    #valida se o produto está vencido
                                elif ano == data_atual.year:
                                    if mes < data_atual.month:
                                        print(' Produto vencido!!! Impossível cadastrar!!')
                                        valid = False
                                    #valida se o produto está vencido
                                    elif mes == data_atual.month:
                                        if dia <= data_atual.day:
                                            print(' Produto vencido!!! Impossível cadastrar!!')
                                            valid = False
                                    #valida se o produto está vencido
                        else:
                            if (mes == 4 or mes == 6 or mes == 9 or mes == 11) and dia > 30:
                                valid = False
                                #valida se o dia não ultrapassa o máximo do mes
                            elif (mes == 2) and dia >= 29:
                                valid = False
                                #valida se o dia não ultrapassa o máximo do mes de fevereiro
                            else:
                                valid = True
                                if ano < data_atual.year:
                                    print(' Produto vencido!!! Impossível cadastrar!!')
                                    valid = False
                                    #valida se o produto está vencido
                                elif ano == data_atual.year:
                                    if mes < data_atual.month:
                                        print(' Produto vencido!!! Impossível cadastrar!!')
                                        valid = False
                                        #valida se o produto está vencido
                                    elif mes == data_atual.month:
                                        if dia <= data_atual.day:
                                            print(' Produto vencido!!! Impossível cadastrar!!')
                                            valid = False
                                            #valida se o produto está vencido
            if valid == False:
                dia = str(dia)
                mes = str(mes)
                ano = str(ano)
                print("  A data: " +dia+"/"+mes+"/"+ano +" é inválida.\n  Por favor insira novamente!")
                #imprime a data para o usuário ver onde errou


        dia = str(dia)
        mes = str(mes)
        ano = str(ano)

        data = dia+'/'+ mes+'/'+ano    
        return data
        #retorna data completa e correta

    def validarIntData(dia, mes, ano):
        try:
            dia = int(dia)
            #tenta transformar o parametro em int
        except ValueError:
            return False
            #se der erro, quer dizer que o valor é inválido para esse input
        try:
            mes = int(mes)
            #tenta transformar o parametro em int
        except ValueError:
            #se der erro, quer dizer que o valor é inválido para esse input
            return False
        try:
            ano = int(ano)
            #tenta transformar o parametro em int
        except ValueError:
            #se der erro, quer dizer que o valor é inválido para esse input
            return False
        
    def validarIdExcluir(validIdExlusao, tamPilha):
        if validIdExlusao == 0:
            print(" "*2 + "Você cancelou a exclusão!")
            return False
        else:
            if validIdExlusao > tamPilha:
                print(" "*2+"Valor do Id não encontrado! Insira novamente!")
                return -1
            else:
                return validIdExlusao


    def validarSair():
        produto = input()
        try:
            produto = int(produto)
            #tenta transformar o valor inserido em inteiro
            if type(produto) == int and produto != 0:
                #se o usuário digitou um numero, mas não é zero ele digitou um valor inválido.
                #retorna uma str vazia
                produto =''
        except ValueError:
            #se na tentativa de transformar em inteiro apresentar um erro,
            #o programa retransforma o valor em string, pois esse é o valor esperado.
            produto = str(produto)
        
        return produto