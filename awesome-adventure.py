import time

devses=True
playing=True
errors=[]
id={1:"apple",2:"bannana",3:"steak",4:"cat",5:"dog",6:"duck",7:"knife",8:"staff",9:"bow"}
rid={"apple":1,"bannana":2,"steak":3,"cat":4,"dog":5,"duck":6,"knife":7,"staff":8,"bow":9}

class player():
    points=0
    inventoryid=[1,2,3,4,5,6,7,8,9]
    inventory=[]
    for i in inventoryid:
        inventory.append(id[i])
    hp=100
    lvl=1
    xp=0
    atk=5*lvl
    critRINT=1
    critBonus=10
class enemy():
    def __init__(self,hp,atk,lvl):
        self.hp=hp
        self.atk=atk
        self.lvl=lvl
        self.critRINT=int((lvl**0.5)+1)
        self.critBonus=int((lvl**0.5)+1)
def combat(eney):
    while True:
        try:
            act=int(input("1.attack  2.heal  3.inventory"))
        except Exception as e:
            errors.append(f"-{e}-")
        if act==1:
            attack(eney,player)
        elif act==2:
            heal(player,player.lvl)
        elif act==3:
            x=0
            for i in player.inventoryid:
                x+=1
            y=0
            for i in player.inventory:
                y+=1
            if x==y:
                pass
            elif x>y:
                for i in player.inventoryid:
                    player.inventory.append(id[i])
            print(*player.inventory)#unfinished
            item=input("pick one item to use")#unfinished
            if item in player.inventory:
                key=rid[item]
                if key==1:
                    player.hp+=5
                    player.inventoryid.remove(1)
                    player.inventory.clear()
                elif key==2:
                    player.hp+=10
                    player.inventoryid.remove(2)
                    player.inventory.clear()
                elif key==3:
                    player.hp+=20
                    player.inventoryid.remove(3)
                    player.inventory.clear()
                elif key==4:
                    player.points+=1
                    player.inventoryid.remove(4)
                    player.inventory.clear()
                elif key==5:
                    player.points+=2
                    player.inventoryid.remove(5)
                    player.inventory.clear()
                elif key==6:
                    player.points+=3
                    player.inventoryid.remove(6)
                    player.inventory.clear()
                elif key==7:
                    player.atk+=1
                    player.critRINT+=3
                    player.critBonus+=1
                    player.inventoryid.remove(7)
                    player.inventory.clear()
                elif key==8:
                    player.atk+=2
                    player.critRINT+=2
                    player.critBonus+=1
                    player.inventoryid.remove(8)
                    player.inventory.clear()
                elif key==9:
                    player.atk+=3
                    player.critRINT+=1
                    player.critBonus+=1
                    player.inventoryid.remove(9)
                    player.inventory.clear()
        else:
            print("you are only supposed to say 1, 2, or 3")
        if eney.hp<=0:
            player.xp+=eney.lvl
            player.points+=1
            break
        if rint(1,2)==1:
            attack(player,eney)
        else:
            heal(eney,eney.lvl)
        if player.hp<=0:
            return("stop")
            break
        print(f"player  enemy \nhp:{player.hp}   {eney.hp}")
def heal(subject,hpUp):
    subject.hp+=hpUp
def attack(atee,ater):
    atee.hp-=ater.atk
    if rint(0,100+(int(atee.critRINT/3)))<=ater.critRINT:
        atee.hp-=ater.critBonus
lvll=rint(player.lvl-5,player.lvl+5)
if lvll<=0:
    lvll=1
ernie=enemy(player.lvl+100,player.lvl+5,lvll)
combat(ernie)

hello=4
north=1
south=1
east=1
west=1
name = input("Hello there traveler! Tell me, what might your name be? ")

print("Hello " +name +"! Here in this 'Adventure RPG!', you win the game by"
      +" defeating villians and becoming a hero!")
