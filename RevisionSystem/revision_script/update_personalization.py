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

    def main(self):

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
            print("List update feature will be soon!")

        self.save()


