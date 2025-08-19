import random
import sys
import pygame.display

from pygame import Surface, Rect
from pygame.font import Font
from code.Background import Background
from code.Const import LEVEL_SOUND, C_WHITE, WIN_HEIGHT, FONT_TYPE, MENU_OPTION, EVENT_ENEMY, \
    C_GREEN, EVENT_TIMEOUT, TIMEOUT_STEP, TIMEOUT_LEVEL1, TIMEOUT_LEVEL2, BOSS_SOUND
from code.Enemy import Enemy
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.EntityMediator import EntityMediator
from code.Explosion import Explosion
from code.Player import Player
from code.Boss import Boss
from code.Logger import Logger


# Classe que gerencia o nível do jogo
class Level:
    def __init__(self, window: Surface, name: str, game_mode: str, player_score: list[int]):
        self.logger = Logger()
        self.logger.info(f"Inicializando nível: {name} com modo: {game_mode}")  # log
        
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        
        # Configura o temporizador do nível
        self._setup_timeout()
        
        # Carrega o fundo do nível
        self._load_background()
        
        # Adiciona os jogadores
        self._add_players(player_score)
        
        # Configura os timers do nível
        self._setup_timers()
        
        self.logger.debug(f"Nível {name} inicializado com sucesso")

    # Configura o temporizador do nível
    def _setup_timeout(self):
        if self.name == "Level1":
            self.timeout = TIMEOUT_LEVEL1
        elif self.name == "Level2":
            self.timeout = TIMEOUT_LEVEL2
        else:  # fase 3 do boss, sem temporizador
            self.timeout = 0

    # Carrega o fundo do nível
    def _load_background(self):
        self.entity_list.extend(EntityFactory.get_entity(self.name + 'BG'))

    # Adiciona os jogadores ao nível
    def _add_players(self, player_score: list[int]):
        self.logger.debug(f"Adicionando jogadores ao nível {self.name}")

        # Adiciona jogador 1
        player_list = EntityFactory.get_entity('Ship_Player1')
        player = player_list[0]
        player.score = player_score[0]
        if len(player_score) >= 3 and player_score[2] > 0:
            player.health = player_score[2]
        self.entity_list.extend(player_list)
        self.logger.debug(f"Jogador 1 adicionado com pontuação: {player.score} e saúde: "
                          f"{player.health}")  # log

        # Adiciona jogador 2 se estiver no modo multiplayer
        if self.game_mode in [MENU_OPTION[1], MENU_OPTION[2]]:
            player_list = EntityFactory.get_entity('Ship_Player2')
            player = player_list[0]
            player.score = player_score[1]
            if len(player_score) >= 4 and player_score[3] > 0:
                player.health = player_score[3]
            self.entity_list.extend(player_list)
            self.logger.debug(f"Jogador 2 adicionado com pontuação: {player.score} e saúde: "
                              f"{player.health}")  # log

    # Configura os timers do nível
    def _setup_timers(self):
        if self.name != "Level3":  # Timer só se não for boss
            if self.name == "Level2":
                pygame.time.set_timer(EVENT_ENEMY, 1100)  # aparecem mais inimigos
            else:
                pygame.time.set_timer(EVENT_ENEMY, 2100)

            pygame.time.set_timer(EVENT_TIMEOUT, TIMEOUT_STEP)  # Conf. timer de timeout do nível

        else:
            self.entity_list.extend(EntityFactory.get_entity('Ship_EnemyBoss'))  # Spawn do Boss

    # Configura a música do nível
    def _setup_music(self):
        pygame.mixer.music.stop()
        self.logger.debug(f"Configurando música para o nível {self.name}")  # log

        # Música diferente para a fase do Boss
        if self.name == "Level3":
            pygame.mixer.music.load(BOSS_SOUND)
            pygame.mixer.music.set_volume(1)
            self.logger.debug("Música do Boss carregada")  # log
        else:
            pygame.mixer.music.load(LEVEL_SOUND)
            pygame.mixer.music.set_volume(0.5)
            self.logger.debug("Música padrão de nível carregada")  # log

        pygame.mixer.music.play(-1)

    # Renderiza os fundos do nível
    def _render_backgrounds(self):
        for bg in self.entity_list:
            if isinstance(bg, Background):
                bg.move()
                self.window.blit(bg.surf, bg.rect)

                # Renderiza uma segunda cópia para criar efeito de paralaxe contínuo
                second_rect = bg.rect.copy()
                second_rect.x += bg.image_width
                self.window.blit(bg.surf, second_rect)

    # Processa todas as entidades do nível
    def _process_entities(self):
        for ent in self.entity_list[:]:
            if isinstance(ent, Background):
                continue

            ent.move()

            # Remove explosões finalizadas
            if isinstance(ent, Explosion) and ent.finished:
                self.entity_list.remove(ent)
                continue

            # Processa tiros das entidades
            if isinstance(ent, (Player, Enemy, Boss)):
                shot = ent.shot()
                if shot is not None:
                    if isinstance(shot, list):
                        self.entity_list.extend(shot)
                    else:
                        self.entity_list.append(shot)

            # Remove entidades que saíram da tela
            if ent.rect.right <= 0 and not isinstance(ent, Player):
                self.entity_list.remove(ent)
                continue

            # Exibe informações dos jogadores
            if ent.name == 'Ship_Player1':
                self.level_text(14, f'Player1 - Health: {ent.health} | Score: {ent.score}',
                                C_GREEN, (10, 30))
            if ent.name == 'Ship_Player2':
                self.level_text(14, f'Player2 - Health: {ent.health} | Score: {ent.score}',
                                C_GREEN, (10, 45))

            # Renderiza a entidade
            self.window.blit(ent.surf, ent.rect)

    # Processa os eventos do jogo
    def _handle_events(self, player_score: list[int]):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.logger.info("Evento de saída detectado")  # log
                pygame.quit()
                sys.exit()

            if event.type == EVENT_ENEMY and self.name != "Level3":
                choice = random.choice(('Ship_Enemy1', 'Ship_Enemy1', 'Ship_Enemy2'))
                self.logger.debug(f"Criando inimigo do tipo {choice}")  # log
                self.entity_list.extend(EntityFactory.get_entity(choice))

            if event.type == EVENT_TIMEOUT and self.name != "Level3":
                self.timeout -= TIMEOUT_STEP
                if self.timeout <= 0:
                    self.logger.info(f"Tempo esgotado no nível {self.name}")  # log
                    self._save_player_data(player_score)
                    return True

    # Verifica o estado atual do jogo
    def _check_game_state(self, player_score: list[int]):

        # Verifica se jogadores morreram
        found_player = False
        for ent in self.entity_list:
            if isinstance(ent, Player):
                found_player = True
                break
        if not found_player:
            self.logger.info("Todos os jogadores foram derrotados")  # log
            self._save_player_data(player_score)
            return "game_over"

        # Verifica vitória na fase do Boss
        if self.name == "Level3":
            boss_alive = any(isinstance(ent, Boss) for ent in self.entity_list)
            if not boss_alive:
                self.logger.info("Boss derrotado! Vitória alcançada")  # log
                self._save_player_data(player_score)
                return "victory"
                
        return None

    # Executa o nível do jogo
    def run(self, player_score: list[int]):

        # Configura a música do nível
        self._setup_music()
        self.logger.info(f"Iniciando execução do nível {self.name}")  # log

        clock = pygame.time.Clock()

        while True:
            self.window.fill((0, 0, 0))

            # Renderiza fundos
            self._render_backgrounds()

            # Processa e renderiza entidades
            self._process_entities()

            # Processa eventos
            event_result = self._handle_events(player_score)
            if event_result is not None:
                self.logger.info(f"Nível {self.name} finalizado com resultado: {event_result}")  # log
                return event_result

            # Verifica estado do jogo
            game_state = self._check_game_state(player_score)
            if game_state is not None:
                self.logger.info(f"Nível {self.name} finalizado com resultado: {game_state}")  # log
                return game_state

            # Renderiza HUD
            self._render_hud(clock)

            # Processa colisões
            self._process_collisions()

            # Atualiza a tela
            pygame.display.update()
            clock.tick(60)

    # Renderiza a interface do usuário
    def _render_hud(self, clock):

        # Exibe informações de tempo restante (exceto na fase do boss)
        if self.name != "Level3":
            self.level_text(14, f'{self.name} - Timeout: {self.timeout / 1000:.1f}s',
                            C_WHITE, (10, 5))
        # Exibe FPS
        self.level_text(14, f'fps: {clock.get_fps():.0f}', C_WHITE, (10, WIN_HEIGHT - 20))

    # Processa as colisões entre entidades
    def _process_collisions(self):
        EntityMediator.verify_collision(entity_list=self.entity_list)
        EntityMediator.verify_healthy(entity_list=self.entity_list)

    # Salva score e vida atual no player_score para manter entre fases
    def _save_player_data(self, player_score: list[int]):
        self.logger.debug("Salvando dados dos jogadores")  # log
        for ent in self.entity_list:
            if isinstance(ent, Player) and ent.name == 'Ship_Player1':
                player_score[0] = ent.score
                if len(player_score) < 3:
                    player_score.append(ent.health)
                else:
                    player_score[2] = ent.health
                self.logger.debug(f"Dados do Jogador 1 salvos: score={ent.score}, "
                                  f"health={ent.health}")  # log

            if isinstance(ent, Player) and ent.name == 'Ship_Player2':
                player_score[1] = ent.score
                if len(player_score) < 4:
                    player_score.append(ent.health)
                else:
                    player_score[3] = ent.health
                self.logger.debug(f"Dados do Jogador 2 salvos: score={ent.score}, "
                                  f"health={ent.health}")  # log

    # Renderiza texto na tela
    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name=FONT_TYPE, size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
