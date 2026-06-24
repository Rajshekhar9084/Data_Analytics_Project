# 🛒 Superstore Sales & Profit Analysis

A complete end-to-end data analytics project using **Python** and **Power BI** to uncover sales and profit insights from the Sample Superstore dataset.

---

## 📊 Project Overview

This project analyzes retail performance across products, categories, regions, cities, customers, and time — producing two interactive Power BI dashboards and actionable business recommendations.

---

## 🖥️ Dashboards

### 1. Sales Performance Dashboard
- **Total Sales:** 2.3M | **Total Customers:** 793 | **Quantity Sold:** 38K
- Top product by sales: Canon imageCLASS 2200 Advanced Copier
- Top city: New York City | Top region: West
- Peak month: November

### 2. Profit Performance Dashboard
- **Total Profit:** 443K | **Profit Margin:** 19.26% | **Total Products:** 1,850
- Top product by profit: Canon imageCLASS 2200
- Top region by profit: East | Top customer: Tamara Chand

---

## 🔧 Tech Stack

| Tool | Purpose |
|------|---------|
| Python (Pandas, NumPy) | Data cleaning & grouping |
| Power BI | Dashboard & visualization |
| Excel (.xlsx) | Intermediate data exports |

---

## 🐍 Python Workflow

```python
# Key steps in Python_Data_Analytics_Project.py
- Load & inspect data (df.info, df.describe, null checks)
- Remove duplicates & nulls
- Fix negative profits using np.where
- Parse dates, extract Month & Year
- Group by Category, Region, City, Month, Customer
- Export grouped data to Excel for Power BI
- Calculate Profit Margin %
- Export final cleaned CSV# Data_Analytics_Project
