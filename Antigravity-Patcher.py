# coding: utf-8
import os
import json
import struct
import subprocess

APP_DIR = os.path.join(os.getenv('LOCALAPPDATA'), 'Programs', 'antigravity')
RESOURCES_DIR = os.path.join(APP_DIR, "resources")
ASAR_PATH = os.path.join(RESOURCES_DIR, "app.asar")
UNPACKED_APP_DIR = os.path.join(RESOURCES_DIR, "app")

DOM_TRANSLATOR_INJECTION = r"""
// Antigravity Chinese Localization Engine
(function() {
  const dictionary = {
    // Top Bar & Global Navigation
    "Goals": "目标", "Tasks": "任务", "Artifacts": "工件", "Scratch": "草稿", "Chat": "对话",
    "Active": "进行中", "Inactive": "未激活", "Completed": "已完成", "Failed": "已失败",
    "History": "历史记录", "Settings": "设置", "System": "系统", "Network": "网络",
    "Model": "模型", "Memory": "记忆", "Tools": "工具", "Agents": "智能体",
    "Overview": "概览", "Logs": "日志", "Clear": "清除", "Save": "保存",
    "Cancel": "取消", "Submit": "提交", "Run": "运行", "Stop": "停止",
    "Edit": "编辑", "Delete": "删除", "Add": "添加", "Remove": "移除", "Download": "下载",
    "Monthly Limit": "每月限额", "Weekly Limit": "每周限额", "Five Hour Limit": "五小时限额",
    "Weekly Limit Remaining": "每周限额剩余", "Five Hour Limit Remaining": "五小时限额剩余",
    "limit": "限额", "limits": "限额", "weekly": "每周", "hourly": "每小时",
    "Sidebar": "侧边栏", "Display Options": "显示选项", "Message input": "消息输入框", "Record voice memo": "录制语音备忘",
    "Typeahead menu": "预输入菜单", "Group By": "分组方式", "Last Updated": "最后更新",
    "Alphabetical (A-Z)": "字母顺序 (A-Z)", "Date Added": "添加日期", "Subtitles": "副标题", "No Subtitle": "无副标题",
    "Filter": "筛选", "Scheduled": "已计划", "Environment": "环境", "None": "无", "Fast": "快速",
    "Project": "项目", "project": "项目", "projects": "项目", "Conversation": "对话", "conversation": "对话",
    "Workspace": "工作区", "workspace": "工作区", "Minimize": "最小化", "Maximize": "最大化", "Back": "返回",
    "Folders": "文件夹", "folders": "文件夹", "Folder": "文件夹", "folder": "文件夹", "including": "包括",
    "Add Folder": "添加文件夹", "+ Add Folder": "+ 添加文件夹", "Add folder": "添加文件夹", "+ Add folder": "+ 添加文件夹",
    "Project Folders": "项目文件夹", "Project folders": "项目文件夹",
    "Manage project folders, agent settings, and permissions.": "管理项目文件夹、智能体设置和权限。",
    "Manage project folders, agent settings, and permissions": "管理项目文件夹、智能体设置和权限。",
    "Rename": "重命名", "Mark Unread": "标记为未读", "Mark Read": "标记为已读", "Duplicate": "制作副本",
    "Export": "导出", "Import": "导入", "Pin": "置顶", "Archive": "归档",
    "Create New Project": "创建新项目", "Archive Conversation": "归档对话", "now": "刚刚",
    "Conversation Name": "对话名称", "Conversation ID": "对话 ID", "Project Name": "项目名称",
    "Toggle Auxiliary Pane": "切换辅助面板", "User cancelled agent execution.": "用户取消了智能体执行。",
    "Open Antigravity IDE": "打开 Antigravity IDE", "Create Project": "创建项目", 
    "Command Palette": "命令面板", "Zoom In": "放大", "Zoom Out": "缩小", "Reset Zoom": "重置缩放",
    "Delete Conversation": "删除对话", "Are you sure you want to delete this conversation? This action cannot be undone.": "您确定要删除此对话吗？此操作无法撤销。",
    "Are you sure you want to delete the project": "您确定要删除项目",
    "Are you sure you want to delete the": "您确定要删除",
    "Are you sure you want to delete": "您确定要删除",
    "This will permanently delete": "这将永久删除包含在其中的",
    "within it.": "", "within it": "",
    "This action cannot be undone.": "此操作无法撤销。", "This action cannot be undone": "此操作无法撤销",
    "Confirm Undo": "确认撤销", "This undo action will not make any code changes.": "此撤销操作不会对代码做出任何更改。",
    "Confirm Redo": "确认重做", "This redo action will not make any code changes.": "此重做操作不会对代码做出任何更改。",
    "Undo changes up to this point": "撤销更改至此处", "Redo changes up to this point": "重做更改至此处",
    "Confirming this undo action will make the following changes:": "确认此撤销操作将做出以下更改：",
    "Confirming this undo action will not make any code changes.": "确认此撤销操作不会做出任何代码更改。",
    "Confirming this redo action will make the following changes:": "确认此重做操作将做出以下更改：",
    "Confirming this redo action will not make any code changes.": "确认此重做操作不会做出任何代码更改。",
    "Undo changes": "撤销更改", "Redo changes": "重做更改",
    "Record Audio": "录制音频", "Record Audio Ctrl+M": "录制音频 Ctrl+M",
    "Send message": "发送消息", "Send message Enter": "发送消息 Enter",
    "Getting started with a Project": "开始使用项目",
    "Now that you've created a project, configure your project's agent settings or start a conversation.": "现在您已经创建了一个项目，接下来请配置该项目的智能体设置，或者直接开始对话。",
    "Open Settings": "打开设置", "Start first conversation": "开始首次对话",
    "Main Agent": "主智能体", "Add Context": "添加上下文",
    "Loading Antigravity": "正在加载 Antigravity", "Loading": "正在加载",
    "+ New Conversation": "+ 新建对话", "New Conversation": "新建对话", "Conversation History": "历史对话", "Scheduled Tasks": "计划任务",
    "No conversations yet": "暂无对话", "Open IDE": "打开 IDE", "Window": "窗口",
    "Review": "审阅", "Email": "电子邮箱", "Upgrade": "升级", "Not in Project": "未分组项目",
    "Ask anything, @ to mention, / for actions": "输入任何问题，使用 @ 提及，使用 / 执行操作",
    "Status": "状态", "Sort Conversations": "对话排序", "Worktree": "工作区树",
    "New Project": "新建项目", "Quick Start": "快速开始",
    "Good response": "好的回答", "Bad response": "差的回答",

    // General Settings Page
    "General": "常规", "Appearance": "外观", "Theme": "主题", "Light": "浅色", "Dark": "深色",
    "Language": "语言", "Version": "版本", "Check for Updates": "检查更新", "About": "关于",
    "Advanced": "高级", "API Key": "API 密钥", "Account": "账号", "Profile": "个人资料",
    "Logout": "退出登录", "Sign Out": "退出登录", "Feedback": "反馈", "Privacy": "隐私",
    "Terms": "条款", "Auto-start": "开机自启", "Launch on startup": "开机时启动",
    "Notifications": "通知", "Shortcuts": "快捷键", "Keyboard Shortcuts": "键盘快捷键",
    "Global Shortcut": "全局快捷键", "Toggle Visibility": "切换显示/隐藏", "Proxy": "代理",
    "Update": "更新", "Updates": "更新", "Check for update": "检查更新",
    "Models": "模型", "Customizations": "自定义", "Browser": "浏览器", "App": "应用", "Application": "应用",
    "Projects": "项目", "Conversations": "对话", "Provide Feedback": "提供反馈",
    "Manage your plan, credentials, and general preferences.": "管理您的套餐、凭据和常规偏好设置。",
    "Enable Telemetry": "启用遥测",
    "When toggled on, Antigravity collects usage data to help Google enhance performance and features.": "开启后，Antigravity 将收集使用数据，以帮助 Google 提升性能和功能。",
    "Marketing Emails": "营销邮件",
    "Receive product updates, tips, and promotions from Google Antigravity via email.": "通过电子邮件接收来自 Google Antigravity 的产品更新、提示和促销信息。",
    "Your Plan: Google AI Pro": "当前计划：Google AI Pro", "Your Plan:": "当前计划：",
    "You can upgrade to a Google AI Ultra plan to receive higher rate limits.": "您可以升级至 Google AI Ultra 套餐以获得更高的使用限额。",
    "By using this app, you agree to its ": "使用本应用即表示您同意其 ",
    "Terms of Service": "服务条款",
    "Configure agent execution, queued message delivery, and permissions.": "配置智能体执行、排队消息发送以及权限。",
    "Execution": "执行", "Agent Settings": "智能体设置", "Agent Behavior": "智能体行为",
    "File Permissions": "文件权限", "Network Permissions": "网络权限",
    "Queued Messages": "排队消息", "Configure when follow-up messages are sent.": "配置发送后续消息的时机。",
    "Queue": "排队", "Send Immediately": "立即发送", "Keyboard shortcuts": "键盘快捷键",
    "Security Preset": "安全预设", 
    "Choose a predefined security preset for the agent. This controls terminal auto-execution policy, and file access policy.": "为智能体选择一个预定义的安全预设。这将控制终端自动执行策略和文件访问策略。",
    "Default": "默认", "Always Ask": "总是询问", "Always Proceed": "自动执行",
    "Artifact Review Policy": "工件审核策略",
    "Specifies Agent's behavior when asking for review on artifacts, which are documents it creates to enable a richer conversation experience.": "指定智能体在请求审核工件时的行为，工件是其为提供更丰富对话体验而创建的文档。",
    "File Access Rules": "文件访问规则", "Configure allowed and denied paths for file reads and writes.": "配置允许和拒绝的文件读取和写入路径。",
    "Network Access Rules": "网络访问规则", "Configure allowed and denied URLs for reading.": "配置允许和拒绝读取的 URL。",
    "File Reads": "文件读取", "File Writes": "文件写入", "Read URLs": "读取 URL",
    "Inherits your General settings when working in this project.": "在此项目中工作时继承您的常规设置。",
    "Inherits your General settings when working in this project": "在此项目中工作时继承您的常规设置",
    "Allow/deny agent read access to specific files or directories.": "允许/拒绝智能体读取特定文件或目录。",
    "Allow/deny agent write access to specific files or directories.": "允许/拒绝智能体写入特定文件或目录。",
    "Allow/deny agent read access to specific URLs or domains.": "允许/拒绝智能体读取特定 URL 或域名。",
    "Allow/deny specific terminal commands.": "允许/拒绝特定的终端命令。",
    "Allow/deny specific commands outside the sandbox.": "允许/拒绝沙盒外的特定命令。",
    "Allow": "允许", "allow": "允许", "Deny": "拒绝", "deny": "拒绝", "Ask": "询问", "ask": "询问", "Allow/deny": "允许/拒绝",
    "Enter Queues after the turn": "Enter 键：在当前轮次后排队",
    "Alt+Enter Sends immediately": "Alt+Enter 键：立即发送",
    "Alt+Enter On empty prompt, sends next in queue": "Alt+Enter 键：在输入为空时，发送队列中的下一条",
    "Useful for typical development with an emphasis on security. It prioritizes safety over speed by requiring manual approval for all terminal commands and files outside the project directory.": "适用于注重安全的典型开发场景。它将安全性置于速度之上，要求对所有终端命令和项目目录之外的文件访问进行手动批准。",
    "Requires manual review for all terminal commands and file accesses outside of the working folders.": "要求对所有终端命令和工作文件夹之外的文件访问进行手动审阅。",
    "Full machine": "完整机器访问",
    "All terminal commands require review. The agent can read or write to any file in the machine.": "所有终端命令均需审阅。智能体可以读取或写入机器上的任何文件。",
    "Turbo mode": "极速模式",
    "Disables all safety barriers for maximal iteration velocity.": "禁用所有安全屏障，以获得最快的迭代速度。",
    "Custom": "自定义配置", "Manually customize individual settings.": "手动自定义各项设置。",
    "System Default": "跟随系统", "Zoom Level": "缩放比例", "Font Size": "字体大小",
    "Small": "小", "Medium": "中", "Large": "大", "Code Font": "代码字体", "Editor Font": "编辑器字体",
    "Default Model": "默认模型", "Temperature": "温度", "System Prompt": "系统提示词",
    "Search Engine": "搜索引擎", "Web Search": "网络搜索", "Enable Web Access": "启用网络访问",
    "Startup": "启动", "Launch at login": "登录时自动启动", "Hardware Acceleration": "硬件加速",
    "Current Version": "当前版本", "Up to date": "已是最新版本", "Downloading": "下载中...",
    "Restart to update": "重启以更新", "Danger Zone": "危险区域", "Clear History": "清除历史记录",
    "Delete Project": "删除项目", "Delete project": "删除项目",
    "Permanently delete": "永久删除", "permanently delete": "永久删除",
    "active conversation": "个进行中的对话", "active conversations": "个进行中的对话",
    "active conversation.": "个进行中的对话。", "active conversations.": "个进行中的对话。",
    "Delete All": "全部删除", "Reset to Default": "恢复默认设置", "Restore Defaults": "恢复默认设置", "Reset to default": "恢复默认", "Restore defaults": "恢复默认设置",
    "Keybindings": "快捷键绑定", "Command": "命令", "Shortcut": "快捷键", "Action": "操作",
    "Advanced Settings": "高级设置", "Developer Tools": "开发者工具", "Toggle Developer Tools": "切换开发者工具",
    "Open Logs": "打开日志", "Proxy Server": "代理服务器", "Enable Proxy": "启用代理",
    "Auto-Updater": "自动更新程序", "Always": "始终", "Never": "从不", "Ask": "询问",
    "Save changes": "保存更改", "Apply": "应用", "OK": "确定", "Features": "功能",
    "Experimental Features": "实验性功能", "Enable": "启用", "Disable": "禁用",
    "API Configuration": "API 配置", "Account Settings": "账号设置", "Profile Settings": "个人资料",
    "Workspace Settings": "工作区设置", "Manage Projects": "管理项目",
    "Terminal & Tooling Permissions": "终端与工具权限",
    "Terminal Commands": "终端命令", "Configure allowed terminal commands.": "配置允许执行的终端命令。",
    "Commands Outside Sandbox": "沙盒外命令", "Configure allowed commands outside the sandbox.": "配置允许在沙盒外执行的命令。",
    "Allow/deny agent command execution outside the sandbox.": "允许/拒绝智能体在沙盒外执行命令。",
    "Allow/deny agent command execution outside the sandbox": "允许/拒绝智能体在沙盒外执行命令",
    "MCP Tools": "MCP 工具", "Configure external tools via Model Context Protocol.": "通过模型上下文协议配置外部工具。",
    "External tools the agent can call via Model Context Protocol.": "智能体可通过模型上下文协议调用的外部工具。",
    "External tools the agent can call via Model Context Protocol": "智能体可通过模型上下文协议调用的外部工具",

    // Models & Usage Tab
    "Models & Usage": "模型与用量", "Manage your model quota and credits.": "管理您的模型配额和积分额度。",
    "Plan": "订阅计划", "Model Credits": "模型积分", "Enable AI Credit Overages": "启用 AI 积分超额使用",
    "When toggled on, Antigravity will use your AI credits to fulfill model requests once you're out of model quota. Antigravity will always use your model quota first before using AI credits.": "启用后，当您的模型配额用尽时，Antigravity 将使用您的 AI 积分来完成模型请求。Antigravity 将始终优先使用模型配额。",
    "See Activity": "查看活动", "Get More AI Credits": "获取更多 AI 积分",
    "Available AI Credits:": "可用 AI 积分：",
    "Gemini Models": "Gemini 模型", "Claude and GPT models": "Claude 和 GPT 模型",
    "Limited time": "限时", "Low": "低", "High": "高", "View Usage": "查看用量",

    // Customizations & Plugins
    "Configure default behaviors, skills, and MCP servers.": "配置默认行为、技能和 MCP 服务器。",
    "Learn more.": "了解更多。", "Learn more": "了解更多",
    "Token Usage": "Token 使用量",
    "The breakdown below shows token usage from customizations like skills, rules, and MCP. If the budget is exceeded, large customizations will be truncated automatically.": "下方的明细展示了来自技能、规则和 MCP 等自定义项的 Token 使用情况。如果超出预算，大型自定义项将被自动截断。",
    "There are no customizations enabled.": "当前未启用任何自定义项。",
    "There are no customizations enabled": "当前未启用任何自定义项",
    "Skills": "技能", "Rules": "规则",
    "Installed MCP Servers": "已安装的 MCP 服务器",
    "Add MCP +": "添加 MCP +", "Add MCP": "添加 MCP", "Add MCP Servers": "添加 MCP 服务器",
    "Search MCP servers by name": "按名称搜索 MCP 服务器",
    "Refresh": "刷新", "Open MCP Config": "打开 MCP 配置",
    "No MCP Servers": "无 MCP 服务器", "No MCP servers installed": "未安装任何 MCP 服务器",
    "No MCP servers installed.": "未安装任何 MCP 服务器。", "No MCP Servers installed": "未安装任何 MCP 服务器",
    "Use Add MCP to browse the store, or add a custom server via the MCP config.": "使用“添加 MCP”浏览商店，或通过 MCP 配置添加自定义服务器。",
    "Use Add MCP to browse the store, or add a custom server via the MCP config": "使用“添加 MCP”浏览商店，或通过 MCP 配置添加自定义服务器",
    "You currently don't have any MCP Servers installed. Add an MCP server above or add a custom one via the MCP Config.": "您目前尚未安装任何 MCP 服务器。请在上方添加 MCP 服务器，或通过 MCP 配置添加自定义服务器。",
    "Plugins": "插件", "plugins": "插件", "Plugin": "插件", "plugin": "插件",
    "Build With Google Plugins": "使用 Google 插件构建", "Build with Antigravity Plugins": "使用 Antigravity 插件构建",
    "Browse and enable plugins from the Build With Google catalog.": "浏览并启用来自 Build With Google 目录的插件。",
    "Browse and enable plugins from the Build With Google catalog": "浏览并启用来自 Build With Google 目录的插件",
    "Browse and enable plugins from the Build with Antigravity catalog.": "浏览并启用来自 Build with Antigravity 目录的插件。",
    "Browse and enable plugins from the Build with Antigravity catalog": "浏览并启用来自 Build with Antigravity 目录的插件",
    "Customize": "自定义", "Hide breakdown": "隐藏明细",
    "coding agent": "编程智能体",
    "Core tools and knowledge required to develop for Android": "开发 Android 所需的核心工具和知识",
    "Modern Web Guidance": "现代 Web 开发指南",
    "Keep your coding agent up to date with the latest web best practices.": "让您的编程智能体掌握最新的 Web 最佳实践。",
    "Google Antigravity SDK": "Google Antigravity SDK",
    "Using the Antigravity Python SDK to build AI agents": "使用 Antigravity Python SDK 构建 AI 智能体",
    "Science": "科学", "Curated collection of agent skills for science.": "精选的科学领域智能体技能集合。",
    "Firebase": "Firebase",
    "Prototype, build & run modern apps users love with Firebase's backend, AI, and operational infrastructure.": "借助 Firebase 的后端、AI 和运营基础设施，设计原型、构建并运行深受用户喜爱的现代应用。",
    "Chrome DevTools": "Chrome 开发者工具",
    "Reliable automation, in-depth debugging, and performance analysis in Chrome using Chrome DevTools and Puppeteer": "使用 Chrome DevTools 和 Puppeteer 在 Chrome 中实现可靠的自动化、深度调试和性能分析",
    "Google Kubernetes Engine (Remote)": "Google Kubernetes Engine (远程)",
    "How to render rich interactive HTML widgets inline in the chat or as standalone artifacts. Use this skill when you want to show the user diagrams, data visualizations, interactive controls, educational walkthroughs, or any rich visual content beyond plain text and markdown.": "在对话中内联呈现丰富的交互式 HTML 小部件或作为独立工件。当您想向用户展示图表、数据可视化、交互式控件、教程指南或任何超出纯文本和 Markdown 的丰富视觉内容时，请使用此技能。",
    "Automatically migrate legacy workflows (.agents/workflows/ or ~/.gemini/config/workflows/) to skills (.agents/skills/ or ~/.gemini/config/skills/). Scans for existing workflows, creates target skills directories, extracts and structures instruction content into SKILL.md, and optionally removes old workflow files after confirmation.": "自动将旧版工作流（.agents/workflows/ 或 ~/.gemini/config/workflows/）迁移到技能（.agents/skills/ 或 ~/.gemini/config/skills/）。扫描现有工作流，创建目标技能目录，将指令内容提取并结构化到 SKILL.md 中，并在确认后可选删除旧工作流文件。",
    "Guidelines for interacting with GitHub and request permissions from the user when commands fail due to restrictions in the agent environment.": "与 GitHub 交互的指南，并在命令由于智能体环境中的限制而失败时向用户请求权限。",

    // Shortcuts Panel
    "Configure keyboard shortcuts.": "配置键盘快捷键。",
    "Keyboard shortcuts for quick navigation and control.": "用于快速导航和控制的键盘快捷键。",
    "RECOMMENDED": "推荐", "NAVIGATION": "导航", "Recommended": "推荐", "Navigation": "导航",
    "Open Conversation Picker": "打开对话选择器", "Open File Search": "打开文件搜索",
    "Focus Input": "聚焦输入框", "File Picker": "文件选择器",
    "Select Previous Conversation": "选择上一个对话", "Select Next Conversation": "选择下一个对话",
    "Previous Pane Tab": "上一个面板标签", "Next Pane Tab": "下一个面板标签",
    "Toggle Model Selector": "切换模型选择器", "Toggle Voice Recording": "切换语音录制",
    "Toggle Terminal": "切换终端", "Toggle terminal": "切换终端",
    "Find in Pane": "在面板中查找", "Add to Chat/Quote": "添加到对话/引用",
    "LAYOUT CONTROLS": "布局控制", "Layout Controls": "布局控制", "Layout controls": "布局控制",
    "App Shortcuts": "应用快捷键", "Editor Shortcuts": "编辑器快捷键", 
    "Global Shortcuts": "全局快捷键", "Terminal Shortcuts": "终端快捷键", 
    "Chat Shortcuts": "对话快捷键", "Press desired key combination": "按下所需的组合键",

    // Feedback Panel
    "Feedback Type": "反馈类型", "Auth and Billing": "认证与计费", "Description": "描述",
    "Please describe the issue in detail. The more actionable your feedback, the quicker our team can address your request. Some helpful information includes:": "请详细描述您的问题。您的反馈越具体，我们的团队就能越快处理您的请求。一些有用的信息包括：",
    "Steps to reproduce the issue": "重现问题的步骤", "Expected behavior": "预期行为",
    "Actual behavior": "实际行为", "Any error messages": "任何错误消息", "Any relevant information": "任何相关信息",
    "Describe the bug you encountered...": "描述您遇到的错误...",
    "Steps to Reproduce": "重现步骤", "Please list the steps to reproduce the issue...": "请列出重现问题的步骤...",
    "Please list the steps to reproduce the issue": "请列出重现问题的步骤",
    "Attach a screenshot (optional)": "附加截图（可选）", "Attach Antigravity server logs": "附加 Antigravity 服务器日志",
    "We'd love to hear from you.": "我们期待您的反馈。", "How can we improve?": "我们该如何改进？",
    "Thinking...": "思考中...", "Thought": "思考过程", "Agent is thinking...": "智能体正在思考...",
    "Show thought process": "显示思考过程", "Hide thought process": "隐藏思考过程",
    "Generating...": "生成中...", "Planning...": "计划中...",
    "Issue Type": "问题类型", "Bug Report": "错误报告", "Feature Request": "功能请求",
    "General Feedback": "常规反馈", "Describe your issue or idea...": "描述您的问题或想法...",
    "Please provide details...": "请提供详细信息...", "Include diagnostic data": "包含诊断数据",
    "Include app logs": "包含应用日志", "Send Feedback": "发送反馈",

    // Browser Tab
    "Browser Settings": "浏览器设置", "Configure the browser subagent. It requires": "配置浏览器子智能体。需要安装",
    "to be installed. The browser subagent can be invoked by typing /browser in the conversation input box.": "。您可以在对话输入框中输入 /browser 来调用浏览器子智能体。",
    "Browser Javascript Execution Policy": "浏览器 JavaScript 执行策略",
    "Controls whether the agent can run custom JavaScript to automate complex browser actions.": "控制智能体是否可以运行自定义 JavaScript 来自动化复杂的浏览器操作。",
    "Disabled": "已禁用", "Block all browser JavaScript execution.": "阻止所有浏览器 JavaScript 执行。",
    "Request Review": "请求审阅", "Prompt for approval before running browser scripts.": "在运行浏览器脚本前提示批准。",
    "Allow full browser script execution without prompting.": "允许执行完整的浏览器脚本而不提示。",
    "Actuation Permissions": "操作权限", "Browser Actuation Rules": "浏览器操作规则",
    "Configure allowed and denied URLs for browser actuation.": "配置允许和拒绝进行浏览器操作的 URL。",

    // App & Application Tab
    "App Settings": "应用设置", "Application Settings": "应用设置", "Manage application settings.": "管理应用设置。",
    "Manage Antigravity app settings.": "管理 Antigravity 应用设置。", "Manage Antigravity app settings": "管理 Antigravity 应用设置",
    "Prevent Sleep": "阻止睡眠", "Prevent the computer from sleeping while the app is running.": "在应用运行时阻止计算机进入睡眠状态。",
    "Keep In Menu Bar": "保留在系统托盘", 
    "The app will be accessible from the menu bar and will keep running in the background when all windows are closed.": "应用将可以从系统托盘访问，并在所有窗口关闭时继续在后台运行。",
    "Keep the app accessible from the menu bar and running in the background when all windows are closed.": "应用将可以从系统托盘访问，并在所有窗口关闭时继续在后台运行。",
    "Remote Control": "远程控制", "remote control": "远程控制",
    "Enable Remote Control": "启用远程控制", "Enable remote control": "启用远程控制",
    "Work with local agents from another device.": "从另一台设备与本地智能体协同工作。",
    "Work with local agents from another device": "从另一台设备与本地智能体协同工作",
    "Automatic Check for Updates": "自动检查更新", "Automatic check for updates": "自动检查更新",
    "Automatically prompt you to restart the app when a new update is available. When disabled, you can check for updates manually from the app menu.": "当有新版本可用时，自动提示您重启应用。禁用后，您可以从应用菜单手动检查更新。",
    "Automatically prompt you to restart the app when a new update is available.": "当有新版本可用时，自动提示您重启应用。",
    "When disabled, you can check for updates manually from the app menu.": "禁用后，您可以从应用菜单手动检查更新。",
    "Notification Settings": "通知设置", "To modify notification settings, open your operating system's system preferences.": "要修改通知设置，请打开操作系统的系统偏好设置。",
    "Open System Preferences": "打开系统偏好设置",

    // Conversations Tab & Permissions
    "Agent settings and permissions for conversations outside of projects.": "针对项目外对话的智能体设置和权限。",
    "Inherit General": "继承全局设置", "Local Permissions": "本地权限",
    "Also includes": "还包括", "global settings": "全局设置",
    "when working in this project.": "（当在此项目中工作时）。",
    "Toggle Sidebar": "切换侧边栏", "View Split Diff": "分屏查看差异", "Collapse All": "全部折叠",
    "Learn more about": "了解更多关于",
    "Configure the agent's visual theme and display preferences.": "配置智能体的视觉主题和显示偏好。",
    "Chat Settings": "聊天设置", "Verbose Agent Chat": "详细的智能体对话",
    "Display and preserve intermediate thinking steps.": "显示并保留中间思考过程。",
    "Conversation Width": "对话宽度", "Configure the maximum width of the conversation panel.": "配置对话面板的最大宽度。",
    "Narrow": "较窄", "Wide": "较宽",
    "Select light, dark, or inherit system settings.": "选择浅色、深色，或跟随系统设置。",
    "Light Theme": "浅色主题", "Preset": "预设", "Default Light": "默认浅色",
    "Background": "背景颜色", "Foreground": "前景颜色", "Accent": "强调色",
    "Dark Theme": "深色主题", "Default Dark": "默认深色",
    "Allow write access to this path?": "允许写入此路径吗？",
    "Allow read access to this path?": "允许读取此路径吗？",
    "Allow execution of this command?": "允许执行此命令吗？",
    "Yes, allow this time": "是，仅本次允许",
    "Yes, and always allow in this conversation": "是，在本次对话中始终允许",
    "Yes, and always allow when not in a project": "是，在未分组项目中始终允许",
    "Yes, and always allow": "是，始终允许",
    "tell the agent what to do instead": "告诉智能体接下来该做什么",
    "(tell the agent what to do instead)": "(告诉智能体接下来该做什么)",
    "Skip": "跳过", "Working.": "运行中。", "Working...": "运行中...",
    "Edited": "已编辑", "Viewed": "已查看", "Created": "已创建", "Deleted": "已删除", "Executed": "已执行",
    "Save rule to always allow write access to this path?": "保存规则以始终允许写入此路径吗？",
    "Save rule to always allow read access to this path?": "保存规则以始终允许读取此路径吗？",
    "Save rule to always allow execution of this command?": "保存规则以始终允许执行此命令吗？",
    "Yes, save rule in this conversation": "是，在本次对话中保存规则",
    "Yes, save rule when not in a project": "是，在未分组项目中保存规则",
    "Yes, save rule globally": "是，全局保存规则",

    // Error & Diagnostics UI
    "Our servers are experiencing high traffic right now, please try again in a minute.": "我们的服务器当前负载较高，请稍后重试。",
    "Error ID:": "错误 ID：",
    "Agent terminated due to error": "智能体因错误而终止",
    "You can prompt the model to try again or start a new conversation if the error persists.": "您可以提示模型重试，或者如果错误仍然存在，可以开启新的对话。",
    "See our troubleshooting guide for more help.": "查看我们的排查指南以获取更多帮助。",
    "See our troubleshooting guide for more help": "查看我们的排查指南以获取更多帮助",
    "troubleshooting guide": "排查指南", "troubleshooting_guide": "排查指南",
    "See our": "查看我们的",
    "for more help.": "以获取更多帮助。", "for more help": "以获取更多帮助",
    "Dismiss": "忽略", "Copy debug info": "复制调试信息"
  };

  const coreWords = {
    "create": "创建", "delete": "删除", "new": "新建", "edit": "编辑", "save": "保存", "cancel": "取消", "confirm": "确认",
    "close": "关闭", "open": "打开", "stop": "停止", "start": "启动", "run": "运行", "add": "添加", "remove": "移除", "download": "下载",
    "update": "更新", "select": "选择", "clear": "清除", "search": "搜索", "find": "查找", "view": "查看", "show": "显示", "hide": "隐藏",
    "copy": "复制", "paste": "粘贴", "cut": "剪切", "rename": "重命名", "duplicate": "制作副本",
    "agent": "智能体", "agents": "智能体", "subagent": "子智能体", "subagents": "子智能体", "task": "任务", "tasks": "任务",
    "workspace": "工作区", "workspaces": "工作区", "directory": "目录", "folder": "文件夹", "file": "文件", "files": "文件",
    "command": "命令", "commands": "命令", "terminal": "终端", "console": "控制台", "output": "输出", "input": "输入",
    "error": "错误", "warning": "警告", "info": "信息", "success": "成功", "failed": "失败", "pending": "等待中", "running": "运行中",
    "yes": "是", "no": "否", "true": "真", "false": "假", "on": "开", "off": "关", "enable": "启用", "disable": "禁用",
    "application": "应用", "applications": "应用", "remote": "远程", "control": "控制",
    "plugin": "插件", "plugins": "插件", "allow": "允许", "deny": "拒绝", "ask": "询问", "inherit": "继承", "inherits": "继承",
    "read": "读取", "reads": "读取", "write": "写入", "writes": "写入",
    "global": "全局", "retry": "重试", "regenerate": "重新生成", "dismiss": "忽略"
  };

  // Structured Prefix & Content Match Rules for Complex / Truncated Text
  const textPrefixRules = [
    // Plugins & Customizations
    ["Plugins are packaged collections of skills and MCPs to help the Agent in", "插件是技能和 MCP 的打包集合，用于帮助 "],
    ["Plugins are packaged collections of skills and MCPs", "插件是技能和 MCP 的打包集合，用于帮助 "],
    ["work with Google developer products. You can always change your choices in Settings.", " 中的智能体与 Google 开发者产品协同工作。您可以随时在“设置”中更改您的选择。"],
    ["Provides a comprehensive guide", "提供 Google Antigravity (AGY) 的综合指南、快速参考和站点地图，包括 Antigravity CLI、Antigravity 2.0、IDE、Python SDK、斜杠命令、快捷键和自定义项。"],
    ["Comprehensive guide and reference for the Antigravity Customization System", "Antigravity 自定义系统的综合指南和参考。用于解释自定义项的工作原理、加载优先级、发现机制，并指导创建技能、规则、插件、钩子和 MCP 服务器。"],
    ["Skills providing tailored instructions for happy path", "提供 Dart 和 Flutter 开发主流程定制化指南的技能。"],
    ["Build and prototype location-aware applications with Google Maps Platform", "使用 Google Maps Platform 构建具有位置感知能力的应用并设计原型。"],
    ["Specialized suite of skills for data engineers and database", "专为 Google Cloud 上的数据工程师和数据库从业人员打造的专业技能套件。"],
    ["Build applications with the Gemini Interactions API and Live API", "使用 Gemini Interactions API 和 Live API 构建应用，包括文本生成、多轮对话等功能。"],

    // MCP Servers Descriptions
    ["Investigate and fix software issues using AI-powered root cause analysis", "使用 AI 驱动的根本原因分析来调查和修复软件问题。此 MCP 服务器连接到您的 Antimetal 账户..."],
    ["Query and act on your marketing, analytics, CRM, e-commerce", "跨 325 多个连接器查询并处理您的营销、分析、CRM、电子商务和仓库数据..."],
    ["Query your GitLab SDLC as a knowledge graph", "将您的 GitLab SDLC 作为知识图谱进行查询。Orbit 会建立相关索引..."],
    ["Enable Antigravity to deploy apps to Google Cloud Run", "使 Antigravity 能够将应用部署到 Google Cloud Run。"],
    ["Search and reference over 600,000 real-world app screens", "搜索并参考超过 600,000 个真实的应用程序屏幕、用户流程和 UI 模式..."],
    ["Build, edit, deploy, and manage full-stack web apps with Lovable", "使用自然语言，通过 Lovable 构建、编辑、部署和管理全栈 Web 应用..."],
    ["The GKE remote MCP server provides read write access to your GKE", "GKE 远程 MCP 服务器提供对您的 GKE Kubernetes 资源的读写访问权限。"],
    ["The Dart and Flutter MCP server exposes Dart (and Flutter)", "Dart 和 Flutter MCP 服务器向兼容的 AI 助手客户端公开相关开发工具操作。"],
    ["The Firebase Model Context Protocol (MCP) Server gives AI-powered", "Firebase MCP 服务器使 AI 工具能够处理您的 Firebase 项目和应用程序代码库。"],
    ["The Genkit Model Context Protocol (MCP) Server gives AI-powered", "Genkit MCP 服务器使 AI 工具能够构建、调试和检查您的 Genkit 应用。"],
    ["The gopls Model Context Protocol (MCP) server provides tools", "gopls MCP 服务器为您的 Go 代码库提供语义代码分析、实时诊断和转换工具。"],
    ["Interact with your BigQuery data using natural language", "使用自然语言与您的 BigQuery 数据交互。允许您安全地连接到您的数据集..."],
    ["The AlloyDB for PostgreSQL remote MCP server lets you access", "AlloyDB for PostgreSQL 远程 MCP 服务器允许您访问和运行 AlloyDB 工具..."],
    ["The Bigtable Admin remote MCP server lets you manage Bigtable", "Bigtable Admin 远程 MCP 服务器允许您管理 Bigtable 资源。"],
    ["The Cloud SQL remote MCP server lets you access and run Cloud SQL", "Cloud SQL 远程 MCP 服务器允许您访问和运行 Cloud SQL 工具..."],
    ["The Spanner remote MCP server lets you access and run Spanner", "Spanner 远程 MCP 服务器允许您访问和运行 Spanner 工具..."],
    ["The Apigee API hub remote MCP server lets you manage", "Apigee API hub 远程 MCP 服务器允许您管理 API、版本、规范、操作等。"],
    ["Connect your AI assistants to Looker business intelligence", "将您的 AI 助手连接到 Looker 商业智能，通过自然语言查询实现数据探索。"],
    ["Connect your AI assistants to the Knowledge Catalog", "将您的 AI 助手连接到 Knowledge Catalog，实现数据发现和治理。"],
    ["The MCP Toolbox for Databases is an open-source MCP server", "MCP Toolbox for Databases 是一个开源 MCP 服务器，旨在简化和保护用于与数据库交互的工具的开发。"],
    ["Interact with your Oracle Database data using natural language", "使用自然语言与您的 Oracle 数据库交互。此 MCP 服务器允许您安全地连接到您的数据库以执行 SQL 查询..."],
    ["The Dev Mode MCP Server brings Figma directly into your workflow", "Dev Mode MCP 服务器通过向从 Figma 生成代码的 AI 智能体提供重要的设计信息和上下文，将 Figma 直接带入您的工作流..."],
    ["The GitHub MCP Server is a Model Context Protocol (MCP) server", "GitHub MCP 服务器提供与 GitHub API 的无缝集成，从而实现高级自动化和..."],
    ["The Google Home Developer MCP server allows you to search", "Google Home Developer MCP 服务器允许您搜索 Google Home 文档、OpenThread 和 Matter 规范文档。"],
    ["Neon MCP Server is an open-source tool that lets you interact", "Neon MCP 服务器是一个开源工具，允许您使用自然语言与您的 Neon Postgres 数据库交互。"],
    ["The Stripe Model Context Protocol server allows you to integrate", "Stripe MCP 服务器允许您通过函数调用与 Stripe API 集成。该协议支持各种交互工具..."],
    ["Interact with Redis key-value stores", "与 Redis 键值存储交互。"],
    ["A Model Context Protocol server for interacting with MongoDB", "用于与 MongoDB Atlas 交互的模型上下文协议服务器。"],
    ["Official Notion MCP Server that allows interaction with Notion", "官方 Notion MCP 服务器，允许通过 Notion API 与 Notion 工作区、页面、数据库和评论进行交互。"],
    ["Official Linear.app MCP Server for interacting with Linear", "官方 Linear.app MCP 服务器，用于与 Linear 项目、议题和工作流进行交互。"],
    ["An MCP server implementation that integrates the Perplexity", "一个集成了 Perplexity Sonar API 的 MCP 服务器实现，以提供实时的、全网范围的研究能力。"],
    ["Official PayPal MCP Server that allows integration with PayPal", "官方 PayPal MCP 服务器，允许与 PayPal API 集成，用于支付处理、交易管理和账户操作。"],
    ["The Heroku Platform MCP Server enables seamless interaction", "Heroku Platform MCP 服务器可实现与 Heroku 平台资源的无缝交互，允许 LLM 读取、管理和操作应用程序..."],
    ["The Pinecone MCP Server enables AI tools to search Pinecone", "Pinecone MCP 服务器使 AI 工具能够搜索 Pinecone 文档、配置索引、根据索引配置生成代码..."],
    ["Connect your Supabase projects to AI assistants.", "将您的 Supabase 项目连接到 AI 助手。此 MCP 服务器允许管理表、获取配置、执行 SQL 查询、管理边缘函数等..."],
    ["The Prisma MCP Server enables AI tools to interact with Prisma", "Prisma MCP 服务器使 AI 工具能够与 Prisma 交互，从而轻松创建和管理 Postgres 数据库。"],
    ["The Locofy MCP Server", "Locofy MCP 服务器使 Locofy.ai 代码能够与您的 IDE 集成并进行扩展。"],
    ["Locofy MCP Server enables Locofy.ai code", "Locofy MCP 服务器使 Locofy.ai 代码能够与您的 IDE 集成并进行扩展。"],
    ["Airweave lets agents search any app.", "Airweave 允许智能体搜索任何应用程序。"],
    ["Atlassian MCP Server for interacting with Atlassian", "用于与 Atlassian 产品交互的 Atlassian MCP 服务器。"],
    ["Interact with your Harness account using natural language", "使用自然语言与您的 Harness 账户交互。此 MCP 服务器允许 AI 智能体检查和管理 CI/CD 流水线、执行、服务..."],
    ["SonarQube MCP Server enables AI assistants to interact", "SonarQube MCP 服务器使 AI 助手能够与 SonarQube 实例交互，进行代码质量分析、项目管理和质量门限操作。"],
    ["Perform searches on ingested data in Google-owned data stores", "在 Google 拥有的数据存储中，对已摄取的数据执行搜索。"],
    ["Interact with documents stored in a Firestore database", "使用自然语言与存储在 Firestore 数据库中的文档进行交互。"],
    ["Access resources in the Cloud Logging platform using natural", "使用自然语言访问 Cloud Logging 平台中的资源。"],
    ["Manage clusters for Managed Service for Apache Kafka", "使用自然语言管理 Apache Kafka 托管服务和 Kafka Connect 的集群。"],
    ["Access resources in the Cloud Monitoring platform using natural", "使用自然语言访问 Cloud Monitoring 平台中的资源。"],
    ["Manage Pub/Sub resources and publish messages. Create, list,", "管理 Pub/Sub 资源并发布消息。创建、列出、获取、更新和删除 Pub/Sub 主题、订阅和快照，以及发布消息..."],
    ["The Cloud Quotas MCP server allows you to view quota allocations", "Cloud Quotas MCP 服务器允许您查看配额分配、请求增加配额以及管理配额调整器配置。"],
    ["Enable Antigravity to control and inspect a live Chrome browser", "使 Antigravity 能够控制和检查实时 Chrome 浏览器，利用 Chrome DevTools 的强大功能进行可靠的自动化、深度调试..."],
    ["Netlify MCP Server enables AI assistants to interact", "Netlify MCP 服务器使 AI 助手能够与 Netlify 平台交互，以管理站点、部署、域名和其他 Web 开发工作流。"],
    ["A Model Context Protocol server that provides structured thinking", "一个模型上下文协议服务器，为 LLM 对话提供结构化思考和推理能力。"],
    ["Sonatype MCP server for interacting with our dependency management", "用于与我们的依赖项管理和安全情报平台交互的 Sonatype MCP 服务器。"],
    ["The Google Maps Platform Code Assist MCP server provides", "Google Maps Platform Code Assist MCP 服务器为您喜爱的 AI 编程助手提供最新、官方的 Google Maps Platform 文档、代码..."],
    ["This MCP server provides your LLM with docs and examples to instrument your AI apps with Arize AX", "此 MCP 服务器为您的 LLM 提供文档和示例，以便使用 Arize AX 检测您的 AI 应用。它还提供对 Arize 支持的访问。将其连接到您的 IDE..."],
    ["The Postman MCP Server connects Postman to AI tools", "Postman MCP 服务器将 Postman 连接到 AI 工具，使 AI 智能体和助手能够访问工作区、管理集合和环境..."],
    ["The Stitch MCP server enables AI assistants to interact with Stitch", "Stitch MCP 服务器使 AI 助手能够与 Stitch 交互以进行设计：从文本和图像生成 UI 设计，以及访问项目和屏幕..."],
    ["The ClickHouse MCP server enables agents to securely interact", "ClickHouse MCP 服务器使智能体能够安全地与 ClickHouse 数据库交互。它提供了一个通用接口来执行 SQL、探索数据和查看..."],
    ["Perform a range of infrastructure management tasks, including: manage virtual machine", "执行一系列基础设施管理任务，包括：管理虚拟机 (VM) 实例、管理实例组管理器和实例模板..."],
    ["Access enterprise mobility data using natural language queries", "使用关于设备队列的自然语言查询、策略合规性的自动审计以及设备集成来访问企业移动数据..."],
    ["Search your Google Cloud projects using natural language", "使用自然语言搜索您的 Google Cloud 项目。"],

    ["Manage Antigravity app settings", "管理 Antigravity 应用设置。"],
    ["Work with local agents from another device", "从另一台设备与本地智能体协同工作。"],
    ["Automatically prompt you to restart the app when a new update is available", "当有新版本可用时，自动提示您重启应用。禁用后，您可以从应用菜单手动检查更新。"],
    ["When disabled, you can check for updates manually from the app menu", "禁用后，您可以从应用菜单手动检查更新。"],
    ["There are no customizations enabled", "当前未启用任何自定义项。"],
    ["No MCP servers installed", "未安装任何 MCP 服务器"],
    ["Use Add MCP to browse the store, or add a custom server via the MCP config", "使用“添加 MCP”浏览商店，或通过 MCP 配置添加自定义服务器。"],
    ["Browse and enable plugins from the Build With Google catalog", "浏览并启用来自 Build With Google 目录的插件。"],
    ["Browse and enable plugins from the Build with Antigravity catalog", "浏览并启用来自 Build with Antigravity 目录的插件。"],
    ["Manage project folders, agent settings, and permissions", "管理项目文件夹、智能体设置和权限。"],
    ["How to render rich interactive HTML widgets", "在对话中内联呈现丰富的交互式 HTML 小部件或作为独立工件。当您想向用户展示图表、数据可视化、交互式控件、教程指南或任何超出纯文本和 Markdown 的丰富视觉内容时，请使用此技能。"],
    ["Automatically migrate legacy workflows", "自动将旧版工作流（.agents/workflows/ 或 ~/.gemini/config/workflows/）迁移到技能（.agents/skills/ 或 ~/.gemini/config/skills/）。扫描现有工作流，创建目标技能目录并将内容提取到 SKILL.md 中。"],
    ["Guidelines for interacting with GitHub", "与 GitHub 交互的指南，并在命令由于智能体环境中的限制而失败时向用户请求权限。"],
    ["Are you sure you want to delete the project", "您确定要删除项目 "],
    ["Are you sure you want to delete the", "您确定要删除 "],
    ["Are you sure you want to delete", "您确定要删除 "],
    ["This will permanently delete", "这将永久删除包含在其中的 "],
    ["Inherits your General settings when working in this project", "在此项目中工作时继承您的常规设置。"],
    ["Inherits your general settings when working in this project", "在此项目中工作时继承您的常规设置。"],
    ["Allow/deny agent read access to specific files or directories", "允许/拒绝智能体读取特定文件或目录。"],
    ["Allow/deny agent write access to specific files or directories", "允许/拒绝智能体写入特定文件或目录。"],
    ["Allow/deny agent read access to specific URLs or domains", "允许/拒绝智能体读取特定 URL 或域名。"],
    ["Allow/deny specific terminal commands", "允许/拒绝特定的终端命令。"],
    ["Allow/deny specific commands outside the sandbox", "允许/拒绝沙盒外的特定命令。"],
    ["Allow/deny agent command execution outside the sandbox", "允许/拒绝智能体在沙盒外执行命令。"],
    ["External tools the agent can call via Model Context Protocol", "智能体可通过模型上下文协议调用的外部工具。"],

    // Error and Fallback Links
    ["Confirming this undo action will make the following changes", "确认此撤销操作将做出以下更改："],
    ["Confirming this undo action will not make any code changes", "确认此撤销操作不会做出任何代码更改。"],
    ["Confirming this redo action will make the following changes", "确认此重做操作将做出以下更改："],
    ["Confirming this redo action will not make any code changes", "确认此重做操作不会做出任何代码更改。"],
    ["Undo changes up to this point", "撤销更改至此处"],
    ["Redo changes up to this point", "重做更改至此处"],
    ["Our servers are experiencing high traffic", "我们的服务器当前负载较高，请稍后重试。"],
    ["Agent terminated due to error", "智能体因错误而终止"],
    ["You can prompt the model to try again", "您可以提示模型重试，或者如果错误仍然存在，可以开启新的对话。"],
    ["for more help", " 以获取更多帮助。"],
    ["See our", "查看我们的 "]
  ];

  function translateText(text) {
    if (!text || typeof text !== 'string') return text;
    let trimmed = text.trim();
    if (!trimmed) return text;

    if (dictionary[trimmed]) {
      return text.replace(trimmed, dictionary[trimmed]);
    }
    
    // Dynamic Regex Translations
    let m;
    if (text.indexOf("of the customization budget is available") !== -1) {
      text = text.replace(/(\d+(?:\.\d+)?)% of the customization budget is available\.?/g, "自定义项预算可用额度为 $1%。");
      text = text.replace(/%\s*of the customization budget is available\.?/g, "% 的自定义项预算可用额度。");
      text = text.replace(/(^\s*)of the customization budget is available\.?/g, "$1的自定义项预算可用额度。");
    }
    if ((m = trimmed.match(/^Show (\d+) breakdowns?$/))) {
      return text.replace(trimmed, "显示 " + m[1] + " 项明细");
    }
    if ((m = trimmed.match(/^Learn more about (.+)$/))) {
      return text.replace(trimmed, "了解更多关于 " + (dictionary[m[1]] || m[1]) + " 的信息");
    }
    if ((m = trimmed.match(/^You have used some of your weekly limit, it will fully refresh in (.*)\.$/))) {
      let timeStr = m[1].replace(/days?/g, "天").replace(/hours?/g, "小时").replace(/minutes?/g, "分钟").replace(/,/g, "");
      return text.replace(trimmed, "您已使用部分每周限额，它将在 " + timeStr + " 后完全重置。");
    }
    if ((m = trimmed.match(/^You have used some of your 5-hour limit, it will fully refresh in (.*)\.$/))) {
      let timeStr = m[1].replace(/days?/g, "天").replace(/hours?/g, "小时").replace(/minutes?/g, "分钟").replace(/,/g, "");
      return text.replace(trimmed, "您已使用部分五小时限额，它将在 " + timeStr + " 后完全重置。");
    }
    if ((m = trimmed.match(/^Available AI Credits: ([\d,]+)$/))) {
      return text.replace(trimmed, "可用 AI 积分: " + m[1]);
    }
    if ((m = trimmed.match(/^Send feedback as (.+)$/))) {
      return text.replace(trimmed, "以 " + m[1] + " 的身份发送反馈");
    }
    if ((m = trimmed.match(/^Permanently delete (.+) (including|包括) (\d+) active conversations?\.?$/))) {
      return text.replace(trimmed, "永久删除 " + m[1] + "，包括 " + m[3] + " 个进行中的对话。");
    }
    if ((m = trimmed.match(/^(\d+) active conversations?\.?$/))) {
      return text.replace(trimmed, m[1] + " 个进行中的对话。");
    }
    if ((m = trimmed.match(/^(\d+) active conversations?$/))) {
      return text.replace(trimmed, m[1] + " 个进行中的对话");
    }
    if ((m = trimmed.match(/^(\+?\d+) more lines$/))) {
      return text.replace(trimmed, "更多 " + m[1] + " 行");
    }
    if ((m = trimmed.match(/^(\d+) files? changed$/))) {
      return text.replace(trimmed, m[1] + " 个文件已修改");
    }
    if ((m = trimmed.match(/^Version ([\d\.]+(-\w+)?)$/))) {
      return text.replace(trimmed, "版本 v" + m[1]);
    }
    if ((m = trimmed.match(/^(\d+)s$/))) return text.replace(trimmed, m[1] + "秒前");
    if ((m = trimmed.match(/^(\d+)m$/))) return text.replace(trimmed, m[1] + "分钟前");
    if ((m = trimmed.match(/^(\d+)h$/))) return text.replace(trimmed, m[1] + "小时前");
    if ((m = trimmed.match(/^(\d+)d$/))) return text.replace(trimmed, m[1] + "天前");

    // Dynamic Time Formatter
    if (text.indexOf("Worked for") !== -1) {
      return text.replace(/Worked for ([\d\.a-z ]+)/gi, function(_, timeStr) {
        let t = timeStr.replace(/ms/g, "毫秒").replace(/s/g, "秒").replace(/m/g, "分").replace(/h/g, "小时");
        return "运行耗时 " + t;
      });
    }
    if (text.indexOf("Thought for") !== -1) {
      return text.replace(/Thought for ([\d\.a-z ]+)/gi, function(_, timeStr) {
        let t = timeStr.replace(/ms/g, "毫秒").replace(/s/g, "秒").replace(/m/g, "分").replace(/h/g, "小时");
        return "思考耗时 " + t;
      });
    }
    if (text.indexOf("Working") !== -1) {
      text = text.replace(/Working(\.*)/g, "运行中$1");
    }

    // Special Multi-segment Matches
    if (text.indexOf("Are you sure you want to delete") !== -1) {
      text = text.replace(/Are you sure you want to delete the\s*(project|项目)?\s*/gi, "您确定要删除项目 ");
      text = text.replace(/Are you sure you want to delete\s*/gi, "您确定要删除 ");
    }
    if (text.indexOf("This will permanently delete") !== -1) {
      text = text.replace(/This will permanently delete\s*/gi, "这将永久删除包含在其中的 ");
    }
    if (text.indexOf("within it") !== -1) {
      text = text.replace(/\s*within it\.?/gi, "");
    }
    if (text.indexOf("Google Developer Knowledge") !== -1 || text.indexOf("official developer documentation and retrieve") !== -1) {
      return "Google Developer Knowledge MCP 服务器使 AI 驱动的开发工具能够搜索 Google 的官方开发者文档并检索相关内容...";
    }
    if (text.indexOf("Ask questions. Get answers") !== -1) {
      if (text.indexOf("PostHog") !== -1) {
        return "提出问题。获取答案。该 MCP 是您的编程智能体与之对话的服务器。用英语提问，它会针对您的 PostHog 数据运行查询并返回结果。";
      }
      return "提出问题。获取答案。该 MCP 是您的 ";
    }
    if (text.indexOf("talks to. Ask a question in English") !== -1 || text.indexOf("runs the query against your") !== -1) {
      return " 与之对话的服务器。用英语提问，它会针对您的 ";
    }
    if (text.indexOf("The answer lands") !== -1 || text.indexOf("data. The answer") !== -1) {
      return " 数据运行查询并返回结果。";
    }

    if (text.indexOf("Configure the browser subagent") !== -1) {
      text = text.replace(/Configure the browser subagent\.?/g, "配置浏览器子智能体。");
    }
    if (text.indexOf("It requires") !== -1 && text.indexOf("Configure") === -1) {
      text = text.replace(/It requires\s?/g, "需要安装 ");
    }
    if (text.indexOf("to be installed.") !== -1) {
      text = text.replace(/\s?to be installed\./g, "");
    }
    if (text.indexOf("The browser subagent can be invoked by typing") !== -1) {
      text = text.replace(/The browser subagent can be invoked by typing \/browser in the conversation input box\./g, "您可以在对话输入框中输入 /browser 来调用浏览器子智能体。");
    }

    if (text.indexOf("You currently don't have any MCP Servers installed.") !== -1) {
      text = text.replace(/You currently don't have any MCP Servers installed\./g, "您目前尚未安装任何 MCP 服务器。");
    }
    if (text.indexOf("Add an MCP server above") !== -1) {
      text = text.replace(/Add an MCP server above or add a custom one via the MCP Config\./g, "请在上方添加 MCP 服务器，或通过 MCP 配置添加自定义服务器。");
    }

    // Prefix Rules Matching
    for (let i = 0; i < textPrefixRules.length; i++) {
      if (text.indexOf(textPrefixRules[i][0]) !== -1) {
        return textPrefixRules[i][1];
      }
    }

    // Short Word Exact Replacement
    let wordsCount = trimmed.split(/\s+/).length;
    if (wordsCount <= 3) {
      let lowerText = trimmed.toLowerCase();
      if (coreWords[lowerText]) {
        return text.replace(trimmed, coreWords[lowerText]);
      }
    }
    
    return text;
  }

  function processNode(node) {
    if (node.nodeType === Node.TEXT_NODE) {
      // Avoid modifying code snippets or editor content
      if (node.parentElement && node.parentElement.closest && node.parentElement.closest('pre, code, .monaco-editor')) {
        return;
      }
      const translated = translateText(node.textContent);
      if (translated !== node.textContent) {
        node.textContent = translated;
      }
    } else if (node.nodeType === Node.ELEMENT_NODE) {
      if (node.tagName === 'SCRIPT' || node.tagName === 'STYLE' || node.tagName === 'CODE' || node.tagName === 'PRE') return;
      if (node.placeholder) {
        const translated = translateText(node.placeholder);
        if (translated !== node.placeholder) {
          node.placeholder = translated;
        }
      }
      if (node.title) {
        const translated = translateText(node.title);
        if (translated !== node.title) {
          node.title = translated;
        }
      }
      if (node.getAttribute && node.getAttribute('aria-label')) {
        const ariaLabel = node.getAttribute('aria-label');
        const translated = translateText(ariaLabel);
        if (translated !== ariaLabel) {
          node.setAttribute('aria-label', translated);
        }
      }
      // Recursively process child nodes
      Array.from(node.childNodes).forEach(processNode);
    }
  }

  const observer = new MutationObserver((mutations) => {
    mutations.forEach(mutation => {
      if (mutation.type === 'childList') {
        mutation.addedNodes.forEach(node => {
          processNode(node);
        });
      } else if (mutation.type === 'characterData') {
        processNode(mutation.target);
      }
    });
  });

  document.addEventListener('DOMContentLoaded', () => {
    processNode(document.body);
    observer.observe(document.body, {
      childList: true,
      subtree: true,
      characterData: true
    });
  });
})();
"""

