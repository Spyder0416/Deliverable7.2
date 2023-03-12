import pandas as pd

# Ask the user to enter an integer value greater than 0
n = int(input("Enter an integer greater than 0: "))

# Use a conditional statement to check the user's entry is greater than 0
if n > 0:
    # Create a list for each sequence, and store the numbers of sequences
    even_nums = [2 * i for i in range(n)]
    odd_nums = [2 * i + 1 for i in range(n)]
    fib_nums = [0, 1]
    for i in range(2, n):
        fib_nums.append(fib_nums[i-1] + fib_nums[i-2])

    # Display your results in a data frame format
    df = pd.DataFrame({'Even': even_nums, 'Odd': odd_nums, 'Fibonacci': fib_nums})
    print(df)
else:
    print("Invalid input. Please enter an integer greater than 0.")
