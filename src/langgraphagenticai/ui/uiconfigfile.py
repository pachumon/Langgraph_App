from configparser import ConfigParser

class Config:
    def __init__(self, config_file='src/langgraphagenticai/ui/uiconfigfile.ini'):
        self.config = ConfigParser()
        self.config.read(config_file)

    def get(self, section, option):
        return self.config.get(section, option)

    def get_list(self, section, option):
        value = self.get(section, option)
        return [item.strip() for item in value.split(',')]
    
    def get_llms(self):
        return self.get_list('DEFAULT', 'LLM_OPTIONS')
    
    def get_usecases(self):
        return self.get_list('DEFAULT', 'USECASE_OPTIONS')
    
    def get_groq_models(self):
        return self.get_list('DEFAULT', 'GROQ_MODEL_OPTIONS')
    
    def get_page_title(self):
        return self.get('DEFAULT', 'PAGE_TITLE')