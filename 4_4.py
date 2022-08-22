#주민등록번호를 입력하면 몇년 몇월 생인지 그리고 남자인지 여자인지 출력
#-포함 14 / 00~21로 시작 시 00년생 이후일 때 남 3 여 4  그 전인 경우 남 1 여 2

def check_id(a):
    #생년/ 월 리스트로 저장
    id_list = [a[:2],a[2:4]]
    if len(a) == 14 and a[6] == "-":
        
        if int(a[:2]) < 22 :
            zero = input("2000년 이후 출생자 입니까? 맞으면 o 아니면 x : ")
            if zero =="o" :
                if a[7] =="3" : id_list.append("남자")
                elif a[7] == "4":id_list.append("여자")
                else : return "Error"
            else :return "Error"
        else :
            if a[7]=="1" : id_list.append("남자")
            elif a[7] == "2":id_list.append("여자")
            else: return "Error"
        return id_list
    else : return "Error"   


a = "000629-2222222"
#check_id(a)
#50년06월 여자


a = input("주민등록번호를 입력하세요: ")

check =check_id(a)
if check =="Error" :print("잘못된 번호입니다.\n올바른 번호를 넣어주세요")
else : print(f"{check[0]}년 {check[1]}월 {check[2]}")
