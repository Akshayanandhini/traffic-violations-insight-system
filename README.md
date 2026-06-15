# 🚔 Traffic Violations Insight System

A data analytics and visualization project built using **Python, MySQL, Streamlit, and Plotly** to analyze over **1 million traffic violation records** and uncover patterns related to violations, locations, demographics, vehicles, and accident-related incidents.

The project follows a complete data analytics workflow including **data cleaning, feature engineering, SQL analysis, exploratory data analysis (EDA), and dashboard development**.

---

# 📊 Dashboard Preview

## Dashboard Overview

<p align="center">
   <img src="images/P1.png" width="900">
</p>

The dashboard provides a high-level overview of:

* Total recorded violations
* Violations involving accidents
* High-risk locations
* Most frequently cited vehicle makes

---

## Interactive Filtering System

<p align="center">
   <img src="images/P2.png" width="900">
</p>

Users can dynamically filter violations by:

* Date Range
* Location
* Vehicle Type
* Gender
* Race
* Violation Category

This allows focused analysis of specific subsets of the traffic violation data.

---

## Time-Based Analysis

<p align="center">
   <img src="images/P3.png" width="900">
</p>

The dashboard visualizes violation trends across:

* Time of Day
* Weekday
* Month

helping identify peak violation periods and temporal patterns.

---

# 🎯 Project Objectives

The project was designed to answer the following questions:

* What are the most common traffic violations?
* Which locations have the highest concentration of violations?
* Do certain demographics correlate with specific violation types?
* How does violation frequency vary by time of day, weekday, or month?
* What types of vehicles are most frequently involved in violations?
* How often do violations involve accidents, injuries, or vehicle damage?

---

# 🧹 Data Cleaning & Feature Engineering

One of the most important parts of this project was transforming a raw traffic violation dataset into an analysis-ready dataset.

### Major Cleaning Tasks

* Removed unnecessary columns that were not required for analysis.
* Standardized categorical values and text fields.
* Cleaned location information and created a normalized `Location_clean` column.
* Parsed date and time fields into a proper datetime format.
* Created new temporal features:

  * Month
  * Weekday
  * Hour
  * TimeOfDay
* Converted boolean fields into appropriate data types.
* Categorized violation charges into broader `Violation_category` groups.
* Categorized vehicle types into simplified `VehicleCategory` values.
* Categorized arrest types into meaningful `ArrestTypeCategory` groups.
* Validated geolocation information and removed redundant fields.
* Handled missing values using rule-based imputation where appropriate.

### Key Learning

A major takeaway from this project was that **data cleaning often requires domain-specific rules rather than generic missing-value techniques**. Several columns required custom mappings, categorization logic, and business-driven decisions before meaningful analysis could be performed.

---
# 🛠 Tech Stack

### Programming & Data Processing

* Python
* Pandas
* NumPy

### Database

* MySQL

### Data Visualization

* Plotly Express
* Streamlit

### Development Tools

* VS Code
* Git
* GitHub

---

# 🗄 Database Integration

The cleaned dataset was loaded into a MySQL database using batch insertion techniques.

### Database Features

* Batch inserts for large datasets
* SQL-based aggregations
* Dynamic filtering
* Optimized analytical queries
* Streamlit-to-MySQL integration


