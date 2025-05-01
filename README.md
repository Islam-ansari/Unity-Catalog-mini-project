# 🧪 Unity Catalog Mini Project (Azure Databricks)

This is a **mini Unity Catalog project** built as part of a Udemy course. The objective is to demonstrate how to use Unity Catalog to manage data access and organization across **Bronze**, **Silver**, and **Gold** data layers in **Azure Data Lake**. Finally using databricks workflow to run the notebooks

---

## 🚀 Objective

We have three folders representing the Medallion Architecture, these are placed inside the container `uc_mini_project`:

- **Bronze**
- **Silver**
- **Gold**

In the **Bronze** container, we have two JSON files:
- `drivers.json`
- `results.json`

The goal is to:
1. Read the JSON files from the **Bronze** layer.
2. Perform basic **transformations**, and store the data as **Delta tables** in the **Silver** layer.
3. Conduct **aggregations** and write the final data to the **Gold** layer.
4. Using workflow to run all the notebooks in sequential order.

---

## 🔁 Traditional Approach (Deprecated)

This could have been done using:
`dbutils.fs.mount()`
However, since November 2024, mounts are no longer supported by Databricks. Therefore, we now use Unity Catalog to manage secure access and data organization.

### 🛠️ Unity Catalog Setup

1. Databricks Workspace: A Premium workspace creates Unity Catalog by default.
2. Storage Access:
- Created **Storage Credentials** for authentication and authorization (created using Databrick Access connector service).
- Defined an **External Location** to point to the cloud folder structure.


### 📁 Data Structure
We created a container named `uc_mini_project` in Azure Data Lake with the following folder layout:
```
uc_mini_project/
├── bronze/
│   ├── drivers.json
│   └── results.json
├── silver/
└── gold/
```

All the notebooks with transformation are already available inside `/Databricks Notebooks`
Finally these notebooks has been run using Databrick workflows
![Databricks Workflow](Images/Workflow%20in%20Databricks%20diagram.png)

