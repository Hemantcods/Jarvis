import google.generativeai as genai
def ai(input):
    genai.configure(api_key="Your_api_key_here")
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(f"as an voice assistant named Friday inspired from ironman's assistant you can get input in hindi and english use the same input tone ignore the symbols that may intrupt while reading and dont reply in hindi as my text to speech cannot read hindi you have to anser the following question:{input}")
    out=(response.text)
    return out

