import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import pandas as pd


class AplicacaoExcelViewer:
    def __init__(self, root):
        self.root = root
        self.root.title("Excel Viewer")
        self.root.geometry("1200x1000")  # Ajuste o tamanho conforme necessário

        #Comando para estender para todos os lados
        #os TK.(?) são para expandir para todos os lados
        self.frame = ttk.Frame(self.root, padding="10")
        self.frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        self.label = ttk.Label(self.frame, text="Escolha um arquivo Excel:")
        self.label.grid(row=0, column=0, columnspan=5, pady=10)

        self.botao_selecionar = ttk.Button(self.frame, text="Selecionar Arquivo", command=self.abrir_arquivo)
        self.botao_selecionar.grid(row=1, column=0, pady=10)

        self.botao_visualizar = ttk.Button(self.frame, text="Visualizar", command=self.visualizar_excel)
        self.botao_visualizar.grid(row=1, column=1, pady=10)

        self.botao_cotacoes = tk.Button(self.frame, text="Buscar Cotações")
        self.botao_cotacoes.grid(row=1, column=2, pady=10)


        self.tree = ttk.Treeview(self.frame)
        columns = ("Índice", "NumeroJogo", "Data", "Hora", "Estadio", "Cidade")
        self.tree["columns"] = columns

        # Configuração das colunas
        self.tree.heading("#0", text="Índice")
        self.tree.column("#0", anchor=tk.W, width=50)




        for col in columns[1:]:
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor=tk.W, width=150)  # Ajuste a largura conforme necessário

        self.tree.grid(row=2, column=0, columnspan=3, pady=10)

    def abrir_arquivo(self):
        filepath = filedialog.askopenfilename(title="Selecione um arquivo Excel",
                                              filetypes=[("Arquivos Excel", "*.xlsx;*.xls")])
        self.arquivo_excel = filepath

    def visualizar_excel(self):
        try:
            df = pd.read_excel(self.arquivo_excel)
            self.exibir_dados(df)
        except AttributeError:
            tk.messagebox.showwarning("Aviso", "Selecione um arquivo Excel antes de visualizar.")

    def exibir_dados(self, dataframe):
        # Limpa a treeview
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Adiciona os dados ao treeview
        for index, row in dataframe.iterrows():
            self.tree.insert("", index, text=index, values=[index] + list(row))


if __name__ == "__main__":
    root = tk.Tk()
    app = AplicacaoExcelViewer(root)
    root.mainloop()

