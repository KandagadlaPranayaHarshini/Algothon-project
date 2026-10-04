"# Algothon-project" 
# 🔎 The Mystery Dataset — Online Retail Analysis

**ALG-DATA-01 | Data Science | ALGOTHON'26**

## 📌 Overview

The Mystery Dataset is a discovery-driven data analysis project based on the **Online Retail Dataset**.

Instead of starting with a predefined business question, the project investigates the dataset systematically to discover hidden patterns, relationships, anomalies, and meaningful insights.

The analysis focuses on unusual transaction behavior involving **negative quantities, invoice types, zero prices, product descriptions, countries, and time patterns**.

---

## 🎯 Objective

The project aims to:

* Understand the dataset
* Investigate data quality
* Identify relationships between variables
* Detect unusual transactions
* Formulate hypotheses from observed patterns
* Visualize important findings
* Produce an evidence-backed analytical discovery

---

## 📊 Dataset

**Dataset:** Online Retail Dataset

**Source:** UCI Machine Learning Repository

### Dataset Size

* **541,909 rows**
* **8 columns**
* **December 2010 – December 2011**

### Variables

| Variable      | Description                        |
| ------------- | ---------------------------------- |
| `InvoiceNo`   | Transaction/invoice identifier     |
| `StockCode`   | Product identifier                 |
| `Description` | Product or transaction description |
| `Quantity`    | Quantity involved in transaction   |
| `InvoiceDate` | Transaction date and time          |
| `UnitPrice`   | Price per unit                     |
| `CustomerID`  | Customer identifier                |
| `Country`     | Customer country                   |

---

## 🛠️ Technologies Used

* Python
* Pandas
* Matplotlib
* Exploratory Data Analysis
* Statistical Analysis

---

## 🔍 Analysis Workflow

```text
Dataset
   ↓
Dataset Understanding
   ↓
Data Quality Investigation
   ↓
Anomaly Detection
   ↓
Relationship Analysis
   ↓
Visualization
   ↓
Hypothesis Formation
   ↓
Analytical Result
   ↓
Final Discovery
```

---

## 🚨 Key Discovery

The analysis identified a distinct group of unusual transactions containing:

* Negative quantity
* Zero unit price
* No `C`-prefixed invoice
* Strong concentration in the United Kingdom
* Descriptions associated with damage, checking, disposal, missing items, or adjustments

### Important Observation

There are **10,624 negative-quantity transactions** in the dataset.

Of these:

* **9,288** have a `C`-prefixed invoice.
* **1,336** do not have a `C`-prefixed invoice.

The **1,336 non-`C` negative transactions** form a particularly interesting subgroup because they also have zero unit price and frequently contain operational descriptions.

---

## 💡 Hypothesis

> A subset of negative-quantity, zero-price transactions may represent operational inventory adjustments or non-sales activities rather than ordinary customer cancellations.

This hypothesis is supported using multiple variables rather than a single observation.

---

## 📈 Visualizations

The project generates four main visualizations:

1. **Negative Quantity Transactions by Invoice Type**
2. **Top Descriptions in Zero-Price Negative Transactions**
3. **Products with Highest Negative Quantity**
4. **Monthly Pattern of Zero-Price Negative Transactions**

All four visualizations are displayed together when the analysis script is executed.

---

## 📁 Project Structure

```text
The-Mystery-Dataset/
│
├── analysis.py
├── Online Retail.xlsx
└── README.md
```

> The dataset file may be excluded from the repository depending on dataset redistribution requirements. It can be obtained separately from the original UCI source.

---

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone <YOUR-REPOSITORY-URL>
```

### 2. Open the project

```bash
cd The-Mystery-Dataset
```

### 3. Install dependencies

```bash
pip install pandas matplotlib openpyxl
```

### 4. Add the dataset

Place the following file in the same folder as `analysis.py`:

```text
Online Retail.xlsx
```

### 5. Run the analysis

```bash
python analysis.py
```

The terminal will display the analytical findings, and the visualization window will display the generated graphs.

---

## 📌 Results

The project demonstrates that negative transactions in a retail dataset should not automatically be treated as one category.

Combining:

* Invoice information
* Quantity
* Unit price
* Product descriptions
* Country
* Time

reveals a more complex transaction structure.

---

## 🚀 Future Scope

* Interactive analytics dashboard
* NLP-based transaction description classification
* Automated anomaly detection
* Product-level anomaly monitoring
* Country-level comparison
* Predictive modeling
* Automated transaction classification

---

## 🏆 Hackathon Alignment

| ALG-DATA-01 Requirement | Status |
| ----------------------- | ------ |
| Data exploration        | ✅      |
| Variable understanding  | ✅      |
| Relationship analysis   | ✅      |
| Anomaly detection       | ✅      |
| Visualization           | ✅      |
| Hypothesis formation    | ✅      |
| Analytical result       | ✅      |
| Meaningful discovery    | ✅      |

---

## 👩‍💻 Project

**ALGOTHON'26 — Data Science**

**Problem Statement:** ALG-DATA-01 — The Mystery Dataset
