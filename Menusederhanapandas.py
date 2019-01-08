import pandas as pd
from sqlalchemy import create_engine

engine=create_engine("mysql+mysqlconnector://root:dessy@localhost/pokemon?host=localhost?port=3306")
conn=engine.connect()

def Mainmenu():
    pilihan =input("Menu utama \n 1. Lihat data \n 2. Filter data \n 3. Keluar \n Masukan Pilihan Anda ")
    return pilihan

def LihatSemuaData():
    results=conn.execute("select * from datapokemon").fetchall()
    dfdata= pd.DataFrame(results)
    print(dfdata.head())

def filterdata():
    results=conn.execute("select distinct Type2 from datapokemon").fetchall()
    dfdata=pd.DataFrame(results)
    print(dfdata)
    pil1=int(input("masukan pilihan anda :"))
    pil2=dfdata.values[pil1][0]
    pil3=conn.execute("select * from datapokemon where Type2 = '{}'".format(pil2)).fetchall()
    dfdata=pd.DataFrame(pil3)
    dfdata.columns=pil3[0].keys()
    print(dfdata)

while (True):
    pilihan = Mainmenu()
    if(pilihan == "1"):
        LihatSemuaData()
    elif(pilihan == "2"):
        filterdata()
    elif(pilihan == "3"):
        print("see you")
        break

