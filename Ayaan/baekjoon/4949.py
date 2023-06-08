parenthesis = {'(': ')', '[': ']'}

while True:
    sentence = input()
    if sentence == '.':
        break
    stack = []
    for ch in sentence:
        if ch == '(' or ch == '[':
            stack.append(ch)
        elif ch == ')' or ch == ']':
            if stack and parenthesis[stack[-1]] == ch:
                stack.pop()
            else:
                print("no")
                break
        elif ch == '.':
            print("no") if stack else print("yes")
