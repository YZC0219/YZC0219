"""Original three-scene data-lab motion graphic. Optional local Pillow tool."""
from pathlib import Path
import math
from PIL import Image, ImageDraw, ImageFont
ROOT=Path(__file__).resolve().parents[1]
FONTS=Path("C:/Windows/Fonts")
BG="#090f1b"; PANEL="#101d2c"; BORDER="#263c50"; MINT="#6be4c1"; BLUE="#87aaff"; WHITE="#edf4ff"; MUTED="#9bb0c8"
def font(size,bold=False,zh=False,mono=False):
    name="msyhbd.ttc" if zh and bold else "msyh.ttc" if zh else "DejaVuSansMono.ttf" if mono else "segoeuib.ttf" if bold else "segoeui.ttf"
    return ImageFont.truetype(str(FONTS/name),size)
def text(d,xy,s,size=14,fill=MUTED,bold=False,zh=False,mono=False):
    d.text(xy,s,font=font(size,bold,zh,mono),fill=fill)
def panel(d,box): d.rounded_rectangle(box,radius=12,fill=PANEL,outline=BORDER,width=1)
def blend(a,b,t): return tuple(round(x+(y-x)*t) for x,y in zip(a,b))
def main():
    base=Image.new("RGB",(1000,460),BG); d=ImageDraw.Draw(base)
    for y in range(460):
        d.line((0,y,1000,y),fill=blend((9,15,27),(14,29,42),y/460))
    for x in range(20,1000,24):
        for y in range(24,460,24): d.point((x,y),fill="#25394c")
    d.rectangle((0,0,999,459),outline=BORDER,width=1)
    d.line((32,58,968,58),fill=BORDER)
    for i,c in enumerate(["#ef8c99","#e6c989",MINT]):d.ellipse((32+i*18,27,40+i*18,35),fill=c)
    text(d,(106,20),"YZC0219 / PERSONAL DATA LAB",12,mono=True)
    text(d,(781,20),"PORTFOLIO  /  01",12,mono=True,fill=MINT)
    text(d,(38,84),"HELLO, WORLD.",13,fill=MINT,mono=True)
    text(d,(34,109),"YZC / 0219",70,WHITE,True)
    text(d,(39,201),"大数据专业学生 · 从问题走向洞察",21,WHITE,zh=True)
    text(d,(40,239),"DATA ENGINEERING  ×  ANALYTICS  ×  VISUALIZATION",12,mono=True)
    d.line((40,285,536,285),fill=BORDER)
    text(d,(40,403),"LEARNING IN PUBLIC",12,fill=MINT,mono=True)
    text(d,(40,426),"BUILD WITH AI. VERIFY WITH EVIDENCE.",11,mono=True)
    panel(d,(593,84,962,303))
    text(d,(611,96),"PROCESS MONITOR",11,mono=True,fill=MINT)
    panel(d,(593,320,962,435))
    text(d,(611,332),"~/data-lab",11,mono=True)
    scene_names=[("01 / BUILD","让数据流动","raw → clean → warehouse","df = clean(raw_records)"),("02 / VERIFY","让结果可信","quality → snapshot → evidence","assert metrics == baseline"),("03 / EXPLAIN","让结论可解释","SQL → visualization → insight","report.render(evidence)")]
    frames=[]
    for frame in range(180):
        scene=frame//60; u=(frame%60)/60; phase=frame/180
        im=base.copy(); d=ImageDraw.Draw(im)
        name,cn,subtitle,code=scene_names[scene]
        opacity=min(1,u*8,(1-u)*8)
        col=blend((14,29,42),(237,244,255),opacity)
        text(d,(40,309),name,14,fill=MINT,mono=True)
        text(d,(40,337),cn,28,col,True,True)
        text(d,(40,378),subtitle,13,fill=MUTED)
        for j in range(3):
            d.rounded_rectangle((810+j*50,418,850+j*50,422),radius=2,fill=MINT if j==scene else BORDER)
        # Decorative particles continue across the entire loop.
        for i in range(14):
            px=557+(i*29+phase*80)%421; py=74+(i*61+phase*18)%366
            d.point((int(px),int(py)),fill="#496276")
        if scene==0:
            nodes=[(638,202),(779,173),(916,202)]
            for a,b in zip(nodes,nodes[1:]):
                d.line((*a,*b),fill=BORDER,width=2)
                t=(u*2)%1
                for k in range(4):
                    q=(t+k/4)%1;px=a[0]+(b[0]-a[0])*q;py=a[1]+(b[1]-a[1])*q
                    d.ellipse((px-3,py-3,px+3,py+3),fill=MINT)
            for i,(x,y) in enumerate(nodes):
                d.rounded_rectangle((x-25,y-26,x+25,y+26),radius=8,fill=BG,outline=MINT if int(u*3)==i else BORDER,width=2)
                text(d,(x-13,y-11),["01","02","03"][i],16,WHITE,mono=True)
                text(d,(x-20,y+40),["RAW","CLEAN","MODEL"][i],10,mono=True)
            for k in range(6):
                x=618+k*54; d.rectangle((x,265,x+32,269),fill=MINT if k<=int(u*6) else BORDER)
        elif scene==1:
            for y in (148,183,218,253):d.line((615,y,940,y),fill=BORDER)
            points=[]
            for i in range(65):
                x=615+i*5; y=212-22*math.sin(i*.21)-8*math.cos(i*.48)
                if i==39:y=142
                points.append((x,y))
            n=max(2,int(min(1,u*1.5)*len(points)))
            d.line(points[:n],fill=BLUE,width=2)
            if n>40:
                x,y=points[39];r=7+int(3*math.sin(u*math.tau))
                d.ellipse((x-r,y-r,x+r,y+r),outline=MINT,width=2)
                text(d,(x-17,y-24),"CHECK",10,fill=MINT,mono=True)
            text(d,(615,279),"TRACE BACK TO THE RECORD",10,mono=True)
        else:
            heights=[58,91,68,107,79,120]
            for k,h in enumerate(heights):
                x=618+k*45;grow=min(1,max(0,u*2-k*.08))
                d.rounded_rectangle((x,263-h*grow,x+24,264),radius=3,fill=MINT if k%2==0 else BLUE)
            d.line((615,265,939,265),fill=BORDER)
            text(d,(615,279),"MEASURE → COMPARE → EXPLAIN",10,mono=True)
        text(d,(611,360),"> "+code[:int(min(1,u*1.6)*len(code))],12,WHITE,mono=True)
        if frame%12<6:text(d,(611+int(min(1,u*1.6)*len(code))*7.2+15,360),"_",12,MINT,mono=True)
        text(d,(611,391),"# original motion illustration",10,mono=True)
        frames.append(im)
    # One palette prevents color flicker between frames.
    sample=Image.new("RGB",(1000,460*3))
    for i,f in enumerate([frames[35],frames[95],frames[155]]):sample.paste(f,(0,i*460))
    palette=sample.quantize(colors=96)
    indexed=[f.quantize(palette=palette,dither=Image.Dither.NONE) for f in frames]
    indexed[0].save(ROOT/"assets/intro.gif",save_all=True,append_images=indexed[1:],duration=80,loop=0,optimize=True,disposal=1)
    for i in [35,95,155]:frames[i].save(ROOT/f"preview/scene-{i}.png")
    print("Rendered 180 frames, three scenes, seamless loop")
if __name__=="__main__":main()
