from datetime import datetime, date, timedelta
from pathlib import Path
import json
from RevisionSystem.revision_script.show_revision_subject import ShowRevisionChapters

BASE = Path(__file__).resolve().parent
personalization_file = BASE / "personalization.json"
revision_log_file = BASE / "revision_log.json"




class RevisionLogic:

    def __init__(self, log_file, all_completed_chapter, Lecture_log_cls):

        self.log_file = log_file
        self.all_completed_chapter = all_completed_chapter
        self.lecture_log_class = Lecture_log_cls
        self.today_date=date.today()

        self.personalization_data = self.load_personalization()

    def get_subject_to_be_revised(self):
        subject_to_be_filter_for_revision=[]
        subject_list_in_personalization=self.get_subject_in_planner_in_personalization()
        for each_chapter_data in self.all_completed_chapter:
            if each_chapter_data["subject_name"] in subject_list_in_personalization:
                subject_to_be_filter_for_revision.append(each_chapter_data)

        return subject_to_be_filter_for_revision

    def open_revision_log_file(self):
        try:
            with open(revision_log_file, 'r') as file:
                self.revision_log_file=json.load(file)

            return self.revision_log_file
        
        except FileNotFoundError:
            print('File not found!')
        except Exception as e:
            print(e)
        



    def load_personalization(self):

        with open(personalization_file, "r") as file:
            return json.load(file)

    def get_revision_interval(self):

        return self.personalization_data.get(
            "revision_interval_days",
            5
        )

    def get_subject_in_planner_in_personalization(self):
        return self.personalization_data.get("subject_in_planner", None)

    def get_each_subjects_chapter_per_day_limit(self):

        return self.personalization_data.get(
            "revision_chapter_per_day",
            1
        )

    def create_list_of_num_for_chapter_choice(self, subject_num_revised_per_day):
        # this method is used to create the list, which will have number for choose the subject to be revised.
        # opening the revision log file for getting the data.
        revision_log_file_data=self.open_revision_log_file()
        # checking that is revision data available?
        if not revision_log_file_data["dates"]:
            indexes_to_choose_sub=[]
            for i in range(subject_num_revised_per_day):
                indexes_to_choose_sub.append(i)
                return indexes_to_choose_sub

        else:
            all_date_list=revision_log_file_data["dates"]


    def subject_choice_page_for_revision(self, subject_in_personalization):
        # showing last two days schedule for easy selection.
        print("Your two days ago history of revision!")
        revision_log_file=self.open_revision_log_file()
        today_date=self.today_date
        for i in range(1, 3):
            date=today_date-timedelta(days=i)
            all_data=revision_log_file.get(f"{date}", None)
            if all_data:
                subject_name=all_data["data"][-1]["subject_name"]
                print(f"{i}. {subject_name} | {all_data["is_saved"]}")


        subject_list=[]
        print('\n\nPlease enter their respective number to choose, you can enter multiple number to select multiple subject.\n e.g-(1, 2)')
        for index, subject in enumerate(subject_in_personalization):
            print(f"{subject}: {index+1}")

        user_input=input("Enter the number:\n")
        user_input_list=user_input.split(',')
        for each_num in user_input_list:
            # checking that is the number is out of range?
            if int(each_num) <= len(subject_in_personalization):
                subject_list.append(subject_in_personalization[int(each_num)-1])
            
        if subject_list:
            # print(subject_list)
            return subject_list
        else:
            print('Please enter the number shown only!')
            return []



    def create_new_list_for_catogarized_subject_to_schedule(self, subject_in_personalization, subject_to_be_in_planner):
        # below var is storing the int that is how many chapters revised per day from the personalization.....
        subject_num_revised_per_day = self.get_each_subjects_chapter_per_day_limit()
        # and to get the subject there is method below will return list of indexes of the chapters.

        subject_list_to_choose_subject = self.subject_choice_page_for_revision(subject_in_personalization)

        planned_subject_chapters = [
            {f"{i}": []}
            for i in subject_list_to_choose_subject
        ]

        for each_subject_chapter in subject_to_be_in_planner:
            subject_name=each_subject_chapter["subject_name"]
            revision_history=each_subject_chapter["revision_history"]
            for subject_dict in planned_subject_chapters:
                for key in subject_dict.keys():
                    if key == subject_name:
                        chapters_to_be_planned_only_for_today=self.filter_out_chapters_not_to_be_revised_only_today(revision_history)
                        if chapters_to_be_planned_only_for_today is True:
                            subject_dict[key].append(each_subject_chapter)
        return planned_subject_chapters

    def filter_out_chapters_not_to_be_revised_only_today(self, revision_history):
        if not revision_history:
            return True

        else:
            # taking the last history as append will be last.
            last_history_data=revision_history[-1]
            # extracting the date after which it can be revised.
            # name it: date_after_it_can_revised as key
            date_after_it_can_be_revised=datetime.strptime(last_history_data["date_after_it_can_revised"], "%Y-%m-%d").date()
            # now checking that is date after revised and today subtraction is greater than date gap of each chapter set by user is.
            if self.today_date >= date_after_it_can_be_revised:
                return True
            else:
                return False




    def revision_logic(self, subject_to_be_in_planner):
        # It must contains that json data whome to be revised
            
            # planned_subject_chapters = self.calculate_revision(chapter, subject_to_be_in_planner)
        subject_in_personalization=self.get_subject_in_planner_in_personalization()
        # creating a varibale that will contain per subject chapter to be revised
        planned_subject_chapters= self.create_new_list_for_catogarized_subject_to_schedule(subject_in_personalization, subject_to_be_in_planner)

        self.revision_brain(planned_subject_chapters)
        
        # print(planned_subject_chapters)
        
        # return planned_subject_chapters




    def revision_brain(self, planned_subject_chapters):
        gap_days_by_user=self.get_revision_interval()
        # This method will be used to sort and give the planner data.
        per_subject_limit_chapter_in_planner=self.get_each_subjects_chapter_per_day_limit()
        for each_subject in planned_subject_chapters:
            for subject_name, list_of_chapter in each_subject.items():
                list_of_chapter.sort(key=lambda each_chapter: each_chapter["revision_count"])
                # Here sort method just iterate the list that is list_of_chapter(it is a list not iterated, because that for loop is iterating {'physics': [{'subject_name': 'physics', 'chapter_name': 'electric_current', 'completed_date': '2026-08-07', 'revision_count': 1, 'last_revision': '2026-08-14', 'strength_status': 'weak', 'revision_history': []}]} this into just key and value, and value that is list_of_chapter is already a list.)
        
        ShowRevisionChapters().main(planned_subject_chapters, per_subject_limit_chapter_in_planner, gap_days_by_user)


    def main(self):
        # asking for specific 
        subject_to_be_in_planner=self.get_subject_to_be_revised()
        self.revision_logic(subject_to_be_in_planner)
        # print(all_schedule)
"""
[{'physics': [{'subject_name': 'physics', 'chapter_name': 'electric_current', 'completed_date': '2026-08-07', 'revision_count': 1, 'last_revision': '2026-08-14', 'strength_status': 'weak', 'revision_history': []}, {'subject_name': 'physics', 'chapter_name': 'electric_charges_fields', 'completed_date': '2026-08-12', 'revision_count': 0, 'last_revision': '', 'strength_status': '', 'revision_history': []}]}, {'chemistry': [{'subject_name': 'chemistry', 'chapter_name': 'solutions', 'completed_date': '2026-08-08', 'revision_count': 0, 'last_revision': '', 'strength_status': '', 'revision_history': []}, {'subject_name': 'chemistry', 'chapter_name': 'chemical_kinetics', 'completed_date': '2026-08-12', 'revision_count': 0, 'last_revision': '', 'strength_status': '', 'revision_history': []}]}, {'mathematics': []}]


[{'physics': [{'subject_name': 'physics', 'chapter_name': 'electric_current', 'completed_date': '2026-08-07', 'revision_count': 1, 'last_revision': '2026-08-14', 'strength_status': 'weak', 'revision_history': []}]}, {'chemistry': []}, {'mathematics': []}]



"""