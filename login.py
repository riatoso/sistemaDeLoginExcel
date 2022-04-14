import pandas as pd


class Lista:
    def __init__(self):
        self.planilha_original = pd.read_excel("senhas.xlsx")
        self.df_original = pd.DataFrame(self.planilha_original)  # CRIA O DATAFRAME ORIGINAL

    def busca_login(self, nome):
        self.reload()
        if nome in [i for i in self.planilha_original["usuario"]]:
            print("Ja existe este usuario.")
            return 1
        else:
            print("Usuario não localizado")
            return 0

    def listar_todos(self):
        self.reload()
        print("LISTA DE LOGINS.")
        for i, x in zip(self.planilha_original["usuario"], self.planilha_original["senha"]):
            print(f"LOGIN -> {i} # SENHA -> {x}")

    def inserir_login(self, usuario, senha):
        df_novo = pd.DataFrame({'usuario': [usuario], 'senha': [senha]})  # CRIA O DATAFRAME SEMPRE COM COLCHETES
        df_lista_nova = pd.concat([self.df_original, df_novo])  # CRIA O DATAFRAME CONCATENADO
        try:
            df_lista_nova.to_excel("senhas.xlsx", index=False)
            print("Dados inseridos com sucesso.")
            self.reload()
        except:
            print("Ocorreu erro ao inserir dados.")

    def logar_sistema(self, usuario, senha):
        if usuario in [y for y in self.planilha_original["usuario"]]:
            for i, x in zip(self.planilha_original["usuario"], self.planilha_original["senha"]):
                try:
                    i = str(i)
                    x = str(x)
                    if i == usuario and x == senha:
                        print("LOGADO COM SUCESSO.")
                    if i == usuario and x != senha:
                        print("SENHA NÃO CONFERE.")
                except:
                    print("Erro desconhecido de formato de campos.")
        else:
            print("USUARIO E SENHAS INCORRETOS.")

    def reload(self):
        self.planilha_original = pd.read_excel("senhas.xlsx")
