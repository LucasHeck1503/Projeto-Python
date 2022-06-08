import pygame
from random import randint
#função randomiza valores
pygame.init #iniciar aplicação

x = 400
y = 100
pos_x = 300
pos_y = 800
pos_y_a = 800
pos_y_c = 800
velocidade = 25
velocidade_outros = 15
fundo = pygame.image.load('Fundo.png')
carro01 = pygame.image.load('carro01.png')
carro02 = pygame.image.load('carro02.png')
carro03 = pygame.image.load('carro03.png')
carro04 = pygame.image.load('carro04.png')

#criando janela
janela = pygame.display.set_mode((800,600)) #tamanho da tela
pygame.display.set_caption("Jogo em Python") #nome da tela

janela_aberta = True
while janela_aberta: #enquanto janela aberta
    pygame.time.delay(50)
    for event in pygame.event.get() : #aguarda evento get
        if event.type == pygame.QUIT: #se evento get for QUIT
            janela_aberta = False #a janela vai encerrar

    # comando de movimentação
    comandos = pygame.key.get_pressed()
#    if comandos[pygame.K_UP] : 
#        y -= velocidade 
 #   if comandos[pygame.K_DOWN] : 
 #       y += velocidade 
    if comandos[pygame.K_LEFT] and x >= 130:
        x -= velocidade 
    if comandos[pygame.K_RIGHT] and x <= 640:
        x += velocidade
    if(pos_y <= -200):
        pos_y = 900

    pos_y -= velocidade_outros


#movimentação do carro
    if (pos_y <= -180) and (pos_y_a <= - 180) and (pos_y_c <= -180):
        pos_y = randint(800,2000)
        pos_y_a = randint(800,2000)
        pos_y_c = randint(800,2000)
    pos_y -= velocidade_outros
    pos_y_a -= velocidade_outros + 5
    pos_y_c -= velocidade_outros + 3


    #pygame.draw.circle(janela,( 255, 255, 255), (x,y), 25)
                        #janela,    cor,        local, tamanho
    

    
    


    janela.blit(fundo,(0,0))
    janela.blit(carro01,(pos_x - 120,pos_y))
    janela.blit(carro02,(pos_x + 80,pos_y_a))
    janela.blit(carro03,(pos_x + 300,pos_y_c))
    janela.blit(carro04,(x,y))


    pygame.display.update()






pygame.QUIT() #encerrar jogo