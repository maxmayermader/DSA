class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = []
        for i in range(1, n+1):
            word = ""
            if i % 3 == 0:
                word += "Fizz"
            if i % 5 == 0:
                word += "Buzz"
            elif i % 3 != 0:
                word += str(i)
            res.append(word)

        return res
        