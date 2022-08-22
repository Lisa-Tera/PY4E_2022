s = ["김갑,3242524215",
"이을,3242524223",
"박병,2242554131",
"최정,4245242315",
"정무,3242524315"]

a = [3,2,4,2,5,2,4,3,1,2]

#점수 계산 함수 student_calculator
def s_cal(a,s):
    # 학생들의 data를 딕셔너리를 만들어 이용하자
    data_dic ={}

    for i in s:
        dic = i.split(',')  #이름하고 답안하고 쪼개기
        stu_num = list(map(int,dic[1])) #답안 숫자로 변경
        sum=0 #으로 총점 계산
        for j in range(len(a)): #정답지랑 개인 답안이랑 비교
            if stu_num[j]== a[j]: sum+=1
        data_dic[dic[0]] = sum*10 #이름하고 점수 담긴 딕셔너리 생성
    #점수 순으로 정렬 ...딕셔너리로 저장할 수 없고 리스트로만 가능...   
    data = sorted(data_dic.items(), key=lambda x: x[1], reverse=True)
    return data


#for i in range(len(data:=s_cal(a,s))): #바다코끼리
#    print(f"학생: {data[i][0]} 점수: {data[i][1]}점 {i+1}등")
for rank,i in enumerate(data:=s_cal(a,s)): #바다코끼리
    print(f"학생: {i[0]} 점수: {i[1]}점 {rank+1}등")
    