# Databricks notebook source
# MAGIC %md
# MAGIC We are making this notebook reiterable
# MAGIC - hense we are deleting existing table and creating new table for all 3 layers

# COMMAND ----------

# MAGIC %sql
# MAGIC Drop table if exists uc_mini_project.bronze.drivers

# COMMAND ----------

# MAGIC %sql
# MAGIC create table if not exists uc_mini_project.bronze.drivers
# MAGIC (
# MAGIC   driverId INT,
# MAGIC   driverRef STRING,
# MAGIC   number INT,
# MAGIC   code STRING,
# MAGIC   name STRUCT<forename: STRING, surname: STRING>,
# MAGIC   dob DATE,
# MAGIC   nationality STRING,
# MAGIC   url STRING
# MAGIC ) using json
# MAGIC options (path 'abfss://unity-catalog-mini-project@formula1dlstg.dfs.core.windows.net/bronze/drivers.json')

# COMMAND ----------

# MAGIC %sql
# MAGIC Drop table if exists uc_mini_project.bronze.results

# COMMAND ----------

# MAGIC %sql
# MAGIC create table if not exists uc_mini_project.bronze.results
# MAGIC (
# MAGIC   resultId INT,
# MAGIC raceId INT,
# MAGIC driverId INT,
# MAGIC constructorId INT,
# MAGIC number INT,grid INT,
# MAGIC position INT,
# MAGIC positionText STRING,
# MAGIC positionOrder INT,
# MAGIC points INT,
# MAGIC laps INT,
# MAGIC time STRING,
# MAGIC milliseconds INT,
# MAGIC fastestLap INT,
# MAGIC rank INT,
# MAGIC fastestLapTime STRING,
# MAGIC fastestLapSpeed FLOAT,
# MAGIC statusId STRING
# MAGIC ) using json
# MAGIC options (path 'abfss://unity-catalog-mini-project@formula1dlstg.dfs.core.windows.net/bronze/results.json')