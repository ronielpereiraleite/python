import pygame

pygame.init()

pygame.mixer.music.load('audio01.mp3')
pygame.mixer.music.play()
pygame.event.wait()
