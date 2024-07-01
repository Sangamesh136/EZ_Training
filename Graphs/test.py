# print(0.2+0.1 == 0.3)
# print(abs(0.2 + 0.1))
# print(abs(0.3))

# To find number of graph combinations possible with n number of vertices: 2 ** n * ((n-1)/2)

# n = 2
# print(int(2**n*((n-1)/2)))
#
# import pygame
# import sys
#
# # Initialize Pygame
# pygame.init()
#
# # Constants
# SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
# BLOCK_SIZE = 50
# GRID_WIDTH, GRID_HEIGHT = SCREEN_WIDTH // BLOCK_SIZE, SCREEN_HEIGHT // BLOCK_SIZE
#
# # Colors
# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)
# BLUE = (0, 0, 255)
# RED = (255, 0, 0)
#
# # Create the screen
# screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# pygame.display.set_caption('Simple Block-building Game')
#
# # Block grid representing the world
# world = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
#
# # Main game loop
# running = True
# while running:
#     # Handle events
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         elif event.type == pygame.MOUSEBUTTONDOWN:
#             # Place or remove blocks on left and right clicks
#             mouse_x, mouse_y = pygame.mouse.get_pos()
#             grid_x, grid_y = mouse_x // BLOCK_SIZE, mouse_y // BLOCK_SIZE
#             if event.button == 1:  # Left mouse button (place block)
#                 world[grid_y][grid_x] = 1
#             elif event.button == 3:  # Right mouse button (remove block)
#                 world[grid_y][grid_x] = 0
#
#     # Clear the screen
#     screen.fill(WHITE)
#
#     # Draw the world grid
#     for y in range(GRID_HEIGHT):
#         for x in range(GRID_WIDTH):
#             if world[y][x] == 1:
#                 pygame.draw.rect(screen, BLACK, (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
#             else:
#                 pygame.draw.rect(screen, WHITE, (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 1)
#
#     # Update the display
#     pygame.display.flip()
#
# # Quit Pygame
# pygame.quit()
# sys.exit()