import os
from typing import Dict, Any, Optional
from openai import OpenAI
from ..profiles.base_profile import BaseProfile, ContentType
from ..profiles.influencer_profile import InfluencerProfile, PersonalityVersion
from ..profiles.gossip_profile import GossipProfile


class ContentGenerator:
    """Motor central de geração de conteúdo usando IA"""
    
    def __init__(self, api_key: Optional[str] = None):
        self.client = OpenAI(api_key=api_key or os.getenv("OPENAI_API_KEY"))
        self.profiles = {
            "influencer": InfluencerProfile(),
            "gossip": GossipProfile()
        }
        
    def get_profile(self, profile_name: str) -> BaseProfile:
        """Retorna o perfil solicitado"""
        if profile_name not in self.profiles:
            raise ValueError(f"Perfil '{profile_name}' não encontrado. Disponíveis: {list(self.profiles.keys())}")
        return self.profiles[profile_name]
    
    def configure_influencer(
        self, 
        personality: PersonalityVersion = PersonalityVersion.SOFT_POWER,
        ousadia: int = 5
    ):
        """Configura a personalidade da influenciadora"""
        influencer = self.profiles["influencer"]
        influencer.set_personality_version(personality)
        influencer.set_ousadia_level(ousadia)
        
    def generate_content(
        self,
        profile_name: str,
        content_type: ContentType,
        topic: str,
        additional_context: str = "",
        auto_validate: bool = True
    ) -> Dict[str, Any]:
        """
        Gera conteúdo para o perfil especificado
        
        Args:
            profile_name: Nome do perfil ("influencer" ou "gossip")
            content_type: Tipo de conteúdo a gerar
            topic: Tema/tópico do conteúdo
            additional_context: Contexto adicional opcional
            auto_validate: Se True, valida automaticamente o conteúdo
            
        Returns:
            Dicionário com o conteúdo gerado
        """
        profile = self.get_profile(profile_name)
        
        # Construir prompt
        user_prompt = self._build_user_prompt(
            profile, 
            content_type, 
            topic, 
            additional_context
        )
        
        # Gerar conteúdo
        response = self.client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": profile.get_personality_context()},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.8,
            max_tokens=2000
        )
        
        raw_content = response.choices[0].message.content
        
        # Parsear resposta
        parsed_content = self._parse_content(raw_content)
        
        # Validar se solicitado
        if auto_validate:
            validated_content = self._validate_and_refine(profile, parsed_content, topic)
            return validated_content
        
        return parsed_content
    
    def _build_user_prompt(
        self,
        profile: BaseProfile,
        content_type: ContentType,
        topic: str,
        additional_context: str
    ) -> str:
        """Constrói o prompt do usuário"""
        
        type_instructions = {
            ContentType.POST: "Gere um POST completo para feed/Instagram.",
            ContentType.STORY: "Gere um STORY (texto curto e impactante para stories).",
            ContentType.ROTEIRO: "Gere um ROTEIRO detalhado para vídeo/reels.",
            ContentType.PACOTE_COMPLETO: "Gere um PACOTE COMPLETO com POST, STORY e ROTEIRO."
        }
        
        prompt = f"""TAREFA: {type_instructions[content_type]}

TEMA/TÓPICO:
{topic}

"""
        
        if additional_context:
            prompt += f"""CONTEXTO ADICIONAL:
{additional_context}

"""
        
        prompt += """FORMATO OBRIGATÓRIO DE SAÍDA:

TÍTULO:
[título chamativo]

TEXTO:
[texto principal do conteúdo]

"""
        
        if content_type in [ContentType.STORY, ContentType.PACOTE_COMPLETO]:
            prompt += """STORY:
[texto para story - curto e impactante]

"""
        
        if content_type in [ContentType.ROTEIRO, ContentType.PACOTE_COMPLETO]:
            prompt += """ROTEIRO:
[roteiro detalhado se aplicável]

"""
        
        prompt += """LEGENDA:
[legenda para a imagem/post]

CTA:
[call-to-action sutil]

OBSERVAÇÕES:
[observações técnicas ou criativas]

IMPORTANTE:
- Siga RIGOROSAMENTE a personalidade e regras do perfil
- O conteúdo deve estar PRONTO PARA POSTAR
- Seja consistente com conteúdos anteriores
- Aplique o checklist de qualidade automaticamente
"""
        
        return prompt
    
    def _parse_content(self, raw_content: str) -> Dict[str, Any]:
        """Parseia o conteúdo bruto da IA em estrutura"""
        content = {
            "titulo": "",
            "texto": "",
            "story": "",
            "roteiro": "",
            "legenda": "",
            "cta": "",
            "observacoes": ""
        }
        
        sections = {
            "TÍTULO:": "titulo",
            "TEXTO:": "texto",
            "STORY:": "story",
            "ROTEIRO:": "roteiro",
            "LEGENDA:": "legenda",
            "CTA:": "cta",
            "OBSERVAÇÕES:": "observacoes"
        }
        
        current_section = None
        lines = raw_content.split("\n")
        
        for line in lines:
            # Verificar se é início de seção
            for marker, key in sections.items():
                if line.strip().startswith(marker):
                    current_section = key
                    break
            else:
                # Adicionar linha à seção atual
                if current_section:
                    content[current_section] += line + "\n"
        
        # Limpar espaços extras
        for key in content:
            content[key] = content[key].strip()
        
        return content
    
    def _validate_and_refine(
        self,
        profile: BaseProfile,
        content: Dict[str, Any],
        original_topic: str
    ) -> Dict[str, Any]:
        """Valida e refina o conteúdo usando checklist automático"""
        
        validation_prompt = f"""Você é um VALIDADOR DE QUALIDADE de conteúdo.

Analise o conteúdo abaixo e responda APENAS "APROVADO" ou liste os problemas encontrados.

CHECKLIST DE QUALIDADE:
1. O conteúdo está coerente com o perfil correto?
2. A linguagem soa humana e natural?
3. Existe impacto logo no início?
4. Não há repetições desnecessárias?
5. O tom respeita o nicho e o nível de ousadia?
6. Está pronto para postar sem ajustes?
7. O CTA é sutil e não forçado?

CONTEÚDO A VALIDAR:
Título: {content.get('titulo')}
Texto: {content.get('texto')}
CTA: {content.get('cta')}

Responda:
"""
        
        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Você é um validador rigoroso de qualidade de conteúdo."},
                {"role": "user", "content": validation_prompt}
            ],
            temperature=0.3,
            max_tokens=500
        )
        
        validation_result = response.choices[0].message.content.strip()
        
        # Se não aprovado, tentar refinar
        if "APROVADO" not in validation_result.upper():
            content["observacoes"] += f"\n\n[VALIDAÇÃO AUTOMÁTICA]: {validation_result}"
            
            # Tentar gerar versão refinada
            refine_prompt = f"""O conteúdo anterior teve os seguintes problemas:
{validation_result}

Por favor, REESCREVA o conteúdo corrigindo esses problemas.

TEMA ORIGINAL: {original_topic}

Mantenha o formato obrigatório de saída.
"""
            
            refined_response = self.client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": profile.get_personality_context()},
                    {"role": "user", "content": refine_prompt}
                ],
                temperature=0.8,
                max_tokens=2000
            )
            
            refined_content = self._parse_content(refined_response.choices[0].message.content)
            refined_content["observacoes"] += "\n[CONTEÚDO REFINADO AUTOMATICAMENTE]"
            return refined_content
        
        content["observacoes"] += "\n[✓ APROVADO NA VALIDAÇÃO AUTOMÁTICA]"
        return content
    
    def generate_and_format(
        self,
        profile_name: str,
        content_type: ContentType,
        topic: str,
        additional_context: str = ""
    ) -> str:
        """Gera conteúdo e retorna formatado para entrega"""
        
        content = self.generate_content(
            profile_name=profile_name,
            content_type=content_type,
            topic=topic,
            additional_context=additional_context,
            auto_validate=True
        )
        
        profile = self.get_profile(profile_name)
        formatted = profile.format_output(content)
        
        # Adicionar ao histórico do perfil
        profile.add_to_memory(content)
        
        return formatted
