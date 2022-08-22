import statistics

# 보너스 실적 1,2위인데 평균실적이 5보다 크지 않으면 불가
#면담 실적 5,6위 인데 평균 실적이 <3 인 경우

def sales_management(member_names, member_records) :
    member_dic = dict(zip(member_names, member_records)) #이름하고 리스트를 딕셔너리로 합치자
    
    mem_work =dict() #평균 실적 딕셔너리

    for k,v in member_dic.items():
        mem_work[round(statistics.mean(v),1)]=k #value를 숫자로 하면 정렬이 힘들어서 key에 숫자/ value에는 이름
    
    i=0 # 0순위부터 시작
    bonus,fire = [],[] #보너스 대상자/ 면접 대상자
    for k, v in (mem_work := sorted(mem_work.items(), reverse=True)):# 실적 높은 순으로 정렬 
        #1,2등 & 평균실적 >5
        if i <=1 and k >5: bonus.append(v)
        #5,6등 & 평균실적 <3
        elif i >=4 and k <3 :fire.append(v)
        i+=1

    return bonus,fire


member_names = ["갑돌이", "갑순이", "을돌이", "을순이", "병돌이", "병순이"]
member_records = [[4,5,3,5,6,5,3,4,1,3,4,5],[2,3,4,3,1,2,0,3,2,5,7,2], 
           [1,3,0,3,3,4,5,6,7,2,2,1],[3,2,9,2,3,5,6,6,4,6,9,9],
           [8,7,7,5,6,7,5,8,8,6,10,9],[7,8,4,9,5,10,3,3,2,2,1,3]]

b,f = sales_management(member_names, member_records)


[print(f"보너스 대상자 : {i}") for i in b]# 몇 사람인지 모르므로 for문 사용
[print(f"면담 대상자 : {i}") for i in f]