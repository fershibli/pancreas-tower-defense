# -*- coding: cp1252 -*-
import pygame
import sys, random,time
from pygame.locals import *

FPS = 10
TAMANHO_DA_TELA = (800,600)

pygame.init()
DISPLAY = pygame.display.set_mode(TAMANHO_DA_TELA)
fpsClock = pygame.time.Clock()
rodando = True
retangulo = pygame.Rect(0,0,40,40)
quadrado = pygame.Rect(305,255,50,50)
andar_esquerda = False
andar_direita = False
andar_baixo = False
andar_cima = False
abrir_menu = False
confirmar_compra = False
aviso_texto = ''
vida_pancreas=1000
atp_grana=200
tabuleiro_plataforma = []
itens = []
posicao_compra=1
caminho_tortuoso=[[True,False,False,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True],[True,False,False,True,True,False,False,False,False,False,False,True,True,False,False,False,False,False,False,True],[True,False,False,True,True,False,False,False,False,False,False,True,True,False,False,False,False,False,False,True],[True,False,False,True,True,False,False,True,True,False,False,True,True,False,False,True,True,False,False,True],[True,False,False,True,True,False,False,True,True,False,False,True,True,False,False,True,True,False,False,True],[True,False,False,True,True,False,False,True,True,False,False,True,True,False,False,True,True,False,False,True],[True,False,False,True,True,False,False,True,True,False,False,True,True,False,False,True,True,False,False,True],[True,False,False,True,True,False,False,True,True,False,False,True,True,False,False,True,True,False,False,True],[True,False,False,True,True,False,False,True,True,False,False,True,True,False,False,True,True,False,False,True],[True,False,False,True,True,False,False,True,True,False,False,True,True,False,False,True,True,False,False,True],[True,False,False,True,True,False,False,True,True,False,False,True,True,False,False,True,True,False,False,True],
                  [True,False,False,False,False,False,False,True,True,False,False,True,True,False,False,True,True,False,False,True],
                  [True,False,False,False,False,False,False,True,True,False,False,False,False,False,False,True,True,False,False,True],
                  [True,True,True,True,True,True,True,True,True,False,False,False,False,False,False,True,True,False,False,True],
                  [False,False,False,False,False,False,False,False,True,True,True,True,True,True,True,True,True,False,False,True]]
y=1
while y<600:
    x=1
    while x<800:
        if x==41 and y!=561 and y!=521 or x==81 and y!=561 and y!=521 or x==201 and y!=561 and y!=521 and y!=1 or x==241 and y!=561 and y!=521 and y!=1 or x==361 and y!=561 and y!=1 or x==401 and y!=561 and y!=1 or x==561 and y!=561 and y!=1 or x==521 and y!=561 and y!=1 or y!=1 and x==721 or y!=1 and x==681 or y==441 and x==121 or y==481 and x==121 or y==481 and x==161 or y==441 and x==161 or y==521 and x==441 or y==481 and x==441 or y==481 and x==481 or y==521 and x==481 or y==41 and x==321 or y==81 and x==321 or y==81 and x==281 or y==41 and x==281 or y==81 and x==641 or y==81 and x==601 or y==41 and x==601 or y==41 and x==641:
            tabuleiro_plataforma.append((pygame.Rect(x,y,38,38),(255,100,100)))
        elif y==40*14+1 and x<8*40:
            tabuleiro_plataforma.append((pygame.Rect(x,y,40,38),(200,200,255)))
        else:
            tabuleiro_plataforma.append((pygame.Rect(x,y,38,38),(200,25,25)))
        x+=40
    y+=40

