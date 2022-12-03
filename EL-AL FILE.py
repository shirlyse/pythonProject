import pandas as pd

#import file, after conversion to csv
df = pd.read_csv(r'C:\Users\sshir\OneDrive\Documents\EL AL PROJECT\original\PitsReport-22_09_01-22_09_16.CSV', error_bad_lines=False, sep="\;", engine="python")

#if needed
#df = pd.read_excel("pit.xlsx")
#df = df.drop([213])

# Drop the first 22 rows of the DataFrame
#first row starts at index 22!!
df.drop(df.index[:22], inplace=True)
#df.drop(df.index[19], inplace=True)
#df.drop(df.index[20], inplace=True)
df = df.reset_index(drop=False)

#REMOVE irelevant columns
#df = df.drop(df.columns[[2, 5 , 8, 10 , 11,14,17,18,20,22]], axis=1)
#KEEP RELEVANT COLOUMNS - see if remove 3 4 9 19 (pits and arrive info
df = df.drop(df.columns.difference(df.columns[[1, 3, 4, 6,  9, 12, 13, 16, 19, 21]]), axis=1)

#give headers name
df.columns = ["Plane_id", "Flight_id2", "Arrival_date", "Arrival_time", "arrival_pit", "Flight_id", "Departure_date", "Departure_time", "Departure_pit", "Parking_time"]
print(df)

#make as an excel file -create a function for that taking the df and wanted name of file
writer = pd.ExcelWriter(r'elal.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='Sheet1', index=False)
# Close the Pandas Excel writer and output the Excel file.
writer.close()
reader = pd.read_excel(r'elal.xlsx')
