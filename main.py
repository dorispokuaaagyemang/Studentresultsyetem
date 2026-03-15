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
              "\n ========== Main Menu ========== \n"
              "1: Add Student \n"
          "2: Update Student \n"
          "3: Delete Student \n"
          "4: View All Student: \n"
          "5: Search Student \n"
          "6: exit to Main menu: \n"
           "select one to continue \n" 
           "\n ======= ======== =========\n"
         )
         if student_operation == "1":
               print(f"\n  =========== Add Student ============\n")
               
               full_name = input("Enter full name: \n").title().strip()
               gender = input("Enter [M]ale / [F]emale \n enter 'm' or 'f'").lower().strip()    
               Form = input("Enter your class or form \n").strip()
               dateofRegistration = input("date of Admission: \n").split() 


               # for _ in data:
               #      if data[-1]["student ID"] == :
               #           id_gen += 1
                 
               data_appending = {
          "student ID" : next(id_gen),
          "full name" : full_name,
          "gender" : gender,
          "form" : Form,
          "date of Adminission" : dateofRegistration
     }  
               data.append(data_appending)

               with open(file=student_file_path, mode="w") as file:
                 json.dump(data, file, indent=4)
     
         
          
         elif student_operation == "2":
              #update student details

              update_by_ID = input("enter  your Student ID \n").strip()

              for var in data:
                   if var["student ID"] == int(update_by_ID):
                        print(var["full name"],)
                        print(var["form"])
                        print(var["date of Adminission"])

                        var1 = input("Enter new Full name: \n").title().strip()
                        var2 = input ("enter new Gender [m]/[f] \n")
                        var3 = input("enter new class/form \n").strip()
                        var4 = input("enter new date of admission \n").strip().split()


                        var["student ID"] = update_by_ID
                        var["full name"] = var1
                        var["gender"] = var2
                        var["form"] = var3
                        var["date of Adminission"] = var4
                       

                        with open(file=student_file_path, mode="a") as file:
                             json.dump(var, file, indent=4)
                     
                        print(var)
                        break
                        
         

         elif student_operation == "3":
              pass
         elif student_operation == "4":
              pass
         elif student_operation == "5":
              pass
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