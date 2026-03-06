import subprocess

# Convert Gooey.yaml to Gooey.toml using yq
with open("Base2Tone Suburb.toml", "w") as f:
    subprocess.run(["yq", "-t", ".", "Base2Tone Suburb.yml"], stdout=f)
