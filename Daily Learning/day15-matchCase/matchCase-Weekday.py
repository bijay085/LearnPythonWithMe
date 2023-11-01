"""Match case for finding day of the week"""
# using integer number choice/match .

day = int(input("Enter the number of that day from 1 to 7: "))
# print("A/c to the day number you had inserted, the corresponding day will be:")

match day:
    case 1:
        print("1st day is Sunday.")
    case 2:
        print("2nd day is Monday.")
    case 3:
        print("3rd day is Tuesday.")
    case 4:
        print("3rd day is Wednesday.")
    case 5:
        print("3rd day is Thursday.")
    case 6:
        print("3rd day is Friday.")
    case 7:
        print("3rd day is Friday.")
    case _:
        print("Invalid day number .")
