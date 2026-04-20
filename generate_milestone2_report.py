from fpdf import FPDF

class ProjectReport(FPDF):
    def header(self):
        self.set_font('Helvetica', 'B', 20)
        self.set_text_color(15, 23, 42) # Slate 900
        self.cell(0, 20, 'AL:ML Project Report', 0, 1, 'C')
        self.set_font('Helvetica', 'I', 12)
        self.cell(0, 10, 'Milestone 2: Agentic AI Research Assistant', 0, 1, 'C')
        self.ln(10)
        self.set_draw_color(226, 232, 240) # Slate 200
        self.line(10, 45, 200, 45)
        self.ln(10)

    def footer(self):
        self.set_y(-20)
        self.set_font('Helvetica', 'I', 8)
        self.set_text_color(100)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

def create_report():
    pdf = ProjectReport()
    pdf.add_page()
    
    # Sections
    sections = [
        ("Executive Summary", "This report details the implementation of Milestone 2, which transforms the traditional NLP system into an autonomous Agentic AI Research Assistant. The system leverages multi-agent orchestration via LangGraph to perform deep research, validation, and synthesis of complex topics."),
        ("Architecture", "The pipeline is designed as a directed graph (LangGraph) consisting of six specialized nodes:\n\n1. Search Node: Autonomous web retrieval via Tavily API.\n2. Retrieve Node: Intelligent scraping and content cleaning.\n3. Summarize Node: High-fidelity summarization using state-of-the-art LLMs.\n4. Reason Node: Facts synthesis and insight extraction.\n5. Validate Node: Quality control for contradictions and gaps.\n6. Report Node: Final structured data generation."),
        ("Technical Stack", "Backend: Python 3.14+, FastAPI, LangGraph, LangChain, Tavily API.\nFrontend: React.js (Vite), Tailwind CSS, Lucide Icons.\nDeployment: Render (Backend) and Vercel (Frontend)."),
        ("Key Features", "- Autonomous Multi-Stage Reasoning\n- Factual Consistency Validation\n- Professional PDF Report Generation\n- Premium Glassmorphism User Interface"),
        ("Conclusion", "Milestone 2 successfully demonstrates the efficiency of agentic workflows. By reducing manual research overhead through intelligent automation, the system provides verified, high-quality technical summaries for researchers.")
    ]

    for title, content in sections:
        pdf.set_font('Helvetica', 'B', 14)
        pdf.set_text_color(37, 99, 235) # Blue 600
        pdf.cell(0, 10, title, 0, 1)
        pdf.ln(2)
        pdf.set_font('Helvetica', '', 11)
        pdf.set_text_color(51, 65, 85) # Slate 700
        pdf.multi_cell(0, 7, content)
        pdf.ln(8)

    pdf.output('Milestone_2_Project_Report.pdf')

if __name__ == "__main__":
    create_report()
