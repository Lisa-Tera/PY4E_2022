
import random
def rcp(my, com):
    #inputs = ((0,'가위'),(1,'바위'), (2,'보'))
    input_num = ['0','1','2']
    input_str = ['가위','바위','보']
    results = ['무승부','패배','승리']
    if my in input_num: 
        print("나 :",input_str[int(my)])
        print("컴퓨터:",input_str[com])
        return results[com-int(my)]
    elif my in input_str : 
        for i in input_num:
            if my ==input_str[int(i)] :
                 print("나 :",my)
                 print("컴퓨터:",input_str[com])
                 return results[com- int(i)]
    

    else :
        print ("잘못된 값이 입력되었습니다")
        return False
    
    
 
    

while True:       
    try: 
        games = int(input("몇 판을 진행하시겠습니까? : "))
        if games > 0:
            i=0
            while i < games :    
                my =input("0:가위, 1:바위, 2:보 ")
                cp =random.randint(0, 2)          
                print("가위바위보:",i)       
                a=rcp(my,cp)
                print(i,"번째 판 나의", a)
                i+=1
            #rsp_advanced(games)   
            break
    except: 
        print(" 다시 입력해주세요")
        
