def readint(txt):
    while True:
        try:
            n = int(input(txt))
        except(ValueError, TypeError):
            print('\033[31mERROR! Type a valid number!\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[mThe program was interrupted by the user!\033[m')
            return 0
        else:
            return n


def readfloat(txt):
    while True:
        try:
            n = float(input(txt))
        except(ValueError, TypeError):
            print('\033[31mERROR! Type a valid number!\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[mThe program was interrupted by the user!\033[m')
            return 0
        else:
            return n


def lin(siz=42):
    return '-' * siz


def header(txt):
    print(lin())
    print(txt.center(42))
    print(lin())


def menu(lis):
    header('Main Menu')
    c = 1
    for item in lis:
        print(f'{c} - {item}')
        c += 1
    print(lin())
    opt = readint('Chose an option: ')
    return opt

