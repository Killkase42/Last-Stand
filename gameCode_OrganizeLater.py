import pygame
import random

#Initialize Pygame.
pygame.init()


#Create screen.
screen = pygame.display.set_mode((1728, 972))


clock = pygame.time.Clock()


#Title and Icon
pygame.display.set_caption('Last Stand')
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)


#Colours
white = (255, 255, 255)
lightGrey = (95, 95, 95)
black = (0, 0, 0)
orange = (225, 98, 0)
lightOrange = (245, 118, 0)


#Displaying text in various colours.
def textObjectsBlack(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def textObjectsWhite(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()

def printWhiteText(text, size, x, y ):
    descriptionText = pygame.font.Font('freesansbold.ttf', size)
    textSurf, textRect = textObjectsWhite(text, descriptionText)
    textRect.center = (x, y)
    screen.blit(textSurf, textRect)


#Battle button needs a separate function due to its shape and function.
def battleButton(action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if 968 > mouse[0] > 770 and 73 > mouse[1] > 13:
        pygame.draw.rect(screen, lightOrange, [784, 13, 170, 60])
        pygame.draw.rect(screen, lightOrange, [770, 13, 7, 60])
        pygame.draw.rect(screen, lightOrange, [961, 13, 7, 60])
        if click[0] == 1 and action != None:
            if action == "play":
                confirmationScreen()

    # add sound later
    else:
        pygame.draw.rect(screen, orange, [784, 13, 170, 60])
        pygame.draw.rect(screen, orange, [770, 13, 7, 60])
        pygame.draw.rect(screen, orange, [961, 13, 7, 60])
    battleText = pygame.font.Font('freesansbold.ttf', 40)
    textSurf, textRect = textObjectsBlack('BATTLE', battleText)
    textRect.center = (869, 43)
    screen.blit(textSurf, textRect)





#The large button with picture, enters player into the game and also runs select enemies function (should be above this one in the code).
def enterGameButton(action=None):
    enterGameButton = pygame.image.load('lastStand.png')
    enterGameButtonX = 502
    enterGameButtonY = 180

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if 1226 > mouse[0] > 502 and 488 > mouse[1] > 180:
        pygame.draw.rect(screen, orange, [500, 178, 728, 312])
        screen.blit(enterGameButton, (enterGameButtonX, enterGameButtonY))
        if click[0] == 1 and action != None:
            if action == "play":
                gameLoop()


    # add sound later
    else:
        screen.blit(enterGameButton, (enterGameButtonX, enterGameButtonY))



#Selected ships.
fleetSlotOne = 'Pioneer'
fleetSlotTwo = 'Colossus'
fleetSlotThree = 'Venturer'


#Menu screen.
def gameMenu():
    splashScreenVariable = True
    menu = True

    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        splashScreenBackground = pygame.image.load('expandedMapBackground.png')
        splashScreen = pygame.image.load('splashScreen.png')

        screen.fill(black)

        #Drawing upper background (behind battle button).
        upperBackground = pygame.image.load('upperBackground.png')
        upperBackgroundX = 0
        upperBackgroundY = 0

        screen.blit(upperBackground, (upperBackgroundX, upperBackgroundY))

        # Backgrounds behind selectable ships.
        Background = pygame.image.load('shipSelectionBackground.png')
        screen.blit(Background, (17, 810))
        screen.blit(Background, (304, 810))
        screen.blit(Background, (585, 810))
        screen.blit(Background, (867, 810))
        screen.blit(Background, (1150, 810))
        screen.blit(Background, (1436, 810))

        #Logos on top of backgrounds.
        logoUSR = pygame.image.load('logoUSR.png')
        screen.blit(logoUSR, (45, 830))
        screen.blit(logoUSR, (335, 830))

        logoZRK = pygame.image.load('logoZRK.png')
        screen.blit(logoZRK, (615, 830))




        if splashScreenVariable == False:
            battleButton("play")

        if splashScreenVariable == True:
            pygame.draw.rect(screen, orange, [784, 13, 170, 60])
            pygame.draw.rect(screen, orange, [770, 13, 7, 60])
            pygame.draw.rect(screen, orange, [961, 13, 7, 60])
            battleText = pygame.font.Font('freesansbold.ttf', 40)
            textSurf, textRect = textObjectsBlack('BATTLE', battleText)
            textRect.center = (869, 43)
            screen.blit(textSurf, textRect)
            screen.blit(splashScreenBackground, (1, 1))
            pygame.draw.rect(screen, lightGrey, [496, 100, 736, 700])
            screen.blit(splashScreen, (502, 106))

            objective1Text = pygame.font.Font('freesansbold.ttf', 15)
            textSurf, textRect101 = textObjectsWhite('Objective:', objective1Text)
            textRect101.center = (541, 430)
            screen.blit(textSurf, textRect101)
            objective2Text = pygame.font.Font('freesansbold.ttf', 15)
            textSurf, textRect102 = textObjectsWhite('Your main objective is to defend the outpost from the Swarm. Each wave, enemies will appear in a', objective2Text)
            textRect102.center = (856, 450)
            screen.blit(textSurf, textRect102)
            objective3Text = pygame.font.Font('freesansbold.ttf', 15)
            textSurf, textRect103 = textObjectsWhite("sector and advance towards that sector's base. If the enemies are not destroyed in a certain", objective3Text)
            textRect103.center = (832, 470)
            screen.blit(textSurf, textRect103)
            objective4Text = pygame.font.Font('freesansbold.ttf', 15)
            textSurf, textRect104 = textObjectsWhite("amount of time, they will capture the sector's base and move on to the outpost. From here, they", objective4Text)
            textRect104.center = (843, 490)
            screen.blit(textSurf, textRect104)
            objective5Text = pygame.font.Font('freesansbold.ttf', 15)
            textSurf, textRect105 = textObjectsWhite("will proceed to damage the base's turrets (which will also damage the enemies). When all three", objective5Text)
            textRect105.center = (843, 510)
            screen.blit(textSurf, textRect105)
            objective6Text = pygame.font.Font('freesansbold.ttf', 15)
            textSurf, textRect106 = textObjectsWhite("turrets are destroyed, the enemies in the outpost's sector will be able to damage the outpost", objective6Text)
            textRect106.center = (834, 530)
            screen.blit(textSurf, textRect106)
            objective7Text = pygame.font.Font('freesansbold.ttf', 15)
            textSurf, textRect107 = textObjectsWhite("until they are destroyed. If the base's health reaches zero, the game is over.", objective7Text)
            textRect107.center = (772, 550)
            screen.blit(textSurf, textRect107)

            controls1Text = pygame.font.Font('freesansbold.ttf', 15)
            textSurf, textRect1 = textObjectsWhite('Controls:', controls1Text)
            textRect1.center = (536, 580)
            screen.blit(textSurf, textRect1)
            controls6Text = pygame.font.Font('freesansbold.ttf', 15)
            textSurf, textRect6 = textObjectsWhite('F (Selects Enemy the Mouse is Hovered Over)', controls6Text)
            textRect6.center = (668, 600)
            screen.blit(textSurf, textRect6)
            controls2Text = pygame.font.Font('freesansbold.ttf', 15)
            textSurf, textRect2 = textObjectsWhite('Number Keys (Abilities; Use Missiles When Enemy is Selected)', controls2Text)
            textRect2.center = (728, 620)
            screen.blit(textSurf, textRect2)
            controls3Text = pygame.font.Font('freesansbold.ttf', 15)
            textSurf, textRect3 = textObjectsWhite('Left Mouse Click (Main Weapon)', controls3Text)
            textRect3.center = (620, 640)
            screen.blit(textSurf, textRect3)
            controls4Text = pygame.font.Font('freesansbold.ttf', 15)
            textSurf, textRect4 = textObjectsWhite('Tab (Open Expanded Map View, Click on Points to Move/Use Jump Drive)', controls4Text)
            textRect4.center = (766, 660)
            screen.blit(textSurf, textRect4)
            controls5Text = pygame.font.Font('freesansbold.ttf', 15)
            textSurf, textRect5 = textObjectsWhite('Left/Right Arrow Keys (Switch Selected Ship)', controls5Text)
            textRect5.center = (668, 680)
            screen.blit(textSurf, textRect5)


            pygame.draw.rect(screen, orange, [790, 720, 150, 50])
            splashText = pygame.font.Font('freesansbold.ttf', 40)
            textSurf, textRect200 = textObjectsWhite('Start', splashText)
            textRect200.center = (864, 748)
            screen.blit(textSurf, textRect200)
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            if 940 > mouse[0] > 790 and 870 > mouse[1] > 720:
                pygame.draw.rect(screen, lightOrange, [790, 720, 150, 50])
                splashText = pygame.font.Font('freesansbold.ttf', 40)
                textSurf, textRect200 = textObjectsWhite('Start', splashText)
                textRect200.center = (864, 748)
                screen.blit(textSurf, textRect200)
                if click[0] == 1:
                    splashScreenVariable = False


        pygame.display.update()
        clock.tick(60)


#Confirmation to enter the game.
def confirmationScreen():
    confirmation = True

    while confirmation:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        confirmationBackground = pygame.image.load('confirmationBackground.png')
        confirmationBackgroundX = 0
        confirmationBackgroundY = 90

        screen.blit(confirmationBackground, (confirmationBackgroundX, confirmationBackgroundY))

        descriptionText = pygame.font.Font('freesansbold.ttf', 20)
        textSurf, textRect = textObjectsWhite("System: Salomon's Rift", descriptionText)
        textRect.center = (617, 520)
        screen.blit(textSurf, textRect)

        description1Text = pygame.font.Font('freesansbold.ttf', 20)
        textSurf, textRect1 = textObjectsWhite("2332       A group of A.I. establish their first settlement: Provenance. In", description1Text)
        textRect1.center = (850, 560)
        screen.blit(textSurf, textRect1)
        description2Text = pygame.font.Font('freesansbold.ttf', 20)
        textSurf, textRect2 = textObjectsWhite("the years that follow, the A.I. claim more worlds and tensions", description2Text)
        textRect2.center = (893, 580)
        screen.blit(textSurf, textRect2)
        description3Text = pygame.font.Font('freesansbold.ttf', 20)
        textSurf, textRect3 = textObjectsWhite("increase in neighboring human colonies.", description3Text)
        textRect3.center = (792, 600)
        screen.blit(textSurf, textRect3)

        description6Text = pygame.font.Font('freesansbold.ttf', 20)
        textSurf, textRect6 = textObjectsWhite("2683       A group of zealots crash a TDS Aegis into the heart of", description6Text)
        textRect6.center = (810, 640)
        screen.blit(textSurf, textRect6)
        description7Text = pygame.font.Font('freesansbold.ttf', 20)
        textSurf, textRect7 = textObjectsWhite("Provenance's capital and detonate the jump drive, destroying", description7Text)
        textRect7.center = (891, 660)
        screen.blit(textSurf, textRect7)
        description8Text = pygame.font.Font('freesansbold.ttf', 20)
        textSurf, textRect8 = textObjectsWhite("the city. In response, the A.I. develop the Swarm to ensure the", description8Text)
        textRect8.center = (894, 680)
        screen.blit(textSurf, textRect8)
        description9Text = pygame.font.Font('freesansbold.ttf', 20)
        textSurf, textRect9 = textObjectsWhite("safety of their home.", description9Text)
        textRect9.center = (690, 700)
        screen.blit(textSurf, textRect9)

        description10Text = pygame.font.Font('freesansbold.ttf', 20)
        textSurf, textRect10 = textObjectsWhite("The Swarm's Objective: Clear out every human colony within a 50", description10Text)
        textRect10.center = (827, 740)
        screen.blit(textSurf, textRect10)
        description11Text = pygame.font.Font('freesansbold.ttf', 20)
        textSurf, textRect11 = textObjectsWhite("light year radius of Provenance. The Swarm has", description11Text)
        textRect11.center = (980, 760)
        screen.blit(textSurf, textRect11)
        description12Text = pygame.font.Font('freesansbold.ttf', 20)
        textSurf, textRect12 = textObjectsWhite("proven to be unstoppable. All any capital ship", description12Text)
        textRect12.center = (970, 780)
        screen.blit(textSurf, textRect12)
        description13Text = pygame.font.Font('freesansbold.ttf', 20)
        textSurf, textRect13 = textObjectsWhite(" commander can hope to do is hold back the tide", description13Text)
        textRect13.center = (977, 800)
        screen.blit(textSurf, textRect13)
        description14Text = pygame.font.Font('freesansbold.ttf', 20)
        textSurf, textRect14 = textObjectsWhite("tide until the civilians escape.", description14Text)
        textRect14.center = (896, 820)
        screen.blit(textSurf, textRect14)


        battleButton("play")
        enterGameButton("play")

        pygame.display.update()
    clock.tick(60)


#General HUD appearance.
def displayHUD():
    #The circular backgrounds of abilities and pictures of abilities the same for every ship.
    abilityBackground = pygame.image.load('Frame-fade.png')
    screen.blit(abilityBackground, (772, 830))
    screen.blit(abilityBackground, (660, 830))
    screen.blit(abilityBackground, (548, 830))
    screen.blit(abilityBackground, (884, 830))
    screen.blit(abilityBackground, (996, 830))
    screen.blit(abilityBackground, (1108, 830))

    pointDefenseSkill = pygame.image.load('pointDefense.png')
    screen.blit(pointDefenseSkill, (783, 841))

    warpSkill = pygame.image.load('warp.png')
    screen.blit(warpSkill, (895, 841))
    screen.blit(warpSkill, (1007, 841))

    #The numbers, signifying which key to press to activate each ability, above each ability.
    printWhiteText('1', 12, 583, 820)
    printWhiteText('2', 12, 695, 820)
    printWhiteText('3', 12, 807, 820)
    printWhiteText('(Tab)', 12, 919, 820)
    printWhiteText('4', 12, 1031, 820)
    printWhiteText('(LMB)', 12, 1143, 820)

    #The names of default abilities (point defense, jump drive, jump home).
    printWhiteText('Point Defense', 12, 807, 915)
    printWhiteText('Jump Drive', 12, 919, 915)
    printWhiteText('Jump Home', 12, 1031, 915)




    #Combat log.
    printWhiteText('Combat Log:', 18, 100, 700)


    #Background to base/turret health indicator at top of screen.
    baseDisplay = pygame.image.load('baseDisplay.png')
    screen.blit(baseDisplay, (499, 25))




#Functions to spawn in different types of enemies.




# The values of each of the player's ships' full health- these values will be modified by upgrades. THESE VALUES WILL CHANGE DEPENDING ON WHICH SHIPS THE PLAYER HAS SELECTED IN THE MENU.
slotOneShipFullHealth = 0
slotTwoShipFullHealth = 0
slotThreeShipFullHealth = 0

slotOneShipFullEnergy = 0
slotTwoShipFullEnergy = 0
slotThreeShipFullEnergy = 0

#When this value is true, the maximum health of each ship in the player's fleet will be set- this only happens at the beginning of the game because the value can later be modified by upgrades.
assignFullEnergyAndHealth = True

#Change this to include all ships when we add more. Also, make sure values appear in the menu.---------------------------------------------------------------------------------------------------------------------------------------------------------------
if assignFullEnergyAndHealth == True:
    if fleetSlotOne == 'Pioneer':
        slotOneShipFullHealth = 9000
        slotOneShipFullEnergy = 5000
        slotOneShipSpeed = 59
    elif fleetSlotTwo == 'Pioneer':
        slotTwoShipFullHealth = 9000
        slotTwoShipFullEnergy = 5000
        slotTwoShipSpeed = 59
    elif fleetSlotThree == 'Pioneer':
        slotThreeShipFullHealth = 9000
        slotThreeShipFullEnergy = 5000
        slotThreeShipSpeed = 59
    if fleetSlotOne == 'Colossus':
        slotOneShipFullHealth = 9000
        slotOneShipFullEnergy = 5000
        slotOneShipSpeed = 41
    elif fleetSlotTwo == 'Colossus':
        slotTwoShipFullHealth = 9000
        slotTwoShipFullEnergy = 5000
        slotTwoShipSpeed = 41
    elif fleetSlotThree == 'Colossus':
        slotThreeShipFullHealth = 9000
        slotThreeShipFullEnergy = 5000
        slotThreeShipSpeed = 41
    if fleetSlotOne == 'Venturer':
        slotOneShipFullHealth = 9000
        slotOneShipFullEnergy = 5000
        slotOneShipSpeed = 43
    elif fleetSlotTwo == 'Venturer':
        slotTwoShipFullHealth = 9000
        slotTwoShipFullEnergy = 5000
        slotTwoShipSpeed = 43
    elif fleetSlotThree == 'Venturer':
        slotThreeShipFullHealth = 9000
        slotThreeShipFullEnergy = 5000
        slotThreeShipSpeed = 43

    fleetSpeed = (slotOneShipSpeed + slotTwoShipSpeed + slotTwoShipSpeed) / 3

    assignFullEnergyAndHealth = False


#How different enemy fleets of different waves will behave.

def waveOnePioneerPioneerFleet():
    pass


def gameLoop():
    gameRunning = True

    selectedSlot = 1

    #Health and energy and speed of player's ships (values will change depending on ships selected).
    slotOneShipHealth = 0
    slotTwoShipHealth = 0
    slotThreeShipHealth = 0

    slotOneShipEnergy = 0
    slotTwoShipEnergy = 0
    slotThreeShipEnergy = 0



    #Only when this variable has a value of True will a player's ship's energy begin to recharge.
    slotOneEnergyCooldown = True
    slotTwoEnergyCooldown = True
    slotThreeEnergyCooldown = True

    #This timer allows energy to be added to a ship only once per given time period.
    slotOneEnergyTimer = 0
    slotTwoEnergyTimer = 0
    slotThreeEnergyTimer = 0

    #When this value is true, all player ships will be assigned full health (used at the beginning of the game).
    assignEnergyAndHealth = True

    #Health of enemy ships (values will change depending on enemies on screen).
    enemyOneHealth = 0
    enemyTwoHealth = 0
    enemyThreeHealth = 0
    enemyFourHealth = 0
    enemyFiveHealth = 0

    #The boolean value that is responsible for assigning enemyOneHealth, etc. to ships as you enter a new sector with enemies.
    assignEnemyHealth = True

    #Aspects of the enemy.
    selectedEnemyHealth = 0

    #Modifications to player fleet effects.


    selectedEnemy = 'None'


    damageAmount = 0

    #How much additional damage the fleet will do based on abilities.
    fleetDamageBoost = 1

    #Which group of enemies will be displayed on-screen and will be available to attack. Enemies not displayed will still deal damage.
    selectedEnemyFleet = 1


    #How effective the player's ships's point defense will be/point defense cooldown variables for the player's ships.
    slotOneShipPointDefenseActive = False
    slotTwoShipPointDefenseActive = False
    slotThreeShipPointDefenseActive = False

    slotOneShipPointDefenseCooldown = 0
    slotTwoShipPointDefenseCooldown = 0
    slotThreeShipPointDefenseCooldown = 0

    slotOneShipPointDefenseCharge = 100
    slotTwoShipPointDefenseCharge = 100
    slotThreeShipPointDefenseCharge = 100

    fleetShipOnePointDefenseEff = 1
    fleetShipTwoPointDefenseEff = 1
    fleetShipThreePointDefenseEff = 1


    #How effective the enemies' point defense will be.
    enemyOnePointDefenseEff = 1
    enemyTwoPointDefenseEff = 1
    enemyThreePointDefenseEff = 1
    enemyFourPointDefenseEff = 1
    enemyFivePointDefenseEff = 1


    #Showing different ships in different slots.
    pioneerIsEnemyOneFleetOne = False
    pioneerIsEnemyTwoFleetOne = False
    pioneerIsEnemyThreeFleetOne = False
    pioneerIsEnemyFourFleetOne = False
    pioneerIsEnemyFiveFleetOne = False

    protectorIsEnemyOneFleetOne = False
    protectorIsEnemyTwoFleetOne = False
    protectorIsEnemyThreeFleetOne = False
    protectorIsEnemyFourFleetOne = False
    protectorIsEnemyFiveFleetOne = False

    #Wave number
    waveNumber = 0

    #Sectors will only we randomly chosen if this value is true.
    randomlySelectSectors = True

    #If these variables are true, their coorisponding wave will change.
    waveOne = True
    startWaveTwo = False
    startWaveThree = False
    startWaveFour = False

    #A new wave will only start when this counter reaches zero, giving the player less time to regroup each wave.
    waveStartCounter = 70

    #Map and coordinate variables.
    #Whether or not the map will be displayed on the screen.
    showExpandedMap = False

    #Enemies will only spawn in (which will change certain variables) if this value is true.
    spawnEnemies = False

    #The warning saying enemies inbound will only show if this is true.
    enemiesInboundMessageTimer = 70

    #Weapons will only decrease a target's health if this value is true.
    inSameSectorAsEnemy = True

    #From the beginning to end of the hyphons, these are statistics of the ships in wave one----------------------------------------------------------------------------------------------------------------------------------------
    #Where various enemy fleets will be encountered (fleet naming convention: ['wave', wave appearing on, ship type one-five if applicable, 'FleetLocation'].
    enemySpawnSectorsPossibilities = ['alpha', 'delta', 'beta']
    coordinatePossibilities = [15000, 25000, 35000]
    coordinatePossibilities2 = [15000, 25000]
    coordinatePossibilities3 = [25000, 35000]


    occupiedCoordinates1X = 0
    occupiedCoordinates1Y = 0

    waveOnePioneerPioneerFleetSector = 'None'

    waveOnePioneerPioneerFleetX = 0
    waveOnePioneerPioneerFleetY = 0

    waveOnePioneerPioneerFleetTargetX = 0
    waveOnePioneerPioneerFleetTargetY = 0

    resivoirHealthTwo = 0
    resivoirHealthThree = 0

    waveOnePioneerPioneerFleetTravelTime = 0

    #If this variable is true, than certain fleets have made it to the outpost and will proceed to damage the core.
    waveOnePioneerPioneerFleetLocationInOutpost = False

    #List of ships for the enemy to select from.
    enemySelectionFull = [1, 2, 3]
    enemySelection1and2 = [1,2]
    enemySelection2and3 = [2, 3]
    enemySelection1and3 = [1, 3]

    #Cooldown of enemy weapons.
    pioneer2VoidChargesCooldown = 0
    pioneer3VoidChargesCooldown = 0

    #The health of enemy targets.
    pioneer2Target = 0
    pioneer3Target = 0

    pioneer2TargetHealth = 0
    pioneer3TargetHealth = 0

    #Coordinates.

    fleetSector = 'outpost'
    fleetX = 35000
    fleetY = 20000
    targetfleetX = 35000
    targetfleetY = 20000

    #Fleet will only jump once the timer reaches zero.
    jumpTimer = 0

    #Fleet will only move to a new spot once this timer reaches zero, affected by fleet mobility and distance.
    distanceToTargetLocation = 0

    #Which sector the players wants to jump the fleet to (variable changed by clicking jump points in map).
    targetSector = 'outpost'

    #The combat log, which will display a message once any ship has taken damage or arrived in a new sector.
    combatLogEntryOne = ''
    combatLogEntryTwo = ''
    combatLogEntryThree = ''
    combatLogEntryFour = ''
    combatLogEntryFive = ''
    combatLogEntrySix = ''
    combatLogEntrySeven = ''
    combatLogEntryEight = ''
    combatLogEntryNine = ''
    combatLogEntryTen = ''


    #Score
    score = 0


    #Cooldown variables.
    #Pioneer
    pioneerVoidChargesCooldown = 0
    pioneerMissilesCooldown = 0

    #Colossus
    colossusFlakCooldown = 0



    while gameRunning:



        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        screen.fill(black)



        #Player input loop.

        for event in pygame.event.get():



            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if showExpandedMap == False:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_TAB:
                        showExpandedMap = True

                    #Selecting different ships in the fleet.
                    if event.key == pygame.K_LEFT and selectedSlot == 1:
                        if slotThreeShipHealth > 0:
                            selectedSlot = 3
                        elif slotThreeShipHealth <= 0 and slotTwoShipHealth > 0:
                            selectedSlot = 2
                        elif slotThreeShipHealth <= 0 and slotTwoShipHealth <= 0:
                            pass
                    elif event.key == pygame.K_LEFT and selectedSlot == 3:
                        if slotTwoShipHealth > 0:
                            selectedSlot = 2
                        elif slotTwoShipHealth <= 0 and slotOneShipHealth > 0:
                            selectedSlot = 1
                        elif slotTwoShipHealth <= 0 and slotOneShipHealth <= 0:
                            pass
                    elif event.key == pygame.K_LEFT and selectedSlot == 2:
                        if slotOneShipHealth > 0:
                            selectedSlot = 1
                        elif slotOneShipHealth <= 0 and slotThreeShipHealth > 0:
                            selectedSlot = 3
                        elif slotOneShipHealth <= 0 and slotThreeShipHealth <= 0:
                            pass
                    elif event.key == pygame.K_RIGHT and selectedSlot == 1:
                        if slotTwoShipHealth > 0:
                            selectedSlot = 2
                        elif slotTwoShipHealth <= 0 and slotThreeShipHealth > 0:
                            selectedSlot = 3
                        elif slotTwoShipHealth <= 0 and slotThreeShipHealth <= 0:
                            pass
                    elif event.key == pygame.K_RIGHT and selectedSlot == 2:
                        if slotThreeShipHealth > 0:
                            selectedSlot = 3
                        elif slotThreeShipHealth <= 0 and slotOneShipHealth > 0:
                            selectedSlot = 1
                        elif slotThreeShipHealth <= 0 and slotTwoShipHealth <= 0:
                            pass
                    elif event.key == pygame.K_RIGHT and selectedSlot == 3:
                        if slotOneShipHealth > 0:
                            selectedSlot = 1
                        elif slotOneShipHealth <= 0 and slotTwoShipHealth > 0:
                            selectedSlot = 2
                        elif slotOneShipHealth <= 0 and slotTwoShipHealth <= 0:
                            pass

                    #Selecting enemies.
                    if 1040 > mouse[0] > 690 and 340 > mouse[1] > 200:
                        if event.key == pygame.K_f and enemyOneHealth > 0 and inSameSectorAsEnemy == True:
                            selectedEnemy = 'One'
                    elif 700 > mouse[0] > 350 and 380 > mouse[1] > 240:
                        if event.key == pygame.K_f and enemyTwoHealth > 0 and inSameSectorAsEnemy == True:
                            selectedEnemy = 'Two'
                    elif 1380 > mouse[0] > 1030 and 380 > mouse[1] > 240:
                        if event.key == pygame.K_f and enemyThreeHealth > 0 and inSameSectorAsEnemy == True:
                            selectedEnemy = 'Three'
                    elif 360 > mouse[0] > 10 and 430 > mouse[1] > 290:
                        if event.key == pygame.K_f and enemyFourHealth > 0 and inSameSectorAsEnemy == True:
                            selectedEnemy = 'Four'
                    elif 1720 > mouse[0] > 1370 and 430 > mouse[1] > 290:
                        if event.key == pygame.K_f and enemyFiveHealth > 0 and inSameSectorAsEnemy == True:
                            selectedEnemy = 'Five'




                    #Ship abilities
                    #Point defense (same for all ships).
                    if slotOneShipPointDefenseCooldown == 0:
                        if selectedSlot == 1:
                            if event.key == pygame.K_3 and slotOneShipPointDefenseActive == False:
                                if slotOneShipPointDefenseCharge != 0:
                                    slotOneShipPointDefenseActive = True
                            elif event.key == pygame.K_3 and slotOneShipPointDefenseActive == True:
                                slotOneShipPointDefenseActive = False
                                slotOneShipPointDefenseCooldown = 10
                    if slotTwoShipPointDefenseCooldown == 0:
                        if selectedSlot == 2:
                            if event.key == pygame.K_3 and slotTwoShipPointDefenseActive == False:
                                if slotTwoShipPointDefenseCharge != 0:
                                    slotTwoShipPointDefenseActive = True
                            elif event.key == pygame.K_3 and slotTwoShipPointDefenseActive == True:
                                slotTwoShipPointDefenseActive = False
                                slotTwoShipPointDefenseCooldown = 10
                    if slotThreeShipPointDefenseCooldown == 0:
                        if selectedSlot == 3:
                            if event.key == pygame.K_3 and slotThreeShipPointDefenseActive == False:
                                if slotThreeShipPointDefenseCharge != 0:
                                    slotThreeShipPointDefenseActive = True
                            elif event.key == pygame.K_3 and slotThreeShipPointDefenseActive == True:
                                slotThreeShipPointDefenseActive = False
                                slotThreeShipPointDefenseCooldown = 10


                    #Pioneer abilities.
                    if fleetSlotOne == 'Pioneer' and selectedSlot == 1 or fleetSlotTwo == 'Pioneer' and selectedSlot == 2 or fleetSlotThree == 'Pioneer' and selectedSlot == 3:
                        #Pioneer missiles.
                        if pioneerMissilesCooldown == 0:
                            if selectedEnemy == 'One':
                                if event.key == pygame.K_2:
                                    if enemyOneHealth > 0 and inSameSectorAsEnemy == True:
                                        enemyOneHealth -= (750 * fleetDamageBoost) * enemyOnePointDefenseEff
                                        damageAmount = (750 * fleetDamageBoost) * enemyOnePointDefenseEff
                                        combatLogEntryTen = combatLogEntryNine
                                        combatLogEntryNine = combatLogEntryEight
                                        combatLogEntryEight = combatLogEntrySeven
                                        combatLogEntrySeven = combatLogEntrySix
                                        combatLogEntrySix = combatLogEntryFive
                                        combatLogEntryFive = combatLogEntryFour
                                        combatLogEntryFour = combatLogEntryThree
                                        combatLogEntryThree = combatLogEntryTwo
                                        combatLogEntryTwo = combatLogEntryOne
                                        combatLogEntryOne = 'Enemy 1 Took ' + str(damageAmount) + ' Damage From Pioneer'
                                        pioneerMissilesCooldown = 100
                            elif selectedEnemy == 'Two':
                                if event.key == pygame.K_2:
                                    if enemyTwoHealth > 0 and inSameSectorAsEnemy == True:
                                        enemyTwoHealth -= (750 * fleetDamageBoost) * enemyOnePointDefenseEff
                                        damageAmount = (750 * fleetDamageBoost) * enemyOnePointDefenseEff
                                        combatLogEntryTen = combatLogEntryNine
                                        combatLogEntryNine = combatLogEntryEight
                                        combatLogEntryEight = combatLogEntrySeven
                                        combatLogEntrySeven = combatLogEntrySix
                                        combatLogEntrySix = combatLogEntryFive
                                        combatLogEntryFive = combatLogEntryFour
                                        combatLogEntryFour = combatLogEntryThree
                                        combatLogEntryThree = combatLogEntryTwo
                                        combatLogEntryTwo = combatLogEntryOne
                                        combatLogEntryOne = 'Enemy 2 Took ' + str(damageAmount) + ' Damage From Pioneer'
                                        pioneerMissilesCooldown = 100
                            elif selectedEnemy == 'Three':
                                if event.key == pygame.K_2:
                                    if enemyThreeHealth > 0 and inSameSectorAsEnemy == True:
                                        enemyThreeHealth -= (750 * fleetDamageBoost) * enemyOnePointDefenseEff
                                        damageAmount = (750 * fleetDamageBoost) * enemyOnePointDefenseEff
                                        combatLogEntryTen = combatLogEntryNine
                                        combatLogEntryNine = combatLogEntryEight
                                        combatLogEntryEight = combatLogEntrySeven
                                        combatLogEntrySeven = combatLogEntrySix
                                        combatLogEntrySix = combatLogEntryFive
                                        combatLogEntryFive = combatLogEntryFour
                                        combatLogEntryFour = combatLogEntryThree
                                        combatLogEntryThree = combatLogEntryTwo
                                        combatLogEntryTwo = combatLogEntryOne
                                        combatLogEntryOne = 'Enemy 3 Took ' + str(damageAmount) + ' Damage From Pioneer'
                                        pioneerMissilesCooldown = 100
                            elif selectedEnemy == 'Four':
                                if event.key == pygame.K_2:
                                    if enemyFourHealth > 0 and inSameSectorAsEnemy == True:
                                        enemyFourHealth -= (750 * fleetDamageBoost) * enemyOnePointDefenseEff
                                        damageAmount = (750 * fleetDamageBoost) * enemyOnePointDefenseEff
                                        combatLogEntryTen = combatLogEntryNine
                                        combatLogEntryNine = combatLogEntryEight
                                        combatLogEntryEight = combatLogEntrySeven
                                        combatLogEntrySeven = combatLogEntrySix
                                        combatLogEntrySix = combatLogEntryFive
                                        combatLogEntryFive = combatLogEntryFour
                                        combatLogEntryFour = combatLogEntryThree
                                        combatLogEntryThree = combatLogEntryTwo
                                        combatLogEntryTwo = combatLogEntryOne
                                        combatLogEntryOne = 'Enemy 4 Took ' + str(damageAmount) + ' Damage From Pioneer'
                                        pioneerMissilesCooldown = 100
                            elif selectedEnemy == 'Five':
                                if event.key == pygame.K_2:
                                    if enemyFiveHealth > 0 and inSameSectorAsEnemy == True:
                                        enemyFiveHealth -= (750 * fleetDamageBoost) * enemyOnePointDefenseEff
                                        damageAmount = (750 * fleetDamageBoost) * enemyOnePointDefenseEff
                                        combatLogEntryTen = combatLogEntryNine
                                        combatLogEntryNine = combatLogEntryEight
                                        combatLogEntryEight = combatLogEntrySeven
                                        combatLogEntrySeven = combatLogEntrySix
                                        combatLogEntrySix = combatLogEntryFive
                                        combatLogEntryFive = combatLogEntryFour
                                        combatLogEntryFour = combatLogEntryThree
                                        combatLogEntryThree = combatLogEntryTwo
                                        combatLogEntryTwo = combatLogEntryOne
                                        combatLogEntryOne = 'Enemy 5 Took ' + str(damageAmount) + ' Damage From Pioneer'
                                        pioneerMissilesCooldown = 100





                #Pioneer weapon systems.
                if fleetSlotOne == 'Pioneer' and selectedSlot == 1 or fleetSlotTwo == 'Pioneer' and selectedSlot == 2 or fleetSlotThree == 'Pioneer' and selectedSlot == 3:
                    #Pioneer's main weapon (Void Cannon), used by left clicking enemies that the player wants to damage.
                    if pioneerVoidChargesCooldown == 0:
                        if 1040 > mouse[0] > 690 and 340 > mouse[1] > 200:
                            if click[0] == 1:
                                if enemyOneHealth > 0 and inSameSectorAsEnemy == True:
                                    enemyOneHealth -= 350 * fleetDamageBoost
                                    damageAmount = 350 * fleetDamageBoost
                                    combatLogEntryTen = combatLogEntryNine
                                    combatLogEntryNine = combatLogEntryEight
                                    combatLogEntryEight = combatLogEntrySeven
                                    combatLogEntrySeven = combatLogEntrySix
                                    combatLogEntrySix = combatLogEntryFive
                                    combatLogEntryFive = combatLogEntryFour
                                    combatLogEntryFour = combatLogEntryThree
                                    combatLogEntryThree = combatLogEntryTwo
                                    combatLogEntryTwo = combatLogEntryOne
                                    combatLogEntryOne = 'Enemy 1 Took ' + str(damageAmount) + ' Damage From Pioneer'
                                    pioneerVoidChargesCooldown = 50
                                elif enemyOneHealth == 0 or inSameSectorAsEnemy == False:
                                    pioneerVoidChargesCooldown = 50

                        elif 700 > mouse[0] > 350 and 380 > mouse[1] > 240:
                            if click[0] == 1:
                                if enemyTwoHealth > 0 and inSameSectorAsEnemy == True:
                                    enemyTwoHealth -= 350 * fleetDamageBoost
                                    damageAmount = 350 * fleetDamageBoost
                                    combatLogEntryTen = combatLogEntryNine
                                    combatLogEntryNine = combatLogEntryEight
                                    combatLogEntryEight = combatLogEntrySeven
                                    combatLogEntrySeven = combatLogEntrySix
                                    combatLogEntrySix = combatLogEntryFive
                                    combatLogEntryFive = combatLogEntryFour
                                    combatLogEntryFour = combatLogEntryThree
                                    combatLogEntryThree = combatLogEntryTwo
                                    combatLogEntryTwo = combatLogEntryOne
                                    combatLogEntryOne = 'Enemy 2 Took ' + str(damageAmount) + ' Damage From Pioneer'
                                    pioneerVoidChargesCooldown = 50
                                elif enemyTwoHealth == 0 or inSameSectorAsEnemy == False:
                                    pioneerVoidChargesCooldown = 50


                        elif 1380 > mouse[0] > 1030 and 380 > mouse[1] > 240:
                            if click[0] == 1:
                                if enemyThreeHealth > 0 and inSameSectorAsEnemy == True:
                                    enemyThreeHealth -= 350 * fleetDamageBoost
                                    damageAmount = 350 * fleetDamageBoost
                                    combatLogEntryTen = combatLogEntryNine
                                    combatLogEntryNine = combatLogEntryEight
                                    combatLogEntryEight = combatLogEntrySeven
                                    combatLogEntrySeven = combatLogEntrySix
                                    combatLogEntrySix = combatLogEntryFive
                                    combatLogEntryFive = combatLogEntryFour
                                    combatLogEntryFour = combatLogEntryThree
                                    combatLogEntryThree = combatLogEntryTwo
                                    combatLogEntryTwo = combatLogEntryOne
                                    combatLogEntryOne = 'Enemy 3 Took ' + str(damageAmount) + ' Damage From Pioneer'
                                    pioneerVoidChargesCooldown = 50
                                elif enemyThreeHealth == 0 or inSameSectorAsEnemy == False:
                                    pioneerVoidChargesCooldown = 50

                        elif 360 > mouse[0] > 10 and 430 > mouse[1] > 290:
                            if click[0] == 1:
                                if enemyFourHealth > 0 and inSameSectorAsEnemy == True:
                                    enemyFourHealth -= 350 * fleetDamageBoost
                                    damageAmount = 350 * fleetDamageBoost
                                    combatLogEntryTen = combatLogEntryNine
                                    combatLogEntryNine = combatLogEntryEight
                                    combatLogEntryEight = combatLogEntrySeven
                                    combatLogEntrySeven = combatLogEntrySix
                                    combatLogEntrySix = combatLogEntryFive
                                    combatLogEntryFive = combatLogEntryFour
                                    combatLogEntryFour = combatLogEntryThree
                                    combatLogEntryThree = combatLogEntryTwo
                                    combatLogEntryTwo = combatLogEntryOne
                                    combatLogEntryOne = 'Enemy 4 Took ' + str(damageAmount) + ' Damage From Pioneer'
                                    pioneerVoidChargesCooldown = 50
                                elif enemyFourHealth == 0 or inSameSectorAsEnemy == False:
                                    pioneerVoidChargesCooldown = 50

                        elif 1720 > mouse[0] > 1370 and 430 > mouse[1] > 290:
                            if click[0] == 1:
                                if enemyFiveHealth > 0 and inSameSectorAsEnemy == True:
                                    enemyFiveHealth -= 350 * fleetDamageBoost
                                    damageAmount = 350 * fleetDamageBoost
                                    combatLogEntryTen = combatLogEntryNine
                                    combatLogEntryNine = combatLogEntryEight
                                    combatLogEntryEight = combatLogEntrySeven
                                    combatLogEntrySeven = combatLogEntrySix
                                    combatLogEntrySix = combatLogEntryFive
                                    combatLogEntryFive = combatLogEntryFour
                                    combatLogEntryFour = combatLogEntryThree
                                    combatLogEntryThree = combatLogEntryTwo
                                    combatLogEntryTwo = combatLogEntryOne
                                    combatLogEntryOne = 'Enemy 5 Took ' + str(damageAmount) + ' Damage From Pioneer'
                                    pioneerVoidChargesCooldown = 50
                                elif enemyFiveHealth == 0 or inSameSectorAsEnemy == False:
                                    pioneerVoidChargesCooldown = 50

                        elif 1728 > mouse[0] > 0 and 972 > mouse[1] > 0 and click[0] == 1:
                            pioneerVoidChargesCooldown = 50

                #Colossus weapon systems.
                if fleetSlotOne == 'Colossus' and selectedSlot == 1 or fleetSlotTwo == 'Colossus' and selectedSlot == 2 or fleetSlotThree == 'Colossus' and selectedSlot == 3:
                    # Colossus' main weapon (Flak), used by left clicking enemies that the player wants to damage.
                    if colossusFlakCooldown == 0:
                        if 1040 > mouse[0] > 690 and 340 > mouse[1] > 200:
                            if click[0] == 1:
                                if enemyOneHealth > 0 and inSameSectorAsEnemy == True:
                                    enemyOneHealth -= 50 * fleetDamageBoost
                                    damageAmount = 50 * fleetDamageBoost
                                    combatLogEntryTen = combatLogEntryNine
                                    combatLogEntryNine = combatLogEntryEight
                                    combatLogEntryEight = combatLogEntrySeven
                                    combatLogEntrySeven = combatLogEntrySix
                                    combatLogEntrySix = combatLogEntryFive
                                    combatLogEntryFive = combatLogEntryFour
                                    combatLogEntryFour = combatLogEntryThree
                                    combatLogEntryThree = combatLogEntryTwo
                                    combatLogEntryTwo = combatLogEntryOne
                                    combatLogEntryOne = 'Enemy 1 Took ' + str(damageAmount) + ' Damage From Colossus'
                                    colossusFlakCooldown = 5
                                elif enemyOneHealth == 0 or inSameSectorAsEnemy == False:
                                    colossusFlakCooldown = 5

                        elif 700 > mouse[0] > 350 and 380 > mouse[1] > 240:
                            if click[0] == 1:
                                if enemyTwoHealth > 0 and inSameSectorAsEnemy == True:
                                    enemyTwoHealth -= 50 * fleetDamageBoost
                                    damageAmount = 50 * fleetDamageBoost
                                    combatLogEntryTen = combatLogEntryNine
                                    combatLogEntryNine = combatLogEntryEight
                                    combatLogEntryEight = combatLogEntrySeven
                                    combatLogEntrySeven = combatLogEntrySix
                                    combatLogEntrySix = combatLogEntryFive
                                    combatLogEntryFive = combatLogEntryFour
                                    combatLogEntryFour = combatLogEntryThree
                                    combatLogEntryThree = combatLogEntryTwo
                                    combatLogEntryTwo = combatLogEntryOne
                                    combatLogEntryOne = 'Enemy 2 Took ' + str(damageAmount) + ' Damage From Colossus'
                                    colossusFlakCooldown = 5
                                elif enemyTwoHealth == 0 or inSameSectorAsEnemy == False:
                                    colossusFlakCooldown = 5

                        elif 1380 > mouse[0] > 1030 and 380 > mouse[1] > 240:
                            if click[0] == 1:
                                if enemyThreeHealth > 0 and inSameSectorAsEnemy == True:
                                    enemyThreeHealth -= 50 * fleetDamageBoost
                                    damageAmount = 50 * fleetDamageBoost
                                    combatLogEntryTen = combatLogEntryNine
                                    combatLogEntryNine = combatLogEntryEight
                                    combatLogEntryEight = combatLogEntrySeven
                                    combatLogEntrySeven = combatLogEntrySix
                                    combatLogEntrySix = combatLogEntryFive
                                    combatLogEntryFive = combatLogEntryFour
                                    combatLogEntryFour = combatLogEntryThree
                                    combatLogEntryThree = combatLogEntryTwo
                                    combatLogEntryTwo = combatLogEntryOne
                                    combatLogEntryOne = 'Enemy 3 Took ' + str(damageAmount) + ' Damage From Colossus'
                                    colossusFlakCooldown = 5
                                elif enemyThreeHealth == 0 or inSameSectorAsEnemy == False:
                                    colossusFlakCooldown = 5

                        elif 360 > mouse[0] > 10 and 430 > mouse[1] > 290:
                            if click[0] == 1:
                                if enemyFourHealth > 0 and inSameSectorAsEnemy == True:
                                    enemyFourHealth -= 50 * fleetDamageBoost
                                    damageAmount = 50 * fleetDamageBoost
                                    combatLogEntryTen = combatLogEntryNine
                                    combatLogEntryNine = combatLogEntryEight
                                    combatLogEntryEight = combatLogEntrySeven
                                    combatLogEntrySeven = combatLogEntrySix
                                    combatLogEntrySix = combatLogEntryFive
                                    combatLogEntryFive = combatLogEntryFour
                                    combatLogEntryFour = combatLogEntryThree
                                    combatLogEntryThree = combatLogEntryTwo
                                    combatLogEntryTwo = combatLogEntryOne
                                    combatLogEntryOne = 'Enemy 4 Took ' + str(damageAmount) + ' Damage From Colossus'
                                    colossusFlakCooldown = 5
                                elif enemyFourHealth == 0 or inSameSectorAsEnemy == False:
                                    colossusFlakCooldown = 5

                        elif 1720 > mouse[0] > 1370 and 430 > mouse[1] > 290:
                            if click[0] == 1:
                                if enemyFiveHealth > 0 and inSameSectorAsEnemy == True:
                                    enemyFiveHealth -= 50 * fleetDamageBoost
                                    damageAmount = 50 * fleetDamageBoost
                                    combatLogEntryTen = combatLogEntryNine
                                    combatLogEntryNine = combatLogEntryEight
                                    combatLogEntryEight = combatLogEntrySeven
                                    combatLogEntrySeven = combatLogEntrySix
                                    combatLogEntrySix = combatLogEntryFive
                                    combatLogEntryFive = combatLogEntryFour
                                    combatLogEntryFour = combatLogEntryThree
                                    combatLogEntryThree = combatLogEntryTwo
                                    combatLogEntryTwo = combatLogEntryOne
                                    combatLogEntryOne = 'Enemy 5 Took ' + str(damageAmount) + ' Damage From Colossus'
                                    colossusFlakCooldown = 5
                                elif enemyFiveHealth == 0 or inSameSectorAsEnemy == False:
                                    colossusFlakCooldown = 5

                        elif 1728 > mouse[0] > 0 and 972 > mouse[1] > 0 and click[0] == 1:
                            colossusFlakCooldown = 50


            if showExpandedMap == True:
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_TAB:
                        showExpandedMap = False





        #Loading in pictures of various ships.
        pioneerInGameDisplay = pygame.image.load('pioneerInGame.png')
        colossusInGameDisplay = pygame.image.load('colossusInGame.png')
        venturerInGameDisplay = pygame.image.load('venturerInGame.png')


        # What will happen if a certain fleet ship is selected.
        # For the Pioneer.
        if fleetSlotOne == 'Pioneer' and selectedSlot == 1 or fleetSlotTwo == 'Pioneer' and selectedSlot == 2 or fleetSlotThree == 'Pioneer' and selectedSlot == 3:
            printWhiteText('Reveal Sector', 12, 583, 915)
            printWhiteText('Pioneer Missiles', 12, 695, 915)
            printWhiteText('Void Charges', 12, 1143, 915)

            detect = pygame.image.load('Detect.png')
            screen.blit(detect, (559, 841))
            missiles = pygame.image.load('missiles.png')
            screen.blit(missiles, (670, 841))
            cannon = pygame.image.load('cannon.png')
            screen.blit(cannon, (1119, 841))

            #Change below display bars to match up with all ship spots!!!!!!!!!!
            if fleetSlotOne == 'Pioneer':
                pygame.draw.rect(screen, orange, [265, 615, 250, 25])
            elif fleetSlotTwo == 'Pioneer':
                pygame.draw.rect(screen, orange, [725, 735, 250, 25])
            elif fleetSlotThree == 'Pioneer':
                pygame.draw.rect(screen, orange, [265, 615, 250, 25])

        # For the Colossus.
        if fleetSlotOne == 'Colossus' and selectedSlot == 1 or fleetSlotTwo == 'Colossus' and selectedSlot == 2 or fleetSlotThree == 'Colossus' and selectedSlot == 3:
            printWhiteText('Boost', 12, 583, 915)
            printWhiteText('Colossus Fighters', 12, 695, 915)
            printWhiteText('Flak', 12, 1143, 915)

            boost = pygame.image.load('boost.png')
            screen.blit(boost, (559, 841))
            fighters = pygame.image.load('fighters.png')
            screen.blit(fighters, (670, 841))
            cannonFlak = pygame.image.load('cannon-flak.png')
            screen.blit(cannonFlak, (1119, 841))

            if fleetSlotOne == 'Colossus':
                pygame.draw.rect(screen, orange, [265, 615, 250, 25])
            elif fleetSlotTwo == 'Colossus':
                pygame.draw.rect(screen, orange, [725, 735, 250, 25])
            elif fleetSlotThree == 'Colossus':
                pygame.draw.rect(screen, orange, [265, 615, 250, 25])

        # For the Venturer.
        if fleetSlotOne == 'Venturer' and selectedSlot == 1 or fleetSlotTwo == 'Venturer' and selectedSlot == 2 or fleetSlotThree == 'Venturer' and selectedSlot == 3:
            printWhiteText('Repair Pulse', 12, 583, 915)
            printWhiteText('Plasma Missiles', 12, 695, 915)
            printWhiteText('Mining Laser', 12, 1143, 915)

            repairPulse = pygame.image.load('pulse-repair.png')
            screen.blit(repairPulse, (559, 841))
            plasmaMissiles = pygame.image.load('missiles-plasma.png')
            screen.blit(plasmaMissiles, (670, 841))
            miningLasers = pygame.image.load('laser-big.png')
            screen.blit(miningLasers, (1119, 841))

            if fleetSlotOne == 'Venturer':
                pygame.draw.rect(screen, orange, [265, 615, 250, 25])
            elif fleetSlotTwo == 'Venturer':
                pygame.draw.rect(screen, orange, [725, 735, 250, 25])
            elif fleetSlotThree == 'Venturer':
                pygame.draw.rect(screen, orange, [1050, 615, 250, 25])


        #Deciding how much initial health and energy the player's ships have.
        if assignEnergyAndHealth == True:
            slotOneShipHealth = slotOneShipFullHealth
            slotTwoShipHealth = slotTwoShipFullHealth
            slotThreeShipHealth = slotThreeShipFullHealth

            slotOneShipEnergy = slotOneShipFullEnergy
            slotTwoShipEnergy = slotTwoShipFullEnergy
            slotThreeShipEnergy = slotThreeShipFullEnergy
            assignEnergyAndHealth = False

        #Deciding which ships to draw and where based on which ones the player selected in the menu.
        if fleetSlotOne == 'Pioneer':
            screen.blit(pioneerInGameDisplay, (250, 450))
        if fleetSlotTwo == 'Colossus':
            screen.blit(colossusInGameDisplay, (689, 575))
        if fleetSlotThree == 'Venturer':
            screen.blit(venturerInGameDisplay, (1000, 460))


        printWhiteText(selectedEnemy, 90, 200, 200)


        #Deciding whether to show enemy health or not (will not show a value of 0 or any value of a ship is not there).
        if enemyOneHealth > 0 and inSameSectorAsEnemy == True:
            printWhiteText(str(enemyOneHealth), 30, 800, 185)
        if enemyTwoHealth > 0 and inSameSectorAsEnemy == True:
            printWhiteText(str(enemyTwoHealth), 30, 550, 235)
        if enemyThreeHealth > 0 and inSameSectorAsEnemy == True:
            printWhiteText(str(enemyThreeHealth), 30, 1200, 235)
        if enemyFourHealth > 0 and inSameSectorAsEnemy == True:
            printWhiteText(str(enemyThreeHealth), 30, 150, 275)
        if enemyFiveHealth > 0 and inSameSectorAsEnemy == True:
            printWhiteText(str(enemyThreeHealth), 30, 1500, 275)



        displayHUD()

        if selectedEnemyFleet == 1:
            if pioneerIsEnemyOneFleetOne == True and enemyOneHealth > 0 and inSameSectorAsEnemy == True:
                screen.blit(pioneerInGameDisplay, (690, 200))
            if pioneerIsEnemyTwoFleetOne == True and enemyTwoHealth > 0 and inSameSectorAsEnemy == True:
                screen.blit(pioneerInGameDisplay, (350, 240))
            if pioneerIsEnemyThreeFleetOne == True and enemyThreeHealth > 0 and inSameSectorAsEnemy == True:
                screen.blit(pioneerInGameDisplay, (1030, 240))
            if pioneerIsEnemyFourFleetOne == True and enemyFourHealth > 0 and inSameSectorAsEnemy == True:
                screen.blit(pioneerInGameDisplay, (10, 290))
            if pioneerIsEnemyFiveFleetOne == True and enemyFiveHealth > 0 and inSameSectorAsEnemy == True:
                screen.blit(pioneerInGameDisplay, (1370, 290))

            if protectorIsEnemyOneFleetOne == True and enemyOneHealth > 0:
                screen.blit(protectorEnemy, (690, 200))
            if protectorIsEnemyTwoFleetOne == True and enemyTwoHealth > 0:
                screen.blit(protectorEnemy, (350, 240))
            if protectorIsEnemyThreeFleetOne == True and enemyThreeHealth > 0:
                screen.blit(protectorEnemy, (1030, 240))
            if protectorIsEnemyFourFleetOne == True and enemyFourHealth > 0:
                screen.blit(protectorEnemy, (10, 290))
            if protectorIsEnemyFiveFleetOne == True and enemyFiveHealth > 0:
                screen.blit(protectorEnemy, (1370, 290))


        #Displaying combat log entries.
        printWhiteText(combatLogEntryOne, 18, 210, 735)
        printWhiteText(combatLogEntryTwo, 18, 210, 755)
        printWhiteText(combatLogEntryThree, 18, 210, 775)
        printWhiteText(combatLogEntryFour, 18, 210, 795)
        printWhiteText(combatLogEntryFive, 18, 210, 815)
        printWhiteText(combatLogEntrySix, 18, 210, 835)
        printWhiteText(combatLogEntrySeven, 18, 210, 855)
        printWhiteText(combatLogEntryEight, 18, 210, 875)
        printWhiteText(combatLogEntryNine, 18, 210, 895)
        printWhiteText(combatLogEntryTen, 18, 210, 915)


        #Energy recharge for the player's ships (energy only recharges every few seconds).
        if slotOneShipEnergy != slotOneShipFullEnergy and slotOneEnergyCooldown == True:
            slotOneEnergyTimer += 1
            if slotOneEnergyTimer == 10:
                slotOneShipEnergy += 25
                slotOneEnergyTimer = 0
        if slotTwoShipEnergy != slotTwoShipFullEnergy and slotTwoEnergyCooldown == True:
            slotTwoEnergyTimer += 1
            if slotTwoEnergyTimer == 10:
                slotTwoShipEnergy += 25
                slotTwoEnergyTimer = 0
        if slotThreeShipEnergy != slotThreeShipFullEnergy and slotThreeEnergyCooldown == True:
            slotThreeEnergyTimer += 1
            if slotThreeEnergyTimer == 10:
                slotThreeShipEnergy += 25
                slotThreeEnergyTimer = 0



        #Cooldown timers for the player's ship's weapons and abilities.
        cooldownBackground = pygame.image.load('FrameCooldown.png')
        cooldownBackgroundDark = pygame.image.load('FrameCooldown_dark.png')
        activeBackground = pygame.image.load('FrameActive.png')

        #Point defense (same for all ships).
        #Point defense for ship one.
        if slotOneShipPointDefenseCooldown != 0 and slotOneShipEnergy != 0:
            slotOneShipPointDefenseCooldown -= 1
            if selectedSlot == 1:
                screen.blit(cooldownBackground, (772, 830))
                screen.blit(cooldownBackgroundDark, (772, 830))
                printWhiteText(str(slotOneShipPointDefenseCooldown), 30, 807, 868)
        elif slotOneShipPointDefenseCooldown == 0:
            if slotOneShipPointDefenseActive == True and slotOneShipPointDefenseCharge != 0 and slotOneShipEnergy != 0:
                fleetShipOnePointDefenseEff = 0.5
                slotOneShipPointDefenseCharge -= 1
                slotOneShipEnergy -= 25
                slotOneEnergyCooldown = False
                if selectedSlot == 1:
                    screen.blit(activeBackground, (772, 830))
                    printWhiteText(str(slotOneShipPointDefenseCharge), 30, 807, 868)
                if slotOneShipPointDefenseCharge == 0 or slotOneShipEnergy == 0:
                    slotOneShipPointDefenseActive = False
                    slotOneShipPointDefenseCooldown = 10
                    slotOneEnergyCooldown = True
            elif slotOneShipPointDefenseActive == False and slotOneShipPointDefenseCharge != 100:
                slotOneShipPointDefenseCharge += 1
                slotOneEnergyCooldown = True
                if selectedSlot == 1:
                    printWhiteText(str(slotOneShipPointDefenseCharge), 30, 807, 868)

        #Point defense for ship two.
        if slotTwoShipPointDefenseCooldown != 0:
            slotTwoShipPointDefenseCooldown -= 1
            if selectedSlot == 2:
                screen.blit(cooldownBackground, (772, 830))
                screen.blit(cooldownBackgroundDark, (772, 830))
                printWhiteText(str(slotTwoShipPointDefenseCooldown), 30, 807, 868)
        elif slotTwoShipPointDefenseCooldown == 0:
            if slotTwoShipPointDefenseActive == True and slotTwoShipPointDefenseCharge != 0:
                fleetShipTwoPointDefenseEff = 0.5
                slotTwoShipPointDefenseCharge -= 1
                slotTwoShipEnergy -= 25
                slotTwoEnergyCooldown = False
                if selectedSlot == 2:
                    screen.blit(activeBackground, (772, 830))
                    printWhiteText(str(slotTwoShipPointDefenseCharge), 30, 807, 868)
                if slotTwoShipPointDefenseCharge == 0:
                    slotTwoShipPointDefenseActive = False
                    slotTwoShipPointDefenseCooldown = 10
                    slotTwoEnergyCooldown = True
            elif slotTwoShipPointDefenseActive == False and slotTwoShipPointDefenseCharge != 100:
                slotTwoShipPointDefenseCharge += 1
                slotTwoEnergyCooldown = True
                if selectedSlot == 2:
                    printWhiteText(str(slotTwoShipPointDefenseCharge), 30, 807, 868)

        # Point defense for ship three.
        if slotThreeShipPointDefenseCooldown != 0:
            slotThreeShipPointDefenseCooldown -= 1
            if selectedSlot == 3:
                screen.blit(cooldownBackground, (772, 830))
                screen.blit(cooldownBackgroundDark, (772, 830))
                printWhiteText(str(slotThreeShipPointDefenseCooldown), 30, 807, 868)
        elif slotThreeShipPointDefenseCooldown == 0:
            if slotThreeShipPointDefenseActive == True and slotThreeShipPointDefenseCharge != 0:
                fleetShipThreePointDefenseEff = 0.5
                slotThreeShipPointDefenseCharge -= 1
                slotThreeShipEnergy -= 25
                slotThreeEnergyCooldown = False
                if selectedSlot == 3:
                    screen.blit(activeBackground, (772, 830))
                    printWhiteText(str(slotThreeShipPointDefenseCharge), 30, 807, 868)
                if slotThreeShipPointDefenseCharge == 0:
                    slotThreeShipPointDefenseActive = False
                    slotThreeShipPointDefenseCooldown = 10
                    slotThreeEnergyCooldown = True
            elif slotThreeShipPointDefenseActive == False and slotThreeShipPointDefenseCharge != 100:
                slotThreeShipPointDefenseCharge += 1
                slotThreeEnergyCooldown = True
                if selectedSlot == 3:
                    printWhiteText(str(slotThreeShipPointDefenseCharge), 30, 807, 868)


        #Pioneer.
        if pioneerVoidChargesCooldown != 0:
            pioneerVoidChargesCooldown -= 1
            if fleetSlotOne == 'Pioneer' and selectedSlot == 1 or fleetSlotTwo == 'Pioneer' and selectedSlot == 2 or fleetSlotThree == 'Pioneer' and selectedSlot == 3:
                screen.blit(cooldownBackground, (1108, 830))
                screen.blit(cooldownBackgroundDark, (1108, 830))
                printWhiteText(str(pioneerVoidChargesCooldown), 30, 1143, 868)
        if pioneerMissilesCooldown != 0:
            pioneerMissilesCooldown -= 1
            if fleetSlotOne == 'Pioneer' and selectedSlot == 1 or fleetSlotTwo == 'Pioneer' and selectedSlot == 2 or fleetSlotThree == 'Pioneer' and selectedSlot == 3:
                screen.blit(cooldownBackground, (660, 830))
                screen.blit(cooldownBackgroundDark, (660, 830))
                printWhiteText(str(pioneerMissilesCooldown), 30, 695, 868)

        #Colossus.
        if colossusFlakCooldown != 0:
            colossusFlakCooldown -= 1
            if fleetSlotOne == 'Colossus' and selectedSlot == 1 or fleetSlotTwo == 'Colossus' and selectedSlot == 2 or fleetSlotThree == 'Colossus' and selectedSlot == 3:
                screen.blit(cooldownBackground, (1108, 830))
                screen.blit(cooldownBackgroundDark, (1108, 830))
                printWhiteText(str(colossusFlakCooldown), 30, 1143, 868)



        #Printing statiscics of various ships.
        printWhiteText('Health: ' + str(slotOneShipHealth), 30, 330, 668)
        printWhiteText('Energy: ' + str(slotOneShipEnergy), 30, 330, 698)

        printWhiteText('Health: ' + str(slotTwoShipHealth), 30, 820, 768)
        printWhiteText('Energy: ' + str(slotTwoShipEnergy), 30, 820, 798)

        printWhiteText('Health: ' + str(slotThreeShipHealth), 30, 1160, 668)
        printWhiteText('Energy: ' + str(slotThreeShipEnergy), 30, 1160, 698)


        #Print score and wave.
        printWhiteText('Score: ' + str(score), 20, 875, 60)

        printWhiteText('Wave', 20, 1170, 80)
        printWhiteText(str(waveNumber), 50, 1172, 118)




        # Minimap.
        if showExpandedMap == False:


            sector = pygame.image.load('sector.png')
            screen.blit(sector, (1280, 700))
            screen.blit(sector, (1404, 700))
            screen.blit(sector, (1528, 700))

            outpostSector = pygame.image.load('outpostSector.png')
            screen.blit(outpostSector, (1384, 830))

            pygame.draw.circle(screen, white, (1453, 887), 28, 3)
            pygame.draw.circle(screen, white, (1329, 770), 18, 2)
            pygame.draw.circle(screen, white, (1453, 770), 18, 2)
            pygame.draw.circle(screen, white, (1577, 770), 18, 2)



            printWhiteText('Alpha', 18, 1330, 687)
            printWhiteText('Delta', 18, 1453, 687)
            printWhiteText('Beta', 18, 1575, 687)
            printWhiteText('Outpost', 18, 1450, 817)

            fleetSmall = pygame.image.load('fleetSmall.png')

            if fleetSector == 'outpost':
                if fleetX == 10000 and fleetY == 40000:
                    screen.blit(fleetSmall, (1401, 864))
                elif fleetX == 35000 and fleetY == 20000:
                    screen.blit(fleetSmall, (1445, 884))
                elif fleetX == 60000 and fleetY == 40000:
                    screen.blit(fleetSmall, (1490, 864))

            elif fleetSector == 'alpha':
                if fleetX == 10000 and fleetY == 15000:
                    screen.blit(fleetSmall, (1290, 762))
                elif fleetX == 40000 and fleetY == 15000:
                    screen.blit(fleetSmall, (1353, 762))
                elif fleetX == 25000 and fleetY == 15000:
                    screen.blit(fleetSmall, (1321, 766))
                elif fleetX == 10000 and fleetY == 40000:
                    screen.blit(fleetSmall, (1291, 717))
                elif fleetX == 20000 and fleetY == 40000:
                    screen.blit(fleetSmall, (1311, 717))
                elif fleetX == 30000 and fleetY == 40000:
                    screen.blit(fleetSmall, (1331, 717))
                elif fleetX == 40000 and fleetY == 40000:
                    screen.blit(fleetSmall, (1351, 717))
                elif fleetX == 10000 and fleetY == 30000:
                    screen.blit(fleetSmall, (1291, 735))
                elif fleetX == 20000 and fleetY == 30000:
                    screen.blit(fleetSmall, (1311, 735))
                elif fleetX == 30000 and fleetY == 30000:
                    screen.blit(fleetSmall, (1331, 735))
                elif fleetX == 40000 and fleetY == 30000:
                    screen.blit(fleetSmall, (1351, 735))

            elif fleetSector == 'delta':
                if fleetX == 10000 and fleetY == 15000:
                    screen.blit(fleetSmall, (1414, 762))
                elif fleetX == 40000 and fleetY == 15000:
                    screen.blit(fleetSmall, (1477, 762))
                elif fleetX == 25000 and fleetY == 15000:
                    screen.blit(fleetSmall, (1445, 766))
                elif fleetX == 10000 and fleetY == 40000:
                    screen.blit(fleetSmall, (1415, 717))
                elif fleetX == 20000 and fleetY == 40000:
                    screen.blit(fleetSmall, (1435, 717))
                elif fleetX == 30000 and fleetY == 40000:
                    screen.blit(fleetSmall, (1455, 717))
                elif fleetX == 40000 and fleetY == 40000:
                    screen.blit(fleetSmall, (1475, 717))
                elif fleetX == 10000 and fleetY == 30000:
                    screen.blit(fleetSmall, (1415, 735))
                elif fleetX == 20000 and fleetY == 30000:
                    screen.blit(fleetSmall, (1435, 735))
                elif fleetX == 30000 and fleetY == 30000:
                    screen.blit(fleetSmall, (1455, 735))
                elif fleetX == 40000 and fleetY == 30000:
                    screen.blit(fleetSmall, (1475, 735))

            elif fleetSector == 'beta':
                if fleetX == 10000 and fleetY == 15000:
                    screen.blit(fleetSmall, (1538, 762))
                elif fleetX == 40000 and fleetY == 15000:
                    screen.blit(fleetSmall, (1601, 762))
                elif fleetX == 25000 and fleetY == 15000:
                    screen.blit(fleetSmall, (1569, 766))
                elif fleetX == 10000 and fleetY == 40000:
                    screen.blit(fleetSmall, (1539, 717))
                elif fleetX == 20000 and fleetY == 40000:
                    screen.blit(fleetSmall, (1559, 717))
                elif fleetX == 30000 and fleetY == 40000:
                    screen.blit(fleetSmall, (1579, 717))
                elif fleetX == 40000 and fleetY == 40000:
                    screen.blit(fleetSmall, (1599, 717))
                elif fleetX == 10000 and fleetY == 30000:
                    screen.blit(fleetSmall, (1539, 735))
                elif fleetX == 20000 and fleetY == 30000:
                    screen.blit(fleetSmall, (1559, 735))
                elif fleetX == 30000 and fleetY == 30000:
                    screen.blit(fleetSmall, (1579, 735))
                elif fleetX == 40000 and fleetY == 30000:
                    screen.blit(fleetSmall, (1599, 735))





        #Fleet will only move to a new location if distanceToTargetLocation == 0.

        if distanceToTargetLocation != 0 and distanceToTargetLocation > 0:
            distanceToTargetLocation -= fleetSpeed * 3
        elif distanceToTargetLocation <= 0 and jumpTimer == 0 and fleetSector == targetSector:
            fleetX = targetfleetX
            fleetY = targetfleetY

        if distanceToTargetLocation > 0:
            printWhiteText('Distance: ' + str(distanceToTargetLocation) + ' Meters', 22, 1500, 190)

        printWhiteText('sector == ' + fleetSector, 22, 1500, 100)
        printWhiteText('fleetX == ' + str(fleetX), 22, 1500, 130)
        printWhiteText('fleetY == ' + str(fleetY), 22, 1500, 160)

        printWhiteText('fleetSpeed == ' + str(fleetSpeed), 22, 1500, 220)


        #Expanded map view.
        expandedMapBackground = pygame.image.load('expandedMapBackground.png')
        outpostSectorLarge = pygame.image.load('outpostSectorLarge.png')
        sectorLarge = pygame.image.load('sectorLarge.png')
        jumpPoint = pygame.image.load('jumpPoint.png')
        jumpPointAvailable = pygame.image.load('jumpPointAvailable.png')
        jumpPointHoverOver = pygame.image.load('jumpPointHoverOver.png')
        fleet = pygame.image.load('fleet.png')

        if showExpandedMap == True:
            screen.blit(expandedMapBackground, (0, 0))

            screen.blit(outpostSectorLarge, (724, 550))
            screen.blit(sectorLarge, (514, 300))
            screen.blit(sectorLarge, (764, 300))
            screen.blit(sectorLarge, (1014, 300))

            if fleetSector == 'outpost':
                pygame.draw.circle(screen, lightGrey, (612, 440), 5, 5)
                pygame.draw.circle(screen, lightGrey, (549, 330), 5, 5)
                pygame.draw.circle(screen, lightGrey, (593, 330), 5, 5)
                pygame.draw.circle(screen, lightGrey, (637, 330), 5, 5)
                pygame.draw.circle(screen, lightGrey, (679, 330), 5, 5)
                pygame.draw.circle(screen, lightGrey, (549, 370), 5, 5)
                pygame.draw.circle(screen, lightGrey, (593, 370), 5, 5)
                pygame.draw.circle(screen, lightGrey, (637, 370), 5, 5)
                pygame.draw.circle(screen, lightGrey, (679, 370), 5, 5)

                pygame.draw.circle(screen, lightGrey, (866, 440), 5, 5)
                pygame.draw.circle(screen, lightGrey, (799, 330), 5, 5)
                pygame.draw.circle(screen, lightGrey, (843, 330), 5, 5)
                pygame.draw.circle(screen, lightGrey, (887, 330), 5, 5)
                pygame.draw.circle(screen, lightGrey, (929, 330), 5, 5)
                pygame.draw.circle(screen, lightGrey, (799, 370), 5, 5)
                pygame.draw.circle(screen, lightGrey, (843, 370), 5, 5)
                pygame.draw.circle(screen, lightGrey, (887, 370), 5, 5)
                pygame.draw.circle(screen, lightGrey, (929, 370), 5, 5)

                pygame.draw.circle(screen, lightGrey, (1113, 440), 5, 5)
                pygame.draw.circle(screen, lightGrey, (1049, 330), 5, 5)
                pygame.draw.circle(screen, lightGrey, (1093, 330), 5, 5)
                pygame.draw.circle(screen, lightGrey, (1137, 330), 5, 5)
                pygame.draw.circle(screen, lightGrey, (1179, 330), 5, 5)
                pygame.draw.circle(screen, lightGrey, (1049, 370), 5, 5)
                pygame.draw.circle(screen, lightGrey, (1093, 370), 5, 5)
                pygame.draw.circle(screen, lightGrey, (1137, 370), 5, 5)
                pygame.draw.circle(screen, lightGrey, (1179, 370), 5, 5)

                screen.blit(jumpPointAvailable, (530, 420))
                screen.blit(jumpPointAvailable, (665, 420))
                screen.blit(jumpPointAvailable, (781, 420))
                screen.blit(jumpPointAvailable, (917, 420))
                screen.blit(jumpPointAvailable, (1030, 420))
                screen.blit(jumpPointAvailable, (1165, 420))
                screen.blit(jumpPoint, (749, 582))
                screen.blit(jumpPoint, (851, 634))
                screen.blit(jumpPoint, (949, 582))
                if 571 > mouse[0] > 540 and 445 > mouse[1] > 420:
                    screen.blit(jumpPointHoverOver, (526, 413))
                    if click[0] == 1 and jumpTimer == 0:
                        jumpTimer = 25
                        targetSector = 'alpha'
                        targetfleetX = 10000
                        targetfleetY = 15000
                elif 696 > mouse[0] > 665 and 445 > mouse[1] > 420:
                    screen.blit(jumpPointHoverOver, (661, 413))
                    if click[0] == 1 and jumpTimer == 0:
                        jumpTimer = 25
                        targetSector = 'alpha'
                        targetfleetX = 40000
                        targetfleetY = 15000
                elif 812 > mouse[0] > 781 and 445 > mouse[1] > 420:
                    screen.blit(jumpPointHoverOver, (777, 413))
                    if click[0] == 1 and jumpTimer == 0:
                        jumpTimer = 25
                        targetSector = 'delta'
                        targetfleetX = 10000
                        targetfleetY = 15000
                elif 948 > mouse[0] > 917 and 445 > mouse[1] > 420:
                    screen.blit(jumpPointHoverOver, (913, 413))
                    if click[0] == 1 and jumpTimer == 0:
                        jumpTimer = 25
                        targetSector = 'delta'
                        targetfleetX = 40000
                        targetfleetY = 15000
                elif 1061 > mouse[0] > 1030 and 445 > mouse[1] > 420:
                    screen.blit(jumpPointHoverOver, (1026, 413))
                    if click[0] == 1 and jumpTimer == 0:
                        jumpTimer = 25
                        targetSector = 'beta'
                        targetfleetX = 10000
                        targetfleetY = 15000
                elif 1196 > mouse[0] > 1165 and 445 > mouse[1] > 420:
                    screen.blit(jumpPointHoverOver, (1161, 413))
                    if click[0] == 1 and jumpTimer == 0:
                        jumpTimer = 25
                        targetSector = 'beta'
                        targetfleetX = 40000
                        targetfleetY = 15000

                if fleetX == 35000 and fleetY == 20000:
                    pygame.draw.circle(screen, lightGrey, (866, 660), 5, 5)
                    pygame.draw.circle(screen, white, (764, 608), 5, 5)
                    pygame.draw.circle(screen, white, (964, 608), 5, 5)
                    screen.blit(fleet, (850, 657))
                    if 778 > mouse[0] > 760 and 622 > mouse[1] > 604:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 32000
                            targetfleetX = 10000
                            targetfleetY = 40000
                    elif 978 > mouse[0] > 960 and 622 > mouse[1] > 604:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 32000
                            targetfleetX = 60000
                            targetfleetY = 40000

                elif fleetX == 10000 and fleetY == 40000:
                    pygame.draw.circle(screen, white, (866, 660), 5, 5)
                    pygame.draw.circle(screen, lightGrey, (764, 608), 5, 5)
                    pygame.draw.circle(screen, white, (964, 608), 5, 5)
                    screen.blit(fleet, (748, 605))
                    if 880 > mouse[0] > 862 and 674 > mouse[1] > 656:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 32000
                            targetfleetX = 35000
                            targetfleetY = 20000
                    elif 978 > mouse[0] > 960 and 622 > mouse[1] > 604:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 50000
                            targetfleetX = 60000
                            targetfleetY = 40000

                elif fleetX == 60000 and fleetY == 40000:
                    pygame.draw.circle(screen, white, (866, 660), 5, 5)
                    pygame.draw.circle(screen, white, (764, 608), 5, 5)
                    pygame.draw.circle(screen, lightGrey, (964, 608), 5, 5)
                    screen.blit(fleet, (948, 605))
                    if 880 > mouse[0] > 862 and 674 > mouse[1] > 656:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 32000
                            targetfleetX = 35000
                            targetfleetY = 20000
                    elif 778 > mouse[0] > 760 and 622 > mouse[1] > 604:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 50000
                            targetfleetX = 10000
                            targetfleetY = 40000


            elif fleetSector == 'alpha':

                if fleetX == 10000 and fleetY == 15000 or fleetX == 40000 and fleetY == 15000:
                    pygame.draw.circle(screen, white, (612, 440), 5, 5)
                    pygame.draw.circle(screen, white, (549, 330), 5, 5)
                    pygame.draw.circle(screen, white, (593, 330), 5, 5)
                    pygame.draw.circle(screen, white, (637, 330), 5, 5)
                    pygame.draw.circle(screen, white, (679, 330), 5, 5)
                    pygame.draw.circle(screen, white, (549, 370), 5, 5)
                    pygame.draw.circle(screen, white, (593, 370), 5, 5)
                    pygame.draw.circle(screen, white, (637, 370), 5, 5)
                    pygame.draw.circle(screen, white, (679, 370), 5, 5)


                pygame.draw.circle(screen, lightGrey, (866, 440), 5, 5)
                pygame.draw.circle(screen, lightGrey, (799, 330), 5, 5)
                pygame.draw.circle(screen, lightGrey, (843, 330), 5, 5)
                pygame.draw.circle(screen, lightGrey, (887, 330), 5, 5)
                pygame.draw.circle(screen, lightGrey, (929, 330), 5, 5)
                pygame.draw.circle(screen, lightGrey, (799, 370), 5, 5)
                pygame.draw.circle(screen, lightGrey, (843, 370), 5, 5)
                pygame.draw.circle(screen, lightGrey, (887, 370), 5, 5)
                pygame.draw.circle(screen, lightGrey, (929, 370), 5, 5)

                pygame.draw.circle(screen, lightGrey, (1113, 440), 5, 5)
                pygame.draw.circle(screen, lightGrey, (1049, 330), 5, 5)
                pygame.draw.circle(screen, lightGrey, (1093, 330), 5, 5)
                pygame.draw.circle(screen, lightGrey, (1137, 330), 5, 5)
                pygame.draw.circle(screen, lightGrey, (1179, 330), 5, 5)
                pygame.draw.circle(screen, lightGrey, (1049, 370), 5, 5)
                pygame.draw.circle(screen, lightGrey, (1093, 370), 5, 5)
                pygame.draw.circle(screen, lightGrey, (1137, 370), 5, 5)
                pygame.draw.circle(screen, lightGrey, (1179, 370), 5, 5)

                pygame.draw.circle(screen, lightGrey, (866, 660), 5, 5)
                pygame.draw.circle(screen, lightGrey, (764, 608), 5, 5)
                pygame.draw.circle(screen, lightGrey, (964, 608), 5, 5)

                screen.blit(jumpPoint, (530, 420))
                screen.blit(jumpPoint, (665, 420))
                screen.blit(jumpPointAvailable, (781, 420))
                screen.blit(jumpPoint, (917, 420))
                screen.blit(jumpPoint, (1030, 420))
                screen.blit(jumpPoint, (1165, 420))
                screen.blit(jumpPointAvailable, (749, 582))
                screen.blit(jumpPointAvailable, (851, 634))
                screen.blit(jumpPoint, (949, 582))



                if fleetX == 10000 and fleetY == 15000:
                    screen.blit(fleet, (529, 433))
                    if 563 > mouse[0] > 545 and 344 > mouse[1] > 326:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 25000
                            targetfleetX = 10000
                            targetfleetY = 40000
                    elif 607 > mouse[0] > 589 and 344 > mouse[1] > 326:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 27000
                            targetfleetX = 20000
                            targetfleetY = 40000
                    elif 651 > mouse[0] > 633 and 344 > mouse[1] > 326:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 32000
                            targetfleetX = 30000
                            targetfleetY = 40000
                    elif 695 > mouse[0] > 677 and 344 > mouse[1] > 326:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 39000
                            targetfleetX = 40000
                            targetfleetY = 40000
                    elif 563 > mouse[0] > 545 and 384 > mouse[1] > 366:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 15000
                            targetfleetX = 10000
                            targetfleetY = 30000
                    elif 607 > mouse[0] > 589 and 384 > mouse[1] > 366:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 18000
                            targetfleetX = 20000
                            targetfleetY = 30000
                    elif 651 > mouse[0] > 633 and 384 > mouse[1] > 366:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 25000
                            targetfleetX = 30000
                            targetfleetY = 30000
                    elif 695 > mouse[0] > 677 and 384 > mouse[1] > 366:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 33000
                            targetfleetX = 40000
                            targetfleetY = 30000
                    elif 626 > mouse[0] > 608 and 454 > mouse[1] > 436:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 15000
                            targetfleetX = 25000
                            targetfleetY = 15000

                elif fleetX == 40000 and fleetY == 15000:
                    screen.blit(fleet, (664, 433))
                    if 563 > mouse[0] > 545 and 344 > mouse[1] > 326:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 39000
                            targetfleetX = 10000
                            targetfleetY = 40000
                    elif 607 > mouse[0] > 589 and 344 > mouse[1] > 326:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 20000
                            targetfleetX = 20000
                            targetfleetY = 40000
                    elif 651 > mouse[0] > 633 and 344 > mouse[1] > 326:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 27000
                            targetfleetX = 30000
                            targetfleetY = 40000
                    elif 695 > mouse[0] > 677 and 344 > mouse[1] > 326:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 25000
                            targetfleetX = 40000
                            targetfleetY = 40000
                    elif 563 > mouse[0] > 545 and 384 > mouse[1] > 366:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 33000
                            targetfleetX = 10000
                            targetfleetY = 30000
                    elif 607 > mouse[0] > 589 and 384 > mouse[1] > 366:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 25000
                            targetfleetX = 20000
                            targetfleetY = 30000
                    elif 651 > mouse[0] > 633 and 384 > mouse[1] > 366:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 18000
                            targetfleetX = 30000
                            targetfleetY = 30000
                    elif 695 > mouse[0] > 677 and 384 > mouse[1] > 366:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 15000
                            targetfleetX = 40000
                            targetfleetY = 30000
                    elif 626 > mouse[0] > 608 and 454 > mouse[1] > 436:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 15000
                            targetfleetX = 25000
                            targetfleetY = 15000


                elif fleetX == 25000 and fleetY == 15000:
                    pygame.draw.circle(screen, lightGrey, (612, 440), 5, 5)
                    pygame.draw.circle(screen, white, (549, 330), 5, 5)
                    pygame.draw.circle(screen, white, (593, 330), 5, 5)
                    pygame.draw.circle(screen, white, (637, 330), 5, 5)
                    pygame.draw.circle(screen, white, (679, 330), 5, 5)
                    pygame.draw.circle(screen, white, (549, 370), 5, 5)
                    pygame.draw.circle(screen, white, (593, 370), 5, 5)
                    pygame.draw.circle(screen, white, (637, 370), 5, 5)
                    pygame.draw.circle(screen, white, (679, 370), 5, 5)
                    screen.blit(fleet, (596, 438))
                    if 563 > mouse[0] > 545 and 344 > mouse[1] > 326:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 29000
                            targetfleetX = 10000
                            targetfleetY = 40000
                    elif 607 > mouse[0] > 589 and 344 > mouse[1] > 326:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 25000
                            targetfleetX = 20000
                            targetfleetY = 40000
                    elif 651 > mouse[0] > 633 and 344 > mouse[1] > 326:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 25000
                            targetfleetX = 30000
                            targetfleetY = 40000
                    elif 695 > mouse[0] > 677 and 344 > mouse[1] > 326:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 29000
                            targetfleetX = 40000
                            targetfleetY = 40000
                    elif 563 > mouse[0] > 545 and 384 > mouse[1] > 366:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 21000
                            targetfleetX = 10000
                            targetfleetY = 30000
                    elif 607 > mouse[0] > 589 and 384 > mouse[1] > 366:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 16000
                            targetfleetX = 20000
                            targetfleetY = 30000
                    elif 651 > mouse[0] > 633 and 384 > mouse[1] > 366:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 16000
                            targetfleetX = 30000
                            targetfleetY = 30000
                    elif 695 > mouse[0] > 677 and 384 > mouse[1] > 366:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 21000
                            targetfleetX = 40000
                            targetfleetY = 30000


                elif fleetX == 10000 and fleetY == 40000:
                    pygame.draw.circle(screen, white, (612, 440), 5, 5)
                    pygame.draw.circle(screen, lightGrey, (549, 330), 5, 5)
                    pygame.draw.circle(screen, white, (593, 330), 5, 5)
                    pygame.draw.circle(screen, white, (637, 330), 5, 5)
                    pygame.draw.circle(screen, white, (679, 330), 5, 5)
                    pygame.draw.circle(screen, white, (549, 370), 5, 5)
                    pygame.draw.circle(screen, white, (593, 370), 5, 5)
                    pygame.draw.circle(screen, white, (637, 370), 5, 5)
                    pygame.draw.circle(screen, white, (679, 370), 5, 5)
                    screen.blit(fleet, (533, 328))
                    if 607 > mouse[0] > 589 and 344 > mouse[1] > 326:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 10000
                            targetfleetX = 20000
                            targetfleetY = 40000
                    elif 651 > mouse[0] > 633 and 344 > mouse[1] > 326:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 20000
                            targetfleetX = 30000
                            targetfleetY = 40000
                    elif 695 > mouse[0] > 677 and 344 > mouse[1] > 326:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 30000
                            targetfleetX = 40000
                            targetfleetY = 40000
                    elif 563 > mouse[0] > 545 and 384 > mouse[1] > 366:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 10000
                            targetfleetX = 10000
                            targetfleetY = 30000
                    elif 607 > mouse[0] > 589 and 384 > mouse[1] > 366:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 14000
                            targetfleetX = 20000
                            targetfleetY = 30000
                    elif 651 > mouse[0] > 633 and 384 > mouse[1] > 366:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 22000
                            targetfleetX = 30000
                            targetfleetY = 30000
                    elif 695 > mouse[0] > 677 and 384 > mouse[1] > 366:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 32000
                            targetfleetX = 40000
                            targetfleetY = 30000
                    elif 626 > mouse[0] > 608 and 454 > mouse[1] > 436:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 29000
                            targetfleetX = 25000
                            targetfleetY = 15000

                elif fleetX == 20000 and fleetY == 40000:
                    pygame.draw.circle(screen, white, (612, 440), 5, 5)
                    pygame.draw.circle(screen, white, (549, 330), 5, 5)
                    pygame.draw.circle(screen, lightGrey, (593, 330), 5, 5)
                    pygame.draw.circle(screen, white, (637, 330), 5, 5)
                    pygame.draw.circle(screen, white, (679, 330), 5, 5)
                    pygame.draw.circle(screen, white, (549, 370), 5, 5)
                    pygame.draw.circle(screen, white, (593, 370), 5, 5)
                    pygame.draw.circle(screen, white, (637, 370), 5, 5)
                    pygame.draw.circle(screen, white, (679, 370), 5, 5)
                    screen.blit(fleet, (577, 328))
                    if 563 > mouse[0] > 545 and 344 > mouse[1] > 326:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 10000
                            targetfleetX = 10000
                            targetfleetY = 40000
                    elif 651 > mouse[0] > 633 and 344 > mouse[1] > 326:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 10000
                            targetfleetX = 30000
                            targetfleetY = 40000
                    elif 695 > mouse[0] > 677 and 344 > mouse[1] > 326:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 20000
                            targetfleetX = 40000
                            targetfleetY = 40000
                    elif 563 > mouse[0] > 545 and 384 > mouse[1] > 366:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 14000
                            targetfleetX = 10000
                            targetfleetY = 30000
                    elif 607 > mouse[0] > 589 and 384 > mouse[1] > 366:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 10000
                            targetfleetX = 20000
                            targetfleetY = 30000
                    elif 651 > mouse[0] > 633 and 384 > mouse[1] > 366:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 14000
                            targetfleetX = 30000
                            targetfleetY = 30000
                    elif 695 > mouse[0] > 677 and 384 > mouse[1] > 366:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 25000
                            targetfleetX = 40000
                            targetfleetY = 30000
                    elif 626 > mouse[0] > 608 and 454 > mouse[1] > 436:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 29000
                            targetfleetX = 25000
                            targetfleetY = 15000

                elif fleetX == 30000 and fleetY == 40000:
                    pygame.draw.circle(screen, white, (612, 440), 5, 5)
                    pygame.draw.circle(screen, white, (549, 330), 5, 5)
                    pygame.draw.circle(screen, white, (593, 330), 5, 5)
                    pygame.draw.circle(screen, lightGrey, (637, 330), 5, 5)
                    pygame.draw.circle(screen, white, (679, 330), 5, 5)
                    pygame.draw.circle(screen, white, (549, 370), 5, 5)
                    pygame.draw.circle(screen, white, (593, 370), 5, 5)
                    pygame.draw.circle(screen, white, (637, 370), 5, 5)
                    pygame.draw.circle(screen, white, (679, 370), 5, 5)
                    screen.blit(fleet, (621, 328))
                    if 563 > mouse[0] > 545 and 344 > mouse[1] > 326:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 20000
                            targetfleetX = 10000
                            targetfleetY = 40000
                    elif 607 > mouse[0] > 589 and 344 > mouse[1] > 326:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 10000
                            targetfleetX = 20000
                            targetfleetY = 40000
                    elif 695 > mouse[0] > 677 and 344 > mouse[1] > 326:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 10000
                            targetfleetX = 40000
                            targetfleetY = 40000
                    elif 563 > mouse[0] > 545 and 384 > mouse[1] > 366:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 22000
                            targetfleetX = 10000
                            targetfleetY = 30000
                    elif 607 > mouse[0] > 589 and 384 > mouse[1] > 366:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 14000
                            targetfleetX = 20000
                            targetfleetY = 30000
                    elif 651 > mouse[0] > 633 and 384 > mouse[1] > 366:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 10000
                            targetfleetX = 30000
                            targetfleetY = 30000
                    elif 695 > mouse[0] > 677 and 384 > mouse[1] > 366:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 50000
                            targetfleetX = 40000
                            targetfleetY = 30000
                    elif 626 > mouse[0] > 608 and 454 > mouse[1] > 436:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 29000
                            targetfleetX = 25000
                            targetfleetY = 15000

                elif fleetX == 40000 and fleetY == 40000:
                    pygame.draw.circle(screen, white, (612, 440), 5, 5)
                    pygame.draw.circle(screen, white, (549, 330), 5, 5)
                    pygame.draw.circle(screen, white, (593, 330), 5, 5)
                    pygame.draw.circle(screen, white, (637, 330), 5, 5)
                    pygame.draw.circle(screen, lightGrey, (679, 330), 5, 5)
                    pygame.draw.circle(screen, white, (549, 370), 5, 5)
                    pygame.draw.circle(screen, white, (593, 370), 5, 5)
                    pygame.draw.circle(screen, white, (637, 370), 5, 5)
                    pygame.draw.circle(screen, white, (679, 370), 5, 5)
                    screen.blit(fleet, (663, 328))
                    if 563 > mouse[0] > 545 and 344 > mouse[1] > 326:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 30000
                            targetfleetX = 10000
                            targetfleetY = 40000
                    elif 607 > mouse[0] > 589 and 344 > mouse[1] > 326:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 20000
                            targetfleetX = 20000
                            targetfleetY = 40000
                    elif 651 > mouse[0] > 633 and 344 > mouse[1] > 326:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 10000
                            targetfleetX = 30000
                            targetfleetY = 40000
                    elif 563 > mouse[0] > 545 and 384 > mouse[1] > 366:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 32000
                            targetfleetX = 10000
                            targetfleetY = 30000
                    elif 607 > mouse[0] > 589 and 384 > mouse[1] > 366:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 22000
                            targetfleetX = 20000
                            targetfleetY = 30000
                    elif 651 > mouse[0] > 633 and 384 > mouse[1] > 366:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 14000
                            targetfleetX = 30000
                            targetfleetY = 30000
                    elif 695 > mouse[0] > 677 and 384 > mouse[1] > 366:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 10000
                            targetfleetX = 40000
                            targetfleetY = 30000
                    elif 626 > mouse[0] > 608 and 454 > mouse[1] > 436:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 29000
                            targetfleetX = 25000
                            targetfleetY = 15000

                elif fleetX == 10000 and fleetY == 30000:
                    pygame.draw.circle(screen, white, (612, 440), 5, 5)
                    pygame.draw.circle(screen, white, (549, 330), 5, 5)
                    pygame.draw.circle(screen, white, (593, 330), 5, 5)
                    pygame.draw.circle(screen, white, (637, 330), 5, 5)
                    pygame.draw.circle(screen, white, (679, 330), 5, 5)
                    pygame.draw.circle(screen, lightGrey, (549, 370), 5, 5)
                    pygame.draw.circle(screen, white, (593, 370), 5, 5)
                    pygame.draw.circle(screen, white, (637, 370), 5, 5)
                    pygame.draw.circle(screen, white, (679, 370), 5, 5)
                    screen.blit(fleet, (533, 367))
                    if 563 > mouse[0] > 545 and 344 > mouse[1] > 326:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 10000
                            targetfleetX = 10000
                            targetfleetY = 40000
                    elif 607 > mouse[0] > 589 and 344 > mouse[1] > 326:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 14000
                            targetfleetX = 20000
                            targetfleetY = 40000
                    elif 651 > mouse[0] > 633 and 344 > mouse[1] > 326:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 22000
                            targetfleetX = 30000
                            targetfleetY = 40000
                    elif 695 > mouse[0] > 677 and 344 > mouse[1] > 326:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 32000
                            targetfleetX = 40000
                            targetfleetY = 40000
                    elif 607 > mouse[0] > 589 and 384 > mouse[1] > 366:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 10000
                            targetfleetX = 20000
                            targetfleetY = 30000
                    elif 651 > mouse[0] > 633 and 384 > mouse[1] > 366:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 20000
                            targetfleetX = 30000
                            targetfleetY = 30000
                    elif 695 > mouse[0] > 677 and 384 > mouse[1] > 366:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 30000
                            targetfleetX = 40000
                            targetfleetY = 30000
                    elif 626 > mouse[0] > 608 and 454 > mouse[1] > 436:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 21000
                            targetfleetX = 25000
                            targetfleetY = 15000



                elif fleetX == 20000 and fleetY == 30000:
                    pygame.draw.circle(screen, white, (612, 440), 5, 5)
                    pygame.draw.circle(screen, white, (549, 330), 5, 5)
                    pygame.draw.circle(screen, white, (593, 330), 5, 5)
                    pygame.draw.circle(screen, white, (637, 330), 5, 5)
                    pygame.draw.circle(screen, white, (679, 330), 5, 5)
                    pygame.draw.circle(screen, white, (549, 370), 5, 5)
                    pygame.draw.circle(screen, lightGrey, (593, 370), 5, 5)
                    pygame.draw.circle(screen, white, (637, 370), 5, 5)
                    pygame.draw.circle(screen, white, (679, 370), 5, 5)
                    screen.blit(fleet, (577, 367))
                    if 563 > mouse[0] > 545 and 344 > mouse[1] > 326:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 14000
                            targetfleetX = 10000
                            targetfleetY = 40000
                    elif 607 > mouse[0] > 589 and 344 > mouse[1] > 326:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 10000
                            targetfleetX = 20000
                            targetfleetY = 40000
                    elif 651 > mouse[0] > 633 and 344 > mouse[1] > 326:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 14000
                            targetfleetX = 30000
                            targetfleetY = 40000
                    elif 695 > mouse[0] > 677 and 344 > mouse[1] > 326:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 229000
                            targetfleetX = 40000
                            targetfleetY = 40000
                    elif 563 > mouse[0] > 545 and 384 > mouse[1] > 366:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 10000
                            targetfleetX = 10000
                            targetfleetY = 30000
                    elif 651 > mouse[0] > 633 and 384 > mouse[1] > 366:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 10000
                            targetfleetX = 30000
                            targetfleetY = 30000
                    elif 695 > mouse[0] > 677 and 384 > mouse[1] > 366:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 20000
                            targetfleetX = 40000
                            targetfleetY = 30000
                    elif 626 > mouse[0] > 608 and 454 > mouse[1] > 436:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 16000
                            targetfleetX = 25000
                            targetfleetY = 15000

                elif fleetX == 30000 and fleetY == 30000:
                    pygame.draw.circle(screen, white, (612, 440), 5, 5)
                    pygame.draw.circle(screen, white, (549, 330), 5, 5)
                    pygame.draw.circle(screen, white, (593, 330), 5, 5)
                    pygame.draw.circle(screen, white, (637, 330), 5, 5)
                    pygame.draw.circle(screen, white, (679, 330), 5, 5)
                    pygame.draw.circle(screen, white, (549, 370), 5, 5)
                    pygame.draw.circle(screen, white, (593, 370), 5, 5)
                    pygame.draw.circle(screen, lightGrey, (637, 370), 5, 5)
                    pygame.draw.circle(screen, white, (679, 370), 5, 5)
                    screen.blit(fleet, (621, 367))
                    if 563 > mouse[0] > 545 and 344 > mouse[1] > 326:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 22000
                            targetfleetX = 10000
                            targetfleetY = 40000
                    elif 607 > mouse[0] > 589 and 344 > mouse[1] > 326:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 14000
                            targetfleetX = 20000
                            targetfleetY = 40000
                    elif 651 > mouse[0] > 633 and 344 > mouse[1] > 326:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 10000
                            targetfleetX = 30000
                            targetfleetY = 40000
                    elif 695 > mouse[0] > 677 and 344 > mouse[1] > 326:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 14000
                            targetfleetX = 40000
                            targetfleetY = 40000
                    elif 563 > mouse[0] > 545 and 384 > mouse[1] > 366:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 20000
                            targetfleetX = 10000
                            targetfleetY = 30000
                    elif 607 > mouse[0] > 589 and 384 > mouse[1] > 366:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 10000
                            targetfleetX = 20000
                            targetfleetY = 30000
                    elif 695 > mouse[0] > 677 and 384 > mouse[1] > 366:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 10000
                            targetfleetX = 40000
                            targetfleetY = 30000
                    elif 626 > mouse[0] > 608 and 454 > mouse[1] > 436:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 16000
                            targetfleetX = 25000
                            targetfleetY = 15000

                elif fleetX == 40000 and fleetY == 30000:
                    pygame.draw.circle(screen, white, (612, 440), 5, 5)
                    pygame.draw.circle(screen, white, (549, 330), 5, 5)
                    pygame.draw.circle(screen, white, (593, 330), 5, 5)
                    pygame.draw.circle(screen, white, (637, 330), 5, 5)
                    pygame.draw.circle(screen, white, (679, 330), 5, 5)
                    pygame.draw.circle(screen, white, (549, 370), 5, 5)
                    pygame.draw.circle(screen, white, (593, 370), 5, 5)
                    pygame.draw.circle(screen, white, (637, 370), 5, 5)
                    pygame.draw.circle(screen, lightGrey, (679, 370), 5, 5)
                    screen.blit(fleet, (663, 367))
                    if 563 > mouse[0] > 545 and 344 > mouse[1] > 326:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 32000
                            targetfleetX = 10000
                            targetfleetY = 40000
                    elif 607 > mouse[0] > 589 and 344 > mouse[1] > 326:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 22000
                            targetfleetX = 20000
                            targetfleetY = 40000
                    elif 651 > mouse[0] > 633 and 344 > mouse[1] > 326:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 14000
                            targetfleetX = 30000
                            targetfleetY = 40000
                    elif 695 > mouse[0] > 677 and 344 > mouse[1] > 326:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 10000
                            targetfleetX = 40000
                            targetfleetY = 40000
                    elif 563 > mouse[0] > 545 and 384 > mouse[1] > 366:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 30000
                            targetfleetX = 10000
                            targetfleetY = 30000
                    elif 607 > mouse[0] > 589 and 384 > mouse[1] > 366:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 20000
                            targetfleetX = 20000
                            targetfleetY = 30000
                    elif 651 > mouse[0] > 633 and 384 > mouse[1] > 366:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 10000
                            targetfleetX = 30000
                            targetfleetY = 30000
                    elif 626 > mouse[0] > 608 and 454 > mouse[1] > 436:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 21000
                            targetfleetX = 25000
                            targetfleetY = 15000

                if 812 > mouse[0] > 781 and 445 > mouse[1] > 420:
                    screen.blit(jumpPointHoverOver, (777, 413))
                    if click[0] == 1 and jumpTimer == 0:
                        jumpTimer = 25
                        targetfleetX = 10000
                        targetfleetY = 15000
                        targetSector = 'delta'
                elif 780 > mouse[0] > 749 and 607 > mouse[1] > 582:
                    screen.blit(jumpPointHoverOver, (745, 575))
                    if click[0] == 1 and jumpTimer == 0:
                        jumpTimer = 25
                        targetfleetX = 10000
                        targetfleetY = 40000
                        targetSector = 'outpost'
                elif 882 > mouse[0] > 851 and 665 > mouse[1] > 634:
                    screen.blit(jumpPointHoverOver, (847, 627))
                    if click[0] == 1 and jumpTimer == 0:
                        jumpTimer = 25
                        targetfleetX = 35000
                        targetfleetY = 20000
                        targetSector = 'outpost'

            elif fleetSector == 'delta':
                if fleetX == 10000 and fleetY == 15000 or fleetX == 40000 and fleetY == 15000:
                    pygame.draw.circle(screen, white, (866, 440), 5, 5)
                    pygame.draw.circle(screen, white, (799, 330), 5, 5)
                    pygame.draw.circle(screen, white, (843, 330), 5, 5)
                    pygame.draw.circle(screen, white, (887, 330), 5, 5)
                    pygame.draw.circle(screen, white, (929, 330), 5, 5)
                    pygame.draw.circle(screen, white, (799, 370), 5, 5)
                    pygame.draw.circle(screen, white, (843, 370), 5, 5)
                    pygame.draw.circle(screen, white, (887, 370), 5, 5)
                    pygame.draw.circle(screen, white, (929, 370), 5, 5)

                pygame.draw.circle(screen, lightGrey, (612, 440), 5, 5)
                pygame.draw.circle(screen, lightGrey, (549, 330), 5, 5)
                pygame.draw.circle(screen, lightGrey, (593, 330), 5, 5)
                pygame.draw.circle(screen, lightGrey, (637, 330), 5, 5)
                pygame.draw.circle(screen, lightGrey, (679, 330), 5, 5)
                pygame.draw.circle(screen, lightGrey, (549, 370), 5, 5)
                pygame.draw.circle(screen, lightGrey, (593, 370), 5, 5)
                pygame.draw.circle(screen, lightGrey, (637, 370), 5, 5)
                pygame.draw.circle(screen, lightGrey, (679, 370), 5, 5)

                pygame.draw.circle(screen, lightGrey, (1113, 440), 5, 5)
                pygame.draw.circle(screen, lightGrey, (1049, 330), 5, 5)
                pygame.draw.circle(screen, lightGrey, (1093, 330), 5, 5)
                pygame.draw.circle(screen, lightGrey, (1137, 330), 5, 5)
                pygame.draw.circle(screen, lightGrey, (1179, 330), 5, 5)
                pygame.draw.circle(screen, lightGrey, (1049, 370), 5, 5)
                pygame.draw.circle(screen, lightGrey, (1093, 370), 5, 5)
                pygame.draw.circle(screen, lightGrey, (1137, 370), 5, 5)
                pygame.draw.circle(screen, lightGrey, (1179, 370), 5, 5)

                pygame.draw.circle(screen, lightGrey, (866, 660), 5, 5)
                pygame.draw.circle(screen, lightGrey, (764, 608), 5, 5)
                pygame.draw.circle(screen, lightGrey, (964, 608), 5, 5)

                screen.blit(jumpPoint, (530, 420))
                screen.blit(jumpPointAvailable, (665, 420))
                screen.blit(jumpPoint, (781, 420))
                screen.blit(jumpPoint, (917, 420))
                screen.blit(jumpPointAvailable, (1030, 420))
                screen.blit(jumpPoint, (1165, 420))
                screen.blit(jumpPointAvailable, (749, 582))
                screen.blit(jumpPointAvailable, (851, 634))
                screen.blit(jumpPointAvailable, (949, 582))

                if fleetX == 10000 and fleetY == 15000:
                    screen.blit(fleet, (780, 433))
                    if 813 > mouse[0] > 795 and 344 > mouse[1] > 326:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 25000
                            targetfleetX = 10000
                            targetfleetY = 40000
                    elif 857 > mouse[0] > 839 and 344 > mouse[1] > 326:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 27000
                            targetfleetX = 20000
                            targetfleetY = 40000
                    elif 901 > mouse[0] > 883 and 344 > mouse[1] > 326:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 32000
                            targetfleetX = 30000
                            targetfleetY = 40000
                    elif 945 > mouse[0] > 927 and 344 > mouse[1] > 326:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 39000
                            targetfleetX = 40000
                            targetfleetY = 40000
                    elif 813 > mouse[0] > 795 and 384 > mouse[1] > 366:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 15000
                            targetfleetX = 10000
                            targetfleetY = 30000
                    elif 857 > mouse[0] > 839 and 384 > mouse[1] > 366:
                        if click[0] == 1 and jumpTimer == 0 :
                            distanceToTargetLocation = 18000
                            targetfleetX = 20000
                            targetfleetY = 30000
                    elif 901 > mouse[0] > 883 and 384 > mouse[1] > 366:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 25000
                            targetfleetX = 30000
                            targetfleetY = 30000
                    elif 945 > mouse[0] > 927 and 384 > mouse[1] > 366:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 33000
                            targetfleetX = 40000
                            targetfleetY = 30000
                    elif 876 > mouse[0] > 858 and 454 > mouse[1] > 436:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 15000
                            targetfleetX = 25000
                            targetfleetY = 15000

                elif fleetX == 40000 and fleetY == 15000:
                    screen.blit(fleet, (916, 433))
                    if 813 > mouse[0] > 795 and 344 > mouse[1] > 326:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 39000
                            targetfleetX = 10000
                            targetfleetY = 40000
                    elif 857 > mouse[0] > 839 and 344 > mouse[1] > 326:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 20000
                            targetfleetX = 20000
                            targetfleetY = 40000
                    elif 901 > mouse[0] > 883 and 344 > mouse[1] > 326:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 27000
                            targetfleetX = 30000
                            targetfleetY = 40000
                    elif 945 > mouse[0] > 927 and 344 > mouse[1] > 326:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 25000
                            targetfleetX = 40000
                            targetfleetY = 40000
                    elif 813 > mouse[0] > 795 and 384 > mouse[1] > 366:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 33000
                            targetfleetX = 10000
                            targetfleetY = 30000
                    elif 857 > mouse[0] > 839 and 384 > mouse[1] > 366:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 25000
                            targetfleetX = 20000
                            targetfleetY = 30000
                    elif 901 > mouse[0] > 883 and 384 > mouse[1] > 366:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 18000
                            targetfleetX = 30000
                            targetfleetY = 30000
                    elif 945 > mouse[0] > 927 and 384 > mouse[1] > 366:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 15000
                            targetfleetX = 40000
                            targetfleetY = 30000
                    elif 876 > mouse[0] > 858 and 454 > mouse[1] > 436:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 15000
                            targetfleetX = 25000
                            targetfleetY = 15000


                elif fleetX == 25000 and fleetY == 15000:
                    pygame.draw.circle(screen, lightGrey, (866, 440), 5, 5)
                    pygame.draw.circle(screen, white, (799, 330), 5, 5)
                    pygame.draw.circle(screen, white, (843, 330), 5, 5)
                    pygame.draw.circle(screen, white, (887, 330), 5, 5)
                    pygame.draw.circle(screen, white, (929, 330), 5, 5)
                    pygame.draw.circle(screen, white, (799, 370), 5, 5)
                    pygame.draw.circle(screen, white, (843, 370), 5, 5)
                    pygame.draw.circle(screen, white, (887, 370), 5, 5)
                    pygame.draw.circle(screen, white, (929, 370), 5, 5)
                    screen.blit(fleet, (850, 438))
                    if 813 > mouse[0] > 795 and 344 > mouse[1] > 326:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 29000
                            targetfleetX = 10000
                            targetfleetY = 40000
                    elif 857 > mouse[0] > 839 and 344 > mouse[1] > 326:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 25000
                            targetfleetX = 20000
                            targetfleetY = 40000
                    elif 901 > mouse[0] > 883 and 344 > mouse[1] > 326:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 25000
                            targetfleetX = 30000
                            targetfleetY = 40000
                    elif 945 > mouse[0] > 927 and 344 > mouse[1] > 326:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 29000
                            targetfleetX = 40000
                            targetfleetY = 40000
                    elif 813 > mouse[0] > 795 and 384 > mouse[1] > 366:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 21000
                            targetfleetX = 10000
                            targetfleetY = 30000
                    elif 857 > mouse[0] > 839 and 384 > mouse[1] > 366:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 16000
                            targetfleetX = 20000
                            targetfleetY = 30000
                    elif 901 > mouse[0] > 883 and 384 > mouse[1] > 366:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 16000
                            targetfleetX = 30000
                            targetfleetY = 30000
                    elif 945 > mouse[0] > 927 and 384 > mouse[1] > 366:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 21000
                            targetfleetX = 40000
                            targetfleetY = 30000


                elif fleetX == 10000 and fleetY == 40000:
                    pygame.draw.circle(screen, white, (866, 440), 5, 5)
                    pygame.draw.circle(screen, lightGrey, (799, 330), 5, 5)
                    pygame.draw.circle(screen, white, (843, 330), 5, 5)
                    pygame.draw.circle(screen, white, (887, 330), 5, 5)
                    pygame.draw.circle(screen, white, (929, 330), 5, 5)
                    pygame.draw.circle(screen, white, (799, 370), 5, 5)
                    pygame.draw.circle(screen, white, (843, 370), 5, 5)
                    pygame.draw.circle(screen, white, (887, 370), 5, 5)
                    pygame.draw.circle(screen, white, (929, 370), 5, 5)
                    screen.blit(fleet, (783, 328))
                    if 857 > mouse[0] > 839 > mouse[1] > 326:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 10000
                            targetfleetX = 20000
                            targetfleetY = 40000
                    elif 901 > mouse[0] > 883 and 344 > mouse[1] > 326:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 20000
                            targetfleetX = 30000
                            targetfleetY = 40000
                    elif 945 > mouse[0] > 927 and 344 > mouse[1] > 326:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 30000
                            targetfleetX = 40000
                            targetfleetY = 40000
                    elif 813 > mouse[0] > 795 and 384 > mouse[1] > 366:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 10000
                            targetfleetX = 10000
                            targetfleetY = 30000
                    elif 857 > mouse[0] > 839 and 384 > mouse[1] > 366:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 14000
                            targetfleetX = 20000
                            targetfleetY = 30000
                    elif 901 > mouse[0] > 883 and 384 > mouse[1] > 366:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 22000
                            targetfleetX = 30000
                            targetfleetY = 30000
                    elif 945 > mouse[0] > 927 and 384 > mouse[1] > 366:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 32000
                            targetfleetX = 40000
                            targetfleetY = 30000
                    elif 876 > mouse[0] > 858 and 454 > mouse[1] > 436:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 29000
                            targetfleetX = 25000
                            targetfleetY = 15000

                elif fleetX == 20000 and fleetY == 40000:
                    pygame.draw.circle(screen, white, (866, 440), 5, 5)
                    pygame.draw.circle(screen, white, (799, 330), 5, 5)
                    pygame.draw.circle(screen, lightGrey, (843, 330), 5, 5)
                    pygame.draw.circle(screen, white, (887, 330), 5, 5)
                    pygame.draw.circle(screen, white, (929, 330), 5, 5)
                    pygame.draw.circle(screen, white, (799, 370), 5, 5)
                    pygame.draw.circle(screen, white, (843, 370), 5, 5)
                    pygame.draw.circle(screen, white, (887, 370), 5, 5)
                    pygame.draw.circle(screen, white, (929, 370), 5, 5)
                    screen.blit(fleet, (827, 328))
                    if 813 > mouse[0] > 795 and 344 > mouse[1] > 326:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 10000
                            targetfleetX = 10000
                            targetfleetY = 40000
                    elif  901 > mouse[0] > 883 and 344 > mouse[1] > 326:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 10000
                            targetfleetX = 30000
                            targetfleetY = 40000
                    elif 945 > mouse[0] > 927 and 344 > mouse[1] > 326:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 20000
                            targetfleetX = 40000
                            targetfleetY = 40000
                    elif 813 > mouse[0] > 795 and 384 > mouse[1] > 366:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 14000
                            targetfleetX = 10000
                            targetfleetY = 30000
                    elif 857 > mouse[0] > 839 and 384 > mouse[1] > 366:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 10000
                            targetfleetX = 20000
                            targetfleetY = 30000
                    elif 901 > mouse[0] > 883 and 384 > mouse[1] > 366:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 14000
                            targetfleetX = 30000
                            targetfleetY = 30000
                    elif 945 > mouse[0] > 927 and 384 > mouse[1] > 366:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 25000
                            targetfleetX = 40000
                            targetfleetY = 30000
                    elif 876 > mouse[0] > 858 and 454 > mouse[1] > 436:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 29000
                            targetfleetX = 25000
                            targetfleetY = 15000

                elif fleetX == 30000 and fleetY == 40000:
                    pygame.draw.circle(screen, white, (866, 440), 5, 5)
                    pygame.draw.circle(screen, white, (799, 330), 5, 5)
                    pygame.draw.circle(screen, white, (843, 330), 5, 5)
                    pygame.draw.circle(screen, lightGrey, (887, 330), 5, 5)
                    pygame.draw.circle(screen, white, (929, 330), 5, 5)
                    pygame.draw.circle(screen, white, (799, 370), 5, 5)
                    pygame.draw.circle(screen, white, (843, 370), 5, 5)
                    pygame.draw.circle(screen, white, (887, 370), 5, 5)
                    pygame.draw.circle(screen, white, (929, 370), 5, 5)
                    screen.blit(fleet, (871, 328))
                    if 813 > mouse[0] > 795 and 344 > mouse[1] > 326:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 20000
                            targetfleetX = 10000
                            targetfleetY = 40000
                    elif 857 > mouse[0] > 839 and 344 > mouse[1] > 326:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 10000
                            targetfleetX = 20000
                            targetfleetY = 40000
                    elif 945 > mouse[0] > 927 and 344 > mouse[1] > 326:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 10000
                            targetfleetX = 40000
                            targetfleetY = 40000
                    elif 813 > mouse[0] > 795 and 384 > mouse[1] > 366:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 22000
                            targetfleetX = 10000
                            targetfleetY = 30000
                    elif 857 > mouse[0] > 839 and 384 > mouse[1] > 366:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 14000
                            targetfleetX = 20000
                            targetfleetY = 30000
                    elif 901 > mouse[0] > 883 and 384 > mouse[1] > 366:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 10000
                            targetfleetX = 30000
                            targetfleetY = 30000
                    elif 945 > mouse[0] > 927 and 384 > mouse[1] > 366:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 50000
                            targetfleetX = 40000
                            targetfleetY = 30000
                    elif 876 > mouse[0] > 858 and 454 > mouse[1] > 436:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 29000
                            targetfleetX = 25000
                            targetfleetY = 15000

                elif fleetX == 40000 and fleetY == 40000:
                    pygame.draw.circle(screen, white, (866, 440), 5, 5)
                    pygame.draw.circle(screen, white, (799, 330), 5, 5)
                    pygame.draw.circle(screen, white, (843, 330), 5, 5)
                    pygame.draw.circle(screen, white, (887, 330), 5, 5)
                    pygame.draw.circle(screen, lightGrey, (929, 330), 5, 5)
                    pygame.draw.circle(screen, white, (799, 370), 5, 5)
                    pygame.draw.circle(screen, white, (843, 370), 5, 5)
                    pygame.draw.circle(screen, white, (887, 370), 5, 5)
                    pygame.draw.circle(screen, white, (929, 370), 5, 5)
                    screen.blit(fleet, (914, 328))
                    if 813 > mouse[0] > 795 and 344 > mouse[1] > 326:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 30000
                            targetfleetX = 10000
                            targetfleetY = 40000
                    elif 857 > mouse[0] > 839 and 344 > mouse[1] > 326:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 20000
                            targetfleetX = 20000
                            targetfleetY = 40000
                    elif 901 > mouse[0] > 883 and 344 > mouse[1] > 326:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 10000
                            targetfleetX = 30000
                            targetfleetY = 40000
                    elif 813 > mouse[0] > 795 and 384 > mouse[1] > 366:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 32000
                            targetfleetX = 10000
                            targetfleetY = 30000
                    elif 857 > mouse[0] > 839 and 384 > mouse[1] > 366:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 22000
                            targetfleetX = 20000
                            targetfleetY = 30000
                    elif 901 > mouse[0] > 883 and 384 > mouse[1] > 366:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 14000
                            targetfleetX = 30000
                            targetfleetY = 30000
                    elif 945 > mouse[0] > 927 and 384 > mouse[1] > 366:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 10000
                            targetfleetX = 40000
                            targetfleetY = 30000
                    elif 876 > mouse[0] > 858 and 454 > mouse[1] > 436:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 29000
                            targetfleetX = 25000
                            targetfleetY = 15000

                elif fleetX == 10000 and fleetY == 30000:
                    pygame.draw.circle(screen, white, (866, 440), 5, 5)
                    pygame.draw.circle(screen, white, (799, 330), 5, 5)
                    pygame.draw.circle(screen, white, (843, 330), 5, 5)
                    pygame.draw.circle(screen, white, (887, 330), 5, 5)
                    pygame.draw.circle(screen, white, (929, 330), 5, 5)
                    pygame.draw.circle(screen, lightGrey, (799, 370), 5, 5)
                    pygame.draw.circle(screen, white, (843, 370), 5, 5)
                    pygame.draw.circle(screen, white, (887, 370), 5, 5)
                    pygame.draw.circle(screen, white, (929, 370), 5, 5)
                    screen.blit(fleet, (783, 367))
                    if 813 > mouse[0] > 795 > mouse[1] > 326:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 10000
                            targetfleetX = 10000
                            targetfleetY = 40000
                    elif 857 > mouse[0] > 839 and 344 > mouse[1] > 326:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 14000
                            targetfleetX = 20000
                            targetfleetY = 40000
                    elif 901 > mouse[0] > 883 and 344 > mouse[1] > 326:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 22000
                            targetfleetX = 30000
                            targetfleetY = 40000
                    elif 945 > mouse[0] > 927 and 344 > mouse[1] > 326:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 32000
                            targetfleetX = 40000
                            targetfleetY = 40000
                    elif 857 > mouse[0] > 839 and 384 > mouse[1] > 366:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 10000
                            targetfleetX = 20000
                            targetfleetY = 30000
                    elif 901 > mouse[0] > 883 and 384 > mouse[1] > 366:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 20000
                            targetfleetX = 30000
                            targetfleetY = 30000
                    elif 945 > mouse[0] > 927 and 384 > mouse[1] > 366:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 30000
                            targetfleetX = 40000
                            targetfleetY = 30000
                    elif 876 > mouse[0] > 858 and 454 > mouse[1] > 436:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 21000
                            targetfleetX = 25000
                            targetfleetY = 15000



                elif fleetX == 20000 and fleetY == 30000:
                    pygame.draw.circle(screen, white, (866, 440), 5, 5)
                    pygame.draw.circle(screen, white, (799, 330), 5, 5)
                    pygame.draw.circle(screen, white, (843, 330), 5, 5)
                    pygame.draw.circle(screen, white, (887, 330), 5, 5)
                    pygame.draw.circle(screen, white, (929, 330), 5, 5)
                    pygame.draw.circle(screen, white, (799, 370), 5, 5)
                    pygame.draw.circle(screen, lightGrey, (843, 370), 5, 5)
                    pygame.draw.circle(screen, white, (887, 370), 5, 5)
                    pygame.draw.circle(screen, white, (929, 370), 5, 5)
                    screen.blit(fleet, (827, 367))
                    if 813 > mouse[0] > 795 and 344 > mouse[1] > 326:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 14000
                            targetfleetX = 10000
                            targetfleetY = 40000
                    elif 857 > mouse[0] > 839 and 344 > mouse[1] > 326:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 10000
                            targetfleetX = 20000
                            targetfleetY = 40000
                    elif 901 > mouse[0] > 883 and 344 > mouse[1] > 326:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 14000
                            targetfleetX = 30000
                            targetfleetY = 40000
                    elif 945 > mouse[0] > 927 and 344 > mouse[1] > 326:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 229000
                            targetfleetX = 40000
                            targetfleetY = 40000
                    elif 813 > mouse[0] > 795 and 384 > mouse[1] > 366:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 10000
                            targetfleetX = 10000
                            targetfleetY = 30000
                    elif 901 > mouse[0] > 883 and 384 > mouse[1] > 366:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 10000
                            targetfleetX = 30000
                            targetfleetY = 30000
                    elif 945 > mouse[0] > 927 and 384 > mouse[1] > 366:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 20000
                            targetfleetX = 40000
                            targetfleetY = 30000
                    elif 876 > mouse[0] > 858 and 454 > mouse[1] > 436:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 16000
                            targetfleetX = 25000
                            targetfleetY = 15000

                elif fleetX == 30000 and fleetY == 30000:
                    pygame.draw.circle(screen, white, (866, 440), 5, 5)
                    pygame.draw.circle(screen, white, (799, 330), 5, 5)
                    pygame.draw.circle(screen, white, (843, 330), 5, 5)
                    pygame.draw.circle(screen, white, (887, 330), 5, 5)
                    pygame.draw.circle(screen, white, (929, 330), 5, 5)
                    pygame.draw.circle(screen, white, (799, 370), 5, 5)
                    pygame.draw.circle(screen, white, (843, 370), 5, 5)
                    pygame.draw.circle(screen, lightGrey, (887, 370), 5, 5)
                    pygame.draw.circle(screen, white, (929, 370), 5, 5)
                    screen.blit(fleet, (871, 367))
                    if 813 > mouse[0] > 795 and 344 > mouse[1] > 326:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 22000
                            targetfleetX = 10000
                            targetfleetY = 40000
                    elif 857 > mouse[0] > 839 and 344 > mouse[1] > 326:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 14000
                            targetfleetX = 20000
                            targetfleetY = 40000
                    elif 901 > mouse[0] > 883 and 344 > mouse[1] > 326:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 10000
                            targetfleetX = 30000
                            targetfleetY = 40000
                    elif 945 > mouse[0] > 927 and 344 > mouse[1] > 326:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 14000
                            targetfleetX = 40000
                            targetfleetY = 40000
                    elif 813 > mouse[0] > 795 and 384 > mouse[1] > 366:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 20000
                            targetfleetX = 10000
                            targetfleetY = 30000
                    elif 857 > mouse[0] > 839 and 384 > mouse[1] > 366:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 10000
                            targetfleetX = 20000
                            targetfleetY = 30000
                    elif 945 > mouse[0] > 927 and 384 > mouse[1] > 366:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 10000
                            targetfleetX = 40000
                            targetfleetY = 30000
                    elif 876 > mouse[0] > 858 and 454 > mouse[1] > 436:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 16000
                            targetfleetX = 25000
                            targetfleetY = 15000

                elif fleetX == 40000 and fleetY == 30000:
                    pygame.draw.circle(screen, white, (866, 440), 5, 5)
                    pygame.draw.circle(screen, white, (799, 330), 5, 5)
                    pygame.draw.circle(screen, white, (843, 330), 5, 5)
                    pygame.draw.circle(screen, white, (887, 330), 5, 5)
                    pygame.draw.circle(screen, white, (929, 330), 5, 5)
                    pygame.draw.circle(screen, white, (799, 370), 5, 5)
                    pygame.draw.circle(screen, white, (843, 370), 5, 5)
                    pygame.draw.circle(screen, white, (887, 370), 5, 5)
                    pygame.draw.circle(screen, lightGrey, (929, 370), 5, 5)
                    screen.blit(fleet, (913, 367))
                    if 813 > mouse[0] > 795 and 344 > mouse[1] > 326:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 32000
                            targetfleetX = 10000
                            targetfleetY = 40000
                    elif 857 > mouse[0] > 839 and 344 > mouse[1] > 326:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 22000
                            targetfleetX = 20000
                            targetfleetY = 40000
                    elif 901 > mouse[0] > 883 and 344 > mouse[1] > 326:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 14000
                            targetfleetX = 30000
                            targetfleetY = 40000
                    elif 945 > mouse[0] > 927 and 344 > mouse[1] > 326:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 10000
                            targetfleetX = 40000
                            targetfleetY = 40000
                    elif 813 > mouse[0] > 795 and 384 > mouse[1] > 366:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 30000
                            targetfleetX = 10000
                            targetfleetY = 30000
                    elif 857 > mouse[0] > 839 and 384 > mouse[1] > 366:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 20000
                            targetfleetX = 20000
                            targetfleetY = 30000
                    elif 901 > mouse[0] > 883 and 384 > mouse[1] > 366:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 10000
                            targetfleetX = 30000
                            targetfleetY = 30000
                    elif 876 > mouse[0] > 858 and 454 > mouse[1] > 436:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 21000
                            targetfleetX = 25000
                            targetfleetY = 15000

                if 696 > mouse[0] > 665 and 445 > mouse[1] > 420:
                    screen.blit(jumpPointHoverOver, (661, 413))
                    if click[0] == 1 and jumpTimer == 0:
                        jumpTimer = 25
                        targetfleetX = 40000
                        targetfleetY = 10000
                        targetSector = 'alpha'
                elif 780 > mouse[0] > 749 and 607 > mouse[1] > 582:
                    screen.blit(jumpPointHoverOver, (745, 575))
                    if click[0] == 1 and jumpTimer == 0:
                        jumpTimer = 25
                        targetfleetX = 10000
                        targetfleetY = 40000
                        targetSector = 'outpost'
                elif 882 > mouse[0] > 851 and 665 > mouse[1] > 634:
                    screen.blit(jumpPointHoverOver, (847, 627))
                    if click[0] == 1 and jumpTimer == 0:
                        jumpTimer = 25
                        targetfleetX = 35000
                        targetfleetY = 20000
                        targetSector = 'outpost'
                elif 980 > mouse[0] > 949 and 607 > mouse[1] > 582:
                    screen.blit(jumpPointHoverOver, (945, 575))
                    if click[0] == 1 and jumpTimer == 0:
                        jumpTimer = 25
                        targetfleetX = 60000
                        targetfleetY = 40000
                        targetSector = 'outpost'
                elif 1061 > mouse[0] > 1030 and 445 > mouse[1] > 420:
                    screen.blit(jumpPointHoverOver, (1026, 413))
                    if click[0] == 1 and jumpTimer == 0:
                        jumpTimer = 25
                        targetfleetX = 10000
                        targetfleetY = 15000
                        targetSector = 'beta'

            elif fleetSector == 'beta':
                if fleetX == 10000 and fleetY == 15000 or fleetX == 40000 and fleetY == 15000:
                    pygame.draw.circle(screen, white, (1113, 440), 5, 5)
                    pygame.draw.circle(screen, white, (1049, 330), 5, 5)
                    pygame.draw.circle(screen, white, (1093, 330), 5, 5)
                    pygame.draw.circle(screen, white, (1137, 330), 5, 5)
                    pygame.draw.circle(screen, white, (1179, 330), 5, 5)
                    pygame.draw.circle(screen, white, (1049, 370), 5, 5)
                    pygame.draw.circle(screen, white, (1093, 370), 5, 5)
                    pygame.draw.circle(screen, white, (1137, 370), 5, 5)
                    pygame.draw.circle(screen, white, (1179, 370), 5, 5)

                pygame.draw.circle(screen, lightGrey, (612, 440), 5, 5)
                pygame.draw.circle(screen, lightGrey, (549, 330), 5, 5)
                pygame.draw.circle(screen, lightGrey, (593, 330), 5, 5)
                pygame.draw.circle(screen, lightGrey, (637, 330), 5, 5)
                pygame.draw.circle(screen, lightGrey, (679, 330), 5, 5)
                pygame.draw.circle(screen, lightGrey, (549, 370), 5, 5)
                pygame.draw.circle(screen, lightGrey, (593, 370), 5, 5)
                pygame.draw.circle(screen, lightGrey, (637, 370), 5, 5)
                pygame.draw.circle(screen, lightGrey, (679, 370), 5, 5)

                pygame.draw.circle(screen, lightGrey, (866, 440), 5, 5)
                pygame.draw.circle(screen, lightGrey, (799, 330), 5, 5)
                pygame.draw.circle(screen, lightGrey, (843, 330), 5, 5)
                pygame.draw.circle(screen, lightGrey, (887, 330), 5, 5)
                pygame.draw.circle(screen, lightGrey, (929, 330), 5, 5)
                pygame.draw.circle(screen, lightGrey, (799, 370), 5, 5)
                pygame.draw.circle(screen, lightGrey, (843, 370), 5, 5)
                pygame.draw.circle(screen, lightGrey, (887, 370), 5, 5)
                pygame.draw.circle(screen, lightGrey, (929, 370), 5, 5)

                pygame.draw.circle(screen, lightGrey, (866, 660), 5, 5)
                pygame.draw.circle(screen, lightGrey, (764, 608), 5, 5)
                pygame.draw.circle(screen, lightGrey, (964, 608), 5, 5)

                screen.blit(jumpPoint, (530, 420))
                screen.blit(jumpPoint, (665, 420))
                screen.blit(jumpPoint, (781, 420))
                screen.blit(jumpPointAvailable, (917, 420))
                screen.blit(jumpPoint, (1030, 420))
                screen.blit(jumpPoint, (1165, 420))
                screen.blit(jumpPoint, (749, 582))
                screen.blit(jumpPointAvailable, (851, 634))
                screen.blit(jumpPointAvailable, (949, 582))

                if fleetX == 10000 and fleetY == 15000:
                    screen.blit(fleet, (1029, 433))
                    if 1063 > mouse[0] > 1045 and 344 > mouse[1] > 326:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 25000
                            targetfleetX = 10000
                            targetfleetY = 40000
                    elif 1107 > mouse[0] > 1089 and 344 > mouse[1] > 326:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 27000
                            targetfleetX = 20000
                            targetfleetY = 40000
                    elif 1151 > mouse[0] > 1133 and 344 > mouse[1] > 326:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 32000
                            targetfleetX = 30000
                            targetfleetY = 40000
                    elif 1195 > mouse[0] > 1177 and 344 > mouse[1] > 326:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 39000
                            targetfleetX = 40000
                            targetfleetY = 40000
                    elif 1063 > mouse[0] > 1045 and 384 > mouse[1] > 366:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 15000
                            targetfleetX = 10000
                            targetfleetY = 30000
                    elif 1107 > mouse[0] > 1089 and 384 > mouse[1] > 366:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 18000
                            targetfleetX = 20000
                            targetfleetY = 30000
                    elif 1151 > mouse[0] > 1133 and 384 > mouse[1] > 366:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 25000
                            targetfleetX = 30000
                            targetfleetY = 30000
                    elif 1195 > mouse[0] > 1177 and 384 > mouse[1] > 366:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 33000
                            targetfleetX = 40000
                            targetfleetY = 30000
                    elif 1126 > mouse[0] > 1108 and 454 > mouse[1] > 436:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 15000
                            targetfleetX = 25000
                            targetfleetY = 15000

                elif fleetX == 40000 and fleetY == 15000:
                    screen.blit(fleet, (1164, 433))
                    if 1063 > mouse[0] > 1045 and 344 > mouse[1] > 326:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 39000
                            targetfleetX = 10000
                            targetfleetY = 40000
                    elif 1107 > mouse[0] > 1089 and 344 > mouse[1] > 326:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 32000
                            targetfleetX = 20000
                            targetfleetY = 40000
                    elif 1151 > mouse[0] > 1133 and 344 > mouse[1] > 326:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 27000
                            targetfleetX = 30000
                            targetfleetY = 40000
                    elif 1195 > mouse[0] > 1177 and 344 > mouse[1] > 326:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 25000
                            targetfleetX = 40000
                            targetfleetY = 40000
                    elif 1063 > mouse[0] > 1045 and 384 > mouse[1] > 366:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 34000
                            targetfleetX = 10000
                            targetfleetY = 30000
                    elif 1107 > mouse[0] > 1089 and 384 > mouse[1] > 366:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 25000
                            targetfleetX = 20000
                            targetfleetY = 30000
                    elif 1151 > mouse[0] > 1133 and 384 > mouse[1] > 366:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 18000
                            targetfleetX = 30000
                            targetfleetY = 30000
                    elif 1195 > mouse[0] > 1177 and 384 > mouse[1] > 366:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 15000
                            targetfleetX = 40000
                            targetfleetY = 30000
                    elif 1126 > mouse[0] > 1108 and 454 > mouse[1] > 436:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 15000
                            targetfleetX = 25000
                            targetfleetY = 15000


                elif fleetX == 25000 and fleetY == 15000:
                    pygame.draw.circle(screen, lightGrey, (1113, 440), 5, 5)
                    pygame.draw.circle(screen, white, (1049, 330), 5, 5)
                    pygame.draw.circle(screen, white, (1093, 330), 5, 5)
                    pygame.draw.circle(screen, white, (1137, 330), 5, 5)
                    pygame.draw.circle(screen, white, (1179, 330), 5, 5)
                    pygame.draw.circle(screen, white, (1049, 370), 5, 5)
                    pygame.draw.circle(screen, white, (1093, 370), 5, 5)
                    pygame.draw.circle(screen, white, (1137, 370), 5, 5)
                    pygame.draw.circle(screen, white, (1179, 370), 5, 5)
                    screen.blit(fleet, (1097, 438))
                    if 1063 > mouse[0] > 1045 and 344 > mouse[1] > 326:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 25000
                            targetfleetX = 10000
                            targetfleetY = 40000
                    elif 1107 > mouse[0] > 1089 and 344 > mouse[1] > 326:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 27000
                            targetfleetX = 20000
                            targetfleetY = 40000
                    elif 1151 > mouse[0] > 1133 and 344 > mouse[1] > 326:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 32000
                            targetfleetX = 30000
                            targetfleetY = 40000
                    elif 1195 > mouse[0] > 1177 and 344 > mouse[1] > 326:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 39000
                            targetfleetX = 40000
                            targetfleetY = 40000
                    elif 1063 > mouse[0] > 1045 and 384 > mouse[1] > 366:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 15000
                            targetfleetX = 10000
                            targetfleetY = 30000
                    elif 1107 > mouse[0] > 1089 and 384 > mouse[1] > 366:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 18000
                            targetfleetX = 20000
                            targetfleetY = 30000
                    elif 1151 > mouse[0] > 1133 and 384 > mouse[1] > 366:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 25000
                            targetfleetX = 30000
                            targetfleetY = 30000
                    elif 1195 > mouse[0] > 1177 and 384 > mouse[1] > 366:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 29000
                            targetfleetX = 40000
                            targetfleetY = 30000

                elif fleetX == 10000 and fleetY == 40000:
                    pygame.draw.circle(screen, white, (1113, 440), 5, 5)
                    pygame.draw.circle(screen, lightGrey, (1049, 330), 5, 5)
                    pygame.draw.circle(screen, white, (1093, 330), 5, 5)
                    pygame.draw.circle(screen, white, (1137, 330), 5, 5)
                    pygame.draw.circle(screen, white, (1179, 330), 5, 5)
                    pygame.draw.circle(screen, white, (1049, 370), 5, 5)
                    pygame.draw.circle(screen, white, (1093, 370), 5, 5)
                    pygame.draw.circle(screen, white, (1137, 370), 5, 5)
                    pygame.draw.circle(screen, white, (1179, 370), 5, 5)
                    screen.blit(fleet, (1033, 328))
                    if 1107 > mouse[0] > 1089 and 344 > mouse[1] > 326:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 10000
                            targetfleetX = 20000
                            targetfleetY = 40000
                    elif 1151 > mouse[0] > 1133 and 344 > mouse[1] > 326:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 20000
                            targetfleetX = 30000
                            targetfleetY = 40000
                    elif 1195 > mouse[0] > 1177 and 344 > mouse[1] > 326:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 30000
                            targetfleetX = 40000
                            targetfleetY = 40000
                    elif 1063 > mouse[0] > 1045 and 384 > mouse[1] > 366:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 10000
                            targetfleetX = 10000
                            targetfleetY = 30000
                    elif 1107 > mouse[0] > 1089 and 384 > mouse[1] > 366:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 14000
                            targetfleetX = 20000
                            targetfleetY = 30000
                    elif 1151 > mouse[0] > 1133 and 384 > mouse[1] > 366:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 22000
                            targetfleetX = 30000
                            targetfleetY = 30000
                    elif 1195 > mouse[0] > 1177 and 384 > mouse[1] > 366:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 32000
                            targetfleetX = 40000
                            targetfleetY = 30000
                    elif 1126 > mouse[0] > 1108 and 454 > mouse[1] > 436:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 29000
                            targetfleetX = 25000
                            targetfleetY = 15000

                elif fleetX == 20000 and fleetY == 40000:
                    pygame.draw.circle(screen, white, (1113, 440), 5, 5)
                    pygame.draw.circle(screen, white, (1049, 330), 5, 5)
                    pygame.draw.circle(screen, lightGrey, (1093, 330), 5, 5)
                    pygame.draw.circle(screen, white, (1137, 330), 5, 5)
                    pygame.draw.circle(screen, white, (1179, 330), 5, 5)
                    pygame.draw.circle(screen, white, (1049, 370), 5, 5)
                    pygame.draw.circle(screen, white, (1093, 370), 5, 5)
                    pygame.draw.circle(screen, white, (1137, 370), 5, 5)
                    pygame.draw.circle(screen, white, (1179, 370), 5, 5)
                    screen.blit(fleet, (1077, 328))
                    if 1063 > mouse[0] > 1045 and 344 > mouse[1] > 326:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 1000
                            targetfleetX = 10000
                            targetfleetY = 40000
                    elif 1151 > mouse[0] > 1133 and 344 > mouse[1] > 326:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 10000
                            targetfleetX = 30000
                            targetfleetY = 40000
                    elif 1195 > mouse[0] > 1177 and 344 > mouse[1] > 326:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 20000
                            targetfleetX = 40000
                            targetfleetY = 40000
                    elif 1063 > mouse[0] > 1045 and 384 > mouse[1] > 366:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 14000
                            targetfleetX = 10000
                            targetfleetY = 30000
                    elif 1107 > mouse[0] > 1089 and 384 > mouse[1] > 366:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 10000
                            targetfleetX = 20000
                            targetfleetY = 30000
                    elif 1151 > mouse[0] > 1133 and 384 > mouse[1] > 366:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 14000
                            targetfleetX = 30000
                            targetfleetY = 30000
                    elif 1195 > mouse[0] > 1177 and 384 > mouse[1] > 366:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 22000
                            targetfleetX = 40000
                            targetfleetY = 30000
                    elif 1126 > mouse[0] > 1108 and 454 > mouse[1] > 436:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 25000
                            targetfleetX = 25000
                            targetfleetY = 15000

                elif fleetX == 30000 and fleetY == 40000:
                    pygame.draw.circle(screen, white, (1113, 440), 5, 5)
                    pygame.draw.circle(screen, white, (1049, 330), 5, 5)
                    pygame.draw.circle(screen, white, (1093, 330), 5, 5)
                    pygame.draw.circle(screen, lightGrey, (1137, 330), 5, 5)
                    pygame.draw.circle(screen, white, (1179, 330), 5, 5)
                    pygame.draw.circle(screen, white, (1049, 370), 5, 5)
                    pygame.draw.circle(screen, white, (1093, 370), 5, 5)
                    pygame.draw.circle(screen, white, (1137, 370), 5, 5)
                    pygame.draw.circle(screen, white, (1179, 370), 5, 5)
                    screen.blit(fleet, (1121, 328))
                    if 1063 > mouse[0] > 1045 and 344 > mouse[1] > 326:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 20000
                            targetfleetX = 10000
                            targetfleetY = 40000
                    elif 1107 > mouse[0] > 1089 and 344 > mouse[1] > 326:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 10000
                            targetfleetX = 20000
                            targetfleetY = 40000
                    elif 1195 > mouse[0] > 1177 and 344 > mouse[1] > 326:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 10000
                            targetfleetX = 40000
                            targetfleetY = 40000
                    elif 1063 > mouse[0] > 1045 and 384 > mouse[1] > 366:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 22000
                            targetfleetX = 10000
                            targetfleetY = 30000
                    elif 1107 > mouse[0] > 1089 and 384 > mouse[1] > 366:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 14000
                            targetfleetX = 20000
                            targetfleetY = 30000
                    elif 1151 > mouse[0] > 1133 and 384 > mouse[1] > 366:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 10000
                            targetfleetX = 30000
                            targetfleetY = 30000
                    elif 1195 > mouse[0] > 1177 and 384 > mouse[1] > 366:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 14000
                            targetfleetX = 40000
                            targetfleetY = 30000
                    elif 1126 > mouse[0] > 1108 and 454 > mouse[1] > 436:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 25000
                            targetfleetX = 25000
                            targetfleetY = 15000

                elif fleetX == 40000 and fleetY == 40000:
                    pygame.draw.circle(screen, white, (1113, 440), 5, 5)
                    pygame.draw.circle(screen, white, (1049, 330), 5, 5)
                    pygame.draw.circle(screen, white, (1093, 330), 5, 5)
                    pygame.draw.circle(screen, white, (1137, 330), 5, 5)
                    pygame.draw.circle(screen, lightGrey, (1179, 330), 5, 5)
                    pygame.draw.circle(screen, white, (1049, 370), 5, 5)
                    pygame.draw.circle(screen, white, (1093, 370), 5, 5)
                    pygame.draw.circle(screen, white, (1137, 370), 5, 5)
                    pygame.draw.circle(screen, white, (1179, 370), 5, 5)
                    screen.blit(fleet, (1163, 328))
                    if 1063 > mouse[0] > 1045 and 344 > mouse[1] > 326:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 30000
                            targetfleetX = 10000
                            targetfleetY = 40000
                    elif 1107 > mouse[0] > 1089 and 344 > mouse[1] > 326:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 20000
                            targetfleetX = 20000
                            targetfleetY = 40000
                    elif 1151 > mouse[0] > 1133 and 344 > mouse[1] > 326:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 10000
                            targetfleetX = 30000
                            targetfleetY = 40000
                    elif 1063 > mouse[0] > 1045 and 384 > mouse[1] > 366:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 32000
                            targetfleetX = 10000
                            targetfleetY = 30000
                    elif 1107 > mouse[0] > 1089 and 384 > mouse[1] > 366:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 22000
                            targetfleetX = 20000
                            targetfleetY = 30000
                    elif 1151 > mouse[0] > 1133 and 384 > mouse[1] > 366:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 14000
                            targetfleetX = 30000
                            targetfleetY = 30000
                    elif 1195 > mouse[0] > 1177 and 384 > mouse[1] > 366:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 10000
                            targetfleetX = 40000
                            targetfleetY = 30000
                    elif 1126 > mouse[0] > 1108 and 454 > mouse[1] > 436:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 29000
                            targetfleetX = 25000
                            targetfleetY = 15000

                elif fleetX == 10000 and fleetY == 30000:
                    pygame.draw.circle(screen, white, (1113, 440), 5, 5)
                    pygame.draw.circle(screen, white, (1049, 330), 5, 5)
                    pygame.draw.circle(screen, white, (1093, 330), 5, 5)
                    pygame.draw.circle(screen, white, (1137, 330), 5, 5)
                    pygame.draw.circle(screen, white, (1179, 330), 5, 5)
                    pygame.draw.circle(screen, lightGrey, (1049, 370), 5, 5)
                    pygame.draw.circle(screen, white, (1093, 370), 5, 5)
                    pygame.draw.circle(screen, white, (1137, 370), 5, 5)
                    pygame.draw.circle(screen, white, (1179, 370), 5, 5)
                    screen.blit(fleet, (1033, 367))
                    if 1063 > mouse[0] > 1045 and 344 > mouse[1] > 326:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 10000
                            targetfleetX = 10000
                            targetfleetY = 40000
                    elif 1107 > mouse[0] > 1089 and 344 > mouse[1] > 326:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 14000
                            targetfleetX = 20000
                            targetfleetY = 40000
                    elif 1151 > mouse[0] > 1133 and 344 > mouse[1] > 326:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 22000
                            targetfleetX = 30000
                            targetfleetY = 40000
                    elif 1195 > mouse[0] > 1177 and 344 > mouse[1] > 326:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 32000
                            targetfleetX = 40000
                            targetfleetY = 40000
                    elif 1107 > mouse[0] > 1089 and 384 > mouse[1] > 366:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 10000
                            targetfleetX = 20000
                            targetfleetY = 30000
                    elif 1151 > mouse[0] > 1133 and 384 > mouse[1] > 366:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 20000
                            targetfleetX = 30000
                            targetfleetY = 30000
                    elif 1195 > mouse[0] > 1177 and 384 > mouse[1] > 366:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 30000
                            targetfleetX = 40000
                            targetfleetY = 30000
                    elif 1126 > mouse[0] > 1108 and 454 > mouse[1] > 436:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 21000
                            targetfleetX = 25000
                            targetfleetY = 15000



                elif fleetX == 20000 and fleetY == 30000:
                    pygame.draw.circle(screen, white, (1113, 440), 5, 5)
                    pygame.draw.circle(screen, white, (1049, 330), 5, 5)
                    pygame.draw.circle(screen, white, (1093, 330), 5, 5)
                    pygame.draw.circle(screen, white, (1137, 330), 5, 5)
                    pygame.draw.circle(screen, white, (1179, 330), 5, 5)
                    pygame.draw.circle(screen, white, (1049, 370), 5, 5)
                    pygame.draw.circle(screen, lightGrey, (1093, 370), 5, 5)
                    pygame.draw.circle(screen, white, (1137, 370), 5, 5)
                    pygame.draw.circle(screen, white, (1179, 370), 5, 5)
                    screen.blit(fleet, (1077, 367))
                    if 1063 > mouse[0] > 1045 and 344 > mouse[1] > 326:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 14000
                            targetfleetX = 10000
                            targetfleetY = 40000
                    elif 1107 > mouse[0] > 1089 and 344 > mouse[1] > 326:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 10000
                            targetfleetX = 20000
                            targetfleetY = 40000
                    elif 1151 > mouse[0] > 1133 and 344 > mouse[1] > 326:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 14000
                            targetfleetX = 30000
                            targetfleetY = 40000
                    elif 1195 > mouse[0] > 1177 and 344 > mouse[1] > 326:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 22000
                            targetfleetX = 40000
                            targetfleetY = 40000
                    elif 1063 > mouse[0] > 1045 and 384 > mouse[1] > 366:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 10000
                            targetfleetX = 10000
                            targetfleetY = 30000
                    elif 1151 > mouse[0] > 1133 and 384 > mouse[1] > 366:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 10000
                            targetfleetX = 30000
                            targetfleetY = 30000
                    elif 1195 > mouse[0] > 1177 and 384 > mouse[1] > 366:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 22000
                            targetfleetX = 40000
                            targetfleetY = 30000
                    elif 1126 > mouse[0] > 1108 and 454 > mouse[1] > 436:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 16000
                            targetfleetX = 25000
                            targetfleetY = 15000

                elif fleetX == 30000 and fleetY == 30000:
                    pygame.draw.circle(screen, white, (1113, 440), 5, 5)
                    pygame.draw.circle(screen, white, (1049, 330), 5, 5)
                    pygame.draw.circle(screen, white, (1093, 330), 5, 5)
                    pygame.draw.circle(screen, white, (1137, 330), 5, 5)
                    pygame.draw.circle(screen, white, (1179, 330), 5, 5)
                    pygame.draw.circle(screen, white, (1049, 370), 5, 5)
                    pygame.draw.circle(screen, white, (1093, 370), 5, 5)
                    pygame.draw.circle(screen, lightGrey, (1137, 370), 5, 5)
                    pygame.draw.circle(screen, white, (1179, 370), 5, 5)
                    screen.blit(fleet, (1121, 367))
                    if 1063 > mouse[0] > 1045 and 344 > mouse[1] > 326:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 22000
                            targetfleetX = 10000
                            targetfleetY = 40000
                    elif 1107 > mouse[0] > 1089 and 344 > mouse[1] > 326:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 14000
                            targetfleetX = 20000
                            targetfleetY = 40000
                    elif 1151 > mouse[0] > 1133 and 344 > mouse[1] > 326:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 10000
                            targetfleetX = 30000
                            targetfleetY = 40000
                    elif 1195 > mouse[0] > 1177 and 344 > mouse[1] > 326:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 14000
                            targetfleetX = 40000
                            targetfleetY = 40000
                    elif 1063 > mouse[0] > 1045 and 384 > mouse[1] > 366:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 20000
                            targetfleetX = 10000
                            targetfleetY = 30000
                    elif 1107 > mouse[0] > 1089 and 384 > mouse[1] > 366:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 10000
                            targetfleetX = 20000
                            targetfleetY = 30000
                    elif 1195 > mouse[0] > 1177 and 384 > mouse[1] > 366:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 10000
                            targetfleetX = 40000
                            targetfleetY = 30000
                    elif 1126 > mouse[0] > 1108 and 454 > mouse[1] > 436:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 16000
                            targetfleetX = 25000
                            targetfleetY = 15000

                elif fleetX == 40000 and fleetY == 30000:
                    pygame.draw.circle(screen, white, (1113, 440), 5, 5)
                    pygame.draw.circle(screen, white, (1049, 330), 5, 5)
                    pygame.draw.circle(screen, white, (1093, 330), 5, 5)
                    pygame.draw.circle(screen, white, (1137, 330), 5, 5)
                    pygame.draw.circle(screen, white, (1179, 330), 5, 5)
                    pygame.draw.circle(screen, white, (1049, 370), 5, 5)
                    pygame.draw.circle(screen, white, (1093, 370), 5, 5)
                    pygame.draw.circle(screen, white, (1137, 370), 5, 5)
                    pygame.draw.circle(screen, lightGrey, (1179, 370), 5, 5)
                    screen.blit(fleet, (1163, 367))
                    if 1063 > mouse[0] > 1045 and 344 > mouse[1] > 326:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 32000
                            targetfleetX = 10000
                            targetfleetY = 40000
                    elif 1107 > mouse[0] > 1089 and 344 > mouse[1] > 326:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 22000
                            targetfleetX = 20000
                            targetfleetY = 40000
                    elif 1151 > mouse[0] > 1133 and 344 > mouse[1] > 326:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 14000
                            targetfleetX = 30000
                            targetfleetY = 40000
                    elif 1195 > mouse[0] > 1177 and 344 > mouse[1] > 326:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 10000
                            targetfleetX = 40000
                            targetfleetY = 40000
                    elif 1063 > mouse[0] > 1045 and 384 > mouse[1] > 366:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 30000
                            targetfleetX = 10000
                            targetfleetY = 30000
                    elif 1107 > mouse[0] > 1089 and 384 > mouse[1] > 366:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 20000
                            targetfleetX = 20000
                            targetfleetY = 30000
                    elif 1151 > mouse[0] > 1133 and 384 > mouse[1] > 366:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 10000
                            targetfleetX = 30000
                            targetfleetY = 30000
                    elif 1126 > mouse[0] > 1108 and 454 > mouse[1] > 436:
                        if click[0] == 1 and jumpTimer == 0:
                            distanceToTargetLocation = 21000
                            targetfleetX = 25000
                            targetfleetY = 15000

                if 980 > mouse[0] > 949 and 607 > mouse[1] > 582:
                    screen.blit(jumpPointHoverOver, (945, 575))
                    if click[0] == 1 and jumpTimer == 0:
                        jumpTimer = 25
                        targetfleetX = 60000
                        targetfleetY = 40000
                        targetSector = 'outpost'
                elif 882 > mouse[0] > 851 and 665 > mouse[1] > 634:
                    screen.blit(jumpPointHoverOver, (847, 627))
                    if click[0] == 1 and jumpTimer == 0:
                        jumpTimer = 25
                        targetfleetX = 35000
                        targetfleetY = 20000
                        targetSector = 'outpost'
                elif 948 > mouse[0] > 917 and 445 > mouse[1] > 420:
                    screen.blit(jumpPointHoverOver, (913, 413))
                    if click[0] == 1 and jumpTimer == 0:
                        jumpTimer = 25
                        targetfleetX = 40000
                        targetfleetY = 15000
                        targetSector = 'delta'


            pygame.draw.circle(screen, white, (864, 662), 65, 3)
            pygame.draw.circle(screen, white, (611, 440), 40, 3)
            pygame.draw.circle(screen, white, (865, 440), 40, 3)
            pygame.draw.circle(screen, white, (1113, 440), 40, 3)

            printWhiteText('Alpha', 22, 612, 285)
            printWhiteText('Delta', 22, 864, 285)
            printWhiteText('Beta', 22, 1112, 285)
            printWhiteText('Outpost', 22, 856, 530)

        # Fleet will only jump to a new sector if jumpTimer == 0.
        if jumpTimer != 0:
            jumpTimer -= 1
            distanceToTargetLocation = 0

            printWhiteText('Jump Timer: ' + str(jumpTimer), 22, 1500, 190)
        elif jumpTimer == 0:
            fleetSector = targetSector




        #The actual game!!! This is just enemy spawn and new wave start.______________________________________________________________________________________________________________________________________

        incomingEnemies = pygame.image.load('incomingEnemies.png')
        enemyFleet = pygame.image.load('enemyFleet.png')
        enemyFleetSmall = pygame.image.load('enemyFleetSmall.png')


        if waveStartCounter != 0:
            waveStartCounter -= 1
            if waveStartCounter == 1:
                waveNumber += 1

        if waveStartCounter == 0 and enemiesInboundMessageTimer != 0:
            enemiesInboundMessageTimer -= 1
            screen.blit(incomingEnemies, (1325, 580))
            printWhiteText('Warning!', 35, 1444, 615)
            printWhiteText('Hostiles Inbound', 20, 1451, 642)


        #Wave one and how it will work.
        if waveStartCounter == 0 and waveOne == True:
            if randomlySelectSectors == True:
                waveOnePioneerPioneerFleetSector = random.choice(enemySpawnSectorsPossibilities)
                waveOnePioneerPioneerFleetX = random.choice(coordinatePossibilities)
                waveOnePioneerPioneerFleetY = 40000
                waveOnePioneerPioneerFleetTargetY = 30000
                enemyTwoHealth = 7000
                enemyThreeHealth = 7000
                pioneerIsEnemyTwoFleetOne = True
                pioneerIsEnemyThreeFleetOne = True
                if waveOnePioneerPioneerFleetX == 15000:
                    waveOnePioneerPioneerFleetTargetX = random.choice(coordinatePossibilities2)

                elif waveOnePioneerPioneerFleetX == 25000:
                    waveOnePioneerPioneerFleetTargetX = random.choice(coordinatePossibilities)

                elif waveOnePioneerPioneerFleetX == 35000:
                    waveOnePioneerPioneerFleetTargetX = random.choice(coordinatePossibilities3)

                if waveOnePioneerPioneerFleetX == 15000:

                    if waveOnePioneerPioneerFleetTargetX == 15000:
                        waveOnePioneerPioneerFleetTravelTime = 10000
                    elif waveOnePioneerPioneerFleetTargetX == 25000:
                        waveOnePioneerPioneerFleetTravelTime = 14000
                elif waveOnePioneerPioneerFleetX == 25000:

                    if waveOnePioneerPioneerFleetTargetX == 15000:
                        waveOnePioneerPioneerFleetTravelTime = 14000
                    elif waveOnePioneerPioneerFleetTargetX == 25000:
                        waveOnePioneerPioneerFleetTravelTime = 10000
                    elif waveOnePioneerPioneerFleetTargetX == 35000:
                        waveOnePioneerPioneerFleetTravelTime = 14000
                elif waveOnePioneerPioneerFleetX == 35000:

                    if waveOnePioneerPioneerFleetTargetX == 25000:
                        waveOnePioneerPioneerFleetTravelTime = 14000
                    elif waveOnePioneerPioneerFleetTargetX == 35000:
                        waveOnePioneerPioneerFleetTravelTime = 10000
                randomlySelectSectors = False








            if waveOnePioneerPioneerFleetSector == fleetSector:
                inSameSectorAsEnemy = True
            elif waveOnePioneerPioneerFleetSector != fleetSector:
                inSameSectorAsEnemy = False

            #Spawning enemies in a random sector and position.
            if waveOnePioneerPioneerFleetSector == 'alpha':
                if waveOnePioneerPioneerFleetX == 15000 and waveOnePioneerPioneerFleetY == 40000:
                    if showExpandedMap == False:
                        screen.blit(enemyFleetSmall, (1300, 710))
                    elif showExpandedMap == True:
                        screen.blit(enemyFleet, (555, 310))
                elif waveOnePioneerPioneerFleetX == 25000 and waveOnePioneerPioneerFleetY == 40000:
                    if showExpandedMap == False:
                        screen.blit(enemyFleetSmall, (1321, 710))
                    elif showExpandedMap == True:
                        screen.blit(enemyFleet, (600, 310))
                elif waveOnePioneerPioneerFleetX == 35000 and waveOnePioneerPioneerFleetY == 40000:
                    if showExpandedMap == False:
                        screen.blit(enemyFleetSmall, (1344, 710))
                    elif showExpandedMap == True:
                        screen.blit(enemyFleet, (643, 310))
                elif waveOnePioneerPioneerFleetX == 15000 and waveOnePioneerPioneerFleetY == 30000:
                    if showExpandedMap == False:
                        screen.blit(enemyFleetSmall, (1300, 726))
                    elif showExpandedMap == True:
                        screen.blit(enemyFleet, (555, 351))
                elif waveOnePioneerPioneerFleetX == 25000 and waveOnePioneerPioneerFleetY == 30000:
                    if showExpandedMap == False:
                        screen.blit(enemyFleetSmall, (1321, 726))
                    elif showExpandedMap == True:
                        screen.blit(enemyFleet, (600, 351))
                elif waveOnePioneerPioneerFleetX == 35000 and waveOnePioneerPioneerFleetY == 30000:
                    if showExpandedMap == False:
                        screen.blit(enemyFleetSmall, (1344, 726))
                    elif showExpandedMap == True:
                        screen.blit(enemyFleet, (643, 351))
                elif waveOnePioneerPioneerFleetX == 25000 and waveOnePioneerPioneerFleetY == 20000:
                    if showExpandedMap == False:
                        screen.blit(enemyFleetSmall, (1321, 755))
                    elif showExpandedMap == True:
                        screen.blit(enemyFleet, (596, 405))
            elif waveOnePioneerPioneerFleetSector == 'delta':
                if waveOnePioneerPioneerFleetX == 15000 and waveOnePioneerPioneerFleetY == 40000:
                    if showExpandedMap == False:
                        screen.blit(enemyFleetSmall, (1424, 710))
                    elif showExpandedMap == True:
                        screen.blit(enemyFleet, (805, 310))
                elif waveOnePioneerPioneerFleetX == 25000 and waveOnePioneerPioneerFleetY == 40000:
                    if showExpandedMap == False:
                        screen.blit(enemyFleetSmall, (1445, 710))
                    elif showExpandedMap == True:
                        screen.blit(enemyFleet, (850, 310))
                elif waveOnePioneerPioneerFleetX == 35000 and waveOnePioneerPioneerFleetY == 40000:
                    if showExpandedMap == False:
                        screen.blit(enemyFleetSmall, (1468, 710))
                    elif showExpandedMap == True:
                        screen.blit(enemyFleet, (893, 310))
                elif waveOnePioneerPioneerFleetX == 15000 and waveOnePioneerPioneerFleetY == 30000:
                    if showExpandedMap == False:
                        screen.blit(enemyFleetSmall, (1424, 726))
                    elif showExpandedMap == True:
                        screen.blit(enemyFleet, (805, 351))
                elif waveOnePioneerPioneerFleetX == 25000 and waveOnePioneerPioneerFleetY == 30000:
                    if showExpandedMap == False:
                        screen.blit(enemyFleetSmall, (1445, 726))
                    elif showExpandedMap == True:
                        screen.blit(enemyFleet, (850, 351))
                elif waveOnePioneerPioneerFleetX == 35000 and waveOnePioneerPioneerFleetY == 30000:
                    if showExpandedMap == False:
                        screen.blit(enemyFleetSmall, (1468, 726))
                    elif showExpandedMap == True:
                        screen.blit(enemyFleet, (893, 351))
                elif waveOnePioneerPioneerFleetX == 25000 and waveOnePioneerPioneerFleetY == 20000:
                    if showExpandedMap == False:
                        screen.blit(enemyFleetSmall, (1445, 755))
                    elif showExpandedMap == True:
                        screen.blit(enemyFleet, (850, 405))
            elif waveOnePioneerPioneerFleetSector == 'beta':
                if waveOnePioneerPioneerFleetX == 15000 and waveOnePioneerPioneerFleetY == 40000:
                    if showExpandedMap == False:
                        screen.blit(enemyFleetSmall, (1548, 710))
                    elif showExpandedMap == True:
                        screen.blit(enemyFleet, (1055, 310))
                elif waveOnePioneerPioneerFleetX == 25000 and waveOnePioneerPioneerFleetY == 40000:
                    if showExpandedMap == False:
                        screen.blit(enemyFleetSmall, (1569, 710))
                    elif showExpandedMap == True:
                        screen.blit(enemyFleet, (1100, 310))
                elif waveOnePioneerPioneerFleetX == 35000 and waveOnePioneerPioneerFleetY == 40000:
                    if showExpandedMap == False:
                        screen.blit(enemyFleetSmall, (1592, 710))
                    elif showExpandedMap == True:
                        screen.blit(enemyFleet, (1143, 310))
                elif waveOnePioneerPioneerFleetX == 15000 and waveOnePioneerPioneerFleetY == 30000:
                    if showExpandedMap == False:
                        screen.blit(enemyFleetSmall, (1548, 726))
                    elif showExpandedMap == True:
                        screen.blit(enemyFleet, (1055, 351))
                elif waveOnePioneerPioneerFleetX == 25000 and waveOnePioneerPioneerFleetY == 30000:
                    if showExpandedMap == False:
                        screen.blit(enemyFleetSmall, (1569, 726))
                    elif showExpandedMap == True:
                        screen.blit(enemyFleet, (1100, 351))
                elif waveOnePioneerPioneerFleetX == 35000 and waveOnePioneerPioneerFleetY == 30000:
                    if showExpandedMap == False:
                        screen.blit(enemyFleetSmall, (1592, 726))
                    elif showExpandedMap == True:
                        screen.blit(enemyFleet, (1143, 351))
                elif waveOnePioneerPioneerFleetX == 25000 and waveOnePioneerPioneerFleetY == 20000:
                    if showExpandedMap == False:
                        screen.blit(enemyFleetSmall, (1569, 755))
                    elif showExpandedMap == True:
                        screen.blit(enemyFleet, (1097, 405))

            #Moving enemies' position to the base in a sector.
            if waveOnePioneerPioneerFleetTravelTime >101:
                waveOnePioneerPioneerFleetTravelTime -= 59
            elif waveOnePioneerPioneerFleetTravelTime < 100:
                waveOnePioneerPioneerFleetX = waveOnePioneerPioneerFleetTargetX
                waveOnePioneerPioneerFleetY = waveOnePioneerPioneerFleetTargetY
                waveOnePioneerPioneerFleetTargetX = 25000
                waveOnePioneerPioneerFleetTargetY = 20000
                if waveOnePioneerPioneerFleetX == 15000:
                    waveOnePioneerPioneerFleetTravelTime = 14000
                elif waveOnePioneerPioneerFleetX == 25000:
                    waveOnePioneerPioneerFleetTravelTime = 10000
                elif waveOnePioneerPioneerFleetX == 35000:
                    waveOnePioneerPioneerFleetTravelTime = 14000

            #How the enemies will decide which fleet ship to attack\.
            if pioneer2TargetHealth == 0:
                if slotOneShipHealth > 0 and slotTwoShipHealth > 0 and slotThreeShipHealth > 0:
                    pioneer2Target = random.choice(enemySelectionFull)
                elif slotOneShipHealth > 0 and slotTwoShipHealth > 0 and slotThreeShipHealth <= 0:
                    pioneer2Target = random.choice(enemySelection1and2)
                elif slotOneShipHealth <= 0 and slotTwoShipHealth > 0 and slotThreeShipHealth > 0:
                    pioneer2Target = random.choice(enemySelection2and3)
                elif slotOneShipHealth > 0 and slotTwoShipHealth <= 0 and slotThreeShipHealth > 0:
                    pioneer2Target = random.choice(enemySelection1and3)
                elif slotOneShipHealth > 0 and slotTwoShipHealth <= 0 and slotThreeShipHealth <= 0:
                    pioneer2Target = 1
                elif slotOneShipHealth <= 0 and slotTwoShipHealth > 0 and slotThreeShipHealth <= 0:
                    pioneer2Target = 2
                elif slotOneShipHealth <= 0 and slotTwoShipHealth <= 0 and slotThreeShipHealth > 0:
                    pioneer2Target = 3
            if pioneer3TargetHealth == 0:
                if slotOneShipHealth > 0 and slotTwoShipHealth > 0 and slotThreeShipHealth > 0:
                    pioneer3Target = random.choice(enemySelectionFull)
                elif slotOneShipHealth > 0 and slotTwoShipHealth > 0 and slotThreeShipHealth <= 0:
                    pioneer3Target = random.choice(enemySelection1and2)
                elif slotOneShipHealth <= 0 and slotTwoShipHealth > 0 and slotThreeShipHealth > 0:
                    pioneer3Target = random.choice(enemySelection2and3)
                elif slotOneShipHealth > 0 and slotTwoShipHealth <= 0 and slotThreeShipHealth > 0:
                    pioneer3Target = random.choice(enemySelection1and3)
                elif slotOneShipHealth > 0 and slotTwoShipHealth <= 0 and slotThreeShipHealth <= 0:
                    pioneer3Target = 1
                elif slotOneShipHealth <= 0 and slotTwoShipHealth > 0 and slotThreeShipHealth <= 0:
                    pioneer3Target = 2
                elif slotOneShipHealth <= 0 and slotTwoShipHealth <= 0 and slotThreeShipHealth > 0:
                    pioneer3Target = 3

            #How the enemies will attack.
            if pioneer2VoidChargesCooldown != 0:
                pioneer2VoidChargesCooldown -= 1
            if pioneer3VoidChargesCooldown != 0:
                pioneer3VoidChargesCooldown -= 1

            if inSameSectorAsEnemy == True:
                if pioneer2VoidChargesCooldown == 0 and enemyTwoHealth > 0:
                    if pioneer2Target == 1:
                        slotOneShipHealth -= 300
                        pioneer2TargetHealth = slotOneShipHealth
                        pioneer2VoidChargesCooldown = 50
                        combatLogEntryTen = combatLogEntryNine
                        combatLogEntryNine = combatLogEntryEight
                        combatLogEntryEight = combatLogEntrySeven
                        combatLogEntrySeven = combatLogEntrySix
                        combatLogEntrySix = combatLogEntryFive
                        combatLogEntryFive = combatLogEntryFour
                        combatLogEntryFour = combatLogEntryThree
                        combatLogEntryThree = combatLogEntryTwo
                        combatLogEntryTwo = combatLogEntryOne
                        combatLogEntryOne = fleetSlotOne + ' Took 300 Damage From Enemy 2'
                    elif pioneer2Target == 2:
                        slotTwoShipHealth -= 300
                        pioneer2TargetHealth = slotTwoShipHealth
                        pioneer2VoidChargesCooldown = 50
                        combatLogEntryTen = combatLogEntryNine
                        combatLogEntryNine = combatLogEntryEight
                        combatLogEntryEight = combatLogEntrySeven
                        combatLogEntrySeven = combatLogEntrySix
                        combatLogEntrySix = combatLogEntryFive
                        combatLogEntryFive = combatLogEntryFour
                        combatLogEntryFour = combatLogEntryThree
                        combatLogEntryThree = combatLogEntryTwo
                        combatLogEntryTwo = combatLogEntryOne
                        combatLogEntryOne = fleetSlotTwo + ' Took 300 Damage From Enemy 2'
                    elif pioneer2Target == 3:
                        slotThreeShipHealth -= 300
                        pioneer2TargetHealth = slotThreeShipHealth
                        pioneer2VoidChargesCooldown = 50
                        combatLogEntryTen = combatLogEntryNine
                        combatLogEntryNine = combatLogEntryEight
                        combatLogEntryEight = combatLogEntrySeven
                        combatLogEntrySeven = combatLogEntrySix
                        combatLogEntrySix = combatLogEntryFive
                        combatLogEntryFive = combatLogEntryFour
                        combatLogEntryFour = combatLogEntryThree
                        combatLogEntryThree = combatLogEntryTwo
                        combatLogEntryTwo = combatLogEntryOne
                        combatLogEntryOne = fleetSlotThree + ' Took 300 Damage From Enemy 2'

                if pioneer3VoidChargesCooldown == 0 and enemyThreeHealth > 0:
                    if pioneer3Target == 1:
                        slotOneShipHealth -= 300
                        pioneer3TargetHealth = slotOneShipHealth
                        pioneer3VoidChargesCooldown = 50
                        combatLogEntryTen = combatLogEntryNine
                        combatLogEntryNine = combatLogEntryEight
                        combatLogEntryEight = combatLogEntrySeven
                        combatLogEntrySeven = combatLogEntrySix
                        combatLogEntrySix = combatLogEntryFive
                        combatLogEntryFive = combatLogEntryFour
                        combatLogEntryFour = combatLogEntryThree
                        combatLogEntryThree = combatLogEntryTwo
                        combatLogEntryTwo = combatLogEntryOne
                        combatLogEntryOne = fleetSlotOne + ' Took 300 Damage From Enemy 3'
                    elif pioneer3Target == 2:
                        slotTwoShipHealth -= 300
                        pioneer3TargetHealth = slotTwoShipHealth
                        pioneer3VoidChargesCooldown = 50
                        combatLogEntryTen = combatLogEntryNine
                        combatLogEntryNine = combatLogEntryEight
                        combatLogEntryEight = combatLogEntrySeven
                        combatLogEntrySeven = combatLogEntrySix
                        combatLogEntrySix = combatLogEntryFive
                        combatLogEntryFive = combatLogEntryFour
                        combatLogEntryFour = combatLogEntryThree
                        combatLogEntryThree = combatLogEntryTwo
                        combatLogEntryTwo = combatLogEntryOne
                        combatLogEntryOne = fleetSlotTwo + ' Took 300 Damage From Enemy 3'
                    elif pioneer3Target == 3:
                        slotThreeShipHealth -= 300
                        pioneer3TargetHealth = slotThreeShipHealth
                        pioneer3VoidChargesCooldown = 50
                        combatLogEntryTen = combatLogEntryNine
                        combatLogEntryNine = combatLogEntryEight
                        combatLogEntryEight = combatLogEntrySeven
                        combatLogEntrySeven = combatLogEntrySix
                        combatLogEntrySix = combatLogEntryFive
                        combatLogEntryFive = combatLogEntryFour
                        combatLogEntryFour = combatLogEntryThree
                        combatLogEntryThree = combatLogEntryTwo
                        combatLogEntryTwo = combatLogEntryOne
                        combatLogEntryOne = fleetSlotThree + ' Took 300 Damage From Enemy 3'





        pygame.display.update()
        clock.tick(60)

gameMenu()
confirmationScreen()
gameLoop()
pygame.quit()
quit()