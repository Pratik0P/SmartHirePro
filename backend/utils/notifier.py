import smtplib
from email.message import EmailMessage

def send_hr_email(candidate_name: str, score: float):
    msg = EmailMessage()
    msg["Subject"] = f"📌 Top Candidate Match: {candidate_name}"
    msg["From"] = "your_email@gmail.com"
    msg["To"] = "hr_email@example.com"
    
    msg.set_content(
        f"""
Hi HR Team,

🎯 A strong match has been found for your job posting!

📄 Candidate: {candidate_name}
✅ Match Score: {score:.2f}

Please check the resume folder for review.
        """
    )

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login("your_email@gmail.com", "your_app_password")
            smtp.send_message(msg)
        print("✅ Email sent to HR")
    except Exception as e:
        print(f"❌ Failed to send email: {e}")
