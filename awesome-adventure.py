from random import randint as rint
devses=False
playing=True
start=True
errors=[]
dubs=0
id={1:"apple",2:"bannana",3:"steak",4:"cat",5:"dog",6:"duck",7:"knife",8:"staff",9:"bow"}
class player():
    inventoryid=[]
    if start:
        inventoryid.append(rint(1,9))
        start=False
    inventory=[]
    for i in inventoryid:
        inventory.append(id[i])
    lvl=1
    hp=100*lvl
    xp=0
    atk=5*lvl
    critRINT=1+rint(1,5)
    critBonus=10+rint(1,5)
    healamt=3*lvl
class enemy():
    def __init__(self,hp,atk,lvl):
        self.hp=hp
        self.atk=atk
        self.lvl=lvl
        self.critRINT=int((lvl**0.5)+1)
        self.critBonus=int((lvl**0.5)+1)
        self.healamt=int((lvl**0.5)+1)
def combat(eney):
    while True:
        try:
            player.inventory.clear()
            for i in player.inventoryid:
                player.inventory.append(id[i])
            inv=player.inventory
            print(f"inventory:  {inv}")
            act=int(input("1.attack  2.heal  3.inventory "))
        except Exception as e:
            errors.append(f"-{e}-")
        if act==1:
            attack(eney,player)
        elif act==2:
            heal(player,player.healamt)
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
            item=input("pick one item to use\n").lower()
            if item in player.inventory:
                i=item
                if i=="apple":
                    player.hp+=7
                    player.inventoryid.remove(1)
                    player.inventory.clear()
                elif i=="bannana":
                    player.hp+=12
                    player.inventoryid.remove(2)
                    player.inventory.clear()
                elif i=="steak":
                    player.hp+=22
                    player.inventoryid.remove(3)
                    player.inventory.clear()
                elif i=="cat":
                    player.critRINT+=3
                    player.healamt+=2
                    player.inventoryid.remove(4)
                    player.inventory.clear()
                elif i=="dog":
                    player.atk+=3
                    player.healamt+=2
                    player.inventoryid.remove(5)
                    player.inventory.clear()
                elif i=="duck":
                    player.critBonus+=3
                    player.healamt+=2
                    player.inventoryid.remove(6)
                    player.inventory.clear()
                elif i=="knife":
                    player.atk+=2
                    player.critRINT+=4
                    player.critBonus+=2
                    player.inventoryid.remove(7)
                    player.inventory.clear()
                elif i=="staff":
                    player.atk+=3
                    player.critRINT+=3
                    player.critBonus+=2
                    player.inventoryid.remove(8)
                    player.inventory.clear()
                elif i=="bow":
                    player.atk+=4
                    player.critRINT+=2
                    player.critBonus+=2
                    player.inventoryid.remove(9)
                    player.inventory.clear()
        else:
            print("you are only supposed to say 1, 2, or 3")
        if rint(1,12)<=1:
            if player.hp>100:
                tree=True
            else:
                tree=False
            player.hp*=1.5
            player.hp=int(player.hp)
            if player.hp>100 and not tree:
                player.hp=100
        if eney.hp<=0:
            player.xp+=eney.lvl
            if player.xp>=100:
                player.xp-=100
                player.lvl+=1
            player.healamt+=1
            return "liv"
            break
        if rint(1,2)==1:
            attack(player,eney)
        else:
            heal(eney,eney.lvl)
        if player.hp<=0:
            return("stop")
            break
        if rint(1,13)==1:
            player.inventoryid.append(rint(1,3))
        elif rint(1,13)==1:
            player.inventoryid.append(rint(4,6))
        elif rint(1,13)==1:
            player.inventoryid.append(rint(7,9))
        print(f"player  enemy \nhp:{player.hp}   {eney.hp}")
def heal(subject,hpUp):
    subject.hp+=hpUp
def attack(atee,ater):
    atee.hp-=ater.atk
    if rint(0,100+(int(atee.critRINT/3)))<=ater.critRINT:
        atee.hp-=ater.critBonus
        ater.hp+=ater.healamt
        ater.critRINT+=1
while playing:
    lvll=rint(player.lvl-5,player.lvl+5)
    if lvll<=0:
        lvll=1
    ernie=enemy(player.lvl+99,player.lvl+5,lvll)
    res=combat(ernie)
    ind=False
    if res=="stop":
        playing=False
        print(f"player  enemy \nhp:{player.hp}   {ernie.hp}")
    elif res=="liv":
        dubs+=1+rint(0,1)
        player.inventoryid.clear()
        for i in range(dubs):
            player.inventoryid.append(rint(1,9))
        player.inventory.clear()
        for i in player.inventoryid:
            player.inventory.append(id[i])
if devses:
    print(*errors)
