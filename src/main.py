from parameters import get_all_parameters
from locations import get_all_location_data
from location_details import get_location_details_for_multiple_locations
from load_data import load_data_to_bigquery_clear_table

parameters = get_all_parameters()
load_data_to_bigquery_clear_table('raw_airquality','raw_parameters', parameters)

ids_list, locations_list = get_all_location_data()
load_data_to_bigquery_clear_table('raw_airquality','raw_locations', locations_list)

location_details = get_location_details_for_multiple_locations(ids_list)
load_data_to_bigquery_clear_table('raw_airquality','raw_location_details', location_details)
