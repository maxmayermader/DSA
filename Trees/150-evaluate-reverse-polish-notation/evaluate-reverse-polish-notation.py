class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []

        def operation(op):
            b = s.pop()
            a = s.pop()
            if op == '*':
                return a * b
            elif op == '/':
                return int(a / b)  # Or use: a // b
            elif op == '+':
                return a + b
            else:
                return a - b

        for t in tokens:
            if t in {'+', '-', '*', '/'}:
                s.append(operation(t))
            else:
                s.append(int(t))

        return s[0]