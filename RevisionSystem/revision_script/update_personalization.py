from pathlib import Path
import json


BASE = Path(__file__).resolve().parent
personalization_file = BASE / "personalization.json"

class UpdatePersonalization:
    def __init__(self):
        try:
            with open(personalization_file, 'r') as file:
                self.personalization_file_data=json.load(file)
        
        except FileNotFoundError:
            print('File not found!')
        except Exception as e:
            print(e)

    def save(self):
        try:
        
            with open(personalization_file, "w") as file:
                json.dump(self.personalization_file_data, file, indent=4)
        
            return True
        except FileNotFoundError:
            print('File not found!')
        except Exception as e:
            print(e)

    def get_data_in_personalization(self):
        all_subjects={}
        for index, data in enumerate(self.personalization_file_data.keys()):
            all_subjects[index+1]=data

        return all_subjects

    def main(self, Lecture_log):
        self.lecture_log=Lecture_log
        all_data=self.get_data_in_personalization()
        print("You can update these things:\n")
        for i in all_data:
            print(f"{all_data[i]}: {i}")

        print("\nEnter the number!\n")
        user_input=int(input())
        self.update_data(user_input, all_data)

    def update_data(self, user_input, all_data):
        personalized_keys_value=self.personalization_file_data[all_data[user_input]]
        type_of_value=type(personalized_keys_value)
        if type_of_value is int:
            name_of_key=all_data[user_input]
            print(f"You are going to update '{name_of_key}'\n")
            num=int(input("Enter the number you want to set:\n"))
            self.personalization_file_data[name_of_key] = num

        elif type_of_value is list:
            # showing already added subject
            subject_in_planner=self.personalization_file_data.get("subject_in_planner")
            print("You have already these subjects in planner.")
            for index, subject in enumerate(subject_in_planner):
                print(f"{index+1}. {subject}")

            print("\nYour subjects that can be added......\n")
            all_subject=self.lecture_log.all_subject()
            for index, subject_key in enumerate(all_subject):
                print(f"{all_subject[subject_key]}: {index+1}")

            subject_num=int(input("\nEnter the number of that subject you want to add in personalization:\n"))
            subject_name=all_subject[subject_num]
            if subject_name not in subject_in_planner:
                subject_in_planner.append(subject_name)
                self.personalization_file_data["subject_in_planner"]= subject_in_planner

        self.save()
        print("Your changes have been updated.")


