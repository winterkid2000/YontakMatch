import random
import smtplib
from email.mime.text import MIMEText

def generate_otp():
    return str(random.randint(100000, 999999))

def send_otp_email(to_email: str, otp: str):
    from_email = "your_email@gmail.com"
    password = "your_app_password"  # 앱 비밀번호

    subject = "YontakMatch 인증코드"
    content = f"안녕하세요!\n\nYontakMatch 인증코드는 다음과 같습니다:\n\n[ {otp} ]\n\n좋은 하루 되세요!"

    msg = MIMEText(content)
    msg["Subject"] = subject
    msg["From"] = from_email
    msg["To"] = to_email

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(from_email, password)
            server.send_message(msg)
    except Exception as e:
        print("이메일 전송 실패:", e)
