print("마라탕 사리 추가 메뉴판")
print("1.채소: 청경채,숙주,버섯,배추:50g --->1000원")
print("2.사리: 옥수수면,치즈떡,중국당면,분모자:50g --->2000원")
print("3.고기: 양고기,소고기:50g ---> 3000원")
ssum,sum1,sum2,sum3=0,0,0,0


while True:
    num=int(input("종류를 선택하세요,다 선택하셨다면 0번을 눌러주세요."))
    if num==0:
        break
    if num==1:
        pakchoi=int(input("청경채 횟수"))
        vegetable=int(input("숙주 횟수"))
        mushroom=int(input("버섯 횟수"))
        cabbage=int(input("배추 횟수"))
        sum1=(pakchoi+vegetable+mushroom+cabbage)*1000
    elif num==2:
        noodle=int(input("옥수수면 횟수"))
        cheese=int(input("치즈떡 횟수"))
        china=int(input("중국당면 횟수"))
        cellophane=int(input("분모자 횟수"))
        sum2=(noodle+cheese+china+cellophane)*2000
    elif num==3:
        meat=int(input("소고기 횟수"))
        mutton=int(input("양고기 횟수"))
        sum3=(meat+mutton)*3000
    else:
        print("잘못 눌렀습니다")
    ssum=sum1+sum2+sum3
print(ssum)    

total_price=ssum

received = int(input(f"가격의 합계는{total_price},원입니다. 지폐를 투입해 주세요----->"))

if received >= total_price:
    change=received-total_price
    print(f"{received}원을 받았습니다. 거스름돈은{change}원입니다.")

    
else:
    print("금액이 부족합니다. 주문이 취소되었습니다")
