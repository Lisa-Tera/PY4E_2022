#3. 2개의 숫자를 입력하여 그 사이에 짝수만 출력하는 함수를 만들어 봅시다. 그리고 중앙값도 함께 출력 해봅시다.(단, 중앙값이 짝수가 아닐 경우에는 중앙값은 출력을 하지 않고, 짝수인 수만 출력한다)
#중앙값: 정중앙에 있는 값
#특정 두 숫자 사이의 수들을 리스트로 만드는 법
import statistics

while True :
    try : 
        n = int(input("첫 번째 수 입력 : "))
        m = int(input("두 번째 수 입력 : "))
        break
    except: 
        print("숫자를 다시 입력하세요")
nums = [ i for i in range(n,m+1)]
mid = statistics.median(nums) 
even = [i for i in nums if i%2 ==0 ]

for i in even :
    print(i,"짝수")
    if i ==mid :
        print(i,"중앙값")




'''    
#2
num,even=[],[]
for i in range(n,1+m):
    num.append(i)
    if i%2 ==0 :
        even.append(i)
        print(i,"짝수")
        if i ==mid :
            print(i,"중앙값")

#3     
for i in range(n,1+m):  
    if i%2 ==0 :
        print(i,"짝수")
        if i ==mid :
            print(i,"중앙값")
'''

