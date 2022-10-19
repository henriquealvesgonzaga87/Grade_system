from lib.Interface import header


def checkfile(name):
    try:
        a = open(name, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def creatfile(name):
    try:
        a = open(name, 'xt')
        a.close()
    except:
        print('Error to create the file!')
    else:
        print(f'{name} was created!')


def readfile(name):
    try:
        a = open(name, 'rt')
    except:
        print('Error to read the file!')
    else:
        header('Students registered')
        for line in a:
            data = line.split(';')
            data[-1] = data[-1].replace('\n', '')
            print(f'{data[0]:<5} - {data[1]:<5} - {data[2]:<5} - {data[3]:<5}')
    finally:
        a.close()


def addstudents(arq, name, grades, average, situation):
    try:
        a = open(arq, 'at')
    except:
        print('Error to open the file!')
    else:
        try:
            a.write(f'{name};{grades};{average:.2f};{situation}\n')
        except KeyboardInterrupt:
            print('\033[31mThe program was interrupted by the user!\033[m')
        except:
            print('Error to add the student!')
        else:
            print(f'{name} was registered!')