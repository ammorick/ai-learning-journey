Multi-Expert Q&A System is a Python-based modular AI dialogue framework. It distributes user questions to multiple domain-specific expert LLMs for parallel reasoning, records full conversation history, filters risky sensitive content via an independent safety module, and unifies scattered expert responses into a complete final answer through a dedicated supervisor aggregator. It supports docking with multiple mainstream large-model service APIs.
✨ Core Features
🧠 Parallel Multi-Expert Inference
Dispatch user queries to medical and legal expert modules concurrently powered by ThreadPoolExecutor to realize parallel multi-source reasoning and accelerate response generation.
🔐 Independent Safety Brain Module
Implements configurable blacklist & whitelist keyword filtering mechanism; automatically logs all input/output content that violates safety rules for subsequent review.
📝 Persistent Conversation Memory
JSON-based local persistent storage for dialogue context, automatically retains the latest 20 rounds of chat history to maintain continuous conversation logic.
🎯 Supervisor Aggregation Brain
Collect raw reply content from all independent expert agents, eliminate redundant information and synthesize a coherent, integrated final answer for end users.
🌍 Dual Large-Model API Compatibility
Native supports two mainstream LLM service vendors: Zhipu AI (GLM-4.5-air) and Alibaba Cloud DashScope (Qwen-Turbo), with encapsulated unified API request adapter.
🚀 Quick Start Guide
Prerequisites
Python 3.9 or higher version installed in local environment
Valid API keys applied from official platforms:
Zhipu AI Open Platform: https://open.bigmodel.cn/
Alibaba Cloud DashScope: https://dashscope.aliyun.com/
Step 1: Install Project & Dependencies
bash
运行
# Clone source code from repository
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name

# Install all required third-party packages
pip install -r requirements.txt
Step 2: Environment Configuration
Copy the template environment file and fill in your personal API credentials:
bash
运行
cp .env.example .env
Edit .env file and write your valid API keys:
env
ZHIPU_API_KEY=your_zhipu_official_api_key_here
ALIYUN_API_KEY=your_aliyun_dashscope_api_key_here
Step 3: Launch the System
bash
运行
python main.py
💡 Running Example
plaintext
User Input: I have a cold, but my company refused to approve my sick leave application.

[Medical Expert Output]: Suggest adequate rest and apply for an official medical certificate from qualified hospital.
[Legal Expert Output]: Interpret relevant local labor protection regulations about statutory sick leave rights and enterprise obligation.
[Supervisor Final Reply]: Combined with medical advice and labor law provisions, you can get a formal doctor's diagnosis certificate first, then negotiate with the company based on legal sick leave regulations if unreasonable rejection persists.
📁 Project Directory Structure
plaintext
.
├── main.py               # Program entry & main runtime logic
├── dispatcher.py         # Task dispatcher: route user question & launch parallel expert calls
├── summarizer.py         # Supervisor core: aggregate multi-expert replies into final answer
├── safe.py               # Safety Brain core implementation, keyword content filtering
├── memory.py             # Conversation memory module, JSON persistent read/write logic
├── safety_logger.py      # Rule violation log collector, save abnormal input/output records
├── api1.py               # Unified API wrapper for Zhipu AI & Aliyun DashScope request
├── test-memory.py        # Independent test script for memory module verification
├── .env.example          # Environment variable configuration template
├── requirements.txt      # Project dependent packages list
├── safety_rules.json     # Editable safety config: custom blacklist & whitelist keywords
└── logs/                 # Auto-generated directory for all safety violation log files
🗺️ Future Development Roadmap
Semantic Query Routing: Replace simple keyword matching with embedding-based text classification to intelligently assign questions to matching expert agents automatically.
Expand Expert Ecosystem: Add more domain expert modules including Finance, Mechanical Engineering, General Knowledge consultation.
External Independent Safety Microservice: Split safety brain into an independent hot-pluggable microservice for decoupled deployment and real-time monitoring.
Frontend Web Demo: Build interactive web UI based on Streamlit for visual operation and quick project demonstration.
Vector Database Memory Upgrade: Migrate original JSON file storage to vector database to realize long-term ultra-large context memory retrieval.
🤝 Contribution Guide
Issues and Pull Requests are warmly welcome!
If you have optimization ideas about safety rules, new domain expert development or concurrency performance improvement, please create an Issue to discuss your proposal before submitting formal code modification.
📜 License
This open-source project is released under the MIT License.