const { chromium } = require('playwright'); const fs=require('fs');
(async()=>{ const b=await chromium.launch();
 const d=[['e1-crossbar-branches','E1 — Cross Trunk with Branches'],['e2-canopy-cross','E2 — Cross Within the Canopy'],['e3-organic','E3 — Organic Tree Cross (no ring)'],['e4-minimal','E4 — Minimal Cross with Crown & Roots']];
 const p=await b.newPage({viewport:{width:1300,height:900},deviceScaleFactor:1});
 await p.setContent(`<html><body style="margin:0;background:#222;font-family:Arial">${d.map(([n,l])=>`<div style="color:#fff;font-size:18px;padding:6px 10px;background:#333">${l}</div><div style="display:flex;align-items:center;gap:0">${fs.readFileSync(n+'-icon.svg','utf8').replace('width="240" height="240"','width="280" height="280"')}<div style="width:120px;background:#FFF;height:280px;display:flex;align-items:center;justify-content:center"><div style="width:100px;height:100px">${fs.readFileSync(n+'-icon.svg','utf8').replace('width="240" height="240"','width="100" height="100"').replace('fill="#0A0A0A"/>','fill="#FFFFFF"/>')}</div></div>${fs.readFileSync(n+'.svg','utf8')}</div>`).join('')}</body></html>`);
 await p.screenshot({path:'tree-cross-sheet.png',fullPage:true});
 for (const [n] of d){ const q=await b.newPage({viewport:{width:900,height:280},deviceScaleFactor:2}); await q.setContent(`<html><body style="margin:0">${fs.readFileSync(n+'.svg','utf8')}</body></html>`); await q.screenshot({path:n+'.png'}); await q.close(); }
 await b.close(); })();
