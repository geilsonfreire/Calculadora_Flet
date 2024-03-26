import flet as ft # Importando a biblioteca Flet
from flet import (
    Column,
    Container,
    ElevatedButton,
    Page,
    Row,
    Text,
    UserControl,
    border_radius,
    colors,
    alignment,
) # Importando os widgets necessários]

Botoes = (
    {"operador": "AC", "fonte": colors.BLACK, "fundo": "#A9A9A9"},
    {"operador": "⌫", "fonte": colors.BLACK, "fundo": "#A9A9A9"},
    {"operador": "%", "fonte": colors.BLACK, "fundo": "#A9A9A9"},
    {"operador": "/", "fonte": colors.BLACK, "fundo": colors.DEEP_ORANGE},
    {"operador": "7", "fonte": colors.WHITE, "fundo": "#1C1C1C"},
    {"operador": "8", "fonte": colors.WHITE, "fundo": "#1C1C1C"},
    {"operador": "9", "fonte": colors.WHITE, "fundo": "#1C1C1C"},
    {"operador": "*", "fonte": colors.BLACK, "fundo": colors.DEEP_ORANGE},
    {"operador": "4", "fonte": colors.WHITE, "fundo": "#1C1C1C"},
    {"operador": "5", "fonte": colors.WHITE, "fundo": "#1C1C1C"},
    {"operador": "6", "fonte": colors.WHITE, "fundo": "#1C1C1C"},
    {"operador": "-", "fonte": colors.BLACK, "fundo": colors.DEEP_ORANGE},
    {"operador": "1", "fonte": colors.WHITE, "fundo": "#1C1C1C"},
    {"operador": "2", "fonte": colors.WHITE, "fundo": "#1C1C1C"},
    {"operador": "3", "fonte": colors.WHITE, "fundo": "#1C1C1C"},
    {"operador": "+", "fonte": colors.BLACK, "fundo": colors.DEEP_ORANGE},
    {"operador": "0", "fonte": colors.WHITE, "fundo": "#1C1C1C"},
    {"operador": ",", "fonte": colors.WHITE, "fundo": "#1C1C1C"},
    {"operador": "=", "fonte": colors.BLACK, "fundo": colors.LIGHT_GREEN_ACCENT_700},
) # Lista de botões da calculadora (dERFININDOS OS BOTÕES DA CALCULADORA E SUAS CORES)

def main(page: ft.Page): # Função principal (Definindo a interface)
    page.title = "Calculadora" # Título da página
    page.bgcolor = "#000" # Cor de fundo da página
    page.window_resizable = False # Desabilitando a redimensionamento da janela
    page.window_width = 350 # Largura da janela
    page.window_height = 520 # Altura da janela
    page.window_position = "center" # Posição da janela
    page.window_always_on_top = True # Mantendo a janela sempre no topo
    
    
    result = ft.Text(value = "0", color = "#ffffff", size = 40) # input display da calculadora
    
    result_displayed = False  # Variável para rastrear se o resultado foi exibido

    def calculate(valor_atual): # Função para calcular as operações
        try:
            value = eval(valor_atual)  # Calculando as operações
        except ZeroDivisionError: # Tratando exceções
            value = "Erro" # Retornando erro caso ocorra
        except Exception as e: # Tratando exceções
            value = f"Erro: {str(e)}" # Retornando erro caso ocorra

        nonlocal result_displayed # Definindo a variável como global
        result_displayed = True  # Atualizando a variável para True
        return value # Retornando o valor calculado


    def select(e): # Função para selecionar os botões
        nonlocal result_displayed # Definindo a variável como global
        valor_atual = result.value if result.value != "0" else "" # Valor atual do display com validação
        value = e.control.content.value # Valor do botão selecionado

        if value.isdigit(): # Verificando se o valor é um número
            if result_displayed:  # Se o resultado foi exibido, limpe o display
                valor_atual = ""
                result_displayed = False  # Atualizando a variável para False
            valor_atual = valor_atual + value  # Concatenando o valor atual com o valor do botão
        elif value == "AC": # Verificando se o valor é "AC"
            valor_atual = "0" # Atualizando o valor para 0
        elif value == "⌫": # Verificando se o valor é "⌫"
            valor_atual = valor_atual[:-1] # Removendo o último caracterer
            if not valor_atual: # Verificando se valor_atual está vazio
                valor_atual = "0" # Definindo valor_atual como "0"
        else:
            if valor_atual and valor_atual[-1] in ["/", "*", "-", "+", ","]: # Verificando se o último valor é um operador
                valor_atual = valor_atual[:-1] # Removendo o último valor

            valor_atual = valor_atual + value # Concatenando o valor atual com o valor do botão

            if valor_atual[-1] in ["=", "%"]: # Verificando se o último valor é um operador
                valor_atual = str(calculate(valor_atual[:-1])) # Chamando a função para calcular as operações

        result.value = valor_atual # Atualizando o valor do display
        result.update() # Atualizando o display

    dislay = ft.Row(
        controls = [result], 
        width = 390,
        alignment = "end",
    ) # Display da calculadora

    btn = [ft.Container(
        content=ft.Text(
            value=btn["operador"],
            color=btn["fonte"], 
            size = 20,  
            expand = 1
        ), # Texto do botão
        width = 148 if btn["operador"] in ["="] else 74,
        height = 70,
        bgcolor = btn["fundo"],
        border_radius = 25, 
        alignment = ft.alignment.center,
        on_click = select,
    ) for btn in Botoes] # replicando os Botões da calculadora

    keyboard = ft.Row(
        controls = btn,
        width = 390,
        wrap = True,
        alignment = "center",
        spacing = 5
    ) # Teclado da calculadora
    

    page.add(dislay, keyboard) # Adicionando o display e o teclado na página
ft.app(target = main) # Iniciando a aplicação  