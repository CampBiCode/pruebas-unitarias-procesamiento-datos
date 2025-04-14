import pandas as pd
from pandas.testing import assert_frame_equal, assert_series_equal
import pytest
from app.main import run_pipeline
from app.utils import load_data

MOCK_DATA = data = {
    "year": [2022]*16,
    "month": [1, 1, 1, 2, 2, 3, 3, 4, 4, 4, 6, 7, 7, 7, 8, 8],
    "country": [
        "australia", "canada", "uk", "canada", "uk", "australia", "usa",
        "australia", "new zealand", "usa", "india", "australia", "india",
        "new zealand", "india", "new zealand"
    ],
    "amount": [
        6.790, 1.442, 7.903, 6.433, 13.685, 3.080, 3.703,
        12.726, 3.990, 3.017, 5.376, 2.835, 4.501,
        168.000, 7.896, 8.379
    ],
    "cost": [
        2.7160, 0.5768, 3.1612, 2.5732, 5.4740, 1.2320, 1.4812,
        5.0904, 1.5960, 1.2068, 2.1504, 1.1340, 1.8004,
        67.2000, 3.1584, 3.3516
    ],
    "unit_price": [
        0.019073, 0.005042, 0.061061, 0.066015, 0.074375, 0.042192, 0.336636,
        0.037211, 0.067627, 0.021550, 0.141474, 0.027794, 0.049462,
        1.076923, 0.084000, 0.048434
    ],
    "unit_cost": [
        0.007629, 0.002017, 0.024424, 0.0264055, 0.029750, 0.016877, 0.134655,
        0.014884, 0.027051, 0.008620, 0.056589, 0.011118, 0.019785,
        0.430769, 0.033600, 0.019373
    ]
}

def test_finance_report_pipeline():
    # configuracion
    test_file_path = "C:/Users/santi/Desktop/Pruebas unitarias en procesamiento de datos/Sample code/tests/test_data.csv"
    cost_percentage = 40

    # procesamiento
    df_result = run_pipeline(test_file_path, cost_percentage)
    df_expected = pd.DataFrame(MOCK_DATA)

    # validacion
    assert_frame_equal(df_result, df_expected)

def test_cost_report():
    test_file_path = "C:/Users/santi/Desktop/Pruebas unitarias en procesamiento de datos/Sample code/tests/test_data.csv"
    cost_percentage = 40

    df_result = run_pipeline(test_file_path, cost_percentage)

    cost_result = df_result["cost"]
    cost_expected = pd.DataFrame(MOCK_DATA)["cost"]
    assert_series_equal(cost_result, cost_expected)


def test_load_data_incorrect_format():
    test_file_path = "C:/Users/santi/Desktop/Pruebas unitarias en procesamiento de datos/Sample code/tests/test_data.parquet"

    with pytest.raises(ValueError):
        df = load_data(test_file_path)