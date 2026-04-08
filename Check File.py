import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox
import chardet


def openedit():
    root = tk.Tk()
    root.withdraw()
    root.attributes('-topmost', True)
    print("Select Main File must be .csv")
    main_file = filedialog.askopenfilename(
        title="Main CSV",
        filetypes=[("CSV Files","*.csv")]
    )
    if not main_file:
        messagebox.showerror("Error","No File Selected")
        return
    with open(main_file,'rb') as f:
        result = chardet.detect(f.read(100000))
    check_encoding = result['encoding'] or 'utf-8'

    try:
        df = pd.read_csv(main_file,encoding=check_encoding)
    except UnicodeDecodeError:
        try: 
            df = pd.read_csv(main_file, encoding='latin1')
        except UnicodeDecodeError:
            df = pd.read_csv(main_file, encoding='cp874',errors='replace')
        
    print(df.dtypes)


openedit()