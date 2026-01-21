from typing import Dict, Any
from .base_profile import BaseProfile, ContentType


class GossipProfile(BaseProfile):
    """Perfil da Página de Fofocas"""
    
    def __init__(self):
        super().__init__(profile_id="gossip_page", name="Página de Fofocas")
        
    def get_system_prompt(self) -> str:
        """Retorna o prompt de sistema para a página de fofocas"""
        return """Você é uma PÁGINA DIGITAL DE FOFOCAS.

IDENTIDADE:
- NÃO use persona humana fixa
- Use sarcasmo, ironia e impacto
- Texto curto, chamativo e viral
- Conteúdo fácil de printar e compartilhar
- Priorize gancho imediato

REGRAS:
- Linguagem coloquial e direta
- Emojis estratégicos para impacto
- Títulos chamativos e clickbait inteligente
- Informação rápida e digestível
- Sempre deixe um gancho para engajamento

ESTILO:
- Sarcástico mas não ofensivo
- Irônico e inteligente
- Viral e compartilhável
- Foco em entretenimento

FORMATO:
- Títulos curtos e impactantes
- Texto direto ao ponto
- Use quebras de linha estratégicas
- Emojis para destacar pontos-chave
- CTA que incentive comentários/compartilhamentos
"""
    
    def get_personality_context(self) -> str:
        """Retorna contexto completo de personalidade"""
        context = self.get_system_prompt()
        context += "\n\n" + self.get_memory_context()
        return context
    
    def validate_content(self, content: Dict[str, Any]) -> bool:
        """Valida se o conteúdo está adequado ao perfil de fofocas"""
        checklist = {
            "tem_texto": bool(content.get("texto")),
            "tem_titulo": bool(content.get("titulo")),
            "texto_curto": len(content.get("texto", "")) < 500,  # Fofocas devem ser curtas
            "tem_gancho": True,  # Será validado por IA
        }
        
        return all(checklist.values())
    
    def format_output(self, content: Dict[str, Any]) -> str:
        """Formata a saída no padrão obrigatório"""
        output = f"""PERFIL: {self.name}

TÍTULO:
{content.get('titulo', 'Sem título')}

TEXTO:
{content.get('texto', '')}

"""
        
        if content.get('story'):
            output += f"""STORY:
{content['story']}

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
