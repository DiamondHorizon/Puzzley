# Imports
import pygame
import sys

# Constants

# Color Constants
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
MAGENTA = (255, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
ORANGE = (255, 165, 0)
PINK = (255, 0, 165)
PURPLE = (145, 0, 255)
GRAY = (128, 128, 128)

TICKSPEED = 0
MONTHS = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]

# Dimensions Constants
BIG = True
if BIG:
    TILE_SIZE = 64
else:
    TILE_SIZE = 32
MARGIN = 20
SCREEN_WIDTH = (TILE_SIZE) * 7 + (MARGIN * 2)
SCREEN_HEIGHT = SCREEN_WIDTH
BUTTON_WIDTH = 200

# Window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Calander Puzzle")
pygame.init()

pieceU = [ # 4 total
    [1, 0, 1, 0,
     1, 1, 1, 0,
     0, 0, 0, 0,
     0, 0, 0, 0],
    [1, 1, 0, 0,
     1, 0, 0, 0,
     1, 1, 0, 0,
     0, 0, 0, 0],
    [1, 1, 1, 0,
     1, 0, 1, 0,
     0, 0, 0, 0,
     0, 0, 0, 0],
    [1, 1, 0, 0,
     0, 1, 0, 0,
     1, 1, 0, 0,
     0, 0, 0, 0]]

pieceL = [ # 8 total
    [1, 0, 0, 0,
     1, 0, 0, 0,
     1, 0, 0, 0,
     1, 1, 0, 0],
    [1, 1, 1, 1,
     1, 0, 0, 0,
     0, 0, 0, 0,
     0, 0, 0, 0],
    [1, 1, 0, 0,
     0, 1, 0, 0,
     0, 1, 0, 0,
     0, 1, 0, 0],
    [0, 0, 0, 1,
     1, 1, 1, 1,
     0, 0, 0, 0,
     0, 0, 0, 0],
    [0, 1, 0, 0,
     0, 1, 0, 0,
     0, 1, 0, 0,
     1, 1, 0, 0],
    [1, 0, 0, 0,
     1, 1, 1, 1,
     0, 0, 0, 0,
     0, 0, 0, 0],
    [1, 1, 0, 0,
     1, 0, 0, 0,
     1, 0, 0, 0,
     1, 0, 0, 0],
    [1, 1, 1, 1,
     0, 0, 0, 1,
     0, 0, 0, 0,
     0, 0, 0, 0]]

pieceZigZag = [ # 8 total
    [0, 1, 0, 0,
     1, 1, 0, 0,
     1, 0, 0, 0,
     1, 0, 0, 0],
    [1, 1, 1, 0,
     0, 0, 1, 1,
     0, 0, 0, 0,
     0, 0, 0, 0],
    [0, 1, 0, 0,
     0, 1, 0, 0,
     1, 1, 0, 0,
     1, 0, 0, 0],
    [1, 1, 0, 0,
     0, 1, 1, 1,
     0, 0, 0, 0,
     0, 0, 0, 0],
    [1, 0, 0, 0,
     1, 1, 0, 0,
     0, 1, 0, 0,
     0, 1, 0, 0],
    [0, 0, 1, 1,
     1, 1, 1, 0,
     0, 0, 0, 0,
     0, 0, 0, 0],
    [1, 0, 0, 0,
     1, 0, 0, 0,
     1, 1, 0, 0,
     0, 1, 0, 0],
    [0, 1, 1, 1,
     1, 1, 0, 0,
     0, 0, 0, 0,
     0, 0, 0, 0]]

pieceCorner = [ # 4 total
    [1, 0, 0, 0,
     1, 0, 0, 0,
     1, 1, 1, 0,
     0, 0, 0, 0],
    [1, 1, 1, 0,
     1, 0, 0, 0,
     1, 0, 0, 0,
     0, 0, 0, 0],
    [1, 1, 1, 0,
     0, 0, 1, 0,
     0, 0, 1, 0,
     0, 0, 0, 0],
    [0, 0, 1, 0,
     0, 0, 1, 0,
     1, 1, 1, 0,
     0, 0, 0, 0]]

pieceZ = [ # 4 total
    [0, 1, 1, 0,
    0, 1, 0, 0,
    1, 1, 0, 0,
    0, 0, 0, 0],
    [1, 0, 0, 0,
    1, 1, 1, 0,
    0, 0, 1, 0,
    0, 0, 0, 0],
    [1, 1, 0, 0,
    0, 1, 0, 0,
    0, 1, 1, 0,
    0, 0, 0, 0],
    [0, 0, 1, 0,
    1, 1, 1, 0,
    1, 0, 0, 0,
    0, 0, 0, 0]]

