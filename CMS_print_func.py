def cust_menu():
    return input("""
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

def cur_cust(cust_list, page):
    print("현재 고객 정보 출력")
    if page >= 0:
        print(cust_list[page])
    else:
        print("입력된 정보가 없습니다.")
    return page

def prev_cust(cust_list, page):
    print("이전 고객 정보 출력")
    if page <= 0 or len(cust_list) == 0:
        print("첫 번째 페이지 입니다.")
    else:
        page = page - 1 
        print(cust_list[page])
    return page

def next_cust(cust_list, page):
    print("다음 고객 정보 출력")
    if page >= len(cust_list)-1:
        print("마지막 번째 페이지 입니다.")
    else:
        page = page + 1
        print(cust_list[page])
    return page

