import pygame
import random #need random to get random position
pygame.init()
pygame.display.set_caption("Diamond Game")


middleTopDoor=165 #in y value
middleLowerDoor=200 #in y value
leftWall=31 #in x value
rightWall=594 #in x value
topWall=34 #in y value
lowerWall=325 #in y value
upperRightMiddleWall=320 #in x value
upperLeftMiddleWall=294 #in x value
lowerRightMiddleWall=322 #in x value
lowerLeftMiddleWall=294 #in x value


def moveUp(x,y):
    canMove=True
    #the x shows the region the if statements are trying to detect

    if middleTopDoor<=y<=middleLowerDoor and ((leftWall>=x) or (x>=rightWall)):
        """
       |---------------------|
       |                     |
-------                       ----------
XXXXXX                       XXXXXXXXXXX
-------                       ---------
       |                    |
       |                    |
       ----------------------

        """
        canMove=True
    elif y<=topWall and upperLeftMiddleWall<=x<=upperRightMiddleWall:
        """
          | X |
    |-----| X |------|
    |                |
    |                |
    ------------------
         


        """
        canMove=True

    elif y>=(lowerWall-50) and lowerLeftMiddleWall<=x<=lowerRightMiddleWall:
        """
        |---------------|
        |               |
        |               |
        ]               |
        -----| X |-------
             | X |


        """
        canMove=True
        
    elif leftWall<=x<=rightWall and topWall<=y<=lowerWall:
        """
        |--------------|
        |              |
        |              |
        |              |
        |--------------|

        """
        canMove=True
    else:
        canMove=False
    if canMove:
        return 1
    else:
        return 0
#the code inside the moveUp, moveDown ,moveRight and moveLeft are exactly the same, so I just call moveUp inside the other three functions
def moveDown(x,y):
    if moveUp(x,y):
        return 1
    else:
        return 0

def moveRight(x,y):
    if moveUp(x,y):
        return 1
    else:
        return 0

def moveLeft(x,y):
    if moveUp(x,y):
        return 1
    else:
        return 0

def movePic(count,pic1,pic2): #to make the character look like moving by using two different pictures when moving
    if 7<count%15<15: #when count is 8-14, it will return pic1
        return pic1
    else: #when count is 0-7, return pic2
        return pic2
    #when this code is executed fast enough, for example when the frame changes more than 30 per second, the character's feet would appear as if moving up and down, instead of moving up 7 times and then moving down 7 times
    

def offScreen(x,y): #I want to make sure if object at edge of screen disappear, if will apear on the other side of screen
    #half of character is 18 for x and 20 for y
    if x<-18: #when half of character is visible at left wall
        x=windowSize[0]+18 #the other half of the character will appear at the edge of the right wall
    elif x>windowSize[0]+18: #when half of character appear out right wall
        x=-18 #the other half of character body will appear at left wall
    if y<=0: #when we saw half of character's body disappearing
        y=windowSize[1] #it reappears on the botton of the screen
    elif y>=windowSize[1]:
        y=0
    return x,y

"""
def playerTouch(pOneX,pOneY,pTwoX,pTwoY):
    xDiff=pOneX-pTwoX
    yDiff=pOneY-pTwoY
    if abs(xDiff)<36 and abs(yDiff)<42:
        for something in range(abs(xDiff)):#this loop is to change the x coordinates of the two characters
            pOneMove=moveLeft(pOneX,pOneY)+moveRight(pOneX,pOneY)
            pTwoMove=moveLeft(pTwoX,pTwoY)+moveRight(pTwoX,pTwoY)

            if xDiff>0: #which means pOneX is to the right of pTwoX
                pOneX+=pOneMove/2 #I want the two character to move far from each other, so I move them to different sides
                pTwoX-=pTwoMove/2
                                                
            else: #which means pOneX is to the left of pTwoX
                pOneX-=pOneMove/2 #I want the two character to move far from each other, so I move them to different sides
                pTwoX+=pTwoMove/2
        for something in range(abs(yDiff)):
            pOneMove=moveDown(pOneX,pOneY)+moveUp(pOneX,pOneY)
            pTwoMove=moveDown(pTwoX,pTwoY)+moveUp(pTwoX,pTwoY)
            if yDiff>0: #which means pOneY lower than pTwoY
                pOneY+=pOneMove/2 #so to increase the distance pOne should move down
                pTwoY-=pTwoMove/2 #and pTwo should move up
            else:#which means pOneY is higher than pTwoY
                pOneY-=pOneMove/2 #so to increase the distance pOne should move up
                pTwoY+=pTwoMove/2 #and pTwo should move down
                
"""

