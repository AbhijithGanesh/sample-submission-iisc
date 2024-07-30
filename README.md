# Evaluation Docker Compose Setup

This repository contains a Docker Compose setup for running an evaluation using a Docker container with GPU support.

## Prerequisites

- Docker
- Docker Compose
- NVIDIA Docker Runtime

## Getting Started

### Clone the Repository

```sh
git clone <repository-url>
cd <repository-directory>
```

### Directory Structure

Ensure the following directory structure is in place:

```sh
/home/videoserver/
├── Phase 1 IEEE BMC 2024/
│   └── Phase 1 Assessment/
│       └── workdir/
│           └── Stn_HD_1.mp4
└── submissions/
```

### Running the Container

To run the container, use the following command:

```sh
docker-compose up
```

This will pull the latest image, create the necessary volumes, and run the evaluation script.

### Command Explanation

The command executed inside the container is:

```sh
python app.py --input=sample.mp4 --output=submission.csv
```

- `--input=sample.mp4`: Specifies the input video file.
- `--output=submission.csv`: Specifies the output CSV file.

### Volumes

The following volumes are mounted:

- `/home/videoserver/Phase 1 IEEE BMC 2024/Phase 1 Assessment/workdir/Stn_HD_1.mp4:/home/users`: Mounts the input video file.
- `/home/videoserver/submissions:/home/users/submissions`: Mounts the submissions directory.

### Resources

The container is configured to use NVIDIA GPUs with the following resource limits:

- Memory: 64GB
- GPU: All available GPUs

## Notes

- Ensure that the NVIDIA Docker runtime is installed and configured on your system.
- Modify the paths in the [`docker-compose.yaml`](docker-compose.yaml) file as per your directory structure if needed.
