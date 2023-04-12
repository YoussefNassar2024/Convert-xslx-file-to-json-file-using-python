import pandas as pd
import json
import os
##First of all you should drop null rows value##
################################################
# Prompt user for file path
file_path = 'E:\\Your file.xlsx'

# Load Excel file
df = pd.read_excel(file_path)

# Remove empty rows
df.dropna(how='all', inplace=True)

# Prompt user for output file path
output_path = "E:\\cleaned_file.xlsx"

# Save cleaned Excel file
df.to_excel(output_path, index=False)

##Now choose the cleaned file to convert it to json##
#####################################################
# Set the file path
file_path = "E:\\\cleaned_file.xlsx"

# Set the number of rows per split
rows_per_split = 20 #set any number you want

# Load the excel file
excel_file = pd.ExcelFile(file_path)


# Get the sheet names
sheet_names = excel_file.sheet_names

# Create the output directory if it does not exist
output_dir = "E:\\json files\\" # files are saved here
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
    
# Split the data into chunks and save each chunk as a json file
for sheet_name in sheet_names:
    # Load the sheet data into a dataframe
    df = pd.read_excel(file_path, sheet_name=sheet_name)

    # Split the dataframe into chunks
    chunks = [df[i:i+rows_per_split] for i in range(0, df.shape[0], rows_per_split)]

    # Save each chunk as a json file
    for i, chunk in enumerate(chunks):
        output_file_path = os.path.join(output_dir, f"{sheet_name}_{i+1}.json")
        with open(output_file_path, 'w', encoding='utf-8') as f:
            f.write(chunk.to_json(force_ascii=False, orient='records'))
            print(f"Saved {output_file_path}")

