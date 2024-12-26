import lotto
import datetime as t

# 고객의 성별 정보를 저장
def choice_gender(guest_log):
    gender = input("\n성별 입력\n1. 남자 / 2. 여자 >> ")
    print("="*30,end="\n")
    if gender == '1':
        #1번 선택 시 guest_log 'gender' 영역에 man 저장
        guest_log["gender"] = 'man'
    elif gender == '2':
        #1번 선택 시 guest_log 'gender' 영역에 woman 저장
        guest_log["gender"] = 'woman'
    else:
        return True
    return False

# 고객의 나이 정보를 저장
def choice_age(guest_log):
    print("0. 10대 이전\t1. 10대\t2. 20대\t3. 30대\t4. 40대\t5. 50대\t6. 60대\t7. 60대 이상\n")
    #age에 나이 입력 값 저장
    age = input("나이 입력 >> ")
    if age == '0':
    #0 선택 시 게스트 로그 나이에 0 저장
        guest_log['age'] = 0
    elif age == '1':
    #1 선택 시 게스트 로그 나이에 1 저장
        guest_log['age'] = 10
    elif age == '2':
    #2 선택 시 게스트 로그 나이에 2 저장 ...
        guest_log['age'] = 20
    elif age == '3':
        guest_log['age'] = 30
    elif age == '4':
        guest_log['age'] = 40
    elif age == '5':
        guest_log['age'] = 50
    elif age == '6':
        guest_log['age'] = 60
    elif age == '7':
        guest_log['age'] = 70
    else:
        #그 외 다른 숫자 선택 시 계속 선택하도록
        return True
    #제대로 숫자 선택 시 빠져나가도록
    return False

# 물건 목록을 띄우고 그 중에서 어떤 물건을 구매할지 선택
# 물건의 수량 정보까지 취합하여 저장
# 구매 물건으로 로또를 선택했을 경우 lotto.main() 호출
def select_goods(tmp,goods):
    #tmp_list에 goods 변수 속 key 값들만 불러와 리스트화
    tmp_list = list(goods.keys())
    #tmp_list 반복
    for i in tmp_list:
        #품목, 가격 출력
        print("\n{}.\t{}\t/\t금액\t:\t{}".format(i,goods[i]['품목'],goods[i]['가격']))
    print("="*30,end="\n")
    s_num = 0
    while True:
        #구매할 상품 번호
        s_num = input("\n구매 상품 번호 >> ")
        #goods에 구매할 상품 번호가 있으면 빠져나가기
        if s_num in goods:
            break
    while True:
        try:
            #몇 개 구매할건지 + 구매 개수 입력 시 빠져나가기
            count = int(input("\n구매 상품 수량 >> "))
            break
        except:
            continue
    #상품 번호가 10번이면 구매 개수 가지고 로또 실행하기
    if s_num == '10':
        lotto.main(count)
    while True:
        #제품과 수량 확인하기
        print("제품: {} / 수량: {}".format(goods[s_num]['품목'],count))
        print("="*30,end="\n")
        #선택한 상품이 맞는지 확인
        num = input("1. 확인 / 2.취소 >> ")
        print("="*30,end="\n")
        #선택한 상품이 맞다면
        if num == '1':
            #tmp s_num에 개수 저장
            tmp[s_num] = count
            return False
        elif num == '2':
            #아니면 구매할 상품 다시 실행
            return True

# 구매하고자 하는 물건의 종류와 수량을 선택하는 흐름 제어
def flow_choice(guest_log,goods):
    boolean = True
    service = 0
    #tmp_goods에 '판매' guest_log 값 할당
    tmp_goods = guest_log['판매']
    while boolean:
        #boolean True면 tmp_goods와 goods를 가지고 상품 선택 실행
        boolean = select_goods(tmp_goods,goods)
    guest_log['판매'] = tmp_goods
    while True:
        #결제할지 다른 물품 또 선택할지
        end_flag = input("1. 다음 / 2. 다른 물품 선택 >> ")
        print("="*30,end="\n")
        if end_flag == '1':
            #다음 선택 시 빠져나가라
            return False
        elif end_flag == '2':
            return True

