import pygame
import sys, random
from pygame.locals import *

FPS = 23
TAMANHO_DA_TELA = (1200,800)

pygame.init()
DISPLAY = pygame.display.set_mode(TAMANHO_DA_TELA)
fpsClock = pygame.time.Clock()
rodando = True
retangulo = pygame.Rect(20,20,40,40)
andar_esquerda = False
andar_direita = False
andar_baixo = False
andar_cima = False
abrir_menu = False
tabuleiro_plataforma = []
itens = []
y=21
while y<TAMANHO_DA_TELA[1]-20:
    x=21
    while x<TAMANHO_DA_TELA[0]-20:
        tabuleiro_plataforma.append(pygame.Rect(x,y,38,38))
        x+=40
    y+=40

while rodando:
    if andar_esquerda and retangulo.x>20:
        retangulo.x -= 40
    if andar_direita and retangulo.x<TAMANHO_DA_TELA[0]-60:
        retangulo.x += 40
    if andar_baixo and retangulo.y<TAMANHO_DA_TELA[1]-60:
        retangulo.y += 40
    if andar_cima and retangulo.y>20:
        retangulo.y -= 40
    if abrir_menu:
        itens.append((pygame.Rect(retangulo.x+1,retangulo.y+1,38,38),(random.randrange(256),random.randrange(256),random.randrange(256))))
    for event in pygame.event.get():
        if event.type == QUIT:
            rodando = False
        if event.type == KEYDOWN:
            if event.key == K_LEFT or event.key == K_a:
                andar_esquerda = True
        if event.type == KEYUP:
            if event.key == K_LEFT or event.key == K_a:
                andar_esquerda = False

            
        if event.type == KEYUP:
            if event.key == K_RIGHT or event.key == K_d:
                andar_direita = False
        if event.type == KEYDOWN:
            if event.key == K_RIGHT or event.key == K_d:
                andar_direita = True

            
        if event.type == KEYUP:
            if event.key == K_UP or event.key == K_w:
                andar_cima = False
        if event.type == KEYDOWN:
            if event.key == K_UP or event.key == K_w:
                andar_cima = True
        if event.type == KEYUP:
            if event.key == K_DOWN or event.key == K_s:
                andar_baixo = False
        if event.type == KEYDOWN:
            if event.key == K_DOWN or event.key == K_s:
                andar_baixo = True
        if event.type == KEYUP:
            if event.key == K_RETURN or event.key == K_SPACE:
                abrir_menu = False
        if event.type == KEYDOWN:
            if event.key == K_RETURN or event.key == K_SPACE:
                abrir_menu = True
    DISPLAY.fill((0,0,0))
    for i in tabuleiro_plataforma:
        DISPLAY.fill((255,255,255),i)
    for i in itens:
        DISPLAY.fill(i[1],i[0])
    DISPLAY.fill((random.randrange(256),random.randrange(256),random.randrange(256)),retangulo)
    pygame.display.update()
    fpsClock.tick(FPS)

pygame.quit()
sys.exit()
