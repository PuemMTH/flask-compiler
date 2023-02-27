# ใช้ Python 3.9 จาก official image ของ Python
FROM node:18-alpine
# ใช้ Node.js 18 จาก official image ของ Node.js
FROM python:3.9-alpine

# กำหนด working directory ให้เป็น /app
WORKDIR /app

# คัดลอกไฟล์ requirements.txt ไปยัง image และติดตั้ง package ที่ระบุในไฟล์
COPY requirements.txt .
RUN pip install -r requirements.txt

# คัดลอกไฟล์ app.py ไปยัง image
COPY app2.py .

# กำหนดค่า ENV สำหรับ Flask app
ENV FLASK_APP=app2.py
ENV FLASK_ENV=development

# เปิดพอร์ต 5000 สำหรับ Flask app
EXPOSE 5000

# เริ่มต้นการรัน Flask app ด้วยคำสั่ง flask run
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]