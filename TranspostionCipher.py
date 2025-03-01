import math

TestMode = False

#Get Plaintext and Key
plaintext = input('Enter plaintext: ').replace(" ","")
key = input('key:')

if not key:
    print("Invalid key. Key cannot be empty.")
    exit()

#Create sequence + grid
sequence = ''.join(sorted(key, key=str.lower))
grid = math.ceil(len(plaintext)/len(key))

#Split plaintext based on key
rows = [plaintext[i * len(key):(i + 1) * len(key)] for i in range(grid)]
row_dict = {f"row{index}": row for index, row in enumerate(rows, start=1)}

#Pull columns
columns = [''.join(row[i] for row in rows if i < len(row)) for i in range(len(key))]
Columns = ''.join(columns)

#Rearrange Columns
sort = sorted(range(len(key)), key=lambda i: key[i].lower())
Jargan = [''.join(columns[i] for i in sort)]
sortedcolumns = ''.join(Jargan)

if TestMode == False:
    print()
    print('Scramble:\n',sortedcolumns)

#test prints
if TestMode == True:
    print()
    print('Plaintext:',plaintext)
    print()
    print('Key:',key)
    print('Alphabetized Key:',sequence)
    print()
    for i in range(1, grid+1):
        print(row_dict[f'row{i}'])
    print()
    print(grid)
    print()
    print(Columns)
    print()
    print(sort)
    print(sortedcolumns)
