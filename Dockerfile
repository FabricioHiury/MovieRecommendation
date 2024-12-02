FROM python:3.12

RUN apt-get update && apt-get install -y curl

RUN curl --proto '=https' --tlsv1.2 https://sh.rustup.rs -sSf | sh -s -- -y

ENV PATH="/root/.cargo/bin:${PATH}"

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
