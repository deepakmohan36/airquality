{{ config(materialized="table") }}
with
    parameters as (select * from {{ source("raw_airquality", "raw_parameters") }})

select
    id as parameter_id,
    name as parameter_name,
    displayName as display_name,
    description,
    units,
from parameters
