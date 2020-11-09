import pandas as pd
import numpy as np




    


##A list of the writing ncessary in the program's front-end interface
def menu (index):
    print('\n\n')
    if index == 0:
        print('1. Read CSV file')
        print('2. Help uploading CSV file')
        
    elif index == 1:
        print ('1.Analyze General Sales Perfomance')
        print ('2.Analyze Specific Category Sale Performance')
        print ('3.Analyze Customer preferances')
        print ('4.Quit Program')
        print('Enter 0 to return to back to Main-Menu')
    elif index == 999:
        print ('The CSV file should be in format :',
               '\t1.Item_Category (Electronics,Grocery,Stationary,Clothing)',
               '\t2.Item_Name','\t3.Original Price','\t4.Selling Price',
               '\t5.Customer_Name','C\t6.ard_Type(VISA/MasterCard)',sep='\n')
        print ('Save the CSV file as \'sales.csv\'')
        print ('\nEnter to exit help menu...')
        
