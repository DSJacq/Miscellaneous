WITH date_axis as (
  SELECT dates
FROM
  UNNEST(generate_date_array("2023-06-20","2023-06-22")) as dates
)

SELECT
  dates
FROM
  date_axis