MENU_TRANSLATOR_INJECTION = r"""
// Antigravity Chinese Localization Engine - Menu
(function() {
  const menuTranslationMap = {
    'File': '文件', 'Edit': '编辑', 'View': '视图', 'Window': '窗口', 'Help': '帮助',
    'New Conversation': '新建对话', 'New Window': '新建窗口', 'Close Window': '关闭窗口',
    'Check for Updates': '检查更新', 'Checking for Updates...': '正在检查更新...',
    'Downloading Update...': '正在下载更新...', 'Restart to Update': '重启以应用更新',
    'Undo': '撤销', 'Redo': '重做', 'Cut': '剪切', 'Copy': '复制', 'Paste': '粘贴',
    'Select All': '全选', 'Minimize': '最小化', 'Close': '关闭', 'Quit Antigravity': '退出 Antigravity',
    'About Antigravity': '关于 Antigravity', 'Services': '服务', 'Hide Antigravity': '隐藏 Antigravity',
    'Hide Others': '隐藏其他', 'Show All': '显示全部', 'Force Reload': '强制重新加载',
    'Reload': '重新加载', 'Actual Size': '实际大小', 'Zoom In': '放大', 'Zoom Out': '缩小',
    'Toggle Full Screen': '切换全屏'
  };
  function translateMenu(menuItem) {
    if (menuItem.label && menuTranslationMap[menuItem.label]) {
      menuItem.label = menuTranslationMap[menuItem.label];
    }
    if (menuItem.submenu && menuItem.submenu.items) {
      menuItem.submenu.items.forEach(translateMenu);
    }
    if (menuItem.submenu && Array.isArray(menuItem.submenu)) {
      menuItem.submenu.forEach(translateMenu);
    }
  }

  try {
    const { Menu } = require('electron');
    if (Menu && Menu.buildFromTemplate && !Menu.__isTranslated) {
      const originalBuildFromTemplate = Menu.buildFromTemplate;
      Menu.buildFromTemplate = function(template) {
        if (template && Array.isArray(template)) {
          template.forEach(translateMenu);
        }
        return originalBuildFromTemplate.call(this, template);
      };
      Menu.__isTranslated = true;
    }
  } catch(e) {
    console.error("Menu hooking failed:", e);
  }
})();
"""

