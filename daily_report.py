import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import requests
import datetime

# ========== 邮箱配置 ==========
import os

SENDER_EMAIL = os.getenv("EMAIL_USER")
SENDER_PASSWORD = os.getenv("EMAIL_PASS")
RECEIVER_EMAIL = os.getenv("EMAIL_RECEIVER")


# ========== 获取数据函数（示例API，可换成更稳定的数据源） ==========
def get_data():
    # 这里只写示例，你可以替换成更权威的数据接口
    data = {
        "美元指数": 104.3,
        "人民币汇率": 7.18,
        "M1": "3.2%",
        "M2": "8.5%",
        "制造业PMI": 50.5,
        "服务业PMI": 52.1,
        "上证综指": 3150,
        "恒生指数": 18500,
        "标普500": 5200,
        "WTI原油": 78.5,
        "黄金": 1940,
        "中国10年期国债": "2.55%",
        "美国10年期国债": "4.25%"
    }
    return data

# ========== 生成日报 ==========
def generate_report(data):
    today = datetime.date.today().strftime("%Y/%m/%d")
    report = f"""📊 每日金融数据简报（{today}）

1. 外汇 & 美元指数
- 美元指数 DXY：{data['美元指数']}
  🔎 美元走强，可能带来人民币贬值压力
- 人民币汇率 USD/CNY：{data['人民币汇率']}
  🔎 人民币小幅波动，受美元走势和资金流动影响

2. 货币供应（最新月度）
- M1 同比：{data['M1']}
  🔎 企业短期资金活跃度一般
- M2 同比：{data['M2']}
  🔎 流动性宽松，政策偏稳健

3. 宏观景气
- 制造业 PMI：{data['制造业PMI']}
  🔎 高于荣枯线，制造业保持扩张
- 服务业 PMI：{data['服务业PMI']}
  🔎 消费和服务业回暖

4. 股指表现
- 上证综指：{data['上证综指']}
  🔎 政策推动下市场情绪改善
- 恒生指数：{data['恒生指数']}
  🔎 港股反弹，科技股带动
- 标普500：{data['标普500']}
  🔎 美股高位震荡，受利率预期影响

5. 大宗商品
- WTI 原油：{data['WTI原油']} 美元/桶
  🔎 地缘风险推升油价
- 黄金：{data['黄金']} 美元/盎司
  🔎 避险需求上升

6. 债券收益率
- 中国10年期国债：{data['中国10年期国债']}
  🔎 资金流入债市，避险情绪增强
- 美国10年期国债：{data['美国10年期国债']}
  🔎 利率预期分歧，美债波动
"""
    return report

# ========== 发送邮件 ==========
def send_email(report):
    msg = MIMEMultipart()
    msg['From'] = SENDER_EMAIL
    msg['To'] = RECEIVER_EMAIL
    msg['Subject'] = "每日金融数据简报"

    msg.attach(MIMEText(report, 'plain', 'utf-8'))

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, msg.as_string())
        print("✅ 邮件已发送")

# ========== 主程序 ==========
if __name__ == "__main__":
    data = get_data()
    report = generate_report(data)
    send_email(report)

