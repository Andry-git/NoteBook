import json
import TimeInterval as TI


def readJSON(FileName="data.json"):
    with open(FileName, "r", encoding='utf-8') as f:
        return json.load(f)


def writeJSON(data, FileName="data.json"):
    with open(FileName, "w", encoding='utf-8') as f:
        return json.dump(data, f)


def delTask(dict_data, key):
    del dict_data[key]
    writeJSON(data=dict_data)


def addTask(dict_data, key, start, end, name, text):
    task = {key: {
        "start": start,
        "end": end,
        "name": name,
        "text": text}}
    dict_data.update(task)
    writeJSON(data=dict_data)


def updateTask(dict_data, key, start, end, name, text):
    del dict_data[key]
    addTask(dict_data, key, start, end, name, text)
    writeJSON(data=dict_data)


def printTask(dict_data, key):
    d = dict_data[key]
    print(d["start"])
    print(d["end"])
    print(d["name"])
    print(d["text"])
    print()


def printTaskALL(dict_data):
    keys = dict_data.keys()
    # print(keys)
    skeys = TI.SortTime(keys)
    for key in skeys:
        printTask(dict_data, key)


# Если есть пересечение интервалов времени - True
# Если пересечение отсутствует - FALSE
def checkInterval(dict_data, TimeStartNew, TimeEndNew):
    keys = dict_data.keys()
    for key in keys:
        d = dict_data[key]
        if TI.TimeInterval(d["start"], d["end"], TimeStartNew, TimeEndNew):
            return True
    return False




def printTasksInInterval(dict_data, TimeStartNew, TimeEndNew):
    keys = dict_data.keys()
    neededKeys = []
    for key in keys:
        d = dict_data[key]
        if TI.TimeInterval(d["start"], d["end"], TimeStartNew, TimeEndNew):
            neededKeys.append(key)
    for key in neededKeys:
        printTask(dict_data, key)
    if len(neededKeys)==0:
        print("Нет задач")




if __name__ == '__main__':
    print()
