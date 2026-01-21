"""
Script de teste do sistema Gerado-02

Testa todos os componentes principais sem necessidade de API keys
"""

import sys
from backend.profiles.influencer_profile import InfluencerProfile, PersonalityVersion
from backend.profiles.gossip_profile import GossipProfile
from backend.profiles.base_profile import ContentType


def test_profiles():
    """Testa a criação e configuração dos perfis"""
    
    print("=" * 80)
    print("TESTE 1: Perfis")
    print("=" * 80)
    
    # Teste Influenciadora
    influencer = InfluencerProfile()
    print(f"✓ Perfil Influenciadora criado: {influencer.name}")
    print(f"  ID: {influencer.profile_id}")
    print(f"  Personalidade padrão: {influencer.personality_version.value}")
    print(f"  Ousadia padrão: {influencer.ousadia_level}")
    
    # Configurar personalidade
    influencer.set_personality_version(PersonalityVersion.AGRESSIVA_MAGNETICA)
    influencer.set_ousadia_level(8)
    print(f"✓ Personalidade alterada para: {influencer.personality_version.value}")
    print(f"✓ Ousadia alterada para: {influencer.ousadia_level}")
    
    # Teste Fofocas
    gossip = GossipProfile()
    print(f"✓ Perfil Fofocas criado: {gossip.name}")
    print(f"  ID: {gossip.profile_id}")
    
    print()
    return True


def test_system_prompts():
    """Testa a geração de prompts do sistema"""
    
    print("=" * 80)
    print("TESTE 2: System Prompts")
    print("=" * 80)
    
    influencer = InfluencerProfile()
    influencer.set_personality_version(PersonalityVersion.SOFT_POWER)
    influencer.set_ousadia_level(5)
    
    prompt = influencer.get_system_prompt()
    print("✓ System prompt da Influenciadora gerado")
    print(f"  Tamanho: {len(prompt)} caracteres")
    print(f"  Contém 'SOFT_POWER': {'SOFT_POWER' in prompt}")
    print(f"  Contém 'NÍVEL DE OUSADIA: 5': {'NÍVEL DE OUSADIA: 5' in prompt}")
    
    gossip = GossipProfile()
    prompt = gossip.get_system_prompt()
    print("✓ System prompt de Fofocas gerado")
    print(f"  Tamanho: {len(prompt)} caracteres")
    print(f"  Contém 'sarcasmo': {'sarcasmo' in prompt.lower()}")
    
    print()
    return True


def test_memory():
    """Testa o sistema de memória"""
    
    print("=" * 80)
    print("TESTE 3: Sistema de Memória")
    print("=" * 80)
    
    from backend.memory.memory_manager import MemoryManager
    
    memory = MemoryManager(storage_path="data/test_memory")
    
    # Salvar conteúdo de teste
    test_content = {
        "titulo": "Teste de Memória",
        "texto": "Este é um conteúdo de teste",
        "cta": "Teste CTA"
    }
    
    test_metrics = {
        "likes": 100,
        "comments": 20,
        "shares": 15,
        "engagement": 135
    }
    
    memory.save_content("test_profile", test_content, test_metrics)
    print("✓ Conteúdo salvo na memória")
    
    # Recuperar conteúdo
    recent = memory.get_recent_contents("test_profile", limit=1)
    print(f"✓ Conteúdo recuperado: {len(recent)} item(s)")
    
    if recent:
        print(f"  Título: {recent[0]['content']['titulo']}")
        print(f"  Métricas: {recent[0]['metrics']}")
    
    # Salvar mais conteúdos para teste de analytics
    for i in range(5):
        memory.save_content(
            "test_profile",
            {"titulo": f"Teste {i+2}", "texto": f"Conteúdo {i+2}"},
            {"engagement": 100 + (i * 10)}
        )
    
    print(f"✓ Total de {len(memory.get_recent_contents('test_profile'))} conteúdos salvos")
    
    # Testar analytics
    analytics = memory.analyze_patterns("test_profile")
    if "error" not in analytics:
        print(f"✓ Analytics gerado")
        print(f"  Total de conteúdos: {analytics.get('total_contents', 0)}")
    
    # Limpar dados de teste
    import shutil
    from pathlib import Path
    test_path = Path("data/test_memory")
    if test_path.exists():
        shutil.rmtree(test_path)
        print("✓ Dados de teste limpos")
    
    print()
    return True


