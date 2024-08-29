from fastapi.responses import JSONResponse
import pandas as pd
from sklearn.model_selection import train_test_split

from app.services.utils.mapper import Mapper
from app.services.utils.datasets_tools import DatasetsTools

def split_dataset(df, ratio):
    """
    Split DataFrame into train and test sets and save to CSV files.

    Args:
    df (pd.DataFrame): Input DataFrame to split.
    ratio (float): Ratio of test data to total data.

    Returns:
    pd.DataFrame: Test DataFrame.
    """
    _, test_df = train_test_split(df, test_size=(1 - ratio))
    return test_df

def filter_test_columns(test_df, columns_to_keep):
    """
    Keep only specified columns in the test DataFrame and save to CSV.

    Args:
    test_df (pd.DataFrame): Test DataFrame to filter.
    columns_to_keep (list): List of columns to keep in the test DataFrame.

    Returns:
    pd.DataFrame: Filtered test DataFrame.
    """
    return test_df[columns_to_keep]

def append_dict_to_csv(data_dict, csv_name):
    """
    Append dictionary data to a CSV file.

    Args:
    data_dict (dict): Dictionary containing data to append to CSV.
    csv_name (str): Name of the CSV file to append to.

    Returns:
    pd.DataFrame: Combined DataFrame after appending.
    """
    # Convert the dictionary to a DataFrame
    df = pd.DataFrame.from_dict(data_dict)
    
    try:
        # Try to read the existing CSV file
        existing_df = pd.read_csv(csv_name)
        # Concatenate the existing DataFrame with the new DataFrame
        combined_df = pd.concat([existing_df, df], ignore_index=True)
    except FileNotFoundError:
        # If the CSV file does not exist, the combined DataFrame is just the new DataFrame
        combined_df = df
    
    # Save the combined DataFrame to the CSV file
    combined_df.to_csv(csv_name, index=False)
    
    return combined_df
        
def process_and_append_maternal_data(maternal, df, name=''):
    """
    Process maternal data, predict outcomes, and append results to CSV files.

    Args:
    maternal (object): Maternal model object for prediction.
    df (pd.DataFrame): Input DataFrame containing maternal data.
    name (str, optional): Name prefix for CSV files (default is None).

    Returns:
    JSONResponse: JSON response indicating completion status.
    """
    for index, row in df.iterrows():
        maternal_row = {
            "Age": row.Age,
            "SystolicBP": row.SystolicBP,
            "DiastolicBP": None,
            "BS": row.BS,
            "BodyTemp": row.BodyTemp,
            "HeartRate": row.HeartRate,
        }
        datasets_tools = DatasetsTools.get_instance()
        k_nearest_rows = datasets_tools.find_nearest_rows(maternal, maternal_row, 1)
        row_to_predict = Mapper.fill_empty_values(maternal_row, k_nearest_rows)
        row_to_predict = Mapper.map_to_ds_row(maternal, row_to_predict)
        result = maternal.predict(row_to_predict)
        result_csv_name = name + 'maternal_result.csv'
        lines_csv_name = name + 'maternal_lines.csv'
        result["Expected_Risk"] = row.RiskLevel
        append_dict_to_csv(result, result_csv_name)
        append_dict_to_csv(row_to_predict, lines_csv_name)
    return JSONResponse(content={"message": "Done"})

