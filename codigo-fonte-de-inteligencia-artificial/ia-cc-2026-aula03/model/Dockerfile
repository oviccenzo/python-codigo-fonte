FROM tensorflow/tensorflow:2.16.1

WORKDIR /app

COPY ../Documents/viccenzo.iftm/inteligencia-artificial/ia-cc-2026-aula03/model/requirements.txt .
RUN python -m pip3 install --no-cache-dir -r requirements.txt

COPY ../Documents/viccenzo.iftm/inteligencia-artificial/ia-cc-2026-aula03/model .

EXPOSE 5000

CMD ["python", "app.py"]