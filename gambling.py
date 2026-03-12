def gamble(money, m1, m2, m3):
    played = 0
    while money > 0:
        money += 1
        m1 +=1
        played +=1
        if m1 == 35:
            money +=30
            m1 = 0
        if money > 0:
            m2 += 1
            played += 1
            if m2 == 100:
                money +=60
                m2 = 0
        if money > 0:
            m3 += 1
            played += 1
            if m3 == 10:
                money += 9
                m3 = 0
    print(played)
gamble(48, 3, 10, 4)
        