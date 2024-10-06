import pandas as pd

def on_search(food_name, df):
    """
    Searches for food items in a DataFrame based on partial or complete food name input.

    Args:
        food_name (str): The food name to search for.
        df (pd.DataFrame): The DataFrame containing food data.

    Returns:
        pd.DataFrame: A DataFrame containing rows matching the search term.
    """
    if not food_name.strip():
        return pd.DataFrame()
    return df[df['food'].str.contains(food_name, case=False, na=False)]


def nutrition_breakdown(food_data):
    """
    Extracts and returns a dictionary containing the nutritional breakdown for a given food item.

    Args:
        food_data (pd.DataFrame): A DataFrame containing data for a single food item.

    Returns:
        dict: A dictionary with keys 'Fat', 'Protein', 'Carbohydrates', and 'Fiber',
              and values corresponding to the respective nutritional values.

    Raises:
        ValueError: If food_data is None or empty.
    """
    if food_data is None or food_data.empty:
        raise ValueError("No valid data for breakdown")

    nutrients = {
        "Fat": food_data['Fat'].iloc[0],
        "Protein": food_data['Protein'].iloc[0],
        "Carbohydrates": food_data['Carbohydrates'].iloc[0],
        "Fiber": food_data['Dietary Fiber'].iloc[0],
    }
    return nutrients


def nutrition_range_filter(selected_nutrition, min_value, max_value, df):
    """
    Filters foods based on a specified nutrition content within a given range.

    Args:
        selected_nutrition (str): The name of the nutrition content to filter by.
        min_value (float): The minimum value for the selected nutrition.
        max_value (float): The maximum value for the selected nutrition.
        df (pd.DataFrame): The DataFrame containing food data.

    Returns:
        list: A list of food names that meet the specified range criteria.

    Raises:
        ValueError: If min_value is greater than or equal to max_value,
                    or if selected_nutrition is not a valid column in the DataFrame.
    """
    if min_value >= max_value:
        raise ValueError("Minimum value must be less than maximum value")

    if selected_nutrition not in df.columns:
        raise ValueError("Invalid nutrition type selected")

    filtered_foods = df[
        (df[selected_nutrition] >= min_value) & (df[selected_nutrition] <= max_value)
        ]['food'].tolist()
    return filtered_foods


def nutrition_level_filter(selected_nutrition, selected_level, df):
    """
    Filters foods based on a specified nutrition content and a level (low, mid, high).

    Args:
        selected_nutrition (str): The name of the nutrition content to filter by.
        selected_level (str): The level of the selected nutrition ('low', 'mid', 'high').
        df (pd.DataFrame): The DataFrame containing food data.

    Returns:
        list: A list of food names meeting the specified level criteria.

    Raises:
        ValueError: If selected_nutrition or selected_level is not provided,
                    or if selected_level is invalid.
    """
    if not selected_nutrition or not selected_level:
        raise ValueError("Please select both a nutrition content and a level")

    max_value = df[selected_nutrition].max()

    low_threshold = max_value * 0.33
    mid_threshold_low = max_value * 0.43
    mid_threshold_high = max_value * 0.66
    high_threshold = max_value * 0.76

    if selected_level == 'low':
        filtered_foods = df[df[selected_nutrition] < low_threshold]['food'].tolist()
    elif selected_level == 'mid':
        filtered_foods = df[
            (df[selected_nutrition] > mid_threshold_low) & (df[selected_nutrition] <= mid_threshold_high)
        ]['food'].tolist()
    elif selected_level == 'high':
        filtered_foods = df[df[selected_nutrition] > high_threshold]['food'].tolist()
    else:
        raise ValueError("Invalid level selected")

    return filtered_foods if filtered_foods else []


def export_as_csv(nutrient_data, path):
    """
    Exports the nutritional data to a CSV file at the specified path.

    Args:
        nutrient_data (list): A list of dictionaries containing nutritional data.
        path (str): The path to the output CSV file.
    """
    df = pd.DataFrame(nutrient_data)
    df.to_csv(path, index=False)


def show_password(current_password, checkbox_state):
    """
    Displays the password based on the checkbox state.

    Args:
        current_password (str): The current password.
        checkbox_state (bool): True if the checkbox is checked, False otherwise.

    Returns:
        str: The current password if the checkbox is checked,
             otherwise a string of asterisks with the same length as the password.
    """
    if checkbox_state:
        return current_password
    else:
        return '*' * len(current_password)