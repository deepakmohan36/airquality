{{ config(materialized="table") }}

with locations as (
    select
        id,
        coordinates.longitude as longitude,
        coordinates.latitude as latitude,
        sensors,
        owner,
        country,
        name,
        instruments,
        datetimeLast
    from {{ source("raw_airquality", "raw_locations") }}
),

unnested_sensors as (
    select
        l.id as location_id,
        l.longitude,
        l.latitude,
        s.id as sensor_id
    from locations l,
    unnest(l.sensors) as s
), 

unnested_instruments as (
    select
        l.id as location_id,
        i.id as instrument_id
    from locations l,
    unnest(l.instruments) as i
),

combined as (
    select
        s.location_id,
        s.longitude,
        s.latitude,
        s.sensor_id,
        i.instrument_id
    from unnested_sensors s
    left join unnested_instruments i
    on s.location_id = i.location_id
)

select
    location_id,
    longitude,
    latitude,
    array_agg(distinct instrument_id order by instrument_id) as instrument_ids,
    array_agg(distinct sensor_id order by sensor_id) as sensor_ids
from combined
group by location_id
