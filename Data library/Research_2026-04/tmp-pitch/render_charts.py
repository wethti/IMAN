"""Pre-render charts as PNGs so the deck uses high-quality editorial graphics,
not pptx's native chart renderer."""
import os
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib import rcParams

OUT = os.path.dirname(os.path.abspath(__file__))

# Match Research Progress palette
BG = "#F4F7F1"
INK = "#1A1A1A"
GREEN_DARK = "#1A3A1A"
GREEN_MID = "#2D5A1B"
LIME = "#7FBA00"
MUTED = "#5A6B5A"
GRID = "#C8D2C6"
GRAY = "#9AA19B"
AMBER = "#E4B25A"
TERRACOTTA = "#B85042"

rcParams["font.family"] = "Calibri"
rcParams["axes.spines.top"] = False
rcParams["axes.spines.right"] = False


def save(fig, name, dpi=220):
    p = os.path.join(OUT, name)
    fig.savefig(p, dpi=dpi, bbox_inches="tight", facecolor=BG, edgecolor="none")
    plt.close(fig)
    print("wrote", p)


# ---- Chart 1: variance decomposition bar ----
def chart_variance():
    fig, ax = plt.subplots(figsize=(5.6, 3.4))
    fig.patch.set_facecolor(BG)
    ax.set_facecolor(BG)
    labels = ["Measurement\nnoise", "Individual\nbehavior", "Healthcare\naccess",
              "Income &\neducation", "Structural /\nplace residual"]
    vals = [5, 10, 15, 22, 48]
    colors = [GRAY] * 4 + [GREEN_MID]
    bars = ax.barh(labels, vals, color=colors, edgecolor="none", height=0.62)
    ax.set_xlim(0, 62)
    ax.set_xticks([0, 10, 20, 30, 40, 50])
    ax.tick_params(colors=MUTED, labelsize=10)
    ax.spines["bottom"].set_color(GRID)
    ax.spines["left"].set_color(GRID)
    ax.grid(axis="x", color=GRID, linewidth=0.5, alpha=0.6)
    ax.set_axisbelow(True)
    for i, (bar, v) in enumerate(zip(bars, vals)):
        w = bar.get_width()
        ax.text(w + 1.2, bar.get_y() + bar.get_height() / 2,
                f"{v}%", va="center", ha="left",
                fontsize=11, fontweight="bold", color=GREEN_DARK if i == 4 else MUTED)
    ax.set_xlabel("Share of variance (%)", color=MUTED, fontsize=10)
    save(fig, "chart_variance.png")


# ---- Chart 2: positive deviant scatter ----
def chart_scatter():
    fig, ax = plt.subplots(figsize=(5.0, 3.5))
    fig.patch.set_facecolor(BG)
    ax.set_facecolor(BG)
    typical = [(12, 82), (18, 80), (25, 76), (28, 73), (32, 70),
               (35, 68), (40, 66), (45, 64), (50, 62), (55, 60), (60, 58)]
    deviants = [("Little Village", 28, 82), ("East Boston", 25, 81),
                ("Sunset Park", 30, 80), ("Mott Haven", 42, 79),
                ("Chinatown", 20, 83)]
    # Per-label annotation offsets (points) to avoid overlap with neighbouring dots
    label_offsets = {
        "Chinatown":    (-8, 10),
        "East Boston":  (-50, 4),
        "Little Village": (8, 6),
        "Sunset Park":  (8, -12),
        "Mott Haven":   (8, 4),
    }
    eng = (43, 67.7)

    # Fit a trend line to typical
    import numpy as np
    xs = np.array([p[0] for p in typical])
    ys = np.array([p[1] for p in typical])
    m, b = np.polyfit(xs, ys, 1)
    xl = np.array([5, 65])
    ax.plot(xl, m * xl + b, color=MUTED, linewidth=1.3, linestyle="--",
            alpha=0.75, label="Trend (typical tracts)")

    ax.scatter(xs, ys, s=58, color=GRAY, edgecolor="none", label="Typical U.S. tract", zorder=3)
    ax.scatter([d[1] for d in deviants], [d[2] for d in deviants], s=90,
               color=AMBER, edgecolor="none", label="Positive deviant", zorder=4)
    # Label deviants
    for name, x, y in deviants:
        dx, dy = label_offsets.get(name, (6, 4))
        ax.annotate(name, (x, y), xytext=(dx, dy), textcoords="offset points",
                    fontsize=8.5, color=GREEN_DARK, fontweight="bold")
    ax.scatter([eng[0]], [eng[1]], s=110, color=TERRACOTTA, edgecolor="none",
               label="Englewood", zorder=5)
    ax.annotate("Englewood", (eng[0], eng[1]), xytext=(8, -10),
                textcoords="offset points", fontsize=9, color=TERRACOTTA,
                fontweight="bold")

    ax.set_xlim(5, 65)
    ax.set_ylim(55, 90)
    ax.set_xlabel("Poverty rate (%)", color=MUTED, fontsize=10)
    ax.set_ylabel("Life expectancy (years)", color=MUTED, fontsize=10)
    ax.tick_params(colors=MUTED, labelsize=9)
    ax.spines["bottom"].set_color(GRID)
    ax.spines["left"].set_color(GRID)
    ax.grid(True, color=GRID, linewidth=0.5, alpha=0.55)
    ax.set_axisbelow(True)
    leg = ax.legend(loc="upper right", frameon=False, fontsize=8.5,
                    labelcolor=MUTED)
    save(fig, "chart_scatter.png")


