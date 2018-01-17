import media
import fresh_tomatoes

coco = media.Movie("Coco",
                    "A story about a boy and his music dream",
                    "http://i.imgur.com/F4t6UVt.jpg",
                    "https://youtu.be/zNCz4mQzfEI",
                    "2017",
                    "1h 49m")

cars_3 = media.Movie("Cars 3",
                     "Blindsided by a new generation of blazing-fast racers, the legendary Lightning McQueen (voice of Owen Wilson) is suddenly pushed out of the sport he loves.",
                     "https://static1.squarespace.com/static/51cdafc4e4b09eb676a64e68/586d6d92b3db2bba412289c7/58b754eff5e2315a529122fd/1506962324105/c3_teaser_poster.jpg",
                     "https://youtu.be/U1eQYk74R1g",
                     "2017",
                     "1h 49m")

piper = media.Movie("Piper",
                    "\"Piper\" tells the story of a hungry sandpiper hatchling who ventures from her nest for the first time to dig for food by the shoreline.",
                    "https://static1.squarespace.com/static/51cdafc4e4b09eb676a64e68/t/579672f75016e1dd93181c7d/1469477641613",
                    "https://youtu.be/Cn5l7HJaYuA",
                    "2016",
                    "0h 6m")

wall_e = media.Movie("Wall-E",
                     "After hundreds of years doing what he was built for, WALL-E discovers a new purpose in life when he meets a sleek search robot named EVE. ",
                     "https://static1.squarespace.com/static/51cdafc4e4b09eb676a64e68/586d6d92b3db2bba412289c7/586d6d92b3db2bba412289cf/1483567757903/09_walle.jpg",
                     "https://youtu.be/5O9ikywnW6M",
                     "2008",
                     "1h 38m")

up = media.Movie("Up",
                 "A 78-year-old curmudgeonly balloon salesman, is not your average hero. ",
                 "https://static1.squarespace.com/static/51cdafc4e4b09eb676a64e68/586d6d92b3db2bba412289c7/586d6d92b3db2bba412289d1/1483567713911/10_up.jpg",
                 "https://youtu.be/vWapgqedDBM",
                 "2009",
                 "1h 36m")

the_blue_umbrella = media.Movie("The Blue Umbrella",
                                "It is just another evening commute until the rain starts to fall, and the city comes alive to the sound of dripping rain pipes, whistling awnings and gurgling gutters.",
                                "https://static1.squarespace.com/static/51cdafc4e4b09eb676a64e68/57dc2232e6f2e1bd882b46e3/57dc22325016e1d637108f8f/1474050169236/blue_umbrella.jpg",
                                "https://youtu.be/3wY7KQmPYlo",
                                "2013",
                                "0h 7m")

movies = [coco,cars_3,piper,wall_e,up,the_blue_umbrella]
fresh_tomatoes.open_movies_page(movies)
