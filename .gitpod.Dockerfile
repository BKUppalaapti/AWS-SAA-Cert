FROM gitpod/workspace-full

USER root

RUN apt-get update && \
    apt-get install -y unzip curl && \
    rm -rf /var/lib/apt/lists/*

USER gitpod