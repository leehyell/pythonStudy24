# pay.main()이 반환한 고객의 매출 정보를 이용하여
# 일 매출과 재고 정보를 갱신
def main(goods,guest_log,day_sale) :
    #guset_dic에 guest_log의 '판매' 배열 값 저장
    guest_dic = guest_log["판매"]
    #guest_dic_key에 guest_dic의 key 값들 리스트화
    guest_dic_key = list(guest_dic.keys())

    ## 일 매출
    #guest_dic의 key 값들 리스트화 반복문
    for i in list(day_sale.keys()):
        #i가 guest_dic_key 변수에 없다면
        if i not in guest_dic_key:
            #계속
            continue
        #guest_dic_key 변수에 있다면
        #day_sale[i]에 guest_dic i번째에 goods i행의 '가격' 곱한 값을 넣기
        day_sale[i] = guest_dic[i] * goods[i]['가격']
        #goods i 행의 '재고'에서 guest_dic i열에 있는 개수 만큼 빼기
        goods[i]['재고'] = goods[i]['재고'] - guest_dic[i]
        
    #결제가 캐쉬로 되어 있으면
    if guest_log['결제'] == 'cash' :              ## 금액 입력부분
        #캐쉬 금액에서 판매금액 만큼을 더하기
        day_sale["cash"] = day_sale["cash"] + guest_log["판매금액"]  
    #결제가 카드로 되어 있으면
    elif guest_log['결제'] == 'card' :
        #카드 금액에서 판매금액 만큼을 더하기
        day_sale["card"] = day_sale["card"] + guest_log["판매금액"]