class anatelDefense(object):#torre celular de defesa huehuehuehe
    def __init__(self,opcao):
        global retangulo,caminho_tortuoso
        if opcao==1:
            self.ataque=1
            self.x=retangulo.x
            self.y=retangulo.y
            self.alcance=2
            caminho_tortuoso[int(retangulo.y/40)][int(retangulo.x/40)]='torre 1'
            self.quadrado=pygame.Rect(int(retangulo.x+1),int(retangulo.y+1),38,38)
            self.imagem=pygame.image.load("torre1.jpg")
            self.posicao=(int(retangulo.x+1),int(retangulo.y+1))
            self.cor=(0,0,0)
        if opcao==2:
            self.ataque=2
            self.x=retangulo.x
            self.y=retangulo.y
            self.alcance=3
            caminho_tortuoso[int(retangulo.y/40)][int(retangulo.x/40)]='torre 1'
            self.quadrado=pygame.Rect(int(retangulo.x+1),int(retangulo.y+1),38,38)
            self.imagem=pygame.image.load("torre2.jpg")
            self.posicao=(int(retangulo.x+1),int(retangulo.y+1))
            self.cor=(0,0,0)
        if opcao==3:
            self.ataque=3
            self.x=retangulo.x
            self.y=retangulo.y
            self.alcance=4
            caminho_tortuoso[int(retangulo.y/40)][int(retangulo.x/40)]='torre 1'
            self.quadrado=pygame.Rect(int(retangulo.x+1),int(retangulo.y+1),38,38)
            self.imagem=pygame.image.load("torre3.jpg")
            self.posicao=(int(retangulo.x+1),int(retangulo.y+1))
            self.cor=(0,0,0)
class diabetesPudim(object):
    def __init__(self,ataque,defesa,vida,velocidade,tamanho,cores,ordem=0):
        self.vida_atual=vida
        self.vida_total=vida
        self.defesa=defesa
        self.ataque=ataque
        self.padrao=(random.randrange(2)+1)
        self.quadrado=pygame.Rect((40*self.padrao+int((40-tamanho)/2)),ordem*(-1),tamanho,tamanho)
        self.velocidade=velocidade+random.randrange(5)
        self.movimento=0
        self.cor=cores
        self.desce=True
        self.direita=False
