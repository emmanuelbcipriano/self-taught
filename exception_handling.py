input = input('Please type an integer')

def convert(string):

    try:

        return int(string)

    except ValueError:

        return 'Please type a valid number'

print(convert(input))