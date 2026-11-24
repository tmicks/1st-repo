const { chromium } = require('playwright'); const fs=require('fs');
(async()=>{ const b=await chromium.launch();
 const p=await b.newPage({viewport:{width:900,height:900},deviceScaleFactor:1});
 const svgs=['a-keystone','b-pillars','c-monogram'].map(n=>fs.readFileSync(n+'.svg','utf8'));
 const labels=['A — Keystone Arch','B — Rising Pillars','C — Monogram Seal'];
 await p.setContent(`<html><body style="margin:0;background:#222;font-family:Arial">${svgs.map((s,i)=>`<div style="color:#fff;font-size:18px;padding:6px 10px;background:#333">${labels[i]}</div>${s}`).join('')}</body></html>`);
 await p.screenshot({path:'concepts-sheet.png',fullPage:true});
 for (const n of ['a-keystone','b-pillars','c-monogram']){ const q=await b.newPage({viewport:{width:900,height:280},deviceScaleFactor:2}); await q.setContent(`<html><body style="margin:0">${fs.readFileSync(n+'.svg','utf8')}</body></html>`); await q.screenshot({path:n+'.png'}); await q.close(); }
 await b.close(); })();
