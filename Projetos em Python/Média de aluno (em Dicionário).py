import pygame
import time
import unidecode

# Inicializa o Pygame
pygame.init()

# Define as cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE
# Configura a janela
size = (600, 400)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Sistema de Avaliação de Alunos")

# Configura a fonte
font = pygame.font.Font(None, 36)

# Função para exibir texto na tela
def draw_text(text, color, x, y):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

# Função para obter entrada do usuário
def get_input(prompt):
    user_input = ""
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return None
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return user_input
                elif event.key == pygame.K_BACKSPACE:
                    user_input = user_input[:-1]
                else:
                    user_input += event.unicode
        screen.fill(WHITE)
        draw_text(prompt, BLACK, 20, 50)
        draw_text(user_input, BLACK, 20, 100)
        pygame.display.flip()

# Função principal
def main():
    running = True
    while running:
        aluno = {}
        aluno['nome'] = get_input('Nome: ')
        if aluno['nome'] is None:
            break
        aluno['média'] = float(get_input(f'Média de {aluno["nome"]}: '))
        if aluno['média'] is None:
            break

        screen.fill(WHITE)
        draw_text('Computando média...', BLUE, 20, 150)
        pygame.display.flip()
        time.sleep(1.2)

        if aluno['média'] >= 7:
            aluno['situação'] = 'Aprovado'
            situation_color = GREEN
        elif 5 <= aluno['média'] < 7:
            aluno['situação'] = 'Recuperação'
            situation_color = YELLOW
        else:
            aluno['situação'] = 'Reprovado'
            situation_color = RED

        screen.fill(WHITE)
        draw_text("Relatório do Aluno:", CYAN, 20, 50)
        draw_text(f"Nome: {aluno['nome']}", BLACK, 20, 100)
        draw_text(f"Média: {aluno['média']}", BLACK, 20, 150)
        draw_text(f"Situação: {aluno['situação']}", situation_color, 20, 200)
        pygame.display.flip()

        # Espera antes de perguntar se deseja continuar
        time.sleep(2)

        # Pergunta ao usuário se deseja continuar
        continue_prompt = get_input('Deseja continuar? (sim/nao): ')
        if continue_prompt is None or unidecode.unidecode(continue_prompt.lower())[0] == 'n':
            running = False

    pygame.quit()

if __name__ == "__main__":
    main()
