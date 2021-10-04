import turtle
import sys
import random
import math
import time


game_start = False
start_of_game = True
computer = False

snowflake = "https://previews.123rf.com/images/31moonlight31/31moonlight311707/31moonlight31170700099/83089676-big-translucent-christmas-snowflake-in-blue-colors-on-transparent-background-transparency-only-in-ve.jpg"
#create screen

screen = turtle.Screen()
screen.bgcolor("cyan")
screen.tracer(3)
screen.addshape(snowflake)

#create border

border = turtle.Turtle()
border.speed(0)
border.penup()
border.setposition(-300,-300)
border.pendown()
border.pensize(4)
for side in range(4):
  border.forward(600)
  border.left(90)
border.hideturtle()


#create score

goals = []
speedp1 = 1
speedp2 = 2
playershoot = False
player1score = 0
player2score = 0
timer_part1 = time.time() + 60

player1 = turtle.Turtle()
player1.penup()
player1.speed(0)
player1.setposition(-250,0)


player2 = turtle.Turtle()
player2.penup()
player2.speed(0)
player2.setposition(250,0)
player2.setheading(180)





goal1 = turtle.Turtle()
goal1.speed(0)
goal1.shape("circle")
goal1.color("green")
goal1.penup()
goal1.setposition(random.randint(-280,280),random.randint(-280,280))
goals.append(goal1)

goal2 = turtle.Turtle()
goal2.speed(0)
goal2.shape("circle")
goal2.color("green")
goal2.penup()
goal2.setposition(random.randint(-280,280),random.randint(-280,280))
goals.append(goal2)

goal3 = turtle.Turtle()
goal3.speed(0)
goal3.shape("circle")
goal3.color("green")
goal3.penup()
goal3.setposition(random.randint(-280,280),random.randint(-280,280))
goals.append(goal3)

goal4 = turtle.Turtle()
goal4.speed(0)
goal4.shape("circle")
goal4.color("green")
goal4.penup()
goal4.setposition(random.randint(-280,280),random.randint(-280,280))
goals.append(goal4)

choose_game = turtle.Turtle()
choose_game.hideturtle()
choose_game.penup()
choose_game.speed(0)
choose_game.setposition(0,340)
choose_game.color("red")
choose_game.write("(1): vs. Computer or (2): vs. player",align = "center", font = ("Ariel",14,"normal"))

score1 = turtle.Turtle()
score1.speed(0)
score1.penup()
score1.hideturtle()
score1.setposition(-280,340)

ice1 = turtle.Turtle()
ice1.hideturtle()
ice1.speed(0)
ice1.shape("circle")
ice1.color("blue")
ice1.penup()
ice1.setposition(-800,-800)
goals.append(ice1)

killer_mode = turtle.Turtle()
killer_mode.hideturtle()
killer_mode.speed(0)
killer_mode.shape("circle")
killer_mode.color("red")
killer_mode.penup()
killer_mode.setposition(-800,-800)
goals.append(killer_mode)

kill_i = turtle.Turtle()
kill_i.speed(0)
kill_i.shape("circle")
kill_i.color("red")
kill_i.hideturtle()
kill_i.penup()
kill_i.setposition(-280,360)

#ice2 = turtle.Turtle()
#ice2.speed(0)
#ice2.shape("circle")
#ice2.color("blue")
#ice2.hideturtle()
#ice2.penup()
#ice2.setposition(-800,-800)

score2 = turtle.Turtle()
score2.speed(0)
score2.penup()
score2.hideturtle()
score2.setposition(280,340)

scorewriter1 = turtle.Turtle()
scorewriter1.speed(0)
scorewriter1.penup()
scorewriter1.hideturtle()
scorewriter1.setposition(-280,360)
scorewriter1.write("Player 1:",align = "left", font = ("Ariel",14,"normal"))

scorewriter2 = turtle.Turtle()
scorewriter2.speed(0)
scorewriter2.penup()
scorewriter2.hideturtle()
scorewriter2.setposition(280,360)
scorewriter2.write("Player 2:",align = "right", font = ("Ariel",14,"normal"))

playerwin = turtle.Turtle()
playerwin.speed(0)
playerwin.penup()
playerwin.hideturtle()
playerwin.setposition(0,360)

collision = turtle.Turtle()
collision.speed(0)
collision.penup()
collision.hideturtle()
collision.setposition(0,0)

