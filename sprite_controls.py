import pygame

pygame.init()

SWidth = 1000
SHeight = 600
idle_sprites = []

screen = pygame.display.set_mode((SWidth, SHeight))
pygame.display.set_caption("FKN PHIL FIGHTER")

# set frame rate
clock = pygame.time.Clock()
FPS = 10

frame_index = 0
frame_count = len(idle_sprites)
last_frame_update = pygame.time.get_ticks()

sprite_sheet = pygame.image.load('ryu.png').convert_alpha()

print(sprite_sheet.get_width())
print(sprite_sheet.get_height())
sprite_info = {'idle': [{'x': 7, 'y': 14, 'width': 59, 'height': 90},
        {'x': 76, 'y': 14, 'width': 60, 'height': 89},
        {'x': 143, 'y': 13, 'width': 59, 'height': 90},
        {'x': 212, 'y': 10, 'width': 55, 'height': 93},
        {'x': 278, 'y': 11, 'width': 58, 'height': 92},
        {'x': 349, 'y': 8, 'width': 54, 'height': 95}
    ],
    'forward': [
        {'x': -9, 'y': -136, 'width': 53, 'height': 83},
        {'x': -78, 'y': -131, 'width': 60, 'height': 88},
        {'x': -152, 'y': -128, 'width': 64, 'height': 92},
        {'x': -229, 'y': -130, 'width': 63, 'height': 90},
        {'x': -307, 'y': -128, 'width': 54, 'height': 91},
        {'x': -371, 'y': -128, 'width': 50, 'height': 89}
    ],
    'backwards': [
        {'x': -430, 'y': -124, 'width': 59, 'height': 90},
        {'x': -495, 'y': -124, 'width': 57, 'height': 90},
        {'x': -559, 'y': -124, 'width': 58, 'height': 90},
        {'x': -631, 'y': -125, 'width': 58, 'height': 91},
        {'x': -707, 'y': -126, 'width': 57, 'height': 89},
        {'x': -777, 'y': -128, 'width': 61, 'height': 87}
    ],
    'jump': [
        {'x': -7, 'y': -268, 'width': 55, 'height': 85},
        {'x': -67, 'y': -244, 'width': 56, 'height': 104},
        {'x': -138, 'y': -233, 'width': 50, 'height': 89},
        {'x': -197, 'y': -233, 'width': 54, 'height': 77},
        {'x': -259, 'y': -240, 'width': 48, 'height': 70},
        {'x': -319, 'y': -234, 'width': 48, 'height': 89},
        {'x': -357, 'y': -244, 'width': 55, 'height': 109}
    ],
    'attack1': [
        {'x': -6, 'y': -466, 'width': 60, 'height': 94},
        {'x': -86, 'y': -465, 'width': 74, 'height': 95},
        {'x': -175, 'y': -465, 'width': 108, 'height': 94}
    ],
    'attack2': [
        {'x': -287, 'y': -921, 'width': 60, 'height': 94},
        {'x': -357, 'y': -920, 'width': 48, 'height': 95},
        {'x': -421, 'y': -922, 'width': 80, 'height': 93}
    ]
}

action = 'idle'
idle_sprites = []
for info in sprite_info[action]:
    rect = pygame.Rect(info['x'], info['y'], info['width'], info['height'])
    print(rect)
    sprite = sprite_sheet.subsurface(rect).copy()
    idle_sprites.append(sprite)
    print(idle_sprites)

if idle_sprites:
    frame_index = 0
    frame_count = len(idle_sprites)
    clock = pygame.time.Clock()

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    currentTime = pygame.time.get_ticks()
    last_frame_update = currentTime - last_frame_update
    time_since_last_frame = currentTime - last_frame_update
    if time_since_last_frame > 1000:
        frame_index = (frame_index + 1) % frame_count
        last_frame_update = pygame.time.get_ticks()

    screen.blit(idle_sprites[frame_index], (100, 100))

    pygame.display.update()

pygame.quit()