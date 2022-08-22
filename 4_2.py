
"""
Q2. 어느날 여러분이 어떤 글을 읽고 있는데, 갑자기 특정 글자가 전체 글에서 몇개 들어있는지 궁금해졌습니다. 그럼 한 번 파이썬 함수로 만들어 봅시다.


글은 어떤 글이 좋습니다. 인터넷에서 검색해서 복사 붙여넣기로 변수에 넣어 줍니다.

변수에 담긴 글을 함수에 넣어주면 txt 파일로 저장도 함께 되도록 해줍니다.


 count_word(a, ":")

🔽출력 예시
"""

def file_store(data):
    file = open('lyrics.txt', 'w')
    file.write(data)               
    file.close() 
a ="""Remember me
Though I have to say goodbye
Remember me
Don't let it make you cry

For even if I'm far away
I hold you in my heart
I sing a secret song to you
Each night we are apart

Remember me
Though I have to travel far
Remember me
Each time you hear a sad guitar

Know that I'm with you
The only way that I can be
Until you're in my arms again

Remember me"""

file_store(a)
with open('lyrics.txt', 'r') as f:
    
    data = f.readlines()
    count =0 
    for line in data: 
        count += line.count('me')
        #if line.find('Remember me') >0:       
         #   count += line.find('Remember me')
print(count)
