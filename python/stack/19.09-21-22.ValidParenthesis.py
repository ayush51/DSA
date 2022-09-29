def isValid(self, s:str)->bool
    stack = []
    closetoOpen = {"}":"{", ")": "(", "]":"["}
        for i in s:
            if i in closetoOpen:  #if this char is a closing parenthesis - every key, we wanna make sure our stack is not empty and the value at top of stack is matching opening parenthes
                if stack and stack[-1] == closetoOpen[i]:  #here closetoOpen refers to the matching opening parenthesis 
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return True if not stack else False
