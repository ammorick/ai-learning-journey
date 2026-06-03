 # 安全防护双专家问答系统（MVP）
Dual-Expert Q&A System with Security Protection

## 📌 项目简介
### 核心功能
用户发起提问 → 系统调度**双专家大脑**综合分析并生成回答 → 独立安全监测模块对**输入、输出内容**进行全链路关键词实时过滤。

### 设计初衷
2025年6月，我初次学习 Agent 相关课程。当时标准的 Agent 流程为：接收用户提问 → 交由大脑处理 → 调用工具 → 执行任务 → 生成结果 → 存入记忆并返回答案。
学习过程中我萌生了一个疑问：**为什么智能体不能拥有多个大脑？** 然后莫名其妙的思路突然全冒出来了。我认为这会是未来的方向，也因此下定决心落地这个项目。但受个人原因影响，项目一度中断，如今重新启动持续开发。

目前市面上多数多智能体项目更侧重功能实现，普遍忽略安全能力。在我看来，AI 的安全需求会随着模型能力增强同步提升。
本项目目标：
1. 实现**独立可插拔、可备份、无法被主逻辑绕过**的外置安全大脑；
2. 验证多大脑之间相互对话、协作的可行性；
3. 以 MVP 形式落地整套设计思路。

---

## 📅 开发进度（时间线）
> 记录从入门到项目搭建的完整过程
1. 2026-05-26：完成 AI 基础雏形搭建
2. 2026-05-28：除主程序外，完成对所有功能的模块化拆分。
3. 2026-05-30：优化专家大脑调度逻辑，由单大脑升级为多大脑；新增‘分化大脑’：负责接受任务，拆解任务，分发任务，收集答案。规划下一步构思。
4. 2026-06-02：增加记忆大脑，基础部分已完成，已成功生成记忆文件。目前在专家大脑阅读上文时发生错误。
5. 2026-06-03：记忆大脑功能修复，已实现上下文联系，回顾历史对话等功能。安全大脑微加强：增加输出过滤，敏感词文件，日志更新，白名单优先。
6. 持续任务：巩固 Python 基础（变量、循环、函数、字典、集合）；每日默写 Agent 逻辑，熟练掌握架构设计。

---

## 🚀 未来规划 Roadmap
### 短期（MVP 阶段）
1. 完成核心 MVP：打通双专家问答 + 关键词安全监测全流程

### 中期（功能拓展）
1. 搭建 Web 交互界面，方便功能演示与使用
2. 将安全监测模块拆分为独立进程，向微服务架构演进
3. 升级安全能力：接入小型模型，实现**语义级安全判断**（不止依赖关键词）

### 长期（标准化&国际化）
1. 搭建自更新安全规则库
2. 模型全部微服务化
3. 完成‘安全大脑’的自我检测，简单自我修复功能。

---

## 🛠️ 技术栈
### 当前使用
- Python 3.9+
- OpenAI API (gpt-4o-mini)

### 后续引入
- Flask（Web 服务）

---

## ▶️ 运行指南
待 MVP 开发完成后补充详细部署、启动步骤。

---

## 🙋 关于我
我是一个外卖员，目前每天12小时跑单+3小时左右的自学。一个零基础自学者，对AI系统架构和安全设计有强烈兴趣。代码很烂，愿景很大。欢迎围观，更欢迎嘲笑——嘲笑会让我跑的更快！
我相信‘安全’和AI应该是深度绑定的，并且真正的AI应该具备独立演化能力，这个项目是我从0到1的开端，也是我AI之路的起点
我始终相信，没有今天，是不会有明天的，只有拥有了今天，真正的明天才会到来！

如果你有任何建议、想法或讨论，都欢迎留言交流！

---


----------------------------------------------------------------------------------------------------------
# Dual-Expert Q&A System with Security Protection (MVP)

## 📌 Project Overview

### Core Features
User submits a question → the system dispatches **dual‑expert brains** for comprehensive analysis and response generation → an independent security monitoring module performs real‑time keyword‑based filtering on **both input and output** content.

### Design Motivation
In June 2025, I was first learning about Agent-related courses. The standard Agent workflow at that time was: receive user query → hand over to a single brain → decide which tools to invoke → execute tools → generate results → store in memory → return the answer.

While learning, a question popped into my head: **Why can’t an agent have multiple brains?** Then, out of nowhere, a stream of ideas surged. I felt this would be the future, and that’s why I decided to bring this project to life. Due to personal reasons, the project was put on hold, but now I have restarted development.

Most multi‑agent projects in the market focus on functionality but often overlook security capabilities. In my opinion, the demand for AI security grows as models become more powerful.

Goals of this project:
1. Build an **external safety brain** that is pluggable, backup‑friendly, and cannot be bypassed by the main logic.
2. Verify the feasibility of **multi‑brain dialogue and collaboration**.
3. Implement the entire design as an MVP.

---

## 📅 Development Progress (Timeline)

> From beginner to project building
1. 2026-05-26: Initial AI prototype completed.
2. 2026-05-28: Full modularisation (except the main program) achieved.
3. 2026-05-30: Upgraded expert dispatching logic from single‑brain to multi‑brain; added a “Distribution Brain” responsible for receiving tasks, breaking them down, dispatching them, and collecting answers. Next steps planned.
4. 2026-06-02: Implemented the Memory Brain with core functions finished; memory files can be generated successfully. Errors currently occur when Expert Brains attempt to load historical context.
5. 2026-06-03: Fixed functions of the Memory Brain; context association and historical dialogue review features are now available. Minor upgrades for the Safety Brain: output filtering, external sensitive word file, violation logging and whitelist priority added.
6. Ongoing: Reinforce Python basics (variables, loops, functions, dictionaries, sets); practice Agent logic daily to master the architecture design.

---

## 🚀 Future Roadmap

### Short‑term (MVP Phase)
1. Complete the core MVP: dual‑expert Q&A + keyword‑based security filtering.

### Mid‑term (Feature Expansion)
1. Build a Web interface for easy demonstration.
2. Split the security monitoring module into an independent process, evolving toward a microservices architecture.
3. Upgrade security capabilities: introduce a small model for **semantic‑level safety judgment** (beyond keywords).

### Long‑term (Standardisation & Internationalisation)
1. Build a self‑updating safety rule base.
2. Fully microservice‑oriented model.
3. Implement self‑checking and simple self‑repair capabilities for the Safety Brain.

---

## 🛠️ Tech Stack

### Current
- Python 3.9+
- OpenAI API (gpt-4o-mini)

### Future
- Flask (Web service)

---

## ▶️ How to Run

To be added after the MVP is completed.

---

## 🙋 About Me

I work as a food delivery rider, spending 12 hours on orders daily and roughly 3 hours on self-study.A self‑taught beginner with a strong interest in AI system architecture and security design. My code is messy, but my vision is huge. You are welcome to watch, and even more welcome to mock me – mockery will only make me run faster.

I believe **security** and **AI** should be deeply bound, and that true AI should be capable of independent evolution. This project is my start from 0 to 1, and the beginning of my AI journey.

I always believe that **without today, there will be no tomorrow**. Only by owning today can the real tomorrow arrive.

If you have any suggestions, ideas, or just want to discuss, feel free to reach out!
