import React, { useState } from 'react';
import axios from 'axios';
import { Search, Loader2, Download, ExternalLink, BookOpen, AlertCircle } from 'lucide-react';
import ReactMarkdown from 'react-markdown';

const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000';

function App() {
  const [query, setQuery] = useState('');
  const [loading, setLoading] = useState(false);
  const [report, setReport] = useState(null);
  const [pdfUrl, setPdfUrl] = useState(null);
  const [error, setError] = useState(null);

  const handleSearch = async (e) => {
    e.preventDefault();
    if (!query.trim()) return;

    setLoading(true);
    setReport(null);
    setPdfUrl(null);
    setError(null);

    try {
      const response = await axios.post(`${API_BASE_URL}/research`, { query });
      setReport(response.data.report);
      setPdfUrl(response.data.pdf_url);
    } catch (err) {
      console.error(err);
      setError(err.response?.data?.detail || 'An error occurred while generating the research report.');
    } finally {
      setLoading(false);
    }
  };

  const handleDownload = () => {
    if (pdfUrl) {
      window.open(`${API_BASE_URL}${pdfUrl}`, '_blank');
    }
  };

  return (
    <div className="min-h-screen bg-[#0f172a] bg-[radial-gradient(ellipse_at_top,_var(--tw-gradient-stops))] from-slate-900 via-slate-900 to-black text-slate-200">
      <div className="max-w-5xl mx-auto px-6 py-12">
        {/* Header */}
        <div className="text-center mb-12 animate-in fade-in slide-in-from-top-4 duration-1000">
          <div className="inline-flex items-center justify-center p-3 mb-4 rounded-2xl bg-blue-600/10 border border-blue-500/20 text-blue-400">
            <BookOpen size={32} />
          </div>
          <h1 className="text-5xl font-extrabold tracking-tight text-white mb-4 bg-clip-text text-transparent bg-gradient-to-r from-white via-white to-slate-400">
            Agentic AI Research Assistant
          </h1>
          <p className="text-slate-400 text-lg max-w-2xl mx-auto">
            Autonomous multi-stage pipeline that explores, retrieves, and synthesizes complex research topics into structured reports.
          </p>
        </div>

        {/* Search Area */}
        <div className="glass-morphism p-8 rounded-3xl border border-white/10 bg-white/5 backdrop-blur-xl shadow-2xl mb-12 animate-in fade-in zoom-in-95 duration-700">
          <form onSubmit={handleSearch} className="relative group">
            <input
              type="text"
              value={query}
              onChange={(e) => setQuery(e.target.value)}
              placeholder="Enter your research topic (e.g., 'Recent breakthroughs in CRIPSR')"
              className="w-full bg-slate-800/50 border border-slate-700 rounded-2xl py-5 px-6 pl-14 text-white placeholder-slate-500 focus:outline-none focus:ring-2 focus:ring-blue-500/50 transition-all duration-300 group-hover:border-slate-600 shadow-inner"
            />
            <div className="absolute left-5 top-1/2 -translate-y-1/2 text-slate-500 group-focus-within:text-blue-400 transition-colors">
              <Search size={22} />
            </div>
            <button
              type="submit"
              disabled={loading || !query.trim()}
              className="absolute right-3 top-1/2 -translate-y-1/2 bg-blue-600 hover:bg-blue-500 disabled:bg-slate-700 text-white px-8 py-3 rounded-xl font-semibold transition-all duration-300 flex items-center gap-2 shadow-lg shadow-blue-900/20 active:scale-95"
            >
              {loading ? (
                <>
                  <Loader2 className="animate-spin" size={20} />
                  Analyzing...
                </>
              ) : (
                'Generate Report'
              )}
            </button>
          </form>
        </div>

        {/* Error State */}
        {error && (
          <div className="mb-12 p-6 rounded-2xl bg-red-500/10 border border-red-500/20 text-red-400 flex items-center gap-4 animate-in fade-in slide-in-from-bottom-4">
            <AlertCircle className="shrink-0" />
            <p>{error}</p>
          </div>
        )}

        {/* Results Area */}
        {report && (
          <div className="space-y-8 animate-in fade-in slide-in-from-bottom-8 duration-1000">
            {/* Action Bar */}
            <div className="flex justify-between items-center gap-4">
              <h2 className="text-2xl font-bold text-white">Analysis Result</h2>
              <button
                onClick={handleDownload}
                className="flex items-center gap-2 bg-slate-800 hover:bg-slate-700 text-white px-6 py-2.5 rounded-xl border border-slate-700 transition-all active:scale-95"
              >
                <Download size={18} />
                Export PDF
              </button>
            </div>

            {/* Report Content */}
            <div className="glass-morphism rounded-3xl border border-white/10 bg-white/5 backdrop-blur-xl shadow-2xl overflow-hidden">
              <div className="p-8 border-b border-white/5 bg-gradient-to-r from-blue-600/10 to-purple-600/10">
                <h3 className="text-3xl font-bold text-white mb-4 leading-tight">{report.title}</h3>
                <div className="flex flex-wrap gap-3">
                   {report.sources?.slice(0, 3).map((url, i) => (
                     <span key={i} className="px-3 py-1 bg-slate-800/80 rounded-lg text-xs font-medium text-slate-400 border border-slate-700">
                        {new URL(url).hostname}
                     </span>
                   ))}
                </div>
              </div>
              
              <div className="p-8 space-y-10 prose prose-invert max-w-none">
                <section>
                  <h4 className="text-xl font-semibold text-blue-400 mb-4 flex items-center gap-2">
                    <span className="w-8 h-8 rounded-lg bg-blue-600/20 flex items-center justify-center text-blue-400 text-sm font-bold italic">A</span>
                    Abstract
                  </h4>
                  <div className="text-slate-300 leading-relaxed text-lg">
                    {report.abstract}
                  </div>
                </section>

                <section>
                  <h4 className="text-xl font-semibold text-blue-400 mb-4 flex items-center gap-2">
                    <span className="w-8 h-8 rounded-lg bg-blue-600/20 flex items-center justify-center text-blue-400 text-sm font-bold italic">F</span>
                    Key Findings
                  </h4>
                  <div className="text-slate-300 leading-relaxed space-y-4">
                    <ReactMarkdown>{report.key_findings}</ReactMarkdown>
                  </div>
                </section>

                <section>
                  <h4 className="text-xl font-semibold text-blue-400 mb-4 flex items-center gap-2">
                    <span className="w-8 h-8 rounded-lg bg-blue-600/20 flex items-center justify-center text-blue-400 text-sm font-bold italic">C</span>
                    Conclusion
                  </h4>
                  <div className="text-slate-300 leading-relaxed">
                    {report.conclusion}
                  </div>
                </section>

                <section>
                  <h4 className="text-xl font-semibold text-slate-400 mb-4">Sources</h4>
                  <div className="grid grid-cols-1 md:grid-cols-2 gap-3">
                    {report.sources?.map((url, i) => (
                      <a 
                        key={i} 
                        href={url} 
                        target="_blank" 
                        rel="noopener noreferrer"
                        className="flex items-center justify-between p-4 bg-slate-800/30 rounded-2xl border border-slate-700 hover:bg-slate-800/50 hover:border-slate-600 transition-all group"
                      >
                        <span className="text-sm text-slate-400 truncate mr-4">{url}</span>
                        <ExternalLink size={14} className="text-slate-600 group-hover:text-blue-400 shrink-0" />
                      </a>
                    ))}
                  </div>
                </section>
              </div>
            </div>
          </div>
        )}

        {/* Placeholder Step-by-Step UI (Hidden) */}
        {!report && !loading && (
           <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mt-12 opacity-50 grayscale hover:grayscale-0 transition-all duration-500 pointer-events-none">
              <div className="p-6 rounded-2xl border border-slate-700 bg-slate-800/20">
                <h5 className="font-semibold mb-2">1. Autonomous Search</h5>
                <p className="text-sm text-slate-500">Tavily API retrieves the most relevant academic and web sources.</p>
              </div>
              <div className="p-6 rounded-2xl border border-slate-700 bg-slate-800/20">
                <h5 className="font-semibold mb-2">2. Deep Reasoning</h5>
                <p className="text-sm text-slate-500">LangGraph nodes process, summarize and validate information chunks.</p>
              </div>
              <div className="p-6 rounded-2xl border border-slate-700 bg-slate-800/20">
                <h5 className="font-semibold mb-2">3. Synthesis</h5>
                <p className="text-sm text-slate-500">LLM combines verified data into a structured professional report.</p>
              </div>
           </div>
        )}
      </div>
    </div>
  );
}

export default App;