def test_content_formatting():
    """Testa a formatação de conteúdo"""
    
    print("=" * 80)
    print("TESTE 4: Formatação de Conteúdo")
    print("=" * 80)
    
    influencer = InfluencerProfile()
    
    test_content = {
        "titulo": "Teste de Formatação",
        "texto": "Este é um texto de teste para verificar a formatação.",
        "story": "Story de teste",
        "legenda": "Legenda de teste",
        "cta": "CTA de teste",
        "observacoes": "Observações de teste"
    }
    
    formatted = influencer.format_output(test_content)
    print("✓ Conteúdo formatado")
    print(f"  Tamanho: {len(formatted)} caracteres")
    print(f"  Contém 'TÍTULO:': {'TÍTULO:' in formatted}")
    print(f"  Contém 'TEXTO:': {'TEXTO:' in formatted}")
    print(f"  Contém 'STORY:': {'STORY:' in formatted}")
    
    print("\nPreview da formatação:")
    print("-" * 80)
    print(formatted[:300] + "...")
    print("-" * 80)
    
    print()
    return True


def test_delivery_clients():
    """Testa os clientes de entrega (modo simulação)"""
    
    print("=" * 80)
    print("TESTE 5: Clientes de Entrega (Simulação)")
    print("=" * 80)
    
    from backend.delivery.whatsapp_client import WhatsAppClient, N8NWebhookClient
    
    # WhatsApp (sem credenciais = modo simulação)
    whatsapp = WhatsAppClient()
    print("✓ WhatsApp client criado")
    
    result = whatsapp.send_text_message(
        to="5511999999999",
        message="Teste de mensagem"
    )
    print(f"✓ Mensagem enviada (simulação): {result.get('status')}")
    
    # n8n (sem webhook = modo simulação)
    n8n = N8NWebhookClient()
    print("✓ n8n client criado")
    
    result = n8n.send_content(
        content={"teste": "conteúdo"},
        profile_id="test",
        action="test_action"
    )
    print(f"✓ Webhook enviado (simulação): {result.get('status')}")
    
    print()
    return True


def test_visual_dna():
    """Testa o gerador de Visual DNA"""
    
    print("=" * 80)
    print("TESTE 6: Visual DNA")
    print("=" * 80)
    
    from backend.generators.visual_dna import VisualDNA
    
    dna = VisualDNA()
    print("✓ Visual DNA criado")
    
    prompt, negative = dna.construct_prompt(
        scenario="sitting in a cafe",
        outfit="white dress",
        lighting="natural lighting"
    )
    
    print("✓ Prompt gerado")
    print(f"  Tamanho do prompt: {len(prompt)} caracteres")
    print(f"  Contém trigger word: {dna.trigger_word in prompt}")
    print(f"  Tamanho do negative: {len(negative)} caracteres")
    
    print("\nPreview do prompt:")
    print("-" * 80)
    print(prompt[:200] + "...")
    print("-" * 80)
    
    print()
    return True


def run_all_tests():
    """Executa todos os testes"""
    
    print("\n")
    print("🎬 GERADO-02 - SUITE DE TESTES")
    print("=" * 80)
    print()
    
    tests = [
        ("Perfis", test_profiles),
        ("System Prompts", test_system_prompts),
        ("Sistema de Memória", test_memory),
        ("Formatação de Conteúdo", test_content_formatting),
        ("Clientes de Entrega", test_delivery_clients),
        ("Visual DNA", test_visual_dna)
    ]
    
    results = []
    
    for name, test_func in tests:
        try:
            success = test_func()
            results.append((name, success, None))
        except Exception as e:
            results.append((name, False, str(e)))
            print(f"❌ ERRO no teste '{name}': {e}")
            print()
    
    # Resumo
    print("=" * 80)
    print("RESUMO DOS TESTES")
    print("=" * 80)
    
    passed = sum(1 for _, success, _ in results if success)
    total = len(results)
    
    for name, success, error in results:
        status = "✅ PASSOU" if success else "❌ FALHOU"
        print(f"{status} - {name}")
        if error:
            print(f"         Erro: {error}")
    
    print()
    print(f"Total: {passed}/{total} testes passaram")
    
    if passed == total:
        print("\n🎉 TODOS OS TESTES PASSARAM!")
        return 0
    else:
        print(f"\n⚠️ {total - passed} teste(s) falharam")
        return 1


if __name__ == "__main__":
    sys.exit(run_all_tests())
