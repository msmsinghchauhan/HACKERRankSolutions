def validBraces(string):
    lst=[]
    validb=True
    table={"(":")","{":"}","[":"]"}
    for st in string:
        if st in table.keys():
            lst.append(st)
             
        elif not lst or (lst and table[lst.pop()]!=st):
            validb=False
            break
    return  True if not lst and validb else False 
