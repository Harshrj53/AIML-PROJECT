📚 Research Topic Analysis System

A traditional NLP-based research analysis system for academic documents (e.g., arXiv papers).
This project implements a classical Natural Language Processing and Machine Learning pipeline to analyze research documents without using Large Language Models (LLMs) or agentic AI systems.

🚀 Project Overview

Researchers often need a quick analytical overview of a research domain but face difficulty when reviewing multiple academic papers.

This system automates research document analysis by:

- Extracting key terms  
- Identifying latent topics  
- Clustering similar documents  
- Generating extractive summaries  
- Providing clustering evaluation metrics  

All using interpretable statistical NLP techniques.

🧠 Key Features

- 📄 Upload multiple `.txt` or `.pdf` research papers  
- 🔎 TF-IDF based key term extraction  
- 🧩 Topic modeling using Non-negative Matrix Factorization (NMF)  
- 📊 Document clustering using KMeans  
- ✂ Extractive summarization using sentence-level TF-IDF scoring  
- 📈 Silhouette score for clustering evaluation  
- 🌐 Interactive Streamlit web interface  

🏗 System Architecture

The system follows a structured NLP pipeline:

**1. Document Input**
- Research keywords  
- Uploaded TXT/PDF files  

**2. Text Preprocessing**
- Tokenization  
- Lowercasing  
- Stop-word removal  
- Lemmatization  
- Sentence segmentation  

**3. Feature Extraction**
- TF-IDF vectorization  

**4. Analysis**
- Topic modeling (NMF)  
- Document clustering (KMeans)  

**5. Summarization**
- TF-IDF-based sentence ranking  

**6. Output**
- Key terms  
- Topic clusters  
- Extractive summaries  
- Evaluation metrics  

📂 Project Structure

```text
research_topic_analysis/
│
├── app.py                # Streamlit user interface
├── nlp_pipeline.py       # Core NLP & ML processing logic
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

⚙️ Installation & Setup

**1️⃣ Clone the Repository**

```bash
git clone <your-repo-link>
cd research_topic_analysis
```

**2️⃣ Create Virtual Environment**

```bash
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
```

**3️⃣ Install Dependencies**

```bash
pip install -r requirements.txt
```

**4️⃣ Download NLP Models**

```bash
python -m spacy download en_core_web_sm
python -m nltk.downloader punkt stopwords wordnet
```

▶️ Run the Application

```bash
streamlit run app.py
```

Open the local URL (typically `http://localhost:8501`) in your browser.

📊 Core Algorithms Used

| Component          | Technique                      |
|--------------------|--------------------------------|
| Feature Extraction | TF-IDF                         |
| Topic Modeling     | NMF                            |
| Clustering         | KMeans                         |
| Summarization      | Sentence-level TF-IDF scoring  |
| Evaluation         | Silhouette Score              |

⚠️ Limitations

While effective and interpretable, traditional NLP approaches have limitations:

- No semantic understanding of context  
- Ignores word order  
- Sensitive to preprocessing decisions  
- Requires manual topic selection  
- Limited generalization across domains  
- No autonomous reasoning or external knowledge retrieval  

These limitations highlight opportunities for future integration of embedding-based models and intelligent workflows.

🔮 Future Enhancements

- Replace sparse TF-IDF with dense semantic embeddings  
- Add visualization dashboards for topic distributions  
- Improve summarization using hybrid statistical methods  
- Integrate intelligent retrieval mechanisms  
- Deploy publicly on cloud platforms  

🛠 Technologies Used

- Python  
- Streamlit  
- scikit-learn  
- spaCy  
- NLTK  

📌 License

This project is intended for academic and educational purposes.

---

# 🤖 Milestone 2: Agentic AI Research Assistant

A multi-agent autonomous research pipeline powered by **LangGraph** and **Tavily API**. Unlike Milestone 1, this system uses Large Language Models and intelligent agents to perform deep reasoning, web retrieval, and synthesis.

## 🚀 Milestone 2 Overview

The Agentic Assistant automates the entire research process:
1.  **Autonomous Search**: Uses Tavily API to fetch top-tier academic and web sources.
2.  **Intelligent Retrieval**: Scrapes and cleans content from URLs.
3.  **Contextual Summarization**: Summarizes document chunks while preserving technical nuances.
4.  **Deep Reasoning**: Synthesizes multiple summaries into cohesive insights.
5.  **Validation Node**: Checks for contradictions or uncertainties in the gathered data.
6.  **Structured Reporting**: Generates a professional report (Markdown & PDF).

## 🏗 Milestone 2 Architecture

The system uses a directed graph (LangGraph) with the following nodes:
- `search_node`: Fetches relevant URLs.
- `retrieve_node`: Scrapes web content.
- `summarize_node`: Processes document chunks.
- `reason_node`: Synthesizes insights.
- `validate_node`: Performance quality control.
- `report_node`: Formats the final research document.

## ⚙️ Tech Stack

- **Backend**: Python, FastAPI, LangGraph, LangChain, Tavily API, OpenAI/Groq.
- **Frontend**: React.js, Tailwind CSS, Vite, Lucide Icons.
- **Export**: PDF generation using `fpdf2`.

## 📂 Structure

```text
milestone2/
├── backend/
│   ├── agent.py         # FastAPI Entry Point
│   ├── graph.py         # LangGraph Workflow
│   ├── nodes/           # Individual Logic Nodes
│   └── utils/           # PDF Generation & Utilities
├── frontend/            # React/Vite UI
└── requirements.txt     # Backend Dependencies
```

## 🛠 Setup & Local Run

### Backend
1. `cd milestone2/backend`
2. `pip install -r requirements.txt`
3. Set environment variables in `.env`:
   ```env
   TAVILY_API_KEY=your_key
   OPENAI_API_KEY=your_key
   ```
4. `python agent.py` (Runs on port 8000)

### Frontend
1. `cd milestone2/frontend`
2. `npm install`
3. `npm run dev` (Runs on port 5173)

---

## 🌐 Public Deployment

- **Backend (Render)**: [Link to Backend]
- **Frontend (Vercel)**: [Link to Frontend]

