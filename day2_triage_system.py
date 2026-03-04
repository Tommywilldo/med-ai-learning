# 1. 模拟一个病人列表，每个病人是一个字典（这是工业级 RAG 数据的常见结构）
patients_data = [
    {"name":"病人A","psa":2.5,"age":55},
    {"name":"病人B","psa":8.2,"age":70},
    {"name":"病人C","psa":15.0,"age":65}
]
print("---泌尿外科自动化分诊系统（演示版）---")

# 2. 遍历列表（Day 3 会深讲循环，今天先体验）
for p in patients_data:
    name = p["name"]
    psa = p["psa"]

    # 3. 嵌套逻辑判断
    if psa > 10:
        risk_level = "🚨 高危"
    elif psa > 4:
        risk_level = "⚠️ 中危"
    else:
        risk_level = "✅ 低危"

    print(f"患者:{name}| PSA:{psa}| 评估结果: {risk_level}")

# 延续之前的 report 字典
report = {
    "name": "张三",
    "symptoms": ["尿频", "排尿困难", "血尿"]
}

# 设置要查找的症状
target_symptom = "血尿"

# 逻辑检查
if target_symptom in report["symptoms"]:
    print(f"⚠️ 警报：患者 {report['name']} 存在核心症状: {target_symptom}，请优先排查！")
else:
    print(f"未发现症状: {target_symptom}")

print("--- 重点患者筛查系统 ---")

for p in patients_data:
    if p["psa"] > 4 and p["age"] > 60:
        print(f"患者：{p['name']}|状态：⭐ 重点关注 (符合高龄且PSA异常)")
    else:
        print(f"患者:{p['name']}|状态：正常观察")

