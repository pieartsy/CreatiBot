# CreatiBot
A Discord bot that generates random palettes and gets random prompts.

For palette generation, it uses [colormind.io](http://colormind.io/api/)'s API, [thecolorapi.com](https://www.thecolorapi.com/), and [Pillow](https://python-pillow.org/) to create palettes and send them to the channel you've typed the command into.

It also uses [reddit's API](https://www.reddit.com/dev/api) for the random prompts.

* $palette to generate a random palette from colormind.io
* $prompt to get a random prompt (out of the newest 50) from r/writingprompts
* $info to get this info description

## Palette process
1. User types `$palette` into the discord channel.
2. Creatibot gets a color palette from colormind.io. I am using this website because I want aesthetically pleasing palettes rather than literally random colors. This only returns the RGB values, however, and we need to make it into an image!
3. Creatibot asks thecolorapi.com for SVG (vector) images using the RGB values from before. This gives me a color and its name.
4. Creatibot converts the SVG to a .png image using svglib.
5. Creatibot stitches the five .png images together using Pillow, and sends the palette to the channel.

This process takes a few seconds!

## Prompt process
This one's far quicker and simpler. When the user types `$prompt`, all it does is make a list out of the newest 50 writing prompts from [r/writingprompts](https://www.reddit.com/r/WritingPrompts/) and sends one of them to the channel.

