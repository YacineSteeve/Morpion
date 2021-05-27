from global_functions import *
import time

clock.tick(60)

RUNNING = True

loading_screen()
time.sleep(loading_duration)
fill_background()

while RUNNING:
    draw_grid()

    win = test_win()
    if win:
        draw_line()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
        if (not win) and event.type == pygame.MOUSEBUTTONDOWN:
            for case in grid:
                if on_case_area(case):
                    if turn % 2 == 0:
                        draw_cross(case[5])
                        case[6] = filled_with_cross
                        turn += 1
                    else:
                        draw_circle(case[4])
                        case[6] = filled_with_circle
                        turn += 1
