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

# Run smoke tests
RUN chmod +x ./smoke.sh

# Run smoke.sh when the container launches
CMD ["bash", "smoke.sh"]