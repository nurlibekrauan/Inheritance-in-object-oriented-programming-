class Formula:
    def solve(self):
        pass


class LinearFormula(Formula):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def solve(self):
        if self.a == 0:
            raise ValueError("Coefficient 'a' cannot be zero in a linear equation.")
        return -self.b / self.a

    def __str__(self) -> str:
        return f'{self.a}x + {self.b} = 0'


class QuadraticFormula(Formula):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def solve(self):
        if self.a == 0:
            raise ValueError("Coefficient 'a' cannot be zero in a quadratic equation.")
        discriminant = self.b ** 2 - 4 * self.a * self.c
        if discriminant > 0:
            root1 = (-self.b + discriminant ** 0.5) / (2 * self.a)
            root2 = (-self.b - discriminant ** 0.5) / (2 * self.a)
            return root1, root2
        elif discriminant == 0:
            root = -self.b / (2 * self.a)
            return root
        else:
            return "No real roots"  # Или можно вернуть комплексные корни, если нужно

    def __str__(self) -> str:
        return f'{self.a}x^2 + {self.b}x + {self.c} = 0'


# Пример использования:
linear = LinearFormula(a=2, b=-4)
quadratic = QuadraticFormula(a=1, b=-3, c=2)

print(linear.solve())  # Решение линейного уравнения
print(quadratic.solve())  # Решение квадратичного уравнения
