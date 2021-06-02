import pygame, sys, time, random
#уровень сложности
lvl = input('Введите уровень сложности')

difficulty = int(lvl)
black = pygame.Color(0, 0, 0)
green = pygame.Color(0, 255, 0)


#размер экрана 


frame_size_x = 720
frame_size_y = 480 


check_error = pygame.init()

if check_error[1] > 0:
    print(f'Возникла ошибка{check_error[1]}') 
    sys.exit()
else:
    print('Игра была успешно с инициализирова')
pygame.display.set_caption('Melis Game')
game_windiw = pygame.display.set_mode((frame_size_x, frame_size_y))

#fps controller 
fps_controller = pygame.time.Clock()

#сама змейка 
snake_pos = [50, 20]
snake_body = [[100, 50], [100-10, 50], [100 -(2*10),50]]
direction = "RIGHT"
change_to = direction
fod_pos = [random.randrange(1, (frame_size_x// 10)) * 10, random.randrange(1, (frame_size_y// 10))* 10]
food_spawn = True


while True:
    #проверка ивентов пай Pygame
    for event in pygame.event.get():
        #если 
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == 'w':
                change_to = "UP"
            if event.key == pygame.K_DOWN or event.key == 's':
                change_to = "DOWN"
            if event.key == pygame.K_LEFT or event.key == 'a':
                change_to = "LEFT" 
            if event.key == pygame.K_RIGHT or event.key == 'd':
                change_to = "RIGHT"
            if event.key == pygame.K_ESCAPE:
                change_to = pygame.post(pygame.event.EVENT(pygame.QUIT))
    
  #определение движения куда будет смотреть змейка 
    if change_to == 'UP'and direction != "DOWN":
        direction = "UP"
    if change_to == 'DOWN'and direction != "UP":
        direction = "DOWN"
    if change_to == 'LEFT'and direction != "RIGHT":
        direction = "LEFT"
    if change_to == 'RIGHT'and direction != "LEFT":
        direction = "RIGHT"
        
   
#логика движения змейки 
    if direction == "UP":
        snake_pos[1] -= 10 
    if direction == "DOWN":
        snake_pos[1] += 10
    if direction == "LEFT":
        snake_pos[0] -= 10
    if direction == "RIGHT":
        snake_pos[0] += 10


    snake_body.insert(0, list(snake_pos))
    if snake_pos[0] == fod_pos[0] and snake_pos[1] == fod_pos[1]:
        food_spawn = False
    else:
        snake_body.pop()
    


    #спавн еды
    if not food_spawn:
        fod_pos = [random.randrange(1, (frame_size_x//10))*10 , random.randrange(1, (frame_size_y // 10))*10]
    food_spawn = True


    game_windiw.fill(black)
#отображение змейки
    
    for pos in snake_body:
        pygame.draw.rect(game_windiw, green, pygame.Rect(pos[0], pos[1], 10, 10))

    # отображение еды
    pygame.draw.rect(game_windiw, green, pygame.Rect(fod_pos[0], fod_pos[1], 10, 10))

    if snake_pos[0] < 0 or snake_pos[0] > frame_size_x -10:
        pygame.quit()
        sys.exit()
    if snake_pos[1] < 0 or snake_pos[1] > frame_size_y -10:
        pygame.quit()
        sys.exit()
    

#обновление экрана
    pygame.display.update()
    game_windiw.fill(black)
    fps_controller.tick((difficulty))



  