#imer_num = turtle.Turtle()
#timer_num.speed(0)
#timer_num.penup()
#timer_num.hideturtle()
#timer_num.setposition(0,330)

invisible_center = turtle.Turtle()
invisible_center.speed(0)
invisible_center.penup()
invisible_center.hideturtle()
invisible_center.setposition(0,0)

cooldown = 0
def distance(turtle1,turtle2):
  d = math.sqrt(math.pow(turtle1.xcor() - turtle2.xcor(),2) + math.pow(turtle1.ycor() - turtle2.ycor(),2))
  return d
#player 1
def turn_left():
  player1.left(30)
def turn_right():
  player1.right(30)
def speedUp():
  global speedp1
  if speedp1 <3:
    speedp1 += .5
  else:
    speedp1 = 3
def slowDown():
  global speedp1
  if speedp1 > 0:
    speedp1 -= .5
  else: 
    speedp1 = 0

def checkbounds(turtle):
  if turtle.xcor() > 295:
    ycord = turtle.ycor()
    turtle.setposition(-295,ycord)
  if turtle.xcor() <-295:
    ycord = turtle.ycor()
    turtle.setposition(295,ycord)
  if turtle.ycor() >295:
    xcord = turtle.xcor()
    turtle.setposition(xcord,-295)
  if turtle.ycor() < -295:
    xcord = turtle.xcor()
    turtle.setposition(xcord,295)

def isCollision(turtle1,turtle2):
  d = math.sqrt(math.pow(turtle1.xcor() - turtle2.xcor(),2) + math.pow(turtle1.ycor() - turtle2.ycor(),2))
  if d < 15:
    return True
  else:
    return False

def isCollision2(turtle1,turtle2):
  d = math.sqrt(math.pow(turtle1.xcor() - turtle2.xcor(),2) + math.pow(turtle1.ycor() - turtle2.ycor(),2))
  if d < 6:
    return True
  else:
    return False
 
def playerunoscore(score):
  score1.write("|",align = "left",font = ("Ariel",14,"normal"))
  score1.forward(10)

def playerdosscore(score):
  score2.write("|", align = "right", font = ("Ariel",14,"normal"))
  score2.backward(10)

#player2

trajectory = False

def closest_point(turtle):
  min1 = 10000
  min_point = None
  for point in goals:
    d = distance(point,turtle)
    if d < min1:
      min1 =  d
      min_point = point
  return min_point
def computer_angle(point,turtle):
  turtle.setheading(turtle.towards(point))
def computer_angle_away(point,turtle):
  turtle.setheading(turtle.towards(point) + 180)
  

def turn_left2():
  global computer
  if not computer:
    player2.left(30)
def turn_right2():
  global comuter
  if not computer:
    player2.right(30)
def speedUp2():
  global speedp2
  global computer
  if not computer:
    if speedp2 <3:
      speedp2 += .5
def slowDown2():
  global speedp2
  global computer
  if not computer:
    if speedp2 >0:
      speedp2 -= .5

def one_player():
  global start_of_game
  global computer
  global game_start
  global choose_game
  if start_of_game:
    computer = True
    start_of_game = False
    game_start = True
    choose_game.clear()

def two_player():
  global start_of_game
  global game_start
  global choose_game
  if start_of_game:
    start_of_game = False
    game_start = True
    choose_game.clear()


screen.onkey(turn_left2,"Left")
screen.onkey(turn_right2,"Right")
screen.onkey(speedUp2,"Up")
screen.onkey(slowDown2,"Down")
screen.onkey(turn_left,"A")
screen.onkey(turn_right,"D")
screen.onkey(speedUp,"W")
screen.onkey(slowDown,"S")
screen.onkey(one_player,"1")
screen.onkey(two_player,"2")

screen.listen()






#ice_time_begin2 = time.time()
player2frozen = False
player1frozen = False
player1killer = False
player2killer = False
frame_rate = 0
freeze_begin = 0
freeze_begin1 = 0
kill_begin = 0
kill_begin1 = 0

frames = []


