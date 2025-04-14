import pandas as pd
from pathlib import Path

def load_data(file_path: str) -> pd.DataFrame:
    ext = Path(file_path).suffix
    
    if ext != ".csv":
        raise ValueError("incorrect file format")
    
    print(file_path)
    df = pd.read_csv(file_path)
    return df


def preprocess_features(data: pd.DataFrame) -> pd.DataFrame:
    data.columns = [x.lower().replace(" ", "_").strip() for x in data.columns]
    data["country"] = data["country"].str.lower()
    data["sales_person"] = data["sales_person"].str.lower()
    data["product"] = data["product"].str.lower()
    data["amount"] = data["amount"].str.replace("$", "").str.replace(",", ".").str.strip().astype(float)
    data["date"] = pd.to_datetime(data["date"])
    data["year"] = data["date"].dt.year.astype("int64")
    data["month"] = data["date"].dt.month.astype("int64")
    return data


def generate_costs(data: pd.DataFrame, percentage: int = 40) -> pd.DataFrame:
    data["cost"] = data["amount"] * (percentage / 100)
    return data


def generate_unit_prices(data: pd.DataFrame) -> pd.DataFrame:
    data["unit_price"] = (data["amount"] / data["boxes_shipped"]).round(6)
    data["unit_cost"] = (data["cost"] / data["boxes_shipped"]).round(6)
    return data


def generate_report(data: pd.DataFrame) -> pd.DataFrame:
    data = data[["year", "month", "country", "amount", "cost", "unit_price", "unit_cost"]].groupby(["year", "month", "country"]).mean().reset_index()
    return data