import pygame
from pygame import mixer
from fighter import Fighter

pygame.init()

# create game window
SWidth = 1000
SHeight = 600

screen = pygame.display.set_mode((SWidth, SHeight))
pygame.display.set_caption("FKN PHIL'S TWITCH FIGHTS!")

# set frame rate
clock = pygame.time.Clock()
FPS = 60

# define colors
RED = (255, 0, 0)

# define game variables
intro_count = 10
last_count_update = pygame.time.get_ticks()
score = [0, 0]  # player scores. [p1, p2]
round_over = False
round_over_cooldown = 2000

# define fighter variables
ryu_size = 162
ryu_scale = 4
ryu_offset = [72, 56]
ryu_data = [ryu_size, ryu_scale, ryu_offset]

car_size = 162
car_scale = 4
car_offset = [72, 56]
car_data = [car_size, car_scale, car_offset]

# Load music and sounds
pygame.mixer.music.load('gamesound.wav')
pygame.mixer.music.set_volume(.5)
pygame.mixer.music.play(-1, 0.0, 5000)
sword_fx = pygame.mixer.Sound('sword.wav')
sword_fx.set_volume(0.5)

# load background image
bgImg = pygame.image.load("background.png").convert_alpha()

# load sprite sheets
ryu_sheet = pygame.image.load('warrior.png').convert_alpha()
car_sheet = pygame.image.load('warrior.png').convert_alpha()


# load victory image
victory_image = pygame.image.load('victory.png').convert_alpha()

# define number of steps in each animation
ryu_animation_steps = [10, 8, 1, 7, 7, 3, 7]
car_animation_steps = [10, 8, 1, 7, 7, 3, 7]

# define font
count_font = pygame.font.Font('turok.ttf', 120)
score_font = pygame.font.Font('turok.ttf', 90)

# function for drawing text
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

# function for background
def draw_bg():
    scaled_bgImg = pygame.transform.scale(bgImg, (SWidth, SHeight))
    screen.blit(scaled_bgImg, (0, 0))

def draw_health_bar(health, x, y):
    ratio = health / 100
    pygame.draw.rect(screen, (255, 255, 255), (x - 2, y - 2, 404, 34))
    pygame.draw.rect(screen, (255, 0, 0), (x, y, 400, 30))
    pygame.draw.rect(screen, (255, 255, 0), (x, y, 400 * ratio, 30))


# create 2 instances of fighters
fighter_1 = Fighter(1, 200, 310, False, ryu_data, ryu_sheet, ryu_animation_steps, sword_fx)
fighter_2 = Fighter(2, 455, 310, True, car_data, car_sheet, car_animation_steps, sword_fx)

# game loop
run = True
while run:

    clock.tick(FPS)

    # draw background
    draw_bg()

    # show player stats
    draw_health_bar(fighter_2.health, 300, 20)

    # update countdown
    if intro_count <= 0:
        # move fighters
        fighter_1.move(SWidth, SHeight, screen, fighter_2, round_over)
        fighter_2.move(SWidth, SHeight, screen, fighter_1, round_over)
    else:
        # display countdown timer
        draw_text(str(intro_count), count_font, RED, SWidth / 2, SHeight / 3)
        # update count timer
        if (pygame.time.get_ticks() - last_count_update) >= 1000:
            intro_count -= 1
            last_count_update = pygame.time.get_ticks()



    # update fighters
    fighter_1.update()
    fighter_2.update()

    #draw fighters
    fighter_1.draw(screen)
    fighter_2.draw(screen)

    # check for player defeat
    if round_over == False:
        if fighter_1.alive == False:
            score[1] == 1
            round_over = True
            round_over_time = pygame.time.get_ticks()
        elif fighter_2.alive == False:
            score[0] == 1
            round_over = True
            round_over_time = pygame.time.get_ticks()
    else:
        # display victory image
        screen.blit(victory_image, (360, 150))
        if pygame.time.get_ticks() - round_over_time > round_over_cooldown:
            round_over = False


    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # update display
    pygame.display.update()

# exit program
pygame.quit()
