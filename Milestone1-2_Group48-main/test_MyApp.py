import pytest
import pandas as pd

from nutrition_function import on_search, nutrition_breakdown, nutrition_range_filter, nutrition_level_filter, export_as_csv, show_password

# Test Functions for on_search

def test_on_search_valid():
    df = pd.DataFrame({'food': ['apple', 'banana', 'cherry']})
    result = on_search('apple', df)
    assert not result.empty
    assert 'apple' in result['food'].values


def test_on_search_invalid():
    df = pd.DataFrame({'food': ['apple', 'banana', 'cherry']})

    result = on_search('unknown_food', df)
    assert result.empty, f"Expected empty result but got {result}"

    result = on_search('', df)
    assert result.empty, f"Expected empty result but got {result}"


# Test Functions for nutrition_breakdown

def test_nutrition_breakdown_valid():
    get_searched = pd.Series({"Fat": 10, "Protein": 5, "Carbohydrates": 15, "Dietary Fiber": 5})
    nutrients = nutrition_breakdown(get_searched)
    assert nutrients['Fat'] == 10
    assert nutrients['Protein'] == 5
    assert nutrients['Carbohydrates'] == 15
    assert nutrients['Fiber'] == 5


def test_nutrition_breakdown_invalid():
    with pytest.raises(ValueError, match="No valid data for breakdown"):
        nutrition_breakdown(None)

    empty_series = pd.Series()
    with pytest.raises(ValueError, match="No valid data for breakdown"):
        nutrition_breakdown(empty_series)


# Test Functions for nutrition_range_filter

def test_nutrition_range_valid():
    df = pd.DataFrame({
        'food': ['apple', 'banana', 'cherry'],
        'Protein': [15, 5, 25]
    })
    result = nutrition_range_filter('Protein', 10, 20, df)
    assert isinstance(result, list)
    assert len(result) == 1
    assert 'apple' in result

def test_nutrition_range_invalid():
    df = pd.DataFrame({
        'food': ['apple', 'banana', 'cherry'],
        'Fat': [10, 20, 30]
    })
    with pytest.raises(ValueError):
        nutrition_range_filter('Fat', 20, 10, df)

# Test Functions for nutrition_level_filter

def test_nutrition_level_valid():
    df = pd.DataFrame({
        'food': ['apple', 'banana', 'cherry'],
        'Fat': [5, 15, 25]
    })
    result = nutrition_level_filter('Fat', 'low', df)
    assert isinstance(result, list)
    assert len(result) == 1
    assert 'apple' in result

def test_nutrition_level_invalid():
    df = pd.DataFrame({
        'food': ['apple', 'banana', 'cherry'],
        'Protein': [10, 20, 30]
    })
    with pytest.raises(ValueError):
        nutrition_level_filter('Protein', 'medium', df)

# Test Functions for export_as_csv

def test_export_as_csv_valid(tmp_path):
    nutrient_data = {
        "Nutrient": ["Fat", "Protein"],
        "Amount": [10, 5]
    }
    path = tmp_path / "nutrients.csv"
    export_as_csv(nutrient_data, str(path))
    assert path.exists()

def test_export_as_csv_path_invalid():
    nutrient_data = {
        "Nutrient": ["Fat", "Protein"],
        "Amount": [10, 5]
    }
    invalid_path = "/invalid_directory/nutrients.csv"
    with pytest.raises(OSError):
        export_as_csv(nutrient_data, invalid_path)

# Test Functions for show_password

def test_show_password_checked():
    password = "mypassword"
    result = show_password(password, True)
    assert result == password

def test_show_password_unchecked():
    password = "mypassword"
    result = show_password(password, False)
    assert result == "**********"