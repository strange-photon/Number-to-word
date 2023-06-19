#code by santosh soni
D1={0:'',      # 0:'' for handle zeros between numbers
    1:"one",
    2:'two',
    3:'three',
    4:'four',
    5:'five',
    6:'six',
    7:'seven',
    8:'eight',
    9:'nine',
}

D2={0:'',  
    10:'ten',
    11:'eleven',
    12:'twelve',
    13:'thirteen',
    14:'fourteen',
    15:'fifteen',
    16:'sixteen',
    17:'seventeen',
    18:'eighteen',
    19:'nineteen',
    20:'twenty',
    30:'thirty',
    40:'forty',
    50:'fifty',
    60:'sixty',
    70:'seventy',
    80:'eighty',
    90:'ninety'
}

D3={
    3:'hundred',
    4:'thousand',
    6:'Lakh',
    8:'crore',
}


def NumToWord(num):
    """support upto 16 digits numbers"""
    s=str(num)
    def upto3(s):
        "handle upto 3 digit numbers"
        s=str(s)
        def upto2(s):
                if int(s) in D2:
                    return D2[int(s)]
                else:
                    return f"{D2[int(str(s)[0]+'0')]} {D1[int(str(s)[-1])]}"   # let assume s=23  D2[int(str(s)[0]+'0')]---> D2[int('2'+'0')]---> D2[20]---> "Twenty"           D1[int(str(s)[-1])]---> D1[3]---> Three
                
        if len(s)==1:
            return D1[int(s)] 
        elif len(s)==2:
            if s[0]=='0':              # while making this Algo i noticed 0 is most mind fuking word so i was find sollution  
                return D1[int(s[-1])]  #possiblity with 0 ---> 01 or 10 , 02 or 20  ---> if 0th char is 0 then we have to find 1st/last element of string
            else:
                return upto2(int(s))   
        else:                                               #for three digit number
            if s[1:]=='00':
                if s=='000':                                #for possiblity : 000
                    return ''                               
                return D1[int(s[0])]+" hundred"             #for possiblity : 200
            elif s[0]=='0' and s[1]!='0':                   #for possiblity : 013  ,010 this possiblity dosnt matter because upto2 can solve this 
                return upto2(s[1:])
            elif s[:2]=='00':                               #for possiblity : 001
                return D1[int(s[-1])]
            elif s[1]=='0':                                 #for possiblity : 101
                return D1[int(s[0])]+" hundred "+D1[int(s[-1])]
            else:                                           #for other numbers like 123, 456,765 or something like that 
                return D1[int(s[0])]+" hundred "+upto2(s[1:])
    

    def main(num):
        "can handle upto 9 digit numbers"
        s=str(num)    
        Temp=[]
        Len=len(s)
        i=0
        while Len!=0:
            if Len<=3:
                Temp.append(upto3(s[i:]))
                break
            elif len(s[i:])%2==0:                # for even len of number we can do normal think below                                                                
                Temp.append(f"{D1[int(s[i])]} {D3[Len] if D1[int(s[i])]!='' else ''}")  #if block of code for handle zeros 0
                Len-=1
                i+=1
            else:                                #but for odd len of number like 54000: code have to consider 54  
                Temp.append(f"{upto3(int(s[i:i+2]))} {D3[Len-1] if upto3(int(s[i:i+2]))!='' else ''}")   #thats why Len-1 and i+2
                Len-=2                           #like len('54000') --->5 ---> 5 is odd so 54--2 000--3 
                i+=2

        return ' '.join(" ".join(list(filter(lambda x: len(x)>0,Temp))).split())
    if len(s)<=3:
        return upto3(s)
    elif len(s)<=9:
        return main(num)
    else:
        return main(s[:len(s)-7]) +' CRORE, '+ main(s[len(s)-7:])[:]
    

print(NumToWord(9000))
