import json
import os 
import sys 
from json import JSONDecodeError



#load student file into memory
student_file_path = os.path.join("config", "student.json")
try:
     with open(file=student_file_path, mode="r") as file:
          data = json.load(file)
except (JSONDecodeError, FileExistsError, FileNotFoundError):
     data = []




#load Subject file into memory
subject_file = os.path.join("config", "subject.json")
try:
     with open (file=subject_file, mode="r", encoding="utf-8") as file:
          subject_data = json.load(file)
except (JSONDecodeError, FileNotFoundError):
     subject_data = []
     
   
   
     
     
#load results file into memory     
results_file = os.path.join("config", "result.json")
try:
     with open (file=results_file, mode="r", encoding="utf-8") as f:
          results_data = json.load(f)
except (JSONDecodeError, FileNotFoundError, FileExistsError):
     results_data = []     


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
               last_name = input("Enter last name: \n").title().strip()
               gender = input("Enter [M]ale / [F]emale \n enter 'm' or 'f' \n").lower().strip()    
               Form = input("Enter your class or form, [1, 2, 3] \n").strip()
               Form if Form in [1, 2, 3] else None
               dateofRegistration = input("date of Admission: eg 27 01 2026 \n").split() 


               for _ in data:
                    id_gen =(data[-1]["student ID"])+1
                   
                 
               data_appending = {
                              "student ID" : id_gen,
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

                             firstname = input("Enter first name: \n").title().strip()
                             lastname = input("Enter last  name: \n").title().strip()
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
         

 



def manage_subjects():
     print("====== Subject Menu ====== \n")
    

     
     while True:
          user_choice = input(
          "1: Add Subject \n"
          "2: view Subject \n"
          "3: delete Subject\n"
          "4:Go Back to Main Menu \n"
          "Select one to continue"
     )

          if user_choice == "1":
          
               subject_to_id_match = {
               "physics" : "SUB-100",
               "chemistry" : "asub-101",
               "biology" : "SUB-102",
               "geography" : "SUB-103",
               "economics" : "SUB-104",
               "literature" : "SUB-105",
               "costing" : "SUB-106",
               "accounting" : "SUB-107",
               "general science" : "SUB-108",
               "mathematics" : "SUB-109",
               "english" : "SUB-110",
               "social studies" : "SUB-111",
               "food and nutrition" : "SUB-112",
               "computing": "SUB-113", 
               "physical education": "SUB-114",
               "picture making": "SUB-115",
               "french":"SUB-116",
               "crs": "SUB-117"
          }

               sub_list: str = ['english','general science','mathematics','physics','chemistry','biology','geography','economics','literature', 'accounting','food and nutrition', 'french','crs','computing','physical education',]
               while True:
                    try:
                         get_student_subject: str = input(
                    "\nAdd Your Subject _ select from these subjects\n"  
                    "['physics','english','mathematics','general science','chemistry','biology','crs','geography','economics', 'french,'literature', 'picture making',' 'accounting','food and nutrition'] \n"
                        
               ).strip().lower()
                         if  get_student_subject  in sub_list:
                              print(f"{get_student_subject} entered  ")
                              get_student_subject
                              break
                    except (TypeError, UnboundLocalError, NameError):
                         print("Subject entered not found   ")
                         continue
          

          

               if get_student_subject in list(subject_to_id_match.keys()):
                Sub_ID = subject_to_id_match.get(get_student_subject)
               

               data_append = {
                         "subject name" :get_student_subject,
                         "subject id" : Sub_ID,
               
          } 

               subject_data.append(data_append)

               with open(file=subject_file, mode="w", encoding="utf-8") as file:
                         json.dump(subject_data, file, indent=4)
                         





          elif user_choice == "2":
               print("==== printing subject and its ID")
               for  element in subject_data:
                    
                    print(f"\nSubject name: {element["subject name"]}\n"
                          f"Subject ID: {element["subject id"]}")
               
               print()




          elif user_choice == "3":
 #delete Subject
 
               get_subject_to_delete = input("Enter Subject name: \n")
               for value in subject_data:
                    if get_subject_to_delete not in value["subject name"]:
                         print("Subject now found")
                         break
                    else:
                         confirm = input(f"do you want to delete {get_subject_to_delete}? ").lower().strip()
                         if confirm == "y" or confirm == "yes":
                              subject_data.remove(value)
                              with open(file=subject_file, mode="w", encoding="utf-8") as f:
                                   json.dump(subject_data, f, indent=4)
                                   
                
               
          elif user_choice == "4":
               return
          else:
               print("invalid user choice")








def data_entry():
     # enter results  
          
     try:
          ask_id = int(input("enter studen ID: \n"))
          ask_id
     except (TypeError, NameError, ValueError):
          print("invalid input")
     
     for elements in data:
          if ask_id == elements["student ID"]:
               print(f"ID matches {elements.get("first name")}")
               break
          
          
          
     
     
     ask_subject = input("enter subject name: \n")
     if ask_subject not in ['english','general science','mathematics','physics','chemistry','biology','geography','economics','literature', 'accounting','food and nutrition','computing','physical education','picture making','french','crs']:
          print("Subject not found\n")

     for element in subject_data:
          if ask_subject == element["subject name"]:
               print(element.get("subject name"))
               print(element.get("subject id"))
          
               
     
          
     
     while True: 
          try:
                ask_score = int(input("enter subject score"))
                if ask_score <= 100:
                     ask_score
                     break
          except (ValueError, TypeError, NameError, UnboundLocalError):
               print("score should be 0-100")
               continue
          
          
          
     if ask_score >= 80:
          score_result = "A1"
     elif ask_score >= 70:
          score_result = "B2"
     elif ask_score >= 65:
           score_result = "B3"
     elif ask_score >= 60:
          score_result = "C4"
     elif ask_score >=55:
           score_result = "C5"
     elif ask_score >=50:
          score_result = "C6"
     elif ask_score >= 45:
          score_data = "D7"
     elif ask_score >= 40:
          score_data = "E8"
     else:
          score_result = "F"
     
          
     score_data = {
          "Student id" : ask_id,
          "subject name" : ask_subject,
          "score" : ask_score,
          "Grade" : score_result
     }
     
     
     
     results_data.append(score_data)
     
     with open(file=results_file, mode="w", encoding="utf-8") as file:
          json.dump(results_data, file, indent=4)
          
     print("\nResults Saved Successfully\n")
     
     
     
     



def view_results():
     
     
     get_student_id = int(input("Enter ID Student: \n"))
     
     for i in data:
          if  get_student_id not in i.values():
               print("Student not found")
               
          else:
               for result in results_data:
                    if result.get("Student id") == get_student_id:
                         print(
                              f"Subject: {result.get("subject name")}\n"
                              f"Score: {result.get("score")}\n"
                              f"Grade: {result.get("Grade")}\n"
                         
                         )
               
          
               
               



def generate_results():
     
     get_student_id = int(input("enter student ID: "))
     
     
     
     for var in data:
          if get_student_id not in var.values():
               print("Student not found")
               return
          
          
          if get_student_id == var.get("student ID"):
               print(
                   f"Student: {var["first name"]} {var["last name"]}\n"
                   f"Student class: {var["form"]}"       
                   )
               
               total_score = 0
               count = 0
               for element in results_data:
                    if get_student_id == element.get("Student id"):
                         print(f"Subject: {element.get("subject name")} ")
                         print(f"Score: {element.get("score")}")
                         print(f"Grade: {element.get("Grade")}")
                         
                         total_score += element.get("score")
                         
                    count +=1
                    print(f"Student's Total Score: {total_score}")
                    print(f"Average: {total_score/count}")
                    break 
                         
                    
                         
                         
                         
     
     








if __name__ == "__main__":
    main()