def is_matched(strOfBrackets):
    stack = []
    pushChars, popChars = "({[", ")}]"
    for c in strOfBrackets:
        if c in pushChars:
            stack.append(c)
        elif c in popChars:
            if not len(stack):
                return False
            else:
                stackTop = stack.pop()
                balancingBracket = pushChars[popChars.index(c)]
                if stackTop != balancingBracket:
                    return False
        else:
            return False
    return not len(stack)

print is_matched("{{[[((([)))]]}}")
print is_matched("{{[[((([])))]]}}")
