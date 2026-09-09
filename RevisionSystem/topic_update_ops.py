from datetime import date


class TopicUpdateOps:
    def __init__(self):
        self.log_file=None
        self.subject_name=""
        self.chapter_name=""
        self.save_log=None


    # def total_lecture(self, subject_name, chapter_name):
    #     lecture_dict=self.log_file[self.subject_name][self.chapter_name]["lectures"]
    #     for index, each_lec in enumerate(lecture_dict):
    #         print(f"{index}. {each_lec}:{lecture_dict[each_lec]}")

    def main(self, log_file, subject_name, chapter_name, save_log):
        self.log_file=log_file
        self.subject_name=subject_name
        self.chapter_name=chapter_name
        self.save_log=save_log


        print("What do you want to update?\n")
        self.all_options={
            1:"completed_date",
            2:"revision_count",
            3:"strength_status"
        }
        for i in self.all_options:
            print(f"{self.all_options[i]}: {i}")

        print('\n')
    
        while True:
            try:
    
                topic_to_edit_num=int(input("Enter the number which you want to edit:\n"))
                self.topic_mapper(topic_to_edit_num)
                # topic_update(all_options[topic_to_edit], log_file, subject_name, chapter_name)
    
                break
    
            except ValueError:
                print("Value error, please enter integer only!")

    def topic_mapper(self, topic_to_edit_num):
        if topic_to_edit_num == 1:
            print("You are at the complete chapter marking page:")
            self.completed_date_update()
        elif topic_to_edit_num == 2:
            print("You are at the revision count page:")
            self.revision_count_ctrl()
        elif topic_to_edit_num == 3:
            print("You are at strength status page:")
            self.strength_status()


    def strength_status(self):
        strength_options={
                    1:"weak",
                    2:"good",
                    3:"strong"
                }
        for i in strength_options:
            print(f"{strength_options[i]}: {i}")
        strenth_number=int(input("Enter the status of the chapter:"))
        
        strength_status=strength_options[strenth_number]
        self.log_file[self.subject_name][self.chapter_name][f"{self.all_options[4]}"]=strength_status
        if self.save_log():
            print(f"Your strength status has been saved as {strength_status}")

    def revision_count_ctrl(self):
        self.log_file[self.subject_name][self.chapter_name][f"{self.all_options[3]}"]+=1
        completion_date=input("Enter the date of chapter completion:\nIf date is today, just write today:\n")
        if completion_date.lower()=='today':
            self.log_file[self.subject_name][self.chapter_name]["last_revision"]=f"{date.today()}"
        else:
            self.log_file[self.subject_name][self.chapter_name]["last_revision"]=completion_date
        
        if self.save_log():
            print(f"Your revision count has been updated. You have revised your chapter {self.log_file[self.subject_name][self.chapter_name][f"{self.all_options[3]}"]} times of chapter {self.chapter_name}.")


    def completed_date_update(self):
        # print("You are at the complete marking page of the chapter:\n")

        print('NOTE: Date format is: yyyy-mm-dd')
        completion_date=input("\nEnter the date of chapter completion:\nIf date is today, just write today:\n\n")
        if completion_date.lower()=='today':
            self.log_file[self.subject_name][self.chapter_name]["completed_date"]=f"{date.today()}"
        else:
            self.log_file[self.subject_name][self.chapter_name]["completed_date"]=completion_date
        if self.save_log():
            print("Your chapter has been marked as completed.")

        
topic_update_ops=TopicUpdateOps()
