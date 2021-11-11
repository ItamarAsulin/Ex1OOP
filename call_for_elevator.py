from csv import reader
class CallForElevator:
    def __init__(self,time,src,dest,type,allocatedTo) :
        self.time=time
        self.src=src
        self.dest=dest
        self.type=type
        self.allocatedTo=allocatedTo

    def fromCsv(self,fileOfCalls):
        open_file = open(fileOfCalls)
        read_file = reader(open_file)
        Calls_data = list(read_file)
        Calls_list=[]
        for c in Calls_data:
            time=float(c[1])
            src=int(c[2])
            dest=int(c[3])
            type=c[4]
            allocatedTo=int(c[5])
            Calls_list.append(CallForElevator(time,src,dest,type,allocatedTo))


    def __str__(self) -> str:
        return f"time:{self.time} ,src:{self.src} ,dest:{self.dest}, type:{self.type}, allocatedTo:{self.allocatedTo} \n"

    def __repr__(self) -> str:
        return self.__str__()