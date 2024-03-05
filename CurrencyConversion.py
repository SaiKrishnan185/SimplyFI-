def ind_currency(number):
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
            # Checking for comma insertion
            if i % 2 == 0 and i != 0:
                result = ',' + result
            result = new_string[length - i - 1] + result
        # Add last 3 removed digits to final result
        return result + ',' + number_string[-3:]


if __name__ == '__main__':

    # Test Set
    # test = [{
    #     'input': 0,
    #     'output': '0'
    # }, {
    #     'input': 1,
    #     'output': '1'
    # }, {
    #     'input': 5,
    #     'output': '5'
    # }, {
    #     'input': 55,
    #     'output': '55'
    # }, {
    #     'input': 123,
    #     'output': '123'
    # }, {
    #     'input': 1234,
    #     'output': '1,234'
    # }, {
    #     'input': 12345,
    #     'output': '12,345'
    # }, {
    #     'input': 123456,
    #     'output': '1,23,456'
    # }]
    #
    # for testValue in test:
    #     currency = ind_currency(testValue['input'])
    #     print(f'Input = { testValue["input"] }  Final Output = {currency}')

    input_value = int(input('Enter value to convert : '))
    currency = ind_currency(input_value)
    print(currency)

