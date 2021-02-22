import pytest
from date import Date, TimeDelta


# TESTS FOR TimeDelta CLASS

# Testing "__init__ method" with correct variables
@pytest.mark.parametrize("days, months, years", [(1, 1, 1), (100, 100, 100)])
def test_init_correct_timedelta(days, months, years):
    my_timedelta = TimeDelta(days, months, years)
    assert my_timedelta.days == days
    assert my_timedelta.months == months
    assert my_timedelta.years == years


# Test related to "days.setter"
@pytest.mark.parametrize("days", [42, None])
def test_correct_days_setter(days):
    my_timedelta = TimeDelta(1, 1, 1)
    my_timedelta.days = days
    assert my_timedelta.days == days


# Test related to "days.setter"
@pytest.mark.parametrize("days", ["pickle", [1, 2, 3]])
def test_evil_days_setter(days):
    my_timedelta = TimeDelta(1, 1, 1)
    with pytest.raises(TypeError) as excinfo:
        my_timedelta.days = days
    assert 'You can input only an integer for a "days" value.' in str(excinfo.value)


# Test related to "days.setter"
def test_negative_days_setter():
    my_timedelta = TimeDelta(1, 1, 1)
    with pytest.raises(NotImplementedError) as excinfo:
        my_timedelta.days = -42
    assert 'Addition of a negative "days" value is not implemented yet.' in str(excinfo.value)


# Test related to "months.setter"
@pytest.mark.parametrize("months", [42, None])
def test_correct_months_setter(months):
    my_timedelta = TimeDelta(1, 1, 1)
    my_timedelta.months = months
    assert my_timedelta.months == months


# Test related to "months.setter"
@pytest.mark.parametrize("months", ["pickle", [1, 2, 3]])
def test_evil_months_setter(months):
    my_timedelta = TimeDelta(1, 1, 1)
    with pytest.raises(TypeError) as excinfo:
        my_timedelta.months = months
    assert 'You can input only an integer for a "months" value.' in str(excinfo.value)


# Test related to "months.setter"
def test_negative_months_setter():
    my_timedelta = TimeDelta(1, 1, 1)
    with pytest.raises(NotImplementedError) as excinfo:
        my_timedelta.months = -42
    assert 'Addition of a negative "months" value is not implemented yet.' in str(excinfo.value)


# Test related to "years.setter"
@pytest.mark.parametrize("years", [42, None])
def test_correct_years_setter(years):
    my_timedelta = TimeDelta(1, 1, 1)
    my_timedelta.years = years
    assert my_timedelta.years == years


# Test related to "years.setter"
@pytest.mark.parametrize("years", ["pickle", [1, 2, 3]])
def test_evil_years_setter(years):
    my_timedelta = TimeDelta(1, 1, 1)
    with pytest.raises(TypeError) as excinfo:
        my_timedelta.years = years
    assert 'You can input only an integer for a "years" value.' in str(excinfo.value)


# Test related to "years.setter"
def test_negative_years_setter():
    my_timedelta = TimeDelta(1, 1, 1)
    with pytest.raises(NotImplementedError) as excinfo:
        my_timedelta.years = -42
    assert 'Addition of a negative "years" value is not implemented yet.' in str(excinfo.value)


# Test related to "__str__ method"
@pytest.mark.parametrize("days, months, years", [(1, 1, 1), (100, 100, 100), (None, None, None)])
def test_str_function_timedelta(days, months, years):
    check = str(TimeDelta(days, months, years))
    assert check == f'{days}.{months}.{years}'


# Test related to "__repr__ method"
@pytest.mark.parametrize("days, months, years", [(1, 1, 1), (100, 100, 100), (None, None, None)])
def test_repr_function_timedelta(days, months, years):
    check = repr(TimeDelta(days, months, years))
    assert check == f'TimeDelta({days}, {months}, {years})'


# TESTS FOR DATE CLASS

# Testing "__init__ method" with correct variables
@pytest.mark.parametrize("day, month, year", [(21, 2, 2021), (8, 3, 1990), (1, 9, 2000)])
def test_init_correct_date_ver1(day, month, year):
    my_date = Date(day, month, year)
    assert my_date.day == day
    assert my_date.month == month
    assert my_date.year == year


# Testing "__init__ method" with correct variables
@pytest.mark.parametrize("date", ["21.02.2021", "08.03.1990", "01.09.2000"])
def test_init_correct_date_ver2(date):
    my_date = Date(date)
    check = date.split('.')
    assert my_date.day == int(check[0])
    assert my_date.month == int(check[1])
    assert my_date.year == int(check[2])


