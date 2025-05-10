d1 = {
    "नाम" : "name",
    "उम्र" : "age",
    "किताब" : "book",
    "भोजन" : "food",
    "शहर" : "city"
}


a = (input("Enter word in \'Hindi\' to identify corresponding \'English\' word : "))
print(d1.get(a))