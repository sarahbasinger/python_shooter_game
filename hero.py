import pygame
from pygame.sprite import Sprite

class Hero(Sprite):
	def __init__(self, screen, settings):
		super(Hero,self).__init__()
		self.image = pygame.image.load('hero.png')
		self.screen = screen
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		print self.screen_rect
		self.rect.centery = self.screen_rect.centery
		self.rect.left = self.screen_rect.left
		self.moving_right = False
		self.moving_left = False
		self.moving_up = False
		self.moving_down = False
		self.speed = settings.hero_speed
		
	def update_me(self):
		if self.moving_right:
			self.rect.centerx += 10 * self.speed
		elif self.moving_left:
			self.rect.centerx -= 10 * self.speed

		if self.moving_down:
			self.rect.centery += 10 * self.speed
		elif self.moving_up:
			self.rect.centery -= 10 * self.speed
			
	def draw_me(self):
		self.screen.blit(source = self.image, dest = self.rect)		