# Testing "__init__ method" with incorrect variables
@pytest.mark.parametrize("day, month, year", [(29, 2, 2001), (31, 4, 2021), (31, 9, 1994)])
def test_init_wrong_date_ver1(day, month, year):
    with pytest.raises(ValueError) as excinfo:
        Date(day, month, year)
    assert f'{day:02d}.{month:02d}.{year:04d} is not a valid date.' in str(excinfo.value)


# Testing "__init__ method" with incorrect variables
@pytest.mark.parametrize("date", ["29.02.2001", "31.04.2021", "31.09.1994"])
def test_init_wrong_date_ver2(date):
    with pytest.raises(ValueError) as excinfo:
        Date(date)
    check = date.split('.')
    assert f'{int(check[0]):02d}.{int(check[1]):02d}.{int(check[2]):04d} is not a valid date.' in str(excinfo.value)


# Test wrong format with extra variable
def test_wrong_format():
    with pytest.raises(ValueError) as excinfo:
        Date(31, 12, 2000, 42)
    assert 'You should input a date in either of the two specified formats.' in str(excinfo.value)


# Test wrong string format
def test_wrong_string_format():
    with pytest.raises(ValueError) as excinfo:
        Date("31.12.2000.42")
    assert 'Incorrect string format. Right format: dd.mm.yyyy' in str(excinfo.value)


# Test related to "__str__ method"
@pytest.mark.parametrize("day, month, year", [(21, 2, 2021), (8, 3, 1990), (1, 9, 2000)])
def test_str_function_date(day, month, year):
    check = str(Date(day, month, year))
    assert check == f'{day:02d}.{month:02d}.{year:04d}'


# Test related to "__repr__ method"
@pytest.mark.parametrize("day, month, year", [(21, 2, 2021), (8, 3, 1990), (1, 9, 2000)])
def test_repr_function_date(day, month, year):
    check = repr(Date(day, month, year))
    assert check == f'Date({day}, {month}, {year})'


# Test related to "is_leap_year method"
@pytest.mark.parametrize("year, expected", [(2020, True), (1991, False), (700, False), (800, True)])
def test_leap_year(year, expected):
    answer = Date.is_leap_year(year)
    assert answer == expected


# Test related to "is_leap_year method"
@pytest.mark.parametrize("year", ["pickle", [1, 2, 3]])
def test_evil_leap_year(year):
    with pytest.raises(TypeError) as excinfo:
        Date.is_leap_year(year)
    assert 'You can input only a positive integer for a "year" value.' in str(excinfo.value)


# Test related to "is_leap_year method"
@pytest.mark.parametrize("year", [0, -100])
def test_zero_negative_leap_year(year):
    with pytest.raises(ValueError) as excinfo:
        Date.is_leap_year(year)
    assert 'The value of "year" can only be between 1 and infinity.' in str(excinfo.value)


# Test related to "get_max_day method"
@pytest.mark.parametrize("month, year, expected", [(2, 2004, 29), (2, 700, 28), (3, 2021, 31), (4, 1994, 30)])
def test_max_day(month, year, expected):
    max_days = Date.get_max_day(month, year)
    assert max_days == expected


# Test related to "is_valid_date method"
@pytest.mark.parametrize("day", [42, 0, 100, 32])
def test_bad_day_from_range(day):
    with pytest.raises(ValueError) as excinfo:
        Date(day, 12, 2000)
    assert 'The value of "day" can only be between 1 and 31.' in str(excinfo.value)


# Test related to "is_valid_date method"
@pytest.mark.parametrize("month", [42, 0, 100, 13])
def test_bad_month_from_range(month):
    with pytest.raises(ValueError) as excinfo:
        Date(12, month, 2000)
    assert 'The value of "month" can only be between 1 and 12.' in str(excinfo.value)


# Test related to "is_valid_date method"
def test_bad_year_from_range():
    with pytest.raises(ValueError) as excinfo:
        Date(12, 12, 0)
    assert 'The value of "year" can only be between 1 and infinity.' in str(excinfo.value)


# Test related to "is_valid_date method"
@pytest.mark.parametrize("day, month, year", [("pickle", 2, 2001), (31, "pickle", 2021), (31, 9, "pickle")])
def test_evil_string(day, month, year):
    with pytest.raises(TypeError) as excinfo:
        Date.is_valid_date(day, month, year)
    assert 'You can input only positive integers for a date.' in str(excinfo.value)


# Test related to "is_valid_date method"
@pytest.mark.parametrize("day, month, year", [(29, 2, 2001), (31, 4, 2021), (31, 9, 1994)])
def test_wrong_date(day, month, year):
    check = Date.is_valid_date(day, month, year)
    assert check is False


# Test related to "day.setter"
def test_correct_day_setter():
    my_date = Date(12, 12, 2020)
    my_date.day = 13
    assert my_date.day == 13


