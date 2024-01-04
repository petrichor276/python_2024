def romanToInt(s):
    '''定义转换规则'''
    rules={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    Int=0
    n=len(s)
    for index in range(n-1):
        print(rules[s[index]])
        if rules[s[index]]<rules[s[index+1]]:
            Int-=rules[s[index]]
        else:
            Int+=rules[s[index]]

    return Int+rules[s[-1]]


result=romanToInt('MCMXCIV')
print(result)