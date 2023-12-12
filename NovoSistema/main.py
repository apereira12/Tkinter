import customtkinter
import tkinter as tk
import os
from PIL import Image
import pandas as pd
from tkinter import ttk


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Campeonato Brasileiro")
        self.geometry("800x1200")

        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # load images with light and dark mode image
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "test_images")
        self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "Analise.png")), size=(26, 26))
        self.Brasileiro = customtkinter.CTkImage(Image.open(os.path.join(image_path, "CampeonatoBrasileiroteste.png")), size=(600, 300))
        self.image_icon_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "image_icon_light.png")), size=(20, 20))
        self.home_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "home_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "home_light.png")), size=(20, 20))
        self.chat_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "chat_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "chat_light.png")), size=(20, 20))
        self.add_user_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "add_user_dark.png")),
                                                     dark_image=Image.open(os.path.join(image_path, "add_user_light.png")), size=(20, 20))

        # create navigation frame
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(5, weight=1)

        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text="Análises do Brasileirão", image=self.logo_image,
                                                             compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.home_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Inicio",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                   image=self.home_image, anchor="w", command=self.home_button_event)
        self.home_button.grid(row=1, column=0, sticky="ew")

        self.frame_2_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Jogos",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.chat_image, anchor="w", command=self.frame_2_button_event)
        self.frame_2_button.grid(row=2, column=0, sticky="ew")

        self.frame_3_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Times",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.add_user_image, anchor="w", command=self.frame_3_button_event)
        self.frame_3_button.grid(row=3, column=0, sticky="ew")

        self.frame_4_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40,
                                                      border_spacing=10, text="Artilheiros",
                                                      fg_color="transparent", text_color=("gray10", "gray90"),
                                                      hover_color=("gray70", "gray30"),
                                                      image=self.add_user_image, anchor="w",
                                                      command=self.frame_3_button_event)
        self.frame_4_button.grid(row=4, column=0, sticky="ew")



        self.appearance_mode_menu = customtkinter.CTkOptionMenu(self.navigation_frame, values=["Light", "Dark", "System"],
                                                                command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=6, column=0, padx=20, pady=20, sticky="s")

        self.create_home_frame()
        self.create_second_frame()
        self.create_third_frame()
        # select default frame
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
        self.second_frame.grid_columnconfigure(0, weight=1)
        self.filtros1 = customtkinter.CTkFrame(self.second_frame)
        self.filtros1.grid(row=0, column=0, sticky="nsew")
        self.filtros1.grid_rowconfigure(7, weight=4)

        self.anos_disponiveis = []

        self.tree1 = ttk.Treeview(self.second_frame, show="headings")
        self.tree1.grid(row=3, column=0, columnspan=3, pady=10, sticky="nsew")



        # Adiciona dados do Excel à Treeview
        self.jogos("CampeonatoBrasileiro_2018-2023_SerieA.xlsx", sheet_name="Jogos")

        scrollbar = ttk.Scrollbar(self.second_frame, orient="vertical", command=self.tree1.yview)
        scrollbar.grid(row=3, column=3, sticky="ns")
        self.tree1.configure(yscrollcommand=scrollbar.set)

        scrollbar_x = ttk.Scrollbar(self.second_frame, orient="horizontal", command=self.tree1.xview)
        scrollbar_x.grid(row=4, column=0, columnspan=3, sticky="ew")
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

        # Cria a StringVar no escopo do frame
        self.anos_disponiveis = sorted(df['AnoJogo'].unique())
        self.anos_disponiveis = ["Todos"] + [str(ano) for ano in self.anos_disponiveis]

        # Cria um novo CTkOptionMenu com as novas opções
        self.filtro_var = tk.StringVar(master=self.filtros1)
        self.filtro_var.set("Todos")  # Valor padrão

        # Opção do filtro
        self.option_menu = tk.OptionMenu(self.filtros1, self.filtro_var, *self.anos_disponiveis)
        self.option_menu.grid(row=0, column=2, padx=(10, 0), pady=(10, 0))

        # Associar a função filtrar_dados à variável de controle
        self.filtro_var.trace_add("write", self.filtrar_dados)


        self.df = df  # Atribui o DataFrame à variável de instância

        self.atualizar_dados()  # Chama a função para atualizar os dados

    def filtrar_dados(self, *args):
        filtro = self.filtro_var.get()

        # Limpar a Treeview
        self.tree1.delete(*self.tree1.get_children())

        # Adicionar de volta apenas os itens que correspondem ao filtro
        for i, row in self.df.iterrows():
            if filtro == "Todos" or filtro.lower() == str(row['AnoJogo']).lower():
                values = [str(row[col]) for col in self.df.columns]
                self.tree1.insert("", "end", values=values)

    def atualizar_dados(self):
        # Limpar a Treeview
        self.tree1.delete(*self.tree1.get_children())

        # Itera sobre as linhas do DataFrame e insere os dados na Treeview
        for i, row in self.df.iterrows():
            values = [str(row[col]) for col in self.df.columns]
            self.tree1.insert("", "end", values=values)

    def create_third_frame(self):
        self.third_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")




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
