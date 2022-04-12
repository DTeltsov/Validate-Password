import re

with open("test.txt", encoding='utf-8') as f:
    valid_passwords = 0
    for line in f:
        if line != '\n':
            # Split string into elemets by space.
            # So we will get list like this: ['symbol','range','password']
            line = line.split()
            symbol = line[0]
            # Find digits in line to define range
            temp = re.findall(r'\d+', line[1])
            # Get a list of 2 numbers which will be start and end of range.
            res = list(map(int, temp))
            # Count occurrences of a symbol in a string
            counter = line[2].count(symbol)
            if res[0] <= counter <= res[1]:
                print('{} valid password\n'.format(line[2]))
                valid_passwords += 1
            else:
                print('{} not valid password\n'. format(line[2]))
    print('Total number of valid passwords: {}'.format(valid_passwords))