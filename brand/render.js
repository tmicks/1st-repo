const { chromium } = require('playwright');
const fs=require('fs');
(async()=>{
 const b=await chromium.launch();
 const jobs=[['mark.svg',240,280,'mark.png',2],['mark.svg',240,280,'favicon.png',0.4],['logo-horizontal-dark.svg',900,280,'logo-horizontal-dark.png',2],['logo-horizontal-light.svg',900,280,'logo-horizontal-light.png',2]];
 for(const [f,w,h,out,s] of jobs){
  const p=await b.newPage({viewport:{width:w,height:h},deviceScaleFactor:s});
  const svg=fs.readFileSync(f,'utf8');
  await p.setContent(`<html><head><style>html,body{margin:0;background:transparent}</style></head><body>${svg}</body></html>`);
  await p.screenshot({path:out,omitBackground:true,clip:{x:0,y:0,width:w,height:h}});
  await p.close();
 }
 await b.close();
})();
