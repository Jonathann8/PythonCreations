from datetime import datetime

# Classe que representa um funcionário
class Funcionario:
    def __init__(self, nome, cpf, cargo, departamento, data_admissao):
        self.nome = nome
        self.cpf = cpf
        self.cargo = cargo
        self.departamento = departamento
        self.data_admissao = self.validar_data(data_admissao)

    def validar_data(self, data_str):
        try:
            return datetime.strptime(data_str, "%d/%m/%Y")
        except ValueError:
            raise ValueError("Data de admissão inválida. Use o formato DD/MM/AAAA.")

    def __str__(self):
        return (f"Nome: {self.nome}\n"
                f"CPF/ID: {self.cpf}\n"
                f"Cargo: {self.cargo}\n"
                f"Departamento: {self.departamento}\n"
                f"Admissão: {self.data_admissao.strftime('%d/%m/%Y')}")

# Função para cadastrar um novo funcionário
def cadastrar_funcionario():
    nome = input("Nome completo: ")
    cpf = input("CPF ou ID interno: ")
    cargo = input("Cargo: ")
    departamento = input("Departamento: ")
    data_admissao = input("Data de admissão (DD/MM/AAAA): ")

    funcionario = Funcionario(nome, cpf, cargo, departamento, data_admissao)
    return funcionario

# Função para exibir todos os funcionários cadastrados
def exibir_funcionarios(lista):
    for i, f in enumerate(lista):
        print(f"\nFuncionário {i+1}:")
        print(f)

# Menu principal do sistema
def menu():
    funcionarios = []

    while True:
        print("\n--- Sistema de RH ---")
        print("1. Cadastrar funcionário")
        print("2. Listar funcionários")
        print("3. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            try:
                funcionario = cadastrar_funcionario()
                funcionarios.append(funcionario)
                print("Funcionário cadastrado com sucesso!")
            except ValueError as e:
                print(f"Erro: {e}")
        elif opcao == "2":
            if funcionarios:
                exibir_funcionarios(funcionarios)
            else:
                print("Nenhum funcionário cadastrado.")
        elif opcao == "3":
            print("Encerrando o sistema.")
            break
        else:
            print("Opção inválida.")

# Executar o sistema
menu()
