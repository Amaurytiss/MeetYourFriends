# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 18:07:20 2020

@author: Utilisateur
"""
""" Algorithme permettant de calculer le barycentre de n villes  -- Made by Amaury"""
#%%

from selenium import webdriver
from time import sleep


def decortique(coord):
    res=""
    for i in range (len(coord)):
        if not(coord[i]=="°" or coord[i]=="′" or coord[i]=="," or coord[i]=='″'):
            res+=coord[i]
    
    (lad,lam,las,lap,lod,lom,los,lop) = [t(s) for t,s in zip((int,int,int,str,int,int,int,str),res.split())]
    return [lad,lam,las,lap,lod,lom,los,lop]

def transforme_coord_angles(coord):
    L=decortique(coord)
    l1=L[:4]
    l2=L[4:]
    lat_deg=l1[0]*3600+l1[1]*60+l1[2]
    if l1[3]=="sud":
        lat_deg*=-1
    long_deg=l2[0]*3600+l2[1]*60+l2[2]
    if l2[3]=="ouest":
        long_deg*=-1
    return [lat_deg,long_deg]

def barycentre(L):
    s1=0
    s2=0
    n=len(L)
    for i in range (len(L)):
        s1+=transforme_coord_angles(L[i])[0]
        s2+=transforme_coord_angles(L[i])[1]
    return [int(s1/n),int(s2/n)]

def angles_to_coord(L):
    lat_deg=L[0]
    long_deg=L[1]
    res=[0,0,0,0,0,0,0,0]
    if lat_deg>=0:
        res[3]="nord"
    else:
        res[3]="sud"
    if long_deg>=0:
        res[7]="est"
    else:
        res[7]="ouest"
    
    res[0]=lat_deg//3600
    res[1]=(lat_deg%3600)//60
    res[2]=(lat_deg%3600)%60
    res[4]=long_deg//3600
    res[5]=(long_deg%3600)//60
    res[6]=(long_deg%3600)%60
    return res
    

n=int(input("nombre de villes :"))

liste_des_villes=[]

for i in range(n):
    
    nombre=str(i+1)
    ville=input("nom de la ville"+nombre)
    liste_des_villes.append(ville)
    
driver=webdriver.Chrome(executable_path='chromedriver')
driver.get('https://fr.wikipedia.org/wiki/Wikip%C3%A9dia:Accueil_principal')
search_box = driver.find_element_by_xpath('//*[@id="searchInput"]')
enter_button=driver.find_element_by_xpath('//*[@id="searchButton"]')


L=[]

for i in range(n):
    ville=liste_des_villes[i]
    search_box = driver.find_element_by_xpath('//*[@id="searchInput"]')
    search_box.send_keys(ville)
    sleep(1)
    enter_button=driver.find_element_by_xpath('//*[@id="searchform"]/button')
    enter_button.click()
    coord_elem=driver.find_element_by_xpath('//*[@id="coordinates"]/a')
    coord=coord_elem.text
    L.append(coord)

bary=barycentre(L)

coord_bary=angles_to_coord(bary)

if coord_bary[3]=="nord":
    l1="N"
else:
    l1="S"
if coord_bary[7]=="ouest":
    l2="O"
else:
    l2="E"


coord_str=str(abs(coord_bary[0]))+"°"+str(abs(coord_bary[1]))+"'"+str(abs(coord_bary[2]))+'"'+l1+" "+str(abs(coord_bary[4]))+"°"+str(abs(coord_bary[5]))+"'"+str(abs(coord_bary[6]))+'"'+l2
print(coord_str)

driver.get('https://www.google.fr/maps')
accept_cookies = driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div/div[2]/div[1]/div[4]/form/div[1]/div/button')
accept_cookies.click()
search_bar=driver.find_element_by_xpath('//*[@id="searchboxinput"]')
search_bar.send_keys(coord_str)
validate=driver.find_element_by_xpath('//*[@id="searchbox-searchbutton"]')
validate.click()



        
        
    
    
    
    
    
    
    
    
    
    
    
        
        