print("--")
print("NORTH")
print("EAST")
print("SOUTH")
print("WEST")
print("--")
while hello>0:
    story = input("Where would you like to go now?")
    if story.lower() == "north" and north==1:
        print("You have reached Riddleland! Solve the riddle "
              +"in order to win!")
        print("What runs but cannot walk, has a mouth but cannot speak, has a "
              +"bed but cannot sleep, has a head but cannot think?")
        riddleresponse=input()
        if riddleresponse.lower() == "river":
            print("You got it correct! Congratulations!")
            hello=hello-1
            north=0
        else:
            print("Wrong! Try again when you visit Riddleland!")
    elif story.lower() == "south" and south==1:
        print("You have reached Mathland! Solve the math problem to win!")
        print("What is eleven factorial plus twelve factorial over "
             +"thirteen factorial simplified?")
        mathresponse=input()
        if mathresponse=="1/12":
            print("You got it correct! Congratulations!")
            hello=hello-1
            south=0
        else:
            print("Wrong! Try again when you visit Mathland!")
    elif story.lower() == "east" and east==1:
        print("You have reached Historyland! Solve the history "
                 +"question to win!")
        print("Who was the first president of the United States?")
        historyresponse=input()
        if historyresponse.lower() =="george washington":
            print("You got it correct! Congratualtions!")
            hello=hello-1
            east=0
        else:
            print("Wrong! Try again when you visit Historyland!")
    elif story.lower() == "west" and west==1:
        print("Welcome to the wild west! The west is different from the North,"
              +" South and East because it does not have a question!")
        print("Instead, the wild west is wild because it is ruled by "+
             "the Wicked Witch of the Wild West!")
        print("They also call the witch WWWW.")
        print("Many brave heros have went to make the west civilized "+
              "but failed!")
        answer=input("You look around and see a path in a forest. Do you"+
             " walk on the path?")
        if answer.lower() =="yes":
            print("Let's continue! You see a castle and walk to it. It is "+
                  "guarded by knights.")
            print("You fight the knights and lose. You lose and run away.")
        elif answer.lower()=="no":
            print("You see a castle and walk around it.")
            print("You find a secret door leading to"+
                  " the castle.")
            print("You walk in and find a tub with water. Since you are "+
                  "thirsty, you fill your canteen with water.")
            print("Then the Wicked Witch of the Wild West comes in!")
            print("Here are your choices:")
            print("1: You throw your canteen at the witch.")
            print("2: You attack the witch with your hands.")
            print("3: You run away to the woods.")
            response=input()
            if response=="1":
                print("The cheap canteen shatters when it hits the witch.")
                print("When the witch touches the water, the witch dissolves!")
                hello=hello-1
                west=0
            elif response=="2":
                print("The witch calls the guards, and they chase you away.")
            elif response=="3":
                print("You run away back to the main lands.")
    elif story.lower=="north" and north==0 or story.lower=="south" and south==0 or story.lower=="east" and east==0 or story.lower=="west" and west==0:
        print("You already went here. You cannot come back again.")
print("When you go back to the mainlands, the Wizard of Oz thanks you for "
      +"defeating the Wicked Witch of the West.")
party=input("He invites you to a party at the Emerald City. Do you go?")
if party.lower()=="yes":
    print("You go to the Emerald City and meet the Wizard of Oz"
          +" at the middle.")
    print("The Wizard of Oz congratulates you, and then he gives you a new "
          +"mission.")
    print("You must kill the Wicked Witch of the East!")
elif party.lower()=="no":
    print("You rest at home and sleep.")
    time.sleep(5)
    print("Time to wake up!")
    print("The mailman has sent you a mail from Oz.")
    print("It congratulates you for killing the Wicked Witch of West.")
    print("You also have new orders. You must get rid of the Wicked Witch of "
          +"the East!")
print("The Wizard will come with you, and you will go today at noon.")
print("He has also sent you a information packet.")
print("The WWE is harder to beat than the WWWW, and WWE's weakness is "
      +"unknown.")
print("Good luck!")

