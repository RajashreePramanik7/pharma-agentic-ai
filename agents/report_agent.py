# report_agent.py
import pandas as pd

class ReportAgent:
    def build_summary_dataframe(self, market, trade, patent):
        return pd.DataFrame({
            "Market_Size_M": [market.get("market_size", 0) / 1e6],
            "CAGR": [market.get("cagr", 0)],
            "Export_KG": [trade.get("export_volume_kg", 0)],
            "Patent_Expiry": [patent.get("expiry_date", "N/A")],
            "FTO_Status": [patent.get("fto_flag", "N/A")],
        })

    def build_text_summary(self, market, trade, patent):
        lines = []
        if market:
            lines.append(
                f"Market: {market.get('therapy_area','N/A')} "
                f"(${market.get('market_size',0)/1e6:.1f}M, "
                f"{market.get('cagr',0)}% CAGR)."
            )
        if trade:
            lines.append(
                f"Trade: {trade.get('api_name','N/A')} export "
                f"{trade.get('export_volume_kg',0)} kg, "
                f"dependency {trade.get('import_dependency','N/A')}."
            )
        if patent:
            lines.append(
                f"Patent: {patent.get('patent_number','N/A')} expires "
                f"{patent.get('expiry_date','N/A')} (FTO: {patent.get('fto_flag','N/A')})."
            )
        return " ".join(lines) if lines else "No data available."
