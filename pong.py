#!/usr/bin/env python
# pong game

import pygame

import config


class Pong:
    def __init__(self):
        self.playing = True
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
            if key == pygame.K_UP:
                print "up"
            elif key == pygame.K_DOWN:
                print "down"
            # ai
            # sprites
            # screen update, flip
#            print self

    def quit(self):
        self.playing = False

    def __str__(self):
        return str(self.playing)


def main():
    p = Pong()
    p.run()

if __name__ == "__main__":
    main()
