import random
num_list,user_list =[],[]
while len(total :=sorted(set(num_list))) <3:#set으로 중복 제거 후 정렬
    num = random.randint(0, 100) #중복 없이 숫자 3개 
    num_list.append(num) #리스트에 추가
    #num_list=[1,1,4]
    
    
num_dict = dict(zip(total, ["최솟값", "중간값","최대값"] ))


count=1
#횟수제한 조건이 없어서 무한루프 사용
while True:
    print(count,"차 시도")
    user = int(input("숫자를 예측해보세요 : "))
    
    if user in num_dict: #값이 맞은 경우
        print(f"숫자를 맞추셨습니다! {user}은 {num_dict.get(user)}입니다.")
        del num_dict[user] #key를 삭제해서 모두 제거 시 종료
        if num_dict == {}: 
            print( f"게임종료\n{count}번 시도만에 예측 성공")
            break
    
    

    else :  
        if user in user_list:print("이미 예측에 사용한 숫자입니다") 
        else :
            print(f"{user}은 없습니다.")        
            user_list.append(user)    
        if (count == 5 or count == 10): #!!!최솟값이나 최대값을 이미 찾았고 중앙값을 찾아야한다면 의미가 없는 힌트 AND 만약 min =0 max =100인데 사용자가 50을 쓴다면 조건이 애매함.. !!!!!!!!!
            if  total[0] < user : print(f"최솟값은 {user}보다 작습니다")
            elif total[2] > user : print(f"최대값은 {user}보다 큽니다")
    count +=1
        
