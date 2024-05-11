from get_date_diff import get_date_diff
from datetime import date

if __name__ == "__main__":
    # input pages amount
    while True:
        try:
            pages = int(input("how many pages you to do : "))
            break
        except:
            print("다시 입력해주세용")

    while True:
        date_diff = get_date_diff(date.today().strftime("%m"), date.today().strftime("%d"))
        amount = pages/date_diff
        print("{}pages".format(amount))

