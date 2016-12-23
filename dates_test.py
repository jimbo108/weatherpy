import time
string_date = '01/01/1997'
formatted_date_obj = time.strptime(string_date, "%d/%m/%Y")
print("formatted_date_obj is " + str(formatted_date_obj))
