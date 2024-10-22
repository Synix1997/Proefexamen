from calendar_month import print_monthly_calendar
from week_number import week_number


def calendar_year_and_weeknumber(year: int):
    for month in range(1, 13):
        week_num = week_number(year, month, 1)  # Calculate the week number for the first day of the month
        print(f"[{week_num}]", end=" ")  # Print the week number
        print_monthly_calendar(year, month)  # Print the monthly calendar
        print()  # New line after each month

if __name__ == "__main__":
    calendar_year_and_weeknumber(2024)
