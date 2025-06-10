import pygame
from pygame.mixer import Sound
from play_khaos import jogar

global gameRun, pulando

pygame.init()
tela = pygame.display.set_mode([800, 600])

# Deixar com fundo branco primeiramente
tela.fill(pygame.Color(255, 255, 255))

# Nome da aba do jogo
pygame.display.set_caption("Project-KHAOS")

gameRun = True
pulando = False

jogar(tela, gameRun, pulando)