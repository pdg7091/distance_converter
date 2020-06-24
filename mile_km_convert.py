# convert miles to kilometers or opposite:


def print_option():
    print('1. Kilometers to Miles')
    print('2. Miles to Kilometers\n')


def km_miles():
    km = float(input('Please enter your distance in kilometers: '))
    miles = km / 1.609

    print(f'Distance in miles: {miles}')


def miles_km():
    miles = float(input('Please enter your distance in miles: '))
    km = miles * 1.609

    print(f'Distance in kilometers: {km}')


if __name__ == '__main__':
    print_option()
    choice = input('Which conversion would you like to see?: ')
    if choice == '1':
        km_miles()

    if choice == '2':
        miles_km()
