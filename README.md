 安全防护双专家问答系统（MVP）

## 这个项目是什么？
功能：用户提问 → 系统调用两个专家（比如医学、法律）综合后回答 → 同时一个独立的安全监测模块对输入/输出进行实时过滤（基于关键词）。

## 为什么做这个？
2025年6月我第一次接触Agent课程，脑子里冒出一些奇怪的想法——我觉得那就是未来。加上兴趣使然，便打算慢慢做。当时因个人原因没能持续，如今终于可以开始了。

市面上的多智能体偏向“功能”，很少考虑“安全”。所以我希望设计一个‘外置安全大脑’：独立运行、不被主逻辑绕过、可插拔、可备份。这个MVP就是该思路的验证。

## 当前进展（2026-05-23）
1.Python学习（变量、循环、函数、字典、集合）

## 未来计划
1. 完成MVP（安全监测 + 双专家）
2. 增加Web界面，方便演示
3. 将安全监测拆分为独立进程（微服务）
4. 引入语义级安全判断（小型模型）
5. 多语言规则库 + UTF-8规范化

## 技术栈
- Python 3.9+
- OpenAI API（gpt-4o-mini）
- （后续：Flask、Unicode规范化）

## 如何运行？
（待补充，完成MVP后写）

## 关于我
一个零基础自学者，对AI系统架构和安全设计有强烈兴趣。代码很烂，愿景很大。欢迎围观，更欢迎嘲笑——嘲笑会让我跑的更快！
我相信‘安全’和AI应该是深度绑定的，并且真正的AI应该具备独立演化能力，这个项目是我从0到1的开端，也是我AI之路的起点
我始终相信，没有今天，是不会有明天的，只有拥有了今天，真正的明天才会到来！

欢迎任何建议或讨论。# ai-learning-journey

----------------------------------------------------------------------------------------------------------
# Secure Dual-Expert Q&A System (MVP)

## What is this project?
User asks a question → The system calls two expert modules (e.g., medical, legal) and synthesizes their answers → Meanwhile, an independent safety monitoring module filters the input/output in real time (keyword-based).

## Why build this?
In June 2025, I was first exposed to an Agent course, and some strange ideas popped into my head — I felt that they were the future. Driven by interest, I decided to slowly work on this project. Due to personal reasons, I couldn’t continue at that time, but now I can finally start.

Most multi-agent frameworks focus on “functionality” and rarely consider “safety”. Therefore, I want to design an **external safety brain**: independent, cannot be bypassed by the main logic, pluggable, and backup-friendly. This MVP is the verification of that idea.

## Current Progress (2026-05-23)
1. Python basics learned (variables, loops, functions, dicts, sets)

## Future Plans
1. Complete MVP (safety monitoring + dual experts)
2. Add a web interface for easy demonstration
3. Separate safety monitoring into an independent process (microservice)
4. Introduce semantic-level safety judgment (small model)
5. Multi-language rule base + UTF-8 normalization

## Tech Stack
- Python 3.9+
- OpenAI API (gpt-4o-mini)
- (Future: Flask, Unicode normalization)

## How to run?
(To be added after MVP completion)

## About Me
A self‑taught beginner with strong interest in AI system architecture and safety design. My code is messy, but my vision is big. Welcome to watch, and even more welcome to mock — mockery will only make me run faster!

I believe that “safety” and AI should be deeply bound, and that true AI should be capable of independent evolution. This project is my start from 0 to 1, and the beginning of my AI journey.

I always believe that without today, there will be no tomorrow. Only when we have today can the real tomorrow arrive.

Any suggestions or discussions are welcome.
