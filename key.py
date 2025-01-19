import google.generativeai as genai

genai_api_key = "AIzaSyCY9L7bXQ0UlJI9xRfQU_zVW7L91NekxSQ"
genai.configure(api_key=genai_api_key)

def get_gemini_response(question):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(question)
    return response.text

question = "Who is the CEO of Tesla?"
print(get_gemini_response(question))