# 영수증 출력을 위하여 구매한 물건의 수량과 합계금액 정보를 저장
def calc_cost(tmp_dic,goods):
    total = 0
    tmp_list = list(tmp_dic.keys())
    sale_dic = {}    
    count = 0
    for i in tmp_list:
        tmp = {}
        count += 1
        t = goods[i]['가격'] * tmp_dic[i]
        total += t
        #품목 수량 합치기
        tmp['품목'] = goods[i]['품목']
        #수량 합치기
        tmp['수량'] = tmp_dic[i]
        tmp['총금액'] = t
        sale_dic[count] = tmp
    return sale_dic,total

# 결제 방법 선택
def select_payment():
    print("="*30)
    payment = input("1. 카드 / 2. 현금 >> ")
    print("="*30,end="\n")
    tmp = 0
    if payment == '1':
        #카드 선택 시
        tmp = 1
    elif payment == '2':
        #현금 선택 시
        tmp = 2
    else:
        return True, tmp
    return False, tmp

# 결제 방법 중 카드 결제 관련 흐름 제어
def select_card(sale_dic,total,guest_log):
    print("========== 영수증 ============")
    print("품목\t수량\t금액")
    for i in sale_dic.keys():
        print("{}\t{}\t{}".format(sale_dic[i]['품목'],sale_dic[i]['수량'],sale_dic[i]['총금액']))
    print()
    print("="*30,end="\n")
    print("\ntotal: {}".format(total))
    print("="*30,end="\n")
    tmp = input("1. 확인 / 2. 취소 >> ")
    print("="*30,end="\n")
    if tmp == '1':
        print("결제 완료")
        print("="*15)
        guest_log["결제"] = "card"
        guest_log["판매금액"] = total
        guest_log["거스름돈"] = None
        return False
    elif tmp == '2':
        print("결제 취소")
        print("="*15)
        return True
    else:
        print("다시 입력하세요")
        return True

# 결제 방법 중 현금 결제 관련 흐름 제어 
def select_cash(sale_dic, total,guest_log):
    print("========== 영수증 ============")
    print("품목\t수량\t금액")
    for i in sale_dic.keys():
       print("{}\t{}\t{}".format(sale_dic[i]['품목'],sale_dic[i]['수량'],sale_dic[i]['총금액']))
    print("="*30,end="\n")
    print("\ntotal: {}".format(total))
    print("="*30,end="\n")
    while True:
        tmp = input("\n받은 현금 >> ")
        try:
            tmp = int(tmp)
            break
        except:
            continue
    if tmp - total < 0:
        print("="*30,end="\n")
        print("받은 현금이 부족합니다")
        print("="*30,end="\n")
        return True
    else:
        print("="*30,end="\n")
        print("\n결제 완료")
        print("="*30,end="\n")
        print("잔돈: {}원".format(tmp - total))
        print("="*30,end="\n")
        guest_log["결제"] = "cash"
        guest_log["판매금액"] = total
        guest_log["거스름돈"] = tmp - total
        return False

# 물건 구매 후에 결제 관련된 모든 흐름 제어
def flow_payment(guest_log,goods):
    boolean = True
    select_num = 0
    tmp_goods = guest_log["판매"]
    sale_dic, total = calc_cost(tmp_goods,goods)
    while boolean:
        boolean, select_num = select_payment()
    boolean = True
    if select_num == 1:
        while boolean:
            boolean = select_card(sale_dic,total,guest_log)
    elif select_num == 2:
        while boolean:
            boolean = select_cash(sale_dic,total,guest_log)
    return False

#pay main 메서드 실행 시
def main(goods):
    now = t.datetime.now()
    guest_log = {'판매':{}}
    #성별 선택
    while choice_gender(guest_log):
        #return True 되면 나올 문구
        print("\n다시 입력하세요")
    #나이 선택
    while choice_age(guest_log):
        #return True 되면 나올 문구
        print("\n다시 입력하세요")
    #구입할 물품들 선택
    while flow_choice(guest_log,goods):
        continue
    #결제 선택
    while flow_payment(guest_log,goods):
        continue
    #오늘 날짜에 대한 포맷 설정
    now_time = "{}-{}-{}/{}:{}".format(now.year,now.month,now.day,now.hour,now.minute)
    #guest_log 일시에 오늘 날짜 정보 할당
    guest_log["일시"] = now_time
    print("="*30,end="\n")
    print()
    #guest_log 값 반환
    return(guest_log)