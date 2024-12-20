# pythonStudy24
파이썬 ai 기초 학습용 24년도

ai 기초 학습으로 파이썬 학습 진행용 in mbc 아카데미 컴퓨터 교육센터 수원점<br/>
└ https://wikidocs.net/book/1

```
#미션
#1. 관리자가 커피 가격과 커피명을 정하고 개수를 입력
#2. 소비자가 커피를 구매하는데 잔돈이 나와야 함
#3. 판매 종료 후 관리자가 커피 판매한 총액을 파악할 수 있어야 함
def showCoffee(coffee,price,wlen,tot):#2번 눌렀을 때 재고 보여주기
    print(f"{coffee}:{price}원 & {wlen}/{tot}개")
    print("-"*80)
def makeCoffee(money,price,slen,wlen):#돈을 잘 받았을 때 커피 만들기
    print("-"*80)
    print("♡종업원이 맛있는 커피를 만듭니다♥")
    print("-"*80)
def nonCoffee():#커피 다 떨어졌을 때(재고X)
    print("★"*40)
    print("커피가 다 떨어졌습니다. 판매 재개를 기다려주세요.")
    print("-"*80)
    print("판매개수         판매금액")
    print(f"  {tot}개            {tot * price}원")
class lessMoney(Exception):#사용자지정 오류 클래스
    pass
class lessLen(Exception):
    pass
def lessmoney(money,slen):#유저가 입력한 금액과 개수를 비교
    if money*slen < price*slen:#가격 비교
        raise lessMoney  
    elif slen > wlen:#재고 확인
        raise lessLen
    else:
        return money*slen #다 OK 되면 총 금액 넘기기

print("어서오세요, 커피 테이크아웃 전문점입니다.")
while True:
    print("="*80)
    num = input("관리자면 1번, 소비자면 2번, 종료는 0번을 입력해주세요: ")
    print("-"*80)
    if num == '1':
        coffee = input(">> 커피 이름 입력: ")
        price = int(input(">> 커피 가격 입력: "))
        wlen = int(input(">> 커피 수량 입력: "))
        tot = wlen
    elif num == '2':
        if wlen == 0:
            nonCoffee()
        else:
            showCoffee(coffee,price,wlen,tot)
            while True:
                try:
                    money = int(input(">> 돈을 넣어주세요: "))
                    slen = int(input(">> 몇 개를 뽑으시나요: "))
                    totprice = lessmoney(money,slen)
                    makeCoffee(money,price,slen,wlen)
                    print(f"재고: {wlen - slen}개 / 잔돈: {money-(price*slen)}원")
                    wlen = wlen - slen
                    if wlen == 0:#재고 개수가 0개가 될 때
                        nonCoffee()
                        break
                    break
                except lessMoney:
                    print("-"*80)
                    print("금액이 모자랍니다. 다시 입력해주세요.")
                    print("-"*80)
                except lessLen:
                    print("-"*80)
                    print("재고가 부족합니다. 다시 입력해주세요.")
                    print("-"*80)
    elif num == '0':
        print("프로그램을 종료합니다.")
        break
    else:
        print("잘못된 입력입니다.")
```
