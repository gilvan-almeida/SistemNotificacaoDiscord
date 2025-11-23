def formatHoras(seconds: int) -> str:
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60
    formatado = f"{hours:02d}:{minutes:02d}:{secs:02d}"
    return formatado