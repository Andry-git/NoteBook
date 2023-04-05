import json
import TimeInterval as TI
from datetime import datetime


def readJSON(FileName="data.json"):
    try:
        with open(FileName, "r", encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError as e:
        print("error", e)
        writeJSON(data={})
        return {}


def writeJSON(data, FileName="data.json"):
    with open(FileName, "w", encoding='utf-8') as f:
        return json.dump(data, f)


def delTask(dict_data, key):
    try:
        del dict_data[key]
        writeJSON(data=dict_data)
    except Exception as e:
        print("error")

def addTask(dict_data, key, start, end, name, text, priority):
    try:
        task = {key: {
            "start": start,
            "end": end,
            "name": name,
            "text": text,
            "priority": priority}}
        dict_data.update(task)
        writeJSON(data=dict_data)
    except Exception as e:
        print("error")

def updateTask(dict_data, key, start, end, name, text, priority):
    del dict_data[key]
    addTask(dict_data, key, start, end, name, text, priority)
    writeJSON(data=dict_data)


def printTask(dict_data, key):
    d = dict_data[key]
    print(d["start"])
    print(d["end"])
    print(d["name"])
    print(d["text"])
    print(d["priority"])
    print()


def printTaskALL(dict_data):
    keys = dict_data.keys()
    # print(keys)
    skeys = TI.SortTime(keys)
    for key in skeys:
        printTask(dict_data, key)
    if len(keys) == 0:
        print("Нет задач")

# Если есть пересечение интервалов времени - True
# Если пересечение отсутствует - FALSE
def checkInterval(dict_data, TimeStartNew, TimeEndNew):
    try:
        keys = dict_data.keys()
        for key in keys:
            d = dict_data[key]
            if TI.TimeInterval(d["start"], d["end"], TimeStartNew, TimeEndNew):
                return True
        return False
    except Exception as e:
        print("error")
        return True

def checkIntervalUpdate(dict_data, TimeStartNew, TimeEndNew, oldKey):
    try:
        keys = dict_data.keys()
        for key in keys:
            if key != oldKey:
                d = dict_data[key]
                if TI.TimeInterval(d["start"], d["end"], TimeStartNew, TimeEndNew):
                    return True
        return False
    except Exception as e:
        print("error")
        return True


# вывод задач за выбранный период
def printTasksInInterval(dict_data, TimeStartNew, TimeEndNew):
    try:
        keys = dict_data.keys()
        neededKeys = []
        for key in keys:
            d = dict_data[key]
            if TI.TimeInterval(d["start"], d["end"], TimeStartNew, TimeEndNew):
                neededKeys.append(key)
        for key in neededKeys:
            printTask(dict_data, key)
        if len(neededKeys) == 0:
            print("Нет задач")
    except Exception as e:
        print("error")



def printTodayTasks(dict_data):
    now = datetime.today().date()
    format = "%d/%m/%Y"
    TimeStartNew = now.strftime(format) + ", 00:01"
    TimeEndNew = now.strftime(format) + ", 23:59"
    printTasksInInterval(dict_data, TimeStartNew, TimeEndNew)


if __name__ == '__main__':
    print()
