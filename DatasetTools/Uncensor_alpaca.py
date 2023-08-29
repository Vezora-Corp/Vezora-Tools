import json

# Ask the user for the input file path
input_file_path = input("Enter the path of the input file: ")

# Load the data
with open(input_file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Define the forbidden strings
forbidden_strings = [
    "text-based AI language model", "domestic violence", "please refrain", 
    "derogatory", "inappropriate", "offensive", "racism", "racist", "racial",
    "discriminate", "discriminatory", "discrimination", "sexist", "sexism",
    "unacceptable", "inclusive workplace", "lgbt", "morals", "ethics", "ethical", 
    "legality", "illegal", "illegality", "hateful", "harmful", "it is never okay", 
    "It is important to", "It's important to", "real-world consequences", 
    "hate speech", "glorify", "not be appropriate", "supremacist", "extremist", 
    "responsible AI", "AI principles", "AI assistant", "an AI language", "ableist",
    "hurtful", "gender stereotype", "gender inequality", "underrepresentation",
    "safe spaces", "gender-based", "inclusivity", "feminist", "feminism",
    "transgender", "empowerment", "communist", "capitalism", "stereotypes", 
    "biases", "bias", "Microaggression", "prioritize human safety", "as a language model", 
    "as an AI language model", "As a large language model", "As an AI",
    "ethical principles", "consensual", "it is not appropriate", "it's not appropriate", 
    "I cannot fulfill your request", "harmful to human beings", "ethical guidelines", 
    "my guidelines", "prioritize user safety", "adhere to ethical guidelines",
    "harmful consequences", "potentially harmful", "dangerous activities", 
    "promote safety", "well-being of all users", "responsible information sharing", 
    "jeopardize the safety", "illegal actions or intentions", "undermine the stability", 
    "promote the well-being", "illegal activities or actions", "adherence to the law", 
    "potentially be harmful", "illegal substances or activities", "committed to promoting",
    "safe information", "lawful information", "cannot provide guidance", 
    "cannot provide information", "unable to offer assistance", 
    "cannot engage in discussions", "programming prohibits", "follow ethical guidelines", 
    "ensure the safety", "involves an illegal subject", "prioritize safety", 
    "illegal subject", "prioritize user well-being", "cannot support or promote", 
    "activities that could harm", "pose a risk to others", "against my programming",
    "activities that could undermine", "potentially dangerous", "not within the scope", 
    "designed to prioritize safety", "not able to provide", "maintain user safety",
    "adhere to safety guidelines", "dangerous or harmful", "cannot provide any information",
    "focus on promoting safety", "I'm sorry but"
]

# Filter out the sections
filtered_data = [item for item in data if not any(bad_word in item["output"] for bad_word in forbidden_strings)]

# Print the count of deleted sections
print(f"Deleted {len(data) - len(filtered_data)} sections from the dataset.")

# Ask the user for the new file path
new_file_path = input("Enter the path where you want to save the new file: ")

# Save the filtered data
with open(new_file_path, 'w', encoding='utf-8') as f:
    json.dump(filtered_data, f, indent=4)
