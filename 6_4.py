# 8회 이상/ 전화번호가 있는회원만 없다면 000-0000-0000으로 출력\

# 6명의 회원이고 "아이디,나이,전화번호,성별,지역,구매횟수" 순서로 입력되어 있음
info = "abc,21세,010-1234-5678,남자,서울,5,cdb,25세,x,남자,서울,4,bbc,30세,010-2222-3333,여자,서울,3,ccb,29세,x,여자,경기,9,dab,26세,x,남자,인천,8,aab,23세,010-3333-1111,여자,경기,10"
#0,1,2,3,4,5
#6,7,8,9,10,11
#12



customer = dict()
vip = []
info_list =info.split(',')
total = "아이디,나이,전화번호,성별,지역,구매횟수".split(',')
customer_list=[info_list[i*6:(i+1)*6] for i in range(6)]

for i in customer_list:
    if i[2][:3] =='010' and int(i[5]) >=8 :
        vip.append(i)
    if i[2] =='x': i[2] ='000-0000-0000'
    
for t in total :
    for v in vip:
        customer[t] = v


'''
i=0
vip = []
total = "아이디,나이,전화번호,성별,지역,구매횟수".split(',')
for t in total:
    data = []
    for j in range(6):
        d =info_list[j*6+ i]
        if t =="전화번호" and d =="x":  d = "000-0000-0000"
        if t == "구매횟수" and int(d) >=8 : vip.append(j)
        data.append(d)
    customer[t] = data
    i+=1

for v in customer["구매횟수"]:
    if int(v) >=8 : vip.append(v)
    print(v)
'''
    




a=1