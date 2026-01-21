"""
Exemplos de uso do sistema Gerado-02

Este arquivo demonstra como usar o sistema de geração de conteúdo
"""

from backend.orchestrator import ContentOrchestrator
from backend.profiles.base_profile import ContentType
from backend.profiles.influencer_profile import PersonalityVersion


def exemplo_influencer_soft():
    """Exemplo: Influenciadora com personalidade Soft Power"""
    
    print("=" * 80)
    print("EXEMPLO 1: Influenciadora - Soft Power - Ousadia 5")
    print("=" * 80)
    
    orchestrator = ContentOrchestrator()
    
    result = orchestrator.generate_influencer_content(
        content_type=ContentType.POST,
        topic="Reflexão sobre autenticidade e ser verdadeira consigo mesma",
        personality=PersonalityVersion.SOFT_POWER,
        ousadia=5
    )
    
    print(result["formatted_content"])
    print()


def exemplo_influencer_agressiva():
    """Exemplo: Influenciadora com personalidade Agressiva Magnética"""
    
    print("=" * 80)
    print("EXEMPLO 2: Influenciadora - Agressiva Magnética - Ousadia 8")
    print("=" * 80)
    
    orchestrator = ContentOrchestrator()
    
    result = orchestrator.generate_influencer_content(
        content_type=ContentType.STORY,
        topic="Confiança e poder feminino",
        personality=PersonalityVersion.AGRESSIVA_MAGNETICA,
        ousadia=8
    )
    
    print(result["formatted_content"])
    print()


def exemplo_gossip():
    """Exemplo: Página de Fofocas"""
    
    print("=" * 80)
    print("EXEMPLO 3: Página de Fofocas")
    print("=" * 80)
    
    orchestrator = ContentOrchestrator()
    
    result = orchestrator.generate_gossip_content(
        content_type=ContentType.POST,
        topic="Celebridade flagrada em situação constrangedora no restaurante"
    )
    
    print(result["formatted_content"])
    print()


def exemplo_pacote_completo():
    """Exemplo: Pacote completo de conteúdo"""
    
    print("=" * 80)
    print("EXEMPLO 4: Pacote Completo - Influenciadora")
    print("=" * 80)
    
    orchestrator = ContentOrchestrator()
    
    result = orchestrator.generate_influencer_content(
        content_type=ContentType.PACOTE_COMPLETO,
        topic="Lançamento de nova coleção de moda",
        personality=PersonalityVersion.SOFT_POWER,
        ousadia=6
    )
    
    print(result["formatted_content"])
    print()


def exemplo_com_entrega_whatsapp():
    """Exemplo: Geração com entrega via WhatsApp"""
    
    print("=" * 80)
    print("EXEMPLO 5: Com Entrega via WhatsApp (Simulação)")
    print("=" * 80)
    
    orchestrator = ContentOrchestrator()
    
    # NOTA: Substitua pelo número real para teste
    result = orchestrator.generate_influencer_content(
        content_type=ContentType.POST,
        topic="Rotina matinal de autocuidado",
        personality=PersonalityVersion.SOFT_POWER,
        ousadia=4,
        delivery_phone="5511999999999"  # Número de exemplo
    )
    
    print(result["formatted_content"])
    print()
    print("Status WhatsApp:", result.get("whatsapp_delivery", {}))
    print()


def exemplo_analytics():
    """Exemplo: Análise de performance do perfil"""
    
    print("=" * 80)
    print("EXEMPLO 6: Analytics do Perfil")
    print("=" * 80)
    
    orchestrator = ContentOrchestrator()
    
    # Primeiro, gerar alguns conteúdos
    for i in range(3):
        orchestrator.generate_influencer_content(
            content_type=ContentType.POST,
            topic=f"Tema de teste {i+1}",
            personality=PersonalityVersion.SOFT_POWER,
            ousadia=5
        )
    
    # Analisar
    analytics = orchestrator.get_profile_analytics("influencer")
    
    print("Analytics:")
    print(analytics)
    print()


if __name__ == "__main__":
    print("\n🎬 GERADO-02 - EXEMPLOS DE USO\n")
    
    # Descomente os exemplos que deseja executar:
    
    # exemplo_influencer_soft()
    # exemplo_influencer_agressiva()
    # exemplo_gossip()
    # exemplo_pacote_completo()
    # exemplo_com_entrega_whatsapp()
    # exemplo_analytics()
    
    print("\n💡 Descomente os exemplos no código para executá-los")
    print("💡 Configure OPENAI_API_KEY no .env antes de usar")
