FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY Pipfile.lock /code/
COPY Pipfile /code/
RUN pip install pipenv
RUN pipenv install --system --deploy --ignore-pipfile
COPY . /code/
