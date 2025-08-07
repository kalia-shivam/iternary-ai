import functions_framework
from dotenv import load_dotenv
import os
from openai import OpenAI

# Load env vars locally (ignored on Google Cloud)
load_dotenv()

@functions_framework.http
def get_travel_details(request):
    request_json = request.get_json(silent=True)
    city = request_json['city']

    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
    
    # Step 1: Generate the itinerary
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a helpful assistant that creates detailed one day itineraries "
                    "based on the city that the user chooses. Create only 3 activities "
                    "(morning, afternoon, evening). Only mention the itinerary, nothing else."
                )
            },
            {
                "role": "user",
                "content": city
            }
        ],
        temperature=0.64,
        max_tokens=1024,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    itinerary = response.choices[0].message.content

    # Step 2: Generate DALL·E prompts
    dalle_response = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a helpful assistant that creates DALL-E prompts based on itineraries. "
                    "The prompts should be short. Create one prompt for Morning, one for Afternoon, "
                    "and one for Evening. The DALL-E prompt should be separated by '|'"
                )
            },
            {
                "role": "user",
                "content": itinerary
            }
        ],
        temperature=0.64,
        max_tokens=1024,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    dalle_prompts_string = dalle_response.choices[0].message.content
    dalle_prompts_list = dalle_prompts_string.split('|')

    # Step 3: Generate DALL·E 3 images
    image_urls = []
    for prompt in dalle_prompts_list:
        image_response = client.images.generate(
            model="dall-e-3",
            prompt=prompt,
            size="1024x1024",
            quality="standard",
            n=1
        )
        image_urls.append(image_response.data[0].url)

    # Step 4: Return the final result
    result = {
        'itinerary': itinerary,
        'morning_image': image_urls[0],
        'afternoon_image': image_urls[1],
        'evening_image': image_urls[2]
    }

    return result
