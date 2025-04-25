# repository/progress_repo.py
import pandas as pd
from db.db import get_connection

def get_student_theme_progress(student_id):
    with get_connection() as conn:
        return pd.read_sql_query(
            f"SELECT * FROM StudentThemeProgress WHERE student_id = {student_id}", conn
        )
