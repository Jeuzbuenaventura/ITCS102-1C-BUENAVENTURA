
import os
import json

os.system('cls')
print("DLL STUDENT INFORMATION SYSTEM")
print("=======================================")

stud_record = {}

while True:

    print("SELECT FROM THE FOLLOWING OPTIONS")
    print("A - Adding Student Record")
    print('B - Print All Record')
    print('C - Search Student')
    print('D - Deleted Student Record')
    print('E - Edit Student Record')
    print('F - Export Data')
    print('G - Exit System')

    choice = input("Input your choice --- > ").lower().strip()

    if choice == 'a':
        os.system('cls')
        print("ADD STUDENT RECORD")
        
        student_id = input("Input Student ID number")

        first_name = input("Input Student First Name --> ").upper()
        last_name = input("Input Student Last Name --> ").upper()
        course = input("Input Student Course --> ").upper()
        section = input("Input Student Section --> ").upper()
        email = input("Input student Email --> ")

        stud_record[student_id] = [first_name, last_name, course, section, email]
        print("DATA SAVED SUCCESSFULLY")

        continue
    elif choice == 'b':
        os.system('cls')

        print("PRINTING STUDENT RECORD")
        print("=======================================")

        for id,info in stud_record.items():
            print(f"STUDENT ID {id} - RECORD - {info}")

        continue
    elif choice == 'c':
        os.system('cls')
        print("SEARCH STUDENT RECORD")

        search_id = input('INPUT STUDENT ID ---- >   ').lower()

        for each_student in stud_record.keys():
            if search_id in stud_record.keys():
                print(f"\n\nRECORD FOUND for {search_id}")
                print("=======================================")
                for id in stud-record[search_id]:
                    print(f" --{id} ")

                print("=======================================")
            else:
                print("NO RECORD FOUND")
            break
        continue
    elif choice == 'd':
        os.system('cls')
        print("DELETE STUDENT RECORD")

        search_id = input('INPUT STUDENT ID ---- >   ').lower()

        for each_student in stud_record.keys():
            if search_id in stud_record.keys():
                print(f"\n\nRECORD FOUND for {search_id}")
                print("=======================================")
                for id in stud-record[search_id]:
                    print(f" --{id} ")

                print("=======================================")

                stud_record.pop(search_id)
                print("RECORD DELETED")
            else:
                print("NO RECORD FOUND")
            break
        continue
    elif choice == 'e':
        os.system('cls')
        print("EDIT / MODIFY STUDENT RECORD")

        for each_student in stud_record.keys():
            if search_id in stud_record.keys():
                print(f"\n\nRECORD FOUND for {search_id}")
                print("=======================================")
                for id in stud-record[search_id]:
                    print(f" --{id} ")

                print("=======================================")

                first_name = input("Input Student First Name --> ").upper()
                last_name = input("Input Student Last Name --> ").upper()
                course = input("Input Student Course --> ").upper()
                section = input("Input Student Section --> ").upper()
                email = input("Input student Email --> ")

                stud_record[search_id][0] = first_name
                stud_record[search_id][1] = last_name
                stud_record[search_id][2] = course
                stud_record[search_id][3] = section
                stud_record[search_id][4] = email
                print("DATA UPDATED SUCCESSFULLY")

            else:
                print("NO RECORD FOUND")
            break
        continue
    elif choice == 'f':
        print("EXPORT DATA")

        with open('student_record.json','w') as new_file:
            json.dump(stud_record, new_file, indet=4)

        print("DATA EXPORTED SUCCESSFULLY")
        continue
    elif choice == 'g':
        print("IMPORT DATA")

        with open('student_record.json','r') as new_file:
            imported_student = json.load(new_file)

        stud_record = imported_student
        print("DATA SAVED SUCCESSFULLY")
        continue
    elif choice == 'x':
        print("System Exit")
        break
    else:
        print("Invalid Choice, Re-enter code")
        continue