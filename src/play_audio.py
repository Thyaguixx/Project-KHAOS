import pygame

def executarAudio(path: str):
    pygame.mixer.music.load(path)
    pygame.mixer.music.play()

