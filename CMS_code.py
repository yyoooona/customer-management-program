import os
import pickle
import CMS_data_func as df
import CMS_print_func as pf

def main():
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
        choice = pf.cust_menu()

        if choice == "I": 
            cust_list, page = df.cust_input(cust_list, page)
        elif choice == "C":
            page = pf.cur_cust(cust_list, page)
        elif choice == "P":
            page = pf.prev_cust(cust_list, page)
        elif choice == "N":
            page = pf.next_cust(cust_list, page)
        elif choice == "U":
            cust_list, page = df.update_cust(cust_list, page)
        elif choice == "D":
            page = df.del_cust(cust_list, page)
        elif choice == "S":
            with open("./CMS_code_test_data/cust_data.pkl", "wb") as f:
                pickle.dump(cust_list, f)
                print("저장 되었습니다.")
        elif choice == "Q":
            print("프로그램을 종료합니다.")
            break
        else:
            print("메뉴를 잘못입력했습니다.")

if __name__ == "__main__":
    main()