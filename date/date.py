from typing import Optional, overload


class TimeDelta:
    """Вспомогательный класс, в котором хранится информация о количестве дней, месяцев или лет,
     которое нужно добавить к дате или вычесть из даты"""

    def __init__(self, days: Optional[int] = None, months: Optional[int] = None, years: Optional[int] = None):
        """Создание некой timedelta. Для каждой из позиции можно использовать число или None"""
        self.days = days
        self.months = months
        self.years = years

    @property
    def days(self):
        return self._days

    @days.setter
    def days(self, days_value: int or None):
        if days_value is None:
            self._days = days_value
        elif not isinstance(days_value, int):
            raise TypeError('You can input only an integer for a "days" value.')
        elif days_value < 0:
            raise NotImplementedError('Addition of a negative "days" value is not implemented yet.')
        self._days = days_value

    @property
    def months(self):
        return self._months

    @months.setter
    def months(self, months_value: int or None):
        if months_value is None:
            self._months = months_value
        elif not isinstance(months_value, int):
            raise TypeError('You can input only an integer for a "months" value.')
        elif months_value < 0:
            raise NotImplementedError('Addition of a negative "months" value is not implemented yet.')
        self._months = months_value

    @property
    def years(self):
        return self._years

    @years.setter
    def years(self, years_value: int or None):
        if years_value is None:
            self._years = years_value
        elif not isinstance(years_value, int):
            raise TypeError('You can input only an integer for a "years" value.')
        elif years_value < 0:
            raise NotImplementedError('Addition of a negative "years" value is not implemented yet.')
        self._years = years_value

    def __str__(self) -> str:
        """Возвращает timedelta в формате days.months.years"""
        return f'{self.days}.{self.months}.{self.years}'

    def __repr__(self) -> str:
        """Возвращает timedelta в формате TimeDelta(days, months, years)"""
        return f'TimeDelta({self.days}, {self.months}, {self.years})'


