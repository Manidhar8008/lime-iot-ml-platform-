# 🚲 Lime IoT Decision Analytics Platform  
*A Data Science–Led Decision System (70% Data Science · 30% Machine Learning)*

---

## 📌 What is this project?

This project demonstrates how **raw mobility and IoT data** can be transformed into **clear, explainable operational decisions**.

The focus is **not on complex machine learning**, but on:
- framing the right business problems  
- designing reliable data foundations  
- defining decision metrics and trade-offs  
- using **simple ML models only where they add value**

This mirrors how **real data science teams** operate in production environments.

---

## 🎯 Core Objective

Convert noisy, real-world micromobility data into:

- **Decision-ready datasets**
- **Actionable risk signals**
- **Explainable recommendations for operations teams**

The output is a **single authoritative decision table** that stakeholders can trust.

---

## 🧠 How Machine Learning is Used (Intentionally Limited)

Machine learning is **not the centerpiece** of this project.

It is used to:
- support **risk estimation**
- highlight **patterns not obvious from raw data**
- provide **decision signals**, not automated actions

Models are:
- simple
- explainable
- compared and evaluated transparently

Final decisions are made through **explicit business logic**, not black-box predictions.

---

## 🏗️ Repository Structure (High-Level)
data/ → raw, processed, and decision datasets
scripts/ → data preparation and model training scripts
pipeline/ → pipeline runner for reproducible execution
reports/ → persisted evaluation reports (human-readable)
artifacts/ → generated visual outputs (PNG)
dashboard/ → static HTML dashboard prototype for stakeholders
docs/ → detailed data science narrative and analysis
notebooks/ → exploratory analysis (non-authoritative)
future_contrib/ → experimental or future extensions


---

## 🧾 Authoritative Output (Very Important)

> **`data/Decision/asset_decision_final.csv`**  
is the **single source of truth** for this system.

All:
- reports
- visuals
- dashboards
- interpretations  

are derived from this table.

---

## 📊 What This Project Shows (Data Science Skills)

- Business problem framing  
- Data pipeline design  
- Feature reasoning and metric design  
- Risk and uncertainty analysis  
- Model comparison and interpretation  
- Decision logic and trade-off thinking  
- Stakeholder-oriented communication  

This is a **decision system**, not just an analysis notebook.

---

## 🖥️ Dashboard Prototype

A lightweight **static dashboard** (`dashboard/index.html`) demonstrates how
decision outputs can be consumed by non-technical stakeholders.

No BI tools or servers required — open in a browser.

---

## 🔁 Reproducibility

A simple pipeline runner orchestrates:
- training data creation
- baseline model training
- output validation

The system is:
- deterministic
- auditable
- easy to extend

---

## 🚫 Out of Scope (By Design)

To keep the project focused, the following are intentionally excluded:
- real-time data ingestion
- automated retraining
- production infrastructure
- live dashboards

This project prioritizes **decision clarity over system complexity**.

---

## 👤 Intended Audience

- Data Scientists  
- Analytics Leads  
- Product & Operations Managers  
- Interviewers evaluating real-world problem solving  

---

## ✅ Final Note

This repository reflects how **modern data science teams** build systems:
- start with decisions
- earn trust through data
- use ML as a tool, not a goal

---
