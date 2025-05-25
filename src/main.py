

from air_quality_data import get_airquality_data
from load_data import load_data_to_bigquery_clear_table

air_quality_data = get_airquality_data('8118')
load_data_to_bigquery_clear_table('raw_airquality','raw_airquality', air_quality_data)
