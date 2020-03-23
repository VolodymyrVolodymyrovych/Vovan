def IsBalanced(file):
    strInput = file
    if strInput:
        brackets = [('(', ')'), ('[', ']'), ('{', '}')]
        kStart = 0
        kEnd = 1

        stack = []
        for char in strInput:
            for bracketPair in brackets:
                if char == bracketPair[kStart]:
                    stack.append(char)
                elif char == bracketPair[kEnd] and len(stack) > 0 and stack.pop() != bracketPair[kStart]:
                    return False
                if len(stack) == 0:
                    return True

    return False


a = str(input(": "))
print(IsBalanced(a))
