import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox
import os

root = tk.Tk()
root.withdraw()
root.lift()
root.attributes('-topmost', True)

def openfile():
    print("Select File")
    file=filedialog.askopenfilename(
        title="Select file",
        filetypes=[("CSV File","*.csv")]
    )
     
    if not file:
        print("No file Select")
        return
    
    print(f"file : {file}")

    df=pd.read_csv(file)
    print(df.head())

    for col in df.columns:
        if df[col].dtype == 'int64':
            df[col] = df[col].astype('int32')
        elif df[col].dtype == 'float64':
            df[col] = df[col].astype('float32')
    base, ext=os.path.splitext(file)
    output=f'{base}_resize{ext}'

    df.to_csv(output,index=False)
    print(f"save as: {output}")
    messagebox.showinfo("Done", f"Saved as:\n{output}")

openfile()