pieceRectangle = [ # 2 total
    [1, 1, 1, 0,
    1, 1, 1, 0,
    0, 0, 0, 0,
    0, 0, 0, 0],
    [1, 1, 0, 0,
    1, 1, 0, 0,
    1, 1, 0, 0,
    0, 0, 0, 0]]

piecePointer = [ # 8 total
    [1, 1, 1, 0,
     1, 1, 0, 0,
     0, 0, 0, 0,
     0, 0, 0, 0],
    [1, 1, 0, 0,
     1, 1, 0, 0,
     0, 1, 0, 0,
     0, 0, 0, 0],
    [0, 1, 1, 0,
     1, 1, 1, 0,
     0, 0, 0, 0,
     0, 0, 0, 0],
    [1, 0, 0, 0,
     1, 1, 0, 0,
     1, 1, 0, 0,
     0, 0, 0, 0],
    [1, 1, 0, 0,
     1, 1, 1, 0,
     0, 0, 0, 0,
     0, 0, 0, 0],
    [1, 1, 0, 0,
     1, 1, 0, 0,
     1, 0, 0, 0,
     0, 0, 0, 0],
    [1, 1, 1, 0,
     0, 1, 1, 0,
     0, 0, 0, 0,
     0, 0, 0, 0],
    [0, 1, 0, 0,
     1, 1, 0, 0,
     1, 1, 0, 0,
     0, 0, 0, 0]]

pieceArm = [ # 8 total
    [1, 1, 1, 1,
     0, 1, 0, 0,
     0, 0, 0, 0,
     0, 0, 0, 0],
    [0, 1, 0, 0,
     1, 1, 0, 0,
     0, 1, 0, 0,
    0, 1, 0, 0],
    [0, 0, 1, 0,
     1, 1, 1, 1,
     0, 0, 0, 0,
     0, 0, 0, 0],
    [1, 0, 0, 0,
     1, 0, 0, 0,
     1, 1, 0, 0,
     1, 0, 0, 0],
    [1, 1, 1, 1,
     0, 0, 1, 0,
     0, 0, 0, 0,
     0, 0, 0, 0],
    [0, 1, 0, 0,
     0, 1, 0, 0,
     1, 1, 0, 0,
     0, 1, 0, 0],
    [0, 1, 0, 0,
     1, 1, 1, 1,
     0, 0, 0, 0,
     0, 0, 0, 0],
    [1, 0, 0, 0,
     1, 1, 0, 0,
     1, 0, 0, 0,
     1, 0, 0, 0]]

# Classes
class Button():
    def __init__(self, x, y, width, height, text):
        self.rect = pygame.Rect(x, y, width, height)
        self.clicked = False
        self.selected = False
        # Setup text
        font = pygame.font.SysFont('timesnewroman', 25, bold = True)
        self.text = font.render(text, True, BLUE)

    def draw(self, screen, text=None):
        pygame.draw.rect(screen, GREEN, self.rect)
        action = False
        # Get mouse position
        pos = pygame.mouse.get_pos()

        # Check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            pygame.draw.rect(screen, MAGENTA, self.rect)
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        # Draw determine text to use
        if text != None:
            # Setup text
            font = pygame.font.SysFont('timesnewroman', 25, bold = True)
            self.text = font.render(text, True, BLUE)

        # Draw button on screen
        screen.blit(self.text, (self.rect.x / 2 + self.rect.width / 2, self.rect.y + self.rect.height / 2))


        return action
    
    def select(self, screen, type="day"):
        global monthSelected
        global daySelected
        if not self.selected:
            pygame.draw.rect(screen, GREEN, self.rect)
        else:
            pygame.draw.rect(screen, ORANGE, self.rect)
        action = False
        # Get mouse position
        pos = pygame.mouse.get_pos()

        # Check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            pygame.draw.rect(screen, MAGENTA, self.rect)
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
                if type == "month":
                    if monthSelected != None:
                        monthSelected.selected = False
                    monthSelected = self
                else:
                    if daySelected != None:
                        daySelected.selected = False
                    daySelected = self
                self.selected = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        # Draw button on screen
        screen.blit(self.text, self.rect)#(self.rect.x / 2 + self.rect.width / 2, self.rect.y + self.rect.height / 2))


        return action

