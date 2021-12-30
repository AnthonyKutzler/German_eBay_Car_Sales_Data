Analyzing data from German eBay car sales

Found no correlation between any variables.


-371528 Rows total\
Null values in columns [vehicle_type, gearbox, model, fuel_type, unrepaired_damage]\
-Renamed columns from CamelCase to snake_case for uniformity
-renamed kilometer to 'odometer_km'

--Dropped columns\
-number_of_pictures as the value of 0 is on every row\
-seller - not many unique values
-offer_type - same as seller

--Columns to clean\
-registration_year -- contains values as low as 1000 and as high as 9999 removed(<1900 & >2016) \
-power_ps -- ~10% = 0\
-fuel_type -- ~10% = NaN\
-unrepaired_damage -- ~20% = NaN
-price -- min = 0  removed (price == 0)
