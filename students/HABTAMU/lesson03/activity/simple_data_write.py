"""
write a csv file data is "anonymous" (no schema)
Creates a file that look like this:
John,502-77-3056,2/27/1985,117.45
"""

import csv

peopledata = ['John', '502-77-3056', '2/27/1985', 117.45]

with open('simple_data_write.csv', 'w') as people:
    peoplewriter = csv.writer(people)
    peoplewriter.writerow(peopledata)

"""
simple Schema file example:
'Person Name','SSN','BirthDate','Account Balance'
'John','502-77-3056','2/27/1985','117.45'

Field Name: 'Person Name', Type: String, Maximum Length: 30, Mandatory
Field Name: ... etc

"""   

