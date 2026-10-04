import pandas as pd
import matplotlib.pyplot as plt

# ============================================================
# 1. LOAD DATASET
# ============================================================

df = pd.read_excel("Online Retail.xlsx")

print("=" * 70)
print("                    ALG-DATA-01")
print("                  THE MYSTERY DATASET")
print("=" * 70)

print("\nDataset Shape:")
print(df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nData Types:")
print(df.dtypes)

print("\nMissing Values:")
print(df.isnull().sum())


# ============================================================
# 2. BASIC DATA PREPARATION
# ============================================================

df["InvoiceNo"] = df["InvoiceNo"].astype(str)

# Total transaction value
df["TotalAmount"] = df["Quantity"] * df["UnitPrice"]

print("\n" + "=" * 70)
print("                    BASIC STATISTICS")
print("=" * 70)

print("\nTotal Rows:", len(df))
print("Unique Invoices:", df["InvoiceNo"].nunique())
print("Unique Products:", df["StockCode"].nunique())
print("Unique Countries:", df["Country"].nunique())


# ============================================================
# 3. NEGATIVE QUANTITY ANALYSIS
# ============================================================

negative_quantity = df[df["Quantity"] < 0]

cancelled = df[
    df["InvoiceNo"].str.startswith("C")
]

negative_cancelled = negative_quantity[
    negative_quantity["InvoiceNo"].str.startswith("C")
]

negative_not_cancelled = negative_quantity[
    ~negative_quantity["InvoiceNo"].str.startswith("C")
]

print("\n" + "=" * 70)
print("              NEGATIVE QUANTITY ANALYSIS")
print("=" * 70)

print("\nTotal Negative Quantity Transactions:")
print(len(negative_quantity))

print("\nNegative Transactions with C Invoice:")
print(len(negative_cancelled))

print("\nNegative Transactions without C Invoice:")
print(len(negative_not_cancelled))


# ============================================================
# 4. MISSING CUSTOMER ANALYSIS
# ============================================================

missing_customer = df[
    df["CustomerID"].isna()
]

print("\n" + "=" * 70)
print("               CUSTOMER ID ANALYSIS")
print("=" * 70)

print("\nMissing CustomerID Rows:")
print(len(missing_customer))

print("\nMissing CustomerID by Country:")
print(
    missing_customer["Country"]
    .value_counts()
    .head(10)
)


# ============================================================
# 5. ZERO-PRICE NEGATIVE TRANSACTIONS
# ============================================================

zero_price_negative = df[
    (df["Quantity"] < 0) &
    (df["UnitPrice"] == 0)
]

print("\n" + "=" * 70)
print("          ZERO-PRICE NEGATIVE TRANSACTIONS")
print("=" * 70)

print("\nNumber of Transactions:")
print(len(zero_price_negative))

print("\nTotal Negative Quantity:")
print(zero_price_negative["Quantity"].sum())

print("\nCountries:")
print(
    zero_price_negative["Country"]
    .value_counts()
)

print("\nInvoice Prefix:")
print(
    zero_price_negative["InvoiceNo"]
    .str.startswith("C")
    .value_counts()
)


# ============================================================
# 6. DESCRIPTION ANALYSIS
# ============================================================

description_counts = (
    zero_price_negative["Description"]
    .value_counts()
    .head(10)
)

print("\n" + "=" * 70)
print("                TOP DESCRIPTIONS")
print("=" * 70)

print(description_counts)


# ============================================================
# 7. PRODUCT ANALYSIS
# ============================================================

product_quantity = (
    zero_price_negative
    .groupby("StockCode")["Quantity"]
    .sum()
    .sort_values()
)

print("\n" + "=" * 70)
print("                 PRODUCT ANALYSIS")
print("=" * 70)

print("\nProducts with Largest Negative Quantity:")
print(product_quantity.head(10))


# ============================================================
# 8. COUNTRY ANALYSIS
# ============================================================

country_transactions = (
    df["Country"]
    .value_counts()
)

print("\n" + "=" * 70)
print("                 COUNTRY ANALYSIS")
print("=" * 70)

print("\nTop Countries by Transactions:")
print(country_transactions.head(10))


# ============================================================
# 9. MONTHLY ANALYSIS
# ============================================================

monthly_sales = (
    df[df["Quantity"] > 0]
    .set_index("InvoiceDate")["TotalAmount"]
    .resample("ME")
    .sum()
)

monthly_negative = (
    zero_price_negative
    .set_index("InvoiceDate")["Quantity"]
    .resample("ME")
    .sum()
)

print("\n" + "=" * 70)
print("                  MONTHLY ANALYSIS")
print("=" * 70)

print("\nMonthly Sales:")
print(monthly_sales)

print("\nMonthly Zero-Price Negative Quantity:")
print(monthly_negative)


# ============================================================
# 10. RELATIONSHIP ANALYSIS
# ============================================================

print("\n" + "=" * 70)
print("              STEP 5: RELATIONSHIP ANALYSIS")
print("=" * 70)


# ------------------------------------------------------------
# Relationship 1:
# Quantity vs UnitPrice
# ------------------------------------------------------------

valid_sales = df[
    (df["Quantity"] > 0) &
    (df["UnitPrice"] > 0)
]

quantity_price_correlation = (
    valid_sales["Quantity"]
    .corr(valid_sales["UnitPrice"])
)

print("\n1. Quantity vs UnitPrice Correlation:")
print(round(quantity_price_correlation, 4))


# ------------------------------------------------------------
# Relationship 2:
# Negative Quantity vs Invoice Type
# ------------------------------------------------------------

c_percentage = (
    len(negative_cancelled) /
    len(negative_quantity)
) * 100

non_c_percentage = (
    len(negative_not_cancelled) /
    len(negative_quantity)
) * 100

print("\n2. Negative Quantity Distribution:")
print(
    f"C Invoice: {c_percentage:.2f}%"
)

print(
    f"Non-C Invoice: {non_c_percentage:.2f}%"
)


# ------------------------------------------------------------
# Relationship 3:
# Missing CustomerID concentration
# ------------------------------------------------------------

uk_missing = len(
    missing_customer[
        missing_customer["Country"] == "United Kingdom"
    ]
)

missing_customer_percentage_uk = (
    uk_missing /
    len(missing_customer)
) * 100

print("\n3. Missing CustomerID Concentration:")
print(
    f"UK: {uk_missing} rows "
    f"({missing_customer_percentage_uk:.2f}%)"
)


# ------------------------------------------------------------
# Relationship 4:
# Zero-price negative transactions concentration
# ------------------------------------------------------------

uk_zero_price = len(
    zero_price_negative[
        zero_price_negative["Country"] == "United Kingdom"
    ]
)

uk_zero_price_percentage = (
    uk_zero_price /
    len(zero_price_negative)
) * 100

print("\n4. Zero-Price Negative Transaction Concentration:")
print(
    f"UK: {uk_zero_price} rows "
    f"({uk_zero_price_percentage:.2f}%)"
)


# ============================================================
# 11. HYPOTHESIS TESTING
# ============================================================

print("\n" + "=" * 70)
print("               STEP 6: HYPOTHESIS")
print("=" * 70)

print("""
Hypothesis:

The dataset contains a distinct group of transactions
that may represent operational inventory adjustments,
damage, disposal, stock checking, or similar non-sales
activities rather than ordinary customer sales.

We investigate this using three signals:

1. Negative Quantity
2. Zero UnitPrice
3. Description text indicating damage, checking,
   disposal, adjustment, etc.
""")


# ------------------------------------------------------------
# Identify operational keywords
# ------------------------------------------------------------

keywords = [
    "damage",
    "damaged",
    "check",
    "destroy",
    "destroyed",
    "throw",
    "thrown",
    "missing",
    "wet",
    "rust",
    "crush",
    "adjustment",
    "unsaleable",
    "smashed",
    "incorrect",
    "reverse"
]

description_text = (
    zero_price_negative["Description"]
    .fillna("")
    .astype(str)
    .str.lower()
)

keyword_mask = description_text.str.contains(
    "|".join(keywords),
    regex=True
)

keyword_transactions = zero_price_negative[
    keyword_mask
]

print("\nZero-price negative transactions:")
print(len(zero_price_negative))

print("\nTransactions containing operational keywords:")
print(len(keyword_transactions))

keyword_percentage = (
    len(keyword_transactions) /
    len(zero_price_negative)
) * 100

print(
    f"\nPercentage with operational keywords: "
    f"{keyword_percentage:.2f}%"
)


# ============================================================
# 12. ANALYTICAL RESULT
# ============================================================

print("\n" + "=" * 70)
print("             STEP 7: ANALYTICAL RESULT")
print("=" * 70)


# ------------------------------------------------------------
# Result 1
# ------------------------------------------------------------

print("\nRESULT 1:")
print(
    f"{len(negative_quantity):,} transactions "
    "contain negative quantities."
)

print(
    f"{len(negative_cancelled):,} of them "
    f"({c_percentage:.2f}%) have a C-prefixed invoice."
)

print(
    f"{len(negative_not_cancelled):,} "
    f"({non_c_percentage:.2f}%) do NOT have a C-prefixed invoice."
)


# ------------------------------------------------------------
# Result 2
# ------------------------------------------------------------

print("\nRESULT 2:")

print(
    f"{len(zero_price_negative):,} transactions have "
    "both negative quantity and zero UnitPrice."
)

print(
    f"{uk_zero_price_percentage:.2f}% of these transactions "
    "are from the United Kingdom."
)


# ------------------------------------------------------------
# Result 3
# ------------------------------------------------------------

print("\nRESULT 3:")

print(
    f"{keyword_percentage:.2f}% of zero-price negative "
    "transactions contain descriptions associated with "
    "damage, checking, disposal, adjustment, or similar "
    "operational activity."
)


# ------------------------------------------------------------
# Result 4
# ------------------------------------------------------------

print("\nRESULT 4:")

print(
    f"{missing_customer_percentage_uk:.2f}% of all rows "
    "with missing CustomerID belong to the United Kingdom."
)


# ============================================================
# 13. FINAL DISCOVERY
# ============================================================

print("\n" + "=" * 70)
print("              STEP 8: FINAL DISCOVERY")
print("=" * 70)

print("""
DISCOVERY:

The investigation revealed a distinct transaction pattern
within the Online Retail dataset.

A group of transactions has:

    • Negative Quantity
    • Zero UnitPrice
    • No C-prefixed invoice
    • Strong concentration in the United Kingdom
    • Descriptions frequently referring to damage,
      checking, disposal, missing items, or adjustments

This pattern is different from ordinary sales transactions
and also differs from the majority of cancellation-style
negative transactions.

Therefore, the dataset appears to contain operational
inventory-related records mixed with normal customer
transactions.

This is an important discovery because treating every
negative quantity as a simple customer cancellation would
hide this second pattern.
""")


# ============================================================
# 14. VISUALIZATION DATA
# ============================================================

# GRAPH 1
invoice_types = [
    "C Invoice",
    "Non-C Invoice"
]

invoice_counts = [
    len(negative_cancelled),
    len(negative_not_cancelled)
]


# GRAPH 2
description_counts = (
    zero_price_negative["Description"]
    .value_counts()
    .head(10)
)


# GRAPH 3
product_quantity = (
    zero_price_negative
    .groupby("StockCode")["Quantity"]
    .sum()
    .sort_values()
    .head(10)
)


# GRAPH 4
monthly_negative = (
    zero_price_negative
    .set_index("InvoiceDate")["Quantity"]
    .resample("ME")
    .sum()
)


# ============================================================
# 15. ALL VISUALIZATIONS IN ONE WINDOW
# ============================================================

fig, axes = plt.subplots(
    2,
    2,
    figsize=(17, 11)
)


# ------------------------------------------------------------
# GRAPH 1
# ------------------------------------------------------------

axes[0, 0].bar(
    invoice_types,
    invoice_counts
)

axes[0, 0].set_title(
    "Negative Quantity Transactions by Invoice Type"
)

axes[0, 0].set_xlabel(
    "Invoice Type"
)

axes[0, 0].set_ylabel(
    "Number of Transactions"
)


# ------------------------------------------------------------
# GRAPH 2
# ------------------------------------------------------------

axes[0, 1].bar(
    description_counts.index.astype(str),
    description_counts.values
)

axes[0, 1].set_title(
    "Top Descriptions in Zero-Price Negative Transactions"
)

axes[0, 1].set_xlabel(
    "Description"
)

axes[0, 1].set_ylabel(
    "Number of Transactions"
)

axes[0, 1].tick_params(
    axis="x",
    rotation=45
)


# ------------------------------------------------------------
# GRAPH 3
# ------------------------------------------------------------

axes[1, 0].bar(
    product_quantity.index.astype(str),
    product_quantity.values
)

axes[1, 0].set_title(
    "Products with Highest Negative Quantity"
)

axes[1, 0].set_xlabel(
    "Stock Code"
)

axes[1, 0].set_ylabel(
    "Total Negative Quantity"
)

axes[1, 0].tick_params(
    axis="x",
    rotation=45
)


# ------------------------------------------------------------
# GRAPH 4
# ------------------------------------------------------------

axes[1, 1].plot(
    monthly_negative.index,
    monthly_negative.values,
    marker="o"
)

axes[1, 1].set_title(
    "Monthly Pattern of Zero-Price Negative Transactions"
)

axes[1, 1].set_xlabel(
    "Month"
)

axes[1, 1].set_ylabel(
    "Total Negative Quantity"
)

axes[1, 1].tick_params(
    axis="x",
    rotation=45
)

axes[1, 1].grid(True)


# ============================================================
# FINAL DISPLAY
# ============================================================

plt.tight_layout()

plt.show()


print("\n" + "=" * 70)
print("                 ANALYSIS COMPLETED")
print("=" * 70)

print("""
DATA-01 ANALYSIS PIPELINE COMPLETE:

1. Dataset Understanding       ✓
2. Data Quality Analysis       ✓
3. Anomaly Detection           ✓
4. Visualization               ✓
5. Relationship Analysis       ✓
6. Hypothesis Formation        ✓
7. Analytical Results          ✓
8. Final Discovery             ✓
""")