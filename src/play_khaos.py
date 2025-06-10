import pygame
from cenario import cenario
from play_audio import executarAudio
from carregar_sprites import carregarSprites


def jogar(tela: pygame.Surface, gameRun: bool, pulando: bool):
    sprites = carregarSprites()

    executarAudio("media/FREE FOR PROFIT Chill Lo-fi Jazz Rap Type Beat 2")

    x_do_bicho = 700
    y_do_bicho = 180

    x = 0
    y = 155
    vivo = True
    i_morreu = True

    cenario(tela, vivo, x_do_bicho, y_do_bicho)
    tela.blit(sprites["kosme_parado"], [x, 155])

    b = 1
    p = 1
    t = 0
    bola_de_fogo = 1
    x_da_bola = x
    ativar_bola_de_fogo = False
    pulando = False
    Kosme_vivo = True

    pygame.display.update()

    # Variável para definir o FPS
    clock = pygame.time.Clock()

    while gameRun:
        # Tick 60 = 60 FPS
        clock.tick(60)

        # MORTE DO KOSME
        if x == x_do_bicho:
            Kosme_vivo = False
            i_morreu = False

            if not i_morreu:
                executarAudio("media/morte.mp3")

            while not Kosme_vivo:
                y = y + 10

                cenario(tela, vivo, x_do_bicho, y_do_bicho)
                tela.blit(sprites["kosme_morrendo"], [x, y])
                pygame.display.update()

                if y > 600:
                    x = 0
                    Kosme_vivo = True
                    
                    cenario(tela, vivo, x_do_bicho, y_do_bicho)
                    tela.blit(sprites["kosme_parado"], [x, 155])
                    i_morreu = True

                    if i_morreu:
                        pygame.time.delay(978)
                        executarAudio(
                            "media/FREE FOR PROFIT Chill Lo-fi Jazz Rap Type Beat 2"
                        )

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

                cenario(tela, vivo, x_do_bicho, y_do_bicho)
                tela.blit(sprites["kosme_parado"], [x, y])
                pygame.display.update()

                if y < 80:
                    p = 0

            while p == 0:
                if t == 1:
                    clock.tick(60)
                    t = 0

                y += 10
                x += 5

                cenario(tela, vivo, x_do_bicho, y_do_bicho)
                tela.blit(sprites["kosme_parado"], [x, y])
                pygame.display.update()

                if y == 155:
                    cenario(tela, vivo, x_do_bicho, y_do_bicho)
                    tela.blit(sprites["kosme_parado"], [x, 155])
                    pygame.display.update()
                    p = 1
                    break

        # KOSME INDO DIREITA
        if comandos[pygame.K_RIGHT]:
            if pulando:
                pulando = False

            x += 10
            
            cenario(tela, vivo, x_do_bicho, y_do_bicho)
            tela.blit(sprites["kosme_andando_direita"][0], [x, 155])
            pygame.display.update()
            clock.tick(60)

            cenario(tela, vivo, x_do_bicho, y_do_bicho)
            tela.blit(sprites["kosme_andando_direita"][1], [x, 155])
            pygame.display.update()

            if x > 799:
                x = 0
                y = 155

                vivo = True
                x_do_bicho = 600
                cenario(tela, vivo, x_do_bicho, y_do_bicho)
                tela.blit(sprites["kosme_andando_direita"][0], [x, 155])
                pygame.display.update()

        # KOSME INDO ESQUERDA
        if comandos[pygame.K_LEFT]:
            if pulando == True:
                pulando = False

            x = x - 10
            
            cenario(tela, vivo, x_do_bicho, y_do_bicho)
            tela.blit(sprites["kosme_andando_esquerda"][0], [x, 155])
            pygame.display.update()
            clock.tick(60)

            cenario(tela, vivo, x_do_bicho, y_do_bicho)
            tela.blit(sprites["kosme_andando_esquerda"][1], [x, 155])
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

                cenario(tela, vivo, x_do_bicho, y_do_bicho)
                tela.blit(sprites["foguinho"], [x_da_bola, 215])
                tela.blit(sprites["kosme_parado"], [x, y])

                posição_da_bola = posição_da_bola + 10
                pygame.display.update()

                if posição_da_bola == 180:
                    final_do_fogo = 0
                    
                    cenario(tela, vivo, x_do_bicho, y_do_bicho)
                    tela.blit(sprites["poof"][0], [x_da_bola, 215])
                    tela.blit(sprites["kosme_parado"], [x, y])
                    pygame.display.update()
                    clock.tick(60)

                    cenario(tela, vivo, x_do_bicho, y_do_bicho)
                    tela.blit(sprites["poof"][1], [x_da_bola, 215])
                    tela.blit(sprites["kosme_parado"], [x, y])
                    pygame.display.update()
                    clock.tick(60)

                    cenario(tela, vivo, x_do_bicho, y_do_bicho)
                    tela.blit(sprites["poof"][2], [x_da_bola, 210])
                    tela.blit(sprites["kosme_parado"], [x, y])
                    pygame.display.update()
                    clock.tick(60)

                    final_do_fogo = 1

                    if final_do_fogo == 1:
                        cenario(tela, vivo, x_do_bicho, y_do_bicho)
                        tela.blit(sprites["kosme_parado"], [x, y])
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
