import pygame
from helper_functions import *
import random
import math
import itertools
import sys

pygame.init()

x_win = pygame.display.get_window_size()[0]
y_win = pygame.display.get_window_size()[1]

circle_radius = 100
# if numBubbles increases past ~20, program has too much delay to have clear fps
numBubbles = 10

bubbleList = list()


class Bubble():
    """
    This class initializes a bubble and contains getter and setter methods as well as createCircle() and move().
    """

    def __init__(self, x: float, y: float, x_rate: float, y_rate: float, color: tuple, radius: float):
        """
        Initializes the bubble

        Args:
            x (float): x position (center of bubble)
            y (float): y position (center of bubble)
            x_rate (float): x speed
            y_rate (float): y speed
            color (tuple): rgb color
            radius (float): radius of bubble
        """
        self.x = x
        self.y = y
        self.x_rate = x_rate
        self.y_rate = y_rate
        self.color = color
        self.circle_radius = radius

    def getX(self):
        """
        Getter for x position

        Returns:
            float: x position
        """
        return self.x

    def getY(self):
        """
        Getter for y position

        Returns:
            float: y position
        """
        return self.y

    def getXRate(self):
        """
        Getter for x speed

        Returns:
            float: x speed
        """
        return self.x_rate

    def getYRate(self):
        """
        Getter for y speed

        Returns:
            float: y speed
        """
        return self.y_rate

    def getColor(self):
        """
        Getter for color

        Returns:
            tuple: color
        """
        return self.color

    def getRadius(self):
        """
        Getter for radius

        Returns:
            float: radius of bubble
        """
        return self.circle_radius

    def createCircle(self):
        """
        Creates the circle object
        """
        create_circle(self.color, (self.x, self.y), self.circle_radius)

    def move(self):
        """
        Moves the bubble one step and checks if the bubble has hit the edge of the border
        """
        self.x = self.x_rate + self.x
        self.y = self.y_rate + self.y

        # check if hit border
        if self.x > x_win or self.x < 0:
            self.x_rate = -self.x_rate
        if self.y > y_win or self.y < 0:
            self.y_rate = -self.y_rate

    def setXRate(self, rate: float):
        """
        Setter method for x speed

        Args:
            rate (float): new x speed
        """
        self.x_rate = rate

    def setYRate(self, rate: float):
        """
        Setter method for y speed

        Args:
            rate (float): new y speed
        """
        self.y_rate = rate


class Collision():
    """
    Takes in a list of bubble objects and determines if they collided. If so, changes the speed of the bubbles. 
    """

    def __init__(self, bubbles: list):
        """
        Initializes the list of bubbles into a dictionary.

        Args:
            bubbles (list): list of bubble objects
        """
        self.bubbledict = dict()
        self.bubbles = bubbles
        for count, bubble in enumerate(bubbles):
            self.bubbledict[count] = bubble

    def checkCollision(self):
        """
        Checks all combinations of bubbles (bubble size choose 2) and determines if they have a collision.

        Returns:
            boolean: true if there was a collision, false if there was not
        """
        collision = False
        for L in range(len(self.bubbles) + 1):
            for subset in itertools.combinations(self.bubbles, L):
                if len(subset) == 2:  # choose 2 loop
                    i = self.bubbles.index(subset[0])  # first index
                    j = self.bubbles.index(subset[1])  # second index

                    x1 = self.bubbledict[i].getX()
                    y1 = self.bubbledict[i].getY()
                    x1_rate = self.bubbledict[i].getXRate()
                    y1_rate = self.bubbledict[i].getYRate()
                    x2 = self.bubbledict[j].getX()
                    y2 = self.bubbledict[j].getY()
                    x2_rate = self.bubbledict[j].getXRate()
                    y2_rate = self.bubbledict[j].getYRate()

                    distance_between = math.sqrt(
                        abs(x1 - x2)**2 + abs(y1 - y2)**2)

                    if distance_between < 2*circle_radius:
                        self.bubbledict[i].setXRate(-x2_rate)
                        self.bubbledict[i].setYRate(-y2_rate)
                        self.bubbledict[j].setXRate(x1_rate)
                        self.bubbledict[j].setYRate(y1_rate)
                        collision = True

        return collision


# Bubble format --> (x, y, x_rate, y_rate, color, radius)
count = 0
while count < 1000:  # iterate until bubbles do not have a collision
    for i in range(numBubbles):
        bubble = Bubble(random.randint(0, x_win), random.randint(0, y_win), random.randrange(5, 25) / 100, random.randrange(5, 25) / 100,
                        (random.randint(1, 255), random.randint(1, 255), random.randint(1, 255)), circle_radius)
        bubbleList.append(bubble)

    collision = Collision(bubbleList)
    if not collision.checkCollision():  # if no collision, break loop and begin movement
        break
    else:
        bubbleList.clear()
    count += 1
    print("Attempt number:", count)
if count == 1000:
    sys.exit("Too many iterations. Change numBubbles or circle_radius and retry.")


running = True
while running:
    screen.fill((0, 0, 0))  # resets screen to black background

    for bubble in bubbleList:  # creates the bubble and moves it
        bubble.createCircle()
        bubble.move()

    collision.checkCollision()  # checks if there is a collision

    pygame.display.update()  # updates screen

    if left_click():  # exits loop if left button is clicked
        running = False


pygame.quit()
