from RevisionSystem.lecture_operation import Lecture_log
from RevisionSystem.revision_script.revision_data_ext import revisionInstance
from RevisionSystem.revision_script.show_revision_subject import ShowRevisionChapters
from RevisionSystem.revision_script.update_personalization import UpdatePersonalization
from colorama import Fore, Style

class TerminalIO:
    def __init__(self):
        print("Hey Welcome to study log.\n\nWhat do you want to do?\nYou have options:\n\nNOTE:Type their respected number:\n")

        self.all_options={
            1:"Show all subjects",
            2:"Show all chapter per subjects",
            3:"Revision System",
            4:"Show today's schedule",
            5:"Mark schedule as completed",
            6:"update personalization",
            7:"Create new subject",
            8:"Create new chapter",
            9:"Update chapter data",
            10:"Self choice subject for revision",
            11:"Exit"
        }

    def user_selected_ops(self):
        while True:

            print('\n')
            
            print(Fore.RED +"============================ OPTIONS START ==============================="+Style.RESET_ALL)
            
            for i in self.all_options:
                print(f"{self.all_options[i]}: {i}")
            print(Fore.RED +"============================ OPTIONS END ================================="+Style.RESET_ALL)
            print('\n')
            try:
                user_ops_num=int(input("Enter the number here:\n"))
                if user_ops_num == 1:
                    print("You are at show all subject page:\n")
                    self.show_all_subjects()

                elif user_ops_num==2:
                    print("You are at show all chapters page:\n")
                    self.show_all_chapter_per_subjects()

                elif user_ops_num == 3:
                    revisionInstance.revision_system()

                elif user_ops_num == 4:
                    ShowRevisionChapters().show_schedule(True)

                elif user_ops_num == 5:
                    ShowRevisionChapters().mark_schedule_completed(Lecture_log)
                elif user_ops_num == 6:
                    UpdatePersonalization().main(Lecture_log)
                elif user_ops_num == 7:
                    print("You are at the create new subject page")
                    Lecture_log.create_new_subject()
                

                elif user_ops_num == 8:
                    print("You are at the create new chapter page")
                    Lecture_log.create_new_chapter()

                elif user_ops_num==9:
                    print("You are at the update chapter page")
                    Lecture_log.chapter_update()

                elif user_ops_num==10:
                    ShowRevisionChapters().self_choice_subject_for_revision(Lecture_log)

                elif user_ops_num==11:
                    break

                else:
                    print("Please enter the correct numberasdfafda.")

            except ValueError:
                print("Enter integer only.")

    def show_all_subjects(self):
        print(Fore.GREEN+'============================ ALL SUBJECTS ==============================='+Style.RESET_ALL)
        all_subject=Lecture_log.all_subject()
        for index, subject_key in enumerate(all_subject):
            print(f"{index+1}. {all_subject[subject_key]}")
        print(Fore.GREEN+"============================ END ========================================"+Style.RESET_ALL)

    def show_all_chapter_per_subjects(self):
        print("\n")
        try:
            all_subject=Lecture_log.all_subject()
            print("You have these existing chapters:\n")
            for i in all_subject:
                print(f"{all_subject[i]}: {i}")

            subject_number=int(input("Enter the number of that subject want see:\n"))
            subject_name=all_subject[subject_number]
            print(f"You have these exisiting chapter in {subject_name}:")
            all_chapter=Lecture_log.all_chapter_of_subject(subject_number, all_subject)
            for index, existing_chapter_num in enumerate(all_chapter):
                print(f"\n{index+1}. {all_chapter[existing_chapter_num]}")
                Lecture_log.show_chapter_details(subject_name, all_chapter[existing_chapter_num])


        except TypeError:
            print("Please enter the correct number.")

TerminalIO().user_selected_ops()