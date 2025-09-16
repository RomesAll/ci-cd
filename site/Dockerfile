FROM python:3.12-slim
RUN pip install --upgrade pip
WORKDIR /site
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8000
CMD [ "python", "main.py" ]