import requests


API_TOKEN = "208620f1-dfe5-4265-9b54-af65d935dee9"


async def api_requests(image_url):
    r = requests.post(
        "https://api.deepai.org/api/toonify",
        data={
            'image': image_url
        },
        headers={'api-key': API_TOKEN}
    )
    data = r.json()

    if data:
        return data["output_url"]

    return None


