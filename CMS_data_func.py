import re

def cust_input(cust_list, page):
    print("고객 정보 입력 로직")
    customer = {"name": "", "gender": "", "email": "", "birthyear": ""}
    while True:
        regex = re.compile("[a-zA-Z|가-힣]")
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
        email_check = re.compile('^[a-zA-Z][a-zA-Z0-9]{4,10}@[a-zA-Z]{2,6}[.][a-zA-Z]{2,4}$')
        # ^[a-zA-Z0-9+-_.]+@[a-zA-Z]+.[a-zA-Z]+$
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
    return cust_list, page


def update_cust(cust_list, page):
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
    return cust_list, page

def del_cust(cust_list, page):
    print("고객 정보 삭제")
    del cust_list[page]
    page = len(cust_list)-1
    return page