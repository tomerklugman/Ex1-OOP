import json
import csv
import sys


class Building:
    def __init__(self, filename):

        self.elevators = []

        try:
            with open(filename, "r") as jsonfile:

                buildingdict = json.load(jsonfile)
                elevatorlist = buildingdict["_elevators"]

                for f in elevatorlist:
                    elevator = Elevator(f["_id"], f["_speed"], f["_minFloor"], f["_maxFloor"], f["_closeTime"],
                                        f["_openTime"], f["_startTime"], f["_stopTime"])
                    self.elevators.append(elevator)

        except IOError as e:
            print(e)


class Elevator:
    def __init__(self, id, speed, minFloor, maxFloor, closeTime, openTime, startTime, stopTime):
        self.id = id
        self.speed = speed
        self.minFloor = minFloor
        self.maxFloor = maxFloor
        self.closeTime = closeTime
        self.openTime = openTime
        self.startTime = startTime
        self.stopTime = stopTime

        self.CallList = []


class CallForElevator:
    def __init__(self, row):
        self.name = row[0]
        self.time = float(row[1])
        self.src = int(row[2])
        self.dest = int(row[3])
        self.status = int(row[4])
        self.allocate = row[5]


def CallsCSV(filename):
    tempcalls = []
    try:
        with open(filename) as CallsCSV:
            getCalls = csv.reader(CallsCSV)
            for row in getCalls:
                c = CallForElevator(row)
                tempcalls.append(c)
    except IOError as e:
        print(e)

    return tempcalls


def algo(build, call, out):  # when elevator gets free go to next call
    ID = 0

    building = Building(build)
    calls = CallsCSV(call)

    for call in calls:

        for elvator in building.elevators:

            if elvator.CallList is None:  # elevator got no calls
                ID = building.elevators.index(elvator)

        building.elevators[ID].CallList.append(call)  # add call
        call.allocate = building.elevators[ID].id

    NewCallsCSV(calls, out)


def NewCallsCSV(calls, filename):
    try:
        callList = []
        for call in calls:
            # print(call.__dict__)
            callList.append(call.__dict__.values())
        with open(filename, "w", newline="") as f:
            out = csv.writer(f)
            out.writerows(callList)
    except IOError as e:
        print(e)


if __name__ == '__main__':
    algo(sys.argv[1], sys.argv[2], sys.argv[3])
