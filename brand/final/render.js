const { chromium } = require('playwright'); const fs=require('fs');
(async()=>{ const b=await chromium.launch();
 const jobs=[['logo-horizontal-dark',900,280,2],['logo-horizontal-light',900,280,2],['logo-stacked-dark',600,620,2],['icon-dark',512,512,1],['icon-transparent',512,512,1],['favicon',512,512,1]];
 for(const [n,w,h,s] of jobs){ const p=await b.newPage({viewport:{width:w,height:h},deviceScaleFactor:s});
  await p.setContent(`<html><head><style>html,body{margin:0;background:transparent}</style></head><body>${fs.readFileSync(n+'.svg','utf8')}</body></html>`);
  await p.screenshot({path:n+'.png',omitBackground:true}); await p.close(); }
 const p=await b.newPage({viewport:{width:64,height:64}}); await p.setContent(`<html><body style="margin:0">${fs.readFileSync('favicon.svg','utf8').replace('width="512" height="512"','width="64" height="64"')}</body></html>`); await p.screenshot({path:'favicon-64.png',omitBackground:true});
 const q=await b.newPage({viewport:{width:1200,height:700}});
 await q.setContent(`<html><body style="margin:0;background:#333;display:flex;flex-wrap:wrap;gap:10px;padding:10px;align-items:flex-start">
 <img src="data:image/png;base64,${fs.readFileSync('logo-horizontal-dark.png').toString('base64')}" width="720">
 <img src="data:image/png;base64,${fs.readFileSync('icon-dark.png').toString('base64')}" width="256">
 <img src="data:image/png;base64,${fs.readFileSync('logo-horizontal-light.png').toString('base64')}" width="720">
 <div style="background:#fff;padding:20px"><img src="data:image/png;base64,${fs.readFileSync('favicon-64.png').toString('base64')}" width="64"> <img src="data:image/png;base64,${fs.readFileSync('favicon-64.png').toString('base64')}" width="32"> <img src="data:image/png;base64,${fs.readFileSync('favicon-64.png').toString('base64')}" width="16"></div>
 </body></html>`); await q.screenshot({path:'final-preview.png',fullPage:true});
 await b.close(); })();
