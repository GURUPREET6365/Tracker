from colorama import Fore, Style
from pathlib import Path
import json
from datetime import date, timedelta

BASE = Path(__file__).resolve().parent
revision_log_file = BASE / "revision_log.json"

class ShowRevisionChapters:
    def __init__(self):
        try:
            with open(revision_log_file, 'r') as file:
                self.revision_log_file=json.load(file)
        
        except FileNotFoundError:
            print('File not found!')
        except Exception as e:
            print(e)

        self.date_today = date.today()

    def show_schedule(self, print_or_not:bool):
        data=self.revision_log_file.get(f"{self.date_today}", None)
        if print_or_not:
            if data is None:
                print("You have not created your schedule yet!")
            else:
                new_data=data['data']
                print(Fore.RED + "Your schedule is:")
                for each_dict in new_data:
                    subject_name=each_dict['subject_name']
                    chapter_name=each_dict['chapter_name']
                    print(Fore.CYAN + f"{subject_name} | {chapter_name}")
                print(Style.RESET_ALL)
                
        else:
            if data is None:
                return False
            else:
                return True


    def show_in_terminal(self, data_of_planner, per_subject_limit_chapter_in_planner, gap_days_by_user):
        revision_log=[]
        n=0
        print(Fore.RED + "Your today's schedule is:\n")
        for each_subject in data_of_planner:
            for subject_name, list_of_subject in each_subject.items():
                for index in range(min(per_subject_limit_chapter_in_planner, len(list_of_subject))):
                    chapter_dict=list_of_subject[index]
                    # creating new dict data to save in the revision log list and then to revision log json file.
                    # date_of_revision is the date when this schedule is created and on that it must be revised.
                    chapter_name = chapter_dict["chapter_name"]

                    custom_data = {
                        "subject_name":subject_name,
                        "chapter_name":chapter_name,
                        "date_of_revision":f"{self.date_today}",
                        "date_after_it_can_revised":f"{self.date_today+timedelta(days=gap_days_by_user)}"
                    }

                    
                    revision_log.append(custom_data)
                    print(Fore.CYAN + f"{n+1}. {subject_name} | {chapter_name}")
                    n+=1
        print(Style.RESET_ALL)
        # saving the revision log to revision log file.
        if revision_log:
            self.save_log_in_file(revision_log)

        else:
            print("Today you have no schedule.")

    def mark_schedule_completed(self, Lecture_log):
        print("You want to mark for today or specific date?")
        print("Type:\n1:today's target\n2:specific date target")
        user_input=int(input())
        if user_input == 1:
            data=self.revision_log_file.get(f"{self.date_today}", None)
            new_data=data['data']
            is_saved=data["is_saved"]
            if not is_saved:
                log_file_data=Lecture_log.log_file
                for each_dict in new_data:
                    subject_name=each_dict['subject_name']
                    chapter_name=each_dict['chapter_name']
                    date_after_it_can_revised=each_dict["date_after_it_can_revised"]
                    date_of_revision=each_dict["date_of_revision"]

                    data_to_add_in_revision_history={
                        "date_of_revision":date_of_revision,
                        "date_after_it_can_revised":date_after_it_can_revised
                    }

                    # Taking revision history from log file
                    log_file_data[subject_name][chapter_name]["revision_history"].append(data_to_add_in_revision_history)
                    log_file_data[subject_name][chapter_name]["last_revision"]=f"{self.date_today}"
                    log_file_data[subject_name][chapter_name]["revision_count"]+=1

                Lecture_log.save()
                
                self.revision_log_file[f"{self.date_today}"]["is_saved"]=True
                self.revision_log_file[f"{self.date_today}"]["is_completed"]=True
                self.save()
                print("Your today's schedule has been marked as completed.")

            else:
                print("Your today's schedule is already marked.")

        elif user_input==2:
            print("Enter date(format: YYYY-MM-DD)")
            date_input= input()
            data=self.revision_log_file.get(f"{date_input}", None)
            if data is None:
                print("No log exists for that date!")

            else:
                new_data=data['data']
                is_saved=data["is_saved"]
                if not is_saved:
                    log_file_data=Lecture_log.log_file
                    for each_dict in new_data:
                        subject_name=each_dict['subject_name']
                        chapter_name=each_dict['chapter_name']
                        date_after_it_can_revised=each_dict["date_after_it_can_revised"]
                        date_of_revision=each_dict["date_of_revision"]
                
                        data_to_add_in_revision_history={
                            "date_of_revision":date_of_revision,
                            "date_after_it_can_revised":date_after_it_can_revised
                        }
                
                        # Taking revision history from log file
                        log_file_data[subject_name][chapter_name]["revision_history"].append(data_to_add_in_revision_history)
                        log_file_data[subject_name][chapter_name]["last_revision"]=f"{self.date_today}"
                        log_file_data[subject_name][chapter_name]["revision_count"]+=1
                
                    Lecture_log.save()
                
                    self.revision_log_file[f"{self.date_today}"]["is_saved"]=True
                    self.revision_log_file[f"{self.date_today}"]["is_completed"]=True
                    self.save()
                    print("Your today's schedule has been marked as completed.")
                else:
                    print("Your schedule is already marked as completed.")

    
    def save_log_in_file(self, revision_log_data):
        self.revision_log_file[f"{self.date_today}"]={}
        self.revision_log_file[f"{self.date_today}"]['data']=revision_log_data
        self.revision_log_file[f"{self.date_today}"]["is_saved"]=False
        self.revision_log_file[f"{self.date_today}"]["is_completed"]=False
        self.save()
    
    def save(self):
        try:
        
            with open(revision_log_file, "w") as file:
                json.dump(self.revision_log_file, file, indent=4)
        
            return True
        except FileNotFoundError:
            print('File not found!')
        except Exception as e:
            print(e)

    def main(self, data_of_planner, per_subject_limit_chapter_in_planner, gap_days_by_user):
        self.show_in_terminal(data_of_planner, per_subject_limit_chapter_in_planner, gap_days_by_user)
        # self.show_schedule()




