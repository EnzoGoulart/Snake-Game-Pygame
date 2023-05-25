import pygame
from pygame.locals import *
from random import randint
pygame.init()
pygame.display.set_caption("Meu jogo")

fonte = pygame.font.SysFont('verdana', 40, True, True)
somColisao = pygame.mixer.Sound('snakeGame/SomClique1.mp3')

largura = 640
altura = 480
tela = pygame.display.set_mode((largura, altura))

tamanhoX = 20
tamanhoY = 20

branco = (255, 255, 255)
azul = (54, 204, 255)
rosa = (255, 45, 247)

xCobra = int(largura / 2 - tamanhoX / 2 + 10)
yCobra = int(altura / 2 - tamanhoY / 2 + 10)

xControle = 20
yControle = 0

macaX = 440
macaY = 340
macaTamX = 20
macaTamY = 20

menu = False
pontos = 0
relogio = pygame.time.Clock()
gameOn = True
movs = []
comprimentoInicial = 5
tirarMenu = False


h1Menu = 'Voce perdeu:('
h1Menu = fonte.render(h1Menu, True, (225, 225, 225))
pMenu = 'Aperte r para recomeçar'
pMenu = fonte.render(pMenu, True, (225, 225, 225))


h1Win = 'Voce ganhou!'
h1Win = fonte.render(h1Win, True, (150,240,100))
youWin = False

def aumentaCobra(movs):
    for xy in movs:
        pygame.draw.rect(tela, azul, (xy[0], xy[1], tamanhoX, tamanhoY))

def exibir_menu():
    tela.blit(h1Menu, (160, 200))
    tela.blit(pMenu, (60, 250))

def menuVitoria():
    tela.blit(h1Win, (160, 200))
    tela.blit(pMenu, (60, 250))
while gameOn:
    print(menuVitoria())
    relogio.tick(18)
    tela.fill((0, 0, 0))
    mensagem = f'Pontos: {pontos}'
    textoPontos = fonte.render(mensagem, True, (25, 125, 225))
    
    for event in pygame.event.get():
        if event.type == QUIT:
            gameOn = False
    
    maca = pygame.draw.rect(tela, (255, 10, 60), (macaX, macaY, macaTamX, macaTamY))
    cobra = pygame.draw.rect(tela, azul, (xCobra, yCobra, tamanhoX, tamanhoY))
    linhaCima = pygame.draw.line(tela, branco, (160, 59), (480, 59), 40)
    linhaBaixo = pygame.draw.line(tela, branco, (160, 419), (480, 419), 40)
    linhaEsq = pygame.draw.line(tela, branco, (139, 40), (139, 439), 40)
    linhaDir = pygame.draw.line(tela, branco, (479, 40), (479, 439), 40)
    
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_d]:
        if xControle == 0:
            xControle = 20
            yControle = 0
    if pressed[pygame.K_a]:
        if xControle == 0:
            xControle = -20
            yControle = 0
    if pressed[pygame.K_w]:
        if yControle == 0:
            yControle = -20
            xControle = 0
    if pressed[pygame.K_s]:
        if yControle == 0:
            yControle = 20
            xControle = 0

    if yCobra < 480 - tamanhoY and yCobra > 0 and xCobra > 0 and xCobra < 640 - tamanhoX:
        xCobra += xControle
        yCobra += yControle
    else:
        xControle = 20
        yControle = 0
        xCobra = int(largura / 2 - tamanhoX / 2 + 10)
        yCobra = int(altura / 2 - tamanhoY / 2 + 10)

    if cobra.colliderect(maca):
        macaPossibilidade = 0
        while True:
            macaX = randint(8, 22) * 20
            macaY = randint(4, 19) * 20
            lista1 = []
            lista1.append(macaX)
            lista1.append(macaY)
            if lista1 not in movs:
                break
            
            elif macaPossibilidade ==240:
                youWin = True
                break
            macaPossibilidade +=1
        movsHead = [xCobra, yCobra]
        movs.append(movsHead)
        aumentaCobra(movs)
        pontos += 1
        comprimentoInicial += 1
        somColisao.play()
    if youWin:
        menuVitoria()
    movsHead = [xCobra, yCobra]
    movs.append(movsHead)

    if xCobra > 440 or xCobra < 160 or yCobra > 380 or yCobra < 80:
        menu = True
    
    if menu:
        exibir_menu()
        cobra = False
        if pressed[pygame.K_r]:
            pontos = 0
            comprimentoInicial = 5
            xCobra = int(largura / 2 - tamanhoX / 2 + 10)
            yCobra = int(altura / 2 - tamanhoY / 2 + 10)
            macaX = 440
            macaY = 340
            movs = []
            movsHead = []
            menu = False
            tirarMenu = True

    if not gameOn:
        break
    
    if tirarMenu:
        cobra = True
        tirarMenu = False
    
    if len(movs) > comprimentoInicial:
        del movs[0]

    aumentaCobra(movs)

    tela.blit(textoPontos, (380, 40))

    pygame.display.flip()

pygame.quit()