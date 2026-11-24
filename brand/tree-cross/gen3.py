import math, json
exec(open("gen2.py").read().split("def wrap")[0])  # reuse constants
def wrap(inner): return RING+inner+GROUND+ROOTS
def leaf(x,y,ang,l=9,w=4.2,fill="url(#g)"):
    return f'<ellipse cx="{x:.1f}" cy="{y:.1f}" rx="{l/2}" ry="{w/2}" transform="rotate({ang:.0f} {x:.1f} {y:.1f})" fill="{fill}"/>'
def cluster(x,y,base,n=3,spread=40,dist=5):
    out=""
    for i in range(n):
        a=base+(i-(n-1)/2)*spread
        r=math.radians(a)
        out+=leaf(x+dist*math.cos(r),y+dist*math.sin(r),a)
    return out
def fruit(x,y,r=3.4):
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="#E6C766"/><circle cx="{x-1}" cy="{y-1}" r="{r*0.35}" fill="#FFF3C4"/>'
def ang(x,y): return math.degrees(math.atan2(y+40,x))  # direction from trunk top
def leaves_at(pts,n=3): return "".join(cluster(x,y,ang(x,y),n) for x,y in pts)
def fruits_at(pts): return "".join(fruit(x,y) for x,y in pts)
E6_TREE=TRUNK+ORIG_MAIN.replace(" M0 -42 V-92","")+ORIG_TWIGS+'<path d="M-2 -40 C-15 -70 -10 -80 -20 -88 M2 -40 C15 -70 10 -80 20 -88 M-12 -75 C-30 -85 -35 -88 -40 -92 M12 -75 C30 -85 35 -88 40 -92" fill="none" stroke="url(#g)" stroke-width="3.5" stroke-linecap="round"/>'+'<path d="M0 -42 V-98" fill="none" stroke="#C9A227" stroke-width="5" stroke-linecap="round"/><path d="M-10 -86 H10" stroke="#C9A227" stroke-width="5" stroke-linecap="round"/>'
E6_TIPS=[(-55,-58),(55,-58),(-70,-65),(70,-65),(-20,-88),(20,-88),(-40,-92),(40,-92)]
E6_MIDS=[(-42,-61),(42,-61),(-28,-83),(28,-83),(-60,-67),(60,-67),(-12,-72),(12,-72),(-34,-58),(34,-58)]
E6_FRUIT=[(-46,-52),(46,-52),(-62,-58),(62,-58),(-26,-76),(26,-76),(-8,-62),(8,-62)]
def midleaves(pts): return "".join(leaf(x,y,(-35 if x<0 else 35)+(180 if i%2 else 0),8,3.6) for i,(x,y) in enumerate(pts))
designs={}
designs["e6a-leaves"]=("E6a — Cross at the Top, with Leaves", wrap(E6_TREE+leaves_at(E6_TIPS)+midleaves(E6_MIDS)))
designs["e6b-leaves-fruit"]=("E6b — Cross at the Top, with Leaves & Fruit", wrap(E6_TREE+leaves_at(E6_TIPS)+midleaves(E6_MIDS)+fruits_at(E6_FRUIT)))
E5_TREE=TRUNK+'<path d="M0 -42 V-92" fill="none" stroke="#C9A227" stroke-width="6" stroke-linecap="round"/><path d="M-62 -48 H62" stroke="#C9A227" stroke-width="6" stroke-linecap="round"/>'+'<path d="M-40 -48 C-50 -60 -62 -66 -72 -64 M40 -48 C50 -60 62 -66 72 -64 M-50 -48 C-60 -40 -70 -38 -78 -40 M50 -48 C60 -40 70 -38 78 -40" fill="none" stroke="url(#g)" stroke-width="3" stroke-linecap="round"/>'+UPPER
E5_TIPS=[(-72,-64),(72,-64),(-78,-40),(78,-40),(-20,-90),(20,-90),(-40,-95),(40,-95),(-64,-48),(64,-48)]
E5_FRUIT=[(-30,-42),(30,-42),(-56,-56),(56,-56),(-60,-38),(60,-38),(-18,-74),(18,-74)]
designs["e5b-leaves-fruit"]=("E5b — Straight Limbs Cross, with Leaves & Fruit", wrap(E5_TREE+leaves_at(E5_TIPS)+midleaves([(-28,-84),(28,-84),(-12,-72),(12,-72)])+fruits_at(E5_FRUIT)))
E7_TREE='<path d="M-15 31 C-12 0 -11 -20 -5 -42 L5 -42 C11 -20 12 0 15 31 Z" fill="url(#g)"/><path d="M0 -28 V20 M-9 -12 H9" stroke="#0A0A0A" stroke-width="4" stroke-linecap="round"/>'+ORIG_MAIN+ORIG_TWIGS+UPPER
E7_TIPS=[(-55,-58),(55,-58),(-70,-65),(70,-65),(-20,-90),(20,-90),(-40,-95),(40,-95),(0,-94)]
designs["e7b-leaves-fruit"]=("E7b — Cross in the Trunk, with Leaves & Fruit", wrap(E7_TREE+leaves_at(E7_TIPS)+midleaves(E6_MIDS)+fruits_at(E6_FRUIT)))
E8_TREE=TRUNK+'<path d="M0 -40 V-96" fill="none" stroke="#C9A227" stroke-width="5" stroke-linecap="round"/><path d="M-70 -51 H70" stroke="#C9A227" stroke-width="5" stroke-linecap="round"/>'+'<path d="M-30 -51 C-36 -60 -40 -64 -46 -66 M-30 -51 C-36 -42 -40 -38 -46 -36 M-52 -51 C-58 -60 -62 -62 -68 -64 M-52 -51 C-58 -42 -62 -40 -68 -38 M30 -51 C36 -60 40 -64 46 -66 M30 -51 C36 -42 40 -38 46 -36 M52 -51 C58 -60 62 -62 68 -64 M52 -51 C58 -42 62 -40 68 -38 M0 -70 C-6 -76 -10 -80 -14 -82 M0 -70 C6 -76 10 -80 14 -82 M0 -84 C-5 -90 -8 -92 -12 -94 M0 -84 C5 -90 8 -92 12 -94" fill="none" stroke="url(#g)" stroke-width="3" stroke-linecap="round"/>'
E8_TIPS=[(-46,-66),(-46,-36),(-68,-64),(-68,-38),(46,-66),(46,-36),(68,-64),(68,-38),(-14,-82),(14,-82),(-12,-94),(12,-94),(-74,-51),(74,-51),(0,-100)]
designs["e8b-leaves-fruit"]=("E8b — Cross-Shaped Canopy, with Leaves & Fruit", wrap(E8_TREE+leaves_at(E8_TIPS)+fruits_at([(-40,-44),(40,-44),(-60,-44),(60,-44),(-20,-58),(20,-58)])))
for name,(label,icon) in designs.items():
    svg=f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 280" width="900" height="280"><rect width="900" height="280" fill="#0A0A0A"/>{G}<g transform="translate(160,140)">{icon}</g>'
    svg+='<text x="300" y="140" textLength="540" lengthAdjust="spacingAndGlyphs" font-family="Playfair Display, Georgia, serif" font-size="76" font-weight="700"><tspan fill="#FFFFFF">LEGACY</tspan><tspan fill="url(#g)" font-weight="400"> WORK</tspan></text>'
    svg+='<text x="302" y="200" letter-spacing="5" font-family="Montserrat, Arial, sans-serif" font-size="22" font-weight="600" fill="#C9A227">GENERATIONS START HERE</text></svg>'
    open(name+".svg","w").write(svg)
    open(name+"-icon.svg","w").write(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="-120 -120 240 240" width="240" height="240"><rect x="-120" y="-120" width="240" height="240" fill="#0A0A0A"/>{G}{icon}</svg>')
json.dump([[k,v[0]] for k,v in designs.items()],open("list3.json","w"))
