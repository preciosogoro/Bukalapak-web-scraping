import selenium
import json


template = '''
{
    "DATA" : [
        {
            "BOOK-ID" : "1",
            "BOOK-INFO" : [
            {
                "TITLE" : "MAATSCHAP FIRMA Dan PERSEKUTUAN KOMANDITER",
                "PRICE" : "Rp154.900",
                "STOCKS" : "",
                "CONDITION" : "BEKAS",
                "IMAGE" : ["", "", ""],
                "DESCRIPTION" : [""]
            }
        ]
        }
    ]
}

'''

data = json.loads(template)
for DATA in data["BOOK-INFO"]:
    print(DATA["TITLE"])