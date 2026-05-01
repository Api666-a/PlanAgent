
class TaskPlanner:
    def __init__(self):
        self.rules = {
            "网站": ["需求分析", "设计页面结构", "前端开发", "后端开发", "部署上线"],
            "学习": ["查资料", "整理笔记", "练习", "复盘总结"],
            "项目": ["需求分析", "技术选型", "开发实现", "测试", "发布"],
        }

    def plan(self, task: str):
        for key in self.rules:
            if key in task:
                return self.rules[key]
        return [task]
