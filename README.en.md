# Multi-Expert Q&A System

![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)
![Status](https://img.shields.io/badge/status-active--development-yellow)
![License](https://img.shields.io/badge/license-MIT-green.svg)

> ⚠️ **Work in Progress** – This project is evolving. Current version is a functional MVP with two expert brains and basic safety/memory. More features coming.

A Python AI assistant that calls multiple expert brains (medical, legal) in parallel, remembers conversation history, filters sensitive content, and summarizes answers.

## ✨ Features

- 🧠 **Multi-expert parallel** – Invokes medical & legal experts simultaneously using `ThreadPoolExecutor`
- 🔐 **Safety brain** – Keyword black/whitelist with violation logging (input & output)
- 📝 **Memory module** – Persistent conversation history (JSON-based, last 20 turns)
- 🎯 **Supervisor brain** – Aggregates multiple expert answers into one final response
- 🌍 **Multi-API support** – Works with Zhipu AI (GLM-4.5-air) and Aliyun DashScope (Qwen-Turbo)

## 🚀 Quick Start

### Prerequisites

- Python 3.9+
- API keys from [Zhipu AI](https://open.bigmodel.cn/) and/or [Aliyun DashScope](https://dashscope.aliyun.com/)

### Installation

```bash
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
pip install -r requirements.txt
```

### Configuration
1.Copy .env.example to .env
2.Fill in your API keys:
```env
ZHIPU_API_KEY=your_zhipu_key_here
ALIYUN_API_KEY=your_aliyun_key_here

```

### Run
```bash
python main.py
```

### Example
```text
User: I have a cold, but my company denied my sick leave.

[Medical expert] recommends rest and medical certificate.
[Legal expert] explains local labor laws about sick leave.
Supervisor: Combines both, suggests doctor's note + legal rights.
```
## 📁 Project Structure
```text
.
├── main.py               # Entry point
├── dispatcher.py         # Routes question to experts, parallel calls
├── summarizer.py         # Aggregates expert answers
├── safe.py               # Safety brain (keyword filter)
├── memory.py             # Conversation memory (JSON)
├── safety_logger.py      # Logs violations
├── api1.py               # Unified API caller for Zhipu/Aliyun
├── test-memory.py        # Memory module test script
├── .env.example          # Environment variables template
├── requirements.txt      # Dependencies
├── safety_rules.json     # Blacklist/whitelist (editable)
└── logs/                 # Safety log directory
```
## 🗺️ Roadmap
Semantic routing – Replace keyword matching with embedding-based classification
More expert brains – Finance, engineering, general knowledge
External safety microservice – Hot‑pluggable, independent monitoring
Web interface – Deploy with Streamlit for easy demo
Vector memory – Use vector DB for long‑term context

## 🤝 Contributing
Issues and pull requests are welcome! If you have ideas for improving safety, adding experts, or optimizing concurrency, feel free to open an issue first.