from classes import listar
from classes.impressaoTelas import EstruturasImpressoes
from classes.validador import Validadores
class Remover:
    def excluir(pilha):
        tamPilha = len(pilha)
        idExclusao = -1
        while idExclusao < 0:
            listar.Imprimir.listar(pilha)
            if tamPilha == 0:
                print("Impossível remover!")
                return
            else:
                print(" "*2+'Insira o valor do Id do produto que deseja excluir ou 0 para sair:')
                idExclusao = Validadores.validarInputInt()
                idExclusao= Validadores.validarIdExcluir(idExclusao, tamPilha)
                if idExclusao == False:
                    return
                else:
                    if idExclusao >= 0:
                        IdProd = idExclusao -1
                        EstruturasImpressoes.estruTabela()
                        print("  | |  ", idExclusao , pilha[IdProd])
                        print(" "*2+"Você deseja excluir esse item?")
                        print(" "*2+"1 - Sim\n"+" "*2+"2 - Não\n")
                        confirmDelete = Validadores.validarInputInt()
                        while confirmDelete >2 or confirmDelete < 0:
                            print(" "*2+" Valor inválido, insira novamente!\n")
                            EstruturasImpressoes.estruTabela()
                            print("  | |  ", idExclusao , pilha[IdProd])
                            print(" "*2+"Você deseja excluir esse item?")
                            print(" "*2+"1 - Sim\n"+" "*2+"2 - Não\n")
                            confirmDelete = Validadores.validarInputInt()
                        if confirmDelete == 1:
                            print(" "*2+"Produto excluído!")
                            pilha.pop(IdProd)
                        elif confirmDelete == 2:
                            print(" "*2+"Remoção do item cancelada!")
                            return
                            