# Methods
def output(string, x, y, fontSize=25, highlight=None):
    font = pygame.font.SysFont('timesnewroman', int(fontSize), bold = True)

    text = font.render(string, True, BLACK, highlight)

    screen.blit(text, (x, y))

def drawMap():
    global map
    x = TILE_SIZE 
    y = TILE_SIZE / 2 + TILE_SIZE / 4
    factor = 6
    row = 0
    col = 0
    for i in range(len(map)):
        rect = pygame.Rect(MARGIN + (row * TILE_SIZE), MARGIN + (col * TILE_SIZE), TILE_SIZE, TILE_SIZE)
        pygame.draw.rect(screen, map[i], rect)
        if BIG:
            if i < 13:
                output(MONTHS[i], x - (TILE_SIZE * .6), y + (TILE_SIZE * .15), TILE_SIZE * .4)
            elif i > 13 and i < 45:
                output(str(i - 13), x - (TILE_SIZE * .2), y, TILE_SIZE * .5)
        else:
            if i < 13:
                output(MONTHS[i], x - (TILE_SIZE * .27), y + (TILE_SIZE * .4), TILE_SIZE * .4)
            elif i > 13 and i < 45:
                output(str(i - 13), x + (TILE_SIZE * .1), y + (TILE_SIZE * .3), TILE_SIZE / 2)
        pygame.display.update() # Update the display
        
        row +=1
        if (i % factor) == 0 and i != 0:
            y += TILE_SIZE
            col += 1
            row = 0
            x = TILE_SIZE
            factor += 7
        else:
            x += TILE_SIZE

def printMap():
    global map
    output = ""
    factor = 6
    for i in range(len(map)):
        output += str(map[i]) + " "

        if (i % factor) == 0 and i != 0:
            # print(output)
            output = ""
            factor += 7
    # print("\n")

def reset():
    # Draw picture
    screen.fill(BLACK)
    border = pygame.Rect(MARGIN - (TILE_SIZE / 8), MARGIN - (TILE_SIZE / 8), (TILE_SIZE * 7) + 2 * (TILE_SIZE / 8), (TILE_SIZE * 7) + 2 * (TILE_SIZE / 8))
    openSpace = pygame.Rect(MARGIN, MARGIN, TILE_SIZE * 7, TILE_SIZE * 7)
    topCorner = pygame.Rect(MARGIN + (TILE_SIZE * 6), MARGIN, TILE_SIZE * 1, TILE_SIZE * 2)
    bottomCorner = pygame.Rect(MARGIN + (TILE_SIZE * 3), MARGIN + (TILE_SIZE * 6), TILE_SIZE * 4, TILE_SIZE * 1)
    pygame.draw.rect(screen, BLUE, border)
    pygame.draw.rect(screen, BLACK, openSpace)
    pygame.draw.rect(screen, BLUE,  topCorner)
    pygame.draw.rect(screen, BLUE,  bottomCorner)

    # Set variables
    global map
    global colorList
    global pieceList
    global placedPieces
    global placedStart
    global map
    global placedPieceTypes
    global placedPieceOrientaions
    placedPieces = []
    placedStart = []
    placedPieceTypes = []
    placedPieceOrientaions = []

    # Setup map
    map = [BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLUE,
           BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLUE,
           BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK,
           BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK,
           BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK,
           BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK,
           BLACK, BLACK, BLACK, BLUE, BLUE, BLUE, BLUE]
    if month < 7:
        map[month - 1] = PURPLE
    else:
        map[month] = PURPLE

    map[day + 13] = PURPLE

    # Setup pieceList array
    pieceList = [pieceU, pieceL, pieceArm, pieceCorner, piecePointer, pieceRectangle, pieceZ, pieceZigZag]
    pieceList = [piecePointer, pieceU, pieceZ, pieceL, pieceZigZag, pieceArm, pieceRectangle, pieceCorner]
    colorList = [PINK, RED, GREEN, WHITE, YELLOW, MAGENTA, CYAN, ORANGE]

    drawMap()

def findStart():
    global map
    for i in range(len(map)):
        if map[i] == BLACK:
            return i
    return -1

