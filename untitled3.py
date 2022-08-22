import random 
 
numbers = list() 
used = list() 
right = 0 
# 시도 횟수를 매개변수로 받아서 수행 
def guess_number(cnt): 
    print(cnt, "차 시도") 
    # 오류가 발생할 경우 함수 재호출 
    try: 
        num = int(input("숫자를 예측해보세요 : ")) 
        # 이미 사용된 번호를 입력한 경우 
        if num in used: 
            print("이미 예측에 사용한 숫자입니다") 
        # 틀린경우 
        elif num not in numbers: 
            if cnt == 5 or cnt == 10: 
                print(num, "는 없습니다.") 
                if num < numbers[0]: print("최솟값은 ", num, "보다 큽니다") 
                elif num > numbers[2]: print("최댓값은 ", num, "보다 작습니다") 
                else: print("최솟값은 ", num, "보다 작습니다") 
        # 숫자를 맞춘경우 
        else: 
            right += 1 
            if num == numbers[0]: 
                print("숫자를 맞추셨습니다! ", num, "는 최솟값입니다.") 
            elif num == numbers[1]: 
                print("숫자를 맞추셨습니다! ", num, "는 중간값입니다.") 
            else: 
                print("숫자를 맞추셨습니다! ", num, "는 최댓값입니다.") 
            print(cnt, "번 시도만에 예측 성공") 
         
        if right == 3: 
          print("게임종료") 
          return 
        used.append(num) 
        guess_number(cnt+1) 
    except: 
        guess_number(cnt) 
    return 
 
# 3가지 다른 숫자를 numbers에 저장 
while True: 
    if len(numbers) == 3: 
        break 
    number = random.randint(0, 100) 
    if number not in numbers: 
        numbers.append(number) 
# 오름차순으로 정렬 
numbers.sort 
 
guess_number(1)
