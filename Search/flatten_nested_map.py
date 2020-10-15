import collections
hashmap = {"a":"11",
            "b":"12",
            "c":{
                "ca": {"cca": {"ccca":"7"}},
                "cd": "24",
           }
   }

def flattenNestedMap(hashmap):
    resMap = {}
    for k, v in hashmap.items():
        flattenHelper(v, resMap, k)
    return resMap


def flattenHelper(item, resMap, parent_key):
    if not isinstance(item, collections.MutableMapping):
        resMap[parent_key] = item 
        return 

    for k, v in item.items():
        if not isinstance(v, collections.MutableMapping):
            resMap[parent_key+'.'+k] = v 
        else:
            flattenHelper(v, resMap, parent_key+'.'+k)
    
result = flattenNestedMap(hashmap)

