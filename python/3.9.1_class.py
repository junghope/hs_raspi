class terran:
    hp = 30
    power = 10
    atk = ""

    def attack(self):
        print(self.atk)
        
u1 = terran()# 클래스 인스턴스 생성
u2 = terran()# 클래스 인스턴스 생성

u1.atk = "---->"# u1 공격 동작
u2.atk = "<----"# u2 공격 동작

while u1.hp != 0 and u2.hp != 0:# u1,u2의 hp가 0이 될 때까지 반복
    at = input("attack(1 or 2):")
    if at == "1":# “1”을 입력하면 u1이 공격
        u1.attack()
        u2.hp = u2.hp - u1.power
    elif at == "2":# “2”을 입력하면 u2가 공격
        u2.attack()
        u1.hp = u1.hp - u2.power# 공격 방향에 따라서 hp 감소

    print("u1.hp=", u1.hp, ", u2.hp=", u2.hp)# 공격이 끝나고 나면 hp 표시


if u1.hp <= 0:# u1의 hp가 0 이하면 u2 승리
    print("u2 win!")
elif u2.hp <= 0:# u2의 hp가 0 이하면 u1 승리
    print("u1 win!“)
