# -*- coding: utf-8 -*-
import pandas as pd
from os import listdir
from os.path import isfile, join
from shutil import copyfile



def juntar():

    path_musicas = r'C:\Users\Red\Desktop\Investigacao2020\Utils\Corpus\771\lyrics'
    path_final = r'C:\Users\Red\Desktop\Investigacao2020\FeatureExtractionSystem\datasets\771 songs'
    path_ids = r'C:\Users\Red\Desktop\Investigacao2020\FeatureExtractionSystem\datasets\Quadrantes-771.csv'
    files = [f for f in listdir(path_musicas) if isfile(join(path_musicas, f))]

    dataset_id_quadrant = pd.read_csv(path_ids,sep=',', encoding='utf-8',header=None)
    data_id = dataset_id_quadrant.iloc[:, 0]
    data_quadrant = dataset_id_quadrant.iloc[:, 1]

    contador = 0


    for ficheiro in files:
        nome = ficheiro.split(".txt")[0]
        for elemento in data_id:
            if nome == elemento:
                contador+=1
                copyfile(path_musicas + "\\" + elemento + ".txt",path_final+ "\\" + elemento + ".txt")
                break
    
    print(contador)


    ''' quadrant=[]

    for element in dataset_total_mt:
        contador=0
        verificou=False
        for element1 in data_id:
            if element == element1:
                quadrant.append(data_quadrant[contador])
                verificou=True
                break
            contador+=1
        if(verificou==False):
            quadrant.append("Q0")

    print(quadrant)

    data_total['Quadrant']=quadrant

    for i in range(len(quadrant)):
        if(quadrant[i]=="Q0"):
            data_total.drop(index=[i], inplace=True)

    print(data_total)

    data_total.to_csv('D:/rpp_mer/semantics_with_quadrant.csv',index=False)'''

if __name__ == '__main__':
    juntar()