import matplotlib.pyplot as plt
import matplotlib.patches as patches


def generate_layout(objects, output_path):

    fig, ax = plt.subplots(figsize=(8, 6))

    ax.set_xlim(0, 1600)
    ax.set_ylim(1200, 0)

    # Room boundary
    room = patches.Rectangle(
        (20, 20),
        1560,
        1160,
        linewidth=2,
        edgecolor="black",
        facecolor="white"
    )

    ax.add_patch(room)

    for obj in objects:

        rect = patches.Rectangle(
            (obj["x"], obj["y"]),
            obj["width"],
            obj["height"],
            linewidth=1,
            edgecolor="blue",
            facecolor="lightblue"
        )

        ax.add_patch(rect)

        ax.text(
            obj["x"] + 5,
            obj["y"] + 15,
            obj["name"],
            fontsize=8
        )

    plt.title("2D Room Layout")

    plt.axis("off")

    plt.savefig(output_path, bbox_inches="tight")

    plt.close()