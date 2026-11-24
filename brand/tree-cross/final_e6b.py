import math, os
src=open("gen3.py").read().split("designs={}")[0]
exec(src)
def build(scale):
    global leaf
    base_leaf=leaf
    def leaf2(x,y,ang,l=9,w=4.2,fill="url(#g)"): return base_leaf(x,y,ang,l*scale,w*scale,fill)
    import builtins
    g=globals(); old=g['leaf']; g['leaf']=leaf2
    icon=wrap(E6_TREE+leaves_at(E6_TIPS)+midleaves(E6_MIDS)+fruits_at(E6_FRUIT))
    g['leaf']=old
    return icon
os.makedirs("../final2",exist_ok=True)
for tag,sc in [("a-original",1.0),("b-larger-leaves",1.3)]:
    icon=build(sc)
    open(f"../final2/compare-{tag}.svg","w").write(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="-120 -120 240 240" width="480" height="480"><rect x="-120" y="-120" width="240" height="240" fill="#0A0A0A"/>{G}{icon}</svg>')
