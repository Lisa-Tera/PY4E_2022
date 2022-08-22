import statistics
#종목과 수익률만 출력
#종목별 수익률이 높은 순서대로 출력해주세요. (소수 둘째자리까지 출력)


#주식 수익률: (평가금액 - 투자원금)/ 투자원금 *100(%)
#(sell*stock[1] -  stock[1]*stock[2]) / (stock[1]*stock[2]) *100
stocks = "삼성전자/10/85000,카카오/15/130000,LG화학/3/820000,NAVER/5/420000"
sells = [82000, 160000, 835000, 410000]
# -3만 45만 4만5천  - 5만

stock = dict() #삼전:[10, 85000, 82000]로 저장
stock_ord = stocks.split(',')
for i in range(4) :
    total = stock_ord[i].split('/')
    total.append(sells[i])
    stock[total[0]] = list(map(int,total[1:]))#숫자로 저장

stock_income = dict()#수입
for k,v in stock.items():
    stock_income[(v[2]-v[1])/v[1]*100] =k #수익률을 key로 정의


for k, v in (stock_income := sorted(stock_income.items(), reverse=True)):# 실적 높은 순으로 정렬 
    print(f"{v}의 수익률 {k:.3}")


#[2]*[0] -[1][0] / [1][0]
#items = "종목명,보유수량,매수금액,매도금액".split(',')

'''
stock_ord,stock_sell = dict(),dict()
for i in stocks.split(','):
    a = i.split('/')
    stock_ord[a[0]] = a[1:] 

for i in range(len(sells)):

'''


