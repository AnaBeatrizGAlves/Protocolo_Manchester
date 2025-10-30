import tkinter as tk
from tkinter import messagebox, simpledialog
from Logica import montar_arvore, criar_filas

class TriagemApp:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title("Sistema de Triagem")
        self.janela.geometry("500x400")
        self.janela.configure(bg="white")

        self.arvore = montar_arvore()
        self.filas = criar_filas()
        self.cores = {
            "Vermelho": "#ff4d4d",
            "Laranja": "#ff944d",
            "Amarelo": "#fff066",
            "Verde": "#99ff99",
            "Azul": "#99ccff"
        }

        self.criar_tela()
        self.atualizar_status()

    def criar_tela(self):
        tk.Label(self.janela, text="Triagem De Pacientes",
                 bg="white", font=("Arial", 14, "bold")).pack(pady=10)

        tk.Button(self.janela, text="Cadastrar Paciente",
                  command=self.cadastrar, width=25).pack(pady=5)
        tk.Button(self.janela, text="Chamar Paciente",
                  command=self.chamar, width=25).pack(pady=5)
        tk.Button(self.janela, text="Mostrar Status",
                  command=self.mostrar_status, width=25).pack(pady=5)
        tk.Button(self.janela, text="Sair",
                  command=self.janela.destroy, width=25).pack(pady=5)

        self.rotulos = {}
        for cor in self.filas:
            linha = tk.Frame(self.janela, bg="white")
            linha.pack(pady=2)
            tk.Label(linha, text=f"{cor}:", width=10, anchor="w",
                     fg=self.cores[cor], bg="white").pack(side="left")
            lbl = tk.Label(linha, text="0 paciente(s)", bg="white")
            lbl.pack(side="left")
            self.rotulos[cor] = lbl

    def cadastrar(self):
        nome = simpledialog.askstring("Cadastro", "Nome do paciente:")
        if not nome:
            return
        cor = self.perguntar(self.arvore)
        self.filas[cor].adicionar(nome)
        messagebox.showinfo("Cadastrado", f"{nome} foi classificado como {cor}.")
        self.atualizar_status()

    def perguntar(self, no):
        while no.cor is None:
            if messagebox.askyesno("Pergunta", no.pergunta):
                no = no.sim
            else:
                no = no.nao
        return no.cor

    def chamar(self):
        for cor in ["Vermelho", "Laranja", "Amarelo", "Verde", "Azul"]:
            if self.filas[cor].tamanho() > 0:
                paciente = self.filas[cor].remover()
                self.destacar(cor)
                messagebox.showinfo("Chamando", f"Chamando {paciente} ({cor})")
                self.atualizar_status()
                return
        messagebox.showinfo("Filas Vazias", "Nenhum paciente aguardando.")

    def mostrar_status(self):
        texto = ""
        for cor, fila in self.filas.items():
            prox = fila.primeiro() if fila.primeiro() else "—"
            texto += f"{cor}: {fila.tamanho()} paciente(s) | Próximo: {prox}\n"
        messagebox.showinfo("Status das Filas", texto)

    def atualizar_status(self):
        for cor, fila in self.filas.items():
            self.rotulos[cor].config(text=f"{fila.tamanho()} paciente(s)")

    def destacar(self, cor):
        self.janela.configure(bg=self.cores[cor])
        self.janela.after(2000, lambda: self.janela.configure(bg="white"))


if __name__ == "__main__":
    janela = tk.Tk()
    TriagemApp(janela)
    janela.mainloop()
