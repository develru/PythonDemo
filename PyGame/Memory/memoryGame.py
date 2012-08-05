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


windowWidth = 640
windowHeight = 480
fps = 30
boxSize = 40
gapSize = 10
boardWith = 10
boardHeight = 7
assert (boardWith * boardHeight) % 2 == 0, \
    "Board needs to have an even number of boxes for pairs of matches."
xMargin = int((windowWidth - (boardWith * (boxSize + gapSize))) / 2)
yMargin = int((windowHeight - (boardHeight * (boxSize + gapSize))) / 2)

navyBlue = (60, 60, 100)
gray = (100, 100, 100)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
orange = (255, 128, 0)
purple = (255, 0, 255)
cyan = (0, 255, 255)

bgColor = navyBlue
boxColor = white

donut = "donut"
square = "square"
diamond = "diamond"
lines = "lines"
oval = "oval"

allColors = (red, green, blue, yellow, orange, purple, cyan)
allShapes = (donut, square, diamond, lines, oval)
assert len(allColors) * len(allShapes) * 2 >= boardWith * boardHeight, \
        "Board is too big for the number of shapes/colors defined."

#fpsClock = None
#displaySurf = None
fpsClock = pygame.time.Clock()
displaySurf = pygame.display.set_mode((windowWidth, windowHeight))


def main():
    """ The main function of the game """
    #global fpsClock, displaySurf
    pygame.init()
#    fpsClock = pygame.time.Clock()
#    displaySurf = pygame.display.set_mode((windowWidth, windowHeight))

    iMousex = 0
    iMousey = 0
    pygame.display.set_caption("Memory Game")

    mainBoard = getRandomizedBoard()
    revealedBoxes = generateRevealedBoxesData(False)

    firstSelection = None

    displaySurf.fill(bgColor)
    startGameAnimation(mainBoard)

    while True:
        mouseClicked = False

        for event in pygame.event.get():
            if event.type == locals.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        fpsClock.tick(fps)


def getRandomizedBoard():
    """ Get a list of every possible shape in every possible color and
    randomized it.
    return with the (list) board """
    icons = []
    for color in allColors:
        for shape in allShapes:
            icons.append((shape, color))

    random.shuffle(icons)
    numIconUsed = int(boardWith * boardHeight / 2)
    icons = icons[:numIconUsed] * 2
    random.shuffle(icons)

    board = []
    for x in range(boardWith):
        column = []
        for y in range(boardHeight):
            # TODO: remove deletion
            column.append(icons[0])
            del icons[0]
        board.append(column)

    return board


def generateRevealedBoxesData(isValid):
    """Generate the revealed boxes with the value 'isValid' and return the
    list of boxes"""
    revealedBoxes = []
    for i in range(boardWith):
        revealedBoxes.append([isValid] * boardHeight)

    return revealedBoxes


def startGameAnimation(board):
    """Start the game animation"""
    coveredBoxes = generateRevealedBoxesData(True)
    boxes = []
    for x in range(boardWith):
        for y in range(boardHeight):
            boxes.append((x, y))
    random.shuffle(boxes)
    boxGroups = splitIntoGroupsOf(8, boxes)

    drawBoard(board, coveredBoxes)


def drawBoard(board, revealed):
    """Draws all of the boxes in their covered or revealed state."""
    for boxX in range(boardWith):
        for boxY in range(boardHeight):
            left, top = leftTopCoordsOfBox(boxX, boxY)
            if not revealed[boxX][boxY]:
                pygame.draw.rect(displaySurf, boxColor, (left, top, boxSize,
                    boxSize))
            else:
                shape, color = getShapeAndColor(board, boxX, boxY)
                drawIcon(shape, color, boxX, boxY)


def splitIntoGroupsOf(groupSize, theList):
    """Splits a list into a list of list, where the inner list have at most
    'groupSize' number of itemsself."""
    result = []
    for i in range(0, len(theList), groupSize):
        result.append(theList[i:i + groupSize])

    return result


def leftTopCoordsOfBox(boxX, boxY):
    """Convert board coordinates to pixel coordinates"""
    left = boxX * (boxSize + gapSize) + xMargin
    top = boxY * (boxSize + gapSize) + yMargin

    return (left, top)


def getShapeAndColor(board, boxX, boxY):
    """Shape value for x, y spot"""
    return board[boxX][boxY][0], board[boxX][boxY][1]


def drawIcon(shape, color, boxX, boxY):
    """Drow the shape"""
    quarter = int(boxSize * 0.25)
    half = int(boxSize * 0.5)
    left, top = leftTopCoordsOfBox(boxX, boxY)

    if shape == donut:
        pygame.draw.circle(displaySurf, color, (left + half, top + half),
                half - 5)
        pygame.draw.circle(displaySurf, bgColor, (left + half, top + half),
                quarter - 5)

if __name__ == "__main__":
    main()
