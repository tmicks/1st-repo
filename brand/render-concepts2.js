const { chromium } = require('playwright'); const fs=require('fs');
(async()=>{ const b=await chromium.launch(); const names=['d-blueprint','e-tree','f-column','g-ascend','h-cornerstone'];
 const labels=['D — Blueprint Grid','E — Legacy Tree','F — Classic Column','G — Ascending Monogram','H — Cornerstone'];
 const p=await b.newPage({viewport:{width:900,height:900},deviceScaleFactor:1});
 await p.setContent(`<html><body style="margin:0;background:#222;font-family:Arial">${names.map((n,i)=>`<div style="color:#fff;font-size:18px;padding:6px 10px;background:#333">${labels[i]}</div>${fs.readFileSync(n+'.svg','utf8')}`).join('')}</body></html>`);
 await p.screenshot({path:'concepts-sheet-2.png',fullPage:true});
 for (const n of names){ const q=await b.newPage({viewport:{width:900,height:280},deviceScaleFactor:2}); await q.setContent(`<html><body style="margin:0">${fs.readFileSync(n+'.svg','utf8')}</body></html>`); await q.screenshot({path:n+'.png'}); await q.close(); }
 await b.close(); })();
