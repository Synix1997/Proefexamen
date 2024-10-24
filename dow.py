def day_of_the_week(year: int, month: int, day: int) -> int:
    """

    :rtype: object
    """
    offset = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
    year -= month < 3
    dow = (year + year // 4 - year // 100 + year // 400 + offset[month-1] + day) % 7

    """
    day_of_the_week function
    
    Author: Sébastien De Ruyck
    Date: 22/10/2024
    
    Original function started with Sunday as day 1.
    For Europe we use Monday as day 1 and Sunday as day 7.
    Slightly altered the function to give the required result with day 1 = Monday.
    """
    if dow == 0:
        dow = 7

    return dow


def main():
    assert day_of_the_week(2022, 1, 1) == 6  # Sat
    assert day_of_the_week(2022, 12, 2) == 5  # Fri
    assert day_of_the_week(2022, 12, 3) == 6  # Sat
    assert day_of_the_week(2022, 12, 4) == 7  # Sun
    assert day_of_the_week(2022, 12, 5) == 1  # Mon
    assert day_of_the_week(2022, 12, 6) == 2  # Tue
    assert day_of_the_week(2022, 12, 7) == 3  # Wed


if __name__ == "__main__":
    main()
