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

    def analyze_portfolio(
        self,
        query: str,
        product: str,
        therapy: str,
        country: str,
        sources: list[str],
    ):
        # If no sources selected → ALL
        if not sources:
            sources = [
                "Market Trends","Trade",
                "Clinical Trials",
                "Patent",
                "Web Search",
                "Internal Docs",
            ]

        market_data = {}
        trade_data = {}
        patent_data = {}
        trials = []
        internal_docs = []
        web_results = []

        if "Market Trends" in sources:
            market_data = self.iqvia.fetch_market_data()

        if "Trade" in sources:
            trade_data = self.exim.fetch_trade_data()

        if "Patent" in sources:
            patent_data = self.patent.fetch_patent_status()

        if "Clinical Trials" in sources:
            trials = self.trials.fetch_trials(
                indication=therapy,
                country=country
            )

        if "Internal Docs" in sources:
            internal_docs = self.internal.search(f"{therapy} {country}")

        if "Web Search" in sources:
            web_results = self.web.search(f"{therapy} {country} guidelines")

        text_summary = self.report.build_text_summary(
            market_data,
            trade_data,
            patent_data
        )

        summary_table = self.report.build_summary_dataframe(
            market_data,
            trade_data,
            patent_data
        )

        return {
            "query": query,
            "sources_used": sources,
            "summary_text": text_summary,
            "market_data": market_data,
            "trade_data": trade_data,
            "patent_data": patent_data,
            "trials": trials,
            "internal_docs": internal_docs,
            "web_results": web_results,
            "summary_table": summary_table.to_dict(orient="records"),
        }