# Test related to "day.setter"
@pytest.mark.parametrize("day, month, year, bad_day", [(30, 9, 2001, 31), (30, 4, 2021, 31), (29, 2, 1996, 30)])
def test_incorrect_day_setter(day, month, year, bad_day):
    my_date = Date(day, month, year)
    with pytest.raises(ValueError) as excinfo:
        my_date.day = bad_day
    assert f'{bad_day:02d}.{month:02d}.{year:04d} is not a valid date.' in str(excinfo.value)


# Test related to "month.setter"
def test_correct_month_setter():
    my_date = Date(31, 7, 2020)
    my_date.month = 8
    assert my_date.month == 8


# Test related to "month.setter"
@pytest.mark.parametrize("day, month, year, bad_month", [(31, 8, 2001, 9), (31, 5, 2021, 6), (30, 1, 1996, 2)])
def test_incorrect_month_setter(day, month, year, bad_month):
    my_date = Date(day, month, year)
    with pytest.raises(ValueError) as excinfo:
        my_date.month = bad_month
    assert f'{day:02d}.{bad_month:02d}.{year:04d} is not a valid date.' in str(excinfo.value)


# Test related to "year.setter"
def test_correct_year_setter():
    my_date = Date(31, 7, 2020)
    my_date.year = 2021
    assert my_date.year == 2021


# Test related to "year.setter"
@pytest.mark.parametrize("day, month, year, bad_year", [(29, 2, 2004, 2005), (29, 2, 2020, 2021)])
def test_incorrect_year_setter(day, month, year, bad_year):
    my_date = Date(day, month, year)
    with pytest.raises(ValueError) as excinfo:
        my_date.year = bad_year
    assert f'{day:02d}.{month:02d}.{bad_year:04d} is not a valid date.' in str(excinfo.value)


# Test related to "__sub__ method" and "__how_many_leaps private method"
@pytest.mark.parametrize("first_date, second_date, expected", [(Date(31, 12, 2020), Date(28, 2, 2021), -59),
                                                               (Date(14, 8, 1994), Date(27, 10, 1972), 7961),
                                                               (Date(14, 8, 1994), Date(14, 8, 1994), 0),
                                                               (Date(6, 8, 1989), Date(14, 8, 1994), -1834)])
def test_sub(first_date, second_date, expected):
    result = first_date - second_date
    assert result == expected


# Test related to "__sub__ method"
def test_correct_type_sub():
    first_date = Date(31, 12, 2020)
    with pytest.raises(TypeError) as excinfo:
        first_date - 'cow'
    assert 'Second parameter should be of class "Date".' in str(excinfo.value)


# Test related to "__add__ method" and "__special_for_add_and_iadd private method"
@pytest.mark.parametrize("date, timedelta, expected",
                         [(Date(31, 12, 2020), TimeDelta(None, None, None), Date(31, 12, 2020)),
                          (Date(29, 2, 2004), TimeDelta(95, 8, 5), Date(1, 2, 2010)),
                          (Date(5, 3, 2016), TimeDelta(None, 30, None), Date(5, 9, 2018)),
                          (Date(15, 11, 2016), TimeDelta(None, 27, None), Date(15, 2, 2019)),
                          (Date(15, 2, 2016), TimeDelta(None, None, 100), Date(15, 2, 2116)),
                          (Date(15, 11, 2016), TimeDelta(100, None, None), Date(23, 2, 2017)),
                          (Date(31, 1, 2016), TimeDelta(None, 1, None), Date(29, 2, 2016))])
def test_add(date, timedelta, expected):
    result = date + timedelta
    assert result.day == expected.day
    assert result.month == expected.month
    assert result.year == expected.year


# Test related to "__add__ method"
def test_correct_type_add():
    date = Date(31, 12, 2020)
    with pytest.raises(TypeError) as excinfo:
        date + 'cow'
    assert 'Second parameter should be of class "TimeDelta".' in str(excinfo.value)


# Test related to "__iadd__ method" and "__special_for_add_and_iadd private method"
@pytest.mark.parametrize("date, timedelta, expected",
                         [(Date(31, 12, 2020), TimeDelta(5, 5, 5), Date(5, 6, 2026)),
                          (Date(10, 9, 1990), TimeDelta(10, 10, 10), Date(20, 7, 2001))])
def test_iadd(date, timedelta, expected):
    date += timedelta
    assert date.day == expected.day
    assert date.month == expected.month
    assert date.year == expected.year


# Test related to "__iadd__ method"
def test_correct_type_iadd():
    date = Date(31, 12, 2020)
    with pytest.raises(TypeError) as excinfo:
        date += 'cow'
    assert 'Second parameter should be of class "TimeDelta".' in str(excinfo.value)
