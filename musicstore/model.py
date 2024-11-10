from datetime import datetime

class Transaction:
    SELL: int = 1
    SUPPLY: int = 2
   
    def __init__(self, type: int, copies: int):
        self.type: int = type 
        self.copies: int = copies
        self.date: datetime = datetime.now() 

class Disc:

    def __init__(self, sid: str, title: str, artist: str, sale_price: float, purchase_price: float, quantity: int):
        self.sid: str = sid 
        self.title: str = title
        self.artist: str = artist
        self.sale_price: float = sale_price
        self.purchase_price: float = purchase_price
        self.quantity: int = quantity
        self.transactions: list[Transaction] = []
        self.song_list: list[str] = []

    def add_song(self, song: str):
        self.song_list.append(song)

    def sell(self, copies: int):
        if copies > self.quantity:
            return False 
        else:
            self.quantity = self.quantity - copies #self.quantity -= copies
            self.transactions.append(Transaction(Transaction.SELL, copies))
            return True
        
    def supply(self, copies: int):
        self.quantity += copies 
        self.transactions.append(Transaction(Transaction.SUPPLY, copies))
        return True 
    
    def copies_sold(self) -> int:
        sum = 0
        for item_transation in self.transactions:
            if item_transation.type == Transaction.SELL:
                sum += item_transation.copies
        return sum 
         
    def __str__(self) -> str:
        return(
            f"SID: {self.sid}/n"
            f"Title: {self.title}/n" 
            f"Artist: {self.artist}/n"
            f"Song List: {', '.join(self.song_list)}"
)

class MusicStore:
    def __init__(self):
        self.discs: dict[str, Disc] = {}

    def add_disc(self, sid: str, title: str, artist: str, sale_price: float, purchase_price: float, quantity: int): 
        if sid not in self.discs:
            self.discs[sid] = Disc(sid, title, artist, sale_price, purchase_price, quantity)

    def search_by_sid(self, sid: str) -> Disc | None:
        return self.discs.get(sid)
        