import logging
import os
from datetime import datetime


class Logger:
    """Classe responsável por gerenciar o sistema de logs do jogo"""
    
    _instance = None
    
    def __new__(cls):
        """Implementa o padrão Singleton para garantir uma única instância do logger."""
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)
            cls._instance._initialize_logger()
        return cls._instance
    
    def _initialize_logger(self):
        """Inicializa o logger com configurações padrão."""
        # Cria diretório de logs se não existir
        log_dir = "logs"
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
            
        # Configura o nome do arquivo de log com timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        log_file = os.path.join(log_dir, f"skyfighters_{timestamp}.log")
        
        # Configura o logger
        self.logger = logging.getLogger("SkyFighters")
        self.logger.setLevel(logging.DEBUG)
        
        # Handler para arquivo
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(logging.DEBUG)
        
        # Handler para console
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        
        # Formato do log
        formatter = logging.Formatter('[%(asctime)s] %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)
        
        # Adiciona handlers ao logger
        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)
        
        self.debug("Logger initialized")
    
    def debug(self, message):
        """Registra uma mensagem de debug.
        
        Args:
            message: Mensagem a ser registrada
        """
        self.logger.debug(message)
    
    def info(self, message):
        """Registra uma mensagem informativa.
        
        Args:
            message: Mensagem a ser registrada
        """
        self.logger.info(message)
    
    def warning(self, message):
        """Registra uma mensagem de aviso.
        
        Args:
            message: Mensagem a ser registrada
        """
        self.logger.warning(message)
    
    def error(self, message):
        """Registra uma mensagem de erro.
        
        Args:
            message: Mensagem a ser registrada
        """
        self.logger.error(message)
    
    def critical(self, message):
        """Registra uma mensagem crítica.
        
        Args:
            message: Mensagem a ser registrada
        """
        self.logger.critical(message)