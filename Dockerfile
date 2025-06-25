# Use Python 3.13 slim image based on Debian Bookworm as the base image
FROM python:3.13-slim-bookworm

# Copy the UV binary from an external container to the /bin directory
COPY --from=ghcr.io/astral-sh/uv:0.7.14 /uv /uvx /bin/

# Set the working directory inside the container
WORKDIR /app

# Copy the project configuration files
COPY pyproject.toml ./
COPY uv.lock ./

# Copy utils and src directories into the container
COPY utils/ ./utils/
COPY src/ ./src/

# Install dependencies using UV, leveraging cache for faster builds
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-install-project

# Copy the main server script into the container
COPY server.py .

# Synchronize dependencies again to ensure everything is up-to-date
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen

# Set the default command to run the server using UV
CMD ["uv", "run", "server.py"]