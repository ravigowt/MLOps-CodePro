# You can create more variables according to your project. The following are the basic variables that have been provided to you
root_folder = "/home/"
data_pipeline_folder = root_folder+"/unit_test/"
DB_PATH = data_pipeline_folder + "database/"
DB_FILE_NAME = "lead_scoring_clean_data.db"
UNIT_TEST_DB_FILE_NAME = "unit_test_cases.db"
DATA_DIRECTORY = data_pipeline_folder
INTERACTION_MAPPING = data_pipeline_folder + "interaction_mapping.csv"
INDEX_COLUMNS_TRAINING = ["created_date","city_tier","first_platform_c","first_utm_medium_c","first_utm_source_c","total_leads_droppped","referred_lead",
 "app_complete_flag"]
INPUT_CSV_PATH = f"{DATA_DIRECTORY}leadscoring_test.csv"




