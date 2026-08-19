# Commercial API Scaffold

这是商业网站 V1 的后端骨架，当前只暴露确定性八字排盘接口，AI 解读尚未接入。

## 本地启动

在仓库根目录：

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
pip install -r requirements.txt
uvicorn apps.api.app.main:app --reload
```

打开：

```text
http://127.0.0.1:8000/docs
```

## API

### GET /health

健康检查。

### POST /v1/bazi/chart

示例：

```json
{
  "solar_date": "1990-05-15",
  "birth_time": "12:00",
  "sex": "男",
  "birth_place": "北京"
}
```

当前接口只输出排盘事实，不生成“命运结论”。下一阶段将在独立 AI Gateway 中完成解释层，防止 AI 改写确定性盘面。

## 下一步

1. 添加 lunar-python 交叉核验 Adapter；
2. 实现真太阳时；
3. 把 pai_pan.py 拆为可测试的 engine 包；
4. 增加 PostgreSQL / Redis；
5. 增加用户、命盘和报告版本模型；
6. 增加 AI Gateway；
7. 增加内容安全策略与审计日志。
