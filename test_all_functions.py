import pytest
import pandas as pd
from all_functions import on_search, nutrition_breakdown, nutrition_range_filter, nutrition_level_filter, export_as_csv, show_password

# Sample DataFrame for testing
test_df = pd.DataFrame({
    'food': ['Apple', 'Banana', 'Carrot', 'Orange', 'Strawberry'],
    'Fat': [0.1, 0.3, 0.2, 0.1, 0.4],
    'Protein': [0.5, 1.0, 0.8, 0.6, 0.7],
    'Carbohydrates': [14.0, 22.0, 9.0, 12.0, 7.0],
    'Dietary Fiber': [4.0, 2.0, 3.0, 2.0, 1.0]
})

def test_on_search_empty_food_name():
    result = on_search('', test_df)
    assert result.empty

def test_on_search_valid_food_name():
    result = on_search('Apple', test_df)
    assert len(result) == 1
    assert result['food'].iloc[0] == 'Apple'

def test_on_search_partial_food_name():
    result = on_search('an', test_df)
    assert len(result) == 2
    assert 'Banana' in result['food'].tolist()
    assert 'Orange' in result['food'].tolist()

def test_nutrition_breakdown_valid_data():
    food_data = test_df[test_df['food'] == 'Apple']
    result = nutrition_breakdown(food_data)
    assert result['Fat'] == 0.1
    assert result['Protein'] == 0.5
    assert result['Carbohydrates'] == 14.0
    assert result['Fiber'] == 4.0

def test_nutrition_breakdown_empty_data():
    with pytest.raises(ValueError):
        nutrition_breakdown(pd.DataFrame())

def test_nutrition_range_filter_valid_range():
    result = nutrition_range_filter('Fat', 0.1, 0.3, test_df)
    assert 'Apple' in result
    assert 'Carrot' in result
    assert 'Orange' in result
    assert 'Banana' in result
    assert 'Strawberry' not in result

def test_nutrition_range_filter_invalid_range():
    with pytest.raises(ValueError):
        nutrition_range_filter('Fat', 0.5, 0.3, test_df)

def test_nutrition_range_filter_invalid_nutrition():
    with pytest.raises(ValueError):
        nutrition_range_filter('Vitamin C', 0.1, 0.3, test_df)

def test_nutrition_level_filter_valid_level():
    result = nutrition_level_filter('Fat', 'low', test_df)
    assert 'Apple' in result
    assert 'Orange' in result
    assert 'Banana' not in result
    assert 'Strawberry' not in result

    result = nutrition_level_filter('Fat', 'mid', test_df)
    assert 'Carrot' in result
    assert 'Strawberry' not in result
    assert 'Apple' not in result
    assert 'Orange' not in result

    result = nutrition_level_filter('Fat', 'high', test_df)
    assert 'Strawberry' in result
    assert 'Banana' not in result
    assert 'Apple' not in result
    assert 'Carrot' not in result
    assert 'Orange' not in result

def test_nutrition_level_filter_invalid_level():
    with pytest.raises(ValueError):
        nutrition_level_filter('Fat', 'medium', test_df)

def test_nutrition_level_filter_missing_input():
    with pytest.raises(ValueError):
        nutrition_level_filter(None, None, test_df)

def test_export_as_csv_valid_data(tmp_path):
    nutrient_data = [
        {'food': 'Apple', 'Fat': 0.1, 'Protein': 0.5, 'Carbohydrates': 14.0, 'Fiber': 4.0},
        {'food': 'Banana', 'Fat': 0.3, 'Protein': 1.0, 'Carbohydrates': 22.0, 'Fiber': 2.0}
    ]
    output_path = tmp_path / 'nutrient_data.csv'
    export_as_csv(nutrient_data, output_path)
    assert output_path.exists()

def test_show_password_checked():
    result = show_password('password', True)
    assert result == 'password'

def test_show_password_unchecked():
    result = show_password('password', False)
    assert result == '********'