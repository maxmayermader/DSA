class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = []
        for i in range(1, n+1):
            word = ""
            divby3 = i % 3 == 0
            if divby3:
                word += "Fizz"
            if i % 5 == 0:
                word += "Buzz"
            elif not divby3:
                word += str(i)
            res.append(word)

        return res
        