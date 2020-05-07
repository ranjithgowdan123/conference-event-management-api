import json 



@app.route('/confDetails', methods=["GET"])
@cross_origin()
def conf():
    data =  flask.request.get_json() 
    result = []
    data['paid'].extend(data['free'])
    for myDict in data['paid']:
        #if myDict not in result:
        result.append(myDict)
    print (len(result))
    for c in result:
        print(c['confName'],c['confUrl'], c['confStartDate'], c['entryType'],c['venue'])
    
    
    #print exact duplicate
    
    seen = set()
    seen1= set()
    new_l = []
    for d in result:
        t = tuple(d.items())
        if t not in seen:
            seen.add(t)
            new_l.append(d)
        else:
            seen1.add(t)
    print(seen1)
    return "done", 200