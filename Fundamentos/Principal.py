
import pygame
import socket
import random
import time

# Configuración inicial de Pygame
pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Marcadores')

# Colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Fuentes
font = pygame.font.Font(None, 74)

# Inicialización de marcadores
marcador1 = 0
marcador2 = 0


# Función para conectar y enviar datos a la Raspberry Pi
def send_data(marcador1, marcador2):
    data = f"{marcador1},{marcador2}"
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('192.168.137.111', 1234))
    s.send(data.encode())
    s.close()


# Función para procesar la lógica de los botones
def process_button(marcador):
    probability = random.randint(1, 100)
    if probability <= 25:  # 25% de aumentar
        marcador = (marcador + 1) % 8
    elif probability <= 50:  # 25% de no cambiar
        pass
    else:  # 50% de restar 3
        marcador = (marcador - 3) % 8
    return marcador


# Bucle principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if 50 <= x <= 150 and 200 <= y <= 250:
                marcador1 = process_button(marcador1)
                send_data(marcador1, marcador2)
            elif 250 <= x <= 350 and 200 <= y <= 250:
                marcador2 = process_button(marcador2)
                send_data(marcador1, marcador2)

    # Dibujar en la pantalla
    screen.fill(WHITE)
    text1 = font.render(str(marcador1), True, BLACK)
    text2 = font.render(str(marcador2), True, BLACK)
    screen.blit(text1, (75, 50))
    screen.blit(text2, (275, 50))

    pygame.draw.rect(screen, BLACK, (50, 200, 100, 50))
    pygame.draw.rect(screen, BLACK, (250, 200, 100, 50))

    pygame.display.flip()
    time.sleep(0.1)

pygame.quit()