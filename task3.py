def odd_even_counter(number):
    number_list = [0,0]
    while number !=0:
        if number % 2 == 0:
            number_list[0] = number_list[0] + number
        else:
            number_list[1] = number_list[1] + number

        number = number - 1
        return number_list
    number = int(input("Please Enter a Number"))
    print(odd_even_counter(number))