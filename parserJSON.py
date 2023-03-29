import json


def readJSON(FileName):
    with open(FileName, "r", encoding='utf-8') as f:
        return json.load(f) 


def writeJSON(data, FileName):
    with open(FileName, "w", encoding='utf-8') as f:
        return json.dump(data, f)      


def delTask(dict_data, key):
        del dict_data[key]


def addTask(dict_data, key, start,end,name,text):
        task = {key:{
                "start":start,
                "end":end,
                "name":name,
                "text":text}}
        dict_data.update(task)
        
        
def updateTask(dict_data, key, start,end,name,text):
        del dict_data[key]
        addTask(dict_data, key, start,end,name,text)
        

def printTask(dict_data, key):

        d = dict_data[key]
        print(d["start"],d["end"])
        print(d["name"])
        print(d["text"])
        print()

def printTaskALL(dict_data):
        keys = dict_data.keys()
        for key in keys:
            printTask(dict_data, key)
        



if __name__ == '__main__':

    fileName = "data.json"
    fileName2 = "data2.json"
    fileName3 = "data3.json"
    #data = json.loads(get_File_Data(fileName)) 
    
    data = readJSON(fileName3)
    print(data) 
    
    addTask(data, "2022", "2022","2023","task3","text3")
    
    print()
    printTask(data, key="2002") 
    delTask(data, key="2002")
    print()
    
    
    #print(get_File_Data("data.json"))   
    writeJSON(data, fileName3)
    print(type(data))
    print(data)
    printTaskALL(data)
    