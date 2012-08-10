##############################################
#                                            #
#      Author: Richard Ruzsa (develru)       #
#      Email: develru [at] me . com          #
#                                            #
##############################################


import sys
import pygame
import random

from pygame import locals


class Card(object):
    """Represent one card"""
    def __init__(self, shape, color, coords):
        self.__coords = coords
        self.__shape = shape
        self.__color = color
        #TODO: change to False
        self.covered = True

    def draw(self, displaySurf):
        """Dra the card"""
        quarter = int(Game.boxSize * 0.25)
        half = int(Game.boxSize * 0.5)
        left = self.__coords[0]
        top = self.__coords[1]
        if self.covered:
            if self.__shape == Game.donaut:
                pygame.draw.circle(displaySurf, self.__color, (left + half,
                    top + half), half - 5)
                pygame.draw.circle(displaySurf, Game.bgColor, (left + half,
                    top + half), quarter - 5)
            elif self.__shape == Game.square:
                pygame.draw.rect(displaySurf, self.__color, (left + quarter,
                    top + quarter, Game.boxSize - half, Game.boxSize - half))
            elif self.__shape == Game.diamond:
                pygame.draw.polygon(displaySurf, self.__color, ((left + half,
                    top), (left + Game.boxSize - 1, top + half), (left + half,
                        top + Game.boxSize - 1), (left, top + half)))
            elif self.__shape == Game.lines:
                for i in range(0, Game.boxSize, 4):
                    pygame.draw.line(displaySurf, self.__color, (left,
                        top + i), (left + i, top))
                    pygame.draw.line(displaySurf, self.__color, (left + i,
                        top + Game.boxSize - 1), (left + Game.boxSize - 1,
                        top + i))
            elif self.__shape == Game.oval:
                pygame.draw.ellipse(displaySurf, self.__color, (left,
                    top + quarter, Game.boxSize, half))
        else:
            pygame.draw.rect(displaySurf, Game.boxColor, (left, top,
                Game.boxSize, Game.boxSize))


class Game(object):
    windowWidth = 640
    windowHeight = 480
    boxSize = 40
    gapSize = 10
    boardWith = 10
    boardHeight = 7
    assert (boardWith * boardHeight) % 2 == 0, \
            "Board needs to have an even number of boxes for pairs of matches."
    xMargin = int((windowWidth - (boardWith * (boxSize +
        gapSize))) / 2)
    yMargin = int((windowHeight - (boardHeight *
        (boxSize + gapSize))) / 2)
    navyBlue = (60, 60, 100)
    white = (255, 255, 255)
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    yellow = (255, 255, 0)
    orange = (255, 128, 0)
    purple = (255, 0, 255)
    cyan = (0, 255, 255)

    donaut = "donaut"
    square = "square"
    diamond = "diamond"
    lines = "lines"
    oval = "oval"

    bgColor = navyBlue
    boxColor = white
    allColors = (red, green, blue, yellow,
            orange, purple, cyan)
    allShapes = (donaut, square, diamond, lines,
            oval)
    assert len(allColors) * len(allShapes) * 2 >= boardWith \
            * boardHeight, " Board is too big for the number of \
            shapes/colors defined"

    def __init__(self):
        """docstring for __init__"""

        self.__cards = self.getRandomizedCards()

        self.displaySurf = pygame.display.set_mode((Game.windowWidth,
            Game.windowHeight))
        Game.fpsClock = pygame.time.Clock()

    def getRandomizedCards(self):
        """Return the random list of the Cards"""
        icons = []
        for color in Game.allColors:
            for shape in Game.allShapes:
                icons.append((shape, color))

        random.shuffle(icons)
        numIconUsed = int(Game.boardWith * Game.boardHeight / 2)
        icons = icons[:numIconUsed] * 2
        random.shuffle(icons)

        cards = []
        ind = 0
        for icon in icons:
            #ind = icons.index(icon)
            boxX = ind / Game.boardHeight
            boxY = ind % Game.boardHeight
            left, top = self.leftTopCoordsOfCard(boxX, boxY)
            cards.append(Card(icon[0], icon[1], (left, top)))
            ind += 1

        return cards

    def leftTopCoordsOfCard(self, boxX, boxY):
        """Return with the real coordinates of the cards"""
        left = boxX * (Game.boxSize + Game.gapSize) + Game.xMargin
        top = boxY * (Game.boxSize + Game.gapSize) + Game.yMargin
        return (left, top)

    def update(self):
        """Update the game graphic"""
        for card in self.__cards:
            card.draw(self.displaySurf)

    def main(self):
        """docstring for main"""
        pygame.init()
        self.displaySurf.fill(Game.bgColor)
        while True:
            self.displaySurf.fill(Game.bgColor)
            self.update()
            for event in pygame.event.get():
                if event.type == locals.QUIT or (event.type == locals.KEYDOWN
                        and event.key == locals.K_ESCAPE):
                    pygame.quit()
                    return

            pygame.display.flip()
            Game.fpsClock.tick(30)


if __name__ == '__main__':
    #pygame.init()
    game = Game()
    game.main()
    sys.exit()
