#!/usr/bin/env python3
import pygms
from PIL import Image
import random
import argparse
import io

parser = argparse.ArgumentParser(description='Convert a GMS animation to GIF')
parser.add_argument('--input', default="data.win", help="Source GMS data")
parser.add_argument('--list', action='store_true', help="List GMS sprites")
parser.add_argument('--speed', default=None, help="Override the speed of the animation")
parser.add_argument('--output', help="output file (or directory if all)")
parser.add_argument('--all', help="ALL the animations")
parser.add_argument('--sprite', help="sprite name(must be valid from --list)")

args = parser.parse_args()

with open(args.input, "rb") as f:
    data = pygms.bytestream(f.read(), "<")
    gms = pygms.form(data)
    if args.list == True:
        print("\n".join(dir(gms.sprt)))
    else:
        if args.sprite not in gms.sprt:
            print("Sprite not found!")
            exit()
        
        texturePages = {}
        frames = []
        palette = None
        i=0
        for page in gms.sprt[args.sprite].texturePages:
            sprite = gms.tpag.from_address(page)
            
            if sprite.TexturePage not in texturePages:
                texturePages[sprite.TexturePage] = Image.open(io.BytesIO(gms.txtr[sprite.TexturePage].data))
            
            src = texturePages[sprite.TexturePage]
                
            dst = src.crop((sprite.x, sprite.y, sprite.x+sprite.width, sprite.y+sprite.height))
            dst.save("spr_asgore_hug_frame{}.png".format(i))
            i=i+1
            tcol = None
            colors = [(a[1][0],a[1][1],a[1][2]) for a in dst.getcolors()]
            while True:
                tcol = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
                if tcol not in colors:
                    break
            dst.putdata([(tcol[0],tcol[1],tcol[2],0) if px[3] == 0 else px for px in list(dst.getdata())])
            frames.append(dst)
        
        speed = round(gms.sprt[args.sprite].playbackSpeed*gms.gen8["GameSpeed"])
        
        if args.speed != None:
            speed = int(args.speed)
        
        frames[0].save(args.sprite+".gif",
            save_all=True,
            append_images=frames[1:],
            duration=speed,
            loop=0,
            disposal=2,
            transparency=0
        )
    
