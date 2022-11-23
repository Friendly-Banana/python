#!/usr/bin/python3

from random import choices


class Tree:
    """
    height = 5
		 /\
		/  \
	   / *  \
	  / o   o\
	 /     i  \
	/___    ___\
		|__|
    """

    def __init__(self, height, deco_percent=0.2):
        self.height = height
        self.deco_percent = deco_percent

    def draw(self):
        f = self.height
        s = ""
        # star on top
        #s += " " * f + "*\n"
        for i in range(f, 0, -1):
            s += " " * i + "/"
            s += "".join(
                choices(
                    " io°*",
                    [
                        1 - self.deco_percent,
                        self.deco_percent / 4,
                        self.deco_percent / 4,
                        self.deco_percent / 4,
                        self.deco_percent / 4,
                    ],
                    k=2 * (f - i),
                )
            )
            s += "\\\n"

        s += "/" + "_" * (f - 2) + " " * 4 + "_" * (f - 2) + "\\\n"
        s += " " * (f - 1) + "|__|" + "\n"
        print(s)


def save(s):
    with open("tree.txt", "at") as f:
        f.write(s)


if __name__ == "__main__":
    Tree(5).draw()
