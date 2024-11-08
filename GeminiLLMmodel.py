import google.generativeai as genai

genai.configure(api_key= 'AIzaSyCBJ-3Vrj9IIDdJz5xlg59_Ye5DnTIlk0A')

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "application/json",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
#   safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
)







    







    


