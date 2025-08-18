import pygame
from enum import Enum, auto


class GameStateType(Enum):
    """Todos os possíveis estados do jogo, foi criado para facilitar o gerenciamento"""
    MENU = auto()
    PLAYING = auto()
    GAME_OVER = auto()
    VICTORY = auto()
    SCORE = auto()
    TRANSITION = auto()
    QUIT = auto()


class GameState:
    """Classe responsável por gerenciar os estados do jogo."""
    
    def __init__(self):
        """Inicializa o estado do jogo."""
        self.current_state = GameStateType.MENU
        self.previous_state = None
        self.level_name = None
        self.game_mode = None
        self.player_score = [0, 0, 0, 0]  # [score_p1, score_p2, health_p1, health_p2]
        self.transition_image = None
        self.transition_delay = 0
        
    def change_state(self, new_state, **kwargs):
        """Altera o estado atual do jogo.
        
        Args:
            new_state: Novo estado do jogo (GameStateType)
            **kwargs: Parâmetros adicionais específicos do estado
        """
        self.previous_state = self.current_state
        self.current_state = new_state
        
        # Processa parâmetros específicos do estado
        if 'level_name' in kwargs:
            self.level_name = kwargs['level_name']
            
        if 'game_mode' in kwargs:
            self.game_mode = kwargs['game_mode']
            
        if 'player_score' in kwargs:
            self.player_score = kwargs['player_score']
            
        if 'transition_image' in kwargs:
            self.transition_image = kwargs['transition_image']
            
        if 'transition_delay' in kwargs:
            self.transition_delay = kwargs['transition_delay']
            
    def reset_game(self):
        """Reinicia os dados do jogo para um novo jogo, zera os dados do jogador"""
        self.player_score = [0, 0, 0, 0]
        self.level_name = None
        
    def is_state(self, state_type):
        """Verifica se o estado atual é do tipo especificado.
        
        Args:
            state_type: Tipo de estado a verificar (GameStateType)
            
        Returns:
            bool: True se o estado atual for do tipo especificado
        """
        return self.current_state == state_type