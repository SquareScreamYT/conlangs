# --- Color helpers ---
def hex_to_rgb(hex_color):
  hex_color = hex_color.lstrip("#")
  return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def rgb_to_hex(rgb):
  return "#" + "".join(f"{c:02x}" for c in rgb)

def midpoint(c1, c2):
  return tuple((a + b) // 2 for a, b in zip(c1, c2))

def ansi_bg(rgb):
  r, g, b = rgb
  return f"\033[48;2;{r};{g};{b}m"

RESET = "\033[0m"

# --- Representative colors ---
palette = {
  "red":     "#ff8787",
  "orange":  "#ffa94d",
  "yellow":  "#ffd43b",
  "lime":    "#a9e34b",
  "green":   "#69db7c",
  "teal":    "#38d9a9",
  "cyan":    "#3bc9db",
  "blue":    "#4dabf7",
  "indigo":  "#748ffc",
  "violet":  "#9775fa",
  "grape":   "#da77f2",
}

order = [
  "red", "orange", "yellow", "lime", "green",
  "teal", "cyan", "blue", "indigo", "violet",
  "grape", "red"
]
midname = [
  "salmon", "amber", "chartreuse", "emerald", "jade",
  "verdigris", "cerulean", "lapis", "iris", "purple",
  "magenta"
]

# --- Convert to RGB ---
rgb_colors = [(name, hex_to_rgb(palette[name])) for name in order]

print("\nOriginal colors and midpoints:\n")

for i in range(len(rgb_colors) - 1):
  name1, c1 = rgb_colors[i]
  name2, c2 = rgb_colors[i + 1]

  mid = midpoint(c1, c2)

  # Original color
  print(f"{ansi_bg(c1)}  {name1:<7}  {rgb_to_hex(c1)}  {RESET}")

  # Midpoint
  print(f"{ansi_bg(mid)}  {midname[i]} {rgb_to_hex(mid)}  {RESET}")

# Final original (closing the loop)
last_name, last_color = rgb_colors[-1]
print(f"{ansi_bg(last_color)}  {last_name:<7} {rgb_to_hex(last_color)}  {RESET}")
