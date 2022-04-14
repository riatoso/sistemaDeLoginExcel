import time

from login import Lista

if __name__ == "__main__":
    temp = Lista()
    while True:
        time.sleep(2)
        print(50 * "-")
        print("1-  FAZER LOGIN.")
        print("2-  BUSCAR LOGIN.")
        print("3-  CADASTRAR LOGIN.")
        print("4-  LISTAR TODOS OS LOGINS.")
        print("5-  SAIR DO SISTEMA DE LOGIN.")
        print("#   DIGITE A OPÇÃO PARA PROSSEGUIR: ")
        print(50 * "-")
        # VALIDAR OPCAO
        while True:
            opcao = input("Qual sua opcao? -> ")
            try:
                opcao = int(opcao)
                break
            except:
                print("Digite um valor valido.")
                continue

        print(50 * "-")
        if opcao == 5:
            print("Saindo.")
            time.sleep(2)
            break
        if opcao == 4:
            temp.listar_todos()
            continue
        if opcao == 3:
            while True:
                caduser = input("Digite um nome de usuario -> ").lower()
                print("Buscando no banco de dados por usuario...")
                status = temp.busca_login(caduser)
                time.sleep(2)
                if status == 1:
                    print("Digite outro nome de usuario , pois o mesmo ja existe.")
                    continuar = input("Deseja continuar como o cadastro -> (s/n): ").lower()
                    if continuar[0] == "s":
                        continue
                    else:
                        print("Finalizando o cadastro de login.")
                        break
                if status == 0:
                    print(f"Usuario {caduser} pode ser cadastrado.")
                    while True:
                        cadsenha = input("Digite sua senha para cadastro - > (max 8 caracteres) : ")
                        if len(cadsenha) > 8:
                            print(f"Senha digitada {cadsenha} sua senha excedeu 8 caracteres.")
                            print("Por favor redigite a mesma.")
                            continue
                        elif len(cadsenha) <= 0:
                            print("Sua senha não pode ser em branco.")
                            print("Redigite a mesma.")
                            continue
                        else:
                            while True:
                                cadsenha2 = input("Por favor confirme sua senha -> ")
                                if cadsenha == cadsenha2:
                                    print("Veificação de senhas ok.")
                                    break
                                else:
                                    print("As senhas não são iguais. Redigite a verificação de senha ->  ")
                                    continue
                        break
                    temp.inserir_login(caduser, cadsenha)
                    break

        if opcao == 2:
            nome = input("Digite o usuario para realizar a pesquisa -> ").lower()
            temp.busca_login(nome)
            continue
        if opcao == 1:
            while True:
                loguser = input("Digite o usuario: ").lower()
                logsenha = input("Digite a senha:  ")
                confere = input(f"Usuario {loguser} , senha {logsenha} -> Confirma (s/n) :").lower()
                if confere == "s":
                    break
                elif confere == "n":
                    print("Ok , redigite usuario e senha.")
                    continue
                else:
                    print("Digite uma opcao valida (s/n).")
                    continue
            temp.logar_sistema(loguser, logsenha)
            continue
        if opcao not in range(1, 5):
            print("Digite um opcao valida.")
            continue
