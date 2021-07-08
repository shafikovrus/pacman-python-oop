import pygame

# Initialize the game engine
pygame.init()

# Define the colors we will use in RGB format
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
PINK_LIGHT = (255, 200, 200)

# Set the height and width of the screen
scale = 2
size = [224 * scale, 288 * scale]  # Old-style screensize right from 80-s scaled x2 both sides
screen = pygame.display.set_mode(size)
pygame.display.set_caption("OOP Python – Pacman")


class Player:
    """
    Our player`s drawing of model and controlling
    """
    def __init__(self):
        pass

    def draw_pacman(self, x, y, index):
        """
        Initial draw of animated Pacman
        :param x, y: coordinates of Pacman
        :param index: used for animation
        """
        pacman_images = [
            pygame.transform.scale(pygame.image.load(r'Images\Pacman_open_mouth.png'), [13 * scale, 13 * scale]),
            pygame.transform.scale(pygame.image.load(r'Images\Pacman_closed_mouth.png'), [13 * scale, 13 * scale])]
        pacman_surf = pacman_images[index]
        screen.blit(pacman_surf, (x * scale, y * scale))


class Monsters:
    """
    Drawing and motions of 4 different monsters
    """
    def __init__(self):
        pass

    def draw_blinky(self, x, y):
        """
        Initial draw of Blinky (red monster)
        :param x, y: coordinates of Blinky
        """
        blinky_surf = pygame.transform.scale(pygame.image.load(r'Images\Blinky.png'), [14 * scale, 14 * scale])
        screen.blit(blinky_surf, (x * scale, y * scale))

    def draw_pinky(self, x, y):
        """
        Initial draw of Pinky (pink monster)
        :param x, y: coordinates of Pinky
        """
        pinky_surf = pygame.transform.scale(pygame.image.load(r'Images\Pinky.png'), [14 * scale, 14 * scale])
        screen.blit(pinky_surf, (x * scale, y * scale))

    def draw_inky(self, x, y):
        """
        Initial draw of Inky (lime monster)
        :param x, y: coordinates of Inky
        """
        inky_surf = pygame.transform.scale(pygame.image.load(r'Images\Inky.png'), [14 * scale, 14 * scale])
        screen.blit(inky_surf, (x * scale, y * scale))

    def draw_clyde(self, x, y):
        """
        Initial draw of Clyde (orange monster)
        :param x, y: coordinates of Clyde
        """
        clyde_surf = pygame.transform.scale(pygame.image.load(r'Images\Clyde.png'), [14 * scale, 14 * scale])
        screen.blit(clyde_surf, (x * scale, y * scale))


