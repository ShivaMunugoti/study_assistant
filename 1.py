from google import genai

from google.genai import types

client = genai.Client(api_key="AIzaSyAUmBONLiO1OoixwFeXN4NuNGCmXpl241s")

def student_assistant(question):
    system_prompt = "You are a helpful assistant for students. Answer the following question: {question}"
    response = client.models.generate_content(
        model = "gemini-2.5-flash",
        config = types.GenerateContentConfig(
            system_instruction= system_prompt
           
        ),
        contents= question
    )
    return response.text

result = student_assistant("What is the capital of France?")
print(result)
