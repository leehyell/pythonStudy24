#management
import datetime as t

# 월 매출을 파일에서 읽어와서 딕셔너리 형태로 저장한 다음 반환
def month_margin(month,day_sale):
    tmp_dic = {}
    tmp_month = {}
    try:
        f = open("관리/"+month+"-total.txt",'r')
        while True :
            line = f.readline()
            if line == '':
                break
            line = line.rstrip('\n')
            tmp_list = line.split('/')
            tmp_month[tmp_list[0]] = int(tmp_list[1])
        tmp_dic[month] = tmp_month
    #파일이 없을 때 예외처리
    except FileNotFoundError:
        print("재고 관리 파일이 없습니다.\n재고 파일을 만듭니다.")
        f = open("관리/"+month+"-total.txt","w")
        for i in day_sale.keys():
            f.write("{}/{}\n".format(i,day_sale[i]))
        f.close()

    return tmp_dic

# 받아온 day_sale 딕셔너리를 이용하여 일매출을 화면에 출력
# 월매출 딕셔너리를 반환 받아서 화면에 출력
def main(goods,day_sale):
    now = t.datetime.now()
    month = now.month
    day = now.day
    if month < 10:
        month = '0'+str(month)
    else:
        month = str(month)
    if day < 10:
        day = '0'+str(day)
    else:
        day = str(day)
    while True:
        try:
            s_num = int(input("1. 일 매출 / 2. 월 매출 / 5. 종료 : "))
            print("="*30,end="\n")
        except:
            continue
        if s_num == 1:
            print("일  매  출")
            print("="*30)
            for i in day_sale.keys():
                if i == 'card' or i == 'cash':
                    continue
                else:
                    print("{}. {} : {}".format(i,goods[i]['품목'],day_sale[i]))
            print("="*30,end="\n")
            print("{} : {}\n{} : {}\n".format('card',day_sale['card'],'cash',day_sale['cash']))
            print("="*30,end="\n")
            print()
        elif s_num == 2:
            dic = month_margin(month,day_sale)
            tmp_dic = dic[month]
            print("월  매  출")
            print("="*30)
            for i in tmp_dic.keys():
                if i == 'card' or i == 'cash':
                    continue
                else:
                    print("{}. {} : {}".format(i,goods[i]['품목'],tmp_dic[i]))
            print("="*30,end="\n")
            print("{} : {}\n{} : {}\n".format('card',tmp_dic['card'],'cash',tmp_dic['cash']))
            print("="*30,end="\n")
            print()
        elif s_num == 5:
            break
        else:
            print("="*30) 
            print("다시 입력하세요")
            print("="*30,end="\n")
            print()