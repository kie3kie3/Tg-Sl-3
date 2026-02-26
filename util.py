import json
    

def writeData(obj, file_name, name=None):
    file = open(file_name, 'r', encoding='utf-8')
    data = json.load(file)
    print(type(data))
    if name:
        data[name] = obj.__dict__
    with open(file_name, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
    

def readData(file_name, name=None):
    with open(file_name, 'r', encoding='utf-8') as file:
        if name:
            return json.load(file[name])
        return json.load(file)

