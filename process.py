log_file = open("um-server-01.txt")
#pulling infromation from um-server

def sales_reports(log_file):
    #function
    for line in log_file:
        #for loop runnning over every line in um-server
        line = line.rstrip()
        #striping spaces out of um-server
        day = line[0:3]
        #pulling at index 0 and 3
        if day == "Mon":
            #only getting indexes from lines that meet requirement
            print(line)
            #displaying lines


sales_reports(log_file) #calles above function
