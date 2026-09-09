from pathlib import Path
import json
from datetime import date
from RevisionSystem.lecture_operation import Lecture_log
from RevisionSystem.revision_script.revision_logic import RevisionLogic
from RevisionSystem.revision_script.show_revision_subject import ShowRevisionChapters

BASE=Path(__file__).resolve().parent.parent
# print(BASE)
lec_log_file_path=BASE/"lec_log.json"

class RevisionDataExt:
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

    def get_all_completed_chapter(self):
        all_completed_chapter_list=[]
        all_subjects=Lecture_log.all_subject()
        for each_subject_num in all_subjects:
            # taking out all the chapter of the subjects.
            subject_name=all_subjects[each_subject_num]
            all_chapter_per_subject=Lecture_log.all_chapter_of_subject(each_subject_num, all_subjects)

            for each_chapter in all_chapter_per_subject:
                chapter_name=all_chapter_per_subject[each_chapter]
                # checking that is the chapter is completed or not?
                is_completed=self.log_file[subject_name][chapter_name]["completed_date"]
                revision_count=self.log_file[subject_name][chapter_name]["revision_count"]
                last_revision=self.log_file[subject_name][chapter_name]["last_revision"]
                strength_status=self.log_file[subject_name][chapter_name]["strength_status"]
                revision_history=self.log_file[subject_name][chapter_name]["revision_history"]
                if not is_completed == "":
                    # print(is_completed)
                    all_completed_chapter={
                        "subject_name":subject_name,
                        "chapter_name":chapter_name,
                        "completed_date":is_completed,
                        "revision_count":revision_count,
                        "last_revision":last_revision,
                        "strength_status":strength_status,
                        "revision_history":revision_history
                    }
                    all_completed_chapter_list.append(all_completed_chapter)

        # print(all_completed_chapter_list)
        RevisionLogic(self.log_file, all_completed_chapter_list, Lecture_log).main()

    def revision_system(self):
        if not ShowRevisionChapters().show_schedule(False):
            self.get_all_completed_chapter()

        else:
            print("You schedule is already created!")

revisionInstance=RevisionDataExt()