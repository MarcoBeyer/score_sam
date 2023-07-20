FROM public.ecr.aws/lambda/python:3.10

COPY app.py requirements.txt ./
COPY bondora-model ./score/

RUN python -m pip install -r requirements.txt -t .

# Command can be overwritten by providing a different command in the template directly.
CMD ["app.lambda_handler"]
