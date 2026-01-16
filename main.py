import schedule
import time
import os
from dotenv import load_dotenv
from backend.generators.visual_dna import VisualDNA
from backend.integrations.instagram import InstagramClient

load_dotenv()

# Configuração
AUTO_MODE = os.getenv("AUTO_MODE", "False") == "True"
dna_engine = VisualDNA()
ig_client = InstagramClient()

def job_morning_routine():
    print("☀️ Iniciando Rotina da Manhã (Stories)...")
    # Lógica de geração de story aqui
    prompt, _ = dna_engine.construct_prompt("drinking coffee at balcony", "pajamas")
    print(f"🎨 Gerando visual com prompt: {prompt}")
    # Simulação de envio
    print("✅ Story Enviado (Simulação)")

def job_evening_routine():
    print("🌙 Iniciando Rotina da Noite (Feed)...")
    prompt, _ = dna_engine.construct_prompt("walking in city center neon lights", "leather jacket")
    print(f"🎨 Gerando visual com prompt: {prompt}")
    
    if AUTO_MODE:
        ig_client.post_photo("https://exemplo.com/imagem.jpg", "Legenda gerada por AI #cyberpunk")
    else:
        print("💾 Conteúdo salvo no Banco de Dados para aprovação manual.")

# Agendamento
schedule.every().day.at("09:00").do(job_morning_routine)
schedule.every().day.at("18:00").do(job_evening_routine)

print("🤖 Gerado-02 Engine Iniciado... Aguardando jobs.")

if __name__ == "__main__":
    while True:
        schedule.run_pending()
        time.sleep(1)