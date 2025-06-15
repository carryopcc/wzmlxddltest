import os
import requests

def pixeldrain_uploader(file_path):
    """
    Uploads the given file to Pixeldrain and returns download info.
    """
    api_url = "https://pixeldrain.com/api/file"

    with open(file_path, 'rb') as f:
        response = requests.post(
            api_url,
            files={"file": (os.path.basename(file_path), f)}
        )

    if response.status_code != 200:
        raise Exception(f"Pixeldrain upload failed: {response.status_code} - {response.text}")

    result = response.json()
    if not result.get("success"):
        raise Exception(f"Pixeldrain error: {result.get('message')}")

    file_id = result.get("id")
    return {
        'filename': os.path.basename(file_path),
        'download_link': f"https://pixeldrain.com/u/{file_id}",
        'filesize': os.path.getsize(file_path),
    }

