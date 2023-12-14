import customtkinter
import tkinter as tk
import os
from PIL import Image
import pandas as pd
from tkinter import ttk
from unidecode import unidecode
import re



customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # Set dark mode style
        self.style = ttk.Style()
        self.style.theme_use('clam')


        self.style.configure("TButton", foreground="green", background="#06C258")  # Button style
        self.style.configure("TLabel", foreground="green", background="#06C258")   # Label style


        self.title("Campeonato Brasileiro")
        self.geometry("1200x1200")
        self.resizable(True, True)
        self.state("zoomed")


        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # load images with light and dark mode image
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "test_images")
        self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "Analise.png")), size=(26, 26))
        self.Brasileiro = customtkinter.CTkImage(Image.open(os.path.join(image_path, "CampeonatoBrasileiroteste.png")), size=(600, 300))
        self.image_icon_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "image_icon_light.png")), size=(20, 20))
        self.home_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "home_light.png")),
                                                 size=(20, 20))
        self.chat_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "chat_light.png")),
                                                size=(20, 20))
        self.add_user_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "add_user_light.png")),
                                                    size=(20, 20))

        # create navigation frame
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="#262626")
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(5, weight=1)

        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text="Análises do Brasileirão", image=self.logo_image,
                                                             compound="left", font=customtkinter.CTkFont(size=18, weight="bold"), text_color=("#7AF71B", "#7AF71B"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.home_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Inicio",
                                                   fg_color="transparent", text_color=("#1BF77A", "#1BF77A"),font=('Arial',15), hover_color=("gray70", "gray30"),
                                                   image=self.home_image, anchor="w", command=self.home_button_event)
        self.home_button.grid(row=1, column=0, sticky="ew")

        self.frame_2_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Jogos",
                                                      fg_color="transparent", text_color=("#1BF77A", "#1BF77A"),font=('Arial',15),hover_color=("gray70", "gray30"),
                                                      image=self.chat_image, anchor="w", command=self.frame_2_button_event)
        self.frame_2_button.grid(row=2, column=0, sticky="ew")

        self.frame_3_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Times",
                                                      fg_color="transparent", text_color=("#1BF77A", "#1BF77A"),font=('Arial',15), hover_color=("gray70", "gray30"),
                                                      image=self.add_user_image, anchor="w", command=self.frame_3_button_event)
        self.frame_3_button.grid(row=3, column=0, sticky="ew")

        self.frame_4_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40,
                                                      border_spacing=10, text="Artilheiros",
                                                      fg_color="transparent", text_color=("#1BF77A", "#1BF77A"),font=('Arial',15),
                                                      hover_color=("gray70", "gray30"),
                                                      image=self.add_user_image, anchor="w",
                                                      command=self.frame_3_button_event)
        self.frame_4_button.grid(row=4, column=0, sticky="ew")

        self.create_home_frame()
        self.create_second_frame()
        self.create_third_frame()



        self.select_frame_by_name("home")

    def create_home_frame(self):
        self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid_columnconfigure(0, weight=1)

        self.home_frame_large_image_label = customtkinter.CTkLabel(self.home_frame, text="", image=self.Brasileiro)
        self.home_frame_large_image_label.grid(row=0, column=0, padx=20, pady=10)

        self.home_frame_button_1 = customtkinter.CTkButton(self.home_frame, text="Número de Jogos", image=self.image_icon_image)
        self.home_frame_button_1.grid(row=2, column=0, padx=20, pady=10)
        self.home_frame_button_2 = customtkinter.CTkButton(self.home_frame, text="Anos Analisados", image=self.image_icon_image, compound="right")
        self.home_frame_button_2.grid(row=3, column=0, padx=20, pady=10)
        self.textboxHome = customtkinter.CTkTextbox(self.home_frame)
        self.textboxHome.grid(row=1, column=0, padx=(10, 0), pady=(10, 0))
        self.textboxHome.insert("0.0", "Seja Bem-vindo a \n "
                                           "\n Análise d"
                                           "o Brasileirão", customtkinter.CENTER)

    def create_second_frame(self):
        self.second_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.second_frame.grid_columnconfigure(1, weight=10)
        self.second_frame.rowconfigure(1, weight=10)
        self.filtros1 = customtkinter.CTkFrame(self.second_frame, fg_color="#808080")
        self.filtros1.place(relx=0.63,rely=0.02, relwidth= 0.35, relheight= 0.15)
        self.textlabelfiltro = customtkinter.CTkLabel(master=self.filtros1,text="Filtros para Análises", font=("verdana",15), text_color=("#1BF77A", "#1BF77A"))
        self.textlabelfiltro.place(relx=0.01,rely=0.2, relwidth= 0.55, relheight= 0.3)
        self.textlabelTitulo = customtkinter.CTkLabel(master=self.second_frame, text="Tabela de Jogos", width=10, font=("verdana",25), text_color=("#1BF77A", "#1BF77A"))
        self.textlabelTitulo.place(relx=0.35,rely=0.20, relwidth= 0.28, relheight= 0.1)


        self.frameTabela=customtkinter.CTkFrame(self.second_frame, fg_color="transparent")
        self.frameTabela.place(relx=0.03, rely=0.28, relwidth= 0.88, relheight= 0.70)

        style1 = ttk.Style()
        style1.configure("Treeview.Heading", font=("Helvetica", 10, "bold"))
        style1.configure("Treeview", font=("Helvetica", 10), rowheight=25)
        style1.configure("Treeview.Tree", background="#262626")
        style1.configure("Treeview.TFrame", background="#f2f2f2")
        self.tree1 = ttk.Treeview(self.frameTabela, show="headings", style="Treeview.TFrame")

        self.tree1.place(relx=0.05,rely=0.01, relwidth= 0.93 , relheight= 0.98)


        # Adiciona dados do Excel à Treeview
        self.jogos("CampeonatoBrasileiro_2018-2023_SerieA.xlsx", sheet_name="Jogos")

        scrollbar = ttk.Scrollbar(self.frameTabela, orient="vertical", command=self.tree1.yview)
        scrollbar.place(relx=0.98,rely=0.01, relwidth= 0.02, relheight= 0.965)
        self.tree1.configure(yscrollcommand=scrollbar.set)

        scrollbar_x = ttk.Scrollbar(self.frameTabela, orient="horizontal", command=self.tree1.xview)
        scrollbar_x.place(relx=0.05,rely=0.96, relwidth= 0.93, relheight= 0.05)
        self.tree1.configure(xscrollcommand=scrollbar_x.set)

    def jogos(self, arquivo_excel, sheet_name):
        # Lê os dados do Excel usando pandas
        df = pd.read_excel(arquivo_excel, sheet_name)

        # Configuração das colunas
        self.tree1["columns"] = df.columns.tolist()

        for col in df.columns:
            self.tree1.heading(col, text=col)
            self.tree1.column(col, anchor=tk.W, width=150)

        # Itera sobre as linhas do DataFrame e insere os dados na Treeview
        for i, row in df.iterrows():
            values = [str(row[col]) for col in df.columns]
            self.tree1.insert("", "end", values=values)

        # Criar as listas para os filtros
        self.anos_disponiveis = sorted(df['AnoJogo'].unique())
        self.anos_disponiveis = ["Todos os Anos"] + [str(i) for i in self.anos_disponiveis]
        self.Resultado_disponivel = sorted(df['Quem Venceu?'].unique())
        self.Resultado_disponivel = ["Todos Resultados"] + [str(i) for i in self.Resultado_disponivel]
        self.rodada = sorted(df['Rodada'].unique())
        self.Rodada = ["Todas Rodadas"] + [str(i) for i in self.rodada]

        #criar os filtros
        self.Resultados = customtkinter.CTkOptionMenu(self.filtros1, values=self.Resultado_disponivel,
                                                       command=self.filtrar_dados)
        self.Anos = customtkinter.CTkOptionMenu(self.filtros1, values=self.anos_disponiveis,
                                                 command=self.filtrar_dados)
        self.Rodada = customtkinter.CTkOptionMenu(self.filtros1, values=self.Rodada,
                                                       command=self.filtrar_dados)

        #localização dos filtros
        self.Anos.place(relx=0.55, rely=0.1, relwidth=0.45, relheight=0.25)
        self.Resultados.place(relx=0.55, rely=0.4, relwidth=0.45, relheight=0.25)
        self.Rodada.place(relx=0.55, rely=0.7, relwidth=0.45, relheight=0.25)




        items = self.tree1.get_children()
        quantidade_registros = len(items)
        self.quantidadeframe = customtkinter.CTkFrame(self.second_frame, fg_color="#0d0d0d")
        self.quantidadeframe.place(relx=0.05, rely=0.02, relwidth=0.15, relheight=0.15)

        self.label_contagem1 = customtkinter.CTkLabel(self.quantidadeframe, text=f"Quantidade Registros",
                                                      fg_color="transparent", text_color=("#1BF77A", "#1BF77A"), font=("verdana",12))
        self.label_contagem1.place(relx=0.05, rely=0.03, relwidth=0.93, relheight=0.45)


        self.label_contagem = customtkinter.CTkLabel(self.quantidadeframe, text=f"{quantidade_registros}", font=("Arial",25))
        self.label_contagem.place(relx=0.30, rely=0.55, relwidth=0.45, relheight=0.30)





        self.df = df  # Atribui o DataFrame à variável de instância

        self.atualizar_dados()  # Chama a função para atualizar os dados

    def filtrar_dados(self, *args):
        filtroAno = self.Anos.get()
        filtroResultado = self.Resultados.get()
        filtroRodada=self.Rodada.get()

        # Limpar a Treeview
        self.tree1.delete(*self.tree1.get_children())

        # Adicionar de volta apenas os itens que correspondem ao filtro
        for i, row in self.df.iterrows():
            if (filtroAno == "Todos os Anos" or filtroAno.lower() == str(row['AnoJogo']).lower()) and \
                    (filtroResultado == "Todos Resultados" or filtroResultado.lower() == str(row['Quem Venceu?']).lower()) and \
                    (filtroRodada == "Todas Rodadas" or filtroRodada.lower() == str(row['Rodada']).lower()):
                values = [str(row[col]) for col in self.df.columns]
                self.tree1.insert("", "end", values=values)
        items = self.tree1.get_children()
        quantidade_registros = len(items)
        self.label_contagem.configure(text=str(quantidade_registros))




    def atualizar_dados(self):
        # Limpar a Treeview
        self.tree1.delete(*self.tree1.get_children())

        # Itera sobre as linhas do DataFrame e insere os dados na Treeview
        for i, row in self.df.iterrows():
            values = [str(row[col]) for col in self.df.columns]
            self.tree1.insert("", "end", values=values)






    def create_third_frame(self):
        self.third_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.filtros1 = customtkinter.CTkFrame(self.third_frame, fg_color="#808080")
        self.filtros1.place(relx=0.63, rely=0.02, relwidth=0.37, relheight=0.22)
        self.textlabelfiltro = customtkinter.CTkLabel(master=self.filtros1, text="Filtros para Análises",
                                                      font=("verdana", 15), text_color=("#1BF77A", "#1BF77A"))
        self.textlabelfiltro.place(relx=0.01, rely=0.2, relwidth=0.55, relheight=0.3)
        self.textlabelTitulo = customtkinter.CTkLabel(master=self.third_frame, text="Tabela de Jogos", width=10,
                                                      font=("verdana", 25), text_color=("#1BF77A", "#1BF77A"))
        self.textlabelTitulo.place(relx=0.35, rely=0.20, relwidth=0.28, relheight=0.1)

        self.frameTabela = customtkinter.CTkFrame(self.third_frame, fg_color="transparent")
        self.frameTabela.place(relx=0.03, rely=0.4, relwidth=0.88, relheight=0.57)

        style1 = ttk.Style()
        style1.configure("Treeview.Heading", font=("Helvetica", 10, "bold"))
        style1.configure("Treeview", font=("Helvetica", 10), rowheight=25)
        style1.configure("Treeview.Tree", background="#262626")
        style1.configure("Treeview.TFrame", background="#f2f2f2")
        self.treeTimes = ttk.Treeview(self.frameTabela, show="headings", style="Treeview.TFrame")

        self.treeTimes.place(relx=0.05, rely=0.01, relwidth=0.93, relheight=0.98)

        # Adiciona dados do Excel à Treeview
        self.times("CampeonatoBrasileiro_2018-2023_SerieA.xlsx", sheet_name="DesempenhoIndividual")

        scrollbar = ttk.Scrollbar(self.frameTabela, orient="vertical", command=self.treeTimes.yview)
        scrollbar.place(relx=0.98, rely=0.01, relwidth=0.02, relheight=0.965)
        self.treeTimes.configure(yscrollcommand=scrollbar.set)

        scrollbar_x = ttk.Scrollbar(self.frameTabela, orient="horizontal", command=self.treeTimes.xview)
        scrollbar_x.place(relx=0.05, rely=0.96, relwidth=0.93, relheight=0.05)
        self.treeTimes.configure(xscrollcommand=scrollbar_x.set)

    def times(self, arquivo_excel, sheet_name):
        # Lê os dados do Excel usando pandas
        dx = pd.read_excel(arquivo_excel, sheet_name)

        dx['Time'] = dx['Time'].apply(unidecode)
        dx['Time'] = dx['Time'].str.replace(r'\s*S\.?A\.?F\s*', '', regex=True, case=False)
        dx['Time'] = dx['Time'].apply(str.title)
        dx['Time'] = dx['Time'].apply(lambda x: x.replace('Fc', '').strip())  # Remove "Fc" e espaços antes e depois
        # Aplicar a lambda para modificar o valor da coluna 'Time' com base nas condições
        dx['Time'] = dx.apply(lambda row: 'Athletico Paranaense' if row['Time'] == 'Atletico' and row['UF Time'] == 'PR' else row['Time'],axis=1)
        dx['Time'] = dx.apply(lambda row: 'America Mineiro' if row['Time'] == 'America' and row['UF Time'] == 'MG' else row['Time'],axis=1)
        dx['Time'] = dx.apply(lambda row: 'Atletico Mineiro' if row['Time'] == 'Atletico' and row['UF Time'] == 'MG' else row['Time'],axis=1)
        dx['Time'] = dx.apply(lambda row: 'AtletiCO Goianiense' if row['Time'] == 'Atletico' and row['UF Time'] == 'GO' else row['Time'],axis=1)
        dx['Rodada'] = dx['NumeroJogo'].apply(lambda num_jogo: int(num_jogo / 10) if num_jogo % 10 == 0 else int(num_jogo // 10) + 1)
        dx['Resultado'] = dx.apply(lambda row: 'Vitória' if row['Pontos'] == 3 else ('Empatou' if row['Pontos'] == 1 else 'Derrota'), axis=1)


        # Configuração das colunas
        self.treeTimes["columns"] = dx.columns.tolist()

        for col in dx.columns:
            self.treeTimes.heading(col, text=col)
            self.treeTimes.column(col, anchor=tk.W, width=150)

        # Itera sobre as linhas do DataFrame e insere os dados na Treeview
        for i, row in dx.iterrows():
            values = [str(row[col]) for col in dx.columns]
            self.treeTimes.insert("", "end", values=values)

        # Criar as listas para os filtros
        self.anos_disponiveis1 = sorted(dx['AnoJogo'].unique())
        self.anos_disponiveis1 = ["Todos os Anos"] + [str(i) for i in self.anos_disponiveis1]
        self.resultado_disponivel1 = sorted(dx['Resultado'].unique())
        self.resultado_disponivel1 = ["Todos Resultados"] + [str(i) for i in self.resultado_disponivel1]
        self.rodada1 = sorted(dx['Rodada'].unique())
        self.Rodada1 = ["Todas Rodadas"] + [str(i) for i in self.rodada]
        self.time1 = sorted(dx['Time'].unique())
        self.Time1 = ["Todos Times"] + [str(i) for i in self.time1]


        # criar os filtros
        self.Resultados1 = customtkinter.CTkOptionMenu(self.filtros1, values=self.resultado_disponivel1,
                                                       command=self.filtrar_dados1)
        self.Anos1 = customtkinter.CTkOptionMenu(self.filtros1, values=self.anos_disponiveis1,
                                                 command=self.filtrar_dados1)
        self.Rodada1 = customtkinter.CTkOptionMenu(self.filtros1, values=self.Rodada1,
                                                  command=self.filtrar_dados1)
        self.Time1 = customtkinter.CTkOptionMenu(self.filtros1, values=self.Time1,
                                                  command=self.filtrar_dados1)

        # localização dos filtros
        self.Anos1.place(relx=0.55, rely=0.02, relwidth=0.45, relheight=0.18)
        self.Resultados1.place(relx=0.55, rely=0.27, relwidth=0.45, relheight=0.18)
        self.Rodada1.place(relx=0.55, rely=0.52, relwidth=0.45, relheight=0.18)
        self.Time1.place(relx=0.55, rely=0.77, relwidth=0.45, relheight=0.18)

        items1 = self.treeTimes.get_children()
        quantidade_registros1 = len(items1)
        self.quantidadeframe = customtkinter.CTkFrame(self.third_frame, fg_color="#0d0d0d")
        self.quantidadeframe.place(relx=0.05, rely=0.02, relwidth=0.15, relheight=0.15)

        self.label_contagem1 = customtkinter.CTkLabel(self.quantidadeframe, text=f"Quantidade Registros",
                                                      fg_color="transparent", text_color=("#1BF77A", "#1BF77A"),
                                                      font=("verdana", 12))
        self.label_contagem1.place(relx=0.05, rely=0.03, relwidth=0.93, relheight=0.45)

        self.label_contagem1 = customtkinter.CTkLabel(self.quantidadeframe, text=f"{quantidade_registros1}",
                                                     font=("Arial", 25))
        self.label_contagem1.place(relx=0.30, rely=0.55, relwidth=0.45, relheight=0.30)

        self.dx = dx  # Atribui o DataFrame à variável de instância

        self.atualizar_dados1()  # Chama a função para atualizar os dados

    def filtrar_dados1(self, *args):
        filtroAno1 = self.Anos1.get()
        filtroResultado1 = self.Resultados1.get()
        filtroRodada1 = self.Rodada1.get()
        filtroTime1 = self.Time1.get()

        # Limpar a Treeview
        self.treeTimes.delete(*self.treeTimes.get_children())

        # Adicionar de volta apenas os itens que correspondem ao filtro
        for i, row in self.dx.iterrows():
            if (filtroAno1 == "Todos os Anos" or filtroAno1.lower() == str(row['AnoJogo']).lower()) and \
                    (filtroResultado1 == "Todos Resultados" or filtroResultado1.lower() == str(
                        row['Resultado']).lower()) and \
                    (filtroRodada1 == "Todas Rodadas" or filtroRodada1.lower() == str(row['Rodada']).lower()) and \
                    (filtroTime1 == "Todos Times" or filtroTime1.lower() == str(row['Time']).lower()):
                values = [str(row[col]) for col in self.dx.columns]
                self.treeTimes.insert("", "end", values=values)
        items1 = self.treeTimes.get_children()
        quantidade_registros1 = len(items1)
        self.label_contagem1.configure(text=str(quantidade_registros1))

    def atualizar_dados1(self):
        # Limpar a Treeview
        self.treeTimes.delete(*self.treeTimes.get_children())

        # Itera sobre as linhas do DataFrame e insere os dados na Treeview
        for i, row in self.dx.iterrows():
            values = [str(row[col]) for col in self.dx.columns]
            self.treeTimes.insert("", "end", values=values)

    def select_frame_by_name(self, name):
        # set button color for selected button
        self.home_button.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
        self.frame_2_button.configure(fg_color=("gray75", "gray25") if name == "frame_2" else "transparent")
        self.frame_3_button.configure(fg_color=("gray75", "gray25") if name == "frame_3" else "transparent")

        # show selected frame
        if name == "home":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()
        if name == "frame_2":
            self.second_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.second_frame.grid_forget()
        if name == "frame_3":
            self.third_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.third_frame.grid_forget()

    def home_button_event(self):
        self.select_frame_by_name("home")

    def frame_2_button_event(self):
        self.select_frame_by_name("frame_2")

    def frame_3_button_event(self):
        self.select_frame_by_name("frame_3")

    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)




if __name__ == "__main__":
    app = App()
    app.mainloop()





if __name__ == "__main__":
    app = App()
    app.mainloop()
