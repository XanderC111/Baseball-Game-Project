import random
import pygame
from PIL import Image
import time
pygame.init()
pygame.quit()

X = 256
Y = 256
screen = pygame.display.set_mode((X, Y))
display_surface = pygame.display.set_mode((X, Y))
Field_GIF = pygame.image.load(r"Image/field.gif")
Homerun_GIF = pygame.image.load(r"Image/Homerun1.gif")
GrandSlam_GIF = pygame.image.load(r"Image/GrandSlam1.gif")
BasesFirst_GIF = pygame.image.load(r"Image/BasesFirst.gif")
BasesSecond_GIF = pygame.image.load(r"Image/BasesSecond.gif")
BasesThird_GIF = pygame.image.load(r"Image/BasesThird.gif")
BasesFirstAndSecond_GIF = pygame.image.load(r"Image/BasesFirstAndSecond.gif")
BasesFirstAndThird_GIF = pygame.image.load(r"Image/BasesFirstAndThird.gif")
BasesSecondAndThird_GIF = pygame.image.load(r"Image/BasesSecondAndThird.gif")
BasesLoaded_GIF = pygame.image.load(r"Image/BasesLoaded.gif")
display_surface.blit(Field_GIF, (0, 0))
pygame.display.flip()

TeamA = 0
TeamB = 0
InningScore = 0
Bases = 1
First = 0
Second = 0
Third = 0
Out = 0
Strike = 0
Inning = 1
Hittype = ""
hits = ["single", "single", "single", "single", "double", "double", "double", "triple", "triple", "homerun", "foul", "foul", "foul", "foul", "out", "out", "out", "out", "out", "out", "out", "out", "out", "out", "out", "out"]

