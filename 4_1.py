'''
πQ1. μ°λ¦¬λ ν° μλ₯Ό λνλΌ λ 3μλ¦¬λ§λ€ , λ₯Ό μ°μ΄μ κ΅¬λΆν΄ μ€λλ€. νμ΄μ¬μμλ μλμ κ°μ΄ μ½κ² λνλΌ μ μμ΅λλ€.

# f"{μ«μ:,}"
print(f"{1000:,}")

νμ§λ§ μ΄λ² λ―Έμμμλ μ«μλ₯Ό μλ ₯ λ°κ³  3μλ¦¬λ§λ€ ,λ₯Ό μ°μ΄μ£Όλ

ν¨μλ₯Ό λ§λ€μ΄ λ΄μλ€.


π½μΆλ ₯ μμ

make_comma(1000000)
1,000,000


if type(num) is float :
    print(1)

'''
#def make_comma(num):
#    print(format(num, ','))


num = 1123456789.567

#μ€μνμΈμ§ μ μνμΈμ§ λͺ¨λ₯΄κΈ° λλ¬Έμ 
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

