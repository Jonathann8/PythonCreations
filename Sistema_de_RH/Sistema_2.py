from datetime import datetime

# Classe que representa a parte de salário do funcionário
class Salario:
    def __init__(self, salario_base, beneficios=None, descontos=None):
        self.salario_base = salario_base
        self.beneficios = beneficios if beneficios else {}
        self.descontos = descontos if descontos else {}

    def calcular_salario_liquido(self):
        total_beneficios = sum(self.beneficios.values())
        total_descontos = sum(self.descontos.values())
        return self.salario_base + total_beneficios - total_descontos

    def __str__(self):
        beneficios = '\n  '.join(f"{k}: R${v:.2f}" for k, v in self.beneficios.items()) or "Nenhum"
        descontos = '\n  '.join(f"{k}: R${v:.2f}" for k, v in self.descontos.items()) or "Nenhum"
        liquido = self.calcular_salario_liquido()
        return (f"Salário Base: R${self.salario_base:.2f}\n"
                f"Benefícios:\n  {beneficios}\n"
                f"Descontos:\n  {descontos}\n"
                f"Salário Líquido: R${liquido:.2f}")

# Classe principal do funcionário
class Funcionario:
    def __init__(self, nome, cpf, cargo, departamento, data_admissao, salario):
        self.nome = nome
        self.cpf = cpf
        self.cargo = cargo
        self.departamento = departamento
        self.data_admissao = self.validar_data(data_admissao)
        self.salario = salario

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
                f"Admissão: {self.data_admissao.strftime('%d/%m/%Y')}\n"
                f"\n--- Dados Salariais ---\n{self.salario}")

# Cadastro do salário
def cadastrar_salario():
    salario_base = float(input("Salário base: R$ "))

    beneficios = {}
    while True:
        add = input("Adicionar benefício? (s/n): ").lower()
        if add == 's':
            nome = input("Nome do benefício: ")
            valor = float(input(f"Valor de {nome}: R$ "))
            beneficios[nome] = valor
        else:
            break

    descontos = {}
    while True:
        add = input("Adicionar desconto? (s/n): ").lower()
        if add == 's':
            nome = input("Nome do desconto: ")
            valor = float(input(f"Valor de {nome}: R$ "))
            descontos[nome] = valor
        else:
            break

    return Salario(salario_base, beneficios, descontos)

# Cadastro completo do funcionário
def cadastrar_funcionario():
    nome = input("Nome completo: ")
    cpf = input("CPF ou ID interno: ")
    cargo = input("Cargo: ")
    departamento = input("Departamento: ")
    data_admissao = input("Data de admissão (DD/MM/AAAA): ")
    print("\n--- Cadastro Salarial ---")
    salario = cadastrar_salario()

    funcionario = Funcionario(nome, cpf, cargo, departamento, data_admissao, salario)
    return funcionario

# Lista todos os funcionários
def exibir_funcionarios(lista):
    for i, f in enumerate(lista):
        print(f"\nFuncionário {i+1}:")
        print(f)

# Menu principal
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
