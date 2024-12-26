import pay
import update
import management
import gmanagement
import ep
import datetime as t

#재고 및 물품 정보를 텍스트 파일에서 읽기
# goods , day_sale 딕셔너리 생성
#재고 디렉터리 속 goods.txt 읽기모드로 불러오기
f = open("재고/goods.txt","r")
# 물품 정보 및 재고 저장
goods ={}
# 일 매출 정보 저장
day_sale = {"card":0, "cash":0}

def today():
    #오늘 날짜
    now = t.datetime.now()
    #오늘 날짜 출력
    print(now)
    print("="*30,end="\n")

today()
while True :
    #tmp_dic 변수
    tmp_dic = {}
    #line 변수에 파일 한 줄씩 읽어오기
    line = f.readline()
    #line 변수 속 \n(엔터) 제거
    line = line.rstrip("\n");
    #line이 빈 값이면 빠져나와라
    if line=="":
        break
    #line 변수에 있는 데이터들을 /로 나눠서 st_list에 배열 저장
    st_list = line.split("/")
    #tmp_dic['분류'] 변수에 st_list 1번째 index 값 저장
    tmp_dic["분류"] = st_list[1]
    #tmp_dic['품목'] 변수에 st_list 2번째 index 값 저장
    tmp_dic["품목"] = st_list[2]
    #tmp_dic['가격'] 변수에 st_list 3번째 index 값 저장
    tmp_dic["가격"] = int(st_list[3])
    #tmp_dic['재고'] 변수에 st_list 4번째 index 값 저장
    tmp_dic["재고"] = int(st_list[4])
    #goods [0] 배열에 tmp_dic 저장
    goods[st_list[0]] = tmp_dic
    #day_sale 0번째 index에 0 할당
    day_sale[st_list[0]] = 0

# menu 불러오기
while True:
    print("1. 결제 \n2. 물품 관리 \n3. 매출 관리 \n9. 종료")
    print("="*30,end="\n")
    #선택한 번호 값 select_num에 저장
    select_num = input('선택 : ')

    # 판매 및 재고, 일매출 정리
    if select_num == '1':
        #tmp에 pay.py의 main 메서드 실행 값 저장
        tmp = pay.main(goods)
        update.main(goods,tmp,day_sale)

    # 재고 및 발주 관리
    elif select_num == '2':
        gmanagement.main(goods)

    # 일매출 및 월매출 확인
    elif select_num == '3':
        management.main(goods,day_sale)

    # 프로그램 종료 전에 메모리에 있는 정보를 텍스트 파일로 저장
    elif select_num == '9':
        ep.main(goods,day_sale)
        break
    else:
        print("다시 선택 하세요\n")

print("\nSystem down")
