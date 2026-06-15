import streamlit as st
from db import fetch_data
import pandas as pd
import plotly.express as px

st.title('🚥Traffic Violations Insight System ')

st.header(
    "📊 Overview"
)
col1,col2,=st.columns(2)

q1 = """select count(*) as count from traffic_violations; """
df = fetch_data(q1)
col1.metric("Total Violations❌",df['count'][0])

q2 = """select count(*) as count from traffic_violations where Accident = true; """
df = fetch_data(q2)
col2.metric("Total Violations involving Accidents🚑",df['count'][0])

col3,col4 = st.columns(2)

with col3:
    st.write("High Risk Zones🚩")
    q3 = """select Location_clean as 'High Risk Zones' from traffic_violations where Fatal = true limit 5; """
    df = fetch_data(q3)
    st.dataframe(df)
with col4:
    st.write("Most Frequently Cited Vehicle Makes🚗")
    q4 = """select Make, count(*)  as count from  traffic_violations group by Make order by count desc limit 5"""
    df = fetch_data(q4)
    st.dataframe(df['Make'])


st.title("Filter By 🔍 ")
col1, col2 = st.columns(2)
with col1:
    location = st.selectbox(
        "Location",
        ["All"]+
        fetch_data(
        """
        SELECT DISTINCT Location_clean
        FROM traffic_violations
        WHERE Location_clean IS NOT NULL
        ORDER BY Location_clean;"""
        )['Location_clean'].tolist()
    )

    Vehicletype = st.selectbox(
        "Vehicle Type",
        ["All"]+
        fetch_data("""
        select distinct VehicleCategory
        from traffic_violations
        ORDER BY VehicleCategory;
            """)['VehicleCategory'].tolist()
    )

    race = st.selectbox(
        "Race",
        ["All"]+
        fetch_data("""
        select distinct Race
        from traffic_violations
        """)['Race'].tolist()
    )

with col2:
    date = date_range = st.date_input(
        "Date Range",
        value=[]
    )

    gender = st.selectbox(
    "Gender",
    ["All"] +
    fetch_data(
        """
        SELECT DISTINCT Gender
        FROM traffic_violations
        ORDER BY Gender
        """
    )['Gender'].tolist()
    )

    violation_category = st.selectbox(
    "Violation Category",
    ["All"] +
    fetch_data(
        """
        SELECT DISTINCT Violation_category
        FROM traffic_violations
        ORDER BY Violation_category
        """
    )['Violation_category'].tolist()
)

query7 = """
SELECT *
FROM traffic_violations
WHERE 1=1
"""

params = []

if location != "All":

    query7 += """
    AND Location_clean = %s
    
    """

    params.append(location)

if gender != "All":

    query7 += """
    AND Gender = %s
    
    """

    params.append(gender)

if race != "All":

    query7 += """
    AND Race = %s
    
    """

    params.append(race)

if Vehicletype != "All":

    query7 += """
    AND VehicleCategory = %s
    
    """

    params.append(Vehicletype)

if violation_category != "All":

    query7 += """
    AND Violation_category = %s
    
    """

    params.append(violation_category)


if len(date_range) == 2:

    start_date, end_date = date_range

    query7 += """
    AND DATE(Stop_dateTime)
    BETWEEN %s AND %s
    
    """

    params.extend([start_date, end_date])


filtered_df = fetch_data(
    query7,
    params
)

st.subheader("Filtered Traffic Violations")

st.write(f"Records Found: {len(filtered_df):,}")

st.dataframe(
    filtered_df.head(20),
    use_container_width=True
)

st.title("Insights🚥")
col1,col2,=st.columns(2)



with col1:
    query1 = """select Violation_category , count(Violation_category) as count
                from traffic_violations
                group by Violation_category
                order by count desc
                limit 4;"""
    df = fetch_data(query1)
    
    fig1 = px.bar(
        df,
        x='count',
        y='Violation_category',
        orientation='h',
        title='Most Common Violations',
        text='count'
    )

    fig1.update_layout(
        xaxis_title='Number of Violations',
        yaxis_title='Violation Category',
        yaxis={'categoryorder':'total ascending'}
    )

    st.plotly_chart(fig1, use_container_width=True)

    st.info("""
    Speeding is the most frequent traffic violation, followed by license and registration-related offenses.
    
    """)

    

