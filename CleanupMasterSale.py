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
    df = df.drop(columns=[
        'PG Reference Number','Close Sync Date','Close Sync Time','Carrier Code','Arrival Time (STA)',
        'Transaction Date','Transaction Time','Aircraft Registration','Aircraft Type','Product Brand',
        'Base Currency','Gross Sales (Base)','Product Tax Code','Product Tax Type','Product Tax','Bill Promo Name',
        'Bill Discount Type','Bill Discount Rate','Bill Discount Amount','Bill Subtotal','Card Holder Name',
        'Authorization Date','Authorization Time','Settlement Date','Refund Reason','Refund Remarks',
        'Device Name','Device ID','Seat Number','AUD','CNY','CUP','EUR','HKD','IDR','INR','JPY','MYR',
        'PHP','SGD','THB','TWD','USD','Card'
        ], errors='ignore')
    df["Flight Number"] = df["Flight Number"].str.extract(r'(\d+)').astype(int)  
    df = df[df["Payment Status"]!='Refunded']
    df["Product Category"] = df["Product Category"].fillna("Combo")
    df["Promo Ref ID"] = df["Promo Ref ID"].fillna("À la carte")
    df.columns = df.columns.str.replace(" ", "")
    df[["Country","Sector","Sector2"]] = ""
    df["Country"] = np.where(df["CountryofDestination"]=="THAILAND",df["CountryofOrigin"],df["CountryofDestination"])
    df["Sector"] = df["Origin"]+df["Destination"]
    df["Sector2"] = df["Destination"]+df["Origin"]
    df=df.rename(columns={"DepartureTime(STD)":"DepartureTime","NetSales(Base)":"NetSales"})
    return df

def openedit():
    print("Select Main File must be .csv")
    main_file = filedialog.askopenfilename(
        title="Main CSV",
        filetypes=[("CSV Files","*.csv")]
    )
    if not main_file:
        messagebox.showerror("Error","No File Selected")
        exit()

    print(f"Main file : {main_file}")

    print("Select File for xlookup must be .csv")
    lookupfile = filedialog.askopenfilename(
        title="Lookup File",
        filetypes=[("CSV Files","*.csv")]
    )
    if not lookupfile:
        messagebox.showerror("Error","No File Selected")
        exit()
    print(f"Xlookup File : {lookupfile}")
    
    df = pd.read_csv(main_file)
    print("\nOriginal shape:", df.shape)
    print(df.head())

    df = cleanup(df)
    print("\nClean up shape:", df.shape)
    print(df.head())

    df_lookup = pd.read_csv(lookupfile)
    df = df.merge(
        df_lookup[["FlightNumber","Route"]], on="FlightNumber", how="left")
    df["Check"] = np.where((df["Sector"]==df["Route"]) | (df["Sector2"]==df["Route"]),"True",'False')
    print("After look up",df.shape)

    today = datetime.now().strftime("Date%Y-%m-%d_Time%H.%M.%S")
    output_file = os.path.join(os.path.dirname(main_file),f"MasterSaleFile{today}.csv")

    df.to_csv(output_file, index=False, encoding="utf-8-sig")
    print("All Done")

openedit()
