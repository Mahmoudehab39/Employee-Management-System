####################################################################################  employee CLASS  #####################################################################################

class employee:                      ## Class employee 
    cls_list=[]

    def Set_Update(self):                 ##Update Method to sort the table as the user want by ID or Salary and Ascent or Descent
        n = len(employee.cls_list)
        print("\nIn this step, you should choose the data that will be saved in the CSV file, arranged by ID or salary.\n")

        while True:
            try:
                sort_column = int(input("Please enter 0 if you want to arrange data depending on ID or enter 3 if you want to arrange data depending on salary: "))
                if sort_column == 0 or sort_column == 3:
                    break
                else:
                    print("\nPlease Try again :( , Please enter 0 or 3 \n")
            except:
                print("\nPlease Try again :( , Please enter 0 or 3 \n")

        while True:
            arange = input("Please enter a if you want to arrange data by ascent or d if you want to arrange data by descent: ")
            if arange == 'a' or arange == 'd':
                break
            else:
                print("\nPlease Try again :( , Please enter a or d \n")

        for i in range(n):
            already_sorted = True
            for j in range(n - i - 1):
                if arange  == 'a':
                    if int(employee.cls_list[j][sort_column]) > int(employee.cls_list[j + 1][sort_column]):
                        employee.cls_list[j], employee.cls_list[j + 1] = employee.cls_list[j + 1], employee.cls_list[j]
                        already_sorted = False
                elif arange  == 'd':
                    if int(employee.cls_list[j][sort_column]) < int(employee.cls_list[j + 1][sort_column]):
                        employee.cls_list[j], employee.cls_list[j + 1] = employee.cls_list[j + 1], employee.cls_list[j]
                        already_sorted = False
            if already_sorted:
                break

    @classmethod
    def Get_Displayy(cls,list):                           ##Display Method to display the Employees table
        header = list[0]
        all_data = []
        for i in list:
            if i[0] == "id":
                continue
            all_data.append(i)
        indexed_data = [[i+1] + row for i, row in enumerate(all_data)]
        print(tabulate(indexed_data, headers = ["Number of employees",header[0],header[1],header[2],header[3],header[4]], tablefmt = "grid")) 
            
####################################################################################  employee_Manger CLASS   ############################################################################
       
