# Use a long-term maintained Linux version as the base image
FROM --platform=linux/amd64 ubuntu:20.04

# Set noninteractive mode to prevent tzdata configuration prompt
ENV DEBIAN_FRONTEND=noninteractive

# Set the working directory
WORKDIR /home/app

# Install Python and other dependencies
RUN apt-get update && \
    apt-get install -y python3 \ 
    python3-pip \
    git \
    perl \
    texlive-xetex \
    texlive-fonts-extra \
    latexmk

# Install Pulp, Pandas, xlrd library
RUN pip3 install pulp \
    pandas \
    xlrd \
    matplotlib

# Docker build pulls in at least one data set for the experiments 
RUN git clone https://resources.oreilly.com/examples/9780596153946.git

# Copy your files to the Docker image
COPY . /home/app

# Run the script when the container launches
# CMD ["python3", "scripts/main.py"]

# CMD ["make", "main.pdf"]

# CMD ["make", "clean"]

# CMD ["cd", "report"]
# CMD ["ls", "-l"]
# Specify the entry point to copy the PDF to /output
# CMD ["cp", "report/main.pdf", "/Users/maojcn/Workspace/ReproEng/project_duckies/main.pdf"]