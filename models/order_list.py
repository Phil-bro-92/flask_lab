from models.order import *

game1 = Order(
    1,
    "Phil",
    "01-01-2022",
    2,
    "God of War",
    "Action/Adventure",
    "God of War[b] is 2018 action-adventure game developed by Santa Monica Studio and published by Sony Interactive Entertainment.",
)
game2 = Order(
    2,
    "Sarah",
    "02-03-2021",
    1,
    "The Last of Us",
    "Horror/Action",
    "The Last of Us is a 2013 action-adventure game developed by Naughty Dog and published by Sony Computer Entertainment.",
)

game3 = Order(
    3,
    "Dave",
    "07-09-2019",
    3,
    "Metal Gear Solid",
    "Stealth/Action",
    "Metal Gear Solid[c] is a stealth game developed by Konami and released for the PlayStation in 1998.",
)
games = [game1, game2, game3]
