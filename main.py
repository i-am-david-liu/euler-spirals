from datetime import datetime
import pygame
#import time
import random
import math

pygame.init()

grid_width, grid_height = 500, 500
pixel_size = 2 
scale = 2

# set up window
window_width = grid_width * pixel_size
window_height = grid_height * pixel_size
window = pygame.display.set_mode((window_width, window_height))

# set up rendering screen 
surface = pygame.Surface((window_width, window_height), pygame.SRCALPHA)
surface.fill((0, 0, 0))

# animation loop
#start_time = time.time()

#curr_x, curr_y = window_width // 2, window_height // 2
curr_x, curr_y = 100, 100 

angle_step = 1
angle_incr = 1
beta = (4 + math.sqrt(5)) / 2 # vary this for magic 
steps = steps_left = 1000000
print("Press SPACE to pause, 'q' to quit.")
print("Running {} steps with beta={}...".format(steps, beta))

running = True
paused = False
while running and steps_left > 0:
    # event handler 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                paused = not paused 
                if paused:
                    print("Animation PAUSED.")
                else:
                    print("Animation unpaused.")
            elif event.key == pygame.K_q:
                running = False 

    if not paused: 
        next_x = scale * math.cos( angle_step * (math.pi / 180) )
        next_y = scale * math.sin( angle_step * (math.pi / 180) )

        pygame.draw.line(surface, (255, 0, 0), (curr_x, curr_y), (curr_x + next_x, curr_y + next_y))

        window.blit(surface, (0, 0))
        pygame.display.flip()

        curr_x += next_x
        curr_y += next_y

        angle_step += beta * angle_incr
        angle_incr += 1
        steps_left -= 1

        #time.sleep(0.01)

        """
        steps_left -= 1
        if steps_left % (steps // 8) == 0:
            execution_time = time.time() - start_time
            print("{}/{} steps performed. ({:.3f} s)".format(steps-steps_left, steps, execution_time))
        """

print("Animation finished.")
print("Press 's' to capture the window as an image, 'q' to quit.")

min_decimal = 2
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                print("Capturing window as image to current directory...")
                """
                time_string = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                pygame.image.save(
                        window,
                        "imgs/{}_b{}.png".format(time_string, str(beta).replace(".", "-"))
                )
                """
                if len(str(beta).split('.')[-1]) < min_decimal:
                    beta_string = "{:.2f}".format(beta)
                else:
                    beta_string = str(beta)


                pygame.image.save(window, "imgs/b{}.png".format(beta_string.replace(".", "-")))
                print("Saved image.")
                running = False

            elif event.key == pygame.K_q:
                running = False 

pygame.quit()
