listed=['Anuj', None, {'Name':'Anuj','Course':None,'Year':{'1st':12098,'2nd':2345,'3rd':None}}]

def recursion_data(data):
    print "starting recusion"
    print type(data)
    if isinstance(data, dict):
        for k, v in data.items():
            if v and isinstance(v, (dict, list, tuple)):
                recursion_data(v)
            elif not v:
                del data[k]
    elif isinstance(data, list):
        for item in data:
            print item
            if item==None:
                print("Found")
                seq = data.index(item)
                data.remove(item)
                item = data[seq]
            else:
                print("Not Found")
           # print index, item
        print item
        recursion_data(item)
    else:
        if not data:
            del data
            return
    return data

b=recursion_data(listed)
print("\nAfter execution")
print(b)
