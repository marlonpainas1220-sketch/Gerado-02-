import requests
import os

class InstagramClient:
    def __init__(self):
        self.access_token = os.getenv("INSTAGRAM_ACCESS_TOKEN")
        self.account_id = os.getenv("INSTAGRAM_ACCOUNT_ID")
        self.base_url = "https://graph.facebook.com/v18.0"

    def post_photo(self, image_url, caption):
        if not self.access_token:
            print("⚠️ MODO SIMULAÇÃO: Token não configurado.")
            return {"id": "mock_id_123"}

        # 1. Criar container de mídia
        url = f"{self.base_url}/{self.account_id}/media"
        payload = {
            "image_url": image_url,
            "caption": caption,
            "access_token": self.access_token
        }
        res = requests.post(url, data=payload).json()
        
        if 'id' in res:
            # 2. Publicar container
            creation_id = res['id']
            publish_url = f"{self.base_url}/{self.account_id}/media_publish"
            pub_payload = {"creation_id": creation_id, "access_token": self.access_token}
            return requests.post(publish_url, data=pub_payload).json()
        return res