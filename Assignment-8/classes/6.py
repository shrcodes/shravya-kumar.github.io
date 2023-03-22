#Write a Python class to implement pow(x, n)
class Pow:
    def my_pow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif n < 0:
            return 1 / self.my_pow(x, -n)
        elif n % 2 == 0:
            return self.my_pow(x * x, n // 2)
        else:
            return x * self.my_pow(x, n - 1)
