import pygame
from cenario import cenario
from play_audio import executarAudio
from main import tela

def jogar(gameRun: bool):
    executarAudio("media/FREE FOR PROFIT Chill Lo-fi Jazz Rap Type Beat 2")
    
    x_do_bicho = 700
    y_do_bicho = 180
    
    FPS = int(1000 / 60)
    FPS_do_fogo = int(1000 / 30)
    FPS_andando = int(1000 / 45)
    FPS_do_bicho = int(1000 / 17)
   
    x = 0
    y = 155
    vivo = True
    i_morreu = True

    # Mario sprite 1
    Kosme_parado = pygame.image.load("assets/original parado.png")
    Kosme_parado_1 = pygame.transform.scale(Kosme_parado, [100, 120])
    cenario(tela, vivo, x_do_bicho, y_do_bicho)
    tela.blit(Kosme_parado_1, [x, 155])

    b = 1
    p = 1
    t = 0
    bola_de_fogo = 1
    x_da_bola = x
    ativar_bola_de_fogo = False
    pulando = False
    Kosme_vivo = True

    pygame.display.update()

    while gameRun:
        # MORTE DO KOSME
        if x == x_do_bicho:
            Kosme_vivo = False
            i_morreu = False
            
            if not i_morreu:
                executarAudio("media/morte.mp3")

            while not Kosme_vivo:
                y = y + 10

                original_morrendo = pygame.image.load("assets/original morrendo.png")
                original_morrendo_1 = pygame.transform.scale(
                    original_morrendo, [100, 120]
                )
                cenario(tela, vivo, x_do_bicho, y_do_bicho)
                tela.blit(original_morrendo_1, [x, y])
                pygame.display.update()

                if y > 600:
                    x = 0
                    Kosme_vivo = True
                    Kosme_parado = pygame.image.load("assets/original parado.png")
                    Kosme_parado_1 = pygame.transform.scale(Kosme_parado, [100, 120])
                    cenario(tela, vivo, x_do_bicho, y_do_bicho)
                    tela.blit(Kosme_parado_1, [x, 155])
                    i_morreu = True

                    if i_morreu:
                        pygame.time.delay(978)
                        executarAudio("media/FREE FOR PROFIT Chill Lo-fi Jazz Rap Type Beat 2")

                    pygame.display.update()
                    y = 155
                    break

        comandos = pygame.key.get_pressed()
       
        # KOSME PULANDO
        if comandos[pygame.K_UP]:
            pulando = True

            while pulando and b == 1 and p == 1:
                y -= 10
                x += 5

                Kosme_parado = pygame.image.load("assets/original parado.png")
                Kosme_parado_1 = pygame.transform.scale(Kosme_parado, [100, 120])
                cenario(tela, vivo, x_do_bicho, y_do_bicho)
                tela.blit(Kosme_parado_1, [x, y])
                pygame.display.update()

                if y < 80:
                    p = 0

            while p == 0:
                if t == 1:
                    pygame.time.wait(FPS)
                    t = 0
                
                y += 10
                x += 5
                
                Kosme_parado = pygame.image.load("assets/original parado.png")
                Kosme_parado_1 = pygame.transform.scale(Kosme_parado, [100, 120])
                cenario(tela, vivo, x_do_bicho, y_do_bicho)
                tela.blit(Kosme_parado_1, [x, y])
                pygame.display.update()

                if y == 155:
                    Kosme_parado = pygame.image.load("assets/original parado.png")
                    Kosme_parado_1 = pygame.transform.scale(Kosme_parado, [100, 120])
                    cenario(tela, vivo, x_do_bicho, y_do_bicho)
                    tela.blit(Kosme_parado_1, [x, 155])
                    pygame.display.update()
                    p = 1
                    break

        # KOSME INDO DIREITA
        if comandos[pygame.K_RIGHT]:
            if pulando:
                pulando = False

            x += 10
            Kosme_andando = pygame.image.load("assets/correndo direita.png")
            Kosme_andando_1 = pygame.transform.scale(Kosme_andando, [100, 120])
            cenario(tela, vivo, x_do_bicho, y_do_bicho)
            tela.blit(Kosme_andando_1, [x, 155])
            pygame.display.update()
            pygame.time.wait(FPS_andando)

            Kosme_correndo = pygame.image.load("assets/correndo direita2.png")
            Kosme_correndo_1 = pygame.transform.scale(Kosme_correndo, [100, 120])
            cenario(tela, vivo, x_do_bicho, y_do_bicho)
            tela.blit(Kosme_correndo_1, [x, 155])
            pygame.display.update()

            if x > 799:
                x = 0
                y = 155

                Kosme_andando = pygame.image.load("assets/correndo direita.png")
                Kosme_andando_1 = pygame.transform.scale(Kosme_andando, [100, 120])
                vivo = True
                x_do_bicho = 600
                cenario(tela, vivo, x_do_bicho, y_do_bicho)
                tela.blit(Kosme_andando_1, [x, 155])
                pygame.display.update()

        # KOSME INDO ESQUERDA
        if comandos[pygame.K_LEFT]:
            if pulando == True:
                pulando = False

            x = x - 10
            Kosme_andando = pygame.image.load("assets/correndo esquerda.png")
            Kosme_andando_1 = pygame.transform.scale(Kosme_andando, [100, 120])
            cenario(tela, vivo, x_do_bicho, y_do_bicho)
            tela.blit(Kosme_andando_1, [x, 155])
            pygame.display.update()

            pygame.time.wait(FPS_andando)
            Kosme_correndo = pygame.image.load("assets/correndo esquerda2.png")
            Kosme_correndo_1 = pygame.transform.scale(Kosme_correndo, [100, 120])
            cenario(tela, vivo, x_do_bicho, y_do_bicho)
            tela.blit(Kosme_correndo_1, [x, 155])
            pygame.display.update()

            if x < 0:
                x = 0

        # KOSME ATIRANDO
        if comandos[pygame.K_SPACE]:
            ativar_bola_de_fogo = True
            x_da_bola = x
            posição_da_bola = 0
            
            while ativar_bola_de_fogo and bola_de_fogo == 1:
                x_da_bola = x_da_bola + 20

                foguinho = pygame.image.load("assets/fireball.png")
                foguinho_2 = pygame.transform.scale(foguinho, [20, 20])

                mario_1 = pygame.image.load("assets/original parado.png")
                mario_11 = pygame.transform.scale(mario_1, [100, 120])

                cenario(tela, vivo, x_do_bicho, y_do_bicho)
                tela.blit(foguinho_2, [x_da_bola, 215])
                tela.blit(mario_11, [x, y])

                posição_da_bola = posição_da_bola + 10
                pygame.display.update()

                if posição_da_bola == 180:
                    final_do_fogo = 0
                    fogo_sprite1 = pygame.image.load("assets/poof-1.png")
                    fogo_sprite1_1 = pygame.transform.scale(fogo_sprite1, [20, 20])
                    cenario(tela, vivo, x_do_bicho, y_do_bicho)
                    tela.blit(fogo_sprite1_1, [x_da_bola, 215])
                    tela.blit(mario_11, [x, y])
                    pygame.display.update()
                    pygame.time.wait(FPS_do_fogo)

                    fogo_sprite2 = pygame.image.load("assets/poof-2.png")
                    fogo_sprite2_2 = pygame.transform.scale(fogo_sprite2, [30, 30])
                    cenario(tela, vivo, x_do_bicho, y_do_bicho)
                    tela.blit(fogo_sprite2_2, [x_da_bola, 215])
                    tela.blit(mario_11, [x, y])
                    pygame.display.update()
                    pygame.time.wait(FPS_do_fogo)

                    fogo_sprite3 = pygame.image.load("assets/poof-3.png")
                    fogo_sprite3_3 = pygame.transform.scale(fogo_sprite3, [50, 50])
                    cenario(tela, vivo, x_do_bicho, y_do_bicho)
                    tela.blit(fogo_sprite3_3, [x_da_bola, 210])
                    tela.blit(mario_11, [x, y])
                    pygame.display.update()
                    pygame.time.wait(FPS_do_fogo)
                    final_do_fogo = 1

                    if final_do_fogo == 1:
                        cenario(tela, vivo, x_do_bicho, y_do_bicho)
                        tela.blit(mario_11, [x, y])
                        pygame.display.update()
                        break

                if x_da_bola == x_do_bicho - 10:
                    x_do_bicho = 1000
                    vivo = False
                    pygame.display.update()

        # SAIR DO JOGO
        sair = False
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                sair = True
        if sair == True:
            pygame.quit()