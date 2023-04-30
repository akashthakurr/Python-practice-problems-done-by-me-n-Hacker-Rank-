
import pygame

# Initialize Pygame mixer
pygame.mixer.init()

# Load music file
pygame.mixer.music.load("music.mp3")

# Play music
pygame.mixer.music.play()

# Keep the program running while the music is playing
while pygame.mixer.music.get_busy():
    pygame.time.delay(100)
