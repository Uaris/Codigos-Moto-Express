import pandas as pd
import glob

mes = str(input("Digite o mês desejado: "))

path = r'C:\Users\Volke\OneDrive\Desktop\Projeto Moto'
filenames = glob.glob(path + "/*.xlsm")

all_data = pd.DataFrame()
for f in glob.glob(path + "/*.xlsm"):
    df = pd.read_excel(f, sheet_name="Acerto", usecols="E")
    all_data = all_data.append(df, ignore_index=True)
Lista = [all_data["TOTAL"][79], all_data["TOTAL"][159], all_data["TOTAL"][239], all_data["TOTAL"][319],
         all_data["TOTAL"][399], all_data["TOTAL"][479], all_data["TOTAL"][559], all_data["TOTAL"][479],
         all_data["TOTAL"][559], all_data["TOTAL"][639], all_data["TOTAL"][719], all_data["TOTAL"][799],
         all_data["TOTAL"][879], all_data["TOTAL"][959], all_data["TOTAL"][1039], all_data["TOTAL"][1119],
         all_data["TOTAL"][1199], all_data["TOTAL"][1279], all_data["TOTAL"][1359], all_data["TOTAL"][1439],
         all_data["TOTAL"][1519], all_data["TOTAL"][1599], all_data["TOTAL"][1679], all_data["TOTAL"][1759],
         all_data["TOTAL"][1839], all_data["TOTAL"][1919], all_data["TOTAL"][1999], all_data["TOTAL"][2079],
         all_data["TOTAL"][2159], all_data["TOTAL"][2239], all_data["TOTAL"][2319], all_data["TOTAL"][2399]]
soma = sum(Lista)
media = sum(Lista)/len(Lista)
print("Lucro do mês de {}: R${:.2f}".format(mes, soma))
print("Média diária de lucro no mês de {}: R${:.2f}".format(mes, media))
