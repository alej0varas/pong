#!/usr/bin/env python
# pong game

import pygame

import config


class Pong:
    def __init__(self):
        self.playing = True
        self.player = Player()
        self.ia = IA()
        self.ball = Ball(self)
        pygame.display.init()
        pygame.event.set_allowed(None)
        pygame.event.set_allowed(pygame.KEYDOWN)

    def run(self):
        # display
        self.display = pygame.display.set_mode(config.resolution)

        while self.playing:
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

            # screen update, flip
            pygame.display.flip()
#            print self

    def quit(self):
        self.playing = False

    def __str__(self):
        return str(self.playing)


class Player:
    def __init__(self):
        self.pad = Pad(self, 10, 100)

    def play(self, key):
        if key == pygame.K_UP:
            self.pad.up()
        elif key == pygame.K_DOWN:
            self.pad.down()


class IA:
    def __init__(self):
        self.pad = Pad(self, 100, 100)
        #super(type(IA), self).__init__()

    def play(self):
        print "ia turn"
        pass


class Pad:
    def __init__(self, owner, x, y):
        self.owner = owner
        self.x = x
        self.y = y
        self.rect = pygame.Rect(0, 0, 0, 0)
        
    def up(self):
        self.y += 1
        print "up"

    def down(self):
        self.y -= 1
        print "down"


class Ball:
    def __init__(self, game):
        self.game = game
        self.x, self.y = config.width/2, config.height/2
        self.vel_x = config.vel_x * 0
        self.vel_y = config.vel_y * -1
        self.rect = pygame.Rect(0, 0, 0, 0)

    def play(self):
        print self.rect.top, self.rect.bottom
        if self.rect.top <= 0 or self.rect.bottom >= config.height:
            self.vel_y *= -1

        if self.rect.collidelist((self.game.player.pad.rect, self.game.ia.pad.rect)) is not -1:
            self.vel_x *= -1

        self.x += self.vel_x
        self.y += self.vel_y
        self.draw()

    def draw(self):
        pygame.draw.rect(self.game.display, config.background_color, self.rect)
        self.rect = pygame.draw.circle(self.game.display, config.ball_color, (self.x, self.y), 20)

def main():
    p = Pong()
    p.run()

if __name__ == "__main__":
    main()
