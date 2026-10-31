# Web port of pancreas_defense.py for pygbag (runs the original game loop asynchronously).
import asyncio
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
cubo_plano =  pygame.Rect(300,250,200,80)
andar_esquerda = False
andar_direita = False
andar_baixo = False
andar_cima = False
abrir_menu = False
comecar_jogo=False
confirmar_compra = False
aviso_texto = ''
vida_pancreas=1002
atp_grana=200
tabuleiro_plataforma = []
itens = []
posicao_compra=1
posicao_tela_inicial=1
caminho_tortuoso=[[True,False,False,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True],[True,False,False,True,True,False,False,False,False,False,False,True,True,False,False,False,False,False,False,True],[True,False,False,True,True,False,False,False,False,False,False,True,True,False,False,False,False,False,False,True],[True,False,False,True,True,False,False,True,True,False,False,True,True,False,False,True,True,False,False,True],[True,False,False,True,True,False,False,True,True,False,False,True,True,False,False,True,True,False,False,True],[True,False,False,True,True,False,False,True,True,False,False,True,True,False,False,True,True,False,False,True],[True,False,False,True,True,False,False,True,True,False,False,True,True,False,False,True,True,False,False,True],[True,False,False,True,True,False,False,True,True,False,False,True,True,False,False,True,True,False,False,True],[True,False,False,True,True,False,False,True,True,False,False,True,True,False,False,True,True,False,False,True],[True,False,False,True,True,False,False,True,True,False,False,True,True,False,False,True,True,False,False,True],[True,False,False,True,True,False,False,True,True,False,False,True,True,False,False,True,True,False,False,True],
                  [True,False,False,False,False,False,False,True,True,False,False,True,True,False,False,True,True,False,False,True],
                  [True,False,False,False,False,False,False,True,True,False,False,False,False,False,False,True,True,False,False,True],
                  [True,True,True,True,True,True,True,True,True,False,False,False,False,False,False,True,True,False,False,True],
                  [False,False,False,False,False,False,False,False,True,True,True,True,True,True,True,True,True,False,False,True]]
def maiorQuezeroINT(numero):
    if numero<0: numero=0
    else: numero=int(numero)
    return numero
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
            self.imagem=pygame.image.load("torre1.png")
            self.posicao=(int(retangulo.x+1),int(retangulo.y+1))
            self.cor=(0,0,0)
        if opcao==2:
            self.ataque=2
            self.x=retangulo.x
            self.y=retangulo.y
            self.alcance=3
            caminho_tortuoso[int(retangulo.y/40)][int(retangulo.x/40)]='torre 1'
            self.quadrado=pygame.Rect(int(retangulo.x+1),int(retangulo.y+1),38,38)
            self.imagem=pygame.image.load("torre2.png")
            self.posicao=(int(retangulo.x+1),int(retangulo.y+1))
            self.cor=(0,0,0)
        if opcao==3:
            self.ataque=3
            self.x=retangulo.x
            self.y=retangulo.y
            self.alcance=4
            caminho_tortuoso[int(retangulo.y/40)][int(retangulo.x/40)]='torre 1'
            self.quadrado=pygame.Rect(int(retangulo.x+1),int(retangulo.y+1),38,38)
            self.imagem=pygame.image.load("torre3.png")
            self.posicao=(int(retangulo.x+1),int(retangulo.y+1))
            self.cor=(0,0,0)
class diabetesPudim(object):
    def __init__(self,ataque,defesa,vida,velocidade,imagem,ordem=0):
        self.vida_atual=vida
        self.vida_total=vida
        self.defesa=defesa
        self.ataque=ataque
        self.padrao=(random.randrange(2)+1)
        self.imagem=pygame.image.load(imagem)
        self.x=(40*self.padrao)
        self.y=ordem*(-1)
        self.velocidade=velocidade+random.randrange(5)
        self.movimento=0
        self.desce=True
        self.direita=False
pancreas=[]
exercito=[]
v=0
d=0


