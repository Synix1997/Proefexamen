from day_number import day_number
from dow import day_of_the_week


def week_number(year: int, month: int, day: int):
    dow = day_of_the_week(year, month, day)  # Get the day of the week (1=Monday, ..., 7=Sunday)
    days = day_number(year, month, day)  # Get the day number in the year
    week = (days - dow) // 7 + 1  # Calculate the week number
    return week

def main():
    assert week_number(2024, 1, 3) == 1
    assert week_number(2024, 3, 16) == 11
    assert week_number(2024, 12, 29) == 52


if __name__ == "__main__":
    main()
