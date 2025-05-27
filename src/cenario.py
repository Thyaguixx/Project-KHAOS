import pygame

def cenario(tela, vivo: bool, x_do_bicho: int, y_do_bicho: int):
    # cenario
    cenario_original = pygame.image.load("assets/cenario 80 porcento.png")
    cenario_aumentado = pygame.transform.scale(cenario_original, [900, 600])
    tela.blit(cenario_aumentado, [0, 0])

    if vivo == True:
        bicho = pygame.image.load("assets/bicho.png")
        bicho1 = pygame.transform.scale(bicho, [70, 90])
        tela.blit(bicho1, [x_do_bicho, y_do_bicho])