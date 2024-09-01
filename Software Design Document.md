# Software Design Document

## Project Name: Desktop Application Project
## Group Number: 48

## Team members

| Student Number | Name      | 
|----------------|-----------|
| s5290341       | Zhongyue Qiu |
| s5226106       | Lowry Zhao | 
| s5261308       | Jiaxin Lin | 


<div style="page-break-after: always;"></div>



# Table of Contents

<!-- TOC -->
* [Table of Contents](#table-of-contents)
  * [1. System Vision](#1-system-vision)
    * [1.1 Problem Background](#11-problem-background)
    * [1.2 System capabilities/overview](#12-system-capabilitiesoverview)
    * [1.3	Potential Benefits](#13potential-benefits)
  * [2. Requirements](#2-requirements)
    * [2.1 User Requirements](#21-user-requirements)
    * [2.2	Software Requirements](#22software-requirements)
    * [2.3 Use Case Diagrams](#23-use-case-diagrams)
    * [2.4 Use Cases](#24-use-cases)
  * [3.	Software Design and System Components](#3-software-design-and-system-components-)
    * [3.1	Software Design](#31software-design)
    * [3.2	System Components](#32system-components)
      * [3.2.1 Functions](#321-functions)
      * [3.2.2 Data Structures / Data Sources](#322-data-structures--data-sources)
      * [3.2.3 Detailed Design](#323-detailed-design)
  * [4. User Interface Design](#4-user-interface-design)
    * [4.1 Structural Design](#41-structural-design)
    * [4.2	Visual Design](#42visual-design)
<!-- TOC -->


<div style="page-break-after: always;"></div>



## 1. System Vision

### 1.1 Problem Background

- Problem Identification:
  With the continuous development of living standards, people's demand for health and nutrition is increasing, but few   
  people go back to consult professional nutrition analyst and doctors. The development of this software is aimed at 
  helping people search and view specific information about the nutrients contained in various foods more easily and 
  quickly.
  
- Dataset:
  The dataset used by this software is Nutritional-Food-Database provided by the course, which contains detailed 
  nutritional information of various foods. These data include the names of various foods, as well as the specific values 
  of the nutrients provided, such as calories, fat, protein, and vitamins.
 
- Data Input/Output:
  
  Input:
  - Users can enter the name of a food in the search bar, click to select a specific food, or choose a specific range of 
    nutrients.
 
  Output:
  - By searching for the name of a food, specific data on all nutrients contained in that food will be displayed.
  - By selecting a single food, pie charts and bar charts will be displayed.
  - By screening the specifc range of nutrients, foods that meet the standards will be displayed.
 
- Target Users:
  - Nutritionist: Analyze and recommend foods based on different dietary needs.
  - Healthcare Professionals: Assess and provide recommendations based on health status.
  - The General Public: Improving health.
  

### 1.2 System capabilities/overview

- System Functionality:
  - Search and filtering: Users can search for food names and filter based on specific nutritional standards.
  - Data analysis and visualization: The system will allow users to analyze the nutritional composition of various foods       and visualize this data in a meaningful way.
  - Customization: Users can set their own unique nutrition plan and share it.

- Features and Functionalities:
  - Food search: Users can search for food by name and view detailed nutritional information.
  - Nutritional Analysis: For any selected food, users can view a detailed breakdown of its nutritional components through 
    pie charts and bar charts.
  - Nutritional Range Filter: Users can filter food by specifying the range of any nutritional indicator.
  - Nutrient Level Filter: Users can filter food based on pre-defined key nutrient levels (low, medium, high).
  - Nutrition Plan Development and Sharing: Users can create different nutrition plans and share them. Professionals can 
    use this feature to assist some confused users and provide them with a template.


### 1.3	Benefit Analysis

  - Time Saving: It saves users the time they need to collect information on their own, providing convenience not only for 
    ordinary users, but also for professionals and doctors.
  - Decision Making: By providing more accurate and professional data, users can analyze and make better decisions. Users 
    can also refer to plans shared by other users.
  - Health: By providing professional data to help users improve their health status and reduce the risk of illness.


## 2. Requirements

### 2.1 User Requirements

Detail how users are expected to interact with or use the program. What functionalities must the system provide from the end-user perspective? This can include both narrative descriptions and a listing of user needs.

Note: Since no specific client or user is assigned, you may create a fictional user. Who do you envision using your software?

### 2.2	Software Requirements
Define the functionality the software will provide. This section should list requirements formally, often using the word "shall" to describe functionalities.

Example Functional Requirements:  
- R1.1 The program shall accept multiple file names as arguments from the command line.  
- R1.2 Each file name can be a simple file name or include the full path of the file with one or more levels.  

- etc …

### 2.3 Use Case Diagram

![Use Case Diagram](./UCD.png)

### 2.4 Use Cases

| Use Case ID    | UC-01      |
|----------------|------------|
| Use Case Name  |Food Search |
| Actors         |Target Users(Nutritionist, Healthcare Professionals, The General Public)|
| Description    |Users can search for food by name and view detailed nutritional information.|
| Flow of Events |1.User enter the desktop application.|
|                |2.User navigate to the search icon.|
|                |3.User enter the name of food they want to search.|
|                |4.System retrieve and display matching results from the database.|
|                |5.User view nutrtional information.|
| Alternate Flow |1.If there are no matching results, system inform the user and provide option for user to refine the search items.| 
|                |2.If the system has technical issues during the search process, the system notifies the user to try again later or contact IT support.|

| Use Case ID    | UC-02                  |
|----------------|------------------------|
| Use Case Name  |Nutritional Range Filter|
| Actors         |Target Users(Nutritionist, Healthcare Professionals, The General Public)|
| Description    |Users can filter food by specifying the range of any nutritional indicator.|
| Flow of Events |1.User access the range filtering icon in the desktop application.|
|                |2.User select the range of nutritional indicator.|
|                |3.The system retrieve and display the list of food items from the database.|
|                |4.User select a specifc food item and view the detailed nutritional information.|
| Alternate Flow |1.If there are no matching nutritional range, the system inform the user and provide options for user to refine the range or choose different nutritional indicator.| 
|                |2.If the system has technical issues during the range filter process, the system notify the user to try again later or contact IT support.|

| Use Case ID    | UC-03               |
|----------------|---------------------|
| Use Case Name  |Nutrient Level Filter|
| Actors         |Target Users(Nutritionist, Healthcare Professionals, The General Public)|
| Description    |Users can filter food based on pre-defined key nutrient levels (low, medium, high).|
| Flow of Events | xxxx |
| Alternate Flow | xxxx |

| Use Case ID    | UC-04              |
|----------------|--------------------|
| Use Case Name  |Nutritional Analysis|
| Actors         |Target Users(Nutritionist, Healthcare Professionals, The General Public)|
| Description    |For any selected food, users can view a detailed breakdown of its nutritional components through pie charts and bar charts.|
| Flow of Events | xxxx |
| Alternate Flow | xxxx |

| Use Case ID    | UC-05                              |
|----------------|------------------------------------|
| Use Case Name  |Nutrition Plan Development & Sharing|
| Actors         |Target Users(Nutritionist, Healthcare Professionals, The General Public)|
| Description    |Users can create different nutritions plans and share them. Professionals can use this feature to assist some confused users and provide them with a template.|
| Flow of Events | xxxx |
| Alternate Flow | xxxx |



## 3.	Software Design and System Components 

### 3.1	Software Design
Include a flowchart that illustrates how your software will operate.

Example:  
![Software Design](./software_design_flowchart.png)

### 3.2	System Components

#### 3.2.1 Functions
List all key functions within the software. For each function, provide:
- Description: Brief explanation of the function’s purpose.
- Input Parameters: List parameters, their data types, and their use.
- Return Value: Describe what the function returns.
- Side Effects: Note any side effects, such as changes to global variables or data passed by reference.

#### 3.2.2 Data Structures / Data Sources
List all data structures or sources used in the software. For each, provide:

- Type: Type of data structure (e.g., list, set, dictionary).
- Usage: Describe where and how it is used.
- Functions: List functions that utilize this structure.

#### 3.2.3 Detailed Design
Provide pseudocode or flowcharts for all functions listed in Section 3.2.1 that operate on data structures. For instance, include pseudocode or a flowchart for a custom searching function.


## 4. User Interface Design

### 4.1 Structural Design
Present a structural design, a hierarchy chart, showing the overall interface’s structure. Address:

- Structure: How will the software be structured?
- Information Grouping: How will information be organized?
- Navigation: How will users navigate through the software?
- Design Choices: Explain why these design choices were made.

![Structural Design](./Structural_Design.png)

### 4.2	Visual Design
Include all wireframes or mock-ups of the interface. Provide a discussion, explanation, and justification for your design choices. Hand-drawn wireframes are acceptable.

- Interface Components: Clearly label all components.
- Screens/Menus: Provide wireframes for different screens, menus, and options.
- Design Details: Focus on the layout and size of components; color and graphics are not required. 

Example:  
![Visual Design](./visual_design.png)



