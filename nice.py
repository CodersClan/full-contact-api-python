import csv
#----------------------------------------------------------------------
def csv_dict_writer(path, fieldnames, data):
    """
    Writes a CSV file using DictWriter
    """
    with open(path, "wb") as out_file:
        writer = csv.DictWriter(out_file, delimiter=',', fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow(row)
#----------------------------------------------------------------------
if __name__ == "__main__":
    data = ["first_name,last_name,city".split(","),
            "Tyrese,Hirthe,Strackeport".split(","),
            "Jules,Dicki,Lake Nickolasville".split(","),
            "Dedric,Medhurst,Stiedemannberg".split(",")
            ]
    my_list = []
    fieldnames = data[0]
    print fieldnames
    for values in data[1:]:
        inner_dict = dict(zip(fieldnames, values))
        print inner_dict
        my_list.append(inner_dict)
        print my_list
    path = "dict_output.csv"
    csv_dict_writer(path, fieldnames, my_list)