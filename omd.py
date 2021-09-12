# Guido van Rossum <guido@python.org>

def step1():
    print(
        'Утка-маляр 🦆 решила выпить зайти в бар. '
        'Взять ей зонтик? ☂️'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()

    if options[option]:
        return step2_umbrella()
    return step2_no_umbrella()

def step2_umbrella():
    print(
        'Утка-маляр 🦆 взяла зонтик. '
        'Она молодец'
    )

def step2_no_umbrella():
    print(
        'Утка-маляр 🦆 не взяла зонтик. '
        'Она молодец'
    )

if __name__ == '__main__':
    step1()