def touchCoin(x,y,coinX,coinY):
    #get the position of the coin
    #x and y can be the coordinate of either character
    if -36<=(x-coinX)<36 and -40<=(y-coinY)<40:
        return True
    else:
        return False

def coinRandomPos():
    x=random.randint(40, 605) #using the coordinate information from the outer walls
    y=random.randint(40,310) #using coordinate info, the coin must not appear in the outer walls
    return x,y

def loadAndScaleImage(img,size):
    hif=pygame.image.load(img)
    dd=pygame.transform.scale(hif,size)
    return dd

#defining variables
windowSize=[650,400]
posCharaOneX=windowSize[0]/4
posCharaOneY=windowSize[1]/2
posCharaTwoX=windowSize[0]/8
posCharaTwoY=windowSize[1]/8

pointCharacterOne=0
pointCharacterTwo=0
pOneCount=0
pTwoCount=0
oneCount=0
twoCount=0
pOneMoveing=False
pTwoMoving=False #the change of image function should only be called when when pOneMoving or pTwoMoving is true. We only want to show the character as moving when it actually moves
#when moving is false, we should display images of characters as standing.
sizeCharacter=[36,42] #here, I define the size of the character
coinPos=[55,55]

display=pygame.display.set_mode(windowSize)
clock=pygame.time.Clock() #I am using the clock to control how fast the character moves in the game loop

font=pygame.font.SysFont("comicsansms",17)#the font I want to use to display the score for each character
fonty=pygame.font.SysFont("comicsansms",20)

bac=pygame.image.load("back.png") #here, I upload the pic of background
background=pygame.transform.scale(bac,[650,400]) #I want my background pic to fit the screen exactly so I transform the size of the background pic

#loading images about character one
charaStandOne=loadAndScaleImage("person1Stand.png",sizeCharacter)
charaMoveOne1=loadAndScaleImage("person1Move.png",sizeCharacter)
charaMoveOne2=loadAndScaleImage("person1Move2.png",sizeCharacter)
#loading images about character two
charaStandTwo=loadAndScaleImage("chara2Standing.png",sizeCharacter)
charaMoveTwo1=loadAndScaleImage("chara2moving.png",sizeCharacter)
charaMoveTwo2=loadAndScaleImage("chara2moving2.png",sizeCharacter)

diamond=loadAndScaleImage("diamond.png",[20,20])

#loading the music to the game
gotCoin=pygame.mixer.Sound("coin.wav")
pygame.mixer.music.load("era - the mass.mp3")
#set volume
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1)#I want the music to play indefinitely while in the game


def preventCharacterStuckX(CharaOneX,CharaOneY): #prevent the character from getting stuck because moveUp made moving false so the character could not move when it hit the wall.
    #This is achieved by passing the character's coordinate to a function that contain a while loop that will continually add or detract from the character's coordinate and moving the character untill moveUp returns true.
    #if moveUp returns true, it will simply return the y or x coordinate
    while not moveUp(CharaOneX,CharaOneY) and CharaOneX<=leftWall:
        CharaOneX+=10
    while not moveUp(CharaOneX,CharaOneY) and CharaOneX>=rightWall:
        CharaOneX-=10
    return CharaOneX

def preventCharacterStuckY(CharaOneX,CharaOneY): #same resoning as preventCharacterStuckX
    while not moveUp(CharaOneX,CharaOneY) and CharaOneY>=lowerWall:     
        CharaOneY-=3
    while not moveUp(CharaOneX,CharaOneY)and CharaOneY<=topWall:
        CharaOneY+=3
    return CharaOneY

done=False #initalize done to false so the game will not end unless we close the game

