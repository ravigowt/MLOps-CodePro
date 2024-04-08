# You can create more variables according to your project. The following are the basic variables that have been provided to you
root_folder = "/home/"
data_pipeline_folder = root_folder+"airflow/dags/lead_scoring_data_pipeline/"
DB_PATH = root_folder + "database/"
DB_FILE_NAME = "lead_scoring_clean_data.db"
DATA_DIRECTORY = data_pipeline_folder + "data/"
INTERACTION_MAPPING = data_pipeline_folder + "/mapping/interaction_mapping.csv"
INDEX_COLUMNS_TRAINING = ["created_date","city_tier","first_platform_c","first_utm_medium_c","first_utm_source_c","total_leads_droppped","referred_lead",
 "app_complete_flag"]
INPUT_CSV_PATH = f"{DATA_DIRECTORY}leadscoring.csv"




