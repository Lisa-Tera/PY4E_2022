'''
📌Q1. 우리는 큰 수를 나타낼 때 3자리마다 , 를 찍어서 구분해 줍니다. 파이썬에서는 아래와 같이 쉽게 나타낼 수 있습니다.

# f"{숫자:,}"
print(f"{1000:,}")

하지만 이번 미션에서는 숫자를 입력 받고 3자리마다 ,를 찍어주는

함수를 만들어 봅시다.


🔽출력 예시

make_comma(1000000)
1,000,000


if type(num) is float :
    print(1)

'''
#def make_comma(num):
#    print(format(num, ','))


num = 1123456789.567

#실수형인지 정수형인지 모르기 때문에 
num_str = str(num).split('.')
int_n = num_str[0] 
comma = len(int_n)//3 
new_num= int_n[len(int_n)-3:]

if len(int_n) > 3: new_num = ',' + new_num

#0~5 0123456

for i in range(len(int_n)-4,-1,-1):
    a = int_n[i]
    new_num = int_n[i] + new_num
    if  ==0: new_num = ','+new_num            
new_num = int_n[0]+ new_num
'''
while comma !=0 : 
    new_num = int_n[n] + new_num
    
        
        comma -=1
    n-=1

#else : return num
   ''' 

