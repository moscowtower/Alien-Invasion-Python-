import pygame.font

class Button():

    def __init__(self, ai_settings, screen, msg):
        #инициализация атрибутов кнопки
        self.screen = screen
        self.screen_rect = screen.get_rect()
        #назначение размеров и свойств кнопок
        self.width, self.height = 600, 150
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        #построение объекта rect кнопки и выравнивание по центру экрана
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        #сообщение кнопки создается только один раз
        self.prep_msg(msg)

    def prep_msg(self, msg):
        #делаем из мессаги прямоугольник и выравниваем
        self.msg_image = self.font.render(
                        msg,
                        True,
                        self.text_color,
                        self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        #отображение пустой кнопки и вывод сообщения
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)


