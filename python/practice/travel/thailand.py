class ThailandPackage:
    def detail(self):
        print("[태국 패키지 3박 5일] 방콕, 파타야 여행 (야시장 투어) 50만원")

# 모듈 직접 실행
# name이 main이면 모듈파일에서 직접 실행
if __name__ == "__main__":                
    print("Thailand 모듈을 직접 실행")
    print("이 문장은 모듈을 직접 실행할 때만 실행돼요")
    trip_to = ThailandPackage()
    trip_to.detail()
else:
    print("Thailand 외부에서 모듈 호출")

'''
이 페이지에서 실행
Thailand 모듈을 직접 실행
이 문장은 모듈을 직접 실행할 때만 실행돼요

practice10_1.py에서 실행
Thailand 외부에서 모듈 호출
'''