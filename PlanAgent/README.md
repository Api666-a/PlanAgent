
# AI Agent Todo

一个基于 **AI Agent 思路** 的任务管理工具（CLI版本）。

## ✨ 特性
- 自动任务拆解（Task Planning Agent）
- 本地JSON持久化
- 模块化设计（Planner / CLI / Storage）
- 可扩展为多Agent系统

## 🧠 Agent架构
用户输入 → TaskPlanner → 子任务生成 → 状态管理

## 🚀 运行
```bash
python main.py
```

## 🔮 Future Work
- 接入 OpenAI API
- 多Agent协作（Planner + Executor）
- Web UI（Flask/React）
