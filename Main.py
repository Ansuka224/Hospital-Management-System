# Imports
from Admin import Admin
from Doctor import Doctor
from Patient import Patient

def main():
    """
    the main function to be ran when the program runs
    """

    # Initialising the actors
    admin = Admin('admin','123','B1 1AB') # username is 'admin', password is '123'
    doctors = [Doctor('John','Smith','Internal Med.'), Doctor('Jone','Smith','Pediatrics'), Doctor('Jone','Carlos','Cardiology')]
    patients = [Patient('Sara','Smith', 20, '07012345678','B1 234'), Patient('Mike','Jones', 37,'07555551234','L2 2AB'), Patient('Daivd','Smith', 15, '07123456789','C1 ABC')]
    discharged_patients = []
    Patient.save_records(patients)

    # keep trying to login tell the login details are correct
    while True:
        if admin.login():
            running = True # allow the program to run
            break
        else:
            print('Incorrect username or password.')

    while running:
        # print the menu
        print('Choose the operation:')
        print(' 1- Register/view/update/delete doctor')
        print(' 2- Discharged patient')
        print(' 3- View patient')
        print(' 4-  View discharge patients')
        print(' 5- Assign doctor to a patient')
        print(' 6- Relocate Doctor to new patient')
        print(' 7- Print patient name of same Family')
        print(' 8 - Add a new patient ')
        print(' 9-  Book an appointment')
        print(' 10- Management Report')
        print(' 11-Update admin details  ')
        print(' 12- Quit')

        # get the option
        op = input('Option: ')

        if op == '1':
            # 1- Register/view/update/delete doctor
         #ToDo1
          admin.doctor_management(doctors)

        elif op == '2':
            # 2- discharge patients
            #ToDo2
            while True:
                op = input('Do you want to discharge a patient(Y/N):').lower()

                if op == 'yes' or op == 'y':
                    #ToDo3
                    admin.discharge(patients,discharged_patients)

                elif op == 'no' or op == 'n':
                    break

                # unexpected entry
                else:
                    print('Please answer by yes or no.')
        
        elif op == '3':
            # 3 - view patient
            #ToDo4
            admin.view_patient(patients)

        elif op == '4':
            # 4- View discharged patients
            admin.view_discharge(discharged_patients)

        elif op == '5':
            # 5- Assign Doctor to Patient
            admin.assign_doctor_to_patient(patients, doctors)

        elif op == '6':
            # 6 - Relocate Doctor to new Patient
            admin.doctor_relocate(patients, doctors)

        elif op == '7':
            #7 - print patient name of same family
            admin.print_patients_of_same_family(patients)

        elif op == '8' :
            #8 - Add a new patient to the file
            admin.add_new_patient(patients)

        elif op == '9':
            #9 - Book an appointment
            admin.book_appointment(doctors)

        elif op == '10':
            #10 - Management Report
            admin.get_management_report(doctors, patients)

        elif op == '11':
            #11 - update admin details
            admin.update_details()

        elif op == '12':
            #12 - Quit
            print('System is Terminated')
            quit()
            
        else:
            # the user did not enter an option that exists in the menu
            print('Invalid option. Try again')

if __name__ == '__main__':
    main()
