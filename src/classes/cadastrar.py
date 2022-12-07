from classes.produtos import Product
from classes.validador import Validadores
from classes.impressaoTelas import EstruturasImpressoes

class Cadastro:
    def cadastroProdutos(indice):
        EstruturasImpressoes.topoTela()
        #imprime topo da tela padrão
        print(" "*2+"Cadastro de produtos")
        print(" "*2+"Se desejar sair durante o processo de cadastro digite '0' em qualquer campo!")
        #se for digitado o valor 0 em qualquer input o sistema retornará para o menu incial e o produto cadastrado será cancelado.
        tipo = -1
        while tipo != 1 and tipo != 2:
            print(" "*2+"Insira o tipo de produto:")
            print(" "*2+"1 - Fruta\n"+" "*2+"2 - Bebida\n"+" "*2+"0 - Sair")
            tipo = Validadores.validarInputInt()
            #valida se o input está dentro dos padrões
            if tipo >=3:
                tipo = -1
                print(" "*2+"Insira um valor válido.")
            if tipo == 0:
                print('Você saiu, cadastro cancelado!')
                return 
        print(" "*2+"Insira o nome do produto:")
        produto=(Validadores.validarProduto())
        #metodo faz o input e valida o valor da variável.
        if produto == 0:
            print('Você saiu, cadastro cancelado!')
            return
        qtd = -1
        while qtd <= 0:    
            print(" "*2+'Insira a quantidade: ')
            qtd = Validadores.validarInputInt()
            #metodo faz o input e valida o valor da variável.
            if qtd <0:
                print(" "*2+'Insira um valor válido maior que 0.')
            if qtd == 0:
                print('Você saiu, cadastro cancelado!')
                return

        medida = -1
        while medida<= 0 or medida>3:
            print(" "*2+'Insira a unidade de medida:')
            print(" "*2+'1 - Unidades\n'+" "*2+'2 - Litros\n'+" "*2+'3 - Kilos\n'+" "*2+'0 - Sair')
            medida = Validadores.validarInputInt()
            #metodo faz o input e valida o valor da variável.
            if medida == 0:
                print('Você saiu, cadastro cancelado!')
                return
            if medida < 0 or medida >3:
                if medida != -330129381023:
                #se o valor digitado no input for uma string o programa solicita para o usuário inserir o valor novamente.
                    print(" "*2+'Valor inválido.')

        validade = Validadores.validarData()
        if validade == False:
            print('Você saiu, cadastro cancelado!')
            #se o valor de algum input da data de validade for 0 o programa cancela o cadastro            
            return
        tipo = Validadores.validarTipo(tipo)
        #transforma o valor da variável para a impressão
        medida = Validadores.validarMedida(medida)
        #transforma o valor da variável para a impressão
        
        Item = Product(tipo, produto, qtd, medida, validade)
        #variavel recebe um objeto concatenado de todas os parametros passados
        return Item
       
    



