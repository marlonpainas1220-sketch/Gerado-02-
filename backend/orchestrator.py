"""
Orquestrador Central do Sistema de Geração de Conteúdo

Este módulo integra todos os componentes do sistema:
- Perfis (Influenciadora e Fofocas)
- Motor de Geração de Conteúdo
- Sistema de Memória
- Entrega via WhatsApp/n8n
"""

from typing import Dict, Any, Optional
from .profiles.base_profile import ContentType
from .profiles.influencer_profile import PersonalityVersion
from .engine.content_generator import ContentGenerator
from .memory.memory_manager import MemoryManager
from .delivery.whatsapp_client import WhatsAppClient, N8NWebhookClient


class ContentOrchestrator:
    """Orquestrador central do sistema de geração de conteúdo"""
    
    def __init__(self):
        self.generator = ContentGenerator()
        self.memory = MemoryManager()
        self.whatsapp = WhatsAppClient()
        self.n8n = N8NWebhookClient()
        
    def generate_and_deliver(
        self,
        profile_name: str,
        content_type: ContentType,
        topic: str,
        delivery_phone: Optional[str] = None,
        use_n8n: bool = False,
        additional_context: str = "",
        **profile_config
    ) -> Dict[str, Any]:
        """
        Pipeline completo: Gera conteúdo, salva na memória e entrega
        
        Args:
            profile_name: Nome do perfil ("influencer" ou "gossip")
            content_type: Tipo de conteúdo
            topic: Tema do conteúdo
            delivery_phone: Número WhatsApp para entrega (opcional)
            use_n8n: Se True, envia via n8n webhook
            additional_context: Contexto adicional
            **profile_config: Configurações específicas do perfil
            
        Returns:
            Resultado completo da operação
        """
        
        # Configurar perfil se necessário
        if profile_name == "influencer" and profile_config:
            if "personality" in profile_config:
                self.generator.configure_influencer(
                    personality=profile_config["personality"],
                    ousadia=profile_config.get("ousadia", 5)
                )
        
        # Adicionar contexto de aprendizado
        learning_context = self.memory.get_learning_context(profile_name)
        full_context = f"{additional_context}\n\n{learning_context}"
        
        # Gerar conteúdo
        print(f"🎨 Gerando conteúdo para perfil: {profile_name}")
        formatted_content = self.generator.generate_and_format(
            profile_name=profile_name,
            content_type=content_type,
            topic=topic,
            additional_context=full_context
        )
        
        # Obter conteúdo estruturado para salvar
        content_dict = self.generator.generate_content(
            profile_name=profile_name,
            content_type=content_type,
            topic=topic,
            additional_context=full_context,
            auto_validate=True
        )
        
        # Salvar na memória
        print(f"💾 Salvando na memória do perfil...")
        self.memory.save_content(
            profile_id=profile_name,
            content=content_dict
        )
        
        result = {
            "status": "success",
            "profile": profile_name,
            "content_type": content_type.value,
            "formatted_content": formatted_content,
            "raw_content": content_dict
        }
        
        # Entregar via WhatsApp
        if delivery_phone:
            print(f"📱 Enviando via WhatsApp para {delivery_phone}...")
            whatsapp_result = self.whatsapp.send_content_delivery(
                to=delivery_phone,
                content=formatted_content,
                profile_name=profile_name
            )
            result["whatsapp_delivery"] = whatsapp_result
        
        # Entregar via n8n
        if use_n8n:
            print(f"🔗 Enviando para n8n webhook...")
            n8n_result = self.n8n.send_content(
                content=content_dict,
                profile_id=profile_name,
                action="new_content"
            )
            result["n8n_delivery"] = n8n_result
        
        print("✅ Processo completo!")
        return result
    
    def generate_influencer_content(
        self,
        content_type: ContentType,
        topic: str,
        personality: PersonalityVersion = PersonalityVersion.SOFT_POWER,
        ousadia: int = 5,
        delivery_phone: Optional[str] = None
    ) -> Dict[str, Any]:
        """Atalho para gerar conteúdo da influenciadora"""
        
        return self.generate_and_deliver(
            profile_name="influencer",
            content_type=content_type,
            topic=topic,
            delivery_phone=delivery_phone,
            personality=personality,
            ousadia=ousadia
        )
    
    def generate_gossip_content(
        self,
        content_type: ContentType,
        topic: str,
        delivery_phone: Optional[str] = None
    ) -> Dict[str, Any]:
        """Atalho para gerar conteúdo de fofocas"""
        
        return self.generate_and_deliver(
            profile_name="gossip",
            content_type=content_type,
            topic=topic,
            delivery_phone=delivery_phone
        )
    
    def get_profile_analytics(self, profile_name: str) -> Dict[str, Any]:
        """Retorna análise completa do perfil"""
        
        return self.memory.analyze_patterns(profile_name)
    
    def get_profile_best_content(
        self,
        profile_name: str,
        metric: str = "engagement",
        limit: int = 5
    ) -> list:
        """Retorna os melhores conteúdos do perfil"""
        
        return self.memory.get_best_performing(
            profile_id=profile_name,
            metric=metric,
            limit=limit
        )
