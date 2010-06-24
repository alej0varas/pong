#!/usr/bin/env python
# pong game

import pygame

import config


class Pong:
    def __init__(self):
        self.playing = True
        self.player = Player()
        self.ia = IA()
        pygame.display.init()
        pygame.event.set_allowed(None)
        pygame.event.set_allowed(pygame.KEYDOWN)

    def run(self):
        # display
        pygame.display.set_mode(config.resolution)

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
            # screen update, flip
#            print self

    def quit(self):
        self.playing = False

    def __str__(self):
        return str(self.playing)


class Player:
    def __init__(self):
        self.pad = Pad(self)

    def play(self, key):
        if key == pygame.K_UP:
            self.pad.up()
        elif key == pygame.K_DOWN:
            self.pad.down()


class IA:
    def __init__(self):
        self.pad = Pad(self)
        #super(type(IA), self).__init__()

    def play(self):
        print "ia turn"
        pass


class Pad:
    def __init__(self, owner, x, y):
        self.owner = owner
        self.x = x
        self.y = y
        
    def up(self):
        print "up"

    def down(self):
        print "down"


def main():
    p = Pong()
    p.run()

if __name__ == "__main__":
    main()
