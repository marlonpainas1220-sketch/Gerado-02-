import os
import requests
from typing import Optional, Dict, Any


class WhatsAppClient:
    """Cliente para envio de conteúdo via WhatsApp Business API"""
    
    def __init__(self, phone_number_id: Optional[str] = None, access_token: Optional[str] = None):
        self.phone_number_id = phone_number_id or os.getenv("WHATSAPP_PHONE_NUMBER_ID")
        self.access_token = access_token or os.getenv("WHATSAPP_ACCESS_TOKEN")
        self.base_url = f"https://graph.facebook.com/v18.0/{self.phone_number_id}/messages"
        
    def send_text_message(self, to: str, message: str) -> Dict[str, Any]:
        """
        Envia mensagem de texto via WhatsApp
        
        Args:
            to: Número do destinatário (formato: 5511999999999)
            message: Texto da mensagem
            
        Returns:
            Resposta da API
        """
        
        if not self.access_token or not self.phone_number_id:
            print("⚠️ MODO SIMULAÇÃO: Credenciais WhatsApp não configuradas.")
            print(f"📱 Mensagem para {to}:")
            print(f"{message}")
            return {"status": "simulated", "to": to}
        
        headers = {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/json"
        }
        
        payload = {
            "messaging_product": "whatsapp",
            "to": to,
            "type": "text",
            "text": {
                "body": message
            }
        }
        
        try:
            response = requests.post(self.base_url, json=payload, headers=headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"❌ Erro ao enviar mensagem WhatsApp: {e}")
            return {"error": str(e)}
    
    def send_content_delivery(
        self,
        to: str,
        content: str,
        profile_name: str = "Sistema"
    ) -> Dict[str, Any]:
        """
        Envia conteúdo formatado via WhatsApp
        
        Args:
            to: Número do destinatário
            content: Conteúdo formatado para envio
            profile_name: Nome do perfil que gerou o conteúdo
            
        Returns:
            Resposta da API
        """
        
        header = f"🎬 *CONTEÚDO GERADO - {profile_name.upper()}*\n"
        header += "━━━━━━━━━━━━━━━━━━━━━━\n\n"
        
        footer = "\n━━━━━━━━━━━━━━━━━━━━━━\n"
        footer += "✅ Conteúdo pronto para publicação\n"
        footer += "🤖 Gerado automaticamente pelo sistema"
        
        full_message = header + content + footer
        
        return self.send_text_message(to, full_message)
    
    def send_image_with_caption(
        self,
        to: str,
        image_url: str,
        caption: str
    ) -> Dict[str, Any]:
        """
        Envia imagem com legenda via WhatsApp
        
        Args:
            to: Número do destinatário
            image_url: URL da imagem
            caption: Legenda da imagem
            
        Returns:
            Resposta da API
        """
        
        if not self.access_token or not self.phone_number_id:
            print("⚠️ MODO SIMULAÇÃO: Credenciais WhatsApp não configuradas.")
            print(f"📱 Imagem para {to}:")
            print(f"URL: {image_url}")
            print(f"Legenda: {caption}")
            return {"status": "simulated", "to": to}
        
        headers = {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/json"
        }
        
        payload = {
            "messaging_product": "whatsapp",
            "to": to,
            "type": "image",
            "image": {
                "link": image_url,
                "caption": caption
            }
        }
        
        try:
            response = requests.post(self.base_url, json=payload, headers=headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"❌ Erro ao enviar imagem WhatsApp: {e}")
            return {"error": str(e)}


class N8NWebhookClient:
    """Cliente para integração com n8n via webhook"""
    
    def __init__(self, webhook_url: Optional[str] = None):
        self.webhook_url = webhook_url or os.getenv("N8N_WEBHOOK_URL")
        
    def send_content(
        self,
        content: Dict[str, Any],
        profile_id: str,
        action: str = "new_content"
    ) -> Dict[str, Any]:
        """
        Envia conteúdo para n8n processar
        
        Args:
            content: Conteúdo gerado
            profile_id: ID do perfil
            action: Ação a ser executada no n8n
            
        Returns:
            Resposta do webhook
        """
        
        if not self.webhook_url:
            print("⚠️ MODO SIMULAÇÃO: Webhook n8n não configurado.")
            print(f"📤 Enviando para n8n:")
            print(f"Perfil: {profile_id}")
            print(f"Ação: {action}")
            return {"status": "simulated"}
        
        payload = {
            "action": action,
            "profile_id": profile_id,
            "content": content,
            "timestamp": None  # Será preenchido pelo n8n
        }
        
        try:
            response = requests.post(self.webhook_url, json=payload)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"❌ Erro ao enviar para n8n: {e}")
            return {"error": str(e)}
