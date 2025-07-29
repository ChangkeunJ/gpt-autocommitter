"""Self-improving script using OpenAI's GPT API.

The script can update a target Python file using GPT and allows
specifying the OpenAI model to use via the command line.
"""
from datetime import datetime
import argparse
import openai
import os

openai_api_key = os.getenv("OPENAI_API_KEY")
if not openai_api_key:
    raise RuntimeError("OPENAI_API_KEY environment variable is not set")
openai.api_key = openai_api_key

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument(
    "-f",
    "--file",
    default="main.py",
    help="Target Python file to improve",
)
parser.add_argument(
    "-m",
    "--model",
    default="gpt-4",
    help="OpenAI model to use",
)
args = parser.parse_args()
target_file = args.file
model = args.model

try:
    with open(target_file, "r") as f:
        current_code = f.read()
except FileNotFoundError:
    raise SystemExit(f"The source file '{target_file}' was not found.")

prompt = f"""
You are a helpful AI programmer.

Your task is to read and analyze the following Python code.
Then, make a **small but meaningful improvement** to the code.
Do not break the existing functionality.

Types of improvements you can make (choose one per run):
- Add a minor feature (e.g., logging, CLI argument, or extra message)
- Refactor a function or clean the code
- Add error handling or input validation
- Optimize logic or improve readability
- Add helpful comments or docstrings

Return only the full updated code, not explanations.

{current_code}
"""

response = openai.ChatCompletion.create(
    model=model,
    messages=[{"role": "user", "content": prompt}]
)

updated_code = response['choices'][0]['message']['content']

print(f"Improving {target_file} at {datetime.now().isoformat()}")
with open(target_file, "w") as f:
    f.write(updated_code)
