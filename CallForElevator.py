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
            time=c[1]
            src=c[2]
            dest=c[3]
            type=c[4]
            allocatedTo=c[5]
            Calls_list.append(CallForElevator(time,src,dest,type,allocatedTo))


    def __str__(self) -> str:
        return super().__str__()

    def __repr__(self) -> str:
        return super().__repr__()