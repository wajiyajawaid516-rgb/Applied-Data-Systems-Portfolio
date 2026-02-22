# Ecommerce Risk & Anomaly Detection Engine

## 📌 Project Overview
This project simulates the high-scale data auditing logic required to protect global marketplaces from **price-gouging**, **counterfeit activity**, and **seller fraud**. 

Inspired by my tenure as a **Business Operations Specialist at Amazon**, where I managed risk for millions of records during global events (FIFA World Cup, Apple Brand Protection), this system demonstrates how Python and SQL-driven heuristics can automate governance.

### 🔑 Key Engineering Features
- **Heuristic-Based Risk Scoring:** Combines price ratio analysis and volume-spike detection into a unified priority score.
- **Scale Simulation:** Designed to handle dense transaction datasets where manual review is impossible.
- **Automated Reporting:** Generates a structured "Audit Register" for compliance teams.

## 🛠️ Tech Stack
- **Python:** Logical core (Pandas, NumPy).
- **Architecture:** Modular, Object-Oriented design for easy integration into ETL pipelines.
- **Data:** Synthetic marketplace transaction data simulating real-world anomalies.

## 📊 Logic Map (Architecture)
```mermaid
graph TD
    A[Raw Transaction Data] --> B{Risk Engine}
    B --> C[Price Gauging Detector]
    B --> D[Volume Spike Detector]
    C --> E[Risk Score Calculation]
    D --> E
    E --> F[Prioritized Audit Report]
    F --> G[Governance Action / Seller Block]
