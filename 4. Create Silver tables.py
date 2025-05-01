# Databricks notebook source
# MAGIC %sql
# MAGIC drop table if exists uc_mini_project.silver.drivers;

# COMMAND ----------

# MAGIC %sql
# MAGIC create table if not exists uc_mini_project.silver.drivers
# MAGIC as
# MAGIC select driverId as driver_id,
# MAGIC   driverRef as driver_ref,
# MAGIC   number,
# MAGIC   code,
# MAGIC   concat(name.forename, ' ', name.surname) as name,
# MAGIC   dob,
# MAGIC   nationality,
# MAGIC   current_timestamp() as ingestion_date
# MAGIC from uc_mini_project.bronze.drivers;

# COMMAND ----------

# MAGIC %sql
# MAGIC drop table if exists uc_mini_project.silver.results;

# COMMAND ----------

# MAGIC %sql
# MAGIC create table if not exists uc_mini_project.silver.results
# MAGIC as
# MAGIC select 
# MAGIC   resultId as result_id,
# MAGIC   raceId as race_id,
# MAGIC   driverId as driver_id,
# MAGIC   constructorId as constructor_id,
# MAGIC   number,
# MAGIC   grid,
# MAGIC   position,
# MAGIC   positionText as position_text,
# MAGIC   positionOrder as position_order,
# MAGIC   points,
# MAGIC   laps,
# MAGIC   time,
# MAGIC   milliseconds,
# MAGIC   fastestLap as fastest_lap,
# MAGIC   rank,
# MAGIC   fastestLapTime fastest_lap_time,
# MAGIC   fastestLapSpeed fastest_lap_speed,
# MAGIC   statusId as status_id,
# MAGIC   current_timestamp() as ingestion_date
# MAGIC from uc_mini_project.bronze.results;

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from uc_mini_project.silver.results;