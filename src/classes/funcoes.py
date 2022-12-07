from classes import cadastrar
from classes import listar
from classes import remover

class Funcoes:
    def func(opc, id, pilhaTodos):
        #Faz a leitura do input e inicia o método escolhido
        if opc == 1:
            id = id+1
            #id serve para o controle do indice do produto
            itemPilha=cadastrar.Cadastro.cadastroProdutos(id)
            #variável itemPilha recebe os valores do metodo de cadastrar.
            pilhaTodos.insert(id, str(itemPilha))
            #adicionado a pilhaTodos no topo da pilha
            if not itemPilha:
                #se houver o cancelamento do cadastro ou algum valor inválido remove o último item cadastrado.
                pilhaTodos.pop()
                id = id-1
            else:
                print('Produto cadastrado!')
                
        elif opc == 2:
            #imprime toda a pilha formatada
            listar.Imprimir.listar(pilhaTodos)
        
        elif opc == 3:
            remover.Remover.excluir(pilhaTodos)
        return id
    
    