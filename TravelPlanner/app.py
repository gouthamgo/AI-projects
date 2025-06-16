import streamlit as st
import os
import base64
from openai import OpenAI
from dotenv import load_dotenv

# Step 1: Load environment variables
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    st.error("🔑 Missing OpenAI API key! Add it to the .env file.")
    st.stop()

# Step 2: Set up OpenAI client
client = OpenAI(api_key=api_key)

# Step 3: Set up Streamlit UI
st.set_page_config(page_title="Travel Planner", page_icon="🌍")
st.title("🤖 Robbie the Travel Planner")
st.write("Hi! Tell me where you want to go or upload a photo!")

# Step 4: User inputs
text_input = st.text_input("Describe your dream vacation")
uploaded_image = st.file_uploader("Or upload a photo", type=["jpg", "png"])

# Step 5: Weather function
def get_weather(city: str):
    return f"Weather in {city}: Sunny 🌞"  # Replace with real API call

# Step 6: Handle the request
if st.button("Plan My Trip! 🚀"):
    if not text_input and not uploaded_image:
        st.warning("Please type or upload a photo first!")
        st.stop()

    with st.spinner("Planning your trip..."):
        try:
            # Prepare messages with text+image
            messages = [{"role": "system", "content": "You're a travel expert. Suggest destinations with reasons and weather."}]
            content = []
            
            if text_input:
                content.append({"type": "text", "text": text_input})
            
            if uploaded_image:
                image_data = base64.b64encode(uploaded_image.read()).decode("utf-8")
                content.append({
                    "type": "image_url",
                    "image_url": f"data:image/jpeg;base64,{image_data}"
                })

            messages.append({"role": "user", "content": content})

            # Make API call
            response = client.chat.completions.create(
                model="gpt-4o",
                messages=messages,
                tools=[{
                    "type": "function",
                    "function": {
                        "name": "get_weather",
                        "description": "Get weather for a city",
                        "parameters": {
                            "type": "object",
                            "properties": {"city": {"type": "string"}}
                        }
                    }
                }],
                response_format={"type": "json_object"}
            )

            # Process response
            result = eval(response.choices[0].message.content)
            
            # Display results
            st.subheader("🌟 Your Travel Plan")
            for dest in result["destinations"]:
                st.markdown(f"### {dest['name']}")
                st.write(f"**Why:** {dest['reason']}")
                st.write(f"**Weather:** {dest['weather']}")

            if uploaded_image:
                st.image(uploaded_image, caption="Your photo", width=200)

        except Exception as e:
            st.error(f"Oops! Error: {e}")