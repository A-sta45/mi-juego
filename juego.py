import pygame
import random
import time


# Iniciamos Pygame
pygame.init()
reloj = pygame.time.Clock()

# Definimos algunas constantes
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# ventana del juego
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Escape de la Masmorra")

ENEMY_WIDTH = 50
ENEMY_HEIGHT = 50
FPS = 20
vida = 3
puntaje = 0
nivel = 1
velocidad_enemigos = 1


# Cargar las imágenes de los personajes
jugador = pygame.Surface((50, 50))
jugador.fill((255, 255, 255))
enemigo1 = pygame.Surface((50, 50))
enemigo1.fill((0, 0, 0))
pygame.draw.polygon(enemigo1, (255, 0, 0), [(0, 0), (25, 50), (50, 0)])
enemigo2 = pygame.Surface((50, 50))
enemigo2.fill((0, 0, 0))
pygame.draw.polygon(enemigo2, (255, 0, 0), [(0, 0), (25, 50), (50, 0)])
enemigo3 = pygame.Surface((50, 50))
enemigo3.fill((0, 0, 0))
pygame.draw.polygon(enemigo3, (255, 0, 0), [(0, 0), (25, 50), (50, 0)])

# Definir la posición inicial del jugador y los enemigos
posicion_jugador_x = SCREEN_WIDTH / 2
posicion_jugador_y = SCREEN_HEIGHT - 50
posicion_enemigo_x = random.randint(0, SCREEN_WIDTH - ENEMY_WIDTH)
posicion_enemigo_y = random.randint(0, SCREEN_HEIGHT - ENEMY_HEIGHT)

# Definir el tiempo en segundos que queremos que pase antes de que aparezcan los enemigos
TIEMPO_ENTRE_OLEADAS = 30

# Definir la última vez que aparecieron los enemigos
ultima_oleada = time.time()

# Definir la velocidad de movimiento del jugador
velocidad_jugador = 5

# Definir la velocidad de movimiento de los enemigos
velocidad_enemigo1 = 1
velocidad_enemigo2 = 1
velocidad_enemigo3 = 1

enemigos = [enemigo1, enemigo2, enemigo3]


def dibujar_personajes():
    # Dibujar el jugador y los enemigos en la pantalla
    screen.blit(jugador, (posicion_jugador_x, posicion_jugador_y))
    screen.blit(enemigo1, (posicion_enemigo_x, posicion_enemigo_y))
    screen.blit(enemigo2, (posicion_enemigo_x, posicion_enemigo_y - 100))
    screen.blit(enemigo3, (posicion_enemigo_x, posicion_enemigo_y + 100))


def mover_enemigos():
    global vida, puntaje, posicion_enemigo_y, posicion_enemigo_x, nivel, velocidad_enemigos
    # Mover cada uno de los enemigos hacia abajo
    posicion_enemigo_y += velocidad_enemigos
    # Si el enemigo llega al final de la pantalla, restar una vida y reiniciar su posición
    if posicion_enemigo_y > SCREEN_HEIGHT:
        posicion_enemigo_x = random.randint(0, SCREEN_WIDTH - ENEMY_WIDTH)
        posicion_enemigo_y = 0
    # Detectar colisiones entre el jugador y los enemigos
    if posicion_jugador_x < posicion_enemigo_x + ENEMY_WIDTH and \
            posicion_jugador_x + ENEMY_WIDTH > posicion_enemigo_x and \
            posicion_jugador_y < posicion_enemigo_y + ENEMY_HEIGHT and \
            posicion_jugador_y + ENEMY_HEIGHT > posicion_enemigo_y:
        # Si hay una colisión, restar una vida
        vida -= 1
        vida.pop()

    # Si el puntaje es un múltiplo de 100, aumentar el nivel y la velocidad de los enemigos
    if puntaje % 100 == 0:
        nivel += 1
        velocidad_enemigos += 1

# Definir la función principal del juego


def jugar():
    global posicion_jugador_x, posicion_jugador_y, vida, puntaje, nivel, velocidad_enemigos, ultima_oleada

    # Ciclo principal del juego
    while True:
        # Manejar eventos de entrada del usuario
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            posicion_jugador_x -= velocidad_jugador
        if keys[pygame.K_RIGHT]:
            posicion_jugador_x += velocidad_jugador
        if keys[pygame.K_UP]:
            posicion_jugador_y -= velocidad_jugador
        if keys[pygame.K_DOWN]:
            posicion_jugador_y += velocidad_jugador

        # Dibujar los personajes en la pantalla
        screen.fill((0, 0, 0))
        dibujar_personajes()
        mover_enemigos()

        # Generar nuevas oleadas de enemigos cada cierto tiempo
        if time.time() - ultima_oleada > TIEMPO_ENTRE_OLEADAS:
            ultima_oleada = time.time()
            posicion_enemigo_x = random.randint(0, SCREEN_WIDTH - ENEMY_WIDTH)
            posicion_enemigo_y = 10

        # Dibujar la información del juego en la pantalla
        fuente = pygame.font.SysFont("arial", 20)
        texto_vida = fuente.render("Vida: " + str(vida), True, (255, 255, 255))
        texto_puntaje = fuente.render(
            "Puntaje: " + str(puntaje), True, (255, 255, 255))
        texto_nivel = fuente.render(
            "Nivel: " + str(nivel), True, (255, 255, 255))
        screen.blit(texto_vida, (10, 10))
        screen.blit(texto_puntaje, (SCREEN_WIDTH -
                    texto_puntaje.get_width() - 10, 10))
        screen.blit(
            texto_nivel, ((SCREEN_WIDTH - texto_nivel.get_width()) // 2, 10))

        # Actualizar la pantalla
        pygame.display.flip()
        reloj.tick(FPS)

        if vida == 0:
            print("GAME OVER")
            pygame.quit()
            quit()


jugar()
