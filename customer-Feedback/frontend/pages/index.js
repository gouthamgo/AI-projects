"use client";
import { useState } from "react";
import axios from "axios";
import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer,
  PieChart,
  Pie,
  Cell,
  Legend,
} from "recharts";
import { motion } from "framer-motion";

export default function Home() {
  const [file, setFile] = useState(null);
  const [columns, setColumns] = useState([]);
  const [selectedColumn, setSelectedColumn] = useState("");
  const [insights, setInsights] = useState(null);
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  const COLORS = ["#3B82F6", "#F97316", "#10B981", "#FBBF24", "#6B7280"];

  const handleFileChange = async (event) => {
    const selectedFile = event.target.files[0];
    console.log("Selected file:", selectedFile);
    setFile(selectedFile);
    setError("");
    if (selectedFile && selectedFile.type === "text/csv") {
      const text = await selectedFile.text();
      const firstLine = text.split("\n")[0];
      const columnNames = firstLine.split(",").map((col) => col.trim());
      console.log("Columns detected:", columnNames);
      setColumns(columnNames);
      setSelectedColumn(columnNames[0] || "");
    } else {
      setError("Please upload a valid CSV file.");
    }
  };

  const handleColumnChange = (event) => {
    console.log("Selected column:", event.target.value);
    setSelectedColumn(event.target.value);
  };

  const handleUpload = async () => {
    if (!file || !selectedColumn) {
      setError("Please upload a file and select a column.");
      return;
    }
    setError("");
    setLoading(true);
    console.log("Uploading file:", file.name, "Column:", selectedColumn);

    const formData = new FormData();
    formData.append("file", file);
    formData.append("column_name", selectedColumn);

    try {
      const response = await axios.post("http://127.0.0.1:8000/upload-feedback/", formData, {
        headers: { "Content-Type": "multipart/form-data" },
        timeout: 10000,
      });
      console.log("Response received:", response.data);
      setInsights(response.data.insights);
    } catch (err) {
      console.error("Upload error:", err);
      setError(err.code === "ECONNABORTED" ? "Request timed out. Try a smaller file." : err.response?.data?.detail || "Failed to process the file.");
    } finally {
      setLoading(false);
    }
  };

  const chartVariants = {
    hidden: { opacity: 0, y: 20 },
    visible: { opacity: 1, y: 0, transition: { duration: 0.8, ease: "easeInOut" } },
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-teal-100 via-blue-100 to-indigo-100 flex flex-col justify-between">
      {/* Hero Section */}
      <motion.div
        initial={{ opacity: 0, y: -50 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.8 }}
        className="w-full bg-gradient-to-r from-blue-600 to-indigo-600 text-white py-16 px-6 text-center rounded-b-3xl shadow-lg"
      >
        <h1 className="text-5xl font-extrabold flex justify-center items-center gap-3 mb-4">
          <span className="text-5xl">📊</span> Customer Feedback Analyzer
        </h1>
        <p className="text-xl max-w-2xl mx-auto opacity-90">
          Transform your customer feedback into actionable insights with a single upload.
        </p>
      </motion.div>

      {/* Main Content */}
      <main className="flex-grow w-full max-w-4xl px-6">
        <motion.div
          initial={{ opacity: 0, scale: 0.95 }}
          animate={{ opacity: 1, scale: 1 }}
          transition={{ duration: 0.5, delay: 0.2 }}
          className="bg-white rounded-xl shadow-xl p-6 -mt-12 z-10"
        >
          <div className="flex flex-col sm:flex-row items-center justify-center gap-4">
            <label className="w-full sm:w-auto flex items-center space-x-2">
              <input
                type="file"
                accept=".csv"
                onChange={handleFileChange}
                className="hidden"
              />
              <span className="inline-block px-4 py-2 bg-blue-50 text-blue-700 font-semibold rounded-md cursor-pointer hover:bg-blue-100 transition-colors shadow-sm">
                Choose CSV
              </span>
              <span className="text-gray-500 truncate max-w-xs text-center flex-grow">
                {file ? file.name : "No file chosen"}
              </span>
            </label>
            <select
              value={selectedColumn}
              onChange={handleColumnChange}
              disabled={!columns.length}
              className="w-full sm:w-48 p-2 border-2 border-gray-300 bg-white rounded-md focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-colors shadow-sm text-gray-700"
            >
              <option value="" className="text-gray-400">
                Select a column
              </option>
              {columns.map((col) => (
                <option key={col} value={col} className="text-gray-700">
                  {col}
                </option>
              ))}
            </select>
            <button
              onClick={handleUpload}
              disabled={loading}
              className={`px-4 py-2 rounded-md text-white font-semibold transition-all duration-300 flex items-center justify-center gap-2 shadow-md ${
                loading ? "bg-gray-400 cursor-not-allowed" : "bg-gradient-to-r from-blue-600 to-indigo-600 hover:from-blue-700 hover:to-indigo-700"
              }`}
            >
              {loading && (
                <svg
                  className="animate-spin h-4 w-4 text-white"
                  xmlns="http://www.w3.org/2000/svg"
                  fill="none"
                  viewBox="0 0 24 24"
                >
                  <circle
                    className="opacity-25"
                    cx="12"
                    cy="12"
                    r="10"
                    stroke="currentColor"
                    strokeWidth="4"
                  ></circle>
                  <path
                    className="opacity-75"
                    fill="currentColor"
                    d="M4 12a8 8 0 018-8v8H4z"
                  ></path>
                </svg>
              )}
              {loading ? "Analyzing..." : "Upload & Analyze"}
            </button>
          </div>

          {error && (
            <motion.p
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              className="text-red-500 mt-4 text-center"
            >
              {error}
            </motion.p>
          )}
        </motion.div>

        {/* Insights Section */}
        {insights && (
          <div className="mt-8 p-6">
            <motion.div
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              className="space-y-12"
            >
              <h2 className="text-3xl font-semibold text-gray-800 text-center">
                Feedback Insights
              </h2>

              <motion.div variants={chartVariants} initial="hidden" animate="visible">
                <h3 className="text-xl font-medium text-gray-700 mb-4 text-center">
                  Sentiment Distribution
                </h3>
                <ResponsiveContainer width="100%" height={300}>
                  <BarChart data={insights.sentiment_distribution}>
                    <XAxis dataKey="category" stroke="#6B7280" fontSize={14} />
                    <YAxis stroke="#6B7280" fontSize={14} />
                    <Tooltip
                      contentStyle={{
                        backgroundColor: "#fff",
                        borderRadius: "8px",
                        boxShadow: "0 2px 5px rgba(0,0,0,0.1)",
                        border: "none",
                      }}
                    />
                    <Bar dataKey="count" fill="#3B82F6" animationDuration={1000} />
                  </BarChart>
                </ResponsiveContainer>
              </motion.div>

              <motion.div variants={chartVariants} initial="hidden" animate="visible">
                <h3 className="text-xl font-medium text-gray-700 mb-4 text-center">
                  Detailed Feedback Categories
                </h3>
                <ResponsiveContainer width="100%" height={300}>
                  <PieChart>
                    <Pie
                      data={insights.detailed_categories}
                      dataKey="count"
                      nameKey="category"
                      cx="50%"
                      cy="50%"
                      outerRadius={100}
                      animationDuration={800}
                      label={({ name, percent }) =>
                        `${name} (${(percent * 100).toFixed(0)}%)`
                      }
                    >
                      {insights.detailed_categories.map((entry, index) => (
                        <Cell
                          key={`cell-${index}`}
                          fill={COLORS[index % COLORS.length]}
                        />
                      ))}
                    </Pie>
                    <Tooltip
                      contentStyle={{
                        backgroundColor: "#fff",
                        borderRadius: "8px",
                        boxShadow: "0 2px 5px rgba(0,0,0,0.1)",
                        border: "none",
                      }}
                    />
                    <Legend verticalAlign="bottom" height={36} />
                  </PieChart>
                </ResponsiveContainer>
              </motion.div>

              <motion.div variants={chartVariants} initial="hidden" animate="visible">
                <h3 className="text-xl font-medium text-gray-700 mb-4 text-center">
                  Top Words in Feedback
                </h3>
                <ResponsiveContainer width="100%" height={300}>
                  <BarChart data={insights.top_words}>
                    <XAxis dataKey="word" stroke="#6B7280" fontSize={14} />
                    <YAxis stroke="#6B7280" fontSize={14} />
                    <Tooltip
                      contentStyle={{
                        backgroundColor: "#fff",
                        borderRadius: "8px",
                        boxShadow: "0 2px 5px rgba(0,0,0,0.1)",
                        border: "none",
                      }}
                    />
                    <Bar dataKey="count" fill="#10B981" animationDuration={1000} />
                  </BarChart>
                </ResponsiveContainer>
              </motion.div>

              <motion.div
                variants={chartVariants}
                initial="hidden"
                animate="visible"
                className="text-center"
              >
                <h3 className="text-xl font-medium text-gray-700 mb-2">
                  Average Feedback Length
                </h3>
                <p className="text-3xl font-bold text-blue-600">
                  {insights.average_length}{" "}
                  <span className="text-lg font-normal text-gray-600">characters</span>
                </p>
              </motion.div>
            </motion.div>
          </div>
        )}
      </main>

      {/* Footer */}
      <footer className="w-full py-4 text-center text-gray-500 text-sm bg-white border-t border-gray-200">
        Built with ❤️ by Goutham | Powered by Next.js & FastAPI
      </footer>
    </div>
  );
}