# ---- Chart 3: stacked LE gains ----
def chart_stacked_le():
    fig, ax = plt.subplots(figsize=(5.4, 3.6))
    fig.patch.set_facecolor(BG)
    ax.set_facecolor(BG)
    programs = [
        ("Health Center / FQHC expansion", 1.5),
        ("Green ReEntry housing + workforce", 2.0),
        ("Medicaid coverage stability", 1.1),
        ("Violence interruption (Cure/READI)", 0.7),
        ("Barbershop BP + meds management", 0.8),
        ("Fresh Market + clinical pairing", 0.5),
        ("Green infrastructure / PM2.5", 0.4),
    ]
    names = [p[0] for p in programs]
    gains = [p[1] for p in programs]
    left = 0
    cmap = [GREEN_DARK, GREEN_MID, "#3A7A2A", "#4F8D3A", "#65A04B", "#7BB45E", LIME]
    for i, (n, g) in enumerate(programs):
        ax.barh([0], [g], left=left, color=cmap[i], edgecolor="white",
                linewidth=1.2, height=0.55, label=f"{n} (+{g} yr)")
        if g >= 0.9:
            # Label inside bar
            ax.text(left + g / 2, 0, f"+{g}", ha="center", va="center",
                    color="white", fontweight="bold", fontsize=10)
        else:
            # Label above bar, rotated
            ax.text(left + g / 2, 0.40, f"+{g}", ha="center", va="bottom",
                    color=GREEN_DARK, fontweight="bold", fontsize=9)
            ax.plot([left + g / 2, left + g / 2], [0.28, 0.38],
                    color=GREEN_DARK, linewidth=0.7)
        left += g
    # Total marker
    ax.text(left + 0.3, 0, f"= {left:.1f} yrs\ngross", va="center",
            ha="left", color=GREEN_DARK, fontweight="bold", fontsize=11)
    ax.set_xlim(0, left + 2)
    ax.set_ylim(-0.55, 0.55)
    ax.set_yticks([])
    ax.set_xticks([0, 1, 2, 3, 4, 5, 6, 7])
    ax.tick_params(colors=MUTED, labelsize=9)
    ax.spines["bottom"].set_color(GRID)
    ax.spines["left"].set_visible(False)
    ax.set_xlabel("Life-expectancy gain (years) in target population, at full dose",
                  color=MUTED, fontsize=9.5)
    ax.grid(axis="x", color=GRID, linewidth=0.5, alpha=0.5)
    ax.set_axisbelow(True)
    # Legend below, 2 columns
    handles = [mpatches.Patch(color=cmap[i], label=f"{names[i]}  +{gains[i]} yr")
               for i in range(len(programs))]
    ax.legend(handles=handles, loc="upper center", bbox_to_anchor=(0.5, -0.35),
              ncol=2, frameon=False, fontsize=8.5, labelcolor=MUTED)
    save(fig, "chart_stacked.png")


if __name__ == "__main__":
    chart_variance()
    chart_scatter()
    chart_stacked_le()
