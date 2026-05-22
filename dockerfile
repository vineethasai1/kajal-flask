FROM python:3.11
WORKDIR /vineetha
COPY requirements.txt .

# "Install all Python packages listed in requirements.txt without saving cache to keep image small"
RUN pip install --no-cache-dir -r requirements.txt

#COPY = copy files from YOUR PC into the container
COPY . .

EXPOSE 5000

#Same as typing in terminal:  python app.py
CMD ["python","app.py"]





