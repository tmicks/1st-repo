G='<defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#E6C766"/><stop offset="0.55" stop-color="#C9A227"/><stop offset="1" stop-color="#9C7A14"/></linearGradient></defs>'
RING='<circle r="105" fill="none" stroke="url(#g)" stroke-width="2"/>'
GROUND='<line x1="-75" y1="32" x2="75" y2="32" stroke="#C9A227" stroke-width="3" stroke-linecap="round"/>'
ROOTS='<path d="M-6 32 C-10 50 -30 58 -50 66 M6 32 C10 50 30 58 50 66 M0 32 V78 M-3 40 C-20 60 -20 70 -28 82 M3 40 C20 60 20 70 28 82" fill="none" stroke="url(#g)" stroke-width="3.5" stroke-linecap="round"/>'
TRUNK='<path d="M-8 30 C-6 0 -6 -20 -2 -40 M8 30 C6 0 6 -20 2 -40" fill="none" stroke="url(#g)" stroke-width="6" stroke-linecap="round"/>'
UPPER='<path d="M-2 -40 C-15 -70 -10 -80 -20 -90 M2 -40 C15 -70 10 -80 20 -90 M-12 -75 C-30 -85 -35 -90 -40 -95 M12 -75 C30 -85 35 -90 40 -95" fill="none" stroke="url(#g)" stroke-width="3.5" stroke-linecap="round"/>'
ORIG_MAIN='<path d="M0 -38 C-10 -55 -30 -60 -55 -58 M0 -38 C10 -55 30 -60 55 -58 M0 -42 V-92" fill="none" stroke="url(#g)" stroke-width="5" stroke-linecap="round"/>'
ORIG_TWIGS='<path d="M-30 -59 C-45 -70 -60 -70 -70 -65 M30 -59 C45 -70 60 -70 70 -65" fill="none" stroke="url(#g)" stroke-width="3.5" stroke-linecap="round"/>'
def wrap(inner): return RING+inner+GROUND+ROOTS
designs={}
# E0 original for reference
designs["e0-original"]=("E0 — Original E (reference)", wrap(TRUNK+ORIG_MAIN+ORIG_TWIGS+UPPER))
# E5: first branch pair straightened into a crossbar
designs["e5-crossbar-limb"]=("E5 — Straight Limbs Form the Cross", wrap(TRUNK+
 '<path d="M0 -42 V-92 M-2 -48 H-62 M2 -48 H62" fill="none" stroke="url(#g)" stroke-width="6" stroke-linecap="round"/>'
 '<path d="M-40 -48 C-50 -60 -62 -66 -72 -64 M40 -48 C50 -60 62 -66 72 -64 M-50 -48 C-60 -40 -70 -38 -78 -40 M50 -48 C60 -40 70 -38 78 -40" fill="none" stroke="url(#g)" stroke-width="3" stroke-linecap="round"/>'+UPPER))
# E6: original tree; trunk rises straight above canopy and ends in a small cross
designs["e6-cross-crown"]=("E6 — Cross at the Top of the Tree", wrap(TRUNK+ORIG_MAIN.replace(" M0 -42 V-92","")+ORIG_TWIGS+
 '<path d="M-2 -40 C-15 -70 -10 -80 -20 -88 M2 -40 C15 -70 10 -80 20 -88 M-12 -75 C-30 -85 -35 -88 -40 -92 M12 -75 C30 -85 35 -88 40 -92" fill="none" stroke="url(#g)" stroke-width="3.5" stroke-linecap="round"/>'
 '<path d="M0 -42 V-98 M-10 -86 H10" fill="none" stroke="url(#g)" stroke-width="5" stroke-linecap="round"/>'))
# E7: subtle - gold cross inlaid in a solid trunk, original branching
designs["e7-cross-in-trunk"]=("E7 — Cross Carved into the Trunk", wrap(
 '<path d="M-15 31 C-12 0 -11 -20 -5 -42 L5 -42 C11 -20 12 0 15 31 Z" fill="url(#g)"/>'
 '<path d="M0 -28 V20 M-9 -12 H9" stroke="#0A0A0A" stroke-width="4" stroke-linecap="round"/>'+ORIG_MAIN+ORIG_TWIGS+UPPER))
# E8: canopy shaped like a cross: tall crown, wide level arms of foliage
designs["e8-cross-canopy"]=("E8 — Tree Canopy Shaped Like a Cross", wrap(TRUNK+
 '<path d="M0 -40 V-96 M-2 -50 C-20 -52 -40 -50 -70 -52 M2 -50 C20 -52 40 -50 70 -52" fill="none" stroke="url(#g)" stroke-width="5" stroke-linecap="round"/>'
 '<path d="M-30 -51 C-36 -60 -40 -64 -46 -66 M-30 -51 C-36 -42 -40 -38 -46 -36 M-52 -51 C-58 -60 -62 -62 -68 -64 M-52 -51 C-58 -42 -62 -40 -68 -38 M30 -51 C36 -60 40 -64 46 -66 M30 -51 C36 -42 40 -38 46 -36 M52 -51 C58 -60 62 -62 68 -64 M52 -51 C58 -42 62 -40 68 -38 M0 -70 C-6 -76 -10 -80 -14 -82 M0 -70 C6 -76 10 -80 14 -82 M0 -84 C-5 -90 -8 -92 -12 -94 M0 -84 C5 -90 8 -92 12 -94" fill="none" stroke="url(#g)" stroke-width="3" stroke-linecap="round"/>'))
# E9: original tree with roots + branches mirrored; cross formed by trunk + horizontal ground line extended through roots (cross whole silhouette)
designs["e9-roots-cross"]=("E9 — Ground Line and Trunk Form the Cross", RING+TRUNK+ORIG_MAIN+ORIG_TWIGS+UPPER+
 '<path d="M-46 4 H46" stroke="#C9A227" stroke-width="7" stroke-linecap="round"/>'
 '<path d="M0 -20 V32" stroke="#C9A227" stroke-width="12" stroke-linecap="round"/>'+GROUND+ROOTS)
for name,(label,icon) in designs.items():
    svg=f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 280" width="900" height="280"><rect width="900" height="280" fill="#0A0A0A"/>{G}<g transform="translate(160,140)">{icon}</g>'
    svg+='<text x="300" y="140" textLength="540" lengthAdjust="spacingAndGlyphs" font-family="Playfair Display, Georgia, serif" font-size="76" font-weight="700"><tspan fill="#FFFFFF">LEGACY</tspan><tspan fill="url(#g)" font-weight="400"> WORK</tspan></text>'
    svg+='<text x="302" y="200" letter-spacing="5" font-family="Montserrat, Arial, sans-serif" font-size="22" font-weight="600" fill="#C9A227">GENERATIONS START HERE</text></svg>'
    open(name+".svg","w").write(svg)
    open(name+"-icon.svg","w").write(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="-120 -120 240 240" width="240" height="240"><rect x="-120" y="-120" width="240" height="240" fill="#0A0A0A"/>{G}{icon}</svg>')
import json; json.dump([[k,v[0]] for k,v in designs.items()],open("list2.json","w"))
