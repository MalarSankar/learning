class Time:
    def __init__(self,hours,mins):
        self.hours=hours
        self.mins=mins
    def display_total_min(self):
        print(self.hours*60+self.mins,"mins")

def add(t1,t2):
        tot_add=t1.hours*60+t1.mins+t2.hours*60+t2.mins
        tot_hour=int(tot_add/60)
        tot_min=tot_add%60
        print("the adition of times is",tot_hour,"hours and",tot_min,"mins")
def sub(t1,t2):
        tot_sub=abs((t1.hours*60+t1.mins)-(t2.hours*60+t2.mins))
        tot_hour = int(tot_sub / 60)
        tot_min = tot_sub % 60
        print("the subraction of times is", tot_hour, "hours and", tot_min, "mins")
t1=Time(5,7)
t2=Time(4,7)
t1.display_total_min()
add(t1,t2)



