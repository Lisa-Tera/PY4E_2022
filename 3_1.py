
#📌Q1. 숫자를 입력 받고 그 숫자의 구구단을 출력하는 함수를 만들어 봅시다. 다만 아래의 조건을 만족해 주세요.
#조건 1: 홀 수 번째만 출력하기
#조건 2: 값이 50이하인 것만 출력하기

def gugudan(num):
	i=1
	while True:
		gugu = number *i
		if gugu > 50:
			break
		print(number , "X" , i ,"=", gugu)
		i += 2 

    
while True:       
    number = input("몇 단? : ")
    try: 
        if (number := int(number)) > 0:
        
            print(number,"단")
            gugudan(number)    
            break
    except: print("양수로 다시 입력해주세요")
        



    






