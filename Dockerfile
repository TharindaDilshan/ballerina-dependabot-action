FROM python:latest

# Add files to the image
ADD entrypoint.py /entrypoint.py

# Install dependencies and make script executable
RUN chmod +x entrypoint.py

RUN echo "DOCKER FILE"

# Run script with the ENV var
ENTRYPOINT export /entrypoint.py