#Q4. 2개의 숫자를 입력하여 그 사이에 소수가 몇 개인지 출력하는 함수를 만들어 봅시다.
#소수: 1과 자기 자신만을 약수로 가지는 수
def prime_num(n): #소수 만드는 함수
    for i in range(2,n):
        if n % i == 0 :
            return 0
    return 1


n = int(input("첫 번째 수 입력 : "))
m = int(input("두 번째 수 입력 : "))
#count_prime_number(n, m)


prime = [] #소수 2,3,5
for i in range(n,m):
    if prime_num(i): 
        prime.append(i)

print("소수는 ", len(prime),"개")


