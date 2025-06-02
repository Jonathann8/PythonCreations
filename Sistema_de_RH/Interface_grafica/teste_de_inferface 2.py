import flet as ft
from datetime import datetime, timedelta, time

# ---------- SISTEMA RH ----------
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
        self.registros = {}

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
        self.data_admissao = datetime.strptime(data_admissao, "%d/%m/%Y")
        self.salario = salario
        self.horario_trabalho = horario_trabalho
        self.ponto = RegistroPonto()

    def __str__(self):
        return (f"Nome: {self.nome}\nCPF: {self.cpf}\nCargo: {self.cargo}\nDepartamento: {self.departamento}\n"
                f"Admissão: {self.data_admissao.strftime('%d/%m/%Y')}\n\n{self.salario}\n\n{self.horario_trabalho}\n\n{self.ponto}")


# ---------- INTERFACE COM FLET ----------
def main(page: ft.Page):
    page.title = "Sistema de RH"
    page.scroll = "auto"

    funcionarios = []

    nome_input = ft.TextField(label="Nome")
    cpf_input = ft.TextField(label="CPF")
    cargo_input = ft.TextField(label="Cargo")
    departamento_input = ft.TextField(label="Departamento")
    data_admissao_input = ft.TextField(label="Data de Admissão (DD/MM/AAAA)")
    salario_input = ft.TextField(label="Salário Base (R$)", keyboard_type=ft.KeyboardType.NUMBER)

    beneficio_nome_input = ft.TextField(label="Nome do Benefício")
    beneficio_valor_input = ft.TextField(label="Valor", keyboard_type=ft.KeyboardType.NUMBER)
    beneficios = {}

    def add_beneficio(e):
        nome = beneficio_nome_input.value
        valor = float(beneficio_valor_input.value)
        beneficios[nome] = valor
        beneficio_nome_input.value = ""
        beneficio_valor_input.value = ""
        page.update()

    desconto_nome_input = ft.TextField(label="Nome do Desconto")
    desconto_valor_input = ft.TextField(label="Valor", keyboard_type=ft.KeyboardType.NUMBER)
    descontos = {}

    def add_desconto(e):
        nome = desconto_nome_input.value
        valor = float(desconto_valor_input.value)
        descontos[nome] = valor
        desconto_nome_input.value = ""
        desconto_valor_input.value = ""
        page.update()

    hora_inicio_input = ft.TextField(label="Hora Início (HH:MM)")
    hora_fim_input = ft.TextField(label="Hora Fim (HH:MM)")
    escala_input = ft.TextField(label="Escala (ex: 6x1, 5x2)")

    funcionario_list = ft.Column(scroll="auto")

    def cadastrar_funcionario(e):
        salario = Salario(float(salario_input.value), beneficios.copy(), descontos.copy())
        horario = HorarioTrabalho(hora_inicio_input.value, hora_fim_input.value, escala_input.value)
        funcionario = Funcionario(
            nome_input.value, cpf_input.value, cargo_input.value,
            departamento_input.value, data_admissao_input.value,
            salario, horario
        )
        funcionarios.append(funcionario)

        funcionario_card = ft.Card(
            content=ft.Container(
                content=ft.Column([
                    ft.Text(funcionario.nome, weight="bold"),
                    ft.Text(str(funcionario)),
                    ft.TextButton("Remover", on_click=lambda _: remover_funcionario(funcionario, funcionario_card))
                ]),
                padding=10,
            )
        )
        funcionario_list.controls.append(funcionario_card)
        page.update()

    def remover_funcionario(funcionario, card):
        funcionarios.remove(funcionario)
        funcionario_list.controls.remove(card)
        page.update()

    form_column = ft.Column(
        [
            ft.Text("Cadastro de Funcionário", size=24, weight="bold"),

            nome_input,
            cpf_input,
            cargo_input,
            departamento_input,
            data_admissao_input,
            salario_input,

            ft.Text("Benefícios"),
            beneficio_nome_input,
            beneficio_valor_input,
            ft.ElevatedButton("Adicionar Benefício", on_click=add_beneficio),

            ft.Text("Descontos"),
            desconto_nome_input,
            desconto_valor_input,
            ft.ElevatedButton("Adicionar Desconto", on_click=add_desconto),

            ft.Text("Horário de Trabalho"),
            hora_inicio_input,
            hora_fim_input,
            escala_input,

            ft.ElevatedButton("Cadastrar Funcionário", on_click=cadastrar_funcionario),
            ft.Divider(),
            funcionario_list
        ],
        scroll="auto",
        expand=True
    )

    page.add(form_column)

ft.app(target=main)
