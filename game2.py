import random
import time


slime = {
    "이름" : "야생의 슬라임",
    "체력" : 20,
    "기본공격" : "몸통박치기",
    "스킬" : "산성액 뿌리기"
}
    

def character(name, Weapons,Amor):
    info = {
        "닉네임" : name,
        "체력": 50,
        "무기" : Weapons,
        "방어구" : Amor,
        "기본공격" : "기본공격",
        "스킬" : "치명타"   
    }        
    print("{0}님 반갑습니다." .format(info["닉네임"]))
    return info
    
name = input("사용할 닉네임을 입력하세요: ")


def choice():

    print("1.검 2.방패 3.활 4.??? 중에 무기를 선택하시오.")
    Weapons = int(input("번호를 입력하세요.: "))

    if Weapons == 1: 
        Weapons = "초보자의 검"
    elif Weapons ==2:
        Weapons = "초보자의 단검"
    elif Weapons == 3:
        Weapons = "초보자의 활"
    elif Weapons == 4:
        Weapons = "맨손"
    else:
        print("잘못입력하셨습니다. 다시 확인해주세요")
        return choice()
    print(Weapons,"을 획득하셨습니다.")    
    
    print("방어구를 선택하시오 1.가죽 조끼 2.천 갑옷 3. 풀 플레이트 아머")
    Amor = int(input("번호를 입력하세요.: "))
    if Amor == 1:
        Amor = "천 갑옷"
    elif Amor == 2:
        Amor = "가죽 갑옷"
    elif Amor == 3:
        Amor = "사슬 갑옷"
    else:
        print("잘못입력하셨습니다. 다시 확인해주세요")
        return choice()
    print(Amor, "(을)를 획득하셨습니다.")
    return Weapons, Amor

Weapons, Amor = choice()
status = character(name,Weapons,Amor)
print(status)



def act1():
    time.sleep(1) 
    print ("길을 가다 슬라임을  만났습니다.")
    
    C_HP = 50
    S_HP = slime["체력"]
    while S_HP > 1:
    
        act1_1 = int(input("\n1.기본공격(공격력 5)\n2.스킬사용(공격력 15)\n"))
        if act1_1 == 1:
            S_HP -= 5
            print("슬라임에게 5의 데미지를 입혀 체력이 {} 남았습니다.".format(S_HP))    
            S_A = random.randint(3,5)
            C_HP -= S_A
            print("슬라임의 몸통박치기에 당해 {}만큼 피해를 입었습니다.".format(S_A))
            print("남은 HP {}!".format(C_HP))
            if C_HP < 0:
                print("슬라임에게 5의 데미지를 입혀 체력이 0 남았습니다.")    
            if S_HP < 1:
                print("슬라임의 체력이 0이되어 사라졌습니다.")
                break
        if act1_1 ==2:
            if S_HP > 9:
                S_HP -= 10
                print("슬라임에게 10의 데미지를 입혀 체력이 {} 남았습니다.".format(S_HP))    
                S_A = random.randint(10,20)
                C_HP -= S_A
                print("슬라임의 산성액 뿌리기 {}만큼 피해를 입었습니다.".format(S_A))
                print("남은 HP {}!".format(C_HP))
            elif S_HP < 11:
                S_HP -= 10
                print("슬라임에게 10의 데미지를 입혀 체력이 0 남았습니다.")    

            if S_HP < 1:
                print("\n슬라임의 체력이 0이되어 사라졌습니다.")
                break
act1()        


    
        
    
      

    
    
    
        
        
    