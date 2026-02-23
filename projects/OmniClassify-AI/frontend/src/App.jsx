import React, { useState } from 'react';
import {
    BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer, Cell
} from 'recharts';
import {
    Brain, Send, ShieldCheck, Zap, BarChart3, Info, Layers
} from 'lucide-react';

const MODELS = ["SVM", "Random Forest", "Naive Bayes"];
const ACCURACY_MAP = {
    "SVM": 0.92,
    "Random Forest": 0.89,
    "Naive Bayes": 0.84
};

export default function App() {
    const [text, setText] = useState('');
    const [selectedModel, setSelectedModel] = useState('SVM');
    const [loading, setLoading] = useState(false);
    const [results, setResults] = useState(null);

    const handleClassify = async () => {
        if (!text.trim()) return;
        setLoading(true);

        // Simulating API call to FastAPI
        setTimeout(() => {
            // Mocked response based on the 20-category project
            const mockResults = [
                { category: 'Sci.Space', probability: 0.842 },
                { category: 'Sci.Electronics', probability: 0.081 },
                { category: 'Comp.Graphics', probability: 0.042 },
                { category: 'Sci.Med', probability: 0.021 },
                { category: 'Sci.Crypt', probability: 0.014 },
            ];
            setResults(mockResults);
            setLoading(false);
        }, 800);
    };

    return (
        <div className="min-h-screen bg-slate-950 text-slate-100 font-sans p-8">
            {/* Header */}
            <header className="max-w-6xl mx-auto mb-12 flex justify-between items-center">
                <div>
                    <h1 className="text-3xl font-bold bg-gradient-to-r from-blue-400 to-emerald-400 bg-clip-text text-transparent">
                        OmniClassify AI
                    </h1>
                    <p className="text-slate-400">Semantic Benchmarking & 20-Category Inference Engine</p>
                </div>
                <div className="flex gap-4">
                    <div className="bg-slate-900 border border-slate-800 p-3 rounded-lg flex items-center gap-3">
                        <ShieldCheck className="text-emerald-500" size={20} />
                        <div>
                            <p className="text-xs text-slate-500 uppercase font-bold tracking-wider">Top Accuracy</p>
                            <p className="text-lg font-mono">{(ACCURACY_MAP[selectedModel] * 100).toFixed(1)}%</p>
                        </div>
                    </div>
                </div>
            </header>

            <main className="max-w-6xl mx-auto grid grid-cols-1 lg:grid-cols-12 gap-8">
                {/* Left Column: Input & Controls */}
                <div className="lg:col-span-7 space-y-6">
                    <div className="bg-slate-900 border border-slate-800 rounded-xl p-6 shadow-xl">
                        <label className="block text-sm font-medium text-slate-400 mb-4 flex items-center gap-2">
                            <Layers size={16} /> Select Model Arena
                        </label>
                        <div className="flex gap-2 mb-6">
                            {MODELS.map(m => (
                                <button
                                    key={m}
                                    onClick={() => setSelectedModel(m)}
                                    className={`px-4 py-2 rounded-md text-sm transition-all ${selectedModel === m
                                            ? 'bg-blue-600 text-white shadow-lg shadow-blue-900/40'
                                            : 'bg-slate-800 text-slate-400 hover:bg-slate-700'
                                        }`}
                                >
                                    {m}
                                </button>
                            ))}
                        </div>

                        <textarea
                            className="w-full h-64 bg-slate-950 border border-slate-800 rounded-lg p-4 text-slate-300 focus:ring-2 focus:ring-blue-500 focus:outline-none transition-all placeholder:text-slate-700"
                            placeholder="Paste raw text here for semantic analysis..."
                            value={text}
                            onChange={(e) => setText(e.target.value)}
                        />

                        <button
                            onClick={handleClassify}
                            disabled={loading || !text}
                            className="mt-4 w-full bg-gradient-to-r from-blue-600 to-blue-700 hover:from-blue-500 hover:to-blue-600 disabled:opacity-50 text-white font-bold py-3 rounded-lg flex items-center justify-center gap-2 transition-all shadow-xl shadow-blue-900/20"
                        >
                            {loading ? "Processing Engine..." : <><Send size={18} /> Classify Text</>}
                        </button>
                    </div>

                    <div className="bg-slate-900/50 border border-slate-800 rounded-xl p-4 flex items-start gap-4 text-sm text-slate-400">
                        <Info className="text-blue-400 shrink-0" size={20} />
                        <p>This model was trained on the 20-Newsgroups dataset, featuring 18,000+ posts across 20 distinct categories. Cross-model benchmarking ensures optimal F1-scores for varied semantic inputs.</p>
                    </div>
                </div>

                {/* Right Column: Analytics */}
                <div className="lg:col-span-5 space-y-6">
                    <div className="bg-slate-900 border border-slate-800 rounded-xl p-6 shadow-xl h-full">
                        <h2 className="text-lg font-bold mb-6 flex items-center gap-2 text-slate-300">
                            <BarChart3 size={20} className="text-emerald-400" /> Probability Distribution
                        </h2>

                        {!results ? (
                            <div className="h-64 flex flex-col items-center justify-center text-slate-600 border-2 border-dashed border-slate-800 rounded-lg">
                                <Brain size={48} className="mb-4 opacity-20" />
                                <p>Awaiting input for inference...</p>
                            </div>
                        ) : (
                            <div className="space-y-8 animate-in fade-in slide-in-from-right-4 duration-500">
                                <div className="h-64 w-full">
                                    <ResponsiveContainer width="100%" height="100%">
                                        <BarChart data={results} layout="vertical">
                                            <CartesianGrid strokeDasharray="3 3" stroke="#1e293b" horizontal={false} />
                                            <XAxis type="number" hide />
                                            <YAxis
                                                dataKey="category"
                                                type="category"
                                                width={100}
                                                tick={{ fill: '#94a3b8', fontSize: 12 }}
                                                axisLine={false}
                                                tickLine={false}
                                            />
                                            <Tooltip
                                                cursor={{ fill: '#1e293b' }}
                                                contentStyle={{ backgroundColor: '#0f172a', border: '1px solid #334155', borderRadius: '8px' }}
                                            />
                                            <Bar dataKey="probability" radius={[0, 4, 4, 0]}>
                                                {results.map((entry, index) => (
                                                    <Cell key={`cell-${index}`} fill={index === 0 ? '#3b82f6' : '#1e293b'} />
                                                ))}
                                            </Bar>
                                        </BarChart>
                                    </ResponsiveContainer>
                                </div>

                                <div className="pt-6 border-t border-slate-800">
                                    <h3 className="text-sm font-bold text-slate-500 uppercase mb-4">Inference Summary</h3>
                                    <div className="space-y-3">
                                        <div className="flex justify-between items-center">
                                            <span className="text-slate-400 text-sm">Top Categorisation</span>
                                            <span className="bg-blue-500/10 text-blue-400 px-2 py-1 rounded text-xs font-bold">{results[0].category}</span>
                                        </div>
                                        <div className="flex justify-between items-center">
                                            <span className="text-slate-400 text-sm">Confidence Level</span>
                                            <span className="text-emerald-400 font-mono">{(results[0].probability * 100).toFixed(1)}%</span>
                                        </div>
                                        <div className="flex justify-between items-center">
                                            <span className="text-slate-400 text-sm">Latent Variance</span>
                                            <span className="text-slate-300 font-mono">Low</span>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        )}
                    </div>
                </div>
            </main>
        </div>
    );
}
