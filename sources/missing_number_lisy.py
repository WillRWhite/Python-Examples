DEBUG = False
def main():
    # Multiple missing numbers
    missing_numbers = [0,2,3,5,6,7,8,9,10,12,13,15,16,20,21]
    # One missing number
    missing_number = [1,2,3,4,5,6,7,8,9,10,12,13,14,15,16,17]
    print(get_missing_numbers(missing_numbers))
    print(get_missing_number(missing_number))

# Function to finds missing numbers in a list (one or more missing)
def get_missing_numbers(number_list: list) -> list:
    missing_numbers = []
    current_index = 0
    if DEBUG == True:
        print(number_list)
    number_list_len = len(number_list)
    # Iterate through list using the index becahse the list may
    # increase if missing numbers found
    while current_index < number_list_len-1:
        current_number = number_list[current_index] 
        next_number = number_list[current_index+1]
        if next_number != current_number+1:
            missing_numbers.append(current_number+1)
            # Insert missing number in the list and decrement the index
            # to catch the case where there are consecutive missing numbers
            number_list.insert(current_index+1, current_number+1)
            # Decrement the index to re-test on the next itteration
            current_index-=1
            # Increase the list lenght by 1 
            number_list_len+=1
        # If no missing number, move on to the next number in the list
        current_index+=1
    if DEBUG == True:
        print(number_list)
    return missing_numbers

# Function to finds one missing number in a list (no itterating required)
# If they are more than one missing number it will return the sum of
# all missing numbers
def get_missing_number(number_list: list) -> int:
    # Calculate actual sum of the list
    actual_sum = sum(number_list)
    #Calculate sum assuming "complete" list from n to m
    n = number_list[0]                  # first number in list
    m = number_list[len(number_list)-1] # last number in list
    # Calculate sum from standard summation of integers from n to m
    expected_sum  = m*(m+1)/2 - n*(n+1)/2 + n
    missing_number = expected_sum-actual_sum
    return int(missing_number)


if __name__ == "__main__":
    main()