while Inning < 10:
  print("Inning", Inning)
  while Out < 8:
    while Strike < 3:
      if Inning == 10:
        break
      if Out == 3:
        TeamB -= InningScore
        InningScore = 0
        print("Visitor", TeamA, "Home", TeamB)
        First = 0
        Second = 0
        Third = 0
        Strike = 0
        Out += 1
      if Out == 7:
        TeamA -= InningScore
        InningScore = 0
        Inning += 1
        print("Inning", Inning)
        print("Visitor", TeamA, "Home", TeamB)
        Out = 0
        Strike = 0
        First = 0
        Second = 0
        Third = 0
      if First == 0 and Second == 0 and Third == 0:
        display_surface.blit(Field_GIF, (0, 0))
        pygame.display.flip()
      if First > 0 and Second == 0 and Third == 0:
        display_surface.blit(BasesFirst_GIF, (0, 0))
        pygame.display.flip()
      if Second > 0 and First == 0 and Third == 0:
        display_surface.blit(BasesSecond_GIF, (0, 0))
        pygame.display.flip()
      if Third > 0 and First == 0 and Second == 0:
        display_surface.blit(BasesThird_GIF, (0, 0))
        pygame.display.flip()
      if First > 0 and Second > 0 and Third == 0:
        display_surface.blit(BasesFirstAndSecond_GIF, (0, 0))
        pygame.display.flip()
      if First > 0 and Third > 0 and Second == 0:
        display_surface.blit(BasesFirstAndThird_GIF, (0, 0))
        pygame.display.flip()
      if Second > 0 and Third > 0 and First == 0:
        display_surface.blit(BasesSecondAndThird_GIF, (0, 0))
        pygame.display.flip()
      if First > 0 and Second > 0 and Third > 0:
        display_surface.blit(BasesLoaded_GIF, (0, 0))
        pygame.display.flip()
      input()
      pitch = random.randint(2,10)
      hit = random.randint(1,10)
      if pitch > hit:
        Strike += 1
        print("Strike", Strike)
      elif hit > pitch:
        Hittype = random.choice(hits)
        print("Hit", Hittype)
        if Hittype == "out":
          Out += 1
          Strike = 0
          if Out == 5 or Out == 6 or Out == 7:
            print("Outs", Out - 4)
          else:
            print("Outs", Out)
          HitOut = random.randint(1,2)
          if HitOut == 1:
            FlyOutAnimation = ["Image/FlyOut01.gif", "Image/FlyOut02.gif", "Image/FlyOut03.gif", "Image/FlyOut04.gif", "Image/FlyOut05.gif", "Image/FlyOut06.gif", "Image/FlyOut07.gif", "Image/FlyOut08.gif", "Image/FlyOut09.gif", "Image/FlyOut10.gif", "Image/FlyOut11.gif", "Image/FlyOut12.gif", "Image/FlyOut13.gif", "Image/FlyOut14.gif", "Image/FlyOut15.gif", "Image/FlyOut16.gif", "Image/FlyOut17.gif", "Image/FlyOut18.gif", "Image/FlyOut19.gif"]
            FlyOut = {}
            for img in FlyOutAnimation:
              FlyOut[img] = pygame.image.load(img)
            for img in FlyOutAnimation:
              screen.blit(FlyOut[img], (0, 0))
              pygame.time.delay(45)
              pygame.display.flip()
          elif HitOut == 2:
            GroundOutAnimation = ["Image/GroundOut01.gif", "Image/GroundOut02.gif", "Image/GroundOut03.gif", "Image/GroundOut04.gif", "Image/GroundOut05.gif", "Image/GroundOut06.gif", "Image/GroundOut07.gif", "Image/GroundOut08.gif", "Image/GroundOut09.gif", "Image/GroundOut10.gif", "Image/GroundOut11.gif", "Image/GroundOut12.gif", "Image/GroundOut13.gif", "Image/GroundOut14.gif", "Image/GroundOut15.gif", "Image/GroundOut16.gif", "Image/GroundOut17.gif", "Image/GroundOut18.gif", "Image/GroundOut19.gif", "Image/GroundOut20.gif", "Image/GroundOut21.gif", "Image/GroundOut22.gif", "Image/GroundOut23.gif", "Image/GroundOut24.gif", "Image/GroundOut25.gif", "Image/GroundOut26.gif"]
            GroundOut = {}
            for img in GroundOutAnimation:
              GroundOut[img] = pygame.image.load(img)
            for img in GroundOutAnimation:
              screen.blit(GroundOut[img], (0, 0))
              pygame.time.delay(80)
              pygame.display.flip()
          continue
        if Hittype == "foul" and Strike < 2:
          Strike += 1
          continue
        elif Hittype == "foul":
          continue
        Strike = 0
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
          if First == 0 and Second == 0 and Third == 0:
            TeamA += 1
            TeamB += 1
            InningScore += 1
          if First > 0 and Second == 0 and Third ==0:
            TeamA += 2
            TeamB += 2
            InningScore += 2
            First = 0
          if Second > 0 and First == 0 and Third == 0:
            TeamA += 2
            TeamB += 2
            InningScore += 2
            Second = 0
          if Third > 0 and First == 0 and Second == 0:
            TeamA += 2
            TeamB += 2
            InningScore += 2
            Third = 0
          if First > 0 and Second > 0 and Third == 0:
            TeamA += 3
            TeamB += 3
            InningScore += 3
            First = 0
            Second = 0
          if Second > 0 and Third > 0 and First == 0:
            TeamA += 3
            TeamB += 3
            InningScore += 3
            Second = 0
            Third = 0
          if First > 0 and Third > 0 and Second == 0:
            TeamA += 3
            TeamB += 3
            InningScore += 3
            First = 0
            Third = 0
          if First > 0 and Second > 0 and Third > 0:
            TeamA += 4
            TeamB += 4
            InningScore += 4
            First = 0
            Second = 0
            Third = 0
            print("GrandSlam")
            display_surface.blit(GrandSlam_GIF, (0, 0))
            pygame.display.flip()
          display_surface.blit(Homerun_GIF, (0, 0))
          pygame.display.flip()
      else:
        print("Foul")
        if Strike < 2:
          Strike += 1
      if Strike == 3:
        Out += 1
        Strike = 0
        print("StrikeOut")
        if Out == 5 or Out == 6 or Out == 7:
          print("Outs", Out - 4)
        else:
          print("Outs", Out)

print("Game Over")