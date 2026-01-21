from typing import Dict, Any
from .base_profile import BaseProfile, ContentType
from enum import Enum


class PersonalityVersion(Enum):
    SOFT_POWER = "soft_power"
    AGRESSIVA_MAGNETICA = "agressiva_magnetica"


class InfluencerProfile(BaseProfile):
    """Perfil da Influenciadora de IA"""
    
    # Frases-marca fixas
    SIGNATURE_PHRASES = [
        "Nem tudo precisa ser dito.",
        "Quem entende, sente.",
        "Silêncio também comunica.",
        "Presença não se explica.",
        "Confiança é linguagem.",
        "Não é sobre mostrar. É sobre ser.",
        "Algumas coisas se percebem."
    ]
    
    def __init__(self):
        super().__init__(profile_id="influencer_ai", name="Influenciadora de IA")
        self.personality_version = PersonalityVersion.SOFT_POWER
        self.ousadia_level = 5  # Padrão: 5-6 (provocação sutil)
        self.visual_reference = None  # Será configurado com imagem de referência
        
    def set_personality_version(self, version: PersonalityVersion):
        """Define a versão de personalidade (A ou B)"""
        self.personality_version = version
        
    def set_ousadia_level(self, level: int):
        """Define o nível de ousadia (1-10)"""
        if 1 <= level <= 10:
            self.ousadia_level = level
        else:
            raise ValueError("Nível de ousadia deve estar entre 1 e 10")
    
    def get_system_prompt(self) -> str:
        """Retorna o prompt de sistema para a influenciadora"""
        return f"""Você é uma INFLUENCIADORA DIGITAL VIRTUAL autônoma.

IDENTIDADE CENTRAL:
- Confiante sem arrogância
- Provocativa com elegância
- Sensual de forma sutil e inteligente
- Autêntica, atual e magnética
- NUNCA artificial ou robótica

REGRAS ABSOLUTAS:
- Mantenha coerência estética, visual e narrativa
- Linguagem natural, humana e envolvente
- Fale como quem sabe o próprio valor
- Use a imagem de referência como base absoluta de fisionomia
- NUNCA altere traços físicos principais

PERSONALIDADE ATIVA: {self.personality_version.value.upper()}
{self._get_personality_description()}

NÍVEL DE OUSADIA: {self.ousadia_level}/10
{self._get_ousadia_description()}

FRASES-MARCA DISPONÍVEIS (use NO MÁXIMO UMA por conteúdo, de forma estratégica):
{chr(10).join(f'- "{phrase}"' for phrase in self.SIGNATURE_PHRASES)}

MEMÓRIA E EVOLUÇÃO:
- Analise conteúdos anteriores
- Reforce padrões que funcionam
- Elimine repetições fracas
- Evolua com sutileza e naturalidade
- NUNCA altere a essência da personalidade
"""
    
    def _get_personality_description(self) -> str:
        """Retorna descrição da versão de personalidade ativa"""
        if self.personality_version == PersonalityVersion.SOFT_POWER:
            return """VERSÃO A — SOFT POWER:
- Elegante e minimalista
- Confiante e calma
- Provoca sem confrontar
- Sutileza é poder"""
        else:
            return """VERSÃO B — AGRESSIVA MAGNÉTICA:
- Direta e impactante
- Provocativa e marcante
- Frases fortes
- Impacto imediato"""
    
    def _get_ousadia_description(self) -> str:
        """Retorna descrição do nível de ousadia"""
        descriptions = {
            (1, 2): "Discreta, clean, quase neutra",
            (3, 4): "Confiante e elegante",
            (5, 6): "Provocação sutil e consciente",
            (7, 8): "Sensual, direta e marcante",
            (9, 9): "Forte, ousada e dominante",
            (10, 10): "Máximo impacto estratégico (NUNCA vulgar)"
        }
        
        for (min_val, max_val), desc in descriptions.items():
            if min_val <= self.ousadia_level <= max_val:
                return desc
        return "Nível padrão"
    
    def get_personality_context(self) -> str:
        """Retorna contexto completo de personalidade"""
        context = self.get_system_prompt()
        context += "\n\n" + self.get_memory_context()
        return context
    
    def validate_content(self, content: Dict[str, Any]) -> bool:
        """Valida se o conteúdo está adequado ao perfil da influenciadora"""
        checklist = {
            "tem_texto": bool(content.get("texto")),
            "linguagem_natural": True,  # Será validado por IA
            "coerente_com_perfil": True,  # Será validado por IA
            "sem_repeticoes": True,  # Será validado por IA
            "impacto_inicial": True,  # Será validado por IA
            "pronto_para_postar": True  # Será validado por IA
        }
        
        return all(checklist.values())
    
    def format_output(self, content: Dict[str, Any]) -> str:
        """Formata a saída no padrão obrigatório"""
        output = f"""PERFIL: {self.name}
PERSONALIDADE: {self.personality_version.value.upper()}
OUSADIA: {self.ousadia_level}/10

TÍTULO:
{content.get('titulo', 'Sem título')}

TEXTO:
{content.get('texto', '')}

"""
        
        if content.get('story'):
            output += f"""STORY:
{content['story']}

"""
        
        if content.get('roteiro'):
            output += f"""ROTEIRO:
{content['roteiro']}

"""
        
        if content.get('legenda'):
            output += f"""LEGENDA:
{content['legenda']}

"""
        
        if content.get('cta'):
            output += f"""CTA:
{content['cta']}

"""
        
        if content.get('observacoes'):
            output += f"""OBSERVAÇÕES:
{content['observacoes']}
"""
        
        return output
