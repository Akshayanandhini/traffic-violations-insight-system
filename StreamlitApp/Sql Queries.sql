# Query 1
select Violation_category , count(Violation_category) as count
from traffic_violations
group by Violation_category
order by count desc
limit 4;

# query2
select Location_clean, count(*) as Incident_count
from traffic_violations
group by Location_clean
order by Incident_count desc
limit 10;

# query5
select VehicleCategory as 'Type of Vehicle', count(*) as 'Violation Count'
from traffic_violations
group by VehicleCategory
order by 'Violation Count' desc
limit 10;

# query6:
select count(*) as 'Count of Violations'
from traffic_violations
where Accident  = true or 'Personal Injury' = true or 'Property Damage' = true;

