countries_temperature = [
    ['Таиланд', [75.2, 77, 78.8, 73.4, 68, 75.2, 77]],
    ['Германия', [57.2, 55.4, 59, 59, 53.6]],
    ['Россия', [35.6, 37.4, 39.2, 41, 42.8, 39.2, 35.6]],
    ['Польша', [50, 50, 53.6, 57.2, 55.4, 55.4]]
]

def get_average_temperature(data):
    print('Средняя температура в странах:')
    for country_data in data:
        country_name = country_data[0]

        sum = 0
        for value in country_data[1]:
            sum += value

        avg_value_f = sum / len(country_data[1])
        avg_value_c = round((avg_value_f - 32) * 5 / 9, 1)
        print(country_name,'-',avg_value_c,'C')

get_average_temperature(countries_temperature)
