import logging

class Logger:
    def __init__(self, filename="registry.log"):
        self.filename = filename
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        
        formatter = logging.Formatter("%(asctime)s - %(threadName)s - %(processName)s - %(levelname)s - %(message)s")
        
        file_handler = logging.FileHandler(filename, mode="a")
        file_handler.setLevel(logging.INFO)
        file_handler.setFormatter(formatter)
        
        self.logger.addHandler(file_handler)
    
    def info(self, message):
        self.logger.info(message)
    
    def error(self, message):
        self.logger.error(message)

# Ejemplo de uso:
# if __name__ == "__main__":
#     logger = Logger()
#     logger.info("Este es un mensaje de información.")
#     logger.error("Este es un mensaje de error.")