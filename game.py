import pygame
pygame.init #iniciar aplicação

x = 400
y = 300
pos_x = 300
pos_y = 300
velocidade = 5
fundo = pygame.image.load('Fundo.png')
carro01 = pygame.image.load('carro1.png')
carro02 = pygame.image.load('carro2.png')
carro03 = pygame.image.load('carro3.png')
carro04 = pygame.image.load('carro4.png')

#criando janela
janela = pygame.display.set_mode((800,600)) #tamanho da tela
pygame.display.set_caption("Jogo em Python") #nome da tela

janela_aberta = True
while janela_aberta: #enquanto janela aberta
    pygame.time.delay(10)
    for event in pygame.event.get() : #aguarda evento get
        if event.type == pygame.QUIT: #se evento get for QUIT
            janela_aberta = False #a janela vai encerrar

    # comando de movimentação
    comandos = pygame.key.get_pressed()
    if comandos[pygame.K_UP] : 
        y -= velocidade 
    if comandos[pygame.K_DOWN] : 
        y += velocidade 
    if comandos[pygame.K_LEFT] : 
        x -= velocidade 
    if comandos[pygame.K_RIGHT] : 
        x += velocidade


    #pygame.draw.circle(janela,( 255, 255, 255), (x,y), 25)
                        #janela,    cor,        local, tamanho
    

    janela.blit(fundo,(0,0))
    janela.blit(carro01,(pos_x - 120,pos_y))
    janela.blit(carro02,(pos_x + 80,pos_y))
    janela.blit(carro03,(pos_x + 300,pos_y))
    janela.blit(carro04,(x,y))


    pygame.display.update()






pygame.QUIT() #encerrar jogo