async def main():
    global abrir_menu, andar_baixo, andar_cima, andar_direita, andar_esquerda, atp_grana, aviso_texto, comecar_jogo, confirmar_compra, cor_cinza, d, event, i, posicao_compra, posicao_tela_inicial, proteina, rodando, torre, v, vida_pancreas, vitoria_verifica
    while rodando:
        if vida_pancreas>=1002:
            if vida_pancreas>=1003:
                if comecar_jogo:
                    vida_pancreas=1002
            else:
                if andar_cima and posicao_tela_inicial>1:
                    cubo_plano.y-=80
                    posicao_tela_inicial-=1
                    andar_cima=False
                if andar_baixo and posicao_tela_inicial<3:
                    cubo_plano.y+=80
                    posicao_tela_inicial+=1
                    andar_baixo=False
                if comecar_jogo:
                    if posicao_tela_inicial==1:
                        vida_pancreas-=1
                    if posicao_tela_inicial==2:
                        vida_pancreas+=1
                    if posicao_tela_inicial==3:
                        vida_pancreas+=2
                    comecar_jogo=False
            for event in pygame.event.get():
                if event.type == QUIT:
                    rodando = False
                if event.type== KEYUP and event.key == K_ESCAPE:
                    rodando = False
                if event.type == KEYUP:
                    if event.key == K_RETURN or event.key == K_SPACE:
                        comecar_jogo = False
                if event.type == KEYDOWN:
                    if event.key == K_RETURN or event.key == K_SPACE:
                        comecar_jogo = True
                if vida_pancreas==1002:
                    if event.type == KEYDOWN:
                        if event.key == K_LEFT or event.key == K_a:
                            andar_cima = True
                    if event.type == KEYUP:
                        if event.key == K_LEFT or event.key == K_a:
                            andar_cima = False
                    if event.type == KEYUP:
                        if event.key == K_RIGHT or event.key == K_d:
                            andar_baixo = False
                    if event.type == KEYDOWN:
                        if event.key == K_RIGHT or event.key == K_d:
                            andar_baixo = True
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
            DISPLAY.fill((255,255,255))
            DISPLAY.blit((pygame.image.load('pancreas_defense.jpg')),(370,150))
            pygame.display.set_icon(pygame.image.load('torre2.png'))
            pygame.mouse.set_visible(0)
            pygame.display.set_caption('PANCREAS - TOWER DEFENSE (by:Pudim Games)')
            DISPLAY.blit(pygame.font.SysFont("arial", 32).render("PÂNCREAS - TOWER DEFENSE",True,(0,0,0)),(200,50))
            DISPLAY.blit(pygame.font.SysFont("arial", 32).render("by: Pudim Games",True,(0,0,0)),(300,82))
            if vida_pancreas==1004:
                DISPLAY.blit(pygame.font.SysFont("arial black", 20).render("Os açúcares, carboidratos e proteínas avançarão pela parte mais baixa.",True,(0,0,0)),(0,255))
                DISPLAY.blit(pygame.font.SysFont("arial black", 20).render("Destrua-as e obtenha ATP antes que eles sobrecarreguem o órgão.",True,(0,0,0)),(0,335))
                DISPLAY.blit(pygame.font.SysFont("arial black", 20).render("Posicione suas torres de defesa celular nas partes mais altas.",True,(0,0,0)),(0,415))
                DISPLAY.blit(pygame.font.SysFont("arial black", 20).render("O ATP obtido pode ser usado para construir mais e mais torres!",True,(0,0,0)),(0,495))
            if vida_pancreas==1003:
                DISPLAY.blit((pygame.image.load('pudim_games.jpg')),(150,350))
                DISPLAY.blit(pygame.font.SysFont("arial black", 20).render("Produtora:",True,(0,0,0)),(300,235))
                DISPLAY.blit(pygame.font.SysFont("arial black", 20).render("Designer:",True,(0,0,0)),(300,315))
                DISPLAY.blit(pygame.font.SysFont("arial black", 20).render("Artista:",True,(0,0,0)),(300,395))
                DISPLAY.blit(pygame.font.SysFont("arial black", 20).render("Programador:",True,(0,0,0)),(300,475))
                DISPLAY.blit(pygame.font.SysFont("arial black", 20).render("Maria Tereza Font Fernandes",True,(0,0,0)),(320,255))
                DISPLAY.blit(pygame.font.SysFont("arial black", 20).render("Luiz Gustavo Pelatieri Teixeira",True,(0,0,0)),(320,335))
                DISPLAY.blit(pygame.font.SysFont("arial black", 20).render("Josias Danny de Viveiro ",True,(0,0,0)),(320,415))
                DISPLAY.blit(pygame.font.SysFont("arial black", 20).render("Fernando Luiz Neme Chibli",True,(0,0,0)),(320,495))
            if vida_pancreas==1002:
                DISPLAY.fill((random.randrange(256),random.randrange(256),random.randrange(256)),pygame.Rect(cubo_plano.x-5,cubo_plano.y-5,cubo_plano.width+10,cubo_plano.height+10))
                DISPLAY.fill((255,255,255),cubo_plano)
                DISPLAY.blit(pygame.font.SysFont("arial black", 40).render("JOGAR",True,(0,0,0)),(320,255))
                DISPLAY.blit(pygame.font.SysFont("arial black", 40).render("EQUIPE",True,(0,0,0)),(315,335))
                DISPLAY.blit(pygame.font.SysFont("arial black", 40).render("REGRAS",True,(0,0,0)),(308,415))
            pygame.display.update()
            await asyncio.sleep(0)
            fpsClock.tick(10)
        elif vida_pancreas==1001:
            if comecar_jogo:
                vida_pancreas-=1
            for event in pygame.event.get():
                if event.type == QUIT:
                    rodando = False
                if event.type== KEYUP and event.key == K_ESCAPE:
                    rodando = False
                if event.type == KEYUP:
                    if event.key == K_RETURN or event.key == K_SPACE:
                        comecar_jogo = False
                if event.type == KEYDOWN:
                    if event.key == K_RETURN or event.key == K_SPACE:
                        comecar_jogo = True
            DISPLAY.fill((255,200,0))
            pygame.display.set_icon(pygame.image.load('torre2.png'))
            pygame.display.set_caption('PANCREAS - TOWER DEFENSE (by:Pudim Games)')
            pygame.mouse.set_visible(0)
            DISPLAY.blit(pygame.font.SysFont("arial", 32).render("PÂNCREAS - TOWER DEFENSE",True,(0,0,0)),(200,200))
            DISPLAY.blit(pygame.font.SysFont("arial", 32).render("by: Pudim Games",True,(0,0,0)),(300,232))
            DISPLAY.blit(pygame.font.SysFont("arial", 32).render(" Defenda o seu pâncreas!",True,(0,0,0)),(250,264))
            pygame.display.update()
            await asyncio.sleep(0)
            fpsClock.tick(int(FPS/2))
        elif vida_pancreas<100:
            for event in pygame.event.get():
                if event.type == QUIT:
                    rodando = False
                if event.type== KEYUP and event.key == K_ESCAPE:
                    rodando = False
            DISPLAY.fill((random.randrange(156)+100,0,0))
            DISPLAY.blit(pygame.font.SysFont("arial", 32).render("SEU PÂNCREAS JÁ ERA!",True,(0,0,0)),(260,280))
            pygame.display.set_icon(pygame.image.load('torre1.png'))
            pygame.display.set_caption('PANCREAS - TOWER DEFENSE (by:Pudim Games)')
            pygame.mouse.set_visible(0)
            pygame.display.update()
            await asyncio.sleep(0)
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
                                aviso_texto= 'Seu pâncreas não tem ATP o suficiente!'
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
                if d==5:#self,ataque,defesa,vida,velocidade,imagem,ordem=0
                    if v>100 and v<=200: exercito.append(diabetesPudim(5,0.1,150,6,'inimigo1.png'))
                    elif v>300 and v<=400: exercito.append(diabetesPudim(5,0.2,200,5,'inimigo2.png'))
                    elif v>500 and v<=600: exercito.append(diabetesPudim(5,0.5,280,4,'inimigo3.png'))
                    elif v>700 and v<=900: exercito.append(diabetesPudim(6,0.5,350,3,'inimigo4.png'))
                    elif v>1000 and v<=1100: exercito.append(diabetesPudim(10,0.5,400,2,'inimigo5.png'))
                    elif v>1200 and v<=1600: exercito.append(diabetesPudim(13,0.8,650,1,'inimigo6.png'))
                    elif v>1700 and v<=1900: exercito.append(diabetesPudim(13,0.9,800,4,'inimigo7.png'))
                    elif v>2000 and v<=2200: exercito.append(diabetesPudim(15,0.99999,900,5,'inimigo8.png'))
                    elif v>2300 and v<=2500: exercito.append(diabetesPudim(15,0.9999999,1000,5,'caramelo.png'))
                    elif v>2600 and v<=2800: exercito.append(diabetesPudim(18,0.999999999,1500,4,'caramelo.png'))
                    elif v>2900 and v<=3100: exercito.append(diabetesPudim(18,0.99999999999,2000,2,'caramelo.png'))
                    elif v>3200 and v<=3400: exercito.append(diabetesPudim(10,0.999999999999,3000,1,'caramelo.png'))
                    elif v>3600 and v<=4700: exercito.append(diabetesPudim(25,1.2,1900,15,'pudim.png'))
                    elif v>4800 and v<=4900: exercito.append(diabetesPudim(35,1.5,50000,25,'pudim.png'))
                    elif v>5000 and v<=5100: exercito.append(diabetesPudim(50,1.8,100000,30,'pudim.png'))
                    elif v==5200: exercito.append(diabetesPudim(50,2,100000,30,'pudim.png'))
                    d=0
                for proteina in exercito:
                    try:
                        for torre in pancreas:
                            if int(proteina.y/40)<int(torre.quadrado.y/40)+torre.alcance and int(proteina.y/40)>int(torre.quadrado.y/40)-torre.alcance and int(proteina.x/40)<int(torre.quadrado.x/40)+torre.alcance and int(proteina.x/40)>int(torre.quadrado.x/40)-torre.alcance:
                                if torre.ataque>proteina.defesa: proteina.vida_atual-=torre.ataque+proteina.defesa
                        if proteina.movimento==proteina.velocidade:
                            proteina.movimento=0
                            if proteina.direita==True:
                                if caminho_tortuoso[int(proteina.y/40)][int(proteina.x/40)+proteina.padrao]==False:
                                    proteina.x+=40
                                else:
                                    proteina.direita=False
                            elif proteina.desce==True:
                                if caminho_tortuoso[int(proteina.y/40)+proteina.padrao][int(proteina.x/40)]==False:
                                    proteina.y+=40
                                else:
                                    proteina.desce=False
                                    proteina.direita=True
                            else:
                                if caminho_tortuoso[int(proteina.y/40)-3+proteina.padrao][int(proteina.x/40)]==False:
                                    proteina.y-=40
                                else:
                                    proteina.desce=True
                                    proteina.direita=True
                        else:
                            proteina.movimento+=1
                        if proteina.vida_atual<=0 and proteina.movimento<1000:
                            #atp_grana+=proteina.ataque+random.randrange(int((proteina.ataque/3)+0.5))+1
                            atp_grana+=1+int(1.5*proteina.ataque)+random.randrange(proteina.ataque)
                            proteina.y=-1
                            proteina.x=-1
                            proteina.movimento=1000
                            proteina.imagem=''
                        if int(proteina.y/40)==15-proteina.padrao and int(proteina.x/40)>=17:
                            vida_pancreas-=proteina.ataque
                            proteina.y=-1
                            proteina.x=-1
                            proteina.movimento=1000
                            proteina.imagem=''
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
                    DISPLAY.blit(proteina.imagem,(proteina.x,proteina.y))
    #                DISPLAY.fill(proteina.cor,proteina.quadrado)
                    if proteina.vida_total<500:
                        DISPLAY.fill((255,255,255),pygame.Rect(proteina.x,proteina.y+40,int(proteina.vida_total/10),5))
                        DISPLAY.fill((255,0,0),pygame.Rect(proteina.x+1,proteina.y+40+1,int(proteina.vida_atual/10),3))
                    elif proteina.vida_total<1000:
                        DISPLAY.fill((255,255,255),pygame.Rect(proteina.x,proteina.y+40,int(proteina.vida_total/20),5))
                        DISPLAY.fill((200,0,0),pygame.Rect(proteina.x+1,proteina.y+40+1,int(proteina.vida_atual/20),3))
                    elif proteina.vida_total<10000:
                        DISPLAY.fill((255,255,255),pygame.Rect(proteina.x,proteina.y+40,int(proteina.vida_total/200),5))
                        DISPLAY.fill((100,0,0),pygame.Rect(proteina.x+1,proteina.y+40+1,int(proteina.vida_atual/200),3))
                    elif proteina.vida_total<=100000:
                        DISPLAY.fill((255,255,255),pygame.Rect(proteina.x,proteina.y+40,int(proteina.vida_total/2000),5))
                        DISPLAY.fill((55,0,0),pygame.Rect(proteina.x+1,proteina.y+40+1,int(proteina.vida_atual/2000),3))
                    else:
                        DISPLAY.fill((255,255,255),pygame.Rect(proteina.x,proteina.y+40,int(proteina.vida_total/100000),5))
                        DISPLAY.fill((0,0,0),pygame.Rect(proteina.x+1,proteina.y+40+1,int(proteina.vida_atual/100000),3))
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
            vitoria_verifica=0
            for proteina in exercito:
                if proteina.imagem!='': vitoria_verifica+=maiorQuezeroINT(proteina.vida_atual)
            if vitoria_verifica<=0 and v>5200:
                DISPLAY.fill((255,255,255),pygame.Rect(0,280,800,80))
                DISPLAY.blit(pygame.font.SysFont("arial", 80).render("PARABÉNS, VENCEDOR!",True,(255,100,100)),(10,280))
            if v>=10 and v<=40:
                DISPLAY.fill((255,250,250),pygame.Rect(35,10*v+10,733,40))
                DISPLAY.blit(pygame.font.SysFont("arial", 40).render("PREPARE-SE! A PRIMEIRA ONDA ESTÁ VINDO!",True,(random.randrange(256),random.randrange(256),random.randrange(256))),(35,10*v+10))
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
            pygame.display.set_icon(pygame.image.load('torre3.png'))
            pygame.display.set_caption('PANCREAS - TOWER DEFENSE (by:Pudim Games)')
            pygame.mouse.set_visible(0)
            pygame.display.update()
            await asyncio.sleep(0)
            if abrir_menu or x>0 and v>5200:
                fpsClock.tick(60)
            else:
                fpsClock.tick(FPS)



asyncio.run(main())
