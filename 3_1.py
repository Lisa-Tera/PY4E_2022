
#๐Q1. ์ซ์๋ฅผ ์๋ ฅ ๋ฐ๊ณ  ๊ทธ ์ซ์์ ๊ตฌ๊ตฌ๋จ์ ์ถ๋ ฅํ๋ ํจ์๋ฅผ ๋ง๋ค์ด ๋ด์๋ค. ๋ค๋ง ์๋์ ์กฐ๊ฑด์ ๋ง์กฑํด ์ฃผ์ธ์.
#์กฐ๊ฑด 1: ํ ์ ๋ฒ์งธ๋ง ์ถ๋ ฅํ๊ธฐ
#์กฐ๊ฑด 2: ๊ฐ์ด 50์ดํ์ธ ๊ฒ๋ง ์ถ๋ ฅํ๊ธฐ

def gugudan(num):
	i=1
	while True:
		gugu = number *i
		if gugu > 50:
			break
		print(number , "X" , i ,"=", gugu)
		i += 2 

    
while True:       
    number = input("๋ช ๋จ? : ")
    try: 
        if (number := int(number)) > 0:
        
            print(number,"๋จ")
            gugudan(number)    
            break
    except: print("์์๋ก ๋ค์ ์๋ ฅํด์ฃผ์ธ์")
        



    






