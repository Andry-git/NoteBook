from datetime import datetime, date, time

format = '%d/%m/%Y, %H:%M'

# Если есть пересечение интервалов времени - True
# Если пересечение отсутствует - FALSE
def TimeInterval(TI1start, TI1end, TI2start, TI2end):

    # format = '%Y'
    TI1start = datetime.strptime(TI1start, format)
    TI1end = datetime.strptime(TI1end, format)
    TI2start = datetime.strptime(TI2start, format)
    TI2end = datetime.strptime(TI2end, format)

    latest_start = max(TI1start, TI2start)
    earliest_end = min(TI1end, TI2end)
    return latest_start <= earliest_end


# Если начало интервала меньше конца интервала - True
# Если конец интервала меньше начала интервала - FALSE
def ProverkaInterval(TIstart, TIend):
    return TIstart <= TIend


# def SortTime(timeList):
#     print(timeList)
#     newlist=[]
#     for i in timeList:
#         format = '%d/%m/%Y, %H:%M'
#         newlist.append(datetime.strptime(i, format))
#     newlist.sort()
#     return newlist


def SortTime(timeList):
    # print(timeList)
    newlist = sorted(timeList, key=lambda x: datetime.strptime(x, format))
    return newlist


def Today(timeList):
    today = datetime.today().date()
    print()
    newlist = []
    for i in timeList:
        if datetime.strptime(i, format).date()==today:
            newlist.append(i)
    return newlist

def TaskInInterval(timeList,starInter, endInter):
    newlist = []

if __name__ == '__main__':
    # datetime.datetime(year, month, day, hour=0, minute=0, second=0, microsecond=0, tzinfo=None)

    ddd = datetime(year=2001, month=2, day=1, hour=0, minute=0)
    ddd2 = datetime(year=2003, month=3, day=1, hour=0, minute=0)

    strd = "23/01/2001, 00:01"
    strd2 = "26/12/2003, 00:02"

    ddd3 = datetime(year=2002, month=2, day=1, hour=0, minute=0)
    ddd4 = datetime(year=2004, month=3, day=1, hour=0, minute=0)
    print(ddd)
    print(ddd < ddd2)

    sortedlist=SortTime([strd,strd2,strd])
    print(sortedlist)
    print(sortedlist[0])

    w = ddd3.year
    print(type(w))
    print(ddd3.year == ddd4.year-2)
    print(ddd3.year == ddd4.year)
    print(ddd3.strftime('%w'))

    print(datetime.today().date())
    print(type(datetime.today().date()))


    # print(TimeInterval(strd, strd, ddd3, ddd4))
    # print(TimeInterval(strd, strd, ddd, ddd2))
    #
    # print(TimeInterval(strd, strd, ddd, ddd3))
    # print(TimeInterval(strd, strd, ddd, ddd2))
    #
    # print(TimeInterval(strd, strd, ddd, ddd3))
    # print(TimeInterval(strd, strd, ddd2, ddd4))

    # current date and time


    now = datetime.now()
    #
    # t = now.strftime("%H:%M:%S")
    # print("Time:", t)
    #
    # s1 = now.strftime("%m/%d/%y, %H:%M:%S")
    # # mm/dd/YY H:M:S format
    # print("s1:", s1)
    #
    s2 = now.strftime("%d/%m/%Y, %H:%M:%S")
    # dd/mm/YY H:M:S format
    print("s2:", s2)
    datetime_str = '09/19/22 13:55:26'
    #
    # datetime_object = datetime.strptime(datetime_str, '%m/%d/%y %H:%M:%S')
    #
    # print(type(datetime_object))
    # print(ddd > datetime_object)
    # print(datetime_object)
    #
    # listTime = [ddd2, ddd4, ddd, ddd3]
    # print(listTime)
    # listTime.sort()
    # print(listTime)
    #
    # ssss = '2033'
    #
    # sss = datetime.strptime(ssss, '%Y')
    # print(sss)
    # print(sss > ddd3)
    # print(sss < ddd3)
