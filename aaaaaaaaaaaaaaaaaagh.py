def love_meter(name1,name2):
    love=0
    meter="love"
    l1=len(meter)
    for letter in range(l1):
        if meter[letter] in name1 or name2:
            love+=1
    print(love)

love_meter("shree venkat","lasya")