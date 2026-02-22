"""
Ecommerce Risk & Anomaly Detection Engine
-----------------------------------------
Author: Wajiya Anam Jawaid
Purpose: Demonstrates the logic used to identify high-risk sellers and price-gouging 
         during high-traffic global events (Inspired by Amazon experience).
"""

import pandas as pd
import numpy as np

class RiskEngine:
    def __init__(self, data_path):
        self.df = pd.read_csv(data_path)
        self.df['timestamp'] = pd.to_datetime(self.df['timestamp'])
        
    def detect_price_gouging(self, threshold=2.0):
        """
        Identifies items where the current price is significantly higher 
        than the historical average for that category/seller.
        """
        self.df['price_ratio'] = self.df['item_price'] / self.df['historical_avg_price']
        gouging_mask = self.df['price_ratio'] > threshold
        return self.df[gouging_mask]

    def flag_suspicious_sellers(self, volume_threshold=500):
        """
        Flags sellers with abnormal volume spikes that might indicate 
        counterfeit dumping or bot activity.
        """
        seller_stats = self.df.groupby('seller_id').agg({
            'units_sold': 'sum',
            'transaction_id': 'count'
        }).reset_index()
        
        suspicious = seller_stats[seller_stats['units_sold'] > volume_threshold]
        return suspicious

    def run_full_audit(self):
        """
        Runs multiple risk heuristics and returns a prioritized 'Risk Register'.
        """
        gougers = self.detect_price_gouging()
        sellers = self.flag_suspicious_sellers()
        
        # Merge heuristics into a single risk report
        risk_report = self.df.copy()
        risk_report['is_gouging'] = risk_report['transaction_id'].isin(gougers['transaction_id'])
        risk_report['is_high_volume'] = risk_report['seller_id'].isin(sellers['seller_id'])
        
        # Calculate a cumulative Risk Score (0-100)
        risk_report['risk_score'] = (
            (risk_report['is_gouging'] * 60) + 
            (risk_report['is_high_volume'] * 40)
        )
        
        return risk_report.sort_values(by='risk_score', ascending=False)

if __name__ == "__main__":
    # Integration Test
    engine = RiskEngine("data/synthetic/marketplace_transactions.csv")
    report = engine.run_full_audit()
    
    print("\n--- TOP HIGH-RISK TRANSACTIONS DETECTED ---")
    print(report[report['risk_score'] > 0].head(10))
    
    # Save results for visualization
    report.to_csv("projects/03-ecommerce-risk-engine/audit_results.csv", index=False)
