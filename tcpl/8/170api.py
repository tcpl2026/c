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

you have permission to access it?), and if all is well, returns to the program a small non-negative integer called a file descriptor. 
Whenever input or output is to be done on the file, the file descriptor is used instead of the name to identify the file. 
(A file descriptor is analogous to the file pointer used by the standard library, or to the file handle of MS-DOS.) 
All information about an open file is maintained by the system; the user program refers to the file only by its file descriptor.

Since input and output involving keyboard and screen is so common, special arrangements exist to make this convenient. 
When the command interpreter (the "shell") runs a program, three files are open, with file descriptors 0, 1, and 2, 
called the standard input, the standard output, and the standard error. 
If a program reads 0 and writes 1 and 2, it can do input and output without worrying about opening files.

The user of a program can redirect I/O to and from files with < and >:

prog <infile >outfile

In this case, the shell changes the default assignments for file descriptors 0 and 1 to the named files. 
Normally file descriptor 2 remains attached to the screen, so error messages can go there. 
Similar observations hold for input or output associated with a pipe. 
In all cases, the file assignments are changed by the shell, not by the program. 
The program does not know where its input comes from nor where its output goes, so long as it uses file 0 for input and 1 and 2 for output.

8.2 Low Level I/O—Read and Write

Input and output uses the read and write system calls, which are accessed from C programs through two functions called read and write. 
For both, the first argument is a file descriptor. 
The second argument is a character array in your program where the data is to go to or come from. 
The third argument is the number of bytes to be transferred.

int n_read = read(int fd, char *buf, int n);

int n_written = write(int fd, char *buf, int n);

Each call returns a count of the number of bytes transferred. 
On reading, the number of bytes returned may be less than the number requested. 
A return value of zero bytes implies end of file, and -1 indicates an error of some sort. 
For writing, the return value is the number of bytes written; an error has occurred if this isn't equal to the number requested.

Any number of bytes can be read or written in one call. 
The most common values are 1, which means one character at a time ("unbuffered"), 
and a number like 1024 or 4096 that corresponds to a physical block size on a peripheral device. 
Larger sizes will be more efficient because fewer system calls
