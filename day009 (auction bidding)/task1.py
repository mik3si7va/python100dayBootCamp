dictionary = {
    "key" : "value number 1",
    "another key" : "value number 2",
    "one more key" : "value number 3",
    "different key" : "value number 4",   
}

print (dictionary["key"])
print(dictionary["different key"])
print(dictionary)

dictionary["new kew"] = "yet another value"

print(dictionary["new kew"])
print(dictionary)

for key in dictionary:
    print(key)
    print(dictionary[key])
    
dictionary2 = {
    "list": ["item1", "item2", "item3"],
    "dictionary3": {
        "list2": ["item4", "item5", "item6"],
        "list3": ["item7", "item8", "item9"]
    }
}


print(f"item 9 = {dictionary2['dictionary3']['list3'][2]}")