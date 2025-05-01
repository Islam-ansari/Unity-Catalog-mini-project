# Databricks notebook source
# MAGIC %sql
# MAGIC drop external location dbc_course_uc_ext_silver

# COMMAND ----------

# MAGIC %sql
# MAGIC create external location if not exists dbc_course_uc_ext_bronze
# MAGIC url 'abfss://unity-catalog-mini-project@formula1dlstg.dfs.core.windows.net/bronze'
# MAGIC with (storage credential `databrickscource-ext-storage-credencial`);

# COMMAND ----------

# MAGIC %sql
# MAGIC desc external location dbc_course_uc_ext_bronze

# COMMAND ----------

# MAGIC %fs
# MAGIC ls 'abfss://unity-catalog-mini-project@formula1dlstg.dfs.core.windows.net/bronze'

# COMMAND ----------

# MAGIC %md
# MAGIC ### Creating similarly for Silver and Gold

# COMMAND ----------

# MAGIC %sql
# MAGIC create external location if not exists dbc_course_uc_ext_silver
# MAGIC url 'abfss://unity-catalog-mini-project@formula1dlstg.dfs.core.windows.net/silver'
# MAGIC with (storage credential `databrickscource-ext-storage-credencial`);

# COMMAND ----------

# MAGIC %sql
# MAGIC create external location if not exists dbc_course_uc_ext_gold
# MAGIC url 'abfss://unity-catalog-mini-project@formula1dlstg.dfs.core.windows.net/gold'
# MAGIC with (storage credential `databrickscource-ext-storage-credencial`);