from transformers import pipeline

generator = pipeline(
    "text-generation",
    model="gpt2",
    pad_token_id=50256  # avoids warning
)

def clean_response(text):
    parts = text.split(":")
    return parts[-1].strip() if len(parts) > 1 else text.strip()

def generate_argument(role, topic):
    prompt = f"{role}: Provide a detailed argument about the topic '{topic}'."
    result = generator(prompt, max_new_tokens=100, do_sample=True, temperature=0.7)
    text = result[0]["generated_text"]
    return clean_response(text)

topic = input("Enter debate topic: ")

for role in ["Scientist", "Philosopher", "Psychologist"]:
    print(f"\n🧠 {role}'s argument:")
    print(generate_argument(role, topic))


