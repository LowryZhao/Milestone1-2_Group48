import wx
import wx.xrc
import wx.adv
import wx.grid
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg

from template_frame_1 import MyFrame1 as MyFrame1
from template_frame_2 import MyFrame2 as MyFrame2
from template_frame_3 import MyFrame3 as MyFrame3
from template_frame_4 import MyFrame4 as MyFrame4
from template_frame_5 import MyFrame5 as MyFrame5
from template_frame_6 import MyFrame6 as MyFrame6
from template_frame_7 import MyFrame7 as MyFrame7
from template_frame_8 import MyFrame8 as MyFrame8
from template_frame_9 import MyFrame9 as MyFrame9
from template_frame_10 import MyFrame10 as MyFrame10
from nutrition_function import on_search, nutrition_breakdown, nutrition_range_filter, nutrition_level_filter, export_as_csv, show_password

matplotlib.use('WXAgg')

class MyApp(wx.App):
    def OnInit(self):
        self.df = pd.read_csv('Food_Nutrition_Dataset.csv')
        self.startPage = MyFrame1(None)
        self.startPage.m_checkBox2.Bind(wx.EVT_CHECKBOX, lambda evt: self.show_password(self.startPage))
        self.startPage.m_button3.Bind(wx.EVT_BUTTON, lambda evt: self.function_loop(self.startPage, MyFrame2))
        self.get_searched = None
        self.startPage.Show()
        return True

    def function_loop(self, current_frame, next_frame_class):
        current_frame.Hide()
        next_frame = next_frame_class(None)


        # Frame 2 Buttons
        if next_frame_class == MyFrame2:
            # Food Search
            next_frame.m_button6.Bind(wx.EVT_BUTTON, lambda evt: self.function_loop(next_frame, MyFrame3))

            # Nutrition Filter
            next_frame.m_button7.Bind(wx.EVT_BUTTON, lambda evt: self.function_loop(next_frame, MyFrame5))

            # Nutrition Plan
            next_frame.m_button8.Bind(wx.EVT_BUTTON, lambda evt: self.function_loop(next_frame, MyFrame7))

        # Frame 3 Buttons
        if next_frame_class == MyFrame3:
            # Next Button
            next_frame.m_button32.Bind(wx.EVT_BUTTON, lambda evt: self.function_loop(next_frame, MyFrame4))

            # Food search function
            next_frame.m_button11.Bind(wx.EVT_BUTTON, lambda evt: self.on_search(next_frame))

        # Frame 4 Buttons
        if next_frame_class == MyFrame4:
            # Display searched food
            next_frame.m_comboBox2.SetLabel(self.get_searched['food'])

            # Return Button
            next_frame.m_button40.Bind(wx.EVT_BUTTON, lambda evt: self.function_loop(next_frame, MyFrame2))

            # Display Button
            next_frame.m_button14.Bind(wx.EVT_BUTTON, lambda evt: self.nutrition_breakdown(next_frame))

            # Export Button
            next_frame.m_button43.Bind(wx.EVT_BUTTON, lambda evt: self.export_as_csv(next_frame))

        # Frame 5 Buttons
        if next_frame_class == MyFrame5:
            # Next Button
            next_frame.m_button34.Bind(wx.EVT_BUTTON, lambda evt: self.function_loop(next_frame, MyFrame6))

            # Populate m_comboBox4 with available nutrition columns from the DataFrame (self.df)
            nutrition_columns = [
                'Caloric Value', 'Fat', 'Saturated Fats', 'Monounsaturated Fats',
                'Polyunsaturated Fats', 'Carbohydrates', 'Sugars', 'Protein',
                'Dietary Fiber', 'Cholesterol', 'Sodium', 'Water', 'Vitamin A',
                'Vitamin B1', 'Vitamin B11', 'Vitamin B12', 'Vitamin B2',
                'Vitamin B3', 'Vitamin B5', 'Vitamin B6', 'Vitamin C', 'Vitamin D',
                'Vitamin E', 'Vitamin K', 'Calcium', 'Copper', 'Iron', 'Magnesium',
                'Manganese', 'Phosphorus', 'Potassium', 'Selenium', 'Zinc', 'Nutrition Density'
            ]

            # Populate the comboBox4 with nutrition columns from dataframe
            next_frame.m_comboBox4.Clear()
            next_frame.m_comboBox4.AppendItems(nutrition_columns)

            # Range Search Button
            next_frame.m_button13.Bind(wx.EVT_BUTTON, lambda evt: self.nutrition_range_filter(next_frame))

        # Frame 6 Buttons
        if next_frame_class == MyFrame6:
            # Return Button
            next_frame.m_button38.Bind(wx.EVT_BUTTON, lambda evt: self.function_loop(next_frame, MyFrame2))

            # Populate m_comboBox2 with levels (low, mid, high)
            level_options = ['low', 'mid', 'high']
            next_frame.m_comboBox2.Clear()
            next_frame.m_comboBox2.AppendItems(level_options)

            # Populate m_comboBox3 with nutrition options
            nutrition_options = ['Fat', 'Protein', 'Carbohydrates', 'Sugars', 'Nutrition Density']
            next_frame.m_comboBox3.Clear()
            next_frame.m_comboBox3.AppendItems(nutrition_options)

            # Level Search Button
            next_frame.m_button32.Bind(wx.EVT_BUTTON, lambda evt: self.nutrition_level_filter(next_frame))

        # Frame 7 Buttons
        if next_frame_class == MyFrame7:
            # Create Nutrition Plan Button
            next_frame.m_button19.Bind(wx.EVT_BUTTON, lambda evt: self.function_loop(next_frame, MyFrame8))

        # Frame 8 Buttons
        if next_frame_class == MyFrame8:
            # Next Button
            next_frame.m_button42.Bind(wx.EVT_BUTTON, lambda evt: self.function_loop(next_frame, MyFrame9))
            # Return Button
            next_frame.m_button41.Bind(wx.EVT_BUTTON, lambda evt: self.function_loop(next_frame, MyFrame2))

        # Frame 9 Buttons
        if next_frame_class == MyFrame9:
            # Share Button
            next_frame.m_button25.Bind(wx.EVT_BUTTON, lambda evt: self.function_loop(next_frame, MyFrame10))

        next_frame.Show()
        current_frame.Hide()

    # Required Function 1: Food Search (Frame3)
    def on_search(self, current_frame):
        food_name = current_frame.m_searchCtrl1.GetValue()
        current_frame.m_listBox1.Clear()
        result = self.df[self.df['food'].str.contains(food_name, case=False, na=False)]

        if not result.empty:
            current_frame.selected_food_data = result.iloc[0]
            self.get_searched = result.iloc[0]
            food_info = [
                f"Food: {current_frame.selected_food_data['food']}",
                f"Caloric Value: {current_frame.selected_food_data['Caloric Value']} kcal",
                f"Fat: {current_frame.selected_food_data['Fat']} g",
                f"Saturated Fats: {current_frame.selected_food_data['Saturated Fats']} g",
                f"Monounsaturated Fats: {current_frame.selected_food_data['Monounsaturated Fats']} g",
                f"Polyunsaturated Fats: {current_frame.selected_food_data['Polyunsaturated Fats']} g",
                f"Carbohydrates: {current_frame.selected_food_data['Carbohydrates']} g",
                f"Sugars: {current_frame.selected_food_data['Sugars']} g",
                f"Protein: {current_frame.selected_food_data['Protein']} g",
                f"Dietary Fiber: {current_frame.selected_food_data['Dietary Fiber']} g",
                f"Cholesterol: {current_frame.selected_food_data['Cholesterol']} mg",
                f"Sodium: {current_frame.selected_food_data['Sodium']} g",
                f"Water: {current_frame.selected_food_data['Water']} g",
                f"Vitamin A: {current_frame.selected_food_data['Vitamin A']} mg",
                f"Vitamin B1: {current_frame.selected_food_data['Vitamin B1']} mg",
                f"Vitamin B11: {current_frame.selected_food_data['Vitamin B11']} mg",
                f"Vitamin B12: {current_frame.selected_food_data['Vitamin B12']} mg",
                f"Vitamin B2: {current_frame.selected_food_data['Vitamin B2']} mg",
                f"Vitamin B3: {current_frame.selected_food_data['Vitamin B3']} mg",
                f"Vitamin B5: {current_frame.selected_food_data['Vitamin B5']} mg",
                f"Vitamin B6: {current_frame.selected_food_data['Vitamin B6']} mg",
                f"Vitamin C: {current_frame.selected_food_data['Vitamin C']} mg",
                f"Vitamin D: {current_frame.selected_food_data['Vitamin D']} mg",
                f"Vitamin E: {current_frame.selected_food_data['Vitamin E']} mg",
                f"Vitamin K: {current_frame.selected_food_data['Vitamin K']} mg",
                f"Calcium: {current_frame.selected_food_data['Calcium']} mg",
                f"Copper: {current_frame.selected_food_data['Copper']} mg",
                f"Iron: {current_frame.selected_food_data['Iron']} mg",
                f"Magnesium: {current_frame.selected_food_data['Magnesium']} mg",
                f"Manganese: {current_frame.selected_food_data['Manganese']} mg",
                f"Phosphorus: {current_frame.selected_food_data['Phosphorus']} mg",
                f"Potassium: {current_frame.selected_food_data['Potassium']} mg",
                f"Selenium: {current_frame.selected_food_data['Selenium']} mg",
                f"Zinc: {current_frame.selected_food_data['Zinc']} mg",
                f"Nutrition Density: {current_frame.selected_food_data['Nutrition Density']}"
            ]

            for _ in food_info:
                current_frame.m_listBox1.Append(_)
        else:
            current_frame.m_listBox1.Append("No Food Found!")

    # Required Function 2: Nutrition Breakdown (Frame4)
    def nutrition_breakdown(self, current_frame):
        if self.get_searched is None:
            wx.MessageBox("No food selected for breakdown!", "Error", wx.OK | wx.ICON_ERROR)
            return

        nutrients = {
            "Fat": self.get_searched['Fat'],
            "Protein": self.get_searched['Protein'],
            "Carbohydrates": self.get_searched['Carbohydrates'],
            "Fiber": self.get_searched['Dietary Fiber'],
            "Sugar": self.get_searched['Sugars']
        }

        # Clear any previous charts from the panels
        self.clear_panel(current_frame.m_panel4)
        self.clear_panel(current_frame.m_panel5)

        # Pie Chart
        self.draw_pie_chart(nutrients, current_frame.m_panel4)

        # Bar Chart
        self.draw_bar_graph(nutrients, current_frame.m_panel5)

    def draw_pie_chart(self, nutrients, panel4):
        figure = plt.Figure(figsize=(4, 4))
        ax = figure.add_subplot(111)
        labels = list(nutrients.keys())
        values = list(nutrients.values())
        ax.pie(values, labels=labels, autopct='%1.1f%%', startangle=90)
        ax.set_title("Nutrient Breakdown (Pie)")

        canvas = FigureCanvasWxAgg(panel4, -1, figure)
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(canvas, 1, wx.EXPAND)
        panel4.SetSizer(sizer)
        panel4.Layout()

    def draw_bar_graph(self, nutrients, panel5):
        figure = plt.Figure(figsize=(4, 4))
        ax = figure.add_subplot(111)
        labels = list(nutrients.keys())
        values = list(nutrients.values())
        ax.bar(labels, values, color='lightblue')
        ax.set_title("Nutrient Breakdown (Bar)")

        canvas = FigureCanvasWxAgg(panel5, -1, figure)
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(canvas, 1, wx.EXPAND)
        panel5.SetSizer(sizer)
        panel5.Layout()

    def clear_panel(self, panel):
        for child in panel.GetChildren():
            child.Destroy()

    # Required Function 3: Nutrition Range Filter (Frame5)
    def populate_nutrition_types(self):
        app = wx.GetApp()

        # Skip the first column if it contains food names
        nutrition_columns = app.df.columns[1:].tolist()
        self.m_comboBox4.AppendItems(nutrition_columns)

    def nutrition_range_filter(self, current_frame):
        selected_nutrition = current_frame.m_comboBox4.GetValue()

        min_val = current_frame.m_textCtrl5.GetValue()
        max_val = current_frame.m_textCtrl12.GetValue()

        try:
            min_value = float(min_val)
            max_value = float(max_val)

            if min_value >= max_value:
                wx.MessageBox("Minimum value must be less than maximum value.", "Input Error", wx.OK | wx.ICON_ERROR)
                return
        except ValueError:
            wx.MessageBox("Please enter valid numeric values.", "Input Error", wx.OK | wx.ICON_ERROR)
            return

        # Use the DataFrame self.df loaded in MyApp
        if selected_nutrition not in self.df.columns:
            wx.MessageBox("Invalid nutrition type selected.", "Error", wx.OK | wx.ICON_ERROR)
            return

        filtered_foods = self.df[
            (self.df[selected_nutrition] >= min_value) &
            (self.df[selected_nutrition] <= max_value)
            ]['food'].tolist()

        # Display the filtered food list in the m_listBox2
        current_frame.m_listBox2.Clear()
        if filtered_foods:
            current_frame.m_listBox2.AppendItems(filtered_foods)
        else:
            wx.MessageBox("No foods found in the specified range.", "No Results", wx.OK | wx.ICON_INFORMATION)

    # Required Function 4: Nutrition Level Filter (Frame6)
    def nutrition_level_filter(self, current_frame):
        selected_nutrition = current_frame.m_comboBox3.GetValue()
        selected_level = current_frame.m_comboBox2.GetValue()

        if not selected_nutrition or not selected_level:
            wx.MessageBox("Please select both a nutrition content and a level.", "Input Error", wx.OK | wx.ICON_ERROR)
            return

        # Get the highest value for the selected nutrition content in the dataset
        max_value = self.df[selected_nutrition].max()

        # "low", "mid", "high" value
        low_threshold = max_value * 0.33
        mid_threshold_low = max_value * 0.33
        mid_threshold_high = max_value * 0.66
        high_threshold = max_value * 0.66

        if selected_level == 'low':
            filtered_foods = self.df[self.df[selected_nutrition] < low_threshold]['food'].tolist()
        elif selected_level == 'mid':
            filtered_foods = self.df[
                (self.df[selected_nutrition] >= mid_threshold_low) &
                (self.df[selected_nutrition] <= mid_threshold_high)
                ]['food'].tolist()
        elif selected_level == 'high':
            filtered_foods = self.df[self.df[selected_nutrition] > high_threshold]['food'].tolist()

        # Display the filtered results in the m_listBox4
        current_frame.m_listBox4.Clear()  # Assuming the ListBox is m_listBox3
        if filtered_foods:
            current_frame.m_listBox4.AppendItems(filtered_foods)
        else:
            wx.MessageBox("No foods found for the selected level.", "No Results", wx.OK | wx.ICON_INFORMATION)

    # Required Function 5: Export to .csv file (Frame4)
    def export_as_csv(self, event):
        if self.get_searched is None:
            wx.MessageBox("No data to save!", "Error", wx.OK | wx.ICON_ERROR)
            return

        save_dialog = wx.FileDialog(None, "Save CSV", wildcard="CSV files (*.csv)|*.csv",
                                    style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT)
        if save_dialog.ShowModal() == wx.ID_CANCEL:
            return  # User canceled

        path = save_dialog.GetPath()

        nutrients = {
            "Nutrient": ["Fat", "Protein", "Carbohydrates", "Fiber", "Sugar"],
            "Amount": [
                self.get_searched['Fat'],
                self.get_searched['Protein'],
                self.get_searched['Carbohydrates'],
                self.get_searched['Dietary Fiber'],
                self.get_searched['Sugars']
            ]
        }

        df = pd.DataFrame(nutrients)
        df.to_csv(path, index=False)
        wx.MessageBox(f"Data saved successfully at {path}", "Success", wx.OK | wx.ICON_INFORMATION)

    # Additional Function 1: Show Password (Frame1)
    def show_password(self, current_frame):
        if current_frame.m_textCtrl2 is not None:
            current_password = current_frame.m_textCtrl2.GetValue()

            pos = current_frame.m_textCtrl2.GetPosition()
            size = current_frame.m_textCtrl2.GetSize()

            if current_frame.m_checkBox2.IsChecked():
                current_frame.m_textCtrl2.Destroy()
                current_frame.m_textCtrl2 = wx.TextCtrl(current_frame, value=current_password, pos=pos, size=size,
                                                        style=wx.TE_PROCESS_ENTER)
            else:
                current_frame.m_textCtrl2.Destroy()
                current_frame.m_textCtrl2 = wx.TextCtrl(current_frame, value=current_password, pos=pos, size=size,
                                                        style=wx.TE_PASSWORD | wx.TE_PROCESS_ENTER)

            current_frame.Layout()
        else:
            wx.MessageBox("Password field is missing!", "Error", wx.OK | wx.ICON_ERROR)


if __name__ == "__main__":
    app = MyApp()
    app.MainLoop()
