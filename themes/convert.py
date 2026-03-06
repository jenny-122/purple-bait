#!/usr/bin/env python3
import yaml
import sys
from pathlib import Path


def hex_to_rgb(hex_color):
    """Convert hex color to RGB values (0-1 range for plist)"""
    hex_color = hex_color.lstrip("#")
    r = int(hex_color[0:2], 16) / 255.0
    g = int(hex_color[2:4], 16) / 255.0
    b = int(hex_color[4:6], 16) / 255.0
    return r, g, b


def create_color_xml(hex_color):
    """Create color XML for Terminal.app"""
    r, g, b = hex_to_rgb(hex_color)
    return f"""	<dict>
		<key>Color Space</key>
		<string>sRGB</string>
		<key>Blue Component</key>
		<real>{b}</real>
		<key>Green Component</key>
		<real>{g}</real>
		<key>Red Component</key>
		<real>{r}</real>
	</dict>"""


def yaml_to_terminal(yaml_file, output_file=None):
    """Convert YAML theme to .terminal file"""

    # Read YAML file
    with open(yaml_file, "r") as f:
        theme = yaml.safe_load(f)

    # Map YAML color names to Terminal.app plist keys
    color_mapping = {
        "color_01": "ANSIBlackColor",
        "color_02": "ANSIRedColor",
        "color_03": "ANSIGreenColor",
        "color_04": "ANSIYellowColor",
        "color_05": "ANSIBlueColor",
        "color_06": "ANSIMagentaColor",
        "color_07": "ANSICyanColor",
        "color_08": "ANSIWhiteColor",
        "color_09": "ANSIBrightBlackColor",
        "color_10": "ANSIBrightRedColor",
        "color_11": "ANSIBrightGreenColor",
        "color_12": "ANSIBrightYellowColor",
        "color_13": "ANSIBrightBlueColor",
        "color_14": "ANSIBrightMagentaColor",
        "color_15": "ANSIBrightCyanColor",
        "color_16": "ANSIBrightWhiteColor",
        "background": "BackgroundColor",
        "foreground": "TextColor",
        "cursor": "CursorColor",
    }

    # Start building the XML
    xml_content = """<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
"""

    # Add colors
    for yaml_key, terminal_key in color_mapping.items():
        if yaml_key in theme:
            xml_content += f"""	<key>{terminal_key}</key>
{create_color_xml(theme[yaml_key])}
"""

    # Add the profile name and type
    profile_name = theme.get("name", "Custom Theme")
    xml_content += f"""	<key>ProfileCurrentVersion</key>
	<real>2.04</real>
	<key>name</key>
	<string>{profile_name}</string>
	<key>type</key>
	<string>Window Settings</string>
</dict>
</plist>"""

    # Set output filename
    if output_file is None:
        output_file = Path(yaml_file).stem + ".terminal"

    # Write the file
    with open(output_file, "w") as f:
        f.write(xml_content)

    print(f"✅ Converted {yaml_file} to {output_file}")
    return output_file


# Main execution
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python yaml_to_terminal.py <theme.yml>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None

    yaml_to_terminal(input_file, output_file)
