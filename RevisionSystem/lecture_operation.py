from pathlib import Path
import json
from datetime import date
from RevisionSystem.topic_update_ops import topic_update_ops

BASE=Path(__file__).resolve().parent

lec_log_file_path=BASE/"lec_log.json"


class LectureOperation:
    def __init__(self):
        # opening the file and saving into the memroy.
        try:
            with open(lec_log_file_path, 'r') as file:
                self.log_file=json.load(file)
        
        except FileNotFoundError:
            print('File not found!')
        except Exception as e:
            print(e)


        self.date_today = date.today()
        self.day_today = self.date_today.strftime("%A")

    def all_subject(self):
        all_subjects={}
        for index, subject in enumerate(self.log_file.keys()):
            all_subjects[index+1]=subject

        return all_subjects

    def all_chapter_of_subject(self, subject_num:int, all_subject:dict):
        print("\n")
        all_chapter={}
        # print("Enter their respective number.\nYou have these chapters:\n")
        try:
            # all_subject=self.all_subject()
            # for i in all_subject:
            #     print(f"{all_subject[i]}: {i}")
            # print('\n')
            # # subject_num=int(input("Enter the number: "))
            # print('\n')

            selected_subject=all_subject[subject_num]

            for index, chapter in enumerate(self.log_file[selected_subject].keys()):
                all_chapter[index+1]=chapter

            return all_chapter


        except KeyError:
            print("Enter the correct number.")

        # except ValueError:
        #     print("Please enter integer only.")

        # except Exception as e:
        #     print(e)

    def save(self):
        try:
        
            with open(lec_log_file_path, "w") as file:
                json.dump(self.log_file, file, indent=4)
        
            return True
        except FileNotFoundError:
            print('File not found!')
        except Exception as e:
            print(e)


    def create_new_subject(self):
        existing_subject=self.all_subject()
        print("You have these existing subjects:\n")
        for index, subject_key in enumerate(existing_subject):
            print(f"{index+1}. {existing_subject[subject_key]}")

        print('\n')
        subject_name=input("Enter the name of the subject to create:\n")
        self.log_file[subject_name]={}
        if self.save():
            print(f"New subject {subject_name} has been created successfully.")
        

    def create_new_chapter(self):
        existing_subject=self.all_subject()
        print("You have these existing subjects:\n")
        for i in existing_subject:
            print(f"{existing_subject[i]}: {i}")
        
        subject_number=int(input("Enter the number of that subject want see:\n"))
        subject_name=existing_subject[subject_number]
        print(f"You have these exisiting chapter in {subject_name}:")
        all_chapter=Lecture_log.all_chapter_of_subject(subject_number, existing_subject)
        for index, existing_chapter_num in enumerate(all_chapter):
            print(f"{index+1}. {all_chapter[existing_chapter_num]}")

        print('\nNOTE:PLease do not type space, keep underscore instead of space. (eg: chemical_kinetics)\n')
        chapter_name=input("Enter the name of the chapter:\n")

        # This is the data must inside the chapter name
        chapter_data={
            "start_date": f"{self.date_today}",
            "start_day": f"{self.day_today}",
            "completed_date": "",
            "revision_count": 0,
            "last_revision": "",
            "strength_status": "",
            "revision_history":[]
        }

        # creating a new key inside the subject.
        subject_name=existing_subject[subject_number]

        self.log_file[subject_name][chapter_name]=chapter_data
        if self.save():

            print(f"\nNew chapter {chapter_name} of subject {subject_name} has been created successfully.\n")


    def chapter_update(self):
        all_subject=self.all_subject()
        print("You have these existing chapters:\n")
        for i in all_subject:
            print(f"{all_subject[i]}: {i}")
        subject_number=int(input("Enter the number of that subject want to update:\n"))
        subject_name=all_subject[subject_number]
        # print('\n')
        # showing the exisiting chapters.
        print(f"You have these exisiting chapter in {subject_name}:")
        all_chapter=self.all_chapter_of_subject(subject_number, all_subject)
        for index, existing_chapter_num in enumerate(all_chapter):
            print(f"{index+1}. {all_chapter[existing_chapter_num]}")
        print('\n')
        chapter_number=int(input("Enter the number of the chapter to update:\n"))
        chapter_name=all_chapter[chapter_number]

        # In this method I am passing the save method, and keep in mind that it will not execute here, if added paranthesis, then it will first execuse and then pass the return value.
        # dynamic_chapter_update(self.log_file, subject_name, chapter_name)
        topic_update_ops.main(self.log_file, subject_name, chapter_name, self.save)

    def show_chapter_details(self, subject_name, chapter_name):
        chapter_details=self.log_file[subject_name][chapter_name]
        print(f"\nDetails of the subject '{subject_name}' of chapter '{chapter_name}' is:\n")
        for index,(detail_name, detail) in enumerate(chapter_details.items()):
            print(f"{index+1}. {detail_name} | {detail}")




Lecture_log=LectureOperation()
# Lecture_log.all_chapter_of_subject()
# Lecture_log.all_subject()
# Lecture_log.create_new_chapter()
# Lecture_log.chapter_update()
# Lecture_log.create_new_subject()



