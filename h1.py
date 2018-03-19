## price and station_name
station_name = ["PS4","NS","XBOX360"]
station_price = [12900,11000,10360]

## your input
play = input("We have PS4 , NS and XBOX360 \nWhich one do you want to buy ? (0,1,2) :")
number = input("How many "+station_name[int(play)]+" do you want ? ")
money = input("How much do you have ? ")

print()

## Calculate your cost
cost = station_price[int(play)] * int(number)

## Check if you can buy or not
print("Do I have enough money ? ",bool(int(money)>=cost))

### if not 
if int(money) < cost :
    can_buy = int(money)//station_price[int(play)]

    ## you can buy at least one
    if can_buy>0:
        print("But you can actually buy ",can_buy," ",station_name[int(play)])
    ## QQ even one is too expensive for you
    else:
        print("No money No gain")

### Left money
print("And left : ",int(money)%station_price[int(play)])
