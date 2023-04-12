import pandas as pd
import json
import os

# Set the file path
file_path = "E:\\steps to add Quran Sound\\cleaned_file.xlsx"

# Set the number of rows per split
rows_per_split = 20

# Load the excel file
excel_file = pd.ExcelFile(file_path)


# Get the sheet names
sheet_names = excel_file.sheet_names

# Create the output directory if it does not exist
output_dir = "E:\\steps to add Quran Sound\\json files\\"
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

# import pandas as pd
# import json

# # Define the input and output file paths
# input_file = 'E:\\steps to add Quran Sound\\cleaned_file.xlsx'
# output_dir = 'E:\\steps to add Quran Sound\\'

# # Read the Excel file into a Pandas dataframe
# df = pd.read_excel(input_file)

# # Drop null rows
# df = df.dropna()

# # Split the dataframe into multiple dataframes based on the number of rows
# num_rows_per_file = 250
# num_files = len(df) // num_rows_per_file + 1

# for i in range(num_files):
#     start_index = i * num_rows_per_file
#     end_index = min(start_index + num_rows_per_file, len(df))
#     filename = f'{output_dir}output_{i+1}.json'

#     # Extract the subset of rows from the dataframe
#     subset_df = df.iloc[start_index:end_index, :]

#     # Convert the subset dataframe to a list of dictionaries and then to JSON
#     subset_list = subset_df.to_dict('records')
#     subset_json = json.dumps(subset_list, ensure_ascii=False)

#     # Write the JSON output to a file
#     with open(filename, 'w', encoding='utf-8') as f:
#         f.write(subset_json)
