# 多专家问答系统

![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)
![状态](https://img.shields.io/badge/status-开发中-yellow)
![许可证](https://img.shields.io/badge/license-MIT-green.svg)

> ⚠️ **持续开发中** – 本项目正在演进。当前版本为功能性 MVP，包含两个专家大脑及基础安全/记忆功能。更多特性即将到来。

一个 Python AI 助手，能并行调用多个专家大脑（医学、法律），记住对话历史，过滤敏感内容，并汇总答案。

## ✨ 特性

- 🧠 **多专家并行** – 使用 `ThreadPoolExecutor` 同时调用医学和法律专家
- 🔐 **安全大脑** – 关键词黑白名单 + 违规日志（输入和输出）
- 📝 **记忆模块** – 持久化对话历史（基于 JSON，保留最近 20 轮）
- 🎯 **总监大脑** – 将多个专家的答案汇总为最终回复
- 🌍 **多 API 支持** – 支持智谱 AI (GLM-4.5-air) 和阿里云 DashScope (Qwen-Turbo)

## 🚀 快速开始

### 环境要求

- Python 3.9+
- 来自 [智谱 AI](https://open.bigmodel.cn/) 和/或 [阿里云 DashScope](https://dashscope.aliyun.com/) 的 API 密钥

### 安装

```bash
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
pip install -r requirements.txt
```
### 配置
1.复制 .env.example 为 .env
2.填入你的 API 密钥：
```env
ZHIPU_API_KEY=你的智谱API密钥
ALIYUN_API_KEY=你的阿里云API密钥
```
### 运行
```bash
python main.py
```
### 示例
```text
用户：我感冒了，但公司不批我的病假。

[医学专家] 建议休息并开具医疗证明。
[法律专家] 解释当地劳动法关于病假的规定。
总监：综合两者建议，提供医生证明 + 法律权利说明。
```

## 📁 项目结构
```text
.
├── main.py               # 入口文件
├── dispatcher.py         # 路由问题到专家，并行调用
├── summarizer.py         # 汇总专家答案
├── safe.py               # 安全大脑（关键词过滤）
├── memory.py             # 对话记忆（JSON）
├── safety_logger.py      # 违规日志
├── api1.py               # 统一的智谱/阿里云 API 调用器
├── test-memory.py        # 记忆模块测试脚本
├── .env.example          # 环境变量模板
├── requirements.txt      # 依赖列表
├── safety_rules.json     # 黑白名单（可编辑）
└── logs/                 # 安全日志目录
```

## 🗺️ 路线图
语义路由 – 用嵌入分类替换关键词匹配
更多专家大脑 – 金融、工程、通用知识等
外部安全微服务 – 热插拔、独立监控
Web 界面 – 使用 Streamlit 部署方便演示
向量记忆 – 使用向量数据库实现长期上下文

### 🤝 贡献
欢迎提交 Issue 和 Pull Request！如果你有改进安全、增加专家或优化并发的想法，请先开一个 Issue 讨论。