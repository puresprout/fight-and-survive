#!/usr/bin/env python

import pygame as pg

SCREEN_RECT = pg.Rect(0, 0, 640, 480)


def main():
    pg.init()

    fullscreen = False

    win_style = 0
    best_depth = pg.display.mode_ok(SCREEN_RECT.size, win_style, 32)
    screen = pg.display.set_mode(SCREEN_RECT.size, win_style, best_depth)

    pg.display.set_caption("Fight and Survive")

    clock = pg.time.Clock()

    end = False

    while not end:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
            if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                return
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_f:
                    if not fullscreen:
                        screen_backup = screen.copy()
                        screen = pg.display.set_mode(
                            SCREEN_RECT.size, win_style | pg.FULLSCREEN, best_depth
                        )
                        screen.blit(screen_backup, (0, 0))
                    else:
                        screen_backup = screen.copy()
                        screen = pg.display.set_mode(
                            SCREEN_RECT.size, win_style, best_depth
                        )
                        screen.blit(screen_backup, (0, 0))

                    pg.display.flip()
                    fullscreen = not fullscreen

        clock.tick(40)

    pg.time.wait(1000)


if __name__ == "__main__":
    main()
    pg.quit()
