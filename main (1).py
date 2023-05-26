import pandas as pd

from tabulate import tabulate


def apen(li, b):
    lista = []
    if b < len(excel_data_df[c[0]].tolist()):
        mar = excel_data_df[c[0]].tolist()
        lista.append(mar[b])
        lista.append(mar[b][:len(mar[b]) - 1] + "st")
        man = excel_data_df[c[1]].tolist()
        lista.append(man[b])
        lista.append("VariantCoding_" + mar[b])
        curent = man[b].split("_")
        curent[1] = curent[1][0] + curent[1][4:]
        var = curent[0] + "_" + curent[1]
        curent2 = mar[b][:len(mar[b]) - 1].split("_")
        var2 = ""
        for n in curent2:
            var2 = var2 + n
        lista.append(var2 + "_st" + "." + var)
        if curent[1] == "u8":
            lista.append("ff")
        elif curent[1] == "u16":
            lista.append("ffff")
        elif curent[1] == "u32":
            lista.append("ffffffff")
        elif curent[1] == "s8":
            lista.append("f")
        elif curent[1] == "s16":
            lista.append("ff")
        elif curent[1] == "s32":
            lista.append("ffff")
        li.append(lista)
        apen(li, b+1)
    else:
        return


excel_data_df = pd.read_excel('Book1.xlsx', sheet_name='Sheet1')

c = excel_data_df.columns.ravel()

MyFile = open("write.txt", "w")
lis = [["NvBlockName", "ConstEnviBlockName", "AttributeFromNvBlockName", "VcBlockName", "AttributeFromVcBlockName",
       "Default"]]

j = 0
apen(lis, j)


MyFile.write(tabulate(lis, headers="firstrow"))
MyFile.close()

MyFile = open("write.txt", "r")
print(MyFile.read())