class employee_Manger(employee):    ##Class employee_Manger

    @classmethod
    def Set_Create(cls):               ## Create Method to Create a New Employee ID , Name , Position , Salary , Email
        while True:
            r =[]

            while True:
                try:
                    t=int(input("Please enter an employee ID: "))
                    r.append(t)
                    n=[i[0] for i in employee.cls_list]
                    if int(r[0]) >= 0 and str(r[0]) not in  n :
                        r[0] = str(r[0])
                        break
                    else:
                        print("\nTry again :( , Please enter ID that not exist in a table above \n")
                        r.remove(r[0])
                except:
                    print("\nTry again :( , Please enter ID that not exist in a table above\n")
            r.append(input("Please enter an employee name: "))      
            r.append(input("Please enter an employee position: "))

            while True:  
                try:
                    t=  int(input("Please enter an employee salary: "))
                    r.append(t)
                    if int(r[3]) >= 0:
                        r[3] = str(r[3])
                        break
                    else:
                        print("\nTry again :( , Please enter salary in numbers\n")
                        r.remove(r[3])
                except:
                    print("\nTry again :( , Please enter salary in numbers\n")

            while True:    
                r.append(input("Please Enter An Employee Email: "))
                if r[4].find("@gmail.com") != -1:
                    break
                else:
                    print("\nTry again :( , Please contain '@gmail.com' in the mail\n")
                    r.remove(r[4])
            print("\nThank You\n")
            employee.cls_list.append(r)
            break

    @classmethod    
    def Get_Read(cls,id):                            ## Read Method to display a specific employee data
        for i in employee.cls_list:
            if i[0] == id:
                print("\n")
                print(tabulate([i], headers = employee.cls_list[0], tablefmt = "grid"))
                break
    
    @classmethod            
    def Set_Update(cls,index,row):                  ## Update Method to update a Employee ID , Name , Position , Salary , Email
        cont = True
        while cont:

            print(f"\nThe Employee Deatails: ID: {row[0]} , Name: {row[1]} , Position: {row[2]} , Salary: {row[3]} , Email: {row[4]}\n")
            print("""
                    |press 1 to change id
                    |press 2 to change name
                    |press 3 to change position
                    |press 4 to change salary
                    |press 5 to change email \n""" )
            
            while True:
                try:
                    answer = int(input("so what do you want to modify: "))
                    if answer > 0 and answer < 6:
                        answer = str(answer)
                    
                        if answer == '1':
                            while True:
                                try:
                                    new = int(input("\nThe New ID will Equal: "))
                                    n=[i[0] for i in employee.cls_list]
                                    if new >= 0 and str(new) not in  n :
                                        new=str(new)
                                        row[0] = new
                                        break
                                    else:
                                        print("\nTry again :( , Please enter ID that not exist in a table above\n")
                                except:
                                    print("\nTry again :( , Please enter ID that not exist in a table above\n") 

                        elif answer == '2':
                            new = input("\nThe New Name will Equal: ")
                            row[1] = new

                        elif answer == '3':
                            new = input("\nThe New Position will Equal: ")
                            row[2] = new

                        elif answer == '4':

                            while True:
                                try:
                                    new = int(input("\nThe New Salary will Equal: "))
                                    if new >= 0:
                                        new=str(new)
                                        row[3] = new
                                        break
                                    else:
                                        print("\nTry again :( , Please enter salary in numbers\n") 
                                except:
                                    print("\nTry again :( , Please enter salary in numbers\n") 

                        elif answer == '5':
                            while True:
                                new = input("\nThe New Mail will Equal: ")
                                if new.find("@gmail.com") != -1:
                                    row[4] = new
                                    break
                                else:
                                    print("\nTry again :( , Please contain '@gmail.com' in the mail\n")     

                        print(f"\nThe New Deatails: ID: {row[0]} , Name: {row[1]} , Position: {row[2]} , Salary: {row[3]} , Email: {row[4]}\n")
                        while True:
                            an = input("\nDo you Want to change other details press y if yes and n if no: ")
                            if an == 'y' or an == 'n':
                                break
                            else:
                                print("\nPlease try again and enter y or n\n")
                        if an =='y':
                            cont = True
                        elif an == 'n':
                            cont = False
                        employee.cls_list[int(index)] = [row[0],row[1],row[2],row[3],row[4]]
                        break

                    else:
                        print("\nTry again :( , Please enter number from 1 to 5\n")

                except:
                        print("\nTry again :( , Please enter number from 1 to 5\n") 
            
    @classmethod
    def Set_Delete(cls,id):         ##Delete Method to delete a specific employee and its data from the system
        for i in employee.cls_list:
            if i[0] == id:
                employee.cls_list.remove(i)
            
####################################################################################  OPENING ##########################################################################

def OPENING():
    print("""
            H         H        EEEEEEEEEEE        LL                 LL                   OOOOOOO
            H         H        E                  LL                 LL                 O         O
            H         H        E                  LL                 LL                 O         O
            HHHHHHHHHHH        EEEEEEEEEEE        LL                 LL                 O         O
            H         H        E                  LL                 LL                 O         O
            H         H        E                  LL                 LL                 O         O
            H         H        EEEEEEEEEEE        LLLLLLLLLLL        LLLLLLLLLLL          OOOOOOO
            """)
    print("Welcome To The EMPLOYEE MANAGER SYSTEM  :)\n")
    print("This System Display All Employees With Their Details Such As ID, NAME, POSITION, SALARY, AND THE EMAIL\n")

####################################################################################  READ_FILE FUNCTION  #########################################################################

def READ_FILE():             ## Read Function To Read CSV File 
    
    with open(CSV_File, mode='r') as file:
            csvFile = csv.reader(file)            
            for i in csvFile:
                a=[]
                for ii in i:
                    a.append(ii)
                employee.cls_list.append(a)
    

####################################################################################  MENU  #########################################################################

