import pandas as pd
import sys
import pathlib
pd.options.display.max_rows = 100
#registry_dataframe.columns =


def parse_registry_dataframe(df: pd.DataFrame):
    parsed_registry_dataframe = pd.DataFrame(columns=['id','Title','Description','Hive','Path','Name',"Type","Value"])
    parsed_registry_dataframe["Title"] = df.get(["Title"])
    parsed_registry_dataframe["id"] = df.get(["id"])
    parsed_registry_dataframe["Description"] = df.get(["Description"])
    parsed_registry_dataframe["Hive"] = df.get(["Hive"]) 
    parsed_registry_dataframe["Path"] = df.get(["Path"]) 
    parsed_registry_dataframe["Name"] = df.get(["Name"]) 
    parsed_registry_dataframe["Type"] = df.get(["Type"]) 
    parsed_registry_dataframe["Value"] = df.get(["Value"]) 
    parsed_registry_dataframe = parsed_registry_dataframe.dropna(how="any")
    return parsed_registry_dataframe

def parse_commands_dataframe(df: pd.DataFrame):
    parsed_command_dataframe = pd.DataFrame()
    parsed_command_dataframe["id"] = df.get(["id"])
    parsed_command_dataframe["Title"] = df.get(["Title"])
    parsed_command_dataframe["Description"] = df.get(["Description"])
    parsed_command_dataframe["Command"] = df.get(["Command"])
    parsed_command_dataframe["Result"] = df.get(["Result"])
    parsed_command_dataframe["Fix"] = df.get(["Fix"])
    parsed_command_dataframe = parsed_command_dataframe.dropna(how="any")
    return parsed_command_dataframe


if __name__ == "__main__":
    if (len(sys.argv) < 2):
        print("Usage: python3 excel_parser.py [csv or excel file] [outfile name]")
    with open(sys.argv[1]) as file:
        if pathlib.Path(sys.argv[1]).suffix == ".csv":
            csv_dataframe = pd.read_csv(file,delimiter=";",header=0)
            prdf = parse_registry_dataframe(csv_dataframe)
            pcdf = parse_commands_dataframe(csv_dataframe)
            prdf.to_xml("assets/registries.xml",index=False,root_name="Tests",row_name="Test")
            pcdf.to_xml("assets/commands.xml",index=False,root_name="Tests",row_name="Test")
        if pathlib.Path(sys.argv[1]).suffix == ".xlsx":
            excel_dataframe = pd.read_excel(file,header=0,sheet_name="siemens")
            parse_dataframe(excel_dataframe)