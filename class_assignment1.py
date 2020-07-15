class time:
    def __init__(self,time1,time2):
        self.time1=time1
        self.time2=time2
        self.time_list1=list(self.time1.split(" "))
        self.time_list2=list(self.time2.split(" "))

    def add(self):
        tot_add=int(self.time_list1[0])*60+int(self.time_list1[3])+int(self.time_list2[0])*60+int(self.time_list2[3])
        tot_add_hour=tot_add/60
        tot_add_min=tot_add%60
        print(int(tot_add_hour),"hours",int(tot_add_min),"mins")
    def sub(self):
        if(int(self.time_list1[0])>=int(self.time_list2[0])):
            tot_sub=(int(self.time_list1[0])*60+int(self.time_list1[3]))-(int(self.time_list2[0])*60+int(self.time_list2[3]))
            tot_sub_hour=tot_sub/60
            tot_sub_min=tot_sub%60
            print(int(tot_sub_hour),"hours",int(tot_sub_min),"mins")
        else:
            tot_sub = (int(self.time_list2[0]) * 60 + int(self.time_list2[3])) - (
                        int(self.time_list1[0]) * 60 + int(self.time_list1[3]))
            tot_sub_hour = tot_sub / 60
            tot_sub_min = tot_sub % 60
            print(int(tot_sub_hour), "hours", int(tot_sub_min), "mins")
    def display_min(self):
        tot_min=int(self.time_list1[0])*60+int(self.time_list1[3])+int(self.time_list2[0])*60+int(self.time_list2[3])
        print(tot_min,"mins")
t1=time(input("enter time1 in the format (e.g 4 hours and 7 min)"),input("enter time2 in the format(e.g 4 hours and 7 min)"))
t1.add()
t1.sub()
t1.display_min()
