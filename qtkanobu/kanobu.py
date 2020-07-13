def main():

    import random

    while True:

        print(locale["bot"]["choice"] + ".", end="")

        bot = random.randint(0, 2)

        massive = [
            [2, 0, 1],
            [1, 2, 0],
            [0, 1, 2]
        ]

        i = 0
        for key in massive[player]:
            a = "" if locale["lang"]["case"] is False else locale["lang"]["case"][bot]

            object = locale["objects"][bot]
            object = object if locale["lang"]["case"] is False else object.lower()

            if bot == i:

                if i == 0:
                    message = yellow(" " + locale["results"][key] + "!")

                if i == 1:
                    message = green(" " + locale["results"][key] + "!")

                if i == 2:
                    message = red(" " + locale["results"][key] + "!")

                print(message + " " + locale["bot"]["have"] + a + " " + object)

            i += 1
