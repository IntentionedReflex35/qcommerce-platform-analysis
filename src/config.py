from pathlib import Path

# Resolves to the project root
PROJECT_ROOT = Path(__file__).resolve().parent.parent

DATA_RAW = PROJECT_ROOT/'data'/'quick_commerce_data_raw.csv'
DATA_CLEAN = PROJECT_ROOT/'data'/'qcommerce_data_clean.csv'
DATA_OUTLIERS = PROJECT_ROOT/'data'/'outlier_log_iqr.csv'
PLOTS_DIR = PROJECT_ROOT/'plots'