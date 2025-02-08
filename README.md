# API-INTEGRATION-AND-DATA-VISUALIZATION

COMPANY: CODTECH IT SOLUTIONS

NAME: P SOORYA SHENOY

INTERN ID: CT12ONS

DOMAIN: PYTHON PROGRAMMING

DURATION: 8 WEEKS

MENTOR: NEELA SANTHOSH


DESCRIPTION:
This Python script is designed for data analysts, developers, and hobbyists interested in visualizing weather data trends using real-time information from the OpenWeatherMap API. It is suitable for execution on any platform that supports Python (Windows, macOS, or Linux). The script can be used in environmental monitoring systems, research projects, or educational purposes to demonstrate API integration and data visualization techniques.

Key Features:
Integration with a public API (OpenWeatherMap) to fetch real-time weather data.
Data extraction and transformation into a structured format using pandas.
Visualization of weather trends using both Matplotlib and Seaborn.
Ability to track temperature and humidity changes over time.

Working of the Code:
1. API Integration:
The script uses the OpenWeatherMap API to retrieve weather forecast data for a specified city (default: London). The API request includes parameters such as the city name, API key, and units for measurement (metric).
2. Data Fetching and Parsing:
The response from the API is in JSON format. The script extracts relevant data such as date, temperature, and humidity from the response.
3. Data Storage:
The extracted data is organized into a pandas DataFrame, which facilitates data manipulation and analysis.
4. Data Visualization:
Matplotlib: A simple line plot is created to visualize the temperature trend over time.
Seaborn: A more sophisticated visualization overlays temperature and humidity trends on a single plot for better comparison.
5. Output:
The script displays two plots: one showing only temperature trends and another comparing temperature and humidity trends. These visualizations provide insights into weather patterns over the forecast period.

Applicability:
Environmental Monitoring: The script can be part of a weather monitoring system to track and predict weather changes.
Data Analytics Projects: Useful for students and professionals to learn about data processing, API integration, and visualization techniques.
Smart City Applications: Can be integrated into larger systems for weather-based decision-making (e.g., traffic control or public safety alerts).
Educational Demonstrations: Suitable for teaching Python programming concepts, data analysis, and visualization libraries.

 How to Use:
1. Install the required libraries by running:
      pip install matplotlib seaborn pandas requests
2. Replace the placeholder `YOUR_API_KEY` with your actual OpenWeatherMap API key.
3. Run the script in any Python environment (e.g., VSCode, Jupyter Notebook, or terminal).

This script provides a practical example of API integration and data visualization. By using powerful libraries such as Matplotlib and Seaborn, users can easily gain insights from weather data and create visually appealing plots.

![Image](https://github.com/user-attachments/assets/b63221c7-c2b4-4110-a64c-0b5b97ad8e29)
![Image](https://github.com/user-attachments/assets/c9cde413-83cc-4eef-8703-37b9ec0f7ed4)


