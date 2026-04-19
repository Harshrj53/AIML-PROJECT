from fpdf import FPDF
import os

class PDFReport(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 15)
        self.cell(0, 10, 'Agentic AI Research Report', 0, 1, 'C')
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

def generate_pdf(report_data, output_path):
    pdf = PDFReport()
    pdf.add_page()
    
    # Title
    pdf.set_font("Arial", 'B', 16)
    pdf.multi_cell(0, 10, report_data.get('title', 'Research Report'))
    pdf.ln(5)
    
    # Abstract
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(0, 10, 'Abstract', 0, 1)
    pdf.set_font("Arial", '', 11)
    pdf.multi_cell(0, 7, report_data.get('abstract', 'N/A'))
    pdf.ln(5)
    
    # Key Findings
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(0, 10, 'Key Findings', 0, 1)
    pdf.set_font("Arial", '', 11)
    pdf.multi_cell(0, 7, report_data.get('key_findings', 'N/A'))
    pdf.ln(5)
    
    # Conclusion
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(0, 10, 'Conclusion', 0, 1)
    pdf.set_font("Arial", '', 11)
    pdf.multi_cell(0, 7, report_data.get('conclusion', 'N/A'))
    pdf.ln(5)
    
    # Sources
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(0, 10, 'Sources', 0, 1)
    pdf.set_font("Arial", '', 10)
    sources = report_data.get('sources', [])
    if isinstance(sources, list):
        for source in sources:
            pdf.write(5, f"- {source}\n")
    else:
        pdf.multi_cell(0, 7, str(sources))

    pdf.output(output_path)
    return output_path
