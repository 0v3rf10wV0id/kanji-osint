import subprocess

def run_container(command):
  print("Entered run container!")
  print(f"Command: {command}")
  try:
      # Run subfinder with capture for stdout and stderr
      process = subprocess.run(command.split(), capture_output=True, check=True)
      output = process.stdout.decode()
      output = output.split("\n")
      # print(type(output))
      # print(output)
      # print(len(output))
      return output

  except subprocess.CalledProcessError as e:
      print("Subfinder execution failed:", e)
