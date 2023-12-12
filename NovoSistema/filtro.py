import tkinter as tk
from tkinter import ttk

class FiltroTreeViewApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Filtro Treeview")

        # Dados de exemplo
        self.data = [
            ("1", "Item 1", "Descrição 1"),
            ("2", "Item 2", "Descrição 2"),
            ("3", "Item 3", "Descrição 3"),
            ("4", "Item 3", "Descrição 4"),
            # Adicione mais dados conforme necessário
        ]

        # Variáveis de controle para o filtro
        self.filtro_var = tk.StringVar()
        self.filtro_var.set("Todos")  # Valor padrão

        # Opções para o filtro
        unique_options = {item[1] for item in self.data}
        opcoes_filtro = ["Todos"] + sorted(list(unique_options))

        # Opção do filtro
        self.option_menu = tk.OptionMenu(root, self.filtro_var, *opcoes_filtro)
        self.option_menu.pack(pady=10)

        # Criação da Treeview
        columns = ("ID", "Nome", "Descrição")
        self.tree = ttk.Treeview(root, columns=columns, show="headings")

        # Configurando os cabeçalhos das colunas
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100)

        # Preencher a Treeview com dados iniciais
        self.atualizar_dados()

        self.tree.pack(expand=True, fill="both")

        # Associar a função filtrar_dados à variável de controle
        self.filtro_var.trace_add("write", self.filtrar_dados)

    def filtrar_dados(self, *args):
        filtro = self.filtro_var.get()

        # Limpar a Treeview
        self.tree.delete(*self.tree.get_children())

        # Adicionar de volta apenas os itens que correspondem ao filtro
        for item in self.data:
            if filtro == "Todos" or filtro.lower() == item[1].lower():
                self.tree.insert("", "end", values=item)

    def atualizar_dados(self):
        # Limpar a Treeview
        self.tree.delete(*self.tree.get_children())
        # Preencher a Treeview com todos os dados
        for item in self.data:
            self.tree.insert("", "end", values=item)

if __name__ == "__main__":
    root = tk.Tk()
    app = FiltroTreeViewApp(root)
    root.mainloop()
