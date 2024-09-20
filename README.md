
# Docker Instructions

This project contains a simple Flask application using GraphQL. The following guide will help you build the Docker image and run the container.

## Prerequisites

- Ensure Docker is installed and running on your machine. You can download Docker from [here](https://www.docker.com/products/docker-desktop).

## Docker Commands

### 1. Build the Docker Image

To build the Docker image, use the `docker build` command. This command looks for a `Dockerfile` in the current directory and builds an image from it.

```bash
docker build -t <image_name> .
```

- `-t <image_name>`: Specifies a tag name for the image.
- `.`: Refers to the current directory where the Dockerfile is located.

#### Example:
```bash
docker build -t graphql-app .
```

### 2. Run the Docker Container

Once the image is built, you can run the container using the `docker run` command.

```bash
docker run -d -p <host_port>:<container_port> --name <container_name> <image_name>
```

- `-d`: Runs the container in detached mode (in the background).
- `-p <host_port>:<container_port>`: Maps a port on your local machine to a port inside the container.
- `--name <container_name>`: Optionally name your container.
- `<image_name>`: The name of the image you built.

#### Example:
```bash
docker run -d -p 5000:5000 --name graphql-container graphql-app
```

In this example:
- Port `5000` on the host machine is mapped to port `5000` in the container.
- The container is named `graphql-container` and runs the `graphql-app` image.

### 3. List Running Containers

To see a list of currently running containers, use:

```bash
docker ps
```

### 4. List All Containers (Running and Stopped)

To view all containers, including those that are stopped:

```bash
docker ps -a
```

### 5. Stop a Running Container

To stop a specific running container:

```bash
docker stop <container_name_or_id>
```

#### Example:
```bash
docker stop graphql-container
```

### 6. Remove a Stopped Container

To remove a container after it is stopped:

```bash
docker rm <container_name_or_id>
```

#### Example:
```bash
docker rm graphql-container
```

### 7. Rename a Container

To rename an existing container:

```bash
docker rename <old_name> <new_name>
```

#### Example:
```bash
docker rename graphql-container graphql-new-container
```

### 8. Start an Existing Container

To start a stopped container:

```bash
docker start <container_name_or_id>
```

#### Example:
```bash
docker start graphql-container
```

### 9. Remove an Image

To remove an image from your system:

```bash
docker rmi <image_name_or_id>
```

#### Example:
```bash
docker rmi graphql-app
```

## Additional Information

- Ensure that your `Dockerfile` is correctly placed in the root of your project directory.
- You can access the Flask application in your browser by navigating to `http://localhost:5000/graphql`.