DISPLAY.fill((255,200,0))
pygame.display.set_caption('PANCREAS - TOWER DEFENSE (by:Pudim Games)')
pygame.mouse.set_visible(0)
DISPLAY.blit(pygame.font.SysFont("arial", 32).render("PÂNCREAS - TOWER DEFENSE",True,(0,0,0)),(200,200))
DISPLAY.blit(pygame.font.SysFont("arial", 32).render("by: Pudim Games",True,(0,0,0)),(300,232))
DISPLAY.blit(pygame.font.SysFont("arial", 32).render(" Defenda o seu pâncreas!",True,(0,0,0)),(250,264))
pygame.display.update()
time.sleep(2)
pancreas=[]
exercito=[]
v=0
d=0
while rodando:
    if vida_pancreas<100:
        for event in pygame.event.get():
            if event.type == QUIT:
                rodando = False
            if event.type== KEYUP and event.key == K_ESCAPE:
                rodando = False
        DISPLAY.fill((random.randrange(156)+100,0,0))
        DISPLAY.blit(pygame.font.SysFont("arial", 32).render("SEU FIGADO JÁ ERA!",True,(0,0,0)),(260,280))
        pygame.display.set_caption('PANCREAS - TOWER DEFENSE (by:Pudim Games)')
        pygame.mouse.set_visible(0)
        pygame.display.update()
        fpsClock.tick(int(FPS/2))
    else:
        if abrir_menu:
            for event in pygame.event.get():
                if andar_direita and quadrado.x<445:
                    quadrado.x+=70
                    posicao_compra+=1
                if andar_esquerda and quadrado.x>305:
                    quadrado.x-=70
                    posicao_compra-=1
                if confirmar_compra:
                    if caminho_tortuoso[int(retangulo.y/40)][int(retangulo.x/40)]==True:
                        if posicao_compra==1 and atp_grana>=50: 
                            pancreas.append(anatelDefense(1))
                            atp_grana-=50
                            aviso_texto= 'Criada a Torre tipo 1 por 50 ATP!'
                        elif posicao_compra==2 and atp_grana>=200:
                            pancreas.append(anatelDefense(2))
                            atp_grana-=200
                            aviso_texto= 'Criada a Torre tipo 2 por 200 ATP!'
                        elif posicao_compra==3 and atp_grana>=500:
                            pancreas.append(anatelDefense(3))
                            atp_grana-=500
                            aviso_texto= 'Criada a Torre tipo 3 por 500 ATP!'
                        else:
                            aviso_texto= 'Seu figado não tem ATP o suficiente!'
                    else:
                        aviso_texto= 'Aqui não dá para colocar a Torre!'
                if event.type== KEYUP and event.key == K_ESCAPE:
                    aviso_texto = ''
                    abrir_menu = False
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
                    if event.key == K_RETURN or event.key == K_SPACE:
                        confirmar_compra = False
                if event.type == KEYDOWN:
                    if event.key == K_RETURN or event.key == K_SPACE:
                        confirmar_compra = True
        else:
            if d==5:
                if v>100 and v<=200: exercito.append(diabetesPudim(5,0.1,50,8,5,(50,200,100)))
                elif v>150 and v<=300: exercito.append(diabetesPudim(6,0.2,100,5,10,(0,220,80)))
                elif v>350 and v<=500: exercito.append(diabetesPudim(7,0.3,150,4,13,(0,10,100)))
                elif v>550 and v<=800: exercito.append(diabetesPudim(8,0.4,200,3,20,(0,0,250)))
                elif v>850 and v<=1000: exercito.append(diabetesPudim(15,0.5,300,2,25,(100,10,100)))
                elif v>1100 and v<=1600: exercito.append(diabetesPudim(25,0.7,400,1,30,(200,10,200)))
                elif v>1700 and v<=1900: exercito.append(diabetesPudim(1,0.8,300,10,2,(140,120,0)))
                elif v>2000 and v<=2200: exercito.append(diabetesPudim(1,0.9,300,8,3,(140,120,0)))
                elif v>2300 and v<=2500: exercito.append(diabetesPudim(1,0.99,300,6,4,(140,120,0)))
                elif v>2600 and v<=2800: exercito.append(diabetesPudim(2,0.999,300,4,5,(140,120,0)))
                elif v>2900 and v<=3100: exercito.append(diabetesPudim(2,0.9999,300,2,6,(140,120,0)))
                elif v>3200 and v<=3400: exercito.append(diabetesPudim(3,0.99999,300,1,7,(140,120,0)))
                elif v>3600 and v<=4700: exercito.append(diabetesPudim(50,1.2,500,30,20,(255,220,0)))
                elif v>4800 and v<=4900: exercito.append(diabetesPudim(80,1.5,50000,30,25,(255,220,0)))
                elif v>5000 and v<=5100: exercito.append(diabetesPudim(130,1.8,100000,30,30,(255,220,0)))
                elif v==5200: exercito.append(diabetesPudim(500,2,100000,30,40,(255,220,0)))
                d=0
            for proteina in exercito:
                try:
                    for torre in pancreas:
                        if int(proteina.quadrado.y/40)<int(torre.quadrado.y/40)+torre.alcance and int(proteina.quadrado.y/40)>int(torre.quadrado.y/40)-torre.alcance and int(proteina.quadrado.x/40)<int(torre.quadrado.x/40)+torre.alcance and int(proteina.quadrado.x/40)>int(torre.quadrado.x/40)-torre.alcance:
                            if torre.ataque>proteina.defesa: proteina.vida_atual-=torre.ataque+proteina.defesa
                    if proteina.movimento==proteina.velocidade:
                        proteina.movimento=0
                        if proteina.direita==True:
                            if caminho_tortuoso[int(proteina.quadrado.y/40)][int(proteina.quadrado.x/40)+proteina.padrao]==False:
                                proteina.quadrado.x+=40
                            else:
                                proteina.direita=False
                        elif proteina.desce==True:
                            if caminho_tortuoso[int(proteina.quadrado.y/40)+proteina.padrao][int(proteina.quadrado.x/40)]==False:
                                proteina.quadrado.y+=40
                            else:
                                proteina.desce=False
                                proteina.direita=True
                        else:
                            if caminho_tortuoso[int(proteina.quadrado.y/40)-3+proteina.padrao][int(proteina.quadrado.x/40)]==False:
                                proteina.quadrado.y-=40
                            else:
                                proteina.desce=True
                                proteina.direita=True
                    else:
                        proteina.movimento+=1
                    if proteina.vida_atual<=0:
                        atp_grana+=int(proteina.ataque/3+0.5)+random.randrange(int(proteina.ataque/3+0.5))+1
                        proteina.quadrado=[]
                        proteina=''
                    if int(proteina.quadrado.y/40)==15-proteina.padrao and int(proteina.quadrado.x/40)>=17:
                        vida_pancreas-=proteina.ataque
                        proteina.quadrado=[]
                        proteina=''
                except:
                    pass
            if andar_esquerda and retangulo.x>0:
                if caminho_tortuoso[int(retangulo.y/40)][int(retangulo.x/40)-1]==False:
                    if retangulo.x!=8*40 or retangulo.y!=14*40:
                        if caminho_tortuoso[int(retangulo.y/40)][int(retangulo.x/40)-3]==False:
                            retangulo.x -= 280
                        else:
                            retangulo.x -= 120
                else:
                    retangulo.x -= 40
            if andar_direita and retangulo.x<760:
                if caminho_tortuoso[int(retangulo.y/40)][int(retangulo.x/40)+1]==False:
                    if caminho_tortuoso[int(retangulo.y/40)][int(retangulo.x/40)+3]==False:
                        retangulo.x += 280
                    else:
                        retangulo.x += 120
                else:
                    retangulo.x += 40
            if andar_baixo and retangulo.y<560:
                if caminho_tortuoso[int(retangulo.y/40)+1][int(retangulo.x/40)]==False:
                    if retangulo.y!=13*40:            
                        if caminho_tortuoso[int(retangulo.y/40)+3][int(retangulo.x/40)]==False:
                            if retangulo.x!=17*40 and retangulo.x!=18*40 and retangulo.x!=5*40 and retangulo.x!=6*40: retangulo.y += 560
                            elif retangulo.x!=5*40 or retangulo.x!=6*40: retangulo.y += 520
                        else:
                            retangulo.y += 120
                else:
                    retangulo.y += 40
            if andar_cima and retangulo.y>0:
                if caminho_tortuoso[int(retangulo.y/40)-1][int(retangulo.x/40)]==False:
                    if caminho_tortuoso[int(retangulo.y/40)-3][int(retangulo.x/40)]==False:
                        if retangulo.x!=40 and retangulo.x!=80 and retangulo.x!=5*40 and retangulo.x!=6*40: retangulo.y -= 560
                        elif retangulo.x!=5*40 or retangulo.x!=6*40: retangulo.y -= 520
                    else:
                        retangulo.y -= 120
                else:
                    retangulo.y -= 40            
            for event in pygame.event.get():
                if event.type == QUIT:
                    rodando = False
                if event.type== KEYUP and event.key == K_ESCAPE:
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
            DISPLAY.fill(i[1],i[0])
        for i in itens:
            DISPLAY.fill(i[1],i[0])
        for torre in pancreas:
            DISPLAY.blit(torre.imagem,torre.posicao)
