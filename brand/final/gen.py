import math, random
random.seed(7)
G='<defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#EBCB6A"/><stop offset="0.55" stop-color="#C9A227"/><stop offset="1" stop-color="#9C7A14"/></linearGradient><linearGradient id="lf" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#F0D57A"/><stop offset="1" stop-color="#B8901C"/></linearGradient></defs>'
GOLD="#C9A227"
def leaf(x,y,a,l=13,w=6):
    # pointed leaf shape (vesica) with midrib
    r=math.radians(a); dx,dy=math.cos(r)*l/2,math.sin(r)*l/2; px,py=-math.sin(r)*w/2,math.cos(r)*w/2
    x1,y1,x2,y2=x-dx,y-dy,x+dx,y+dy
    return (f'<path d="M{x1:.1f} {y1:.1f} Q{x+px:.1f} {y+py:.1f} {x2:.1f} {y2:.1f} Q{x-px:.1f} {y-py:.1f} {x1:.1f} {y1:.1f} Z" fill="url(#lf)"/>')
def fruit(x,y,r=4.2):
    return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="#E9C85F" stroke="#9C7A14" stroke-width="0.8"/><circle cx="{x-1.3:.1f}" cy="{y-1.3:.1f}" r="{r*0.33:.1f}" fill="#FFF4CC"/>'
TRUNK='<path d="M-9 30 C-7 0 -7 -20 -2.5 -40 L2.5 -40 C7 -20 7 0 9 30 Z" fill="url(#g)"/>'
BRANCHES=('<path d="M0 -38 C-10 -55 -30 -60 -55 -58 M0 -38 C10 -55 30 -60 55 -58" fill="none" stroke="url(#g)" stroke-width="5" stroke-linecap="round"/>'
 '<path d="M-30 -59 C-45 -70 -60 -70 -70 -65 M30 -59 C45 -70 60 -70 70 -65 M-2 -40 C-15 -70 -10 -80 -20 -86 M2 -40 C15 -70 10 -80 20 -86 M-12 -74 C-30 -84 -35 -86 -40 -89 M12 -74 C30 -84 35 -86 40 -89" fill="none" stroke="url(#g)" stroke-width="3.5" stroke-linecap="round"/>')
CROSS=f'<path d="M0 -40 V-100" stroke="#0A0A0A" stroke-width="10" stroke-linecap="round"/><path d="M-12 -87 H12" stroke="#0A0A0A" stroke-width="10" stroke-linecap="round"/><path d="M0 -40 V-100" stroke="{GOLD}" stroke-width="5.5" stroke-linecap="round"/><path d="M-12 -87 H12" stroke="{GOLD}" stroke-width="5.5" stroke-linecap="round"/>'
GROUND=f'<line x1="-72" y1="32" x2="72" y2="32" stroke="{GOLD}" stroke-width="3" stroke-linecap="round"/>'
ROOTS='<path d="M-6 32 C-10 50 -30 58 -50 66 M6 32 C10 50 30 58 50 66 M0 32 V80 M-3 40 C-20 60 -20 70 -28 84 M3 40 C20 60 20 70 28 84 M-28 56 C-38 64 -40 72 -42 78 M28 56 C38 64 40 72 42 78" fill="none" stroke="url(#g)" stroke-width="3.5" stroke-linecap="round"/>'
def canopy(n_leaves=70, fruits=True, leafsize=1.0):
    # leaves distributed along branch paths and in clusters near tips, inside an ellipse canopy
    pts=[]
    tips=[(-36,-56),(36,-56),(-50,-82),(50,-82),(-76,-56),(76,-56),(-8,-74),(8,-74),(-55,-58),(55,-58),(-70,-65),(70,-65),(-20,-86),(20,-86),(-40,-89),(40,-89),(-42,-62),(42,-62),(-28,-80),(28,-80),(-14,-70),(14,-70),(-62,-70),(62,-70)]
    out=""
    for (tx,ty) in tips:
        k=10
        for i in range(k):
            a=random.uniform(0,360); d=random.uniform(2,17)
            x=tx+d*math.cos(math.radians(a)); y=ty+d*math.sin(math.radians(a))*0.8
            if abs(x)<9 and y<-80: continue   # keep cross area clear
            if (x/88)**2+((y+68)/44)**2>1: continue
            out+=leaf(x,y,random.uniform(-180,180),17*leafsize,8*leafsize)
    fr=""
    if fruits:
        for (x,y) in [(-48,-50),(48,-50),(-64,-58),(64,-58),(-30,-70),(30,-70),(-8,-60),(8,-60),(-50,-76),(50,-76),(-20,-94),(20,-94)]:
            fr+=fruit(x,y)
    return out,fr
def icon(ring=True, fruits=True, simple=False):
    random.seed(7)
    lv,fr=canopy(fruits=fruits, leafsize=1.25 if simple else 1.0)
    s=''
    if ring: s+=f'<circle r="108" fill="none" stroke="url(#g)" stroke-width="2.5"/>'
    s+=f'<g transform="translate(0,4) scale(0.95)">{TRUNK}{BRANCHES}{lv}{fr}{CROSS}{GROUND}{ROOTS}</g>'
    return s
def svg_wrap(w,h,body,bg): 
    r=f'<rect width="{w}" height="{h}" fill="{bg}"/>' if bg else ''
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">{r}{G}{body}</svg>'
def wordmark(x,y,dark=True,tag=True,anchor="start",size=76,width=540):
    c="#FFFFFF" if dark else "#0A0A0A"
    s=f'<text x="{x}" y="{y}" text-anchor="{anchor}" textLength="{width}" lengthAdjust="spacingAndGlyphs" font-family="Playfair Display, Georgia, serif" font-size="{size}" font-weight="700"><tspan fill="{c}">LEGACY</tspan><tspan fill="url(#g)" font-weight="400"> WORK</tspan></text>'
    if tag: s+=f'<text x="{x if anchor=="start" else x}" y="{y+58}" text-anchor="{anchor}" letter-spacing="5" font-family="Montserrat, Arial, sans-serif" font-size="22" font-weight="600" fill="{GOLD}">GENERATIONS START HERE</text>'
    return s
files={
 "logo-horizontal-dark": svg_wrap(900,280,f'<g transform="translate(150,140) scale(1.15)">{icon()}</g>'+wordmark(310,140),"#0A0A0A"),
 "logo-horizontal-light": svg_wrap(900,280,f'<g transform="translate(150,140) scale(1.08)"><circle r="118" fill="#0A0A0A"/>{icon()}</g>'+wordmark(310,140,dark=False),"#FFFFFF"),
 "logo-stacked-dark": svg_wrap(600,620,f'<g transform="translate(300,200) scale(1.55)">{icon()}</g>'+wordmark(300,470,anchor="middle",size=62,width=470),"#0A0A0A"),
 "icon-dark": svg_wrap(512,512,f'<g transform="translate(256,256) scale(2.25)">{icon()}</g>',"#0A0A0A"),
 "icon-transparent": svg_wrap(512,512,f'<g transform="translate(256,256) scale(2.25)"><circle r="112" fill="#0A0A0A"/>{icon()}</g>',None),
 "favicon": svg_wrap(512,512,f'<rect width="512" height="512" rx="96" fill="#0A0A0A"/><g transform="translate(256,262) scale(2.3)">{icon(ring=False,fruits=False,simple=True)}</g>',None),
}
for k,v in files.items(): open(k+".svg","w").write(v)
print(list(files))
