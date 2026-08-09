# coding: utf-8
import os
import json
import platform

if platform.system() == 'Darwin':
    APP_DIR = '/Applications/Antigravity.app'
    RESOURCES_DIR = os.path.join(APP_DIR, 'Contents', 'Resources')
else:
    APP_DIR = os.path.join(os.environ.get('LOCALAPPDATA', ''), 'Programs', 'antigravity')
    RESOURCES_DIR = os.path.join(APP_DIR, "resources")

ASAR_PATH = os.path.join(RESOURCES_DIR, "app.asar")
UNPACKED_APP_DIR = os.path.join(RESOURCES_DIR, "app")

DOM_TRANSLATOR_INJECTION = r"""
// Antigravity Chinese Localization Engine
(function() {
  const dictionary = {
    "Goals": "目标", "Tasks": "任务", "Artifacts": "工件", "Scratch": "草稿", "Chat": "对话",
    "Active": "进行中", "Inactive": "未激活", "Completed": "已完成", "Failed": "已失败",
    "History": "历史记录", "Settings": "设置", "System": "系统", "Network": "网络",
    "Model": "模型", "Memory": "记忆", "Tools": "工具", "Agents": "智能体",
    "Overview": "概览", "Logs": "日志", "Clear": "清除", "Save": "保存",
    "Cancel": "取消", "Submit": "提交", "Run": "运行", "Stop": "停止",
    "Edit": "编辑", "Delete": "删除", "Add": "添加", "Remove": "移除",
    "Monthly Limit": "每月限额", "limit": "限额", "limits": "限额", "weekly": "每周", "hourly": "每小时",
    "Sidebar": "侧边栏", "Display Options": "显示选项", "Message input": "消息输入框", "Record voice memo": "录制语音备忘",
    "Typeahead menu": "预输入菜单", "Group By": "分组方式", "Last Updated": "最后更新",
    "Alphabetical (A-Z)": "字母顺序 (A-Z)", "Date Added": "添加日期", "Subtitles": "副标题", "No Subtitle": "无副标题",
    "Filter": "筛选", "Scheduled": "已计划", "Environment": "环境", "None": "无", "Fast": "快速",
    "Project": "项目", "project": "项目", "projects": "项目", "Conversation": "对话", "conversation": "对话",
    "Workspace": "工作区", "workspace": "工作区", "Minimize": "最小化", "Maximize": "最大化", "Back": "返回",
    "Folders": "文件夹", "folders": "文件夹", "including": "包括",
    "Rename": "重命名", "Mark Unread": "标记为未读", "Mark Read": "标记为已读", "Duplicate": "制作副本",
    "Export": "导出", "Import": "导入",
    // New Settings Vocabulary
    "General": "常规", "Appearance": "外观", "Theme": "主题", "Light": "浅色", "Dark": "深色",
    "Language": "语言", "Version": "版本", "Check for Updates": "检查更新", "About": "关于",
    "Advanced": "高级", "API Key": "API 密钥", "Account": "账号", "Profile": "个人资料",
    "Logout": "退出登录", "Sign Out": "退出登录", "Feedback": "反馈", "Privacy": "隐私",
    "Terms": "条款", "Auto-start": "开机自启", "Launch on startup": "开机时启动",
    "Notifications": "通知", "Shortcuts": "快捷键", "Keyboard Shortcuts": "键盘快捷键",
    "Global Shortcut": "全局快捷键", "Toggle Visibility": "切换显示/隐藏", "Proxy": "代理",
    "Update": "更新", "Updates": "更新", "Check for update": "检查更新",
    "Models": "模型", "Customizations": "自定义", "Browser": "浏览器", "App": "应用",
    "Projects": "项目", "Conversations": "对话", "Provide Feedback": "提供反馈",
    "+ New Conversation": "+ 新建对话", "New Conversation": "新建对话", "Conversation History": "历史对话", "Scheduled Tasks": "计划任务",
    "No conversations yet": "暂无对话", "Open IDE": "打开 IDE", "Window": "窗口",
    "Review": "审阅", "Email": "电子邮箱", "Upgrade": "升级", "Not in Project": "未分组项目",
    "Manage your plan, credentials, and general preferences.": "管理您的套餐、凭据和常规偏好设置。",
    "Enable Telemetry": "启用遥测",
    "When toggled on, Antigravity collects usage data to help Google enhance performance and features.": "开启后，Antigravity 将收集使用数据，以帮助 Google 提升性能和功能。",
    "Marketing Emails": "营销邮件",
    "Receive product updates, tips, and promotions from Google Antigravity via email.": "通过电子邮件接收来自 Google Antigravity 的产品更新、提示和促销信息。",
    "Your Plan: Google AI Pro": "您的套餐: Google AI Pro",
    "You can upgrade to a Google AI Ultra plan to receive higher rate limits.": "您可以升级至 Google AI Ultra 套餐以获得更高的使用限额。",
    "By using this app, you agree to its ": "使用本应用即表示您同意其 ",
    "Terms of Service": "服务条款",
    "Ask anything, @ to mention, / for actions": "输入任何问题，使用 @ 提及，使用 / 执行操作",
    // Customizations Page
    "Configure default behaviors, skills, and MCP servers.": "配置默认行为、技能和 MCP 服务器。",
    "Learn more.": "了解更多。", "Learn more": "了解更多",
    "Token Usage": "Token 使用量",
    "The breakdown below shows token usage from customizations like skills, rules, and MCP. If the budget is exceeded, large customizations will be truncated automatically.": "下方的明细展示了来自技能、规则和 MCP 等自定义项的 Token 使用情况。如果超出预算，大型自定义项将被自动截断。",
    "Skills": "技能", "Rules": "规则",
    "Installed MCP Servers": "已安装的 MCP 服务器",
    "Add MCP +": "添加 MCP +", "Add MCP": "添加 MCP",
    "Refresh": "刷新",
    "Open MCP Config": "打开 MCP 配置",
    "No MCP Servers": "无 MCP 服务器",
    "You currently don't have any MCP Servers installed. Add an MCP server above or add a custom one via the MCP Config.": "您目前尚未安装任何 MCP 服务器。请在上方添加 MCP 服务器，或通过 MCP 配置添加自定义服务器。",
    "Build With Google Plugins": "使用 Google 插件构建",
    "Customize": "自定义",
    // Main UI Menus
    "Status": "状态", "Sort Conversations": "对话排序", "Worktree": "工作区树",
    "New Project": "新建项目", "Quick Start": "快速开始",
    // General Settings Page
    "Configure agent execution, queued message delivery, and permissions.": "配置智能体执行、排队消息发送以及权限。",
    "Execution": "执行", "Agent Settings": "智能体设置", "Agent Behavior": "智能体行为",
    "File Permissions": "文件权限", "Network Permissions": "网络权限",
    "Queued Messages": "排队消息", "Configure when follow-up messages are sent.": "配置发送后续消息的时机。",
    "Queue": "排队", "Send Immediately": "立即发送", "Keyboard shortcuts": "键盘快捷键",
    "Security Preset": "安全预设", 
    "Choose a predefined security preset for the agent. This controls terminal auto-execution policy, and file access policy.": "为智能体选择一个预定义的安全预设。这将控制终端自动执行策略和文件访问策略。",
    "Default": "默认", "Always Ask": "总是询问",
    "Artifact Review Policy": "工件审核策略",
    "Specifies Agent's behavior when asking for review on artifacts, which are documents it creates to enable a richer conversation experience.": "指定智能体在请求审核工件时的行为，工件是其为提供更丰富对话体验而创建的文档。",
    "File Access Rules": "文件访问规则", "Configure allowed and denied paths for file reads and writes.": "配置允许和拒绝的文件读取和写入路径。",
    "Network Access Rules": "网络访问规则", "Configure allowed and denied URLs for reading.": "配置允许和拒绝读取的 URL。",
    // Comprehensive Settings Panel additions
    "System Default": "跟随系统", "Zoom Level": "缩放比例", "Font Size": "字体大小",
    "Small": "小", "Medium": "中", "Large": "大", "Code Font": "代码字体", "Editor Font": "编辑器字体",
    "Default Model": "默认模型", "Temperature": "温度", "System Prompt": "系统提示词",
    "Search Engine": "搜索引擎", "Web Search": "网络搜索", "Enable Web Access": "启用网络访问",
    "Startup": "启动", "Launch at login": "登录时自动启动", "Hardware Acceleration": "硬件加速",
    "Current Version": "当前版本", "Up to date": "已是最新版本", "Downloading": "下载中...",
    "Restart to update": "重启以更新", "Danger Zone": "危险区域", "Clear History": "清除历史记录",
    "Delete All": "全部删除", "Reset to Default": "恢复默认设置", "Restore Defaults": "恢复默认值",
    "Keybindings": "快捷键绑定", "Command": "命令", "Shortcut": "快捷键", "Action": "操作",
    "Advanced Settings": "高级设置", "Developer Tools": "开发者工具", "Toggle Developer Tools": "切换开发者工具",
    "Open Logs": "打开日志", "Proxy Server": "代理服务器", "Enable Proxy": "启用代理",
    "Auto-Updater": "自动更新程序", "Always": "始终", "Never": "从不", "Ask": "询问",
    "Save changes": "保存更改", "Apply": "应用", "OK": "确定", "Features": "功能",
    "Experimental Features": "实验性功能", "Enable": "启用", "Disable": "禁用",
    "API Configuration": "API 配置", "Account Settings": "账号设置", "Profile Settings": "个人资料",
    "Workspace Settings": "工作区设置", "Manage Projects": "管理项目",
    // More Main UI
    "Create New Project": "创建新项目", "Archive Conversation": "归档对话", "now": "刚刚",
    "Pin": "置顶", "Archive": "归档",
    "Conversation Name": "对话名称", "Conversation ID": "对话 ID", "Project Name": "项目名称",
    "Toggle Auxiliary Pane": "切换辅助面板", "User cancelled agent execution.": "用户取消了智能体执行。",
    // Menus and Topbar
    "Open Antigravity IDE": "打开 Antigravity IDE", "Create Project": "创建项目", 
    "Command Palette": "命令面板", "Zoom In": "放大", "Zoom Out": "缩小", "Reset Zoom": "重置缩放",
    "Delete Conversation": "删除对话", "Are you sure you want to delete this conversation? This action cannot be undone.": "您确定要删除此对话吗？此操作无法撤销。",
    // Tooltips & Popups
    "Record Audio": "录制音频", "Record Audio Ctrl+M": "录制音频 Ctrl+M",
    "Send message": "发送消息", "Send message Enter": "发送消息 Enter",
    "Getting started with a Project": "开始使用项目",
    "Now that you've created a project, configure your project's agent settings or start a conversation.": "现在您已经创建了一个项目，接下来请配置该项目的智能体设置，或者直接开始对话。",
    "Open Settings": "打开设置", "Start first conversation": "开始首次对话",
    "Main Agent": "主智能体", "Add Context": "添加上下文",
    "Loading Antigravity": "正在加载 Antigravity", "Loading": "正在加载",
    // General Settings Dropdowns & Tooltips
    "Enter Queues after the turn": "Enter 键：在当前轮次后排队",
    "Alt+Enter Sends immediately": "Alt+Enter 键：立即发送",
    "Alt+Enter On empty prompt, sends next in queue": "Alt+Enter 键：在输入为空时，发送队列中的下一条",
    "Useful for typical development with an emphasis on security. It prioritizes safety over speed by requiring manual approval for all terminal commands and files outside the project directory.": "适用于注重安全的典型开发场景。它将安全性置于速度之上，要求对所有终端命令和项目目录之外的文件访问进行手动批准。",
    "Requires manual review for all terminal commands and file accesses outside of the working folders.": "要求对所有终端命令和工作文件夹之外的文件访问进行手动审阅。",
    "Full machine": "完整机器访问",
    "All terminal commands require review. The agent can read or write to any file in the machine.": "所有终端命令均需审阅。智能体可以读取或写入机器上的任何文件。",
    "Turbo mode": "极速模式",
    "Disables all safety barriers for maximal iteration velocity.": "禁用所有安全屏障，以获得最快的迭代速度。",
    "Custom": "自定义配置",
    "Manually customize individual settings.": "手动自定义各项设置。",
    // Terminal & Tooling Permissions
    "Terminal & Tooling Permissions": "终端与工具权限",
    "Terminal Commands": "终端命令", "Configure allowed terminal commands.": "配置允许执行的终端命令。",
    "Commands Outside Sandbox": "沙盒外命令", "Configure allowed commands outside the sandbox.": "配置允许在沙盒外执行的命令。",
    "MCP Tools": "MCP 工具", "Configure external tools via Model Context Protocol.": "通过模型上下文协议配置外部工具。",
    // Models Tab
    "Models & Usage": "模型与用量", "Manage your model quota and credits.": "管理您的模型配额和积分额度。",
    "Plan": "订阅计划", "Your Plan: Google AI Pro": "当前计划：Google AI Pro",
    "Your Plan:": "当前计划：", "Your Plan: ": "当前计划：",
    "Model Credits": "模型积分", "Enable AI Credit Overages": "启用 AI 积分超额使用",
    "When toggled on, Antigravity will use your AI credits to fulfill model requests once you're out of model quota. Antigravity will always use your model quota first before using AI credits.": "启用后，当您的模型配额用尽时，Antigravity 将使用您的 AI 积分来完成模型请求。Antigravity 将始终优先使用模型配额。",
    "See Activity": "查看活动", "Get More AI Credits": "获取更多 AI 积分",
    "Available AI Credits:": "可用 AI 积分：", "Available AI Credits: ": "可用 AI 积分：",
    "Gemini Models": "Gemini 模型", "Weekly Limit": "每周限额", "Five Hour Limit": "五小时限额",
    "Claude and GPT models": "Claude 和 GPT 模型",
    // Custom Tab (MCP Empty state)
    "You currently don't have any MCP Servers installed. Add an MCP server above or add a custom one via the MCP Config.": "您目前没有安装任何 MCP 服务器。请在上方添加 MCP 服务器，或通过 MCP 配置添加自定义服务器。",
    // Shortcuts Panel
    "Configure keyboard shortcuts.": "配置键盘快捷键。",
    "Keyboard shortcuts for quick navigation and control.": "用于快速导航和控制的键盘快捷键。",
    "RECOMMENDED": "推荐", "NAVIGATION": "导航",
    "Recommended": "推荐", "Navigation": "导航",
    "Open Conversation Picker": "打开对话选择器", "Open File Search": "打开文件搜索",
    "Focus Input": "聚焦输入框", "File Picker": "文件选择器",
    "Select Previous Conversation": "选择上一个对话", "Select Next Conversation": "选择下一个对话",
    "Previous Pane Tab": "上一个面板标签", "Next Pane Tab": "下一个面板标签",
    "Toggle Model Selector": "切换模型选择器", "Toggle Voice Recording": "切换语音录制",
    "Find in Pane": "在面板中查找", "Add to Chat/Quote": "添加到对话/引用",
    "LAYOUT CONTROLS": "布局控制", "Layout Controls": "布局控制", "Layout controls": "布局控制",
    "App Shortcuts": "应用快捷键", "Editor Shortcuts": "编辑器快捷键", 
    "Global Shortcuts": "全局快捷键", "Terminal Shortcuts": "终端快捷键", 
    "Chat Shortcuts": "对话快捷键", "Press desired key combination": "按下所需的组合键", 
    "Reset to default": "恢复默认", "Restore defaults": "恢复默认设置",
    // Tooltips and Chat UI
    "Good response": "好的回答", "Bad response": "差的回答",
    // Feedback Panel
    "Feedback Type": "反馈类型", "Auth and Billing": "认证与计费",
    "Description": "描述",
    "Please describe the issue in detail. The more actionable your feedback, the quicker our team can address your request. Some helpful information includes:": "请详细描述您的问题。您的反馈越具体，我们的团队就能越快处理您的请求。一些有用的信息包括：",
    "Steps to reproduce the issue": "重现问题的步骤", "Expected behavior": "预期行为",
    "Actual behavior": "实际行为", "Any error messages": "任何错误消息",
    "Any relevant information": "任何相关信息",
    "Describe the bug you encountered...": "描述您遇到的错误...",
    "Steps to Reproduce": "重现步骤", "Please list the steps to reproduce the issue...": "请列出重现问题的步骤...",
    "Please list the steps to reproduce the issue": "请列出重现问题的步骤",
    "Attach a screenshot (optional)": "附加截图（可选）", "Attach Antigravity server logs": "附加 Antigravity 服务器日志",
    "We'd love to hear from you.": "我们期待您的反馈。", "How can we improve?": "我们该如何改进？",
    // AI Status and Thoughts
    "Thinking...": "思考中...", "Thought": "思考过程", "Agent is thinking...": "智能体正在思考...",
    "Show thought process": "显示思考过程", "Hide thought process": "隐藏思考过程",
    "Generating...": "生成中...", "Planning...": "计划中...",
    "Issue Type": "问题类型", "Bug Report": "错误报告", "Feature Request": "功能请求",
    "General Feedback": "常规反馈", "Describe your issue or idea...": "描述您的问题或想法...",
    "Please provide details...": "请提供详细信息...", "Include diagnostic data": "包含诊断数据",
    "Include app logs": "包含应用日志", "Send Feedback": "发送反馈",
    // Custom Tab Additions
    "Hide breakdown": "隐藏明细",
    "Provides a comprehensive guide, quick reference, and sitemap for Google Antigravity (AGY), including the Antigravity CLI (agy), Antigravity 2.0, Antigravity IDE, Python SDK, slash commands,...": "提供 Google Antigravity (AGY) 的综合指南、快速参考和站点地图，包括 Antigravity CLI、Antigravity 2.0、IDE、Python SDK、斜杠命令...",
    "Provides a comprehensive guide, quick reference, and sitemap for Google Antigravity (AGY), including the Antigravity CLI (agy), Antigravity 2.0, Antigravity IDE, Python SDK, slash commands, keybindings, and customizations (skills, rules, MCP, sidecars).": "提供 Google Antigravity (AGY) 的综合指南、快速参考和站点地图，包括 Antigravity CLI、Antigravity 2.0、IDE、Python SDK、斜杠命令、快捷键和自定义项。",
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
    // App Tab
    "App Settings": "应用设置", "Manage application settings.": "管理应用设置。",
    "Prevent Sleep": "阻止睡眠", "Prevent the computer from sleeping while the app is running.": "在应用运行时阻止计算机进入睡眠状态。",
    "Keep In Menu Bar": "保留在系统托盘", "The app will be accessible from the menu bar and will keep running in the background when all windows are closed.": "应用将可以从系统托盘访问，并在所有窗口关闭时继续在后台运行。",
    "Notification Settings": "通知设置", "To modify notification settings, open your operating system's system preferences.": "要修改通知设置，请打开操作系统的系统偏好设置。",
    "Open System Preferences": "打开系统偏好设置",
    // Conversations Tab
    "Agent settings and permissions for conversations outside of projects.": "针对项目外对话的智能体设置和权限。",
    "Inherit General": "继承全局设置", "Local Permissions": "本地权限",
    "Also includes": "还包括", "global settings": "全局设置",
    "when working in this project.": "（当在此项目中工作时）。",
    // Customization Budget fallback
    "99.2% of the customization budget is available.": "自定义项预算可用额度为 99.2%。",
    "100% of the customization budget is available.": "自定义项预算可用额度为 100%。",
    "of the customization budget is available.": "的自定义项预算可用额度。",
    // Appearance Tab & Fixes
    "Toggle Sidebar": "切换侧边栏", "View Split Diff": "分屏查看差异", "Collapse All": "全部折叠",
    "Learn more about": "了解更多关于", "Learn more about ": "了解更多关于 ",
    "Configure the agent's visual theme and display preferences.": "配置智能体的视觉主题和显示偏好。",
    "Chat Settings": "聊天设置", "Verbose Agent Chat": "详细的智能体对话",
    "Display and preserve intermediate thinking steps.": "显示并保留中间思考过程。",
    "Conversation Width": "对话宽度", "Configure the maximum width of the conversation panel.": "配置对话面板的最大宽度。",
    "Narrow": "较窄", "Wide": "较宽",
    "Select light, dark, or inherit system settings.": "选择浅色、深色，或跟随系统设置。",
    "Light Theme": "浅色主题", "Preset": "预设", "Default Light": "默认浅色",
    "Background": "背景颜色", "Foreground": "前景颜色", "Accent": "强调色",
    "Dark Theme": "深色主题", "Default Dark": "默认深色",
    // Permission Dialog
    "Allow write access to this path?": "允许写入此路径吗？",
    "Allow read access to this path?": "允许读取此路径吗？",
    "Allow execution of this command?": "允许执行此命令吗？",
    "Yes, allow this time": "是，仅本次允许",
    "Yes, and always allow in this conversation": "是，在本次对话中始终允许",
    "Yes, and always allow when not in a project": "是，在未分组项目中始终允许",
    "Yes, and always allow": "是，始终允许",
    "tell the agent what to do instead": "告诉智能体接下来该做什么",
    "(tell the agent what to do instead)": "(告诉智能体接下来该做什么)",
    "Skip": "跳过",
    "Working.": "运行中。",
    "Working...": "运行中...",
    "Edited": "已编辑",
    "Viewed": "已查看",
    "Created": "已创建",
    "Deleted": "已删除",
    "Executed": "已执行",
    // Save Rule Dialog
    "Save rule to always allow write access to this path?": "保存规则以始终允许写入此路径吗？",
    "Save rule to always allow read access to this path?": "保存规则以始终允许读取此路径吗？",
    "Save rule to always allow execution of this command?": "保存规则以始终允许执行此命令吗？",
    "Yes, save rule in this conversation": "是，在本次对话中保存规则",
    "Yes, save rule when not in a project": "是，在未分组项目中保存规则",
    "Yes, save rule globally": "是，全局保存规则"
  };

  const coreWords = {
    "create": "创建", "delete": "删除", "new": "新建", "edit": "编辑", "save": "保存", "cancel": "取消", "confirm": "确认",
    "close": "关闭", "open": "打开", "stop": "停止", "start": "启动", "run": "运行", "add": "添加", "remove": "移除",
    "update": "更新", "select": "选择", "clear": "清除", "search": "搜索", "find": "查找", "view": "查看", "show": "显示", "hide": "隐藏",
    "copy": "复制", "paste": "粘贴", "cut": "剪切", "rename": "重命名", "duplicate": "制作副本",
    "agent": "智能体", "agents": "智能体", "subagent": "子智能体", "subagents": "子智能体", "task": "任务", "tasks": "任务",
    "workspace": "工作区", "workspaces": "工作区", "directory": "目录", "folder": "文件夹", "file": "文件", "files": "文件",
    "command": "命令", "commands": "命令", "terminal": "终端", "console": "控制台", "output": "输出", "input": "输入",
    "error": "错误", "warning": "警告", "info": "信息", "success": "成功", "failed": "失败", "pending": "等待中", "running": "运行中",
    "yes": "是", "no": "否", "true": "真", "false": "假", "on": "开", "off": "关", "enable": "启用", "disable": "禁用"
  };

  function translateText(text) {
    if (!text || typeof text !== 'string') return text;
    let trimmed = text.trim();
    if (!trimmed) return text;

    if (dictionary[trimmed]) {
      return text.replace(trimmed, dictionary[trimmed]);
    }
    
    // Dynamic Regex Translations
    let m;
    if ((m = trimmed.match(/^(\d+(\.\d+)?)% of the customization budget is available\.$/))) {
      return text.replace(trimmed, "自定义项预算可用额度为 " + m[1] + "%。");
    }
    if ((m = trimmed.match(/^Show (\d+) breakdown$/))) {
      return text.replace(trimmed, "显示 " + m[1] + " 项明细");
    }
    if ((m = trimmed.match(/^Show (\d+) breakdowns$/))) {
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
    if ((m = trimmed.match(/^(\+?\d+) more lines$/))) {
      return text.replace(trimmed, "更多 " + m[1] + " 行");
    }
    if ((m = trimmed.match(/^(\d+) files? changed$/))) {
      return text.replace(trimmed, m[1] + " 个文件已修改");
    }
    // Bulletproof fallback replacements for stubborn text fragments
    if (text.indexOf("Configure the browser subagent") !== -1) {
      text = text.replace(/Configure the browser subagent\.?/g, "配置浏览器子智能体。");
    }
    if (text.indexOf("It requires") !== -1 && text.indexOf("Configure") === -1) {
      text = text.replace(/It requires\s?/g, "需要安装 ");
    }
    if (text.indexOf("to be installed.") !== -1) {
      text = text.replace(/\s?to be installed\./g, ""); // "Google Chrome to be installed" -> "Google Chrome" since we put "需要安装" before it.
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
    if (text.indexOf("of the customization budget is available") !== -1) {
      text = text.replace(/(\d+(?:\.\d+)?)% of the customization budget is available\.?/g, "自定义项预算可用额度为 $1%。");
      text = text.replace(/%\s*of the customization budget is available\.?/g, "% 的自定义项预算可用额度。");
      text = text.replace(/(^\s*)of the customization budget is available\.?/g, "$1的自定义项预算可用额度。");
    }
    if (text.indexOf("Worked for") !== -1) {
      text = text.replace(/Worked for ([\d\.a-z ]+)/gi, function(match, timeStr) {
        let translatedTime = timeStr.replace(/ms/g, "毫秒").replace(/s/g, "秒").replace(/m/g, "分").replace(/h/g, "小时");
        return "运行耗时 " + translatedTime;
      });
    }
    if (text.indexOf("Working") !== -1) {
      text = text.replace(/Working(\.*)/g, "运行中$1");
    }
    if (text.indexOf("Thought for") !== -1) {
      text = text.replace(/Thought for ([\d\.a-z ]+)/gi, function(match, timeStr) {
        let translatedTime = timeStr.replace(/ms/g, "毫秒").replace(/s/g, "秒").replace(/m/g, "分").replace(/h/g, "小时");
        return "思考耗时 " + translatedTime;
      });
    }
    
    // Bulletproof skill description match
    if (text.indexOf("Provides a comprehensive guide") !== -1 && text.indexOf("quick reference") !== -1) {
      return "提供 Google Antigravity (AGY) 的综合指南、快速参考和站点地图，包括 Antigravity CLI、Antigravity 2.0、IDE、Python SDK、斜杠命令、快捷键和自定义项。";
    }

    if ((m = trimmed.match(/^Version ([\d\.]+(-\w+)?)$/))) {
      return text.replace(trimmed, "版本 v" + m[1]);
    }
    if ((m = trimmed.match(/^(\d+)s$/))) {
      return text.replace(trimmed, m[1] + "秒前");
    }
    if ((m = trimmed.match(/^(\d+)m$/))) {
      return text.replace(trimmed, m[1] + "分钟前");
    }
    if ((m = trimmed.match(/^(\d+)h$/))) {
      return text.replace(trimmed, m[1] + "小时前");
    }
    if ((m = trimmed.match(/^(\d+)d$/))) {
      return text.replace(trimmed, m[1] + "天前");
    }

    let wordsCount = trimmed.split(/\s+/).length;
    if (wordsCount > 3) return text;

    let lowerText = trimmed.toLowerCase();
    if (coreWords[lowerText]) {
      return text.replace(trimmed, coreWords[lowerText]);
    }
    
    return text;
  }

  function processNode(node) {
    if (node.nodeType === Node.TEXT_NODE) {
      const translated = translateText(node.textContent);
      if (translated !== node.textContent) {
        node.textContent = translated;
      }
    } else if (node.nodeType === Node.ELEMENT_NODE) {
      if (node.tagName === 'SCRIPT' || node.tagName === 'STYLE') return;
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

def apply_patch():
    print("=======================================================")
    print("          Antigravity v2.5.0 桌面端 一键汉化补丁")
    print("=======================================================")
    print("\n[执行] 正在为您关闭 Antigravity 程序...")
    if platform.system() == 'Darwin':
        os.system("pkill -9 -f Antigravity >/dev/null 2>&1")
    else:
        os.system("taskkill /F /IM Antigravity.exe >nul 2>&1")

    # 1. 确保 unpacked app 文件夹存在
    if not os.path.exists(UNPACKED_APP_DIR):
        if not os.path.exists(ASAR_PATH):
            print(f"[错误] Cannot find app.asar at {ASAR_PATH} or {UNPACKED_APP_DIR}")
            return False
        

        print("[执行] 正在提取 app.asar 核心文件 (使用原生 Python 解析器)...")
        import struct
        def extract_asar(asar_path, dest_dir):
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

    # 2.5 汉化 loadingOverlay (Splash Screen)
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
        print("\n[执行] 正在禁用官方 app.asar，以强制读取汉化代码...")
        os.rename(ASAR_PATH, ASAR_PATH + ".disabled")
        print("[成功] app.asar -> app.asar.disabled")

    print("\n=======================================================")
    print("  汉化补丁注入成功！正在为您自动启动 Antigravity v2.5.0...")
    print("=======================================================")
    if platform.system() == 'Darwin':
        os.system(f"open '{APP_DIR}'")
    else:
        exe_path = os.path.join(APP_DIR, "Antigravity.exe")
        if os.path.exists(exe_path):
            os.startfile(exe_path)
    return True

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


if __name__ == "__main__":
    apply_patch()
