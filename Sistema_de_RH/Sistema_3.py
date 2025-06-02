from datetime import datetime, time, timedelta

# ---------- CLASSES AUXILIARES ----------

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


class HorarioTrabalho:
    def __init__(self, hora_inicio, hora_fim, escala):
        self.hora_inicio = self.str_para_hora(hora_inicio)
        self.hora_fim = self.str_para_hora(hora_fim)
        self.escala = escala
        self.banco_de_horas = timedelta()

    def str_para_hora(self, hora_str):
        return datetime.strptime(hora_str, "%H:%M").time()

    def calcular_jornada_diaria(self):
        dt_inicio = datetime.combine(datetime.today(), self.hora_inicio)
        dt_fim = datetime.combine(datetime.today(), self.hora_fim)
        return dt_fim - dt_inicio

    def __str__(self):
        return (f"Jornada: {self.hora_inicio.strftime('%H:%M')} às {self.hora_fim.strftime('%H:%M')} | "
                f"Escala: {self.escala} | Banco de Horas: {self.banco_de_horas}")


class RegistroPonto:
    def __init__(self):
        self.registros = {}  # data -> (entrada, saída)

    def registrar_entrada(self, data, hora):
        if data not in self.registros:
            self.registros[data] = [hora, None]
        else:
            self.registros[data][0] = hora

    def registrar_saida(self, data, hora):
        if data in self.registros:
            self.registros[data][1] = hora
        else:
            self.registros[data] = [None, hora]

    def calcular_horas_trabalhadas(self, data):
        entrada, saida = self.registros.get(data, (None, None))
        if entrada and saida:
            return saida - entrada
        return timedelta(0)

    def __str__(self):
        resultado = "Registros de Ponto:\n"
        for data, (entrada, saida) in self.registros.items():
            resultado += f"{data.strftime('%d/%m/%Y')} - Entrada: {entrada.strftime('%H:%M') if entrada else '---'} | Saída: {saida.strftime('%H:%M') if saida else '---'}\n"
        return resultado


# ---------- CLASSE FUNCIONÁRIO ----------

class Funcionario:
    def __init__(self, nome, cpf, cargo, departamento, data_admissao, salario, horario_trabalho):
        self.nome = nome
        self.cpf = cpf
        self.cargo = cargo
        self.departamento = departamento
        self.data_admissao = self.validar_data(data_admissao)
        self.salario = salario
        self.horario_trabalho = horario_trabalho
        self.ponto = RegistroPonto()

    def validar_data(self, data_str):
        try:
            return datetime.strptime(data_str, "%d/%m/%Y")
        except ValueError:
            raise ValueError("Data de admissão inválida. Use o formato DD/MM/AAAA.")

    def bater_ponto(self, tipo):
        agora = datetime.now()
        data = agora.date()
        hora = agora.time()

        if tipo == "entrada":
            self.ponto.registrar_entrada(data, hora)
        elif tipo == "saida":
            self.ponto.registrar_saida(data, hora)

        self.atualizar_banco_de_horas(data)

    def atualizar_banco_de_horas(self, data):
        jornada = self.horario_trabalho.calcular_jornada_diaria()
        horas_trabalhadas = self.ponto.calcular_horas_trabalhadas(data)
        diferenca = horas_trabalhadas - jornada
        self.horario_trabalho.banco_de_horas += diferenca

    def __str__(self):
        return (f"Nome: {self.nome}\n"
                f"CPF/ID: {self.cpf}\n"
                f"Cargo: {self.cargo}\n"
                f"Departamento: {self.departamento}\n"
                f"Admissão: {self.data_admissao.strftime('%d/%m/%Y')}\n\n"
                f"--- Dados Salariais ---\n{self.salario}\n\n"
                f"--- Horário de Trabalho ---\n{self.horario_trabalho}\n\n"
                f"--- Controle de Ponto ---\n{self.ponto}")


# ---------- FUNÇÕES DE CADASTRO ----------

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

def cadastrar_horario():
    hora_inicio = input("Hora de entrada (HH:MM): ")
    hora_fim = input("Hora de saída (HH:MM): ")
    escala = input("Escala (ex: 6x1, 5x2, noturno): ")
    return HorarioTrabalho(hora_inicio, hora_fim, escala)

def cadastrar_funcionario():
    nome = input("Nome completo: ")
    cpf = input("CPF ou ID interno: ")
    cargo = input("Cargo: ")
    departamento = input("Departamento: ")
    data_admissao = input("Data de admissão (DD/MM/AAAA): ")

    print("\n--- Cadastro Salarial ---")
    salario = cadastrar_salario()

    print("\n--- Horário de Trabalho ---")
    horario = cadastrar_horario()

    return Funcionario(nome, cpf, cargo, departamento, data_admissao, salario, horario)

def exibir_funcionarios(lista):
    for i, f in enumerate(lista):
        print(f"\n--- Funcionário {i+1} ---")
        print(f)


# ---------- MENU PRINCIPAL ----------

def menu():
    funcionarios = []

    while True:
        print("\n=== Sistema de RH ===")
        print("1. Cadastrar funcionário")
        print("2. Listar funcionários")
        print("3. Bater ponto (entrada/saída)")
        print("4. Sair")

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
            if not funcionarios:
                print("Cadastre um funcionário primeiro.")
                continue

            for i, f in enumerate(funcionarios):
                print(f"{i + 1}. {f.nome}")
            idx = int(input("Escolha o número do funcionário: ")) - 1

            if 0 <= idx < len(funcionarios):
                tipo = input("Tipo de ponto (entrada/saida): ").lower()
                funcionarios[idx].bater_ponto(tipo)
                print("Ponto registrado com sucesso!")
            else:
                print("Funcionário inválido.")

        elif opcao == "4":
            print("Encerrando o sistema.")
            break

        else:
            print("Opção inválida.")

# ---------- EXECUTAR SISTEMA ----------
menu()
