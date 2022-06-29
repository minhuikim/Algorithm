#문자열
sentence = '나는 소년입니다'
print(sentence)
sentence2 = "파이썬은 쉬워요"
print(sentence2)
sentence3 = """
나는 소년이고,
파이썬은 쉬워요
"""

#슬라이싱 (필요한 만큼만 잘라서 사용)
jumin = "940825-1234567"
print("성별 : " + jumin[7])
print("연 : " + jumin[0:2]) # 0 부터 2 직전까지 (0~1)
print("월 : " + jumin[2:4])
print("일 : " + jumin[4:6])

print("생년월일 : " + jumin[:6])                # 처음부터 6 직전까지
print("뒤 7자리 : " + jumin[7:])                # 7 부터 끝까지
print("뒤 7자리 (뒤에서부터) : " + jumin[-7:])   # 맨 뒤에서 7번째부터 끝까지

#문자열 처리 함수
python = "Python is Amazing"

print(python.lower())       # 소문자로 변경
print(python.upper())       # 대문자로 변경
print(python[0].isupper())  # 지정한 글자가 대문자인지 확인
print(len(python))          # 문자열 길이 반환
print(python.replace("Python", "Java")) # 문자를 찾아서 변경

index = python.index("n")   # 문자의 위치를 찾음
print(index)
print(python.index("n", index + 1)) # 문자의 두번째 위치를 찾음

print(python.find("n"))     # 문자의 위치를 찾음
print(python.find("Java"))  # 찾는 값이 없으면 -1 반환
#print(python.index("Java")) # 찾는 문자가 없으면 오류 반환 (프로그램 진행 멈춤)

print(python.count("n"))    # 문자를 사용한 회수 출력

# 문자열 포멧
print("a" + "b")
print("a", "b")

## 방법 1 %
print("나는 %d살입니다." % 20)          # 정수값을 대체해서 입력
print("나는 %s을 좋아해요." % "파이썬") # 문자열을 대체해서 입력
print("Apple은 %c로 시작해요" % "A")    # 문자를 대체해서 입력
print("나는 %s살입니다." % 20)          # 문자열에 숫자 입력 가능
print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨간")) # 여러 문자 대체

## 방법 2 {}
print("나는 {}살입니다.".format(20)) # format 괄호의 값을 {}에 대체
print("나는 {}색과 {}색을 좋아해요.".format("파란", "빨간")) # 여러 문자 대체
print("나는 {0}색과 {1}색을 좋아해요.".format("파란", "빨간")) # 여러 문자를 순서대로 대체
print("나는 {1}색과 {0}색을 좋아해요.".format("파란", "빨간"))

## 방법 3 {}
print("나는 {age}살이며, {color}색을 좋아해요".format(age = 20, color = "빨간")) # 변수처럼 활용해서 대체
print("나는 {age}살이며, {color}색을 좋아해요".format(color = "빨간", age = 20))

## 방법 4 f{} (v3.6 이상~)
age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요.")

# 탈출문자
print("백문이 불여일견\n백견이 불여일타") # \n 줄바꿈
print("저는 '김민희'입니다.")            # \" \' 문장 내 따옴표 출력
print('저는 "김민희"입니다.')            # \" \' 문장 내 따옴표 출력
print("저는 \"김민희\"입니다.")          # \" \' 문장 내 따옴표 출력
print('저는 \'김민희\'입니다.')          # \" \' 문장 내 따옴표 출력
print("D:\\source\\repos\\Algorithm>")  # \\ 문장 내에서 \ 출력
print("Red Apple\rPine")                # \r 커서를 맨 앞으로 이동
                                        # Red자리로 커서가 이동해서 Pine을 덮어씀
                                        # PineApple 출력
print("Redd\bApple")                    # \b 백스페이스 (한글자 삭제)
                                        # RedApple
print("Red\tApple")                     # \t 탭

'''
사이트 별로 비밀번호를 만들어 주는 프로그램 작성

예) http://naver.com
규칙1 : http:// 부분은 제외 => naver.com
규칙2 : 처음 만나는 점(.) 이후 부분은 제외 => naver
규칙3 : 남은 글자 중 처음 세자리 + 글자개수 + 글자 내 'e'갯수 + '!'로 구성
                        (nav)      (5)             (1)       (!)
생성된 비밀번호 : nav51!
'''
# url = "http://naver.com"
# url = "http://daum.net"
# url = "http://google.com"
url = "http://youtube.com"
addr = url.replace("http://", "")
print(addr)         # naver.com / daum.net / google.com / youtube.com
addr = addr[:addr.find(".")]
print(addr)         # naver / daum / google / youtube
password = addr[:3] + str(len(addr)) + str(addr.count("e")) + "!"
print(password)     # nav51! / dau40! / goo61! / you71!
print("{0}의 비밀번호는 {1}입니다.".format(url, password))
# http://naver.com의 비밀번호는 nav51!입니다.
# http://daum.net의 비밀번호는 dau40!입니다.
# http://google.com의 비밀번호는 goo61!입니다.
# http://youtube.com의 비밀번호는 you71!입니다.