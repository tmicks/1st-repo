const { chromium } = require('playwright'); const fs=require('fs');
const b64=f=>'data:image/png;base64,'+fs.readFileSync(f).toString('base64');
const darkIcon=b64('icon-dark.png'), tIcon=b64('icon-transparent.png');
const grad='background:linear-gradient(135deg,#EBCB6A,#C9A227 55%,#9C7A14);-webkit-background-clip:text;background-clip:text;color:transparent;';
const font=`<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700&family=Montserrat:wght@600&display=swap" rel="stylesheet">`;
const word=(dark,size)=>`<div style="font-family:'Playfair Display',Georgia,serif;font-size:${size}px;letter-spacing:4px;line-height:1"><span style="font-weight:700;color:${dark?'#fff':'#0A0A0A'}">LEGACY</span> <span style="font-weight:400;${grad}">WORK</span></div>`;
const tag=(size)=>`<div style="font-family:Montserrat,Arial,sans-serif;font-weight:600;font-size:${size}px;letter-spacing:6px;color:#C9A227;margin-top:18px">GENERATIONS START HERE</div>`;
const jobs={
 'logo-horizontal-dark':[1000,320,`<body style="margin:0;background:#0A0A0A;display:flex;align-items:center;height:320px;padding-left:30px"><img src="${tIcon}" style="width:290px;height:290px"><div style="margin-left:30px">${word(true,82)}${tag(22)}</div></body>`],
 'logo-horizontal-light':[1000,320,`<body style="margin:0;background:#fff;display:flex;align-items:center;height:320px;padding-left:30px"><img src="${darkIcon}" style="width:270px;height:270px;border-radius:50%"><div style="margin-left:40px">${word(false,82)}${tag(22)}</div></body>`],
 'logo-horizontal-transparent':[1000,320,`<body style="margin:0;background:transparent;display:flex;align-items:center;height:320px;padding-left:30px"><img src="${tIcon}" style="width:290px;height:290px"><div style="margin-left:30px">${word(true,82)}${tag(22)}</div></body>`],
 'logo-stacked-dark':[700,760,`<body style="margin:0;background:#0A0A0A;display:flex;flex-direction:column;align-items:center;justify-content:center;height:760px"><img src="${tIcon}" style="width:470px;height:470px"><div style="text-align:center;margin-top:10px">${word(true,68)}${tag(20)}</div></body>`],
 'header-logo-dark':[720,160,`<body style="margin:0;background:transparent;display:flex;align-items:center;height:160px"><img src="${tIcon}" style="width:150px;height:150px"><div style="margin-left:16px">${word(true,58)}</div></body>`],
};
(async()=>{ const b=await chromium.launch();
 for (const [n,[w,h,body]] of Object.entries(jobs)){ const p=await b.newPage({viewport:{width:w,height:h},deviceScaleFactor:2});
  await p.setContent(`<html><head>${font}<style>html{background:transparent}</style></head>${body}</html>`); await p.waitForTimeout(400);
  await p.screenshot({path:n+'.png',omitBackground:true}); await p.close(); }
 const q=await b.newPage({viewport:{width:1100,height:900}});
 await q.setContent(`<html><body style="margin:0;background:#444;padding:10px;display:flex;flex-wrap:wrap;gap:10px;align-items:flex-start">
  <img src="${b64('logo-horizontal-dark.png')}" width="700"><img src="${b64('icon-dark.png')}" width="300">
  <img src="${b64('logo-horizontal-light.png')}" width="700"><div style="background:#fff;padding:20px"><img src="${b64('favicon-64.png')}" width="64"> <img src="${b64('favicon-64.png')}" width="32"> <img src="${b64('favicon-64.png')}" width="16"></div>
  <img src="${b64('logo-stacked-dark.png')}" width="300"><div style="background:#0A0A0A;padding:10px"><img src="${b64('header-logo-dark.png')}" width="360"></div>
 </body></html>`); await q.screenshot({path:'preview.png',fullPage:true});
 await b.close(); })();