def MENU():
    print("ENTER NUMBER FROM 1 TO 6 each NUMBER serve you Specific Service \n")
    print("           | Enter 1 If you Want To Add An Employee with his details")
    print("           | Enter 2 If you Want To Update An Employee details")
    print("           | Enter 3 If you Want To Display A Specific Employee with his details")
    print("           | Enter 4 If you Want To Delete An Employee")
    print("           | Enter 5 If you Want To Display All Employees with their details")
    print("           | Enter 6 If you Want To Exit The System")

####################################################################################  SYSTEM FUNCTION  #########################################################################

def SYSTEM(again):
    
    if again == '1':
        employee.Get_Displayy(employee.cls_list)
        print("\nWelcome To the ADD An Employee Details Part")
        print("\nIn This Part You Will ADD the Employee Details Such As ID, NAME, POSITION, SALARY, AND THE EMAIL \n")
        employee_Manger.Set_Create()
      
    elif again == '2':
        employee.Get_Displayy(employee.cls_list)
        print("\nWelcome To the UPDATE An Employee Details Part")
        print("\nIn This Part You Will UPDATE the Employee Details Such As ID, NAME, POSITION, SALARY, AND THE EMAIL Each one of them One Time \n")
        while True:
            try:
                index = int(input("Please Enter The Employee number that you want to Change: "))
                n=[i[0] for i in employee.cls_list]
                if  index in range(1,len(n)):
                    employee_Manger.Set_Update(index,employee.cls_list[int(index)])
                    break
                else:
                    print("\nTry again :( , Please enter employee number that exist in the table above \n")
            except:
                print("\nTry again :( , Please enter employee number that exist in the table above\n")
 
    elif again == '3':
        print("\nWelcome To the Display A Specific Employee with his Details Part")
        print("\nIn This Part You Will Display the Employee Details Such As ID, NAME, POSITION, SALARY, AND THE EMAIL \n")
        while True:
            try:
                id = int(input("\nPlease Enter The Employee ID that you want to Display: "))
                n=[i[0] for i in employee.cls_list]
                if id >=0 and str(id) in n :
                    id = str(id)
                    employee_Manger.Get_Read(id)
                    break
                else:
                    print("\nTry again :( , Please enter ID that exists in a table above")
            except:
                print("\nTry again :( , Please enter ID that exists in a table above\n")
            
    elif again == '4':
        employee.Get_Displayy(employee.cls_list)
        print("\nWelcome To the Delete An Employee Part")
        print("\nIn This Part You Will Delete the Employee  \n")
        while True:
            try: 
                id = int(input("Please Enter The Employee ID that you want to Delete: "))
                n=[i[0] for i in employee.cls_list]
                if id >=0 and str(id) in n :
                    id = str(id)
                    employee_Manger.Set_Delete(id)
                    break
                else:
                    print("\nTry again :( , Please enter ID that exists in a table above\n")
            except:
                print("\nTry again :( , Please enter ID that exists in a table above\n")
         
    elif again == '5':
        employee.Get_Displayy(employee.cls_list)

    first_row=employee.cls_list.pop(0)
    if again == '1' or  again == '2' or again == '4': 
        employee.Set_Update(employee.cls_list)
    employee.cls_list.insert(0,first_row)

####################################################################################  WRITE_IN_Funcrtion #########################################################################

def WRITE_IN_Funcrtion(again):     ## Write Function to write data in the CSV file
    if again == '1' or  again == '2' or again == '4':
        with open(CSV_File, 'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerows(employee.cls_list)
            print("\nWell Done\n")

####################################################################################  MAIN FUNCTION #########################################################################

import csv
from tabulate import tabulate
CSV_File = "Project_System.csv"
again = 0   
OPENING()
READ_FILE()

while  True:
    MENU() 
    while True:
        try:
            again = int(input("\nEnter Your Choice Please: ")) 
            if again in range(1,7):
                print("\n")
                again = str(again) 
                break
            else:
                print("\ntry again :( , Please Enter number from 1 t0 6")
        except:
            print("\ntry again :( , Please Enter number from 1 t0 6")

    SYSTEM(again)
    
    if again == '6':
        print("Thank you for using our system, and we hope you had a wonderful experience :)\n")
        break
    WRITE_IN_Funcrtion(again)

        
        


    


