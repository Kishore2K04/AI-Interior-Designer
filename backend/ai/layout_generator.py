import matplotlib.pyplot as plt

def generate_layout(objects, output_path):
    plt.figure(figsize=(8,6))

    for obj in objects:
        plt.scatter(obj["x"], obj["y"])
        plt.text(obj["x"], obj["y"], obj["name"])

    plt.gca().invert_yaxis()

    plt.title("Room Layout")

    plt.savefig(output_path)

    plt.close()