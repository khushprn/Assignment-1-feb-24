numbers = input("Enter a list of numbers separated by spaces or press enter to Exit : ")

num = [float(num) for num in numbers.split()]   #I read about these functions "split", "for" and "in" from Google

if num:
    smallest = min(num)  # I have the knowledge of "min" and "max" functions
    largest = max(num)

    print("The smallest number from list is:", smallest)
    print("The largest number from list is:", largest)
else:
    print("empty list. enter some numbers.")