class Date:
    """Класс для работы с датами"""
    days_in_months = [(31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31),  # number of days in the months of a normal year
                      (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)]  # number of days in the months of a leap year

    @overload
    def __init__(self, day: int, month: int, year: int):
        """Создание даты из трех чисел"""

    @overload
    def __init__(self, date: str):
        """Создание даты из строки формата dd.mm.yyyy"""

    def __init__(self, *args):
        if len(args) == 3 and all(isinstance(i, int) for i in args):
            check = self.is_valid_date(args[0], args[1], args[2])  # check for incorrect values
            if check:
                self._day, self._month, self._year = args
            else:
                raise ValueError(f'{args[0]:02d}.{args[1]:02d}.{args[2]:04d} is not a valid date.')

        elif len(args) == 1 and isinstance(args[0], str):
            to_split = args[0].split('.')
            if len(to_split) != 3:
                raise ValueError('Incorrect string format. Right format: dd.mm.yyyy')
            else:
                check = self.is_valid_date(int(to_split[0]), int(to_split[1]), int(to_split[2]))
                if check:
                    self._day, self._month, self._year, = int(to_split[0]), int(to_split[1]), int(to_split[2])
                else:
                    raise ValueError(f'{int(to_split[0]):02d}.{int(to_split[1]):02d}.{int(to_split[2]):04d}'
                                     f' is not a valid date.')

        else:
            raise ValueError('You should input a date in either of the two specified formats.')  # REVISE!!!

    def __str__(self) -> str:
        """Возвращает дату в формате dd.mm.yyyy"""
        return f'{self.day:02d}.{self.month:02d}.{self.year:04d}'

    def __repr__(self) -> str:
        """Возвращает дату в формате Date(day, month, year)"""
        return f'Date({self.day}, {self.month}, {self.year})'

    @staticmethod
    def is_leap_year(year: int) -> bool:
        """Проверяет, является ли год високосным"""
        if not isinstance(year, int):
            raise TypeError('You can input only a positive integer for a "year" value.')
        if not 1 <= year <= float('inf'):
            raise ValueError('The value of "year" can only be between 1 and infinity.')
        if year % 4 != 0 or (year % 100 == 0 and year % 400 != 0):
            return False
        else:
            return True

    # Private method. For internal use only ;)
    def __how_many_leaps(self, first_year: int, second_year: int) -> int:
        """This function returns a number of leap years between two given years"""
        leaps = 0
        current_year = first_year
        if first_year > second_year:
            sign = -1
        elif first_year < second_year:
            sign = 1
        else:
            check = self.is_leap_year(current_year)
            return 1 if check else 0
        while current_year != second_year + 1 * sign:
            check = self.is_leap_year(current_year)
            if check:
                leaps += 1
            current_year = current_year + 1 * sign
        return leaps

    @classmethod
    def get_max_day(cls, month: int, year: int) -> int:
        """Возвращает максимальное количество дней в месяце для указанного года"""
        return cls.days_in_months[cls.is_leap_year(year)][month - 1]

    @classmethod
    def is_valid_date(cls, day: int, month: int, year: int):
        """Проверяет, является ли дата корректной"""
        if not str(day).isdigit() or not str(month).isdigit() or not str(year).isdigit():
            raise TypeError('You can input only positive integers for a date.')
        if not 1 <= int(day) <= 31:
            raise ValueError('The value of "day" can only be between 1 and 31.')
        if not 1 <= int(month) <= 12:
            raise ValueError('The value of "month" can only be between 1 and 12.')
        if not 1 <= int(year) <= float('inf'):
            raise ValueError('The value of "year" can only be between 1 and infinity.')
        max_days = cls.get_max_day(int(month), int(year))
        if int(day) <= max_days:
            return True
        else:
            return False

    @property
    def day(self):
        return self._day

    @day.setter
    def day(self, day_value: int):
        """value от 1 до 31. Проверять значение и корректность даты"""
        check = self.is_valid_date(day_value, self.month, self.year)
        if check:
            self._day = day_value
        else:
            raise ValueError(f'{day_value:02d}.{self.month:02d}.{self.year:04d} is not a valid date.')

    @property
    def month(self):
        return self._month

    @month.setter
    def month(self, month_value: int):
        """value от 1 до 12. Проверять значение и корректность даты"""
        check = self.is_valid_date(self.day, month_value, self.year)
        if check:
            self._month = month_value
        else:
            raise ValueError(f'{self.day:02d}.{month_value:02d}.{self.year:04d} is not a valid date.')

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, year_value: int):
        """value от 1 до ... . Проверять значение и корректность даты"""
        check = self.is_valid_date(self.day, self.month, year_value)
        if check:
            self._year = year_value
        else:
            raise ValueError(f'{self.day:02d}.{self.month:02d}.{year_value:04d} is not a valid date.')

    def __sub__(self, other: "Date") -> int:
        """Разница между датой self и other (-)"""
        if not isinstance(other, Date):
            raise TypeError('Second parameter should be of class "Date".')
        diff_years = abs(self.year - other.year)
        leap_years = self.__how_many_leaps(self.year, other.year)
        total = leap_years * 366 + (diff_years + 1 - leap_years) * 365
        type_year_1 = self.is_leap_year(self.year)
        type_year_2 = other.is_leap_year(other.year)
        count_1 = self.day
        count_2 = other.day

        for i in range(0, self.month - 1):
            count_1 += self.days_in_months[type_year_1][i]
        for j in range(0, other.month - 1):
            count_2 += other.days_in_months[type_year_2][j]
        if self.year > other.year:
            result = total - count_2 - (366 if type_year_1 else 365 - count_1)
        elif self.year < other.year:
            result = - (total - count_1 - (366 if type_year_2 else 365 - count_2))
        else:
            result = count_1 - count_2

        return result

    # Private method. For internal use only ;)
    def __special_for_add_and_iadd(self, some_timedelta: TimeDelta):
        """This function contains the required logic for the __add__ and __iadd__ functions"""
        current_day = self.day
        current_month = self.month
        current_year = self.year

        years_to_add = some_timedelta.years
        if years_to_add is None:
            result_year = current_year
        else:
            result_year = current_year + years_to_add

        months_to_add = some_timedelta.months
        if months_to_add is None:
            result_month = current_month
        else:
            while current_month + months_to_add > 12:
                result_year += 1
                months_to_add -= 12
            result_month = current_month + months_to_add

        days_to_add = some_timedelta.days
        days_number = current_day
        if days_to_add is None:
            result_day = days_number
            check = self.get_max_day(result_month, result_year)
            if result_day > check:
                result_day = self.get_max_day(result_month, result_year)
        else:
            while days_number + days_to_add > self.get_max_day(result_month, result_year):
                days_to_add -= (self.get_max_day(result_month, result_year) - days_number)
                days_number = 0
                result_month += 1
                if result_month == 13:
                    result_year += 1
                    result_month = 1
            result_day = days_number + days_to_add

        return result_day, result_month, result_year

    def __add__(self, other: TimeDelta) -> "Date":
        """Складывает self и некий timedelta. Возвращает НОВЫЙ инстанс Date, self не меняет (+)"""
        if not isinstance(other, TimeDelta):
            raise TypeError('Second parameter should be of class "TimeDelta".')
        result = self.__special_for_add_and_iadd(other)
        return Date(result[0], result[1], result[2])

    def __iadd__(self, other: TimeDelta) -> "Date":
        """Добавляет к self некий timedelta меняя сам self (+=)"""
        if not isinstance(other, TimeDelta):
            raise TypeError('Second parameter should be of class "TimeDelta".')
        result = self.__special_for_add_and_iadd(other)
        self._day, self._month, self._year = result
        return self