def process_and_append_ckd_data(ckd, df, name=''):
    """
    Process CKD data, predict outcomes, and append results to CSV files.

    Args:
    ckd (object): CKD model object for prediction.
    df (pd.DataFrame): Input DataFrame containing CKD data.
    name (str, optional): Name prefix for CSV files (default is None).

    Returns:
    JSONResponse: JSON response indicating completion status.
    """
    for index, row in df.iterrows():
        ckd_row = {
            "age": row.age,
            "bp": row.bp,
            "sg": None,
            "al": None,
            "su": None,
            "rcb": None,
            "pc": None,
            "pcc": None,
            "ba": None,
            "bgr": row.bgr,
            "bu": None,
            "sc": None,
            "sod": None,
            "pot": None,
            "hemo": None,
            "pcv": None,
            "wbcc": None,
            "rbcc": None,
            "htn": None,
            "dm": None,
            "cad": None,
            "appet": None,
            "pe": None,
            "ane": None,
        }
        datasets_tools = DatasetsTools.get_instance()
        k_nearest_rows = datasets_tools.find_nearest_rows(ckd, ckd_row, 1)
        row_to_predict = Mapper.fill_empty_values(ckd_row, k_nearest_rows)
        row_to_predict = Mapper.map_to_ds_row(ckd, row_to_predict)
        result = ckd.predict(row_to_predict)
        result_csv_name = name + 'ckd_result.csv'
        lines_csv_name = name + 'ckd_lines.csv'
        result["Expected_CKD"] = row.ckd
        append_dict_to_csv(result, result_csv_name)
        append_dict_to_csv(row_to_predict, lines_csv_name)
    return JSONResponse(content={"message": "Done"})

def process_and_append_disease_data(disease, df, name=''):
    """
    Process Disease data, predict outcomes, and append results to CSV files.

    Args:
    disease (object): Disease model object for prediction.
    df (pd.DataFrame): Input DataFrame containing Disease data.
    name (str, optional): Name prefix for CSV files (default is None).

    Returns:
    JSONResponse: JSON response indicating completion status.
    """
    for index, row in df.iterrows():
        disease_row = {
            "Discharge": None,
            "Feelings_and_Urge": row.Feelings_and_Urge,
            "Pain_and_Infection": None,
            "Physical_Conditions": None,
            "Critical_Feelings": row.Critical_Feelings,
            "Disease": row.Disease,
        }
        datasets_tools = DatasetsTools.get_instance()
        k_nearest_rows = datasets_tools.find_nearest_rows(disease, disease_row, 1)
        row_to_predict = Mapper.fill_empty_values(disease_row, k_nearest_rows)
        row_to_predict = Mapper.map_to_ds_row(disease, row_to_predict)
        result = disease.predict(row_to_predict)
        result_csv_name = name + 'disease_result.csv'
        lines_csv_name = name + 'disease_lines.csv'
        result["Expected_Critical"] = row.Critical
        append_dict_to_csv(result, result_csv_name)
        append_dict_to_csv(row_to_predict, lines_csv_name)
    return JSONResponse(content={"message": "Done"})

def process_and_append_cass_data(cassi, df, name=''):
    """
    Process Cassi data, predict outcomes, and append results to CSV files.

    Args:
    cassi (object): Cassi model object for prediction.
    df (pd.DataFrame): Input DataFrame containing Cassi data.
    name (str, optional): Name prefix for CSV files (default is None).

    Returns:
    JSONResponse: JSON response indicating completion status.
    """
    for index, row in df.iterrows():
        cassi_row = {
            "Operative_Procedure": row.Operative_Procedure,
            "Infections_Reported": row.Infections_Reported,
            "Infections_Predicted": None,
            "Procedure_Count": row.Procedure_Count,
        }
        datasets_tools = DatasetsTools.get_instance()
        k_nearest_rows = datasets_tools.find_nearest_rows(cassi, cassi_row, 1)
        row_to_predict = Mapper.fill_empty_values(cassi_row, k_nearest_rows)
        row_to_predict = Mapper.map_to_ds_row(cassi, row_to_predict)
        result = cassi.predict(row_to_predict)
        result_csv_name = name + 'cassi_result.csv'
        lines_csv_name = name + 'cassi_lines.csv'
        result["Expected_SIR"] = row.SIR
        append_dict_to_csv(result, result_csv_name)
        append_dict_to_csv(row_to_predict, lines_csv_name)
    return JSONResponse(content={"message": "Done"})