FROM python:latest

# Add files to the image
ADD lib/ballerina_dependabot/entrypoint.py entrypoint.py
ADD lib/ballerina_dependabot/commons.py commons.py
ADD lib/ballerina_dependabot/file_fetcher.py file_fetcher.py
ADD lib/ballerina_dependabot/file_parser.py file_parser.py
ADD lib/ballerina_dependabot/file_updater.py file_updater.py
ADD lib/ballerina_dependabot/update_checker.py update_checker.py

# Install dependencies and make script executable
RUN pip install requests
RUN pip install retry
RUN pip install semver
RUN pip install PyGithub
RUN chmod +x entrypoint.py

RUN echo "DOCKER FILE"

# Run script with the ENV var
ENTRYPOINT /entrypoint.py
