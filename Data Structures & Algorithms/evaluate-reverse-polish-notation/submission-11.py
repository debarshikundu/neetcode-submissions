class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        reg = []
        for t in range(len(tokens)):
            if tokens[t] == "+":
                reg.append(int(reg.pop()+reg.pop()))
            elif tokens[t] == "-":
                a, b = reg.pop(), reg.pop()
                reg.append(int(b - a))
            elif tokens[t] == "*":
                reg.append(int(reg.pop()*reg.pop()))
            elif tokens[t] == "/":
                a, b = reg.pop(), reg.pop()
                reg.append(int(b/a))
            else:
                reg.append(int(tokens[t]))
        return reg[0]
    