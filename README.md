# MBTI性格测试系统

这是一个基于Flask框架开发的简单MBTI性格测试网站，用户可以通过回答4个核心问题来了解自己的MBTI性格类型。

## 功能特点

- 简洁的用户界面
- 4个核心MBTI维度测试题
- 即时计算并显示测试结果
- 支持重新测试功能

## 技术栈

- Python 3
- Flask
- HTML/CSS

## 安装说明

1. 克隆项目
ihoo
```bash
git clone https://github.com/ihoo/mbti_test.git
cd mbti-test
```

2. 安装依赖

```bash
pip install -r requirements.txt
```

3. 运行项目

```bash
python app.py
```

访问 `https://f0c65c89-f603-49c1-86ef-1c7eb122893b-00-5tmabap187sx.sisko.replit.dev/` 即可使用测试系统。

## 项目结构

```
项目根目录/
├── app.py              # 主应用程序文件
├── templates/          # HTML模板文件
│   ├── index.html     # 测试题页面
│   └── result.html    # 结果显示页面
├── requirements.txt    # 项目依赖
└── README.md          # 项目说明文档
```

## MBTI维度说明

测试包含四个维度：
- E(外向) vs I(内向)
- S(感知) vs N(直觉)
- T(思考) vs F(情感)
- J(判断) vs P(知觉)

## 部署说明

项目已配置好在Replit平台运行，支持以下部署方式：
- Cloud Run 部署
- Replit 在线运行

## 开发者

如果你想贡献代码，欢迎提交 Pull Request。

## 许可证ihoo

MIT License

## 联系方式

- 项目链接: [https://github.com/ihoooohi/mbti_test](https://github.com/ihoooohi/mbti_test)
