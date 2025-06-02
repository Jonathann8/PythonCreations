import flet as ft
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
            return datetime.combine(datetime.today(), saida) - datetime.combine(datetime.today(), entrada)
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


# ---------- INTERFACE GRÁFICA COM FLET ----------

funcionarios = []

def main(page: ft.Page):
    page.title = "Sistema de RH"
    page.scroll = ft.ScrollMode.AUTO

    nome = ft.TextField(label="Nome completo")
    cpf = ft.TextField(label="CPF ou ID interno")
    cargo = ft.TextField(label="Cargo")
    departamento = ft.TextField(label="Departamento")
    data_admissao = ft.TextField(label="Data de admissão (DD/MM/AAAA)")

    salario_base = ft.TextField(label="Salário Base", keyboard_type=ft.KeyboardType.NUMBER)
    beneficio_nome = ft.TextField(label="Nome do Benefício")
    beneficio_valor = ft.TextField(label="Valor do Benefício", keyboard_type=ft.KeyboardType.NUMBER)

    desconto_nome = ft.TextField(label="Nome do Desconto")
    desconto_valor = ft.TextField(label="Valor do Desconto", keyboard_type=ft.KeyboardType.NUMBER)

    entrada = ft.TextField(label="Horário de Entrada (HH:MM)")
    saida = ft.TextField(label="Horário de Saída (HH:MM)")
    escala = ft.TextField(label="Escala (ex: 6x1, 5x2)")

    resultado = ft.Text()

    beneficios = {}
    descontos = {}

    def adicionar_beneficio(e):
        if beneficio_nome.value and beneficio_valor.value:
            beneficios[beneficio_nome.value] = float(beneficio_valor.value)
            resultado.value = f"Benefício '{beneficio_nome.value}' adicionado."
            page.update()

    def adicionar_desconto(e):
        if desconto_nome.value and desconto_valor.value:
            descontos[desconto_nome.value] = float(desconto_valor.value)
            resultado.value = f"Desconto '{desconto_nome.value}' adicionado."
            page.update()

    def cadastrar_funcionario(e):
        try:
            salario = Salario(float(salario_base.value), beneficios, descontos)
            horario = HorarioTrabalho(entrada.value, saida.value, escala.value)
            f = Funcionario(nome.value, cpf.value, cargo.value, departamento.value, data_admissao.value, salario, horario)
            funcionarios.append(f)
            resultado.value = f"Funcionário {nome.value} cadastrado com sucesso!"
        except Exception as ex:
            resultado.value = f"Erro: {str(ex)}"
        page.update()

    def listar_funcionarios(e):
        resultado.value = "\n\n".join(str(f) for f in funcionarios)
        page.update()

    page.add(
        ft.Column([
            nome, cpf, cargo, departamento, data_admissao,
            salario_base,
            beneficio_nome, beneficio_valor, ft.ElevatedButton("Adicionar Benefício", on_click=adicionar_beneficio),
            desconto_nome, desconto_valor, ft.ElevatedButton("Adicionar Desconto", on_click=adicionar_desconto),
            entrada, saida, escala,
            ft.Row([
                ft.ElevatedButton("Cadastrar Funcionário", on_click=cadastrar_funcionario),
                ft.ElevatedButton("Listar Funcionários", on_click=listar_funcionarios)
            ]),
            resultado
        ])
    )

ft.app(target=main)
