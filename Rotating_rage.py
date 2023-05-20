import pygame
from sys import exit


#   #   #Initialising
pygame.init()
WINDOW = pygame.display.set_mode((960,720))
CLOCK = pygame.time.Clock()
pygame.display.set_caption("Rotating Rage")


#   #   #Variables

FONT =  pygame.font.Font("data\\Pixeltype.ttf", 50)
angle = 0
Level_Number = 0
Fails = 0
game_active = True
r_direction = True

#   #   #Text


Level_Number_Display = FONT.render("Level: " + str(Level_Number+1), False , (204, 119, 33))
Level_Number_Display_rect = Level_Number_Display.get_rect(center = (70, 660))
Fails_Display = FONT.render("Fails: " + str(Fails), False , (204, 119, 33))
Fails_Display_rect = Level_Number_Display.get_rect(center = (70, 695))


#   #   #Player

Player = pygame.image.load("data\\Player.png")
Player_rect = Player.get_rect(center = (100,100))
Player_mask = pygame.mask.from_surface(Player)

#   #   #Fail Screen
Fail_Screen = pygame.image.load("data\\Fail_Screen.png")
Retry_Button = pygame.image.load("data\\Retry_Button.png")
Retry_Button_rect = Retry_Button.get_rect(center=(65, 150))

#   #   # Levels
Green_1 = pygame.image.load("data\\Green_1.png")
Green_1_finish = pygame.image.load("data\\Green_1_finish.png")
Green_2 = pygame.image.load("data\\Green_2.png")
Green_2_finish = pygame.image.load("data\\Green_2_finish.png")
Green_3 = pygame.image.load("data\\Green_3.png")
Green_3_finish = pygame.image.load("data\\Green_3_finish.png")
Green_4 = pygame.image.load("data\\Green_4.png")
Green_4_finish = pygame.image.load("data\\Green_4_finish.png")
Green_5 = pygame.image.load("data\\Green_5.png")
Green_5_finish = pygame.image.load("data\\Green_5_finish.png")
Green_6 = pygame.image.load("data\\Green_6.png")
Green_6_finish = pygame.image.load("data\\Green_6_finish.png")

Orange_1 = pygame.image.load("data\\Orange_1.png")
Orange_1_finish = pygame.image.load("data\\Orange_1_finish.png")
Orange_2 = pygame.image.load("data\\Orange_2.png")
Orange_2_finish = pygame.image.load("data\\Orange_2_finish.png")
Orange_3 = pygame.image.load("data\\Orange_3.png")
Orange_3_finish = pygame.image.load("data\\Orange_3_finish.png")
Orange_4 = pygame.image.load("data\\Orange_4.png")
Orange_4_finish = pygame.image.load("data\\Orange_4_finish.png")

Red_1 = pygame.image.load("data\\Red_1.png")
Red_1_finish = pygame.image.load("data\\Red_1_finish.png")
Red_2 = pygame.image.load("data\\Red_2.png")
Red_2_finish = pygame.image.load("data\\Red_2_finish.png")
Red_3 = pygame.image.load("data\\Red_3.png")
Red_3_finish = pygame.image.load("data\\Red_3_finish.png")
Red_4 = pygame.image.load("data\\Red_4.png")
Red_4_finish = pygame.image.load("data\\Red_4_finish.png")

White_1 = pygame.image.load("data\\White_1.png")
White_1_finish = pygame.image.load("data\\White_1_finish.png")
White_2 = pygame.image.load("data\\White_2.png")
White_2_finish = pygame.image.load("data\\White_2_finish.png")
White_3 = pygame.image.load("data\\White_3.png")
White_3_finish = pygame.image.load("data\\White_3_finish.png")

Wood_1 = pygame.image.load("data\\Wood_1.png")
Wood_1_finish = pygame.image.load("data\\Wood_1_finish.png")
Wood_2 = pygame.image.load("data\\Wood_2.png")
Wood_2_finish = pygame.image.load("data\\Wood_2_finish.png")
Wood_3 = pygame.image.load("data\\Wood_3.png")
Wood_3_finish = pygame.image.load("data\\Wood_3_finish.png")
Wood_4 = pygame.image.load("data\\Wood_4.png")
Wood_4_finish = pygame.image.load("data\\Wood_4_finish.png")


