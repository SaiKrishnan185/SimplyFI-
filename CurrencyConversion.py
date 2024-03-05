def ind_currency(number):
    """
        Converts an integer value into Indian currency notation.

        Parameters:
            number (int): The integer value to be converted.

        Returns:
            str: Indian currency notation of the input integer.

        Example:
            >>> ind_currency(1234)
            '1,234'
    """

    number_string = str(number)
    length = len(number_string)

    # Requires no conversion if length less than 4
    if length <= 3:
        return number_string
    else:
        # Separating last 3 digits
        new_string = number_string[:-3]
        length = length - 3
        result = ""
        # Iterating in reverse order for comma insertion
        for i in range(length):
            if i % 2 == 0 and i != 0:
                result = ',' + result
            result = new_string[length - i - 1] + result
        # Add last 3 removed digits to final result
        return result + ',' + number_string[-3:]


if __name__ == '__main__':
    input_value = int(input('Enter value to convert : '))
    currency = ind_currency(input_value)
    print(currency)

