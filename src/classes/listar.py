from classes.impressaoTelas import EstruturasImpressoes

class Imprimir:
    def listar(pilhaTodos):
        tam = len(pilhaTodos)
        #pega o tamanho da pilha
        i = 0
        if tam == 0:
            print('Nenhum produto cadastrado!')
            #avisa o usuário que não existem produtos cadastrados
        else:
            EstruturasImpressoes.estruTabela()
            while i < tam:
                #enquanto o contador for menor que o tamanho da pilha ele vai imprimir um item
                print("  | |  ", i+1 , pilhaTodos[i])
                #printa um objeto por vez da pilhas
                i = i + 1