def main():
    
    celcius = float(input('Enter celcius value:\n'))
    fahrenheit = ((9 / 5) * celcius) + 32

    print(f'Fahrenheit: {fahrenheit}')

    return celcius, fahrenheit


if __name__ == '__main__':
    main()
