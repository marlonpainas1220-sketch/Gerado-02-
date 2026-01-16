import os

class VisualDNA:
    def __init__(self):
        # Configure aqui os dados do seu LoRA treinado
        self.trigger_word = "ohwx woman"  # Palavra-gatilho do modelo
        self.base_features = "pale skin, platinum blonde bob cut hair, blue eyes, sharp jawline"
        self.quality_modifiers = "8k, raw photo, f/1.8, bokeh, masterpiece, highly detailed skin texture"
        self.negative_prompt = "nsfw, nude, deformed, anime, cartoon, 3d render, bad hands, missing fingers, text, watermark"

    def construct_prompt(self, scenario, outfit="casual trendy outfit", lighting="natural lighting"):
        """
        Constrói o prompt final garantindo que a identidade visual (rosto) seja mantida.
        """
        full_prompt = (
            f"({self.trigger_word}:1.2), {self.base_features}, "
            f"BREAK, {scenario}, "
            f"wearing {outfit}, "
            f"lighting: {lighting}, {self.quality_modifiers}"
        )
        return full_prompt, self.negative_prompt