from objects import *
import time
from pygame.constants import QUIT, MOUSEBUTTONDOWN


def draw_grid():
    position = [case_position[0], case_position[1]]
    for i in range(3):
        for j in range(3):
            case = pygame.Rect(position[0], position[1], case_width, case_width)
            pygame.draw.rect(window_surface, case_color, case, case_thickness)
            position[0] += case_width
        position[0] = 75
        position[1] += case_width
    window_surface.blit(playing_title_surface, playing_title_position)
    pygame.display.flip()


def fill_background():
    window_surface.blit(background_img_2, (0, 0))
    window_surface.blit(copyright_surface, playing_copyright_position)
    draw_grid()
    pygame.display.flip()


def loading_screen():
    position = [background_img_position[0], background_img_position[1]]
    for i in range(3):
        for j in range(5):
            window_surface.blit(loading_img, position)
            pygame.display.flip()
            position[0] += loading_img_width
        position[0] = 0
        position[1] += loading_img_width - 10
    window_surface.blit(title_surface, title_position)
    window_surface.blit(loading_surface, loading_position)
    window_surface.blit(copyright_surface, copyright_position)
    pygame.display.flip()


def on_case_area(case):
    mouse_pos = pygame.mouse.get_pos()
    if case[0] < mouse_pos[0] < case[1] and case[2] < mouse_pos[1] < case[3]:
        return True
    else:
        return False


def draw_circle(center):
    pygame.draw.circle(window_surface, circle_color, center, circle_radius, circle_thickness)
    pygame.display.flip()


def draw_cross(summits):
    pygame.draw.line(window_surface, cross_color, summits[0], summits[1], cross_thickness)
    pygame.display.flip()
    pygame.draw.line(window_surface, cross_color, summits[2], summits[3], cross_thickness)
    pygame.display.flip()


def test_aligns():
    for triplet in aligns:
        check_circle = 0
        check_cross = 0
        for i in range(3):
            if grid[triplet[i]][6] == filled_with_circle:
                check_circle += 1
            elif grid[triplet[i]][6] == filled_with_cross:
                check_cross += 1
        if check_circle == 3:
            return 1
        elif check_cross == 3:
            return 2


def test_win():
    if test_aligns() == 1 or test_aligns() == 2:
        return True
    else:
        return False


def draw_line():
    for triplet in aligns:
        check_circle = 0
        check_cross = 0
        for i in range(3):
            if grid[triplet[i]][6] == filled_with_circle:
                check_circle += 1
            elif grid[triplet[i]][6] == filled_with_cross:
                check_cross += 1
        if check_circle == 3 or check_cross == 3:
            pygame.draw.line(window_surface, line_color, grid[triplet[0]][4], grid[triplet[2]][4], line_thickness)
            pygame.display.flip()
            return None


def test_filling():
    fill = 0
    for i in range(9):
        if grid[i][6] != empty:
            fill += 1
    if fill == 9:
        return True
    else:
        return False

# player 1 => cercles
# player 2 => croix


def say_winner(mark, player):
    winner = player[mark - 1]
    winner_surface = winner_font.render(f"{winner} a gagné!", True, winner_color)
    window_surface.blit(winner_surface, winner_position)
    pygame.display.flip()


def say_equality():
    window_surface.blit(equality_surface, winner_position)
    pygame.display.flip()


def draw_start(box_color):
    pygame.draw.rect(window_surface, box_color, start_box, border_radius=start_box_radius)
    pygame.display.flip()
    window_surface.blit(start_text_surface, start_text_position)
    pygame.display.flip()


def turn_of(text):
    """if player_turn % 2 == 1:
        turn_text_surface = turn_font.render("Tour de:  O", True, turn_text_color)
        window_surface.blit(turn_text_surface, turn_text_position)
    elif player_turn % 2 == 0:
        turn_text_surface = turn_font.render("Tour de:  X", True, turn_text_color)
        window_surface.blit(turn_text_surface, turn_text_position)"""
    turn_text_surface = turn_font.render(text, True, turn_text_color)
    window_surface.blit(turn_text_surface, turn_text_position)
    pygame.display.flip()


def play():
    running = True
    start = False
    end = True
    turn = 1

    fill_background()
    draw_start(start_box_inactive_color)

    while running:

        win = test_win()
        full = test_filling()

        if win and end:
            draw_line()
            say_winner(test_aligns(), ["O", "X"])
            end = False

        if full and end and not win:
            say_equality()
            end = False

        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            if start and (not win) and (not full) and event.type == MOUSEBUTTONDOWN:
                for case in grid:
                    if on_case_area(case):
                        if turn % 2 == 0 and case[6] == empty:
                            draw_cross(case[5])
                            case[6] = filled_with_cross
                            turn += 1
                        elif turn % 2 == 1 and case[6] == empty:
                            draw_circle(case[4])
                            case[6] = filled_with_circle
                            turn += 1
            if (not start) and event.type == MOUSEBUTTONDOWN:
                if start_box.collidepoint(pygame.mouse.get_pos()):
                    start = True
                    draw_start(start_box_active_color)
                    time.sleep(0.2)
                    draw_start(start_box_inactive_color)
                    time.sleep(0.35)
                    fill_background()
                    turn_of("C'est parti!")
                    time.sleep(1.2)
                    fill_background()
                    turn_of("        ...")
