from locations import get_all_location_data
from air_quality_data import get_airquality_data
from load_data import load_data_to_bigquery_clear_table


ids_list, locations_list = get_all_location_data()
load_data_to_bigquery_clear_table('raw_airquality','raw_locations', locations_list)

air_quality_data = get_airquality_data(ids_list)
load_data_to_bigquery_clear_table('raw_airquality','raw_airquality', air_quality_data)
