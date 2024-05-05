import pygame #importing module 
pygame.init() #initalize 

screen = pygame.display.set_mode([300, 300]) #displaying screen and setting size
pygame.display.set_caption('Ping Pong Game') #Name of the game 

timer = pygame.time.Clock()
frameRate = 60 #standardizing frame rate 
colourBlack = (0,0,0)
colourWhite = (255,255,255)
font = pygame.font.Font('freesansbold.ttf', 20)

#game variable
player_y = 130
computer_y = 130
ball_x = 145
ball_y = 145
player_direction = 0
player_speed = 5
ball_x_direction = 1
ball_y_direction = 1
ball_speed = 2
ball_y_speed = 1
score = 0
gameOver = False

def update_ai(ball_y, computer_y):
    computer_speed = 3
    if computer_y + 15 > ball_y + 5: #if compRectangle mid section is farther than the ball
        computer_y -= computer_speed #compRectangle will go down to hit the ball back
    elif computer_y + 15 < ball_y + 5:
        computer_y += computer_speed
    return computer_y

def update_ball(ball_x_direction, ball_y_direction, ball_x, ball_y, ball_speed):
    #updating in x direction
    if ball_x_direction == 1 and ball_x < 290:
        ball_x += ball_speed
    elif ball_x_direction == 1 and ball_x >= 290:
        ball_x_direction *= -1
    if ball_x_direction == -1 and ball_x > 0:
        ball_x -= ball_speed
    elif ball_x_direction == -1 and ball_x <= 0:
        ball_x_direction *= -1
    #updating in y direction   
    if ball_y_direction == 1 and ball_y < 290:
        ball_y += ball_y_speed
    elif ball_y_direction == 1 and ball_y >= 290:
        ball_y_direction *= -1
    if ball_y_direction == -1 and ball_y > 0:
        ball_y -= ball_y_speed
    elif ball_y_direction == -1 and ball_y <= 0:
        ball_y_direction *= -1
    return ball_x_direction, ball_y_direction, ball_x, ball_y

#check for collision
def check_collision(ball, player, computer, ball_x_direction, score):
    if ball.colliderect(player) and ball_x_direction == -1: #if ball and rect collides
        ball_x_direction = 1
        score+=1
    elif ball.colliderect(computer) and ball_x_direction == 1:
        ball_x_direction = -1
        score+=1
    return ball_x_direction, score

#check for game over
def check_game_over(ball_x, gameOver):
    if ball_x <= 0 or ball_x >= 290 and gameOver == False: #when ball hits the wall
        gameOver = True
    return gameOver

running = True 
while running:
    timer.tick(frameRate) #setting frame rates per second
    screen.fill(colourBlack) #screen colour
    gameOver = check_game_over(ball_x, gameOver)
    player = pygame.draw.rect(screen, colourWhite, [5, player_y, 10, 40]) #player rectangle
    computer = pygame.draw.rect(screen, colourWhite, [285, computer_y, 10, 40]) #computer rectangle
    ball = pygame.draw.rect(screen, colourWhite, [ball_x, ball_y, 10, 10]) #ping pong ball
    score_text = font.render('Score: '+ str(score), True, colourWhite, colourBlack)
    screen.blit(score_text, (90, 10))

    if not gameOver: #ball will only update if game is not over
        computer_y = update_ai(ball_y, computer_y) #update ball coordinates for ocmputer accordingly
        ball_x_direction, ball_y_direction, ball_x, ball_y = update_ball(ball_x_direction, ball_y_direction, ball_x, ball_y, ball_speed)

    #check collision
    ball_x_direction, score = check_collision(ball, player, computer, ball_x_direction, score) #flip the x direction when a collion happens

    if gameOver:
        game_over_text = font.render('Game Over', True, colourWhite, colourBlack)
        screen.blit(game_over_text, (80, 130)) #displaying text on screen
        restart_button = pygame.draw.rect(screen, colourBlack, [60, 150, 100, 20])
        restart_text = font.render('Press to restart', True, colourWhite, colourBlack)
        screen.blit(restart_text, (60, 150)) #displaying text on screen
        
    
    for event in pygame.event.get(): #handling user inputs 
        if event.type == pygame.QUIT: 
            running = False #if user clicks on x button
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w: #if 'W' is pressed
                player_direction = -1 #playerRectangle moves up
            if event.key == pygame.K_s: #if 'S' is pressed
                player_direction = 1 #playerRectangle moves down 
        if event.type == pygame.KEYUP: 
            if event.key == pygame.K_w: #if 'W' is released
                player_direction = 0 #playerRectangle goes back to 0
            if event.key == pygame.K_s:
                player_direction = 0
        if event.type == pygame.MOUSEBUTTONDOWN and gameOver == True: #if user press restart
            if restart_button.collidepoint(event.pos):
                gameOver = False
                #reset all variables
                player_y = 130
                computer_y = 130
                ball_x = 145
                ball_y = 145
                player_direction = 0
                player_speed = 5
                ball_x_direction = 1
                ball_y_direction = 1
                ball_speed = 2
                ball_y_speed = 1
                score = 0


    player_y += player_speed*player_direction #increasing speed of playerRectangle
    
                
    pygame.display.flip()

pygame.quit()
