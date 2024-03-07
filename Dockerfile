# Stage 1: Prepare the environment and install dependencies
FROM ubuntu:20.04 AS prepare

# Avoid stuck build due to user prompt
ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install --no-install-recommends -y python3.9 python3.9-dev python3.9-venv python3-pip python3-wheel build-essential texlive-full texlive-lang-czechslovak texlive-fonts-recommended && \
	apt-get clean && rm -rf /var/lib/apt/lists/*

# Stage 2: Copy necessary files and run the script
FROM prepare AS run

# Invalidate cache to force run the following code
#ADD "https://www.random.org/cgi-bin/randbyte?nbytes=10&format=h" skipcache

# Copy the necessarry files - the script, resources and orgonit
#COPY script.py /

# Run the sript to generate the text outputs
#ENTRYPOINT ["python", "./script.py"]
ENTRYPOINT ["entrypoint.sh"]
#ENTRYPOINT ["sh", "-c", "echo \"Hello from Docker\""]


# Copy the generated files out of the container
# this is done in build
#COPY /sell_text.txt .
#COPY /galter_print.pdf .