def play_game():
  global frames
  global frame_rate
  global trajectory
  global score_time_begin
  global ice_time_begin
  global killermode_time_begin
  global player2frozen
  global player1frozen
  global player1killer
  global player2killer
  global freeze_begin
  global freeze_begin1
  global kill_begin
  global kill_begin1
  global speedp1
  global speedp2
  global computer
  global player1score
  global player2score
  global player1
  global player2
  global goal1
  global goal2
  global goal3
  global goal4
  global ice1
  global killer_mode
  global kill_i
  global collision
  frame_rate = time.time()
  #timer_number = timer_part1 - time.time()
  if player1frozen == False:
    player1.forward(speedp1)
  checkbounds(player1)
  if computer == True:
    if player2killer:
      computer_angle(player1,player2)
    elif player1killer:
      if distance(player1,player2) <80 and not player1frozen:
        computer_angle_away(player1,player2)
        speedp2 = 2.5
      else:
        speedp2 = 2
        if not trajectory: 
          computer_angle(closest_point(player2),player2)
          trajectory = True
    else:
      if not trajectory:
        computer_angle(closest_point(player2),player2)
        trajectory = True
  if player2frozen == False:
    player2.forward(speedp2)
  checkbounds(player2)
  if isCollision(player1,goal1) == True:
    if time.time() > score_time_begin:
      player1score += 1
      playerunoscore(player1score)
      score_time_begin = time.time()
      print("Player 1 score",player1score)
      goal1.setposition(random.randint(-280,280),random.randint(-280,280))
      trajectory = False

  if isCollision(player1,goal2) == True:
    if time.time() > score_time_begin:
      player1score += 1
      playerunoscore(player1score)
      score_time_begin = time.time()
      print("Player 1 score",player1score)
      goal2.setposition(random.randint(-280,280),random.randint(-280,280))
      trajectory = False
  if isCollision(player1,goal3) == True: 
    if time.time() > score_time_begin:
      player1score += 1
      playerunoscore(player1score)
      score_time_begin = time.time()
      print("Player 1 score",player1score)
      goal3.setposition(random.randint(-280,280),random.randint(-280,280))
      trajectory = False
  if isCollision(player1,goal4) == True:
    if time.time() > score_time_begin:
      player1score += 1
      playerunoscore(player1score)
      score_time_begin = time.time()
      print("Player 1 score",player1score)
      goal4.setposition(random.randint(-280,280),random.randint(-280,280))
      trajectory = False
    #Player 2 score 
  if isCollision(player2,goal1) == True:
    if time.time() > score_time_begin:
      player2score += 1
      playerdosscore(player2score)
      score_time_begin = time.time()
      print("Player2 score",player2score)
      goal1.setposition(random.randint(-280,280),random.randint(-280,280))  
      trajectory = False
  if isCollision(player2,goal2) == True:
    if time.time() > score_time_begin:
      player2score += 1
      playerdosscore(player2score)
      score_time_begin = time.time()
      print("Player2 score",player2score)
      goal2.setposition(random.randint(-280,280),random.randint(-280,280))
      trajectory = False
  if isCollision(player2,goal3) == True: 
    if time.time() > score_time_begin:
      player2score += 1
      playerdosscore(player2score)
      score_time_begin = time.time()
      print("Player2 score",player2score)
      goal3.setposition(random.randint(-280,280),random.randint(-280,280))
      trajectory = False
  if isCollision(player2,goal4) == True:
    if time.time() > score_time_begin:
      player2score += 1
      playerdosscore(player2score)
      score_time_begin = time.time()
      print("Player2 score",player2score)
      goal4.setposition(random.randint(-280,280),random.randint(-280,280))
      trajectory = False
  #timer_num.write(int(timer_number),align = "center", font = ("Ariel",14,"normal"))
  #timer_num.clear()
  #if timer_number <= 0:
    #
  if time.time() >= ice_time_begin + 5:
    ice1.setposition(random.randint(-280,280),random.randint(-280,280))
    trajectory = False
    ice1.showturtle()
    ice_time_begin += 10
  if time.time() >= killermode_time_begin + 7:
    killer_mode.setposition(random.randint(-280,280),random.randint(-280,280))
    trajectory = False
    killer_mode.showturtle()
    killermode_time_begin += 12
  
  if player1frozen == True:
    player1.color("blue")
  elif player1killer == True:
    player1.color("red")
  else:
    player1.color("black")
  
  if player2frozen == True:
    player2.color("blue")
  elif player2killer == True:
    player2.color("red")
  else:
    player2.color("black")
  
  if computer:
    if player2killer:
      speedp2 = 2.5
    else:
      speedp2 = 2


  #if time.time() >= ice_time_begin2 + 12:
   # ice2.setposition(random.randint(-280,280),random.randint(-280,280))
    #ice2.showturtle()
    #ice_time_begin2 += 20
  if isCollision(player1,ice1) == True:
    ice1.setposition(-800,-800)
    trajectory = False
    freeze_begin1 = time.time()
    player2frozen = True

  
  if isCollision(player1,killer_mode) == True:
    killer_mode.setposition(-800,-800)
    trajectory = False
    kill_begin = time.time()
    kill_i.setposition(-300,360)
    kill_i.showturtle()

    player1killer = True
  if isCollision(player2,killer_mode) == True:
    killer_mode.setposition(-800,-800)
    trajectory = False
    kill_begin1 = time.time()
    kill_i.setposition(300,360)
    kill_i.showturtle()

    player2killer = True

  #if isCollision(player1,ice2) == True:
    #ice2.setposition(-800,-800)
    #freeze_begin = time.time()
    #player2frozen = True
   # speedp2 = 0

  if time.time() >= kill_begin + 8:
    player1killer = False
    kill_i.hideturtle()
  if time.time() >= kill_begin1 + 8:
    player2killer = False
    kill_i.hideturtle()
    

  if time.time() >= freeze_begin1 + 4:
    player2frozen = False
  if isCollision(player2,ice1) == True:
    ice1.setposition(-800,-800)
    trajectory = False
    freeze_begin = time.time()
    player1frozen = True
  #if isCollision(player2,ice2) == True:
    #ice2.setposition(-800,-800)
    #freeze_begin = time.time()
   # player1frozen = True
    #speedp1 = 0
    #speedp2
  if time.time() >= freeze_begin + 4:
    player1frozen = False
  if isCollision2(player1,player2) == True:
    if player2killer == False and player1killer == False:
      collision.write("Spaceships have crashed. Game Over",align = "center", font = ("Ariel",14,"normal"))
    elif player2killer == True and player1killer == True:
      if computer:
        collision.write("Player 1 and the computer have kiled each other!!!",align = "center", font = ("Ariel",14,"normal"))
      else:
        collision.write("Player 1 and Player 2 have kiled each other!!!",align = "center", font = ("Ariel",14,"normal"))
    elif player2killer == True:
      if computer:
        collision.write("The computer has killed Player 1 !!!",align = "center", font = ("Ariel",14,"normal"))
      else:
        collision.write("Player 2 has killed Player 1 !!!",align = "center", font = ("Ariel",14,"normal"))
    elif player1killer == True:
      if computer:
        collision.write("Player 1 has killed the computer !!!",align = "center", font = ("Ariel",14,"normal"))
      else:
        collision.write("Player 1 has killed Player 2 !!!",align = "center", font = ("Ariel",14,"normal"))
    return False
  if player1score == 10:
    return False
  if player2score == 10:
    return False
  fps = time.time() -frame_rate
  if computer:
    if fps < 0.039:
      time.sleep(0.039 - fps)
  return True
