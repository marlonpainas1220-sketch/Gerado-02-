from abc import ABC, abstractmethod
from typing import Dict, Any, List
from enum import Enum


class ContentType(Enum):
    POST = "post"
    STORY = "story"
    ROTEIRO = "roteiro"
    PACOTE_COMPLETO = "pacote_completo"


class BaseProfile(ABC):
    """Classe base abstrata para todos os perfis de conteúdo"""
    
    def __init__(self, profile_id: str, name: str):
        self.profile_id = profile_id
        self.name = name
        self.memory: List[Dict[str, Any]] = []
        
    @abstractmethod
    def get_system_prompt(self) -> str:
        """Retorna o prompt de sistema específico do perfil"""
        pass
    
    @abstractmethod
    def get_personality_context(self) -> str:
        """Retorna o contexto de personalidade do perfil"""
        pass
    
    @abstractmethod
    def validate_content(self, content: Dict[str, Any]) -> bool:
        """Valida se o conteúdo está adequado ao perfil"""
        pass
    
    def add_to_memory(self, content: Dict[str, Any], metrics: Dict[str, Any] = None):
        """Adiciona conteúdo à memória do perfil"""
        self.memory.append({
            "content": content,
            "metrics": metrics or {},
            "timestamp": None  # Será preenchido pelo sistema
        })
    
    def get_memory_context(self, limit: int = 5) -> str:
        """Retorna contexto dos últimos conteúdos para aprendizado"""
        if not self.memory:
            return "Nenhum conteúdo anterior registrado."
        
        recent = self.memory[-limit:]
        context = "CONTEÚDOS ANTERIORES (para referência e evolução):\n\n"
        
        for idx, item in enumerate(recent, 1):
            context += f"--- Conteúdo {idx} ---\n"
            context += f"{item['content'].get('texto', '')}\n"
            if item.get('metrics'):
                context += f"Métricas: {item['metrics']}\n"
            context += "\n"
        
        return context