def extract_asar(asar_path, dest_dir):
    """Pure-Python asar archive extractor."""
    with open(asar_path, 'rb') as f:
        data = f.read(16)
        magic, size, u1, header_size = struct.unpack('<4I', data)
        header_json = f.read(header_size).decode('utf-8')
        header = json.loads(header_json)
        base_offset = 8 + size
        
        def extract_node(node, current_path):
            if not os.path.exists(current_path):
                os.makedirs(current_path)
            for name, info in node.items():
                path = os.path.join(current_path, name)
                if 'files' in info:
                    extract_node(info['files'], path)
                elif 'offset' in info:
                    f.seek(base_offset + int(info['offset']))
                    file_data = f.read(int(info['size']))
                    with open(path, 'wb') as out_f:
                        out_f.write(file_data)
        
        extract_node(header.get('files', {}), dest_dir)

def append_once(file_path, content, marker, name):
    if not os.path.exists(file_path):
        print(f"[警告] 未找到文件 {os.path.basename(file_path)}，已跳过注入 {name}。")
        return
    
    with open(file_path, "r", encoding="utf-8") as f:
        existing = f.read()
    
    if marker in existing:
        print(f"[状态] 发现已存在的 {name}，正在热更新词典...")
        idx = existing.find("// " + marker)
        if idx == -1:
            idx = existing.find(marker)
        if idx != -1:
            clean_content = existing[:idx].rstrip()
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(clean_content + "\n" + content + "\n")
            print(f"[成功] 词典热更新完成：{name} ({os.path.basename(file_path)})")
        return
    
    with open(file_path, "a", encoding="utf-8") as f:
        f.write("\n" + content + "\n")
    print(f"[成功] 注入完成：{name} ({os.path.basename(file_path)})")

