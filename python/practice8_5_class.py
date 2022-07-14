## super - 다중상속시 발생하는 문제점
class Unit:
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")

# class FlyableUnit(Unit, Flyable):   # Unit 생성자만 초기화되고 Flyable은 실행되지 않음
class FlyableUnit(Flyable, Unit):     # 다중상속시 하나의 생성자만 초기화되는 문제점이 발생한다.
    def __init__(self):
        # super().__init__()
        Unit.__init__(self)               # 모든 부모 클래스에 대해서 초기화가 필요한 경우 super를 사용하지 않고 직접 작성한다.
        Flyable.__init__(self)

# 드랍쉽
dropship = FlyableUnit()
'''
FlyableUnit(Unit, Flyable)
super().__init__()
    Unit 생성자

FlyableUnit(Flyable, Unit)
super().__init__()
    Flyable 생성자

FlyableUnit(Flyable, Unit)
Unit.__init__(self)
Flyable.__init__(self)
    Unit 생성자
    Flyable 생성자
'''

