import pandas as pd


def on_search(food_name, df):
    if not food_name.strip():
        return pd.DataFrame()
    return df[df['food'].str.contains(food_name, case=False, na=False)]




def nutrition_breakdown(food_data):
    if food_data is None or food_data.empty:
        raise ValueError("No valid data for breakdown")

    nutrients = {
        "Fat": food_data['Fat'],
        "Protein": food_data['Protein'],
        "Carbohydrates": food_data['Carbohydrates'],
        "Fiber": food_data['Dietary Fiber'],
    }
    return nutrients


def nutrition_range_filter(selected_nutrition, min_value, max_value, df):
    if min_value >= max_value:
        raise ValueError("Minimum value must be less than maximum value")

    if selected_nutrition not in df.columns:
        raise ValueError("Invalid nutrition type selected")

    filtered_foods = df[
        (df[selected_nutrition] >= min_value) & (df[selected_nutrition] <= max_value)
        ]['food'].tolist()
    return filtered_foods


def nutrition_level_filter(selected_nutrition, selected_level, df):
    if not selected_nutrition or not selected_level:
        raise ValueError("Please select both a nutrition content and a level")

    max_value = df[selected_nutrition].max()

    low_threshold = max_value * 0.33
    mid_threshold_low = max_value * 0.33
    mid_threshold_high = max_value * 0.66
    high_threshold = max_value * 0.66

    if selected_level == 'low':
        filtered_foods = df[df[selected_nutrition] < low_threshold]['food'].tolist()
    elif selected_level == 'mid':
        filtered_foods = df[
            (df[selected_nutrition] >= mid_threshold_low) & (df[selected_nutrition] <= mid_threshold_high)
            ]['food'].tolist()
    elif selected_level == 'high':
        filtered_foods = df[df[selected_nutrition] > high_threshold]['food'].tolist()
    else:
        raise ValueError("Invalid level selected")

    return filtered_foods


def export_as_csv(nutrient_data, path):
    df = pd.DataFrame(nutrient_data)
    df.to_csv(path, index=False)


def show_password(current_password, checkbox_state):
    if checkbox_state:
        return current_password
    else:
        return '*' * len(current_password)
