import pygame
import time
import random

pygame.init()

# Configuración del juego
width, height = 800, 600
snake_block = 10
snake_speed = 15

# Colores
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Inicialización de la ventana de juego
game_display = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')

# Reloj para controlar la velocidad del juego
clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 25)

# Función para dibujar la serpiente en la pantalla
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(game_display, white, [x[0], x[1], snake_block, snake_block])

# Función para mostrar el puntaje en la pantalla
def Your_score(score):
    value = font.render("Puntaje: " + str(score), True, white)
    game_display.blit(value, [0, 0])

# Función principal del juego
def gameLoop():
    game_over = False
    game_close = False

    # Posición inicial de la serpiente
    x1 = width / 2
    y1 = height / 2

    # Velocidad inicial de la serpiente
    x1_change = 0
    y1_change = 0

    # Longitud inicial de la serpiente
    snake_list = []
    length_of_snake = 1

    # Posición aleatoria de la comida
    foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close == True:
            game_display.fill(black)
            Your_score(length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        # Actualizar la posición de la serpiente
        x1 += x1_change
        y1 += y1_change

        # Comprobar si la serpiente alcanza los bordes de la pantalla
        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True

        # Actualizar la posición de la comida
        game_display.fill(black)
        pygame.draw.rect(game_display, red, [foodx, foody, snake_block, snake_block])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        # Comprobar si la serpiente se come a sí misma
        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        # Dibujar la serpiente en la pantalla
        our_snake(snake_block, snake_list)

        # Mostrar el puntaje en la pantalla
        Your_score(length_of_snake - 1)

        pygame.display.update()

        # Comprobar si la serpiente come la comida
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
            length_of_snake += 1

        # Controlar la velocidad del juego
        clock.tick(snake_speed)

    pygame.quit()
    quit()

# Iniciar el juego
gameLoop()
