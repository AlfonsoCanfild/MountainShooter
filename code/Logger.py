import logging


# Classe responsável por gerenciar o sistema de logs do jogo
class Logger:
    _instance = None

    # Implementa o padrão Singleton para garantir uma única instância do logger
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)
            cls._instance._initialize_logger()
        return cls._instance

    # Inicializa o logger com configurações padrão
    def _initialize_logger(self):
        # Configura o logger apenas para console (sem arquivo de log)
        self.logger = logging.getLogger("SkyFighters")
        self.logger.setLevel(logging.DEBUG)

        # Handler para console
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)

        # Formato do log (sem milissegundos, com data/hora personalizada)
        formatter = logging.Formatter(
            '[%(asctime)s] %(levelname)s - %(message)s',
            datefmt='%d-%m-%Y %H:%M'
        )
        console_handler.setFormatter(formatter)

        # Adiciona apenas o handler de console
        self.logger.addHandler(console_handler)

        self.debug("Logger initialized")

    def debug(self, message):  # Registra uma mensagem de debug
        self.logger.debug(message)

    def info(self, message):  # Registra uma mensagem informativa
        self.logger.info(message)

    def warning(self, message):  # Registra uma mensagem de aviso
        self.logger.warning(message)

    def error(self, message):  # Registra uma mensagem de erro
        self.logger.error(message)

    def critical(self, message):  # Registra uma mensagem crítica
        self.logger.critical(message)