with col2:
    st.markdown("### Areas with Most violations: ")
    query2 = """select Location_clean as Area, count(*) as Incident_count
        from traffic_violations
        group by Location_clean
        order by Incident_count desc
        limit 10;"""
    df = fetch_data(query2)
    st.dataframe(df['Area'])
    st.info("""
    List of areas with the most violations.
    
    """)
    
col3, col4 = st.columns(2)
with col3:
   
    query3 = """SELECT
                Gender,
                `Violation Type`,
                COUNT(*) AS violation_count
            FROM traffic_violations
            GROUP BY Gender, `Violation Type`
            ORDER BY Gender, violation_count DESC;"""
    df = fetch_data(query3)
    
    fig = px.bar(
    df,
    x='Violation Type',
    y='violation_count',
    color='Gender',
    barmode='group',
    title='Violation Type by Gender'
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )
    st.info("""
    According to the chart, male drivers account for majority of violations. Citations are observed to be the most common violation type.
    """)

with col4:
    st.markdown("### Type of vehicles Most often involved in Violations")
    query5 = """select VehicleCategory as 'Type of Vehicle', count(*) as 'Violation Count'
        from traffic_violations
        group by VehicleCategory
        order by 'Violation Count' desc
        limit 10;"""
    df = fetch_data(query5)
    st.dataframe(df)
    st.info("""
    Automobiles account for the majority of traffic violations. Light duty trucks come second in the list although the violations are relative less when compared to automobiles.
    """)


col1,col2= st.columns(2)

with col1:
    q41 = """SELECT
            TimeOfDay,
            COUNT(*) AS violation_count
        FROM traffic_violations
        GROUP BY TimeOfDay
        ORDER BY violation_count DESC;"""
    df = fetch_data(q41)
    

    fig41 = px.bar(
    df,
    x='TimeOfDay',
    y='violation_count',
    title='Violations by Time of Day',
    text='violation_count'
    )

    fig41.update_traces(textposition='outside')

    fig41.update_layout(
        xaxis_title='Time of Day',
        yaxis_title='Violation Count'
    )

    st.plotly_chart(fig41, use_container_width=True)

    st.info("""
    Night and Morning times of the day is seen to have more violations. And the violations seem to gradually reduce through the day with the evenings recording the least number of violations followed by afternoons.
    """)

with col2:

    q42="""SELECT
        Weekday,
        COUNT(*) AS violation_count
    FROM traffic_violations
    GROUP BY Weekday
    ORDER BY FIELD(
        Weekday,
        'Monday',
        'Tuesday',
        'Wednesday',
        'Thursday',
        'Friday',
        'Saturday',
        'Sunday'
    );"""

    df = fetch_data(q42)
    
    fig42 = px.bar(
    df,
    x='Weekday',
    y='violation_count',
    title='Violations by Weekday',
    text='violation_count'
    )

    fig42.update_traces(textposition='outside')

    fig42.update_layout(
        xaxis_title='Weekday',
        yaxis_title='Violation Count'
    )

    st.plotly_chart(fig42, use_container_width=True)

    st.info("""
    Trafiic violations are more on weekdays when compared to weekends.Tuesdays have recorded the highest number of violations followed by wednesdays, thursdays and fridays.
    """)

q43="""SELECT
    Month,
    COUNT(*) AS violation_count
FROM traffic_violations
GROUP BY Month
ORDER BY FIELD(
    Month,
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December'
);"""

df = fetch_data(q43)

fig43 = px.line(
    df,
    x='Month',
    y='violation_count',
    markers=True,
    title='Monthly Violation Trend'
)

fig43.update_layout(
    xaxis_title='Month',
    yaxis_title='Violation Count'
)

st.plotly_chart(fig43, use_container_width=True)

st.info("""
    May and March seems to have the most number of violations. A decline in the number of violations is observed from the month of july.
""")