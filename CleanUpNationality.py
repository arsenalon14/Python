import pandas as pd
import numpy as np
import tkinter as tk
from tkinter import filedialog, messagebox
import os
from datetime import datetime

root = tk.Tk()
root.withdraw()
root.lift()
root.attributes('-topmost', True)

def cleanupnat(df):
    df = df.drop(columns=["FareClassType"])
    df = df[df["LiftStatus"]=='Boarded']
    df["Nationality"] = df["Nationality"].fillna("Thailand")
    df["Sector2"] = ""
    df["Sector2"] = df["Sector"].str[3:]+df["Sector"].str[:3]
    return df

def openandfinishfile():
    print("Select Main File Must be .csv")
    main= filedialog.askopenfilename(
        title="MainCSV",
        filetypes=[("CSV File","*.csv")]
    )
    if not main:
        messagebox.showerror("Error","No File Selected")
        exit()
    print(f'Main File:{main}')

    print("Select Main File Must be .csv")
    lookupfile= filedialog.askopenfilename(
        title="lookupCSV",
        filetypes=[("CSV File","*.csv")]
    )
    if not lookupfile:
        messagebox.showerror("Error","No File Selected")
        exit()
    print(f'lookup File:{lookupfile}')

    df = pd.read_csv(main)
    print(df.head())

    df = cleanupnat(df)
    print(df.head())
    
    df_lookup = pd.read_csv(lookupfile) 
    df=df.merge(
        df_lookup[["FlightNumber","Country","Route"]], on="FlightNumber", how="left")
    df["Check"] = np.where((df["Sector"]==df["Route"]) | (df["Sector2"]==df["Route"]),"True",'False')
    print("After look up",df.shape)

    today = datetime.now().strftime("Date%Y-%m-%d_Time%H.%M.%S")
    output_file = os.path.join(os.path.dirname(main),f"NationalityFile{today}.csv")

    df.to_csv(output_file, index=False, encoding="utf-8-sig")
    print("All Done")

openandfinishfile()

