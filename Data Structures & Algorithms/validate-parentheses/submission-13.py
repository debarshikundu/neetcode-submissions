class Solution:
    def isValid(self, s: str) -> bool:
        q=[]
        val = True
        for i in range(len(s)):
            if s[i] in "({[":
                q.append(s[i])
            if s[i] in "]})":
                if s[i] == ']':
                    if len(q) > 0:
                        if q.pop() != '[':
                            val = False
                            break
                    else: 
                        val = False
                        break
                elif s[i] == '}':
                    if len(q) > 0:
                        if q.pop() != '{':
                            val = False
                            break
                    else: 
                        val = False
                        break
                elif s[i] == ')':
                    if len(q) > 0:
                        if q.pop() != '(':
                            val = False
                            break
                    else:
                        val = False
                        break
        if len(q) > 0:
            val = False
        return val




            