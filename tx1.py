class Employee:
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string.")
        if not value.isalpha():
            raise ValueError("Name must contain only alphabetic characters.")
        if len(value) < 3:
            raise ValueError("Name must be at least 3 characters long.")
        self.__name = value

    @property
    def base_salary(self):
        return self.__base_salary

    @base_salary.setter
    def base_salary(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Salary must be a number.")
        if value < 0:
            raise ValueError("Salary must be a positive number.")
        self.__base_salary = value


class Manager(Employee):
    def __init__(self, name, base_salary, team_size=5):
        super().__init__(name, base_salary)
        self.team_size = team_size

    @property
    def team_size(self):
        return self.__team_size

    @team_size.setter
    def team_size(self, value):
        if not isinstance(value, int):
            raise ValueError("Team size must be an integer.")
        if value < 1:
            raise ValueError("Team size must be at least 1.")
        self.__team_size = value

    def calculate_bonus(self):
        return self.base_salary * 0.15 * self.team_size

    @property
    def total_salary(self):
        return self.base_salary + self.calculate_bonus()


class Developer(Employee):  # Наследуем от Employee
    def __init__(self, name, base_salary, experience_year=3, level="senior"):
        super().__init__(name, base_salary)
        self.experience_year = experience_year
        self.level = level
        self.bonus = 0

    @property
    def experience_year(self):
        return self.__experience_year

    @experience_year.setter
    def experience_year(self, value):
        if not isinstance(value, int):
            raise ValueError("Experience year must be an integer.")
        if value < 0:
            raise ValueError("Experience year must be a non-negative number.")
        self.__experience_year = value

    @property
    def level(self):
        return self.__level

    @level.setter
    def level(self, value):
        if not isinstance(value, str):
            raise ValueError("Level must be a string.")
        if value not in ["junior", "middle", "senior"]:
            raise ValueError("Level must be 'junior', 'middle' or 'senior'.")
        self.__level = value

    def calculate_bonus(self):
        if self.level == "junior":
            self.bonus = 0.05
        elif self.level == "middle":
            self.bonus = 0.1
        elif self.level == "senior":
            self.bonus = 0.15
        else:
            raise ValueError("Invalid level.")
        return self.base_salary * self.bonus * self.experience_year

    @property
    def total_salary(self):
        return self.base_salary + self.calculate_bonus()


# Пример использования
manager = Manager("Alice", base_salary=5000, team_size=5)
developer = Developer("Bob", base_salary=4000, experience_year=3, level="senior")

print(manager.total_salary)  # Учитывая бонусы
print(developer.total_salary)  # Учитывая стаж и уровень
