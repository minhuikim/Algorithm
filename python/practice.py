# 연습) 기본문법 
# 자료형 - 숫자
print(5)
print(-10)
print(3.14)
print(1000)
print(5+3)
print(2*8)
print(3*(3+1))

# 자료형 - 문자열
print('풍선')
print("나비")
print("ㅋ")
print("ㅋ"*9)

# 자료형 - 참/거짓
print(5 > 10)
print(5 < 10)
print(True)
print(False)
print(not True)
print(not False)
print(not (5 > 10))

# 변수
animal = "강아지"
name = "연탄이"
age = 4
hobby = "공놀이"
is_adult = age >= 3

print("우리집 "+animal+"의 이름은 "+name+"이예요")
hobby = "산책"
#print(name+"는 "+str(age)+"살이며, "+hobby+"을 아주 좋아해요")
print(name,"는 ",age,"살이며, ",hobby,"을 아주 좋아해요")
print(name+"는 어른일까요? "+str(is_adult))

#주석
'''print(주석)'''

# 변수를 이용하여 다음 문장을 출력
# 변수명 
#     : station
# 변수값 
#     : "사당", "신도림", "인천공항" 순서대로 입력
# 출력문장 
#     : xx행 열차가 들어오고 있습니다.
station = "인천공항"
print(station+"행 열차가 들어오고 있습니다.")