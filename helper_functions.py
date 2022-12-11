import pygame

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen.fill((0, 0, 0))  # resets screen to black background


def left_click():
    """
    Checks if the left button on the mouse is pressed. 

    Returns:
        boolean: if clicked, returns true. Else, returns false.
    """
    event_list = pygame.event.get()
    for event in event_list:
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0] is True:
                return True
    return False


def create_circle(color: tuple, center_coords: tuple, radius):
    """
    Uses pygame's draw.circle() function to create a circle. 

    Args:
        color (tuple): color of the circle
        center_coords (tuple): (x, y) coords of the circle
        radius (float): radius of the circle

    Returns:
        tuple: contains x and y coordinates of the circle enclosed by a rectangle. 
    """
    rect = pygame.draw.circle(screen, color, center_coords, radius)
    pygame.draw.circle(screen, (0, 0, 0), center_coords, radius * 14/15)
    return rect
