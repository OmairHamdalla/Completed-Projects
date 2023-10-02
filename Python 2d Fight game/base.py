import module as extra
import random
import time
class Game:
    def __init__ (self):
        self.menu()

    def menu(self):
        print("Welcome to 2D Python Fighting Game!")
        inp = input(
"""
    Enter:
    1.Play the game
    2.Instructions
    3.About
    -->
"""            
        )

        if int(inp) == 1 : game = Core()
        elif  int(inp) == 2: self.instructions()
        elif  int(inp) == 3: self.about()
        else: print("Invalid entry")


    def instructions():
        print("To play the game you choose to attack or defend each turn,\nAttacking would be an approximate number close to your attack average number thats given to your character.\nSame thing goes for defending too.")
        input("\nPress anything to go back...")
        extra.clear()

    def about():
        print("To play the game you choose to attack or defend each turn,\nAttacking would be an approximate number close to your attack average number thats given to your character.\nSame thing goes for defending too.")
        input("\nPress anything to go back...")
        extra.clear()


class Core:
    def __init__(self):
        blob = Entity("Blob", 13 , 16,"Blobber spat")
        ghosterk = Entity("Ghosterk", 10 , 19,"Fire Charge")
        slither = Entity("Slither", 15 , 14,"Venomous Bite")
        enemies = [blob, ghosterk, slither]
        self.enemy = random.choice(enemies)

        print("Welcome to the battle !")
        time.sleep(1)
        self.player = Player()

        print(f"Your attack: {self.player.damageAvg} & Your defence: {self.player.defenceAvg}")
        time.sleep(1)
        print(f"{self.enemy.name} Attack: {self.enemy.damageAvg} & Defence: {self.enemy.defenceAvg}")
        time.sleep(1)
        print(self.player.name ,"VS",self.enemy.name)
        time.sleep(1)

        extra.sure("Are you Ready?")
        extra.counter(3)
        extra.clear()

        self.isDone = False
        self.begin()       



    def display(self):
        for row in zip(self.player.shape.split("\n") , self.enemy.shape.split("\n")):
            print(row[0] + "      " + row[1])
        print(self.player.name + ":"+str(self.player.health) + "            " + self.enemy.name + ":" + str(self.enemy.health))

    def turn(self):
        self.display()
        playerMove = int(input("Choose your next move warrior!\nAttack(1)\nDefence(2)\n--> "))
        time.sleep(1)
        extra.clear()
        enemyMove = random.randint(1,2)

        if playerMove == 1 :
            print(self.player.name + " attacks!")
            if enemyMove == 1:
                print("And " + self.enemy.name + " attacks Back!")
                self.attackAndAttack()
            if enemyMove == 2:
                print("But " + self.enemy.name + " Blocks!")
                self.attackAndBlock(self.player,self.enemy)

        if playerMove == 2 :
            print(self.player.name + " Blocks!")
            if enemyMove == 1:
                print("And " + self.enemy.name + " attacks!")
                self.attackAndBlock(self.enemy,self.player)
            if enemyMove == 2:
                print("Both chose defence!")
                self.defenceAndDefence()
            
        self.checkWinner()

   
    def checkWinner(self):
        if self.player.health <= 0 or self.enemy.health <= 0 :
            if self.player.health <= 0:
                print(self.enemy.shape)
                print("You died warrior!\nGame over...")
                
            elif self.enemy.health <= 0:
                print(self.player.shape)
                print("WARRIOR YOU WON!")
            print("Going to main menu in 5 secs")
            extra.counter(5)
            

    def pointSetter(self,pointAvg,isAttack):
        if isAttack:
            point = random.randint(pointAvg - 2, pointAvg + 10)
        else :
            point = random.randint(pointAvg - 6, pointAvg + 2)
        return(int(point))
    
#########################################################################
# Attack Functions 
#########################################################################
    def attackAndBlock(self,attacker,victim):
        damage = self.pointSetter(attacker.damageAvg,1)
        defence =  self.pointSetter(victim.defenceAvg,0)

        hit = damage - defence
        # hit = 12 - 14
        if hit < 0 or hit == 0:
            print("Blocked")
        if hit > 0:
            victim.health -= hit
            # health = health - (-2)
            print(f"Yet {attacker.name} {attacker.attName} and breaks the block! {hit} Damage to {victim.name}!")
            print(f"Hit! {hit} Damage done to {victim.name}!")
            

    def attackAndAttack(self):
        playerDamage = self.pointSetter(self.player.damageAvg,1)
        enemyDamage =  self.pointSetter(self.enemy.damageAvg,1)
        self.enemy.health -= playerDamage
        self.player.health -= enemyDamage

        print(f"{self.player.name} {self.player.attName} and did {playerDamage} Damage to {self.enemy.name}!")
        print(f"But {self.enemy.name} hit back with {self.enemy.attName} dealing {enemyDamage} Damage to you!")

    def defenceAndDefence(self):
        print("Nothing happened...")
        
#########################################################################

    def begin(self):
        while not self.isDone:
            self.turn()
        time.sleep(1)
        extra.clear()
        self.display()
            

        

class Entity:
    def __init__(self,name,damage,defence,attName):
        self.name = name
        self.damageAvg = damage
        self.defenceAvg = defence
        self.attName = attName
        self.health = 1
        self.shape = extra.getShape(self.name)

class Player:
    def __init__(self):
        self.name = input("What's your name warrior: ")
        self.health = 100
        self.attName = "Swings his sword"
        
        total = 0
        #damage = 20 | defence = 18
        while total <= 28 or total > 32:
            self.damageAvg = random.randint(12,20)
            self.defenceAvg = random.randint(10,18)
            total = self.damageAvg + self.defenceAvg
        
        self.shape = r'''
  (_oo) /
 /--|--/ 
/ /--l   
 /   L   
 L       
'''


    
    
    

    