def getPlaceableOrientations():
    global pieceList
    global map
    placeables = []
    for piece in pieceList:
        for orientation in piece:
            start = findStart()
            if start == -1:
                return -1
            row = 0
            col = 0
            failed = False
            backwards = 0
            for i in range(len(orientation)):
                if orientation[i] == 1:
                    if i > 0:
                        backwards = i
                    break
            # Shift backwards if applicable
            if (start - backwards) >= 0:
                start -= backwards
            for i in range(len(orientation)):
                spot = orientation[i]
                # Check for wrap-around
                if i > 0 and row > 0 and spot == 1 and ((row + start) % 7) == 0:
                    failed = True
                if spot == 1 and (start + row + col) <= len(map) - 1 and map[start + row + col] == BLACK:
                    row += 1
                elif spot == 0:
                    row += 1
                else: # If any spot collides...
                    failed = True

                # Check for next column
                if (row % 4) == 0:
                    col += 7
                    row = 0
            if not failed:
                placeables.append(orientation)
    return placeables
        
def placePiece(piece):
    global map
    global colorList
    global pieceList
    global placedPieceTypes
    global placedStart
    global placedPieceOrientaions
    global visual
    start = findStart()
    row = 0
    col = 0
    backwards = 0
    for i in range(len(piece)):
        if piece[i] == 1:
            if i > 0:
                backwards = i
            break
    # Shift backwards if applicable
    if (start - backwards) >= 0:
        start -= backwards
    for spot in piece:
        if spot == 1:
            map[start + row + col] = colorList[8 - len(pieceList)]
        row += 1
        if (row % 4) == 0:
            col += 7
            row = 0

    if visual:
        drawMap()
    for pieceType in pieceList:
        for orientation in pieceType:
            if orientation == piece:
                pieceList.remove(pieceType)
                placedPieceTypes.append(pieceType)
                placedPieceOrientaions.append(piece)
                placedStart.append(start)

def undoPlace():
    global placedPieceTypes
    global pieceList
    global placedStart
    global visual
    start = placedStart[len(placedStart) - 1]
    pieceType = placedPieceTypes[len(placedPieceTypes) - 1]
    piece = placedPieceOrientaions[len(placedPieceOrientaions) - 1]
    row = 0
    col = 0
    for spot in piece:
        if spot == 1:
            map[start + row + col] = BLACK
        row += 1
        if (row % 4) == 0:
            col += 7
            row = 0
    
    if visual:
        drawMap()
    pieceList.append(pieceType)
    placedPieceOrientaions.remove(piece)
    placedStart.remove(start)
    placedPieceTypes.remove(pieceType)

def findNextPiece(depth=1):
    placeables = getPlaceableOrientations()
    if placeables == -1:
        return True
    if len(placeables) > 0:
        for piece in placeables:
            placePiece(piece)
            if findNextPiece(depth + 1):
                return True
        undoPlace()
    else:
        if len(pieceList) > 0:
            undoPlace()
        else:
            return True

def toggleSpeed():
    global visual
    if visual:
        visual = False
        speedButton.draw(screen, "Instant")
    else:
        visual = True
        speedButton.draw(screen, "Visual")

running = True
gameState = "menu"
global visual
visual = False
global monthSelected
global daySelected
monthSelected = None
daySelected = None
month = 1
day = 1
# Create button instances
runButton = Button(SCREEN_WIDTH / 2 - (BUTTON_WIDTH / 2), MARGIN, BUTTON_WIDTH, BUTTON_WIDTH / 2, "Run")
speedButton = Button(SCREEN_WIDTH / 2 - (BUTTON_WIDTH / 2), MARGIN * 2 + (BUTTON_WIDTH / 2), BUTTON_WIDTH, BUTTON_WIDTH / 2, "Instant")
exitButton = Button(SCREEN_WIDTH / 2 - (BUTTON_WIDTH / 2), MARGIN * 3 + BUTTON_WIDTH, BUTTON_WIDTH, BUTTON_WIDTH / 2, "Exit")

