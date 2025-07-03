# utils/data_processing.py

import pandas as pd

def load_data():
    try:
        data = pd.read_csv(r"C:\Users\Hp\Desktop\airline_demand_app\data\sample_data.csv.txt")
        return data
    except:
        return pd.DataFrame()

def process_data(df):
    popular_routes = df.groupby(["origin", "destination"]).size().reset_index(name="count")
    popular_routes = popular_routes.sort_values(by="count", ascending=False).head(5)

    peak_days = df.groupby("date")["demand"].sum().reset_index()
    peak_days = peak_days.sort_values(by="demand", ascending=False).head(5)

    return {
        "popular_routes": popular_routes,
        "peak_days": peak_days
    }
