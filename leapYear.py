#       leap year and next leap year checker

year = int(input("Enter year to check: "))
print("")

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("-----------------")
    print("Leap Year")
    print("-----------------")
else:
    print("-----------------")
    print("Not a Leap Year")
    print("-----------------")
    print("")
    nowYear = year
    nextYear = nowYear + 4

    for y in range(nowYear, nextYear):
        if (y % 4 == 0 and year % 100 != 0) or (y % 400 == 0):
            print("-----------------")
            print("Next Leap Year: ", y)
            print("-----------------")
            break
print("\nThank you for using this program.")

# (c) Subhrapratim Dutta
