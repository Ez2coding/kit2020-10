import json

def set_charact(name, Weapons,Amor):
    info = {
        "닉네임" : name,
        "체력": 50,
        "무기" : Weapons,
        "방어구" : Amor,
        "기본공격" : "기본공격",
        "스킬" : "치명타"   
    }        
    with open("static/save.txt", "w", encoding='utf-8') as f:
        json.dump(character, f, ensure_ascii = False, indent=4)
    return character

def save_game(filename, charact):
    f = open(filename, "w", encoding='utf-8')
    for key in charact:
        print("%s:%s" % (key, charact[key]))
        f.write("%s:%s\n" % (key, charact[key]))
    f.close()     

# ##캐릭터 설정 함수
character = set_charact(name)    

##캐릭터 정보 파일에 저장
save_game("save.txt",character)