class GameField:
    def __init__(self):
        pass

    def draw_field(self):
        """
        Takes 224x288 field from already drawn one
        Snap point = top left
        """
        screen.fill(BLACK)
        field_surf = pygame.transform.scale(pygame.image.load(r'Images\Game_field.png'), size)
        field_rect = field_surf.get_rect(topleft=(0, 0))
        screen.blit(field_surf, field_rect)

    def dots(self):
        """
        Takes 240 of 2x2 dots at their places
        Snap point = top left
        """
        # Fill the list of coordinates
        dots_coordinates = []
        dots_coordinates += list([x, 35] for x in range(11, 107, 8))
        dots_coordinates += list([x, 35] for x in range(123, 219, 8))
        dots_coordinates += list([x, 67] for x in range(11, 219, 8))
        dots_coordinates += list([x, 91] for x in range(11, 59, 8))
        dots_coordinates += list([x, 91] for x in range(75, 107, 8))
        dots_coordinates += list([x, 91] for x in range(123, 155, 8))
        dots_coordinates += list([x, 91] for x in range(171, 219, 8))
        dots_coordinates += list([x, 187] for x in range(11, 107, 8))
        dots_coordinates += list([x, 187] for x in range(123, 219, 8))
        dots_coordinates += list([x, 211] for x in range(19, 35, 8))
        dots_coordinates += list([x, 211] for x in range(51, 107, 8))
        dots_coordinates += list([x, 211] for x in range(123, 179, 8))
        dots_coordinates += list([x, 211] for x in range(195, 211, 8))
        dots_coordinates += list([x, 235] for x in range(11, 59, 8))
        dots_coordinates += list([x, 235] for x in range(75, 107, 8))
        dots_coordinates += list([x, 235] for x in range(123, 155, 8))
        dots_coordinates += list([x, 235] for x in range(171, 219, 8))
        dots_coordinates += list([x, 259] for x in range(11, 219, 8))
        dots_coordinates += list([11, y] for y in range(35, 51, 8))
        dots_coordinates += list([11, y] for y in range(59, 99, 8))
        dots_coordinates += list([11, y] for y in range(187, 211, 8))
        dots_coordinates += list([11, y] for y in range(235, 267, 8))
        dots_coordinates += list([27, y] for y in range(211, 243, 8))
        dots_coordinates += list([51, y] for y in range(35, 243, 8))
        dots_coordinates += list([75, y] for y in range(67, 99, 8))
        dots_coordinates += list([75, y] for y in range(211, 243, 8))
        dots_coordinates += list([99, y] for y in range(35, 75, 8))
        dots_coordinates += list([99, y] for y in range(187, 219, 8))
        dots_coordinates += list([99, y] for y in range(235, 267, 8))
        dots_coordinates += list([123, y] for y in range(35, 75, 8))
        dots_coordinates += list([123, y] for y in range(187, 219, 8))
        dots_coordinates += list([123, y] for y in range(235, 267, 8))
        dots_coordinates += list([147, y] for y in range(67, 99, 8))
        dots_coordinates += list([147, y] for y in range(211, 243, 8))
        dots_coordinates += list([171, y] for y in range(35, 243, 8))
        dots_coordinates += list([195, y] for y in range(211, 243, 8))
        dots_coordinates += list([211, y] for y in range(35, 51, 8))
        dots_coordinates += list([211, y] for y in range(59, 99, 8))
        dots_coordinates += list([211, y] for y in range(187, 211, 8))
        dots_coordinates += list([211, y] for y in range(235, 267, 8))
        dots_set = set()
        for x, y in dots_coordinates:
            dots_set.add((x, y))
        dots_coordinates = list(dots_set)

        # Put them at the screen
        for x, y in dots_coordinates:
            dots_points = [[x * scale, y * scale], [(x + 1) * scale, y * scale],
                           [(x + 1) * scale, (y + 1) * scale], [x * scale, (y + 1) * scale]]
            pygame.draw.polygon(screen, PINK_LIGHT, dots_points)

    def big_dots(self):
        """
        Takes 4 of big dots at their places
        Snap point = top left
        """
        # Fill the list of coordinates
        big_dots_coordinates = [[12, 52], [212, 52], [12, 212], [212, 212]]

        # Put them at the screen
        for x, y in big_dots_coordinates:
            center = [x * scale, y * scale]
            pygame.draw.circle(screen, PINK_LIGHT, center, 3.00 * scale)

    def draw_text(self, player_name, current_score, high_score):
        """
        Draws text at the top of game_field
        :param player_name: Chosen player name
        :param current_score: Number of points reached at current game session and at current continue
        :param high_score: Maximum of points reached at current game session
        """
        pygame.font.init()
        font = pygame.font.SysFont('Impact', 11 * scale)
        text_field_1 = font.render(player_name + '     ' + 'HIGH SCORE', True, WHITE)
        text_field_2 = font.render(' ' + str(current_score), True, WHITE)
        text_field_3 = font.render('' + str(high_score), True, WHITE)
        screen.blit(text_field_1, (26 * scale, 0 * scale))
        screen.blit(text_field_2, (33 * scale, 9 * scale))
        screen.blit(text_field_3, (75 * scale, 9 * scale))

    def draw_lives(self, lives: int):
        """
        Draws number of lives at the bottom of game field
        :param lives: number of lives at current continue
        """
        start_point = [19 * scale, 274 * scale]
        pacman_surf = pygame.transform.scale(pygame.image.load(r'Images\Pacman_open_mouth.png'),
                                             [13 * scale, 13 * scale])
        for live in range(lives):
            screen.blit(pacman_surf, start_point)
            start_point[0] += 20 * scale


class GameView:
    def __init__(self):
        pass


class RoundManager:
    """
    Main loop manager
    """
    def __init__(self, lives_number: int):
        self._lives = []


class GameWindow:
    def __init__(self):
        pass

    def main_loop(self):
        # Loop until the user clicks the close button.
        done = False
        clock = pygame.time.Clock()
        animation_index = 1
        while not done:
            clock.tick(8)
            for event in pygame.event.get():  # User did something
                if event.type == pygame.QUIT:  # If user clicked close
                    done = True  # Flag that we are done so we exit this loop

            draw_game_field = GameField()
            draw_game_field.draw_field()
            draw_game_field.dots()
            draw_game_field.big_dots()
            draw_game_field.draw_text('1UP', 0, 2048)
            draw_game_field.draw_lives(3)


            draw_player = Player()
            draw_player.draw_pacman(106, 206, animation_index)
            pygame.display.update()
            if animation_index == 0:
                animation_index = 1
            else:
                animation_index = 0
            
            draw_monster = Monsters()
            draw_monster.draw_blinky(105, 110)
            draw_monster.draw_pinky(89, 136)
            draw_monster.draw_inky(105, 136)
            draw_monster.draw_clyde(121, 136)


            # Go ahead and update the screen with what we've drawn.
            # This MUST happen after all the other drawing commands.
            pygame.display.flip()

        # Be IDLE friendly
        pygame.quit()


def main():
    window = GameWindow()
    window.main_loop()
    print('Game Over!')


if __name__ == "__main__":
    main()
