class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        fizz = 0
        buzz = 0
        A =[]
        for i in range(1,n+1):
            fizz += 1
            buzz += 1
            if fizz==3 and buzz==5:
                A.append("FizzBuzz")
                fizz = 0
                buzz = 0
            elif fizz==3:
                A.append("Fizz")
                fizz = 0
            elif buzz==5:
                A.append("Buzz")
                buzz = 0
            else:
                A.append(str(i))
        return A