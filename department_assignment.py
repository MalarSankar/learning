class Department:
    def __init__(self,dept_name,dept_std_details,dept_sub):
        self.dept_name=dept_name.lower()
        self.dept_std_details=dept_std_details
        self.dept_sub=dept_sub
    def print_and_display_student_details(self):
        print("Student Details in",self.dept_name,"department:")
        for student in range(len(self.dept_std_details)):
            print(self.dept_std_details[student])
    def print_and_display_dept_sub(self):
        print("The subjects offered by",self.dept_name,"departmnt:")
        for subject in range(len(self.dept_sub)):
            print("      " ,self.dept_sub[subject])
    def print_and_display_std_names(self):
        print("Student names of",self.dept_name,"department:")
        for name in self.dept_std_details:
            print(name[1])

def overlap_subjects(civil,cse,eee):
    print("The overlapping subjects are",set(cse.dept_sub).intersection(set(civil.dept_sub),set(eee.dept_sub)))

def morthan3_subjects(dep_ob):
    print("Departments take morethan 3 subjects:")
    for deb in dep_ob:
        for sub in deb.dept_std_details:
            if(len(sub[2])>3):
                print(deb.dept_name)

cse=Department("cse",[[1,"malar",["m1","pe","mca"]],[2,"shiva",["m1","km","mca","physics"]],[3,"abi",["c","physics","mca"]]],["m1","pe","mca","km","physics","c"])
civil=Department("civil",[[1,"madhan",["physics","solid mechanic","m1"]],[2,"ajith",["chemistry","kmm","dynamics"]],[3,"lakshmi",["m1","solid mechanic","chemisty","physics"]]],["physics","solid mechanic","m1","chemistry","kmm","dynamics"])
eee=Department("EEE",[[1,"arthi",["electric","power","analytics"]],[2,"mohana",["physics","m1","power"]],[3,"karthi",["analytics","chemistry","power"]]],["electric","power","analytics","physics","m1","chemistry"])

overlap_subjects(cse,civil,eee)
dep_ob=[cse,civil,eee]
morthan3_subjects(dep_ob)
cse.print_and_display_std_names()
