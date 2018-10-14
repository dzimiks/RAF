def convertToFahrenheit(temp):
    return 1.8 * temp + 32


cels = float(input('Enter a temperature in Celsius: '))
print('Celsius: %.2f, Fahrenheit: %.2f' % (cels, convertToFahrenheit(cels)))
