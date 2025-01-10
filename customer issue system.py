import os
import subprocess
import psutil
import time
import json

# Function to run a bash command and return the output
def run_bash_command(command):
    """Executes a bash command and returns the output."""
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout.strip()

# Function to gather system metrics
def gather_system_metrics():
    """Collects CPU, memory, and disk usage metrics."""
    metrics = {
        "cpu_usage": psutil.cpu_percent(interval=1),
        "memory_usage": psutil.virtual_memory()._asdict(),
        "disk_usage": psutil.disk_usage('/')._asdict(),
    }
    return metrics

# Function to run a Docker container
def run_docker_container(image_name):
    """Starts a Docker container with the specified image."""
    print(f"Starting Docker container with image: {image_name}")
    run_bash_command(f"docker run --rm -d --name test_container {image_name}")
    time.sleep(5)  # Wait for the container to initialize

# Function to stop the Docker container
def stop_docker_container():
    """Stops the running Docker container."""
    print("Stopping Docker container...")
    run_bash_command("docker stop test_container")

# Main function to simulate the customer issue reproduction
def main():
    """Main function to orchestrate the issue reproduction."""
    docker_image = "nginx:latest"  # Example Docker image

    # Gather initial system metrics
    initial_metrics = gather_system_metrics()
    print("Initial System Metrics:", json.dumps(initial_metrics, indent=4))

    # Run the Docker container
    run_docker_container(docker_image)

    # Gather metrics after running the container
    post_metrics = gather_system_metrics()
    print("Post-Container System Metrics:", json.dumps(post_metrics, indent=4))

    # Stop the Docker container
    stop_docker_container()

    # Final metrics after stopping the container
    final_metrics = gather_system_metrics()
    print("Final System Metrics:", json.dumps(final_metrics, indent=4))

if __name__ == "__main__":
    main()