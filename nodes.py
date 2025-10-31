from transformers import pipeline

# Load a free Hugging Face model (GPT-2)
generator = pipeline("text-generation", model="gpt2")

def clean_response(text):
    """Removes repeated prompts or unnecessary prefixes from output."""
    parts = text.split(":")
    return parts[-1].strip() if len(parts) > 1 else text.strip()

def scientist(state):
    topic = state["topic"]
    prompt = f"Scientist: Provide a scientific and logical argument about the topic '{topic}'."
    response = generator(prompt, max_new_tokens=120, do_sample=True, temperature=0.8)
    text = clean_response(response[0]["generated_text"])
    state["scientist_response"] = text
    return state

def philosopher(state):
    topic = state["topic"]
    prompt = f"Philosopher: Provide a philosophical and ethical argument about the topic '{topic}'."
    response = generator(prompt, max_new_tokens=120, do_sample=True, temperature=0.8)
    text = clean_response(response[0]["generated_text"])
    state["philosopher_response"] = text
    return state
