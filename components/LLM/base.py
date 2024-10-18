import subprocess

class SimpleOllamaLLM:
    def __init__(self, model):
        self.model = model

    def run(self, prompt):
        # Construct the Docker command to execute
        command = f'sudo docker exec ollama ollama run {self.model} "{prompt}"'

        try:
            # Execute the command and capture the output
            result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            print(result)
            # Decode the output from bytes to string
            output = result.stdout.decode('utf-8').strip()
            return output
        except subprocess.CalledProcessError as e:
            # Handle errors in command execution
            print("Error occurred:", e.stderr.decode('utf-8').strip())
            return None

def generate_summary(input_text: str) -> str:
    """
    Generates a summary for the provided input text using the Ollama model.

    :param input_text: The text to be summarized.
    :return: The generated summary as a string.
    """
    model_name = "mistral-small"  # Example model name
    ollama_model = SimpleOllamaLLM(model=model_name)

    # Construct the prompt for summarization
    prompt = f"Summarize the following text:\n\n{input_text}\n\nSummary:"

    # Get the summary from the model
    summary = ollama_model.run(prompt)

    return summary

if __name__ == "__main__":
    input_text = (
        "Hello."
    )

    summary = generate_summary(input_text)
    print("Generated Summary:")
    print(summary)
