from scrapy.core.downloader.handlers.http11 import tunnel_request_data
# --- 变量定义：像填写病历页一样 ---
patient_name ="张三"
patient_age = 68
patient_bmi = 24.5
has_prostate_cancer = True
# --- 逻辑输出：像向带教老师汇报一样 ---
print("--- 泌尿外科患者初步评估 ---")
print(f"患者姓名: {patient_name}")
print(f"患者年龄: {patient_age}岁")
print(f"BMI指数: {patient_bmi}")
# 简单的判断（下一章会深入，今天先体验）
if has_prostate_cancer:
    print("诊断状态：确诊前列腺癌，需进一步评估Gleason评分。")
else:
    print("诊断状态：未见明显恶性肿瘤体征。")
# 检查你的显卡是否被 Python 识别（这决定了你未来的微调能力）
print("\n--- 硬件体检 ---")
print(f"你的显卡型号是：RTX 4070 Super")