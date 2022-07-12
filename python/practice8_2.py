## 클래스 - 상속

# 일반 유닛
class Unit:
    def __init__(self, name, hp):   # Unit의 생성자
        self.name = name                 
        self.hp = hp                     

# 공격 유닛
class AttackUnit(Unit):                     # 괄호 안에 상속 받을 클래스명을 적는다. (Unit 클래스 상속)
    def __init__(self, name, hp, damage):   # 부모 클래스 : Unit, 자식클래스 : AttackUnit
        Unit.__init__(self, name, hp)                     # Unit의 생성자 호출
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

## 클래스 - 다중상속

# 드랍쉽 : 공중 유닛, 수송기. 마린 / 파이어뱃 / 탱크 등을 수송. 공격 X

# 날 수 있는 기능을 가진 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed
    
    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.flying_speed))

# 공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage)
        Flyable.__init__(self, flying_speed)

# 발키리 : 공중 공격 유닛, 한번에 14발 미사일 발사.
valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
valkyrie.fly(valkyrie.name, "3시")
'''
발키리 : 3시 방향으로 날아갑니다. [속도 5]
'''

# FlyableAttackUnit -상속-> AttackUnit
# FlyableAttackUnit -상속-> Flyable
# AttackUnit -상속-> Unit