while True:
  if game_start:
    if not play_game():
      break
  else:
    score_time_begin = 0
    ice_time_begin = time.time()
    killermode_time_begin = time.time()


playerwin.color("gold")


if player2killer == True and player1killer == True and player1score < 10 and player2score <10:
  playerwin.write("No one wins",align = "center", font=("Ariel",30,"normal"))
elif player1killer == True and player1score < 10 and player2score <10:
  playerwin.write("Player 1 wins",align = "center", font=("Ariel",30,"normal"))
elif player2killer == True and player1score < 10 and player2score <10:
  if computer:
    playerwin.write("The computer wins",align = "center", font=("Ariel",30,"normal"))
  else:
    playerwin.write("Player 2 wins",align = "center", font=("Ariel",30,"normal"))
elif player1score > player2score:
  playerwin.write("Player 1 wins",align = "center", font=("Ariel",30,"normal"))
elif player2score > player1score:
  if computer:
    playerwin.write("The computer wins",align = "center", font=("Ariel",30,"normal"))
  else:
    playerwin.write("Player 2 wins",align = "center", font=("Ariel",30,"normal"))
elif player1score == player2score:
  playerwin.write("It's a tie",align = "center", font=("Ariel",30,"normal"))
else:
  playerwin.write("Computer is unable to tell what has happened, Nobody wins",align = "center", font=("Ariel",30,"normal"))