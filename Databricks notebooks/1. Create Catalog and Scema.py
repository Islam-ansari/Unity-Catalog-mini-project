# Databricks notebook source
# MAGIC %md
# MAGIC - Create Catalog
# MAGIC - Create Schema for all 3 bronze, silver and gold

# COMMAND ----------

# MAGIC %sql
# MAGIC show external locations;

# COMMAND ----------

# MAGIC %sql
# MAGIC create catalog if not exists uc_mini_project
# MAGIC managed location 'abfss://unity-catalog-mini-project@formula1dlstg.dfs.core.windows.net/';

# COMMAND ----------

# MAGIC %sql
# MAGIC use catalog uc_mini_project

# COMMAND ----------

# MAGIC %sql
# MAGIC create schema uc_mini_project.bronze
# MAGIC managed location 'abfss://unity-catalog-mini-project@formula1dlstg.dfs.core.windows.net/bronze'

# COMMAND ----------

# MAGIC %sql
# MAGIC create schema uc_mini_project.silver
# MAGIC managed location 'abfss://unity-catalog-mini-project@formula1dlstg.dfs.core.windows.net/silver'

# COMMAND ----------

# MAGIC %sql
# MAGIC create schema uc_mini_project.gold
# MAGIC managed location 'abfss://unity-catalog-mini-project@formula1dlstg.dfs.core.windows.net/gold'