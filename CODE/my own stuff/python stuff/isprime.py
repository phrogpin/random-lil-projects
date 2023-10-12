def is_prime(number):
    # return true if number is prime and false otherwise
    if number <= 1:
        return False
    
    if number <= 3:
        return True
    
    if number % 2 == 0 or number % 3 == 0:
        return False
    
    i = 5
    
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    
    return True

# main program loop
while True: 
    # error handler for idiots that think charaters are numbers
    try:
        user_input = int(input("Enter a number: "))
        if user_input < 2:
            print("prime numbers start from 2 and above")
            
        else:
            print("prime numbers up to", user_input, "are: ")
            for number in range(2, user_input + 1):
                if is_prime(number):
                    print(number, end = " ")

    except ValueError:
        print("please enter a valid integer")
    
