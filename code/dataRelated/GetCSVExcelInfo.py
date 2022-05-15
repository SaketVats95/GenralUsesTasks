import pandas as pd
import os


def SelectFileName(dirName = ''):
    if dirName == '':
        dirName = '.'
    files = [f for f in os.listdir(dirName) if os.path.isfile(f) \
        and (os.path.splitext(f)[1].lower() == 'csv' or  os.path.splitext(f)[1].lower() == 'xlsx')]
    
    print(files)
    fileName = input("Please Enter File Name Index Starts From 0 :: ")
    print(os.path.abspath(files[int(fileName)]))
    # print(files[])
    return os.path.abspath(files[int(fileName)])

# SelectFileName()

def ReadFile(fileName = ''):
    if fileName == '':
        fileName = SelectFileName()
    if os.path.splitext(fileName)[1].lower() == 'csv':
        df = pd.read_csv(fileName)
        df.describe()
    else:
        xl = pd.ExcelFile('foo.xlsx')
        print(xl.sheet_names)
        sheetName = input("Please Enter Sheet Name Index Starts From 0 :: ")
        df = xl.parse(xl.sheet_names[int(sheetName)])
        xl.close()

def GetInfoAndDf(df):

    print(f"totalCols = {len(df.columns)}")

    print(f"totalRows = {df[0].count()}")
    print(f"Info : {df.info()}")
    return df

