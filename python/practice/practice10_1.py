### 패키지

# 모듈이나 패키지만 import 가능 (class는 불가)
# import travel.thailand
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()
'''[태국 패키지 3박 5일] 방콕, 파타야 여행 (야시장 투어) 50만원'''

# from ~ import 구문에서는 class도 import가능
# from travel.thailand import ThailandPackage
# trip_to = ThailandPackage()
# trip_to.detail()
'''[태국 패키지 3박 5일] 방콕, 파타야 여행 (야시장 투어) 50만원'''

# from travel import vietnam
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()
'''[베트남 패키지 3박 5일] 다낭 효도 여행 60만원'''

from travel import *
# # __init__에서 공개범위 지정
# # trip_to = vietnam.VietnamPackage()
trip_to = thailand.ThailandPackage()
trip_to.detail()

import inspect
import random
print(inspect.getfile(random))
print(inspect.getfile(thailand))    # python310/lib/travel/thailand.py에 가져다두면 전체적으로 사용 가능