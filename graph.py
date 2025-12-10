import numpy as np
import matplotlib.pyplot as plt

def draw_example():
    x = np.linspace(0, 10, 300)
    y1 = np.sin(x)
    y2 = 0.5 * np.cos(x)
    y3 = 0.3 * np.sin(2 * x)

    fig, axs = plt.subplots(2, 2, figsize=(10, 6))
    axs = axs.ravel()

    # Line plot
    axs[0].plot(x, y1, label="sin(x)", color="tab:blue")
    axs[0].plot(x, y2, label="0.5·cos(x)", linestyle="--", color="tab:orange")
    axs[0].plot(x, y3, label="0.3·sin(2x)", linestyle=":", color="tab:green")
    axs[0].set_title("Line plot")
    axs[0].legend()
    axs[0].grid(True)

    # Scatter plot
    rng = np.random.default_rng(1)
    xs = rng.uniform(0, 10, 120)
    ys = np.sin(xs) + rng.normal(0, 0.2, xs.size)
    sc = axs[1].scatter(xs, ys, c=ys, cmap="viridis", s=40, edgecolors="k")
    axs[1].set_title("Scatter plot")
    fig.colorbar(sc, ax=axs[1], shrink=0.8)

    # Bar chart
    cats = ["A", "B", "C", "D", "E"]
    vals = [5, 3, 6, 2, 4]
    axs[2].bar(cats, vals, color="tab:purple")
    axs[2].set_title("Bar chart")
    axs[2].set_ylabel("Value")

    # Histogram
    data = rng.normal(loc=0.0, scale=1.0, size=1000)
    axs[3].hist(data, bins=30, color="tab:cyan", edgecolor="black")
    axs[3].set_title("Histogram")

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    draw_example()