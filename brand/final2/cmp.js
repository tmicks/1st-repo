const { chromium } = require('playwright'); const fs=require('fs');
(async()=>{ const b=await chromium.launch(); const p=await b.newPage({viewport:{width:1000,height:540}});
 await p.setContent(`<html><body style="margin:0;background:#333;font-family:Arial;color:#fff;display:flex;gap:20px;padding:10px;align-items:flex-start">
 <div><div style="padding:4px">1 — E6b leaves (no fruit)</div>${fs.readFileSync('compare-a-original.svg','utf8')}</div>
 <div><div style="padding:4px">2 — Slightly larger leaves (no fruit)</div>${fs.readFileSync('compare-b-larger-leaves.svg','utf8')}</div></body></html>`);
 await p.screenshot({path:'compare.png'}); await b.close(); })();
