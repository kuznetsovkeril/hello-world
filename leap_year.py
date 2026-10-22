def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0


def is_leap_year_elif(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False


if __name__ == "__main__":
    year = int(input("Введите год: "))
    if is_leap_year(year):
        print("високосный")
    else:
        print("НЕ високосный")