janButton = Button(MARGIN, MARGIN, TILE_SIZE, TILE_SIZE, MONTHS[0])
febButton = Button(MARGIN + TILE_SIZE, MARGIN, TILE_SIZE, TILE_SIZE, MONTHS[1])
marButton = Button(MARGIN + (2 * TILE_SIZE), MARGIN, TILE_SIZE, TILE_SIZE, MONTHS[2])
aprButton = Button(MARGIN + (3 * TILE_SIZE), MARGIN, TILE_SIZE, TILE_SIZE, MONTHS[3])
mayButton = Button(MARGIN + (4 * TILE_SIZE), MARGIN, TILE_SIZE, TILE_SIZE, MONTHS[4])
junButton = Button(MARGIN + (5 * TILE_SIZE), MARGIN, TILE_SIZE, TILE_SIZE, MONTHS[5])
julButton = Button(MARGIN, MARGIN + TILE_SIZE, TILE_SIZE, TILE_SIZE, MONTHS[7])
augButton = Button(MARGIN + TILE_SIZE, MARGIN + TILE_SIZE, TILE_SIZE, TILE_SIZE, MONTHS[8])
sepButton = Button(MARGIN + (2 * TILE_SIZE), MARGIN + TILE_SIZE, TILE_SIZE, TILE_SIZE, MONTHS[9])
octButton = Button(MARGIN + (3 * TILE_SIZE), MARGIN + TILE_SIZE, TILE_SIZE, TILE_SIZE, MONTHS[10])
novButton = Button(MARGIN + (4 * TILE_SIZE), MARGIN + TILE_SIZE, TILE_SIZE, TILE_SIZE, MONTHS[11])
decButton = Button(MARGIN + (5 * TILE_SIZE), MARGIN + TILE_SIZE, TILE_SIZE, TILE_SIZE, MONTHS[12])
button1 = Button(MARGIN, MARGIN + (2 * TILE_SIZE), TILE_SIZE, TILE_SIZE, "1")
button2 = Button(MARGIN + TILE_SIZE, MARGIN + (2 * TILE_SIZE), TILE_SIZE, TILE_SIZE, "2")
button3 = Button(MARGIN + (2 * TILE_SIZE), MARGIN + (2 * TILE_SIZE), TILE_SIZE, TILE_SIZE, "3")
button4 = Button(MARGIN + (3 * TILE_SIZE), MARGIN + (2 * TILE_SIZE), TILE_SIZE, TILE_SIZE, "4")
button5 = Button(MARGIN + (4 * TILE_SIZE), MARGIN + (2 * TILE_SIZE), TILE_SIZE, TILE_SIZE, "5")
button6 = Button(MARGIN + (5 * TILE_SIZE), MARGIN + (2 * TILE_SIZE), TILE_SIZE, TILE_SIZE, "6")
button7 = Button(MARGIN + (6 * TILE_SIZE), MARGIN + (2 * TILE_SIZE), TILE_SIZE, TILE_SIZE, "7")
button8 = Button(MARGIN, MARGIN + (3 * TILE_SIZE), TILE_SIZE, TILE_SIZE, "8")
button9 = Button(MARGIN + TILE_SIZE, MARGIN + (3 * TILE_SIZE), TILE_SIZE, TILE_SIZE, "9")
button10 = Button(MARGIN + (2 * TILE_SIZE), MARGIN + (3 * TILE_SIZE), TILE_SIZE, TILE_SIZE, "10")
button11 = Button(MARGIN + (3 * TILE_SIZE), MARGIN + (3 * TILE_SIZE), TILE_SIZE, TILE_SIZE, "11")
button12 = Button(MARGIN + (4 * TILE_SIZE), MARGIN + (3 * TILE_SIZE), TILE_SIZE, TILE_SIZE, "12")
button13 = Button(MARGIN + (5 * TILE_SIZE), MARGIN + (3 * TILE_SIZE), TILE_SIZE, TILE_SIZE, "13")
button14 = Button(MARGIN + (6 * TILE_SIZE), MARGIN + (3 * TILE_SIZE), TILE_SIZE, TILE_SIZE, "14")
button15 = Button(MARGIN, MARGIN + (4 * TILE_SIZE), TILE_SIZE, TILE_SIZE, "15")
button16 = Button(MARGIN + TILE_SIZE, MARGIN + (4 * TILE_SIZE), TILE_SIZE, TILE_SIZE, "16")
button17 = Button(MARGIN + (2 * TILE_SIZE), MARGIN + (4 * TILE_SIZE), TILE_SIZE, TILE_SIZE, "17")
button18 = Button(MARGIN + (3 * TILE_SIZE), MARGIN + (4 * TILE_SIZE), TILE_SIZE, TILE_SIZE, "18")
button19 = Button(MARGIN + (4 * TILE_SIZE), MARGIN + (4 * TILE_SIZE), TILE_SIZE, TILE_SIZE, "19")
button20 = Button(MARGIN + (5 * TILE_SIZE), MARGIN + (4 * TILE_SIZE), TILE_SIZE, TILE_SIZE, "20")
button21 = Button(MARGIN + (6 * TILE_SIZE), MARGIN + (4 * TILE_SIZE), TILE_SIZE, TILE_SIZE, "21")
button22 = Button(MARGIN, MARGIN + (5 * TILE_SIZE), TILE_SIZE, TILE_SIZE, "22")
button23 = Button(MARGIN + TILE_SIZE, MARGIN + (5 * TILE_SIZE), TILE_SIZE, TILE_SIZE, "23")
button24 = Button(MARGIN + (2 * TILE_SIZE), MARGIN + (5 * TILE_SIZE), TILE_SIZE, TILE_SIZE, "24")
button25 = Button(MARGIN + (3 * TILE_SIZE), MARGIN + (5 * TILE_SIZE), TILE_SIZE, TILE_SIZE, "25")
button26 = Button(MARGIN + (4 * TILE_SIZE), MARGIN + (5 * TILE_SIZE), TILE_SIZE, TILE_SIZE, "26")
button27 = Button(MARGIN + (5 * TILE_SIZE), MARGIN + (5 * TILE_SIZE), TILE_SIZE, TILE_SIZE, "27")
button28 = Button(MARGIN + (6 * TILE_SIZE), MARGIN + (5 * TILE_SIZE), TILE_SIZE, TILE_SIZE, "28")
button29 = Button(MARGIN, MARGIN + (6 * TILE_SIZE), TILE_SIZE, TILE_SIZE, "29")
button30 = Button(MARGIN + TILE_SIZE, MARGIN + (6 * TILE_SIZE), TILE_SIZE, TILE_SIZE, "30")
button31 = Button(MARGIN + (2 * TILE_SIZE), MARGIN + (6 * TILE_SIZE), TILE_SIZE, TILE_SIZE, "31")

