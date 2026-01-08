student_id_counter =100000

first_name =input("Enter your first name: ")
last_name = input ("enter your last name: ")

age = int(input("enter age:"))
height = float(input("enter height in meters:"))

enroll_input = input("is student enrolled? (yes/no):")

is_enrolled = enroll_input.lower() == "yes"

subjects = ["MATH","CS","FINANCE"]

marks = { 
            "Math":85,
            "CS":100,
            "FINANCE":90,
                
        }
clubs ={"Robotics","Quant","Ethical Hacking"}

accepted_rules = frozenset({
    "no cheating",
    "Maintain attendance",
    "follow code at conduct"
})

student_record= {
    "student_id" :student_id_counter,
    "first_name" :first_name,
    "last_name" : last_name,
    "age" : age,
    "height": height,
    "enrolled": is_enrolled,
    "subjects": subjects,
    "marks":marks,
    "clubs":clubs,
    "accepted_rules": accepted_rules
}
