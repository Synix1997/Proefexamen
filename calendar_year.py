from calendar_month import print_monthly_calendar


def calendar_year(year: int):
    for month in range(1,13):
        print_monthly_calendar(year, month)
        print()
        print()

if __name__ == '__main__':
    calendar_year(2024)