# Request Random Jokes

一个 AI Skill，随机从公开 API 获取笑话、段子或毒鸡汤。
已经上传到 ClawHub，欢迎安装使用！

## 安装

在通过 ClawHub 安装：

```
clawhub install request-random-jokes
```

或手动克隆到本地 skills 目录：

```bash
git clone https://github.com/Aolinlu/request-random-jokes.git
```

## 支持的内容类型

| 参数 | 类型 | 说明 |
|------|------|------|
| `xiaohua` | 笑话 | 随机笑话 |
| `duanzi` | 段子 | 随机搞笑段子 |
| `dujitang` | 毒鸡汤 | 随机毒鸡汤语录 |

## 使用方法

```bash
# 随机获取一条内容（自动随机选择类型）
python request_random_jokes.py

# 指定类型
python request_random_jokes.py xiaohua
python request_random_jokes.py duanzi
python request_random_jokes.py dujitang
```

## 依赖

```bash
pip install requests
```
