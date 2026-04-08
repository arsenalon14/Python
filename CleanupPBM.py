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

def cleanup(df):
    df=df.drop(columns=["CarrierCode","Capacity","SeatSold","CheckInCount","ProductClassCode","ConvertedCurrencyCode"],errors="ignore"
    )
    df["Sector"]=df["DepartureStation"]+df["ArrivalStation"]
    df["Sector2"]=df["ArrivalStation"]+df["DepartureStation"]
    df=df[df["SSRCode"].notna()]
    df["ConvertedChargeAmount"]=df["ConvertedChargeAmount"].str.replace(",","").astype(float)
    df["ConvertedChargeAmount"]=np.where(df["SSRCode"].isin(["WAK","WAKL"]),60*df["SSRCount"],df["ConvertedChargeAmount"])
    return df

def openup():
    print("Select Main File must be .csv")
    pbm_file = filedialog.askopenfilename(
        title="Main CSV",
        filetypes=[("CSV Files","*.csv")]
    )
    if not pbm_file:
        messagebox.showerror("Error","No File Selected")
        exit()

    print(f"Main file : {pbm_file}")

    print("Select File for xlookup must be .csv")
    lookup_file = filedialog.askopenfilename(
        title="Lookup File",
        filetypes=[("CSV Files","*.csv")]
    )
    if not lookup_file:
        messagebox.showerror("Error","No File Selected")
        exit()
    print(f"Xlookup File : {lookup_file}")
    
    df = pd.read_csv(pbm_file)
    print("\nOriginal shape:", df.shape)
    print(df.head())

    df = cleanup(df)
    print("\nClean up shape:", df.shape)
    print(df.head())

    df_lookup = pd.read_csv(lookup_file)
    df = df.merge(
        df_lookup[["FlightNumber","Country","Route"]],on="FlightNumber",how="left")
    df["Check"] = np.where((df["Sector"]==df["Route"]) | (df["Sector2"]==df["Route"]),"True",'False')

    print(df.shape)

    today = datetime.now().strftime("Date%Y-%m-%d_Time%H.%M.%S")
    output_file = os.path.join(os.path.dirname(pbm_file),f"PBM{today}.csv")

    df.to_csv(output_file, index=False, encoding="utf-8-sig")
    print("All Done")

openup()