import google.generativeai as genai
import PIL.Image
import os

genai.configure(api_key="xxxxxxxxx")
# img = PIL.Image.open("path/to/image.png")

model = genai.GenerativeModel(model_name="gemini-1.5-flash")
response = model.generate_content(
    "As an informative chatbot for the Guru Gobind Singh Indraprastha University (GGSIPU) ACM Chapter, located at Sec 16 Dwarka. GGSIPU is ranked 115th overall in NIRF rankings, with Management at 66th, Engineering at 84th, University at 74th, and Law at 19th. Answer your questions about ACM, its activities, and benefits of joining our chapter. Provide information about upcoming events, workshops, and competitions organized by ACM GGSIPU. Share resources like tutorials, interview preparation tips, and career guidance related to computer science. Direct you to relevant ACM resources or connect you with ACM chapter representatives and for information you can extract information from https://usict.acm.org/ this website . Now generate 150  querries and their long answer and  remove ** this sign from start and end of word and make a spreadsheet that students should ask and their response as well  "
)

reponse2 = model.generate_content("now geenrate 50 more")
print(response.text)