Level = [Green_1, Green_2, Green_3, Green_4, Green_5, Green_6, Orange_1, Orange_2, Orange_3, Orange_4, Red_1, Red_2, Red_3, Red_4, White_1, White_2, White_3, Wood_1, Wood_2, Wood_3, Wood_4]
Level_finish = [Green_1_finish, Green_2_finish, Green_3_finish, Green_4_finish, Green_5_finish, Green_6_finish, Orange_1_finish, Orange_2_finish, Orange_3_finish, Orange_4_finish, Red_1_finish, Red_2_finish, Red_3_finish, Red_4_finish, White_1_finish, White_2_finish, White_3_finish, Wood_1_finish, Wood_2_finish, Wood_3_finish, Wood_4_finish]
Level_mask = pygame.mask.from_surface(Level[Level_Number])
Level_finish_mask = pygame.mask.from_surface(Level_finish[Level_Number])






#   #   #Functions

def restart():
    global Level_Number
    global Level_Number_Display
    global Fails
    global Fails_Display
    global game_active

    Fails += 1
    Fails_Display = FONT.render("Fails: " + str(Fails), False , (204, 119, 33))
    if Level_Number < 6: # 0-5
        Level_Number = 0
    elif Level_Number > 5 and Level_Number < 10: # 6-9
        Level_Number = 6
    elif Level_Number > 9 and Level_Number < 14: #10 - 13
        Level_Number = 10
    elif Level_Number > 13 and Level_Number < 17:# 15 - 16
        Level_Number = 14
    elif Level_Number > 16 and Level_Number < 21:
        Level_Number = 17

    Level_Number_Display = FONT.render("Level: " + str(Level_Number+1), False , (204, 119, 33))
    game_active = False


Rotation_switch = pygame.USEREVENT + 1
pygame.time.set_timer(Rotation_switch, 6000)

#   #   #Main loop
pygame.mouse.set_pos([50, 50])
while True:

    if Level_Number < 6:
        angle += -1
    elif Level_Number > 5 and Level_Number < 10:
        if r_direction:
            angle += -1
        else:
            angle += 1
    elif Level_Number > 9 and Level_Number < 15:
        angle += -2
    elif Level_Number > 14 and Level_Number < 17:
        angle += -2
    elif Level_Number > 16 and Level_Number < 21:
        angle += -1

    mouse_pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           pygame.quit()
           exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if not game_active:
                if Retry_Button_rect.collidepoint(mouse_pos):
                    game_active = True
        if event.type == Rotation_switch and game_active and Level_Number > 5 and Level_Number < 10:
            r_direction = not r_direction
            print(r_direction)

    if game_active:
        WINDOW.fill((0,6,73))


        Player_rect.center = mouse_pos

        # Rotation
        img_copy = pygame.transform.rotate(Level[Level_Number], angle)
        img_finish_copy = pygame.transform.rotate(Level_finish[Level_Number], angle)
        Level_pos = (480 - int(img_copy.get_width() / 2) , 360 - int(img_copy.get_height() / 2))


        #Collision
        Level_mask = pygame.mask.from_surface(img_copy)
        Level_finish_mask = pygame.mask.from_surface(img_finish_copy)

        offset_x = Level_pos[0] - Player_rect.left
        offset_y = Level_pos[1] - Player_rect.top

        if Player_mask.overlap(Level_mask, (offset_x, offset_y)):
            print("Collision detected")
            restart()
            #pygame.quit()
            #exit()

        if Player_mask.overlap(Level_finish_mask, (offset_x, offset_y)):
            print("Finished")
            if Level_Number < 20:
                Level_Number += 1
            if Level_Number == 14 or Level_Number == 17:
                pygame.mouse.set_pos([50, 50])


            Level_Number_Display = FONT.render("Level: " + str(Level_Number+1), False , (204, 119, 33))





        WINDOW.blit(img_copy, Level_pos)
        WINDOW.blit(img_finish_copy, Level_pos)
        WINDOW.blit(Player, Player_rect)
        WINDOW.blit(Level_Number_Display, Level_Number_Display_rect)
        WINDOW.blit(Fails_Display, Fails_Display_rect)

    #print(CLOCK.get_fps())

    if not game_active:
        WINDOW.blit(Fail_Screen, (0,0))
        WINDOW.blit(Retry_Button, Retry_Button_rect)





    pygame.display.update()
    CLOCK.tick(30)
