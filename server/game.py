import random

import codes
import setting
from card import Card
from player import Player
from server import Server


class Game(Server):
    def __init__(self):
        super().__init__()
        self.players = []
        self.playerTurn = 0

        self.tableCard = None
        self.deck = []
        self.discard = []

        self.turnQueue = 1  # -1 -- counterclockwise
        self.game = False

    # --- Game init ---

    def _startGame(self):
        self._onGameStart(self.tableCard)
        self._createDeck()
        self._shuffleDeck()
        self._setTableCard()
        self.game = True

    def _stopGame(self):
        self._onGameEnd()

    def _createDeck(self):
        self.deck = [
            Card(color, value)
            for color in codes.CardCodes.COLORS
            for value in (codes.CardCodes.NUMBERS + codes.CardCodes.ACT_CARDS)
            for _ in range(2)
        ]
        self.deck += [
            Card(codes.CardCodes.WILD, value)
            for value in codes.CardCodes.WILD_CARDS
            for _ in range(4)
        ]

    def _setTableCard(self):
        self.tableCard = self._getCard()

    # --- Game process ---

    def _shuffleDeck(self):
        for card in self.discard:
            self.deck.append(card)

        random.shuffle(self.deck)

    def _getCard(self):
        if len(self.deck) == 0:
            self._shuffleDeck()

        if len(self.deck) > 0:
            card = self.deck[-1]
            self.deck.pop(-1)
            return card

        return 0x0F  # Empty card code

    def _playerTurn(self):
        pass

    # --- Player ---

    def _areAllPlayersReady(self):
        return all(player.ready for player in self.players)

    def _drawCard(self, player):
        card = self._getCard()
        player.drawCard(card)
        self._onCardDraw(player)

    def _placeCard(self, card):
        self.tableCard = card

    def _waitForPlayers(self):
        while len(self.players) < setting.MAX_PLAYERS:
            sock = self._waitForPlayer()

            if not sock or sock is None:
                continue

            player = Player(sock, len(self.players))
            if not self._onPlayerJoined(player):
                self._onPlayerLeft(player)
                continue

            self.players.append(player)
            if self._areAllPlayersReady():
                break

        return True

    # --- Main ---

    def start(self):
        if not self._createServer():
            return

        if not self._waitForPlayers():
            return

        self._startGame()

        while self.game:
            self._playerTurn()

        self._stopGame()


def _main():
    game = Game()
    game.start()


if __name__ == "__main__":
    _main()
