class ServerCodes:
    """Server sends ServerCodes to players"""

    CONNECTED = 0x00  # PLAYER_ID
    FAILED = 0x01  # FAIL CODE
    """Server sends CONNECTED/FAILED to player when he trying to connect"""

    PLAYER_JOINED = 0x02  # PLAYER_ID
    PLAYER_LEFT = 0x03  # PLAYER_ID
    """Server sends these codes to all players when player left/joined"""

    PLAYER_TURN = 0x04  # PLAYER_ID
    PLAYER_DRAWED = 0x05  # CARD_COUNT
    PLAYER_PLACED = 0x06  # CARD_CODE
    PLAYER_TURN_END = 0x07  # 00
    """Server sends PLAYER_TURN code with <player id>
        Then Player sends his codes to draw/place cards
        Server sends code PLAYER_DRAWED/PLAYER_PLACED to all players
    Server sends PLAYER_TURN_END to all players"""

    FORCE_DRAW = 0x08  # CARD_COUNT
    """Server sends this code to player who needs to card with <card count>
        Next <card count> bytes are card codes which player drawed( or FF if cannot draw and loop ends )"""

    GAME_START = 0x09  # TABLE_CARD_CODE
    GAME_END = 0x0A  # WINNER_ID
    """Server sends these codes at the start/end of game
    GAME_END's second arg is <player id> of winning player"""


class PlayerCodes:
    """Player sends PlayerCodes to server"""

    DRAW_CARD = 0x00
    PLACE_CARDS = 0x01
    """After PLACE_CARDS next byte is <count>, then goes <count> bytes with card ids
    Card id is index of card in player's hand( 0 -- <card count - 1>)"""

    LEAVE_GAME = 0x02
    TOGGLE_READY = 0x03
    """if all players are ready and there are >1 players, game starts
    Game also starts if there are <max players> players"""


class CardCodes:
    """Server sends CardCodes with FORCE_DRAW and PLAYER_PLACED codes"""

    # -- Colors --
    WILD = 0x00
    RED = 0x10
    GREEN = 0x20
    YELLOW = 0x30
    BLUE = 0x40
    # MAGENTA    =    0x50
    # CYAN        =    0x60
    COLORS = [RED, GREEN, YELLOW, BLUE]
    """Wild color only exist in hand for Wild cards,
    you must specify color before placing Wild card"""

    # -- Values --
    # Numbers
    NUMBERS = list(range(0, 10))  # 0 - 9

    # Act
    REVERSE = 0x0A
    BLOCK = 0x0B
    PLUS_2 = 0x0C
    ACT_CARDS = [REVERSE, BLOCK, PLUS_2]

    # Wild
    FORTUNE = 0x0D
    WILD_PLUS_4 = 0x0E
    """ 0x0F is sent if deck is empty """
    ERROR_EMPTY_DECK = 0x0F
    WILD_CARDS = [FORTUNE, WILD_PLUS_4]
