import random
import pygame
from PIL import Image
pygame.init()
pygame.quit()

X = 256
Y = 256
#display_surface = pygame.display.set_mode((X, Y))
#Field_GIF = pygame.image.load(r"Image/field.gif")
#Batter_GIF = Image.open("Batter.gif")
#Baseball_GIF = Image.open("Baseball.gif")
#Field_GIF = Image.open("Field.gif")
#Fielder_GIf = Image.open("fielder.gif")
#Homerun_GIF = pygame.image.load(r"Image/homerun.gif")
#Grandslam_GIf = pygame.image.load(r"Image/grandslam.gif")
#Flyout_GIF = pygame.image.load(r"Image/flyoutanimation.gif")
#Groundout_GIF = pygame.image.load(r"Image/groundoutanimation.gif")
#display_surface.blit(Field_GIF, (0, 0))
#pygame.display.flip()
#HitOut = random.randint(1,2)

TeamA = 0
TeamB = 0
InningScore = 0
Bases = 0
First = 0
Second = 0
Third = 0
Out = 0
Strike = 0
Inning = 1
Hittype = ""
hits = ["single", "single", "single", "single", "double", "double", "double", "triple", "triple", "homerun", "foul", "foul", "foul", "out", "out", "out", "out", "out", "out"]
while Inning < 10:
  print("Inning", Inning)
  while Out < 7:
    while Strike < 3:
      pitch = random.randint(1,10)
      hit = random.randint(1,10)
      input()
      #display_surface.blit(Field_GIF, (0, 0))
      #pygame.display.flip()
      if pitch > hit:
        Strike += 1
        print("Strike", Strike)
      elif hit > pitch:
        Hittype = random.choice(hits)
        print("Hit", Hittype)
        Strike = 0
        if Hittype == "out":
          Out += 1
          print("Outs", Out)
          #if HitOut == 1:
            #display_surface.blit(Flyout_GIF, (0, 0))
          #if HitOut == 2:
            #display_surface.blit(Groundout_GIF, (0, 0))
          #pygame.display.flip()
          continue
        if Hittype == "foul" and Strike < 2:
          Strike += 1
        if Hittype == "single" and First == 0 and Second == 0 and Third == 0:
          First += 1
          continue
        if Hittype == "double" and First == 0 and Second == 0 and Third == 0:
          Second += 1
          continue
        if Hittype == "triple" and First == 0 and Second == 0 and Third == 0:
          Third += 1
          continue
        if Hittype == "single" and First > 0 and Second == 0 and Third == 0:
          Second += 1
          continue
        if Hittype == "double" and First > 0 and Second == 0 and Third  == 0:
          Second += 1
          Third += 1
          First = 0
          continue
        if Hittype == "triple" and First > 0 and Second == 0 and Third == 0:
          Third += 1
          TeamA +=1
          TeamB += 1
          InningScore += 1
          First = 0
          continue
        if Hittype == "single" and Second > 0 and First == 0 and Third == 0:
          First += 1
          Third += 1
          Second = 0
          continue
        if Hittype == "double" and Second > 0 and First == 0 and Third == 0:
          TeamA += 1
          TeamB += 1
          InningScore += 1
          continue
        if Hittype == "triple" and Second > 0 and First == 0 and Third == 0:
          Third += 1
          TeamA += 1
          TeamB += 1
          InningScore += 1
          Second = 0
          continue
        if Hittype == "single" and Third > 0 and Second == 0 and First == 0:
          First += 1
          TeamA += 1
          TeamB += 1
          InningScore += 1
          Third = 0
          continue
        if Hittype == "double" and Third > 0 and Second == 0 and First == 0:
          Second += 1
          TeamA +=1
          TeamB += 1
          InningScore += 1
          Third = 0
          continue
        if Hittype == "triple" and Third > 0 and Second == 0 and First == 0:
          TeamA += 1
          TeamB += 1
          InningScore += 1
          continue
        if Hittype == "single" and First > 0 and Second > 0 and Third == 0:
          Third += 1
          continue
        if Hittype == "double" and First > 0 and Second > 0 and Third == 0:
          Third += 1
          TeamA += 1
          TeamB += 1
          InningScore += 1
          First = 0
          continue
        if Hittype == "triple" and First > 0 and Second > 0 and Third == 0:
          First = 0
          Second = 0
          Third += 1
          TeamA += 2
          TeamB += 2
          InningScore += 2
          continue
        if Hittype == "single" and Second > 0 and Third > 0 and First == 0:
          First +=1 
          Second = 0
          TeamA += 1
          TeamB += 1
          InningScore += 1
          continue
        if Hittype == "double" and Second > 0 and Third > 0 and First == 0:
          Third = 0
          TeamA += 2
          TeamB += 2
          InningScore += 2
          continue
        if Hittype == "triple" and Second > 0 and Third > 0 and First == 0:
          TeamA += 2
          TeamB += 2
          InningScore += 2
          Second = 0
          continue
        if Hittype == "single" and First > 0 and Third > 0 and Second == 0:
          Second += 1
          TeamA += 1
          TeamB += 1
          InningScore += 1
          Third = 0
          continue
        if Hittype == "double" and First > 0 and Third > 0 and Second == 0:
          Second += 1
          TeamA += 1
          TeamB += 1
          InningScore += 1
          Third = 0
          continue
        if Hittype == "triple" and First > 0 and Third > 0 and Second == 0:
          TeamA += 2
          TeamB += 2
          InningScore += 2
          First = 0
          continue
        if Hittype == "single" and First > 0 and Second > 0 and Third > 0:
          TeamA += 1
          TeamB += 1
          InningScore += 1
          continue
        if Hittype == "double" and First > 0 and Second > 0 and Third > 0:
          First = 0
          TeamA += 2
          TeamB += 2
          InningScore += 2
          continue
        if Hittype == "triple" and First > 0 and Second > 0 and Third > 0:
          First = 0
          Second = 0
          TeamA += 3
          TeamB += 3
          InningScore += 3
          continue
        if Hittype == "homerun":
          Bases += 1
          Bases + First + Second + Third
          Bases + TeamA
          Bases + TeamB
          Bases + InningScore
          Bases = 0
          #display_surface.blit(Homerun_GIF, (0, 0))
          #pygame.display.flip()
      else:
        print("Foul")
        if Strike < 2:
          Strike += 1
      if Strike == 3:
        Out += 1
        Strike = 0
        print("StrikeOut")
        print("Outs", Out)
      if Out == 3:
        TeamB -= InningScore
        InningScore = 0
        print("Visitor", TeamA, "Home", TeamB)
        First = 0
        Second = 0
        Third = 0
        Strike = 0
      if Out == 6:
        TeamA -= InningScore
        InningScore = 0
        print("Visitor", TeamA, "Home", TeamB)
        Out = 0
        Strike = 0
        First = 0
        Second = 0
        Third = 0
    Inning += 1
    print("Inning", Inning)