while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if gameState == "running":
                    gameState = "menu"
                    reset()
                    screen.fill(BLACK)
                else:
                    gameState = "running"
                    done = False
                    reset()
        if event.type == pygame.QUIT:
            running = False

    if gameState == "menu":
        # Draw menu buttons and run what they do
        if speedButton.draw(screen):
            toggleSpeed()
        if exitButton.draw(screen):
            running = False
        if runButton.draw(screen):
            gameState = "starting"
            screen.fill(BLACK)
    elif gameState == "starting":
        if janButton.select(screen, "month"):
            month = 1
        if febButton.select(screen, "month"):
            month = 2
        if marButton.select(screen, "month"):
            month = 3
        if aprButton.select(screen, "month"):
            month = 4
        if mayButton.select(screen, "month"):
            month = 5
        if junButton.select(screen, "month"):
            month = 6
        if julButton.select(screen, "month"):
            month = 7
        if augButton.select(screen, "month"):
            month = 8
        if sepButton.select(screen, "month"):
            month = 9
        if octButton.select(screen, "month"):
            month = 10
        if novButton.select(screen, "month"):
            month = 11
        if decButton.select(screen, "month"):
            month = 12
        if button1.select(screen):
            day = 1
        if button2.select(screen):
            day = 2
        if button3.select(screen):
            day = 3
        if button4.select(screen):
            day = 4
        if button5.select(screen):
            day = 5
        if button6.select(screen):
            day = 6
        if button7.select(screen):
            day = 7
        if button8.select(screen):
            day = 8
        if button9.select(screen):
            day = 9
        if button10.select(screen):
            day = 10
        if button11.select(screen):
            day = 11
        if button12.select(screen):
            day = 12
        if button13.select(screen):
            day = 13
        if button14.select(screen):
            day = 14
        if button15.select(screen):
            day = 15
        if button16.select(screen):
            day = 16
        if button17.select(screen):
            day = 17
        if button18.select(screen):
            day = 18
        if button19.select(screen):
            day = 19
        if button20.select(screen):
            day = 20
        if button21.select(screen):
            day = 21
        if button22.select(screen):
            day = 22
        if button23.select(screen):
            day = 23
        if button24.select(screen):
            day = 24
        if button25.select(screen):
            day = 25
        if button26.select(screen):
            day = 26
        if button27.select(screen):
            day = 27
        if button28.select(screen):
            day = 28
        if button29.select(screen):
            day = 29
        if button30.select(screen):
            day = 30
        if button31.select(screen):
            day = 31
    else:
        # Game logic and drawing code goes here
        if not done:
            pygame.display.update() # Update the display
            if findNextPiece():
                done = True
                drawMap()
    
    pygame.display.update() # Update the display

# Run after window is closed
pygame.quit()
sys.exit()