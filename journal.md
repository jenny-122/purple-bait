# wezterm journal

stuff i've figured out, things i keep forgetting, and notes to future me.

---

## theme tweaking

so catppuccin is great but the yellow is so harsh. i spent a while messing with replacements — the yellow slots are `ansi[4]` and `brights[4]` in the color scheme. here's what i tried:

| color    | hex       | vibe            |
|----------|-----------|-----------------|
| teal     | `#94e2d5` | cool cyan-green |
| lavender | `#b7bdf8` | soft purple     |
| mauve    | `#cba6f7` | stronger purple |
| green    | `#a6e3a1` | green           |
| blue     | `#89b4fa` | blue            |

teal on mocha and lavender on macchiato felt the best. mauve is nice too if you want something stronger.

to cycle through themes: `alt + shift + A`. i always forget this one.

---

## keybindings i keep forgetting

i set up vim-style pane navigation with cmd but i literally forget my own bindings all the time lol

### panes
- `cmd + ]` — split right
- `cmd + [` — split down
- `cmd + d` — close pane
- `cmd + f` — toggle zoom (i disabled the mac default for this)
- `cmd + h/j/k/l` — navigate between panes
- `cmd + shift + H/J/K/L` — resize panes

### other stuff
- `alt + shift + A` — cycle theme (the one i always forget)
- `alt + v` — copy mode / visual select
- `alt + u` — clear search pattern

i also disabled a bunch of mac defaults (`cmd + m` for minimize, `cmd + h` for hide, etc) bc they kept getting in the way of my bindings.

---

## vim tips

### visual block mode

i forget this flow every single time and have to look it up:

1. `ctrl + v` to enter visual block mode
2. highlight where you want it to go
3. `shift + i`
4. type what you want to duplicate
5. hit `escape` — and it applies to all the selected lines