#"The girl is the first character and the boy is the second character."
#beginning Game loop
while not done:
    pOneMoving=False #initialize moving to false at the beginning of each game loop so the character's moving motion do not change without first initialize it
    pTwoMoving=False
    key=pygame.key.get_pressed()#using keys to determine where the character move

    #make sure character one did not move or stuck to the wall.
    #this function is executed at the beginning of each game loop to constantly follow the character's change of coordinate
    posCharaOneX=preventCharacterStuckX(posCharaOneX,posCharaOneY)
    posCharaOneY=preventCharacterStuckY(posCharaOneX,posCharaOneY)
    #make sure character two did not move or stuck to the wall
    posCharaTwoX=preventCharacterStuckX(posCharaTwoX,posCharaTwoY)
    posCharaTwoY=preventCharacterStuckY(posCharaTwoX,posCharaTwoY)

    #north, south, east and west for character one
    if key[pygame.K_n]:
        posCharaOneY-=moveUp(posCharaOneX,posCharaOneY)
        pOneMoving=True
    elif key[pygame.K_s]:
        posCharaOneY+=moveDown(posCharaOneX,posCharaOneY)
        pOneMoving=True
    elif key[pygame.K_e]:
        posCharaOneX-=moveLeft(posCharaOneX,posCharaOneY)
        pOneMoving=True

    elif key[pygame.K_w]:
        posCharaOneX+=moveRight(posCharaOneX,posCharaOneY)
        pOneMoving=True
        
    #up, down, left, right for character two
    elif key[pygame.K_u]:
        posCharaTwoY-=moveUp(posCharaTwoX,posCharaTwoY)
        pTwoMoving=True
    elif key[pygame.K_d]:
        posCharaTwoY+=moveDown(posCharaTwoX,posCharaTwoY)
        pTwoMoving=True
    elif key[pygame.K_l]:
        posCharaTwoX-=moveLeft(posCharaTwoX,posCharaTwoY)
        pTwoMoving=True

    elif key[pygame.K_r]:
        posCharaTwoX+=moveRight(posCharaTwoX,posCharaTwoY)
        pTwoMoving=True
        
    if pOneMoving: #if character one is moving, then character two cannot be moving. However, when either is moving, we can test to make sure the other is still. Since the only way to make moving false for either character is in going through the game loop again, I can create separate if statement to test if either characer is still
        pOneCount+=1
        pOneImage=movePic(pOneCount,charaMoveOne1,charaMoveOne2)
    elif pTwoMoving:
        pTwoCount+=1
        pTwoImage=movePic(pTwoCount,charaMoveTwo1,charaMoveTwo2)
    if not pTwoMoving:
        pTwoImage=charaStandTwo
    if not pOneMoving:
        pOneImage=charaStandOne
    
    posCharaTwoX,posCharaTwoY=offScreen(posCharaTwoX,posCharaTwoY)
    posCharaOneX,posCharaOneY=offScreen(posCharaOneX,posCharaOneY)
    
    #check if character one touched the coin
    if(touchCoin(posCharaOneX,posCharaOneY,coinPos[0],coinPos[1])):
        oneCount+=1
        gotCoin.play()
        coinPos=coinRandomPos()
        
    elif(touchCoin(posCharaTwoX,posCharaTwoY,coinPos[0],coinPos[1])):
        twoCount+=1
        gotCoin.play()
        coinPos=coinRandomPos()

    #defining the rules 
    rule1="To move girl,press n,s,e,w correspond to North,South,East,West."
    rule2="To move boy,press u,d,l,r correspond to up,down,left,right"

    gameRule1=fonty.render(rule1,1,(255,255,255))#creating the surface to display rules
    gameRule2=fonty.render(rule2,1,(255,255,255))
    
    #creating the surface to show the points of each player
    pointCharacterOne=font.render(str(oneCount),1,(255,255,255))
    pointCharacterTwo=font.render(str(twoCount),1,(255,255,255))
    
    #combining the image and surfaces so it can appear on screen
    display.blit(background,(0,0))
    display.blit(pOneImage,[posCharaOneX,posCharaOneY])
    display.blit(pointCharacterOne,[posCharaOneX-10,posCharaOneY-10])
    display.blit(diamond ,coinPos)
    
    display.blit(pointCharacterTwo,[posCharaTwoX-10,posCharaTwoY-10])
    display.blit(pTwoImage,[posCharaTwoX,posCharaTwoY])
 
    display.blit(gameRule1,[0,20])
    display.blit(gameRule2,[0,0])
    
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True





#the code below is used to find out the coordinate of the walls of the background
#by using mouse click and mouse.get_pos()
"""
while not done:
    display.blit(background,(0,0))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos=pygame.mouse.get_pos()
            print pos
        if event.type==pygame.QUIT:
            done=True

"""
pygame.quit()
    
