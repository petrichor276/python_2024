s = "()[]{}"

# s = "(]"
def isValid(s: str) -> bool:
    dic = {'(': ')', '[': ']', '{': '}', '?': '?'}
    stack = ['?']
    for i in s:
        if i in dic:
            stack.append(i)
            print('----', stack)
            # print(dic[stack.pop()])
        elif dic[stack.pop()] != i:
            print('====',stack)
            return False

    print(stack)
    return len(stack) == 1


isValid(s)
