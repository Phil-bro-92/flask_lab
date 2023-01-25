class Order:
    def __init__(self,id, customer_name, order_date, quantity, game_title, genre, description):
        self.id = id
        self.customer_name = customer_name
        self.order_date = order_date
        self.quantity = quantity
        self.game_title = game_title
        self.genre = genre
        self.description = description