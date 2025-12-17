# agents/master_agent.py
from agents.iqvia_agent import IQVIAAgent
from agents.exim_agent import EXIMAgent
from agents.patent_agent import PatentAgent
from agents.trials_agent import ClinicalTrialsAgent
from agents.internal_knowledge_agent import InternalKnowledgeAgent
from agents.web_intelligence_agent import WebIntelligenceAgent
from agents.report_agent import ReportAgent
import requests

class MasterAgent:
    def __init__(self):
        self.iqvia = IQVIAAgent()
        self.exim = EXIMAgent()
        self.patent = PatentAgent()
        self.trials = ClinicalTrialsAgent()
        self.internal = InternalKnowledgeAgent()
        self.web = WebIntelligenceAgent()
        self.report = ReportAgent()

    def _call_report_pdf(self, sections):
        try:
            resp = requests.post(
                "http://localhost:7006/generate-report",
                json={"title": "Portfolio Analysis", "sections": sections},
                timeout=10,
            )
            if resp.ok:
                # In real use, save to storage and return link; here we just say "PDF generated"
                return "PDF report generated (download via /generate-report call)."
        except Exception:
            return "PDF generation failed."
        return "PDF generation failed."

    def analyze_portfolio(self, query: str, product: str, therapy: str, country: str):
        # 1. Market
        market_data = self.iqvia.fetch_market_data()
        market_text = self.iqvia.get_summary(market_data)

        # 2. Trade
        trade_data = self.exim.fetch_trade_data()
        trade_bullets = self.exim.get_bullets(trade_data)

        # 3. Patent
        patent_data = self.patent.fetch_patent_status()

        # 4. Trials
        trials = self.trials.fetch_trials(indication=therapy, country=country)
        trials_summary = self.trials.get_summary(trials)

        # 5. Internal docs
        internal_docs = self.internal.search(f"{therapy} {country}")
        internal_summary = self.internal.get_summary(internal_docs)

        # 6. Web
        web_results = self.web.search(f"{therapy} {country} guidelines")
        web_summary = self.web.get_summary(web_results)

        # 7. Text + Data summary
        text_summary = self.report.build_text_summary(market_data, trade_data, patent_data)
        df_summary = self.report.build_summary_dataframe(market_data, trade_data, patent_data)

        sections = [
            {"heading": "User Question", "text": query},
            {"heading": "Market Insights", "text": market_text},
            {"heading": "Trade Insights", "text": " ".join(trade_bullets)},
            {"heading": "Patent Landscape", "text": f"Patent data: {patent_data}"},
            {"heading": "Clinical Trials", "text": trials_summary},
            {"heading": "Internal Insights", "text": internal_summary},
            {"heading": "Web Signals", "text": web_summary},
            {"heading": "Overall Summary", "text": text_summary},
        ]

        pdf_note = self._call_report_pdf(sections)

        return {
            "summary_text": text_summary,
            "market_data": market_data,
            "trade_data": trade_data,
            "patent_data": patent_data,
            "trials": trials,
            "internal_docs": internal_docs,
            "web_results": web_results,
            "summary_table": df_summary.to_dict(orient="records"),
            "pdf_status": pdf_note,
        }

