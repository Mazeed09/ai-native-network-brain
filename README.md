# Metel AI Core — The Brain of 6G Networks

**Metel AI Core** is an AI-driven network intelligence system designed to **monitor, analyze, and optimize 6G networks**.  
This project simulates network metrics, labels network states, generates AI reasoning insights, and visualizes the data — all in a **single end-to-end workflow**.

---

## **Features**

1. **Network Simulation**
   - Generates realistic network metrics: `latency`, `packet_loss`, `throughput`, `jitter`
   - Produces a CSV file (`data/network_metrics.csv`) for analysis

2. **State Analysis**
   - Labels each network snapshot as:
     - `healthy`
     - `warning`
     - `degraded`
   - Thresholds are adjustable for demonstration or real-world use

3. **AI Reasoning**
   - Provides insights and optimization suggestions per network state
   - Supports:
     - **OpenAI GPT API** (if key available)  
     - **Mock reasoning** (for free/demo mode)

4. **Visualizations**
   - Time-series graphs of metrics
   - Network state distribution charts
   - Fully interactive in Google Colab

---

Copy_of_AI_Native_Network_Brain.ipynb

## **Getting Started**

### **1. Run in Google Colab**
1. Open the notebook: `Metel_AI_Core.ipynb`
2. Run all cells in order  
   - The simulation generates `network_metrics.csv`
   - AI reasoning will provide insights (mock/API)
   - Visualizations will appear at the end

### **2. Dependencies**
- Python 3.12+
- Libraries: `pandas`, `matplotlib`, `seaborn`, `openai` (optional), `gpt4all` (optional)

---

## **Example Output**

| Timestamp     | Latency | Packet Loss | Throughput | Jitter | State    | AI Reasoning                         |
|---------------|--------|------------|-----------|--------|----------|-------------------------------------|
| 1767241286    | 79.24  | 0.27       | 595.55    | 27.33  | healthy  | Network is healthy. No action needed|
| 1767241287    | 196.07 | 2.04       | 588.00    | 14.30  | warning  | Network warning. Monitor latency     |
| 1767241288    | 525.38 | 0.56       | 541.15    | 25.99  | degraded | Network degraded. Consider rerouting |

*(Graphs and AI insights are interactive in Colab)*

---

## **How to Contribute**

- Fork the repo and submit PRs for:
  - New visualization styles
  - Improved AI reasoning
  - Real-time network data integration

---

## **About Metel Inc**

Metel AI Core is part of **Metel Inc’s next-gen 6G AI research**, focused on **autonomous network intelligence**.  
This prototype demonstrates **AI-driven network monitoring, state analysis, and optimization** — bridging simulation and practical insights.

---

## **License**

MIT License — free to use, modify, and share.

©️ 2026 Metel_Inc 