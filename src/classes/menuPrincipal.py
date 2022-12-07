from classes.impressaoTelas import EstruturasImpressoes
from classes.validador import Validadores
from classes.funcoes import Funcoes
import collections

class MenuPrincipal:
    def menu():
        opc = -1
        pilhaTodos = []
        #inicia a pilha de todos os produtos
        i = 0
        while opc != 0:
            EstruturasImpressoes.topoTela()
            print(" "*2+"Insira o numero da opção desejada:")
            print(" "*2+"1 - Cadastrar produtos\n"+" "*2+"2 - Listar produtos cadastrados\n"+" "*2+"3 - Remover produtos cadastrados\n"+" "*2+"0 - Sair\n")
            opc = (Validadores.validarInputInt())
            #valida se o valor inserido está correto
            i = Funcoes.func(opc, i, pilhaTodos)
            #pega o valor do input e dá continuidade para as funçoes do sistema

        print(" "*2+"Você finalizou o programa.")
