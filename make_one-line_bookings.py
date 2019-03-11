# -*- coding: utf-8 -*-
"""
Created on Sat Sep  8 19:10:10 2018

@author: diana
"""
#!/opt/rh/rh-python36/root/usr/bin/python

#Question 3a to use sys.argv
import csv
import sys
inputfile = sys.argv[1]
outputfile = sys.argv[2]
csvout = open(outputfile, 'w')
recordwriter = csv.writer(csvout, dialect='unix', quoting=csv.QUOTE_MINIMAL)

with open(inputfile) as csvfile:
    recordreader = csv.reader(csvfile, dialect='unix')
    row = []
    for line in recordreader:
        row.extend(line)
        if line[0][:12]=='RELEASE DATE':
            recordwriter.writerow(row)
            row = []
        #print(row)
        
csvout = open('cleanfile', 'w')
recordwriter = csv.writer(csvout, dialect='unix', quoting=csv.QUOTE_MINIMAL)


#Question 3b
# this is the function to check empty fields
def isBlank (teststr):
    return not (teststr and teststr.strip())
# we use the outputfile from Question 3a
with open(outputfile) as csvfile:
    recordreader = csv.reader(csvfile, dialect='unix')
    emptyfield = []
    count = 0
    row = []
    for line in recordreader:
        #print("before ", line)
        for i in range(len(line)):
            if isBlank(line[i]):
                emptyfield.append(i)
                
        #print(emptyfield)
        
        for i in range(len(emptyfield)-1,-1,-1):
            #print("deleted at ",emptyfield[i])
            line.pop(emptyfield[i])
            #print("after delete = ", line)
        emptyfield = []
            
        #print("after ", line)
        row.extend(line)
        recordwriter.writerow(row)
        row = []
        
#Question 3c and d. Separate the output into 2 csv's 
        
csvout1 = open('bookingsB_charges.csv', 'w')
recordwriter1 = csv.writer(csvout1, dialect='unix', quoting=csv.QUOTE_MINIMAL)
row1 = ['bookingNumber', 'chargeType','charge', 'court', 'caseNumber']
recordwriter1.writerow(row1)
        
csvout2 = open('bookingsB_info.csv', 'w')
recordwriter2 = csv.writer(csvout2, dialect='unix', quoting=csv.QUOTE_MINIMAL)
row2 = ['bookingNumber', 'name', 'agency', 'ABN', 'race', 'sex', 'e', 'DOB',
        'address', 'POB', 'releaseDate', 'releaseCode', 'SOID']
recordwriter2.writerow(row2)
                   
with open('cleanfile') as csvfile:
    recordreader = csv.reader(csvfile, dialect='unix')
     
    row = []
    for line in recordreader:
        name=""
        bookingNumber=""
        agency=""
        ABN=""
        race=""
        sex=""
        e=""
        DOB=""
        chargeType=""
        charge=""
        court=""
        caseNumber=""
        address=""
        POB=""
        releaseDate=""
        releaseCode=""
        SOID=""
        
        name = line[0]
        #if name is empty, we skip the line
        if not (line[0].find(",")== -1):
            continue
            
        bookingnumber=line[1]
        agency=line[2]
        linenbr = 0
        if line[3].find("/") == -1:
            ABN=line[3]
            splitrace = line[4]
            race = line[4].split("/ ")[0].strip()
            sex = line[4].split("/ ")[1].strip()
            e = line[4].split("/ ")[2].strip()
            DOB = line[4].split("/ ")[3].strip()
            linenbr = 5
        else:
            ABN=''
            splitrace = line[3]
            race = line[3].split("/ ")[0].strip()
            #print (race)
            sex = line[3].split("/ ")[1].strip()
            #print (sex)
            e = line[3].split("/ ")[2].strip()
            #print (e)
            DOB = line[3].split("/ ")[3].strip()
            #print (DOB)
            linenbr =4
      
        #print ('name', name)
        #print ('bn', bookingnumber)
        #print ('agency',agency)
        #print ('ABN', ABN)
        #print ("mysplit", splitrace)
       
        chargeType=[]
        charge=[]
        court=[]
        caseNumber=[]
        i=0
        index = 0
        #print("line: ", line)
        for i in range(linenbr, len(line), 4):
            if not line[i].startswith("ADDRESS"):
                chargeType.append(line[i])
                #print(i, chargeType)                
                
                index = i + 1
                if not line[index].startswith("ADDRESS"):
                    charge.append(line[index])
                else:
                    charge.append("")
                    court.append("")
                    caseNumber.append("")
                    i = index
                    break
                #print(index, charge)                

                index= i + 2
                if not line[index].startswith("ADDRESS"):
                    court.append(line[index])
                else:
                    court.append("")
                    caseNumber.append("")
                    i = index
                    break
                #print(index, court)

                index= i + 3
                if not line[index].startswith("ADDRESS"):
                    caseNumber.append(line[index])
                else:
                    caseNumber.append("")
                    i = index
                    break
                #print(index, caseNumber)

            else:
                break
            
        address=line[i]
        POB=line[i+1]
        releaseDate=line[i+2]
        releaseCode=line[i+3]
        SOID=line[i+4]
        
        
        # to separate the file
        
        row1 =[]
        
        #because charge type can have multiple records
        for i in range(len(chargeType)):
            row1.append(bookingnumber)
            row1.append(chargeType[i])
            row1.append(charge[i])
            row1.append(court[i])
            row1.append(caseNumber[i])
            recordwriter1.writerow(row1)
            row1 =[]
            
        row2 =[]
        
         
        
       
                       
    
        
    
