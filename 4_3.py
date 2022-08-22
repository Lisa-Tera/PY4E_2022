#조건 010으로 시작/ -로 구분 / 총 13

def file_store(data):#txt저장 함수
    file = open('phonenum.txt', 'w')
    file.write(data)         
    file.close() 

def wrong_guest(guest):
    # 리스트로 만들어서 쪼개자
    data_list = guest.split('\n')
    #알맞게 들어간 데이터와 잘못된 데이터를 딕셔너리로 구분
    data_dic,wrong ={},{}
    for i in data_list:
        dic = i.split(',')
        if len(dic[1]) ==13 and dic[1][:4]=='010-' and dic[1][8] == '-':
            data_dic[dic[0]] =dic[1]
        else : 
            wrong[dic[0]] =dic[1]    
    
    
    return wrong

guest ="""김갑,123456789
이을,010-1234-5678
박병,010-5678-111
최정,111-1111-1111
정무,010-3333-3333"""
#txt파일 저장
file_store(guest)


a = wrong_guest(guest)
for i in a:
    print("잘못 쓴 사람: ",i)
    print(f"잘못 쓴 번호: {a[i]} \n")
    







