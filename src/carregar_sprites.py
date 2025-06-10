import pygame


def carregarSprites():
    size_kosme = [100, 120]

    kosme_parado = pygame.transform.scale(
        pygame.image.load("assets/original parado.png"), size_kosme
    )
    kosme_morrendo = pygame.transform.scale(
        pygame.image.load("assets/original morrendo.png"), size_kosme
    )
    kosme_andando_direita_frame1 = pygame.transform.scale(
        pygame.image.load("assets/correndo direita.png"), size_kosme
    )
    kosme_andando_direita_frame2 = pygame.transform.scale(
        pygame.image.load("assets/correndo direita2.png"), size_kosme
    )
    kosme_andando_esquerda_frame1 = pygame.transform.scale(
        pygame.image.load("assets/correndo esquerda.png"), size_kosme
    )
    kosme_andando_esquerda_frame2 = pygame.transform.scale(
        pygame.image.load("assets/correndo esquerda2.png"), size_kosme
    )

    foguinho = pygame.transform.scale(pygame.image.load("assets/fireball.png"), [20,20])

    poof_1 = pygame.transform.scale(pygame.image.load("assets/poof-1.png"), [20,20])
    poof_2 = pygame.transform.scale(pygame.image.load("assets/poof-2.png"), [30,30])
    poof_3 = pygame.transform.scale(pygame.image.load("assets/poof-3.png"), [50,50])

    return {
        "kosme_parado": kosme_parado,
        "kosme_morrendo": kosme_morrendo,
        "kosme_andando_direita": [
            kosme_andando_direita_frame1,
            kosme_andando_direita_frame2,
        ],
        "kosme_andando_esquerda": [
            kosme_andando_esquerda_frame1,
            kosme_andando_esquerda_frame2,
        ],
        "foguinho": foguinho,
        "poof": [poof_1, poof_2, poof_3],
    }