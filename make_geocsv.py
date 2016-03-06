"""scan all articles inside the 'content' folder recursivly (without images and pages folder)
   and write a csv file for use with google fusion chart. fields are seperated by an ; the geodata is comma seperated
   fields in csv file:
   example of .md file
   Title: Are IDNs (Internationalized Domain Names) the answer to a Multi-lingual Internet?
   Date: 2016-02-16 16:00
   Modfied: 2016-02-16 17:43
   Tags: multi-lingual, Africa
   Slug: 2016-02-16-multilingual
   ICBM: -6.162959, 35.751607
   GeoRegion: TZ-03
   GeoPlacename: Dodoma
   GeoPosition: -6.162959;35.751607
   Authors: WITABA Bonface
"""

import os 

exclude = ["images", "pages", "magazine"]

text = "'Title'; 'Date'; 'Location'; 'Author'; 'tags';'URL'\n"



data = {"Title:": None,
        "Date:": None,
        "Tags:": None,
        "ICBM:": None,
        "Authors:": None,
        "Slug:":None}


for root, dirs, files in os.walk(os.path.join(".","content")):
    print("processing:", root)
    skip = False
    for forbiddenfolder in exclude:
        if forbiddenfolder in root:
            skip = True
    if skip:
        print("skipping because i found forbidden folder:", root)
        continue
    for filename in files:
        if filename[-3:] == ".md":
            with open(os.path.join(root, filename)) as file:
                lines = file.readlines()
            for line in lines:
                for startword in data:
                    if line[:len(startword)] == startword:
                        data[startword] = line[len(startword):]
            print("file read complete. data is:", data)
            text += "{};{};{};{};{};{}\n".format(data["Title:"].strip(), 
                                               data["Date:"].strip(),
                                               data["ICBM:"].strip(),
                                               data["Authors:"].strip(),
                                               data["Tags:"].strip(),
                                               "http://internationalopenmagazine.org/"+data["Slug:"].strip())
# writing file
with open("geodata.csv", "w") as output:
    output.write(text)
print("geodata written")
print("-------------------")
print(text)
                    
                
    
