from objects import *


def draw_grid():
    position = [case_position[0], case_position[1]]
    for i in range(3):
        for j in range(3):
            case = pygame.Rect(position[0], position[1], case_width, case_width)
            pygame.draw.rect(window_surface, case_color, case, case_thickness)
            position[0] += case_width
        position[0] = 75
        position[1] += case_width


def fill_background():
    position = [background_img_position[0], background_img_position[1]]
    for i in range(3):
        for j in range(5):
            window_surface.blit(background_img, position)
            pygame.display.flip()
            position[0] += background_img_width
        position[0] = 0
        position[1] += background_img_width
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
