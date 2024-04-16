import os
import subprocess

def run_container(command):
    print("entered run container!")
    print(command)
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Check if the subprocess executed successfully
    if result.returncode == 0:
        stdout_str = result.stdout
        stdout_lines = stdout_str.splitlines()
        print("Subprocess stdout:")
        for line in stdout_lines:
            print(line)
        print(f"Length : {len(stdout_lines)}")
        return stdout_str
    else:
        stderr_str = result.stderr
        print(f"Subprocess failed with error: {stderr_str}")
        return None

# def run_container(mounts,command):
#     """Runs the 'test' image with the provided domain argument."""

#     client = docker.from_env()
#     try:
#         # Create a container configuration without 'hostconfig'
#         mounts_arr = []
#         for mnt in mounts:
#             mounts_arr.append(docker.types.Mount(type='bind',source=str(os.getcwd())+mnt['root'],target=mnt['target']))
#         container_config = {
#             'image': 'test',
#             'command': command,
#             'mounts' : mounts_arr
#         }

#         # Create and run the container
#         container = client.containers.create(**container_config)
#         container.start()
#         container.wait()
#         enum_output = container.logs()

#         # Optionally handle logs or other container interactions here

#     except Exception as e:
#         print(f"Error running container: {e}")

#     finally:
#         # Stop and remove the container (adjust as needed)
#         if container:  # Check if container exists before stopping and removing
#             container.stop()
#             container.remove()
#             return enum_output
