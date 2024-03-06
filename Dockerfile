FROM python:3.9

WORKDIR /MovieRecommendation

COPY requirements.txt /MovieRecommendation/

RUN pip install --no-cache-dir -r requirements.txt

RUN pip install notebook

COPY . /MovieRecommendation

# Jupyter Notebook
EXPOSE 8888

# Django
EXPOSE 8000

CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]
