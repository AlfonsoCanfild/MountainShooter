import os
import sys

from code.Game import Game
from code.Logger import Logger

# Inicializa o logger (apenas console, sem arquivo de log)
logger = Logger()
logger.info("Iniciando o jogo SkyFighters...")  # log

# Tentativa de tirar os avisos do libpng, movendo stderr para o arquivo nulo
original_stderr = sys.stderr
sys.stderr = open(os.devnull, 'w')

# Inicializa e executa o jogo
try:
    game = Game()
    logger.info("Jogo inicializado com sucesso...")  # log
    game.run()
except Exception as e:
    logger.critical(f"Erro fatal: {str(e)}")  # mensagem de erro, caso haja
    raise
finally:
    sys.stderr.close()  # Restaura o stderr original
    sys.stderr = original_stderr
    logger.info("Encerrando o jogo...")
