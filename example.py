from sexyNy64 import sexyNY64

#example.py
섹시 = sexyNY64()

result = 섹시.make(int(input("ID : ")))
print(f"Generated Word: {result}")

authenticated = 섹시.check(id=int(input("ID : ")), word=input("섹시한 단어를 입력하세요 : "))
if authenticated:
    print("Authentication Successful. Data has been removed.")
else:
    print("Authentication Failed.")
