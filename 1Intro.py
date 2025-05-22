import pygame

pygame.init()#starts pygame
screen = pygame.display.set_mode((1000,800))#φτιάχνει παράθυρο screen με διαστάσεις #400,300
done = False#μεταβλητή false

xb = 910
yb = 30
xr = 30
yr = 30

clock = pygame.time.Clock()


while done == False:#όσο το done είναι false το παιχνίδι παίζει
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
         done = True

    screen.fill((0,0,0))

    Font = pygame.font.SysFont("comicsansms", 60, True)
    Title1 = Font.render("Maze", True, (255,255,255))
    screen.blit(Title1, (435,0))

    Font = pygame.font.SysFont("comicsansms", 20, True)
    Title2 = Font.render("By Panos", True, (255,255,255))
    screen.blit(Title2, (437,65))


    player1 = pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(xb, yb, 60, 60))
    player2 = pygame.draw.rect(screen, (0, 128, 25), pygame.Rect(xr, yr, 60, 60))
    winpad = pygame.draw.rect(screen, (0, 128, 25), pygame.Rect(480, 30, 60, 60))
    w1 = pygame.draw.rect(screen, (255, 128, 25), pygame.Rect(200, 30, 120, 520))
    w2 = pygame.draw.rect(screen, (255, 128, 25), pygame.Rect(680, 30, 120, 520))
    w3 = pygame.draw.rect(screen, (255, 128, 25), pygame.Rect(450, 500, 120, 50))
    w4 = pygame.draw.rect(screen, (255, 128, 25), pygame.Rect(300, 450, 120, 50))
    w5 = pygame.draw.rect(screen, (255, 128, 25), pygame.Rect(595, 450, 120, 50))
    w6 = pygame.draw.rect(screen, (255, 128, 25), pygame.Rect(220, 300, 120, 50))
    w7 = pygame.draw.rect(screen, (255, 128, 25), pygame.Rect(665, 300, 120, 50))
    w8 = pygame.draw.rect(screen, (255, 128, 25), pygame.Rect(450, 300, 120, 50))

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]: yr = yr - 3
    if pressed[pygame.K_DOWN]: yr = yr + 3
    if pressed[pygame.K_LEFT]: xr = xr - 3
    if pressed[pygame.K_RIGHT]: xr = xr + 3
    if pressed[pygame.K_w]: yb = yb - 3
    if pressed[pygame.K_s]: yb = yb + 3
    if pressed[pygame.K_a]: xb = xb - 3
    if pressed[pygame.K_d]: xb = xb + 3

    if player1.colliderect(w1) or player1.colliderect(w2):
        if pressed[pygame.K_w]: yb += 10
        if pressed[pygame.K_s]: yb -= 10
        if pressed[pygame.K_a]: xb += 10
        if pressed[pygame.K_d]: xb -= 10
    if player2.colliderect(w1) or player2.colliderect(w2):
        if pressed[pygame.K_UP]: yr += 10
        if pressed[pygame.K_DOWN]: yr -= 10
        if pressed[pygame.K_LEFT]: xr += 10
        if pressed[pygame.K_RIGHT]: xr -= 10


    if player1.colliderect(player2) or player1.colliderect(winpad):
        xb = 910
        yb = 30
    if player2.colliderect(player1) or player2.colliderect(winpad):
        xr = 30
        yr = 30

    if player1.bottom > screen.get_rect().bottom:
        yb -= 3
    if player1.top -3< screen.get_rect().top:
        yb += 3
    if player1.left > screen.get_rect().left:
        xb -= 3
    if player1.right < screen.get_rect().right:
        xb += 3
    if player2.bottom > screen.get_rect().bottom:
        yr -= 3
    if player2.top -3< screen.get_rect().top:
        yr += 3
    if player2.left > screen.get_rect().left:
        xr -= 3
    if player2.right < screen.get_rect().right:
        xr += 3

    pygame.display.flip()#Τελευτέα εντολή ΠΆΝΤΑ, εξαιτίας της βλεπουμε το παράθυρο
    clock.tick(60)