def replace_in_file(file_path, target, replacement):
    if not os.path.exists(file_path):
        return
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    if replacement in content:
        print(f"[跳过] 目标已替换 ({os.path.basename(file_path)})")
        return
    content = content.replace(target, replacement)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"[成功] 执行目标替换 ({os.path.basename(file_path)})")

def apply_patch():
    print("==================================================================")
    print("                                                                ")
    print("              Antigravity v2.8.1 桌面端 一键汉化补丁               ")
    print("Github 开源项目地址：https://github.com/MIMICTE/Antigravity-zh-CN")
    print("                                                                ")
    print("==================================================================")
    print("                                                                ")
    print("[执行] 正在为您关闭 Antigravity 程序...")
    os.system("taskkill /F /IM Antigravity.exe >nul 2>&1")

    # 1. 确保 unpacked app 文件夹存在
    if not os.path.exists(UNPACKED_APP_DIR):
        if not os.path.exists(ASAR_PATH):
            print(f"[错误] Cannot find app.asar at {ASAR_PATH} or {UNPACKED_APP_DIR}")
            return False

        print("[执行] 正在提取 app.asar 核心文件 (使用原生 Python 解析器)...")
        try:
            extract_asar(ASAR_PATH, UNPACKED_APP_DIR)
            print("[完成] 文件提取完毕.")
        except Exception as e:
            print(f"[错误] 提取 app.asar 失败: {e}")
            return False
    else:
        print(f"[状态] 发现已解包的工作目录: {UNPACKED_APP_DIR}")

    # 2. 注入各个组件
    preload_path = os.path.join(UNPACKED_APP_DIR, "dist", "preload.js")
    menu_path = os.path.join(UNPACKED_APP_DIR, "dist", "menu.js")
    tray_path = os.path.join(UNPACKED_APP_DIR, "dist", "tray.js")

    append_once(preload_path, DOM_TRANSLATOR_INJECTION, "Antigravity Chinese Localization Engine", "Web UI Injection")
    append_once(menu_path, MENU_TRANSLATOR_INJECTION, "Antigravity Chinese Localization Engine - Menu", "Menu Translator Injection")

    replace_in_file(tray_path, "'Show Antigravity'", "'显示 Antigravity'")
    replace_in_file(tray_path, "'Quit'", "'退出'")

    # 3. 汉化 loadingOverlay (Splash Screen)
    loading_path = os.path.join(UNPACKED_APP_DIR, "dist", "loadingOverlay.js")
    if os.path.exists(loading_path):
        with open(loading_path, "r", encoding="utf-8") as f:
            loading_content = f.read()
        patched_loading = loading_content.replace(">Loading Antigravity<", ">正在加载 Antigravity<")
        if patched_loading != loading_content:
            with open(loading_path, "w", encoding="utf-8") as f:
                f.write(patched_loading)
            print(f"[成功] 已成功汉化启动加载界面 ({os.path.basename(loading_path)})")

    # 4. 禁用原生 app.asar
    if os.path.exists(ASAR_PATH):
        print("[执行] 正在禁用官方 app.asar，以强制读取汉化代码...")
        os.rename(ASAR_PATH, ASAR_PATH + ".disabled")
        print("[成功] app.asar -> app.asar.disabled")

    print("                                                                ")
    print("==================================================================")
    print("                                                                ")
    print("       汉化补丁注入成功！正在为您自动启动 Antigravity...              ")
    print("                                                                ")
    print("==================================================================")
    
    exe_path = os.path.join(APP_DIR, "Antigravity.exe")
    if os.path.exists(exe_path):
        DETACHED_PROCESS = 0x00000008
        CREATE_NEW_PROCESS_GROUP = 0x00000200
        subprocess.Popen(
            [exe_path],
            stdin=subprocess.DEVNULL,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            creationflags=DETACHED_PROCESS | CREATE_NEW_PROCESS_GROUP,
            close_fds=True
        )
    return True

if __name__ == "__main__":
    apply_patch()
