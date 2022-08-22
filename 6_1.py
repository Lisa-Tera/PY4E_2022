king_dict = dict()
counts =list()
#조건 중복되는 왕  + 총 명 수 
korea_king = "태조,혜종,정종,광종,경종,성종,목종,현종,덕종,정종,문종,순종,선종,헌종,숙종,예종,인종,의종,명종,신종,희종,강종,고종,원조,충렬왕,충선왕,충숙왕,충혜왕,충목왕,충정왕,공민왕,우왕,창왕,공양왕"
chosun_king = "태조,정종,태종,세종,문종,단종,세조,예종,성종,연산군,중종,인종,명종,선조,광해군,인조,효종,현종,숙종,경종,영조,정조,순조,헌종,철종,고종,순종"
#주의 : 고려는 중복되는 왕이 있음


for king in (korea :=korea_king.split(',')):
    king_dict[king] = 1


for king in (cho:=set(chosun_king.split(','))):
    king_dict[king] = king_dict.get(king,0) + 1 

     
for (k,v) in king_dict.items():
    if v ==2: 
        counts.append(k)
        print(f"조선과 고려에 모두 있는 왕 이름 : {k}")
print(f"조선과 고려에 모두 있는 왕 이름은 총 {len(counts)}개 입니다")

     