from transformers import AutoTokenizer, AutoModelForCausalLM
import pandas as pd
from datasets import Dataset

# Step 1: Load Mistral Model
model_name = "mistral-model-name"  # Replace with the actual model name or path
print("Loading tokenizer and model...")
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Step 2: Load and Customize Dataset
def load_and_prepare_data(file_path):
    """
    Load and prepare a dataset from a file (e.g., Parquet, CSV).

    Args:
        file_path (str): Path to the dataset file.

    Returns:
        Dataset: Hugging Face Dataset ready for processing.
    """
    # Load the file into a Pandas DataFrame
    if file_path.endswith(".parquet"):
        df = pd.read_parquet(file_path)
    elif file_path.endswith(".csv"):
        df = pd.read_csv(file_path)
    else:
        raise ValueError("Unsupported file format. Please use a Parquet or CSV file.")

    # Convert to a Hugging Face Dataset
    dataset = Dataset.from_pandas(df)
    return dataset

# Step 3: Generate Responses from Mistral Model
def generate_response(prompt, max_length=100):
    """
    Generate a response from the Mistral model.

    Args:
        prompt (str): Input prompt for the model.
        max_length (int): Maximum length of the generated response.

    Returns:
        str: Generated response from the model.
    """
    input_ids = tokenizer.encode(prompt, return_tensors="pt")
    output_ids = model.generate(input_ids, max_length=max_length, num_return_sequences=1)
    response = tokenizer.decode(output_ids[0], skip_special_tokens=True)
    return response

# Example Usage
if __name__ == "__main__":
    # Load a custom dataset
    file_path = "path/to/your_dataset.parquet"  # Replace with your dataset path
    print("Loading dataset...")
    dataset = load_and_prepare_data(file_path)

    # Example prompt using the dataset (assuming a 'context' column exists)
    sample_context = dataset[0]['context'] if 'context' in dataset.column_names else "Example context."
    prompt = f"Based on the following context, answer the question: {sample_context}\nQuestion: What is this about?"

    # Generate a response
    print("Generating response...")
    response = generate_response(prompt)
    print("Response:", response)
