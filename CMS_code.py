import os
import pickle
import re

cust_list = []
page = -1

if os.path.exists("./CMS_code_test_data/cust_data.pkl"):
    with open("./CMS_code_test_data/cust_data.pkl", "rb") as f:
        cust_list = pickle.load(f)
        print("현재 시스템에 저장되어있는 고객 정보")
        for i in cust_list:
            print(i)    
    page = len(cust_list) - 1
else:
    page = -1

while True:
    choice = input("""
    #####################################
    다음 중 작업 하실 메뉴를 입력 하세요.
    I - 고객 정보 입력
    C - 현재 고객 정보 출력
    P - 이전 고객 정보 출력
    N - 다음 고객 정보 출력
    U - 고객 정보 수정
    D - 고객 정보 삭제
    S - 데이타 저장
    Q - 프로그램 종료
    #####################################
    입력 : """).strip().upper()

    if choice == "I": 
        print("고객 정보 입력 로직")
        customer = {"name": "", "gender": "", "email": "", "birthyear": ""}
        while True:
            regex = re.compile("[a-z|A-Z|ㄱ-ㅎ|ㅏ-ㅣ|가-힣]")
            name = input("이름을 입력 하세요 : ")
            if regex.search(name):
                break
            else :
                print("한글 또는 영어만 사용해서 입력하세요.")
        while True:
            gender = input("성별(M/F)을 입력 하세요 : ").upper()
            if gender in ("M", "F"):
                break
            else :
                print("M 과 F 중에 입력하세요.")

        while True:
            email = input("이메일 주소를 입력 하세요 : ")
            email_check = re.compile('^[a-zA-Z0-9+-_.]+@[a-zA-Z]+.[a-zA-Z]+$')
            if email_check.search(email):
                break
            else :
                print("올바른 이메일 양식으로 입력하세요 (ex. example@example.com)")
            #if email.find("@") > -1:  # True, False 0 == False, -2 == True
            #    break
        
        while True:
            birth_check = re.compile('^[0-9]{4}$')
            birthyear = input("출생 년도 4자리를 입력 하세요 : ")
            if birth_check.search(birthyear):
                break

        customer["name"] = name
        customer["gender"] = gender
        customer["email"] = email
        customer["birthyear"] = birthyear
        cust_list.append(customer)

        page = len(cust_list)-1

    elif choice == "C":
        print("현재 고객 정보 출력")
        if page >= 0:
            print(cust_list[page])
        else:
            print("입력된 정보가 없습니다.")

    elif choice == "P":
        print("이전 고객 정보 출력")
        if page <= 0 or len(cust_list) == 0:
            print("첫 번째 페이지 입니다.")
        else:
            page = page - 1 
            print(cust_list[page])

    elif choice == "N":
        print("다음 고객 정보 출력")
        if page >= len(cust_list)-1:
            print("마지막 번째 페이지 입니다.")
        else:
            page = page + 1
            print(cust_list[page])

    elif choice == "U":
        while True:
            choice1 = input("수정하고 싶은 고객 정보의 이름을 입력하세요 : ")
            idx = -1
            for i, val in enumerate(cust_list):
                if val["name"] == choice1.strip():
                    idx = i
                    break
            if idx == -1:
                print("등록되지 않은 이름입니다.")
                break

            choice1 = input("""수정하고싶은 항목을 입력하세요
            name, gender, email, birthyer, cancel
            """)
            if choice1 in ("name", "gender", "email", "birthyear"):
                cust_list[idx][choice1] = input(
                    "수정할 {}을 입력 하세요. ".format(choice1))
                break
            elif choice1 == "cancel":
                break
            else:
                print("존재하지 않는 항목입니다.")
                break
    elif choice == "D":
        print("고객 정보 삭제")
        del cust_list[page]
        page = len(cust_list)-1 
    elif choice == "S":
        with open("./CMS_code_test_data/cust_data.pkl", "wb") as f:
            pickle.dump(cust_list, f)
            print("저장 되었습니다.")
    elif choice == "Q":
        print("프로그램을 종료합니다.")
        break
    else:
        print("메뉴를 잘못입력했습니다.")
