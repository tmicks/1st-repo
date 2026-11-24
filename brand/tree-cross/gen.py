import math
G='<defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#E6C766"/><stop offset="0.55" stop-color="#C9A227"/><stop offset="1" stop-color="#9C7A14"/></linearGradient></defs>'
def leaf(x,y,ang,l=14,w=6,fill="url(#g)"):
    return f'<ellipse cx="{x:.1f}" cy="{y:.1f}" rx="{l/2}" ry="{w/2}" transform="rotate({ang} {x:.1f} {y:.1f})" fill="{fill}"/>'
def roots(y0,spread=60,depth=55,sw=4):
    p=[f'M0 {y0} V{y0+depth+8}']
    for s in (-1,1):
        p.append(f'M{s*3} {y0} C{s*6} {y0+20} {s*spread*0.5} {y0+28} {s*spread} {y0+depth}')
        p.append(f'M{s*2} {y0+10} C{s*10} {y0+30} {s*spread*0.3} {y0+40} {s*spread*0.45} {y0+depth+6}')
        p.append(f'M{s*spread*0.55} {y0+28} C{s*spread*0.8} {y0+30} {s*spread*0.95} {y0+34} {s*spread*1.1} {y0+40}')
    return f'<path d="{" ".join(p)}" fill="none" stroke="url(#g)" stroke-width="{sw}" stroke-linecap="round"/>'

# E1: solid cross trunk, branches + leaves from crossbar ends & top, roots, in circle
def e1():
    s='<circle r="108" fill="none" stroke="url(#g)" stroke-width="2.5"/>'
    s+='<path d="M-9 50 L-7 -70 Q0 -78 7 -70 L9 50 Z" fill="url(#g)"/>'          # vertical beam (tapered)
    s+='<path d="M-62 -26 Q-66 -32 -60 -36 L60 -36 Q66 -32 62 -26 Z" fill="url(#g)"/>' # crossbar
    br=[]
    for sx in (-1,1):
        br.append(f'M{sx*60} -31 C{sx*75} -40 {sx*80} -55 {sx*78} -68')
        br.append(f'M{sx*60} -31 C{sx*76} -28 {sx*86} -20 {sx*90} -8')
        br.append(f'M0 -70 C{sx*8} -82 {sx*20} -88 {sx*30} -92')
    s+=f'<path d="{" ".join(br)}" fill="none" stroke="url(#g)" stroke-width="3.5" stroke-linecap="round"/>'
    for (x,y,a) in [(-78,-72,-70),(-84,-60,-30),(-90,-6,70),(-84,-18,30),(78,-72,70),(84,-60,30),(90,-6,-70),(84,-18,-30),(-30,-95,-20),(-20,-90,-50),(30,-95,20),(20,-90,50),(0,-84,90)]:
        s+=leaf(x,y,a)
    s+=roots(50,62,45,3.5)
    return s
# E2: round canopy of leaves with cross in negative space; roots below
def e2():
    s='<circle r="108" fill="none" stroke="url(#g)" stroke-width="2.5"/>'
    leaves=[]
    import random; random.seed(4)
    for r in (30,46,60,72):
        n=int(r/3.2)
        for i in range(n):
            a=2*math.pi*i/n+r
            x=r*math.cos(a); y=r*math.sin(a)*0.9-28
            if abs(x)<11 or (abs(y+38)<10 and abs(x)<52): continue  # cross cutout
            leaves.append(leaf(x,y,math.degrees(a)+90,13,6))
    s+="".join(leaves)
    s+='<path d="M-6 30 L-5 -90 M6 30 L5 -90" stroke="none"/>'
    s+='<rect x="-5" y="-92" width="10" height="130" fill="url(#g)" rx="2"/><rect x="-46" y="-43" width="92" height="10" fill="url(#g)" rx="2"/>'
    s+=roots(38,58,48,3.5)
    return s
# E3: line-art, no circle, organic trunk & limbs form cross, leaf clusters
def e3():
    s='<path d="M0 55 C-4 20 -3 -20 0 -95 M0 -38 C-25 -40 -50 -36 -78 -42 M0 -38 C25 -40 50 -36 78 -42" fill="none" stroke="url(#g)" stroke-width="9" stroke-linecap="round"/>'
    for (x,y,a) in [(-84,-48,-30),(-86,-36,20),(-70,-54,-60),(-64,-30,40),(84,-48,30),(86,-36,-20),(70,-54,60),(64,-30,-40),(0,-104,90),(-10,-98,-50),(10,-98,50),(-9,-84,-30),(9,-84,30)]:
        s+=leaf(x,y,a,18,8)
    s+=roots(52,70,52,4.5)
    return s
# E4: minimal: clean cross with crown of 5 leaves on top and roots, thin double circle
def e4():
    s='<circle r="108" fill="none" stroke="url(#g)" stroke-width="2"/><circle r="98" fill="none" stroke="url(#g)" stroke-width="1"/>'
    s+='<rect x="-7" y="-70" width="14" height="120" fill="url(#g)" rx="2"/><rect x="-44" y="-40" width="88" height="14" fill="url(#g)" rx="2"/>'
    for (x,y,a) in [(0,-84,90),(-14,-80,-60),(14,-80,60),(-22,-70,-20),(22,-70,20)]:
        s+=leaf(x,y,a,20,8)
    s+=roots(50,54,40,3.5)
    return s
designs=[("e1-crossbar-branches","E1 — Cross Trunk with Branches",e1),("e2-canopy-cross","E2 — Cross Within the Canopy",e2),("e3-organic","E3 — Organic Tree Cross (no ring)",e3),("e4-minimal","E4 — Minimal Cross with Crown & Roots",e4)]
for name,label,fn in designs:
    svg=f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 280" width="900" height="280"><rect width="900" height="280" fill="#0A0A0A"/>{G}<g transform="translate(160,140)">{fn()}</g>'
    svg+='<text x="300" y="140" textLength="540" lengthAdjust="spacingAndGlyphs" font-family="Playfair Display, Georgia, serif" font-size="76" font-weight="700"><tspan fill="#FFFFFF">LEGACY</tspan><tspan fill="url(#g)" font-weight="400"> WORK</tspan></text>'
    svg+='<text x="302" y="200" letter-spacing="5" font-family="Montserrat, Arial, sans-serif" font-size="22" font-weight="600" fill="#C9A227">GENERATIONS START HERE</text></svg>'
    open(name+".svg","w").write(svg)
    # icon-only large
    open(name+"-icon.svg","w").write(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="-120 -120 240 240" width="240" height="240"><rect x="-120" y="-120" width="240" height="240" fill="#0A0A0A"/>{G}{fn()}</svg>')
print("ok")
