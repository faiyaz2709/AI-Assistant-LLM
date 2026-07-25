import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

print("Code is running!")

my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("API Error: GROQ_API_KEY not found")

client = Groq(api_key=my_api_key)

model = "llama-3.3-70b-versatile"

print("\n========== AI Assistant ==========")
print("1. Normal Chat")
print("2. Role-Based Chat")

choice = input("\nChoose an option (1/2): ")

# -----------------------------
# NORMAL CHAT
# -----------------------------
if choice == "1":

    prompt = input("\nEnter your question: ")

    messages = [
        {
            "role": "user",
            "content": prompt
        }
    ]

# -----------------------------
# ROLE-BASED CHAT
# -----------------------------
elif choice == "2":

    system_role = input("\nEnter the role (Teacher, Doctor, Software Engineer, etc.): ")

    prompt = input("Enter your question: ")

    messages = [
        {
            "role": "system",
            "content": system_role
        },
        {
            "role": "user",
            "content": prompt
        }
    ]

else:
    print("Invalid Choice!")
    exit()

# -----------------------------
# SEND REQUEST
# -----------------------------
response = client.chat.completions.create(
    model=model,
    messages=messages,
    temperature=1
)

answer = response.choices[0].message.content

print("\n" + "=" * 70)
print("AI Response:\n")
print(answer)
print("=" * 70)