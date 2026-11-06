def ft_harvest_helper(harvest_day, current_day):
    if (current_day > harvest_day):
        print("Harvest time!")
        return
    print(f"Day {current_day}")
    ft_harvest_helper(harvest_day, current_day + 1)
    return


def ft_count_harvest_recursive():
    days_to_harvest: int = int(input("Days until harvest: "))
    ft_harvest_helper(days_to_harvest, 1)
    return
