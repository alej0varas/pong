#!/usr/bin/env python
# pong game

import pygame

import config


class Pong:
    def __init__(self):
        self.playing = True
        self.player = Player(self)
        self.ia = IA(self)
        self.board = Board(self)
        self.ball = Ball(self)
        self.winer = 0
        pygame.display.init()
        pygame.font.init()
        pygame.event.set_allowed(None)
        pygame.event.set_allowed(pygame.KEYDOWN)
        
    def run(self):
        # display
        self.display = pygame.display.set_mode(config.resolution)
        while self.playing:
            self.board.draw()
            # events
            key = pygame.event.wait().key
            # check quit
            if key == pygame.K_q:
                self.quit()
                continue
            # player
            self.player.play(key)
            # ai
            self.ia.play()
            # draw
            self.ball.play()
            self.player.pad.draw()
            self.ia.pad.draw()
            # check winer
            self.check_winer()
            # screen update, flip
            pygame.display.flip()

    def check_winer(self):
        if self.winer > 0:
            self.player.score += 1
        elif self.winer < 0:
            self.ia.score += 1
        if self.winer:
            self.winer = 0
            self.restart()

    def restart(self):
        self.display.fill(config.background_color)
        self.board.draw()
        self.ball.rect.center = (config.ball_init_x, config.ball_init_y)
        self.ball.draw()
        self.player.pad.centerx = config.init_y
        self.ia.pad.centery = config.init_y

    def quit(self):
        self.playing = False


class Player:
    def __init__(self, game):
        self.game = game
        self.pad = Pad(self, 10, 100)
        self.score = 0

    def play(self, key):
        if key == pygame.K_UP:
            self.pad.up()
        elif key == pygame.K_DOWN:
            self.pad.down()


class IA:
    def __init__(self, game):
        self.game = game
        self.pad = Pad(self, 100, 100)
        self.score = 0

    def play(self):
        if self.game.ball.rect.centery < self.pad.rect.centery:
            self.pad.up()
        else:
            self.pad.down()


class Pad:
    def __init__(self, owner, x, y):
        self.owner = owner
        self.rect = pygame.Rect(x, y, config.pad_width, config.pad_height)
        self._rect = self.rect.copy()
        
    def up(self):
        self.rect.top -= config.pad_speed

    def down(self):
        self.rect.top += config.pad_speed

    def draw(self):
        pygame.draw.rect(self.owner.game.display, config.background_color, self._rect)
        pygame.draw.rect(self.owner.game.display, config.ball_color, self.rect)
        self._rect = self.rect.copy()

class Ball:
    def __init__(self, game):
        self.game = game
        self.vel_x = config.vel_x
        self.vel_y = config.vel_y
        self.rect = pygame.Rect(config.ball_init_x, config.ball_init_y, 0, 0)
        self._rect = self.rect.copy()

    def play(self):
        if self.rect.top <= 0 or self.rect.bottom >= config.height:
            self.vel_y *= -1

        if self.rect.collidelist((self.game.player.pad.rect, self.game.ia.pad.rect)) is not -1:
            self.vel_x *= -1

        if self.rect.left <= 0 or self.rect.right >= config.width:
            self.game.winer = self.vel_x

        self._rect = self.rect.copy()
        self.rect.centerx += self.vel_x
        self.rect.centery += self.vel_y
        self.draw()

    def draw(self):
        pygame.draw.rect(self.game.display, config.background_color, self._rect)
        self.rect = pygame.draw.circle(
            self.game.display, config.ball_color, (self.rect.centerx, self.rect.centery), config.ball_ratio)


class Board:
    def __init__(self, game):
        self.game = game
        self.line = pygame.Rect(config.line_init_x, 0, config.line_width, config.height)

    def draw(self):
        pygame.draw.rect(self.game.display, config.ball_color, self.line)
        self.font = pygame.font.Font(pygame.font.get_default_font(), config.score_text_size)
        self.player = self.font.render(str(self.game.player.score), 1, config.ball_color)
        self.ia = self.font.render(str(self.game.ia.score), 1, config.ball_color)

        self.game.display.blit(self.player, (config.score_text_size, config.score_y))
        self.game.display.blit(self.ia, (config.width - config.score_text_size, config.score_y))

def main():
    p = Pong()
    p.run()

if __name__ == "__main__":
    main()
