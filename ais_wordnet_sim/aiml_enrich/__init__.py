from .enrich_model import AIMLEnrich

def aiml_enrich(aiml_file_in, aiml_file_out='enriched_data.aiml'):
    model = AIMLEnrich(aiml_file_in, aiml_file_out)
    model.compute()