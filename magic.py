import pygame
from settings import *
from random import randint

class MagicPlayer:
    def __init__(self, animation_player):
        self.animation_player = animation_player
        self.sounds = {
            "heal" : pygame.mixer.Sound("audio/heal.wav"),
            "flame" : pygame.mixer.Sound("audio/Fire.wav")
        }
        self.sounds["heal"].set_volume(0.4)
        self.sounds["flame"].set_volume(0.4)
    
    def heal(self, player, strength, cost, groups):
        if player.energy >= cost:

            self.sounds["heal"].play()

            player.health += strength
            player.energy -= cost

            self.animation_player.create_particles('aura', player.rect.center, groups)
            self.animation_player.create_particles('heal', player.rect.center - pygame.math.Vector2(0, 60), groups)

            if player.health > player.stats["health"]:

                player.health = player.stats["health"]

    def flame(self, player, cost, groups):
        if player.energy >= cost:

            self.sounds["flame"].play()

            player.energy -= cost

            direction = player.status.split("_")[0]

            if direction == "right":
                direction = pygame.math.Vector2(1, 0)
            
            elif direction == "left":
                direction = pygame.math.Vector2(-1, 0)

            elif direction == "up":
                direction = pygame.math.Vector2(0, -1)

            else:
                direction = pygame.math.Vector2(0, 1)
            
            for i in range(1, 6):

                if direction.x: # Horizontal

                    offset_x = (direction.x * i) * TILESIZE
                    x = player.rect.centerx + offset_x + randint(-TILESIZE // 4, TILESIZE // 4)
                    y = player.rect.centery + randint(-TILESIZE // 4, TILESIZE // 4)
                    self.animation_player.create_particles("flame", (x, y), groups)

                else: # Vertical
                    
                    offset_y = (direction.y * i) * TILESIZE
                    x = player.rect.centerx + randint(-TILESIZE // 4, TILESIZE // 4)
                    y = player.rect.centery + offset_y + randint(-TILESIZE // 4, TILESIZE // 4)
                    self.animation_player.create_particles("flame", (x, y), groups)

