class No:
    def __init__(self, pergunta=None, cor=None, sim=None, nao=None):
        self.pergunta = pergunta
        self.cor = cor
        self.sim = sim
        self.nao = nao

class Fila:
    def __init__(self):
        self.itens = []

    def adicionar(self, nome):
        self.itens.append(nome)

    def remover(self):
        if self.itens:
            return self.itens.pop(0)
        return None

    def tamanho(self):
        return len(self.itens)

    def primeiro(self):
        return self.itens[0] if self.itens else None

def montar_arvore():
    vermelho = No(cor="Vermelho")
    laranja = No(cor="Laranja")
    amarelo = No(cor="Amarelo")
    verde = No(cor="Verde")
    azul = No(cor="Azul")

    no4 = No("É um problema leve (ex: dor leve, receita)?", sim=verde, nao=azul)
    no3 = No("Está com dor forte?", sim=amarelo, nao=no4)
    no2 = No("Está consciente?", sim=no3, nao=laranja)
    raiz = No("O paciente está respirando?", sim=no2, nao=vermelho)

    return raiz

def criar_filas():
    return {c: Fila() for c in ["Vermelho", "Laranja", "Amarelo", "Verde", "Azul"]}

def triagem(paciente, no, filas):
    while no.cor is None:
        resposta = input(f"{no.pergunta} (sim/não): ").strip().lower()
        if resposta == "sim":
            no = no.sim
        elif resposta == "não":
            no = no.nao
        else:
            print("Resposta inválida, digite 'sim' ou 'não'.")
    filas[no.cor].adicionar(paciente)
    print(f"{paciente} foi colocado na fila {no.cor}.")

if __name__ == "__main__":
    arvore = montar_arvore()
    filas = criar_filas()

    while True:
        paciente = input("Nome do paciente (ou 'sair' para encerrar): ").strip()
        if paciente.lower() == "sair":
            break
        triagem(paciente, arvore, filas)

    print("\nFilas de pacientes:")
    for cor, fila in filas.items():
        print(f"{cor}: {fila.itens}")


