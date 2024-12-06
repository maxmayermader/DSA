class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = [""]*n
        for i in range(1, n+1):
            divby3 = i % 3 == 0
            if divby3:
                res[i-1] += "Fizz"
            if i % 5 == 0:
                res[i-1]  += "Buzz"
            elif not divby3:
                res[i-1]  += str(i)
            # res.append(word)

        return res