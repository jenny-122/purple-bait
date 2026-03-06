import yaml
import os
import sys


def yaml_to_wezterm_toml(yaml_file):
    with open(yaml_file, "r") as f:
        theme = yaml.safe_load(f)

    name = theme.get("name", "Unknown")
    author = theme.get("author", "")

    toml = f'''[metadata]
name = "{name}"
author = "{author}"

[colors]
foreground = "{theme.get("foreground", "#ffffff")}"
background = "{theme.get("background", "#000000")}"
cursor_bg = "{theme.get("cursor", "#ffffff")}"
cursor_fg = "{theme.get("background", "#000000")}"
cursor_border = "{theme.get("cursor", "#ffffff")}"

ansi = [
    "{theme.get("color_01", "#000000")}",  # black
    "{theme.get("color_02", "#ff0000")}",  # red
    "{theme.get("color_03", "#00ff00")}",  # green
    "{theme.get("color_04", "#ffff00")}",  # yellow
    "{theme.get("color_05", "#0000ff")}",  # blue
    "{theme.get("color_06", "#ff00ff")}",  # magenta
    "{theme.get("color_07", "#00ffff")}",  # cyan
    "{theme.get("color_08", "#ffffff")}",  # white
]

brights = [
    "{theme.get("color_09", "#808080")}",  # bright black
    "{theme.get("color_10", "#ff8080")}",  # bright red
    "{theme.get("color_11", "#80ff80")}",  # bright green
    "{theme.get("color_12", "#ffff80")}",  # bright yellow
    "{theme.get("color_13", "#8080ff")}",  # bright blue
    "{theme.get("color_14", "#ff80ff")}",  # bright magenta
    "{theme.get("color_15", "#80ffff")}",  # bright cyan
    "{theme.get("color_16", "#ffffff")}",  # bright white
]
'''

    # Create output filename
    output_name = name.lower().replace(" ", "_").replace("'", "") + ".toml"
    output_path = os.path.expanduser(f"~/.config/wezterm/colors/{output_name}")

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        f.write(toml)

    print(f"Created: {output_path}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python convert_themes.py theme.yml [theme2.yml ...]")
        sys.exit(1)

    for yaml_file in sys.argv[1:]:
        if os.path.exists(yaml_file):
            yaml_to_wezterm_toml(yaml_file)
        else:
            print(f"File not found: {yaml_file}")
