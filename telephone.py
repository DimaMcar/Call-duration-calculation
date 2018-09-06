from datetime import timedelta
from collections import defaultdict

class call(timedelta):
    """
    __slots__ = '_days', '_seconds', '_microseconds', '_hashcode', '_telephone'
    def __new__(cls, days=0, seconds=0, microseconds=0,
                milliseconds=0, minutes=0, hours=0, weeks=0, telephone=0):
        self = super().__new__(cls, days=0, seconds=0, microseconds=0,
                milliseconds=0, minutes=0, hours=0, weeks=0)
        self._telephone = telephone
        return self
        """
        
    def total_minutes(self):
        return self.total_seconds() // 60
    
    def real_minutes(self):
        return self.total_seconds() / 60
    
    
def data_to_dict(S):
    telephones = defaultdict(list)
    for line in S.splitlines():
        time, number = line.split(",")
        number = number.replace("-","")
        
        hours, minutes, seconds = time.split(":")
        time = call(hours = int(hours), minutes = int(minutes),
                    seconds = int(seconds))
        
        telephones[int(number)].append(time)
    return telephones

def count_total(telephones):
    duration = {}
    for number, calls in telephones.items():
        duration[number] = sum(calls, timedelta())
        duration[number] = duration[number].total_seconds()
    maximum = [number for m in [max(duration.values())] for number,val in duration.items() if val == m]  
    return min(maximum)
        
def count_paid(telephones):
    sum = 0
    for number in telephones.values():
        for i in number:
            if i.real_minutes() <= 5.0:
                print (i.real_minutes())
                sum+=3*i.total_seconds()
            else:
                sum+=(i.total_minutes()+1)*150
    return int(sum)
                

def solution(S):
    telephones = data_to_dict(S)
    free = count_total(telephones)
    del telephones[free]
    print (telephones)
    sum = count_paid(telephones)
    return sum            

telephones = ('00:01:07,400-234-090\n00:05:01,701-080-080\n00:05:00,400-234-090')

print (solution(telephones))
            