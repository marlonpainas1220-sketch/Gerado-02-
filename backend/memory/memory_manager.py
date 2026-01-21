import json
import os
from datetime import datetime
from typing import Dict, Any, List, Optional
from pathlib import Path


class MemoryManager:
    """Gerenciador de memória evolutiva para perfis"""
    
    def __init__(self, storage_path: str = "data/memory"):
        self.storage_path = Path(storage_path)
        self.storage_path.mkdir(parents=True, exist_ok=True)
        
    def _get_profile_file(self, profile_id: str) -> Path:
        """Retorna o caminho do arquivo de memória do perfil"""
        return self.storage_path / f"{profile_id}_memory.json"
    
    def save_content(
        self,
        profile_id: str,
        content: Dict[str, Any],
        metrics: Optional[Dict[str, Any]] = None
    ):
        """Salva conteúdo na memória do perfil"""
        
        memory_file = self._get_profile_file(profile_id)
        
        # Carregar memória existente
        if memory_file.exists():
            with open(memory_file, 'r', encoding='utf-8') as f:
                memory_data = json.load(f)
        else:
            memory_data = {
                "profile_id": profile_id,
                "contents": [],
                "analytics": {
                    "total_contents": 0,
                    "best_performing": [],
                    "patterns": {}
                }
            }
        
        # Adicionar novo conteúdo
        entry = {
            "timestamp": datetime.now().isoformat(),
            "content": content,
            "metrics": metrics or {},
            "id": len(memory_data["contents"]) + 1
        }
        
        memory_data["contents"].append(entry)
        memory_data["analytics"]["total_contents"] += 1
        
        # Salvar
        with open(memory_file, 'w', encoding='utf-8') as f:
            json.dump(memory_data, f, ensure_ascii=False, indent=2)
    
    def get_recent_contents(
        self,
        profile_id: str,
        limit: int = 10
    ) -> List[Dict[str, Any]]:
        """Retorna os conteúdos mais recentes do perfil"""
        
        memory_file = self._get_profile_file(profile_id)
        
        if not memory_file.exists():
            return []
        
        with open(memory_file, 'r', encoding='utf-8') as f:
            memory_data = json.load(f)
        
        return memory_data["contents"][-limit:]
    
    def get_best_performing(
        self,
        profile_id: str,
        metric: str = "engagement",
        limit: int = 5
    ) -> List[Dict[str, Any]]:
        """Retorna os conteúdos com melhor performance"""
        
        memory_file = self._get_profile_file(profile_id)
        
        if not memory_file.exists():
            return []
        
        with open(memory_file, 'r', encoding='utf-8') as f:
            memory_data = json.load(f)
        
        # Ordenar por métrica
        contents = memory_data["contents"]
        sorted_contents = sorted(
            contents,
            key=lambda x: x.get("metrics", {}).get(metric, 0),
            reverse=True
        )
        
        return sorted_contents[:limit]
    
    def analyze_patterns(self, profile_id: str) -> Dict[str, Any]:
        """Analisa padrões nos conteúdos do perfil"""
        
        memory_file = self._get_profile_file(profile_id)
        
        if not memory_file.exists():
            return {"error": "Nenhuma memória encontrada"}
        
        with open(memory_file, 'r', encoding='utf-8') as f:
            memory_data = json.load(f)
        
        contents = memory_data["contents"]
        
        if not contents:
            return {"error": "Nenhum conteúdo na memória"}
        
        # Análise básica
        analysis = {
            "total_contents": len(contents),
            "date_range": {
                "first": contents[0]["timestamp"],
                "last": contents[-1]["timestamp"]
            },
            "avg_metrics": self._calculate_avg_metrics(contents),
            "common_themes": self._extract_common_themes(contents),
            "performance_trends": self._analyze_trends(contents)
        }
        
        return analysis
    
    def _calculate_avg_metrics(self, contents: List[Dict[str, Any]]) -> Dict[str, float]:
        """Calcula métricas médias"""
        
        metrics_sum = {}
        metrics_count = {}
        
        for content in contents:
            metrics = content.get("metrics", {})
            for key, value in metrics.items():
                if isinstance(value, (int, float)):
                    metrics_sum[key] = metrics_sum.get(key, 0) + value
                    metrics_count[key] = metrics_count.get(key, 0) + 1
        
        avg_metrics = {}
        for key in metrics_sum:
            avg_metrics[key] = metrics_sum[key] / metrics_count[key]
        
        return avg_metrics
    
    def _extract_common_themes(self, contents: List[Dict[str, Any]]) -> List[str]:
        """Extrai temas comuns dos conteúdos"""
        # Implementação simplificada - pode ser melhorada com NLP
        themes = []
        
        for content in contents[-10:]:  # Últimos 10
            titulo = content.get("content", {}).get("titulo", "")
            if titulo:
                themes.append(titulo[:50])  # Primeiras palavras
        
        return themes
    
    def _analyze_trends(self, contents: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Analisa tendências de performance"""
        
        if len(contents) < 5:
            return {"status": "Dados insuficientes para análise de tendências"}
        
        recent = contents[-5:]
        older = contents[-10:-5] if len(contents) >= 10 else contents[:-5]
        
        recent_avg = self._calculate_avg_metrics(recent)
        older_avg = self._calculate_avg_metrics(older)
        
        trends = {}
        for metric in recent_avg:
            if metric in older_avg:
                change = ((recent_avg[metric] - older_avg[metric]) / older_avg[metric]) * 100
                trends[metric] = {
                    "change_percent": round(change, 2),
                    "direction": "up" if change > 0 else "down",
                    "recent_avg": round(recent_avg[metric], 2),
                    "older_avg": round(older_avg[metric], 2)
                }
        
        return trends
    
    def get_learning_context(self, profile_id: str) -> str:
        """Gera contexto de aprendizado para o perfil"""
        
        recent = self.get_recent_contents(profile_id, limit=5)
        best = self.get_best_performing(profile_id, limit=3)
        patterns = self.analyze_patterns(profile_id)
        
        context = "=== CONTEXTO DE APRENDIZADO ===\n\n"
        
        # Conteúdos recentes
        if recent:
            context += "CONTEÚDOS RECENTES:\n"
            for idx, item in enumerate(recent, 1):
                content = item.get("content", {})
                context += f"\n{idx}. {content.get('titulo', 'Sem título')}\n"
                context += f"   Texto: {content.get('texto', '')[:100]}...\n"
                if item.get("metrics"):
                    context += f"   Métricas: {item['metrics']}\n"
            context += "\n"
        
        # Melhores performances
        if best:
            context += "MELHORES PERFORMANCES:\n"
            for idx, item in enumerate(best, 1):
                content = item.get("content", {})
                context += f"\n{idx}. {content.get('titulo', 'Sem título')}\n"
                context += f"   Métricas: {item.get('metrics', {})}\n"
            context += "\n"
        
        # Padrões e tendências
        if "error" not in patterns:
            context += "ANÁLISE DE PADRÕES:\n"
            context += f"Total de conteúdos: {patterns.get('total_contents', 0)}\n"
            
            if patterns.get("avg_metrics"):
                context += f"Métricas médias: {patterns['avg_metrics']}\n"
            
            if patterns.get("performance_trends"):
                context += "\nTendências de performance:\n"
                for metric, trend in patterns["performance_trends"].items():
                    context += f"  - {metric}: {trend['direction']} ({trend['change_percent']}%)\n"
        
        context += "\n=== FIM DO CONTEXTO ===\n"
        
        return context
