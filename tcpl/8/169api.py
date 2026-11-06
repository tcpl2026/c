"""
API for the cards project
"""
from dataclasses import asdict
from dataclasses import dataclass
from dataclasses import field

from .db import DB

__all__ = [
    "Card",
    "CardsDB",
    "CardsException",
    "MissingSummary",
    "InvalidCardId",
]


@dataclass
class Card:
    summary: str = None
    owner: str = None
    state: str = "todo"
    id: int = field(default=None, compare=False)

    @classmethod
    def from_dict(cls, d):
        return Card(**d)
    def to_dict(self):
        return asdict(self)


class CardsException(Exception):
    pass


class MissingSummary(CardsException):
    pass


class InvalidCardId(CardsException):
    pass


class CardsDB:
    def __init__(self, db_path):
        self._db_path = db_path
        self._db = DB(db_path, ".cards_db")

    def add_card(self, card: Card) -> int:
        """Add a card, return the id of card."""
        if not card.summary:
            raise MissingSummary
        if card.owner is None:
            card.owner = ""
        id = self._db.create(card.to_dict())
        self._db.update(id, {"id": id})
        return id

    def get_card(self, card_id: int) -> Card:
        """Return a card with a matching id."""
        db_item = self._db.read(card_id)
        if db_item is not None:
            return Card.from_dict(db_item)
        else:
            raise InvalidCardId(card_id)

    def list_cards(self, owner=None, state=None):
        """Return a list of cards."""
        all = self._db.read_all()
        if (owner is not None) and (state is not None):
            return [
                Card.from_dict(t)
                for t in all
                if (t["owner"] == owner and t["state"] == state)
            ]
        elif owner is not None:
            return [
                Card.from_dict(t) for t in all if t["owner"] == owner
            ]
        elif state is not None:
            return [
                Card.from_dict(t) for t in all if t["state"] == state
            ]
        else:
            return [Card.from_dict(t) for t in all]

    def count(self) -> int:
        """Return the number of cards in db."""
        return self._db.count()

    def update_card(self, card_id: int, card_mods: Card) -> None:
        """Update a card with modifications."""
        try:
            self._db.update(card_id, card_mods.to_dict())
        except KeyError as exc:
            raise InvalidCardId(card_id) from exc

    def start(self, card_id: int):
        """Set a card state to 'in prog'."""
        self.update_card(card_id, Card(state="in prog"))

    def finish(self, card_id: int):
        """Set a card state to 'done'."""
        self.update_card(card_id, Card(state="done"))

    def delete_card(self, card_id: int) -> None:
        """Remove a card from db with given card_id."""
        try:
            self._db.delete(card_id)
        except KeyError as exc:
            raise InvalidCardId(card_id) from exc

    def delete_all(self) -> None:
        """Remove all cards from db."""
        self._db.delete_all()

    def close(self):
        self._db.close()

    def path(self):
        return self._db_path

The UNIX System Interface

The UNIX operating system provides its services through a set of system calls, 
which are in effect functions within the operating system that may be called by user programs. 
This chapter describes how to use some of the most important system calls from C programs. 
If you use UNIX, this should be directly helpful, for it is sometimes necessary to employ system calls for maximum efficiency, 
or to access some facility that is not in the library. 
Even if you use C on a different operating system, however, 
you should be able to glean insight into C programming from studying these examples; 
although details vary, similar code will be found on any system. 
Since the ANSI C library is in many cases modeled on UNIX facilities, this code may help your understanding of the library as well.

The chapter is divided into three major parts: input/output, file system, and storage allocation. 
The first two parts assume a modest familiarity with the external characteristics of UNIX systems.

Chapter 7 was concerned with an input/output interface that is uniform across operating systems. 
On any particular system the routines of the standard library have to be written in terms of the facilities provided by the host system. 
In the next few sections we will describe the UNIX system calls for input and output, and show how parts of the standard library can be implemented with them.

File Descriptors

In the UNIX operating system, all input and output is done by reading or writing files, 
because all peripheral devices, even keyboard and screen, are files in the file system. 
This means that a single homogeneous interface handles all communication between a program and peripheral devices.

In the most general case, before you read or write a file, you must inform the system of your intent to do so, 
a process called opening the file. 
If you are going to write on a file it may also be necessary to create it or to discard its previous contents. 
The system checks your right to do so (Does the file exist? Do
