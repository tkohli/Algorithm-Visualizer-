import pygame
import random
pygame.init()


class DrawInformation:
    BLACK = 0, 0, 0
    WHITE = 255, 255, 255
    GREEN = 0, 255, 0
    RED = 255, 0, 0
    GREY = 128, 128, 128
    BACKGROUND_COLOR = WHITE

    GRADIENTS = [
        (128, 128, 128),
        (160, 160, 160),
        (192, 192, 192)
    ]

    FONT = pygame.font.SysFont('comicsans', 16)
    SIDE_PAD = 100
    TOP_PAD = 150

    def __init__(self, width, height, lst):
        self.width = width
        self.height = height
        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Sorting Algorithm Visualizer")
        self.set_list(lst)

    def set_list(self, lst):
        """
        We want to create the list in such a manner that it is dynamic 
        i.e. changing width and height of bars in output screen automatically 
        add padding 
        """
        self.lst = lst
        self.min_val = min(lst)
        self.max_val = max(lst)
        self.block_width = round(
            (self.width - self.SIDE_PAD) / len(lst))  # Width of each block
        self.block_height = round(
            (self.height-self.TOP_PAD)/(self.max_val-self.min_val))
        self.start_x = self.SIDE_PAD // 2


def generating_starting_list(n, min_val, max_val):
    lst = []
    for _ in range(n):
        val = random.randint(min_val, max_val)
        lst.append(val)
    return lst


def draw(draw_info):
    """
    Background
    """
    draw_info.window.fill(draw_info.BACKGROUND_COLOR)
    pygame.display.update()
    draw_list(draw_info)


def draw_list(draw_info):
    """
    Find it's height width and then five them diffrent shades to see them properly
    """
    lst = draw_info.lst

    for i, val in enumerate(lst):
        """
        We start drawing from top left corner so too keep pixel in mind
        also keep track of colors 
        """
        x = draw_info.start_x + i * draw_info.block_width
        y = draw_info.height - ((val - draw_info.min_val)
                                * draw_info.block_height)
        color = draw_info.GRADIENTS[i % 3]
        pygame.draw.rect(draw_info.window, color,
                         (x, y, draw_info.block_width, draw_info.height))


def main():
    run = True
    sorting = False
    ascending = True
    clock = pygame.time.Clock()

    n = 50
    min_val = 0
    max_val = 100

    lst = generating_starting_list(n, min_val, max_val)
    draw_info = DrawInformation(800, 600, lst)

    while run:
        clock.tick(20)
        draw(draw_info)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type != pygame.KEYDOWN:
                continue
            if event.key == pygame.K_r:
                """
                To reset the list
                """
                lst = generating_starting_list(n, min_val, max_val)
                draw_info.set_list(lst)
                sorting = False
            elif event.key == pygame.K_space and sorting == False:
                """
                To sort the list
                """
                sorting = True
            elif event.key == pygame.K_a and not sorting:
                """
                To ascending sort of the list
                """
                ascending = True
            elif event.key == pygame.K_d and not sorting:
                """
                To ascending sort of the list
                """
                ascending = False

    pygame.quit()


if __name__ == "__main__":
    main()
