from PIL import Image, ImageDraw, ImageFont, ImageFilter
from pathlib import Path

OUT=Path("release"); OUT.mkdir(exist_ok=True)
ROOT=Path("source")
REG="/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
BOLD="/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
def font(s,bold=False): return ImageFont.truetype(BOLD if bold else REG,s)

def cover(kicker,title,subtitle,source,crop,foot,accent,name,local=False):
    image=Image.new("RGB",(1000,750),"#f6f5f2")
    d=ImageDraw.Draw(image)
    d.text((46,34),kicker,font=font(16),fill=accent)
    # use a constrained title width, never truncate
    title_size=45
    while d.textbbox((0,0),title,font=font(title_size,True))[2]>909:
        title_size-=1
    d.text((46,76),title,font=font(title_size,True),fill="#17272c")
    d.text((46,140),subtitle,font=font(17),fill="#607684")
    d.line((46,169,954,169),fill="#d6d9d8",width=1)
    sh=Image.new("RGBA",(1000,750),(0,0,0,0))
    ImageDraw.Draw(sh).rectangle((43,184,957,680),fill=(0,0,0,58))
    image=Image.alpha_composite(image.convert("RGBA"),sh.filter(ImageFilter.GaussianBlur(10))).convert("RGB")
    screen=Image.open(ROOT/source).convert("RGB")
    if local:
        dd=ImageDraw.Draw(screen)
        dd.rectangle((44,361,234,386),fill="#111820")
        dd.text((62,365),"SYNTHETIC UI DATA",font=font(12,True),fill="#69dbff")
    screen=screen.crop(crop)
    screen.thumbnail((916,494),Image.Resampling.LANCZOS)
    panel=Image.new("RGB",(916,494),"#090d12" if local else "#04140d")
    panel.paste(screen,((916-screen.width)//2,(494-screen.height)//2))
    image.paste(panel,(42,184))
    d=ImageDraw.Draw(image)
    d.rectangle((42,184,957,677),outline="#b6c0c3",width=1)
    d.text((46,708),foot,font=font(15),fill="#17272c")
    d.line((914,710,925,699),fill=accent,width=2)
    d.line((915,710,925,710),fill=accent,width=2)
    d.line((925,699,925,710),fill=accent,width=2)
    image.save(OUT/name,optimize=True)

cover("02 / WORKFLOW AUTOMATION","Turn missed calls into decisions.",
      "Revenue Recovery OS / auditable synthetic workflow demonstration",
      "revenue-recovery-normal.png",(150,490,1240,1080),
      "Completed 7-stage demo  ·  idempotent CRM write  ·  explicit booking state",
      "#0c8669","revenue-recovery-cover.png")
cover("03 / PRODUCT WORKFLOWS","Review before you submit.",
      "RolePilot / original application UI, synthetic offline fixture",
      "rolepilot-source-ui.png",(40,350,1405,968),
      "Independent prototype  ·  readiness checks  ·  human approval",
      "#117897","rolepilot-cover.png",local=True)
print("Output files:",*[str(p) for p in OUT.glob("*.png")])
