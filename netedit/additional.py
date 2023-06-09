import random
import os

from settings import get_options


def generate_tllogic1():
    """
    Generate a random traffic light logic for the given scenario
    """
    options = get_options()
    name = options.filename
    random.seed(int(options.seed))
    red_duration = [20, 45]
    green_duration = [20, 45]

    edges = []
    with open("data/nod.tmp", "r") as f:
        edges = f.read().strip().split(" ")
    os.remove("data/nod.tmp")

    with open(f"data/{name}.add.xml", "w") as f:
        f.write("""<additional>\n""")
        for edge in edges:
            phases = [
                f"""\
                    \t\t<phase \
                    duration="{random.randrange(*green_duration)}" state="G" \
                    /> \
                """,
                f"""\
                    \t\t<phase \
                    duration="{random.randrange(*red_duration)}" state="r" \
                    /> \
                """,
            ]
            random.shuffle(phases)
            f.write(
                f""" \
                    \t<tlLogic id="{edge}" type="static" \
                    programID="tl{edge}" offset="0">\n \
                """
            )
            f.write("\n".join(phases))
            f.write("""\n\t</tlLogic>\n""")

        f.write("""</additional>""")
