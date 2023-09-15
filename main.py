# Подключение модулей
import pygame
# Константы
WINDOW_SIZE = WINDOW_WIDTH, WINDOW_HEIGHT = (300, 300)
# Переменные и инициализация
pygame.init()
screen = pygame.display.set_mode(WINDOW_SIZE)
# Цикл программы
while True:
	# Условие закрытия программы
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()