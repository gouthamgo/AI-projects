"use client";
import { useState } from "react";
import axios from "axios";
import { BarChart, Bar, XAxis, YAxis, Tooltip, ResponsiveContainer, PieChart, Pie, Cell } from "recharts";

export default function Home() {
  const [file, setFile] = useState(null);
  const [columnName, setColumnName] = useState("");
  const [insights, setInsights] = useState(null);
  const [error, setError] = useState("");

  const COLORS = ["#0088FE", "#FF8042", "#00C49F"];

  // Handle file selection
  const handleFileChange = (event) => {
    setFile(event.target.files[0]);
  };

  // Handle column name input
  const handleColumnChange = (event) => {
    setColumnName(event.target.value);
  };

  // Handle file upload
  const handleUpload = async () => {
    if (!file || !columnName) {
      setError("Please select a file and enter a column name.");
      return;
    }
    setError(""); // Reset error

    const formData = new FormData();
    formData.append("file", file);
    formData.append("column_name", columnName);

    try {
      const response = await axios.post("http://127.0.0.1:8000/upload-feedback/", formData, {
        headers: { "Content-Type": "multipart/form-data" },
      });
      setInsights(response.data.insights);
    } catch (err) {
      setError("Failed to process the file. Make sure the backend is running.");
    }
  };

  return (
    <div style={{ textAlign: "center", padding: "20px", fontFamily: "Arial, sans-serif" }}>
      <h1 style={{ color: "#333", fontSize: "2rem" }}>📊 Customer Feedback Analysis</h1>

      <input type="file" onChange={handleFileChange} style={{ margin: "10px" }} />
      <input type="text" placeholder="Enter column name" value={columnName} onChange={handleColumnChange} style={{ margin: "10px", padding: "5px" }} />
      <button onClick={handleUpload} style={{ padding: "10px", backgroundColor: "#007BFF", color: "white", border: "none", cursor: "pointer" }}>
        Upload & Analyze
      </button>

      {error && <p style={{ color: "red" }}>{error}</p>}

      {insights && (
        <div>
          <h2>Feedback Insights</h2>
          
          {/* Bar Chart */}
          <ResponsiveContainer width="80%" height={300}>
            <BarChart data={insights}>
              <XAxis dataKey="category" />
              <YAxis />
              <Tooltip />
              <Bar dataKey="count" fill="#8884d8" />
            </BarChart>
          </ResponsiveContainer>

          {/* Pie Chart */}
          <ResponsiveContainer width="50%" height={300}>
            <PieChart>
              <Pie data={insights} dataKey="count" nameKey="category" cx="50%" cy="50%" outerRadius={80} fill="#8884d8">
                {insights.map((entry, index) => (
                  <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
                ))}
              </Pie>
              <Tooltip />
            </PieChart>
          </ResponsiveContainer>
        </div>
      )}
    </div>
  );
}
