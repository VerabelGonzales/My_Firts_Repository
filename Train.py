# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 16:45:06 2021

@author: gonza
"""

import cv2 
import os
import numpy as np


DataPath = "D:\I_2022\Vision Artificial\Repositories\My_Firts_Repository\Dataset_Faces"
Dir_list = os.listdir(DataPath)
print("Lista archivos:",Dir_list)

Labels = []
FacesData = []
Label = 0

for Name_Dir in Dir_list:
    Dir_Path = DataPath + "/" + Name_Dir
    
    for Fine_Name in os.listdir(Dir_Path):
        Image_Path = Dir_Path + "/" + Fine_Name
        print(Image_Path)
        Image = cv2.imread(Image_Path,0)
        #cv2.imshow("Image",Image)
        #cv2.waitKey(10)
        
        FacesData.append(Image)
        Labels.append(Label)
    Label += 1
    
print("Etiqueta 0:", np.count_nonzero(np.array(Labels) == 0))
print("Etiqueta 1:", np.count_nonzero(np.array(Labels) == 1))
        
# LBPH FaceRecognizer
Face_Mask = cv2.face.LBPHFaceRecognizer_create()

#Entrenamiento 
print("Entrenamiento.....")
Face_Mask.train(FacesData, np.array(Labels))

#Almacenando Modelo
Face_Mask.write("Face_Mask_Model.xml")
print("Modelo Almacenado")
        