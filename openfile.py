import csv
def open_file (file_name):
    ''' args file_name
        return nested list'''
    my_list = []
    try:
        with open(file_name, 'r') as csvfile: #close file after statement execute
            for rows in csv.reader(csvfile): #iterate through data
                my_list.append(rows)
    except Exception as e: # e-name associated with exception being passed
        print (e)
    return my_list



data = open_file("2020-presidential.csv")
print (data)
