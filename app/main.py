from app.utils import load_data, preprocess_features, generate_costs, generate_unit_prices, generate_report

def run_pipeline(file_path, cost_percentage):
    df = load_data(file_path)

    df = preprocess_features(df)

    df = generate_costs(df, cost_percentage)

    df = generate_unit_prices(df)

    df = generate_report(df)
    print(df)
    return df

if __name__ == "__main__":
    FILE_PATH = "C:/Users/santi/Desktop/Pruebas unitarias en procesamiento de datos/Sample code/data/Chocolate Sales.csv"
    COST_PERCENTAGE = 40
    run_pipeline(FILE_PATH, COST_PERCENTAGE)