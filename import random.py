import random
class lotto
    def __init__(self):
        number = input(f'{}번째 숫자를 입력해주세요.'.format)
        #number= input("띄어쓰기로 6개 입력 :").split(" ")
        mine = []
        for n in number:
            mine.append(int(n))


        pass\
    
   # number = {
  "첫번째 입력숫자":value1,
  "두번째 입력숫자":value2,
  "세번째 입력숫자":value3,
  "네번째 입력숫자":value4,
  "다섯번째 입력숫자":value5,
  "여섯번째 입력숫자":value6,
}

 

    def lottery():
        alist = []   # 뽑은 a를 넣어 중복 방지해주는 리스트     
        for i in range(6) # 6번 뽑는다
            a = random.randint(1,45)
            while a in alist :              # a가 이미 뽑은 리스트에 있을 때까지 다시 뽑자
                a = random.randint(1,45)
    alist.append(a) # 새로운 a 값을 리스트에 추가
            print(a)
        return alist
    lottery.sort()
    print(f'{lottery}')

  # a = random.sample(range(1,101),10) # 1부터 100까지의 범위중에 10개를 중복없이 뽑겠다.

