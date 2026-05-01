# 自策（AutoPlanner）— 轻量级 AI 任务规划 Agent

> 一个基于 **AI Agent 思路** 的任务管理工具，让任务从“想法”自动变成“可执行步骤”。

---

## ✨ 项目简介

传统待办工具只能记录任务，但无法帮助用户拆解复杂目标。
**自策（AutoPlanner）** 引入 *Task Planning Agent*，能够对用户输入的抽象任务进行自动解析与结构化拆解，将目标转化为一系列可执行步骤。

该项目是一个轻量级的 AI Agent 实践，验证了“任务规划（Task Planning）”在生产力工具中的应用可行性。

---

## 🚀 核心特性

* 🧠 **任务自动拆解（Task Planning）**
  输入一句话目标，自动生成执行步骤

* 🤖 **Agent 架构设计**
  模拟 LLM 决策流程（Parsing → Planning → Execution）

* 🧩 **模块化结构**
  Agent / CLI / Storage 解耦，易于扩展

* 💾 **本地持久化**
  使用 JSON 实现轻量级状态管理

* 🔌 **可扩展 AI 能力**
  支持接入 OpenAI / 多 Agent 系统

---

## 🧠 系统架构

```text
用户输入
   ↓
TaskPlanner（Agent）
   ↓
子任务生成（Task Decomposition）
   ↓
任务存储（JSON）
   ↓
执行状态管理
```

该架构模拟了一个简化的 AI Agent Pipeline：

* **Parsing**：解析用户输入
* **Planning**：生成任务步骤
* **Execution Tracking**：记录执行状态

---

## 📦 项目结构

```text
.
├── main.py              # CLI入口
├── agent/
│   └── planner.py      # Task Planning Agent
├── tasks.json          # 本地任务存储
└── README.md
```

---

## ⚙️ 快速开始

### 1️⃣ 克隆项目

```bash
git clone https://github.com/your-username/auto-planner-agent.git
cd auto-planner-agent
```

### 2️⃣ 运行项目

```bash
python main.py
```

---

## 🧪 使用示例

输入：

```text
做一个网站
```

输出（自动拆解）：

```text
1. 需求分析
2. 设计页面结构
3. 前端开发
4. 后端开发
5. 部署上线
```

---

## 🧩 技术实现

* Python（CLI交互）
* JSON（数据持久化）
* Rule-based Planner（模拟 LLM 推理）
* 模块化 Agent 架构设计

---

## 🔮 Future Work

* 🔗 接入 OpenAI API（真实 LLM 规划能力）
* 🤖 多 Agent 协作（Planner + Executor + Memory）
* 🌐 Web UI（Flask / React）
* 📊 任务优先级与自动调度
* 🧠 引入长期记忆（Memory System）

---

## 💡 项目亮点

* 将传统 Todo 工具升级为 **具备初步 AI 能力的系统**
* 使用 **Agent 思维建模问题，而非简单功能堆叠**
* 具备清晰的扩展路径（可进化为完整 AI 工作流系统）

---

## 📄 License

MIT License

---

## ⭐ 如果这个项目对你有帮助

欢迎 Star ⭐ / Fork 🍴 支持一下！
