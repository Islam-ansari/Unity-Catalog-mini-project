# Databricks notebook source
# MAGIC %sql
# MAGIC drop table if exists uc_mini_project.gold.driver_win;

# COMMAND ----------

# MAGIC %sql
# MAGIC create table if not exists uc_mini_project.gold.driver_win
# MAGIC as
# MAGIC select d.name, count(1) as number_of_wins
# MAGIC from uc_mini_project.silver.drivers d
# MAGIC join uc_mini_project.silver.results r
# MAGIC on d.driver_id = r.driver_id
# MAGIC where r.position = 1
# MAGIC group by d.name;

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from uc_mini_project.gold.driver_win order by number_of_wins desc;