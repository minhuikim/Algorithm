### 내장함수
# import 할 필요 없이 바로 사용할 수 있는 함수

# language = input("무슨 언어를 좋아하세요?")
# print("{0}은 아주 좋은 언어입니다!".format(language))
#input, print, format은 내장함수
'''
무슨 언어를 좋아하세요?파이썬
파이썬은 아주 좋은 언어입니다!
'''

# dir : 어떤 객체를 넘겨줫을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시
# print(dir())
'''['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'language']'''
# import random #외장 함수
# print(dir())
'''['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'language', 'random']'''
# import pickle
# print(dir())
'''['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'language', 'pickle', 'random']'''


# print(dir(random)) # 외장함수 random 내에서 사용할 수 있는 객체 표시
'''
['BPF', 'LOG4', 'NV_MAGICCONST', 'RECIP_BPF', 'Random', 'SG_MAGICCONST', 'SystemRandom', 'TWOPI', '_ONE', '_Sequence', '_Set', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_accumulate', '_acos', '_bisect', '_ceil', '_cos', '_e', '_exp', '_floor', '_index', '_inst', '_isfinite', '_log', '_os', '_pi', '_random', '_repeat', '_sha512', '_sin', '_sqrt', '_test', '_test_generator', '_urandom', '_warn', 'betavariate', 'choice', 'choices', 'expovariate', 'gammavariate', 'gauss', 'getrandbits', 'getstate', 'lognormvariate', 'normalvariate', 'paretovariate', 'randbytes', 'randint', 'random', 'randrange', 'sample', 'seed', 'setstate', 'shuffle', 'triangular', 'uniform', 'vonmisesvariate', 'weibullvariate']
'''

lst = [1, 2, 3]
# print(dir(lst)) # 내장함수 list내에서 쓸 수 있는 객체 표시
'''['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']'''

name = "Jim"
# print(dir(name)) # name에 대해서 실행할 수 있는 명령 출력
'''['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']'''

# list of python builtins 검색하면 내장함수 목록 확인 가능


### 외장함수
# list of python modules 파이썬 외장함수 목록 확인 가능

# glob : 경로 내의 폴더 / 파일 목록 조회 (윈도우 dir)
import glob
# print(glob.glob("*.py"))    # 확장자가 py인 모든 파일
'''['1152_number_of_words.py', '2231_dec_sum.py', '7568_bulky.py', 'unit_test.py']'''

# os : 운영체제에서 제공하는 기본 기능
import os
# print(os.getcwd()) # 현재 디렉토리
'''D:\source\repos\Algorithm\python'''

folder = "sample_dir"

# if os.path.exists(folder):
#     print("이미 존재하는 폴더입니다.")
#     os.rmdir(folder)
#     print(folder, "폴더를 삭제하였습니다.")
#     '''
#     이미 존재하는 폴더입니다.
#     sample_dir 폴더를 삭제하였습니다.
#     '''
# else:
#     os.makedirs(folder) # 폴더 생성
#     print(folder, "폴더를 생성하였습니다.")
#     '''sample_dir 폴더를 생성하였습니다.'''

# print(os.listdir())
'''['1152_number_of_words.py', '2231_dec_sum.py', '3003_chess', '7568_bulky.py', 'practice', 'profile.pickle', 'sample_dir', 'score.txt', 'study.txt', 'unit_test.py']'''

# time : 시간 관련 함수
import time
print(time.localtime())
'''time.struct_time(tm_year=2022, tm_mon=8, tm_mday=16, tm_hour=23, tm_min=31, tm_sec=3, tm_wday=1, tm_yday=228, tm_isdst=0)'''
print(time.strftime("%Y-%m-%d %H-%M-%S"))
'''2022-08-16 23-31-30'''

import datetime
print("오늘 날짜는 ", datetime.date.today())
'''오늘 날짜는  2022-08-16'''

# timedelta : 두 날짜 사이의 간격
today = datetime.date.today()               # 오늘 날짜 저장
td = datetime.timedelta(days=100)           # 100일 저장
print("우리가 만난지 100일은 ", today + td)  # 오늘부터 100일 후
'''우리가 만난지 100일은  2022-11-24'''