def gerar_arquivo(atividades):
    with open("atividades.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write("=== SIGAA ASSISTANT ===\n")
    
        for atividade in atividades:
            arquivo.write(f"📅 {atividade['data']}\n")
            arquivo.write(f"📚 {atividade['disciplina']}\n")
            arquivo.write(f"📝 {atividade['tipo']}: {atividade['nome']}\n\n")