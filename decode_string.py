import csv


with open('Piccolo\TX_5.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    list_s = []
    tx_list = []
    full_string = ''
    for row in csv_reader:
        #tx_list.append((row[0], row[2]))
        #print(row[2])
        if (len(full_string) < 1):
            full_string = row[2]
            list_s.append(row[2])
        else:
            if row[2] == '\\n' or row[2] == '\\r':
                continue
            else:
                if row[2] == 'm':
                    full_string += " "
                    full_string += row[2]
                else:
                    full_string += row[2]
                    if len(full_string) == 165:
                        full_string += " "
                    list_s.append(row[2]) 
#print("TX list ", tx_list)
print("Tx: ", full_string.split(' ')[4:])    


with open('Piccolo\RX_9.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    full_string = ''
    for row in csv_reader:
        
        if (len(full_string) < 1):
            full_string = row[2]
        else:
            if row[2] == '\\n' or row[2] == '\\r':
                continue
            else:
                if row[2] == 't' or row[2] == 'o':
                    full_string += " "
                    full_string += row[2]
                
                elif row[2] == 'k' or row[2] == 'm':
                    full_string += row[2]
                    full_string += " "
                else:
                    full_string += row[2]
print("Rx: ", full_string.split(' ')[4:])    
