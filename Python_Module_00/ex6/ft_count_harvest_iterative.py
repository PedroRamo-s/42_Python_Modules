def ft_count_harvest_iterative() -> None:
    days_to_harvest: int = int(input("Days until harvest: "))
    for i in range(1, days_to_harvest + 1):
        print(f"Day {i}")
    print("Harvest time!")
    return
