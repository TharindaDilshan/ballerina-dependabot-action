FROM python:latest

# Add files to the image
ADD lib/ballerina_dependabot/entrypoint.py entrypoint.py

# Install dependencies and make script executable
RUN pip install requests
RUN pip install retry
RUN pip install semver
RUN chmod +x entrypoint.py

RUN echo "DOCKER FILE"

# Run script with the ENV var
ENTRYPOINT /entrypoint.py
