import json
import os 
import sys 
from json import JSONDecodeError




def main():
    ff = result_management_system()
    print(ff)
   

def result_management_system():
    
    while True:
          message = input (
                "1: Manage Student \n"
                "2: Manage Subjects \n"
                "3: Enter Results \n"
                "4: View Results \n"
                "5: Generate report \n"
                "6: Exit \n"
                "Select number to continue \n"

            ).strip()

          if message == "1":
                 manage_student()
          elif message == "2":
                 manage_subjects()
          elif message == "3":
               data_entry()
          elif message == "4":
               view_results()
          elif message == "5":
               generate_results()
          elif message == "6":
               print("Program exited")
               sys.exit()
          else:
               print("invalid choice: \n")

          



def manage_student():
     student_file_path = os.path.join("config", "student.json")
     try:
          with open(file=student_file_path, mode="r") as file:
               data = json.load(file)
     except (JSONDecodeError, FileExistsError, FileNotFoundError):
          data = []
     
     while True:
         student_operation = input(
                              "\n ========== Student Menu ========== \n"
                              "1: Add Student \n"
                                   "2: Update Student \n"
                                   "3: Delete Student \n"
                                   "4: View All Student: \n"
                                   "5: exit to Main menu: \n"
                                   "select one to continue \n" 
                                   "\n ======= ======== =========\n"
                         )
         if student_operation == "1":
               print(f"\n  =========== Add Student ============\n")
               
               first_name = input("Enter First name: \n").title().strip()
               last_name = input("Enter first name: \n").title().strip()
               gender = input("Enter [M]ale / [F]emale \n enter 'm' or 'f' \n").lower().strip()    
               Form = input("Enter your class or form \n").strip()
               dateofRegistration = input("date of Admission: \n").split() 


               # for _ in data:
               #      if data[-1]["student ID"] == :
               #           id_gen += 1
                 
               data_appending = {
                              "student ID" : next(id_gen),
                              "first name" : first_name,
                              "last name" : last_name,
                              "gender" : gender,
                              "form" : Form,
                              "date of Adminission" : dateofRegistration
                                }  
               data.append(data_appending)

               with open(file=student_file_path, mode="w") as file:
                 json.dump(data, file, indent=4)
     
         
          
         elif student_operation == "2":
              #update student details
              print("\n===== Update Student Information ===== \n")

              update_by_ID = int( input("enter  your Student ID \n").strip())

              if len(data) == 0:
                   print("Data Not Found")
                   break
              else:
                   for  index,value in enumerate(data):
                        if value["student ID"] == update_by_ID:
                             print(data[index], end="\n")
                             print("\nYou about to update you Data\nStudent ID cant be updated ..... \nb")

                             firstname = input("Enter full name: \n").title().strip()
                             lastname = input("Enter full name: \n").title().strip()
                             new_gender = input("Enter [M]ale / [F]emale \n enter 'm' or 'f'").lower().strip()    
                             new_form = input("Enter your class or form \n").strip()
                             new_dateofRegistration = input("date of Admission: \n").split() 

                             data[index]["student ID"] = update_by_ID
                             data[index]["first name"] = firstname
                             data[index]["last name"] = lastname
                             data[index]["gender"] = new_gender
                             data[index]["form"] = new_form
                             data[index]["date of Adminission"] = new_dateofRegistration

                             with open(file=student_file_path, mode="w") as f:
                                  json.dump(data, f, indent=4)
                             print(F"\n{lastname}, your New data has been updatedly successfully... \n")







                             break
                        
         

         elif student_operation == "3":
              #delete Student
              print("\n===== Removing Student information =====\n")
              update_ID = int( input("enter  your Student ID \n").strip())
              for  index,value in enumerate(data):
                        if value["student ID"] == update_ID:
                             print(data[index], "\n", "data will be deleted from our system\n")

                             caution = input("do you want to delete your data? y /n \n").strip().lower()
                             if caution == "y" or caution == "yes":
                                  data.remove(data[index])
                                 
                                 
                                  with open(file=student_file_path, mode="w") as f:
                                    json.dump(data, f, indent=4)
                                  print("\nStudent Information Deleted Successfully\n")
                                  break
                             else:
                                  print("\n ... Student Student Deletion Aborted... \n")
          


             
         elif student_operation == "4":
              counter =1
              
              for  index,value in enumerate(data):
                   print(f"\n==== Student No:{counter} ====\n")
                   print(f"Student ID:{value["student ID"]} ")
                   print(f"First Name:{value["first name"]} ")
                   print(f"Last name:{value["last name"]} ")
                   print(f"Gender:{value["gender"]} ")
                   print(f"Student class:{value["form"]} ")
                   print(f"Date of Admission:{value["date of Adminission"]} \n")
                   counter +=1

         else:
              return
         

 

         


def student_id_generator():



     start = 100
     
     while start > 0:
          yield start
          start +=1 
          

id_gen = student_id_generator()
          



     
    

     

     
    
     


     





def manage_subjects():
     pass

def data_entry():
     pass


def view_results():
     pass



def generate_results():
     pass








if __name__ == "__main__":
    main()