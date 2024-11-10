import subprocess
import os

def launch_streamlit_app(script_name="TinyAGI.py"):
    # Check if the script file exists
    if not os.path.isfile(script_name):
        print(f"Error: {script_name} not found.")
        return

    # Run the Streamlit app
    try:
        subprocess.run(["streamlit", "run", script_name], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Failed to launch Streamlit app: {e}")

if __name__ == "__main__":
    launch_streamlit_app()
