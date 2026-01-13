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
        print(">>>> Game started")
        self._createDeck()
        self._shuffleDeck()
        self._setTableCard()
        self.game = True
        self._onGameStart(self.tableCard)

    def _stopGame(self):
        self._onGameEnd()
        print(">>>> Game stopped")

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
        print(f" >>> Deck created: {len(self.deck)} cards")

    def _setTableCard(self):
        self.tableCard = self._getCard()
        print(f"  >> New table card: {self.tableCard}")

    # --- Game process ---

    def _shuffleDeck(self):
        for card in self.discard:
            self.deck.append(card)

        random.shuffle(self.deck)
        print(f"  >> Deck shuffled: {len(self.deck)} cards")

    def _getCard(self):
        if len(self.deck) == 0:
            self._shuffleDeck()

        if len(self.deck) > 0:
            card = self.deck[-1]
            self.deck.pop(-1)
            return card

        raise IndexError("Run out of cards :(")

    def _playerTurn(self):
        player = self.players[self.playerTurn]
        self._onPlayerTurn(player)
        print(f" >>> Player turn: {player.id}")

        self.playerTurn = (self.playerTurn + self.turnQueue) % len(self.players)

        # -- Client sending codes

        data = player.recvData(1)
        # print(data)

        match data[0]:
            case codes.PlayerCodes.DRAW_CARD:
                self._drawCard(player)
                print("  >> Player drawed card")

            case codes.PlayerCodes.PLACE_CARDS:
                count = player.recvData(1)[0]
                card_codes = map(int, bytearray(player.recvData(count)))
                print(f"  >> Player placing {count} cards")
                for card_id in card_codes:
                    if card_id < player.canPlaceCount:
                        card = player.hand[card_id]
                        player.hand.pop(card_id)
                        player.canPlaceCount -= 1

                        self._placeCard(card)
                        print(f"   > {card}")

            case _:
                print(f"  >> Invalid code: {data}")

        print(" >>> End of turn")

        # -- Client sent codes

        # For debugging(to prevent infinity loop actually xd)
        if "n" == input("Continue? "):
            return False

        self._onPlayerTurnEnd(player)
        return True

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
            if not self._playerTurn():
                break

        self._stopGame()


def _main():
    game = Game()
    game.start()


if __name__ == "__main__":
    _main()
