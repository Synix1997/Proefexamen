from date_string import name_of_month, name_of_day
from dom import days_of_month
from dow import day_of_the_week


def calendar_month_and_year(year: int, month: int) -> int:
    print(f"{name_of_month(month)} {year}")
    print()

def days_abbreviations():
    for day in range(1, 8):
        print(name_of_day(day), end=" ")
    print()

def days_for_monthly_calendar(year: int, month: int):
    # Get the number of days in the month
    total_days = days_of_month(year, month)

    # Find the starting day of the week for the 1st of the month
    start_day = day_of_the_week(year, month, 1)

    # Print spaces for the first week until the first day of the month
    print("   " * (start_day - 1), end="")

    for day in range(1, total_days + 1):
        print(f"{day:2}", end=" ")
        if (start_day + day - 1) % 7 == 0:
            print()

def print_monthly_calendar(year: int, month: int):
    calendar_month_and_year(year, month)
    days_abbreviations()
    days_for_monthly_calendar(year, month)

if __name__ == "__main__":
    print_monthly_calendar(2024, 2)



