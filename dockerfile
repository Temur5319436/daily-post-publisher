FROM python:3.9

RUN apt-get update -y && apt-get upgrade -y

RUN useradd -m app

USER app

WORKDIR /home/app/daily-post-publisher

COPY --chown=app:app requirements.txt .

ENV PATH="/home/app/.local/bin:${PATH}"

RUN pip install -r requirements.txt

COPY --chown=app:app . .

CMD [ "python", "main.py" ]