#            DISPLAY.fill(torre.cor,torre.quadrado)
        for proteina in exercito:
            try:
                DISPLAY.fill(proteina.cor,proteina.quadrado)
                if proteina.vida_total<1000:
                    DISPLAY.fill((255,255,255),pygame.Rect(proteina.quadrado.x,proteina.quadrado.y+proteina.quadrado.width,int(proteina.vida_total/10),5))
                    DISPLAY.fill((255,0,0),pygame.Rect(proteina.quadrado.x+1,proteina.quadrado.y+proteina.quadrado.width+1,int(proteina.vida_atual/10),3))
                else:
                    DISPLAY.fill((255,255,255),pygame.Rect(proteina.quadrado.x,proteina.quadrado.y+proteina.quadrado.width,int(proteina.vida_total/10000),5))
                    DISPLAY.fill((255,0,0),pygame.Rect(proteina.quadrado.x+1,proteina.quadrado.y+proteina.quadrado.width+1,int(proteina.vida_atual/10000),3))
            except:
                pass
        DISPLAY.fill((255,255,255),retangulo)
        DISPLAY.fill((255,255,255),pygame.Rect(20,580,200,10))
        DISPLAY.fill((255,0,0),pygame.Rect(20,580,int(vida_pancreas/5),10))
        DISPLAY.fill((255,255,255),pygame.Rect(20,590,100,5))
        DISPLAY.fill((200,200,200),pygame.Rect(20,590,40,5))
        DISPLAY.fill((150,150,150),pygame.Rect(20,590,10,5))
        DISPLAY.fill((0,255,0),pygame.Rect(20,590,int(atp_grana/5),5))
        DISPLAY.blit(pygame.font.SysFont("arial", 10).render("VIDA",True,(0,0,0)),(0,580))
        DISPLAY.blit(pygame.font.SysFont("arial", 10).render("ATP",True,(0,0,0)),(0,590))
        if v>=10 and v<=40:
            DISPLAY.fill((255,255,255),pygame.Rect(35,10*v,733,40))
            DISPLAY.blit(pygame.font.SysFont("arial", 40).render("PREPARE-SE! A PRIMEIRA ONDA ESTÁ VINDO!",True,(random.randrange(256),random.randrange(256),random.randrange(256))),(35,10*v))
        if abrir_menu:
            DISPLAY.fill((255,200,200),pygame.Rect(275,200,250,200))
            DISPLAY.fill((200,20,20),pygame.Rect(300,225,200,150))
            DISPLAY.blit(pygame.font.SysFont("arial", 12).render(aviso_texto,True,(0,0,0)),(310,240))
            DISPLAY.fill((0,0,0),quadrado)
            DISPLAY.blit((pygame.image.load('torre1.jpg')),(310,260))
            DISPLAY.blit(pygame.font.SysFont("arial", 15).render('Torre 1',True,(0,0,0)),(310,310))
            DISPLAY.blit(pygame.font.SysFont("arial", 12).render('ATP: 50',True,(0,0,0)),(310,325))
            DISPLAY.blit(pygame.font.SysFont("arial", 10).render('Alcance: 2',True,(0,0,0)),(310,337))
            DISPLAY.blit(pygame.font.SysFont("arial", 10).render('Ataque: 1',True,(0,0,0)),(310,347))
            DISPLAY.blit((pygame.image.load('torre2.jpg')),(380,260))
            DISPLAY.blit(pygame.font.SysFont("arial", 15).render('Torre 2',True,(0,0,0)),(380,310))
            DISPLAY.blit(pygame.font.SysFont("arial", 12).render('ATP: 200',True,(0,0,0)),(380,325))
            DISPLAY.blit(pygame.font.SysFont("arial", 10).render('Alcance: 3',True,(0,0,0)),(380,337))
            DISPLAY.blit(pygame.font.SysFont("arial", 10).render('Ataque: 2',True,(0,0,0)),(380,347))
            DISPLAY.blit((pygame.image.load('torre3.jpg')),(450,260))
            DISPLAY.blit(pygame.font.SysFont("arial", 15).render('Torre 3',True,(0,0,0)),(450,310))
            DISPLAY.blit(pygame.font.SysFont("arial", 12).render('ATP: 500',True,(0,0,0)),(450,325))
            DISPLAY.blit(pygame.font.SysFont("arial", 10).render('Alcance: 4',True,(0,0,0)),(450,337))
            DISPLAY.blit(pygame.font.SysFont("arial", 10).render('Ataque: 3',True,(0,0,0)),(450,347))
            cor_cinza=random.randrange(56)+100
            DISPLAY.fill((255,255,255),pygame.Rect(592,55,160,15))
            DISPLAY.blit(pygame.font.SysFont("arial", 12).render('Pressione ESC para voltar ao jogo.',True,(0,0,0)),(592,55))
            DISPLAY.blit(pygame.font.SysFont("arial black", 45).render("PAUSE",True,(cor_cinza,cor_cinza,cor_cinza)),(591,0))
            DISPLAY.blit(pygame.font.SysFont("arial black", 41).render("PAUSE",True,(255,255,255)),(595,1))
            DISPLAY.blit(pygame.font.SysFont("arial black", 38).render("PAUSE",True,(0,0,0)),(598,4))
        else:
            d+=1
            v+=1
        pygame.display.set_caption('PANCREAS - TOWER DEFENSE (by:Pudim Games)')
        pygame.mouse.set_visible(0)
        pygame.display.update()
        if abrir_menu:
            fpsClock.tick(60)
        else:
            fpsClock.tick(FPS)

pygame.quit()
sys.exit()
