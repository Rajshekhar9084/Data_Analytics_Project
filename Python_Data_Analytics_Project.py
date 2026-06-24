import pandas as pd
import numpy as np

df=pd.read_excel("Sample - Superstore.xlsx")
print(df)

print(df.info())
print(df.describe())
print(df.isnull().sum())
df.drop_duplicates(inplace=True)
df.dropna(inplace=True)
df["Profit"]=np.where(df["Profit"]<0,0,df["Profit"])
df["Order Date"]=pd.to_datetime(df["Order Date"])
df["Month"]=df["Order Date"].dt.month_name()
df["Year"]=df["Order Date"].dt.year

# #GROUPING DATA BY CATEGORY AND CALCULATING TOTAL SALES AND PROFIT
grouped_category=df.groupby("Category").agg(Total_Sales=("Sales","sum"),Total_Profit=("Profit","sum")).reset_index()
grouped_category.to_excel("Category_Analysis.xlsx", index=False)
grouped_region=df.groupby("Region").agg(Total_Sales=("Sales","sum"),Total_Profit=("Profit","sum")).reset_index()
grouped_region.to_excel("Region_Profit_Analysis.xlsx", index=False)
grouped_city=df.groupby("City").agg(Total_Sales=("Sales","sum"),Total_Profit=("Profit","sum")).reset_index()
grouped_city.to_excel("City_Profit_Analysis.xlsx", index=False)
grouped_df=df.groupby("Category").agg(Total_Sales=("Sales", "sum"),Total_Profit=("Profit", "sum")).reset_index()
grouped_df.to_excel("Category_Profit_Analysis.xlsx", index=False)
grouped_df_month=df.groupby("Month").agg(Total_Sales=("Sales","sum"),Total_Profit=("Profit", "sum")).reset_index()
grouped_df_month.to_excel("Monthly_Profit_Analysis.xlsx", index=False)
grouped_df_year=df.groupby("Year").agg(Total_Sales=("Sales","sum"),Total_Profit=("Profit", "sum")).reset_index()
grouped_df_year.to_excel("Yearly_Profit_Analysis.xlsx", index=False)
df["Profit_Margin"]=(df["Profit"]/df["Sales"])*100
df["Shipping Days"]=(df["Ship Date"]-df['Order Date']).dt.days
grouped_Customer=df.groupby("Customer Name").agg(Total_Sales=("Sales","sum"),Total_Profit=("Profit","sum")).reset_index()
grouped_Customer.to_excel("Customer_Profit_Analysis.xlsx", index=False)
df[df["Profit"]<0].groupby("Product Name")["Profit"].sum().sort_values(ascending=False).head(10)
df[df["Profit"]<0].groupby("Region")["Profit"].sum().sort_values(ascending=False).head(10)

df.drop(columns=["Sub-Category"],inplace=True)

df.to_csv("Superstore_Analysis.csv", index=False)