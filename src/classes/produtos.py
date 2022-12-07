class Product:
    def __init__(self, tipo, produto, qtd, medida, validade):
        self.tipo = str(tipo)
        self.produto = str(produto)
        self.qtd = str(qtd)
        self.medida = str(medida)
        self.validade = str(validade)
        self.itemCompleto ="  | |  " + self.tipo + "  | |  " + self.produto+ "  | |     " + self.qtd + "     | |  " + self.medida + "  | |  " + self.validade +"  | |  "
    def __str__(self):
        return str(self.itemCompleto)
    #retorna para a variável Item o objeto concatenado
