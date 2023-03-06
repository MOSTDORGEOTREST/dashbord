
from openpyxl import load_workbook

def get_staff(full=False):
    wb = load_workbook("/Users/mac1/Desktop/projects/dashboard/data/staff.xlsx")
    result = {}
    for i in range(2, 50):
        name = wb["Лист1"]['B' + str(i)].value
        if name is not None:
            if full:
                result[name.strip()] = int(wb["Лист1"]['A' + str(i)].value)
            else:
                name = name.strip().split(" ")
                result[f"{name[0]} {name[1][0]}.{name[2][0]}."] = int(wb["Лист1"]['A' + str(i)].value)
    return result


print(get_staff())