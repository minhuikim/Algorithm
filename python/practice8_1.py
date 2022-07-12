# 클래스

# 마린 : 공격 유닛, 군인. 총을 쏠 수 있음
name = "마린"   # 유닛의 이름
hp = 40         # 유닛의 체력
damage = 5      # 유닛의 공격력

print("{0} 유닛이 생성되었습니다.".format(name))
print("체력 {0}, 공격력 {1}\n".format(hp, damage))

# 탱크 : 공격 유닛, 탱크. 포를 쏠 수 있는데, 일반 모드 / 시즈 모드가 있다.
tank_name = "탱크"
tank_hp = 150
tank_damage = 35

print("{0} 유닛이 생성되었습니다.".format(tank_name))
print("체력 {0}, 공격력 {1}\n".format(tank_hp, tank_damage))

tank2_name = "탱크2"
tank2_hp = 150
tank2_damage = 35

print("{0} 유닛이 생성되었습니다.".format(tank2_name))
print("체력 {0}, 공격력 {1}\n".format(tank2_hp, tank2_damage))

def attack(name, location, damage):
    print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]".format( \
        name, location, damage))

attack(name, "1시", damage)
attack(tank_name, "1시", tank_damage)
attack(tank2_name, "1시", tank2_damage)

'''
마린 유닛이 생성되었습니다.
체력 40, 공격력 5

탱크 유닛이 생성되었습니다.
체력 150, 공격력 35

탱크2 유닛이 생성되었습니다.
체력 150, 공격력 35

마린 : 1시 방향으로 적군을 공격 합니다. [공격력 5]
탱크 : 1시 방향으로 적군을 공격 합니다. [공격력 35]
탱크2 : 1시 방향으로 적군을 공격 합니다. [공격력 35]
'''

# 일반 유닛
class Unit:
    def __init__(self, name, hp, damage):   # self를 제외하고 함수에 정의된 파라미터의 개수만큼 인수를 보내야 오류가 나지 않는다.
        self.name = name                    # self : 멤버변수, 자기 자신. 클래스내에서 메소드를 작성할 때 항상 작성한다.
        self.hp = hp                        # self.name, self.hp, ... : 멤버변수, 클래스 내에서 정의된 변수
        self.damage = damage                # 멤버변수 : 초기화할 수 있고 사용할 수 있다.
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

marine1 = Unit("마린", 40, 5)
marine2 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35)
#tank = Unit("탱크", 150) # 에러 출력
'''
마린 유닛이 생성되었습니다.
체력 40, 공격력 5
마린 유닛이 생성되었습니다.
체력 40, 공격력 5
탱크 유닛이 생성되었습니다.
체력 150, 공격력 35
'''

# 레이스 : 공중 유닛, 비행기. 클로킹 (상대방에게 보이지 않음)
wraith1 = Unit("레이스", 80, 5)
print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage)) # 저장된 변수를 출력

# 마인드 컨트롤 : 상대방 유닛을 내 것으로 만드는 것 (빼앗음)
wraith2 = Unit("빼앗은 레이스", 80, 5)
wraith2.clocking = True                 # 외부에서 새로운 변수 추가해서 값 할당

if wraith2.clocking == True:
    print("{0} 는 현재 클로킹 상태입니다.".format(wraith2.name))

#if wraith1.clocking == True:           # 에러 출력 : 외부에서 변수 추가시 확장한 개체에만 적용
#    print("{0} 는 현재 클로킹 상태입니다.".format(wraith2.name))
'''
레이스 유닛이 생성되었습니다.
체력 80, 공격력 5
유닛 이름 : 레이스, 공격력 : 5
빼앗은 레이스 유닛이 생성되었습니다.
체력 80, 공격력 5
빼앗은 레이스 는 현재 클로킹 상태입니다.
'''

## 멤버 변수
# 공격 유닛
class AttackUnit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]"\
            .format(self.name, location, self.damage))              # 클래스 내 메소드에서는 self.으로 자기자신의 멤버변수를 불러옴

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

# 파이어뱃 : 공격 유닛, 화염방사기.
firebat = AttackUnit("파이어뱃", 50, 16)
firebat.attack("5시")

# 공격 2번 받는다고 가정
firebat.damaged(25)
firebat.damaged(25)
'''
파이어뱃 : 5시 방향으로 적군을 공격 합니다. [공격력 16]
파이어뱃 : 25 데미지를 입었습니다.
파이어뱃 : 현재 체력은 25 입니다.
파이어뱃 : 25 데미지를 입었습니다.
파이어뱃 : 현재 체력은 0 입니다.
파이어뱃 : 파괴되었습니다.
'''
