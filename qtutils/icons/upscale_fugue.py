import os
from subprocess import check_call

# This is a short script that upscales the fugue icons to 2x resolution using the xbr
# filter, which is designed for pixel art and does a slightly better job than plain
# interpolation, which results in blurrier images. When downscaled with plain
# interpolation, the icons look very similar to the originals, so we just store the
# upscaled versions, and allow Qt to downscale if it wants to.

def upscale_fugue():
    fugue = 'fugue_orig'
    fugue_2x = 'fugue'

    if not os.path.exists(fugue_2x):
        os.mkdir(fugue_2x)
    orig_icons = os.listdir(fugue)
    for i, name in enumerate(orig_icons):
        print('{}/{}'.format(i + 1, len(orig_icons)), name)
        inpath = os.path.join(fugue, name)
        outpath = os.path.join(fugue_2x, name)
        # upscale if not done already
        if not os.path.exists(outpath):
            # check_call(['convert', inpath, '-magnify', outpath])
            # check_call(['pixelscale', inpath, outpath, 'xbr2x'])
            check_call(
                ['convert', inpath, '-filter', 'point', '-resize', '200%', outpath]
            )


if __name__ == '__main__':
    upscale_fugue()