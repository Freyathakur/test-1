FROM debian:bookworm-slim

RUN apt-get update && apt-get install -y \
    libssl-devel \
    git \
 && rm -rf /var/lib/apt/lists/*

CMD ["echo", "hello"]
