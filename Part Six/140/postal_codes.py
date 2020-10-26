#Ex. 140 Postal Codes

postal_code_dict ={"Newfoundland":"A", "Nova Scotia":"B", "Prince Edward Island":"C", "New Brunswick":"D",\
    "Quebec":["G","H","J"], "Ontario":["K","L","M","N","P"], "Manitoba":"R", "Saskatchewan": "S",\
        "Alberta":"T", "British Columbia":"V", "Nunavut":"X", "Northwest Territories":"X", "Yukon":"Y"}

line = input("Inserisci codice postale:").upper()

if line[0] not in postal_code_dict.values() or line[1].isdigit()==False:
    print("Il codice postale inserito non è valido!")
else:
    province = ""

    for key, value in postal_code_dict.items():
        if line[0] in value:
            province = key

    if line[1] == 0:
        province += ". It's a rural address"
    else:
        province += ". It's a urban address"

    print(province)


