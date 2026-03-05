import json

def analyze_aip_log(log_data):
    # 模拟从 AIP 日志提取 HJS 判定的极简逻辑
    decision = log_data.get("decision")
    print(f"[AIP Context] Decision: {decision}")
    
    if decision == "ALLOW":
        print("[HJS Judgment] Derived: AUTHORIZED_EXECUTION")
    else:
        print("[HJS Judgment] Derived: POLICY_BLOCKED")

