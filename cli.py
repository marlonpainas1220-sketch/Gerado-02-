#!/usr/bin/env python3
"""
CLI para geração rápida de conteúdo

Uso:
    python cli.py influencer post "tema do post"
    python cli.py gossip story "tema da fofoca"
    python cli.py influencer pacote "tema completo" --ousadia 8 --personality agressiva
"""

import argparse
import sys
from backend.orchestrator import ContentOrchestrator
from backend.profiles.base_profile import ContentType
from backend.profiles.influencer_profile import PersonalityVersion


def main():
    parser = argparse.ArgumentParser(
        description="Gerado-02 - Sistema de Geração de Conteúdo",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    parser.add_argument(
        "profile",
        choices=["influencer", "gossip"],
        help="Perfil para gerar conteúdo"
    )
    
    parser.add_argument(
        "type",
        choices=["post", "story", "roteiro", "pacote"],
        help="Tipo de conteúdo"
    )
    
    parser.add_argument(
        "topic",
        help="Tema/tópico do conteúdo"
    )
    
    parser.add_argument(
        "--personality",
        choices=["soft", "agressiva"],
        default="soft",
        help="Personalidade da influenciadora (apenas para perfil influencer)"
    )
    
    parser.add_argument(
        "--ousadia",
        type=int,
        default=5,
        choices=range(1, 11),
        help="Nível de ousadia 1-10 (apenas para perfil influencer)"
    )
    
    parser.add_argument(
        "--phone",
        help="Número WhatsApp para entrega (formato: 5511999999999)"
    )
    
    parser.add_argument(
        "--n8n",
        action="store_true",
        help="Enviar via n8n webhook"
    )
    
    parser.add_argument(
        "--context",
        help="Contexto adicional para geração"
    )
    
    args = parser.parse_args()
    
    # Mapear tipo de conteúdo
    content_type_map = {
        "post": ContentType.POST,
        "story": ContentType.STORY,
        "roteiro": ContentType.ROTEIRO,
        "pacote": ContentType.PACOTE_COMPLETO
    }
    
    content_type = content_type_map[args.type]
    
    # Mapear personalidade
    personality_map = {
        "soft": PersonalityVersion.SOFT_POWER,
        "agressiva": PersonalityVersion.AGRESSIVA_MAGNETICA
    }
    
    # Inicializar orquestrador
    print("🎬 Iniciando Gerado-02...")
    orchestrator = ContentOrchestrator()
    
    # Preparar configurações
    config = {}
    if args.profile == "influencer":
        config["personality"] = personality_map[args.personality]
        config["ousadia"] = args.ousadia
        
        print(f"🌟 Perfil: Influenciadora de IA")
        print(f"   Personalidade: {args.personality.upper()}")
        print(f"   Ousadia: {args.ousadia}/10")
    else:
        print(f"💬 Perfil: Página de Fofocas")
    
    print(f"📝 Tipo: {args.type.upper()}")
    print(f"🎯 Tema: {args.topic}")
    print()
    
    try:
        # Gerar conteúdo
        print("⚙️ Gerando conteúdo...")
        result = orchestrator.generate_and_deliver(
            profile_name=args.profile,
            content_type=content_type,
            topic=args.topic,
            delivery_phone=args.phone,
            use_n8n=args.n8n,
            additional_context=args.context or "",
            **config
        )
        
        print()
        print("=" * 80)
        print(result["formatted_content"])
        print("=" * 80)
        print()
        
        if args.phone:
            print(f"✅ Enviado via WhatsApp para {args.phone}")
        
        if args.n8n:
            print(f"✅ Enviado via n8n webhook")
        
        print()
        print("🎉 Conteúdo gerado com sucesso!")
        
    except Exception as e:
        print(f"❌ Erro: {str(e)}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
