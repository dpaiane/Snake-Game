# Configurações iniciais
import pygame, sys
from pygame.locals import *
import random
# inicializacao
pygame.init()   
pygame.display.set_caption("Jogo Snake Python")
largura, altura = 800, 600
tela = pygame.display.set_mode((largura, altura))
relogio = pygame.time.Clock()

# Cores
cor_placar = (255,255,255)
cor_maca = (255,0,0)
cor_cobra = (103,53,0)

# parametros gerais
tamanho_quadrado = 20
velocidade_jogo = 10

#parametros de som
pygame.mixer.music.set_volume(0.5)
musica_fundo = pygame.mixer.music.load("sound\coin.wav")

def gerar_comida():
    # gera a posicao da comida
    comida_x = round(random.randrange(0, largura - tamanho_quadrado) / float(tamanho_quadrado)) * float(tamanho_quadrado)
    comida_y = round(random.randrange(0, altura - tamanho_quadrado) / float(tamanho_quadrado)) * float(tamanho_quadrado)
    return comida_x, comida_y

def desenhar_comida(tamanho, comida_x, comida_y):
    # coloca a comida na tela
    image_comida = pygame.image.load('img\Apple.webp')
    image_comida = pygame.transform.scale(image_comida, (tamanho, tamanho))
    tela.blit(image_comida, (comida_x, comida_y))

def desenhar_cobra(tamanho, pixels):
    # coloca a cobra na tela
    for pixel in pixels:
        pygame.draw.rect(tela, cor_cobra, [pixel[0], pixel[1], tamanho, tamanho])

        #image_cobra = pygame.image.load('img\Snake.png')
        #image_cobra = pygame.transform.scale(image_cobra, (tamanho, tamanho))
        #tela.blit(image_cobra, (pixel[0],pixel[1]))

def desenhar_pontuacao(pontuacao):
    # placar
    fonte = pygame.font.SysFont("Helvetica", 30)
    texto = fonte.render(f"Pontos: {pontuacao}", True, cor_placar)
    tela.blit(texto, [1,1])

def selecionar_direcao(tecla):
    # inputs
    if tecla == pygame.K_DOWN:
        velocidade_x = 0
        velocidade_y = tamanho_quadrado
    elif tecla == pygame.K_UP:
        velocidade_x = 0
        velocidade_y = -tamanho_quadrado
    elif tecla == pygame.K_RIGHT:
        velocidade_x = tamanho_quadrado
        velocidade_y = 0
    elif tecla == pygame.K_LEFT:
        velocidade_x = -tamanho_quadrado
        velocidade_y = 0
    return velocidade_x, velocidade_y

def rodar_jogo():
    fim_jogo = False
    flag = False

    x = largura/2
    y = altura/2

    velocidade_x = 0
    velocidade_y = 0

    tamanho_cobra = 1
    pixels = []
    comida_x, comida_y = gerar_comida()
    # Enquanto não é o fim do jogo
    while not fim_jogo: 
        # tratamento da imagem de fundo
        image_fundo = pygame.image.load('img\gramado.png')
        image_fundo = pygame.transform.scale(image_fundo, (largura, altura))
        tela.blit(image_fundo, (0, 0))
        # captura do evento do teclado 
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fim_jogo = True
                exit()
            elif evento.type ==  pygame.KEYDOWN:
                velocidade_x, velocidade_y = selecionar_direcao(evento.key)
                flag = True
        if flag == True:
            desenhar_comida(tamanho_quadrado, comida_x, comida_y)
        # colisao na tela
        if x < 0 or x >= largura or y < 0 or y >= altura:
            fonte = pygame.font.SysFont("Helvetica", 80)
            texto = fonte.render(f"GAME OVER", True, cor_maca)
            tela.blit(texto, [180,200])
            fim_jogo = True
            pygame.display.update()
            pygame.time.wait(3000)

        x += velocidade_x
        y += velocidade_y
        pixels.append([x,y])
        if len(pixels) > tamanho_cobra:
            del pixels[0]
        
        # colisao no corpo 
        for pixel in pixels[:-1]:
            if pixel == [x,y]:
                fonte = pygame.font.SysFont("Helvetica", 80)
                texto = fonte.render(f"GAME OVER", True, cor_maca)
                tela.blit(texto, [180,200])
                fim_jogo = True
                pygame.display.update()
                pygame.time.wait(3000)

        desenhar_cobra(tamanho_quadrado, pixels) 
        desenhar_pontuacao(tamanho_cobra - 1)
        pygame.display.update()
        # Criar uma nova comida
        if x == comida_x and y == comida_y:
            tamanho_cobra += 1
            comida_x, comida_y = gerar_comida()
            # pygame.mixer.music.play(-1)
        relogio.tick(velocidade_jogo)
rodar_jogo()