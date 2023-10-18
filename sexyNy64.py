import random
import json

class sexyNY64():
    def make(self, id:int):
        # 입력 숫자
        input_number = id

        # 리스트 1과 리스트 2 (여기에 자신의 실제 데이터를 대입하십시오)
        list_1 = ["귀여운", "멋진", "이쁜", "아름다운", "똑똑한", "음주하는", "키가 작은", "키가 큰", "비행하는", "슬픈", "기쁜", "외로운", "재밌는", "신나는", "허졉한", "배부른", "망상하는", "히키코모리", "샌즈한", "대화하는", "웃긴", "말랑한"]
        list_2 = ["남냥", "프젝", "프이", "뉴비", "머핀", "어린이", "바게트", "참새", "라면", "생수", "정수기", "샌즈", "고양이", "리트리버", "강아지"]

        # 리스트 1과 리스트 2에서 무작위로 항목 선택
        random_item_1 = random.choice(list_1)
        random_item_2 = random.choice(list_2)

        if random_item_1 == "음주하는" and random_item_2 != "프젝":
            random_item_2 = "프젝"

        # JSON 데이터 생성
        data = {
            "input_number": input_number,
            "word": f"{random_item_1} {random_item_2}"
        }

        # JSON 파일로 저장
        with open('data.json', 'w') as json_file:
            json.dump(data, json_file)

        return f"{random_item_1} {random_item_2}"

    def check(self, id:int, word:str):
        input_number = id

        # JSON 파일에서 데이터 불러오기
        with open('data.json', 'r') as json_file:
            data = json.load(json_file)

        if (data["input_number"] == input_number and data["word"] == word):
            # 인증이 성공하면 JSON 파일에서 해당 데이터만 제거
            with open('data.json', 'w') as json_file:
                data = {}
                json.dump(data, json_file)
            return True
        else:
            return False
