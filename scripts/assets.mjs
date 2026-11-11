import fs from 'node:fs';
const items=[
['hero-poster','1526870916906-cb9e571f8c69','Jessica Newendyke','https://unsplash.com/photos/eEYAbuxP1gA'],
['airport','1486556813609-9a827fdc306f','CHUTTERSNAP','https://unsplash.com/photos/xDjcU1Pglro'],
['passport','1586441133374-ed1cb4007a47','CardMapr.nl','https://unsplash.com/photos/LVA3S6isNYQ'],
['city','1440190243641-996d004b8c66','Jenny Kim','https://unsplash.com/photos/QnQmw0JfQr8'],
['hotel','1560662105-57f8ad6ae2d1','Tim Photoguy','https://unsplash.com/photos/FPS7a7XQZ0w'],
['map','1643585816267-88f72ea031df','Hans','https://unsplash.com/photos/48BvPxBwQPs']];
for(const [name,id] of items){for(const w of [640,1600]){const r=await fetch('https://images.unsplash.com/photo-'+id+'?w='+w+'&q=82&fit=crop&fm=webp');if(!r.ok)throw Error(name+' '+r.status);fs.writeFileSync('public/media/'+name+(w===640?'-small':'')+'.webp',Buffer.from(await r.arrayBuffer()))}console.log(name)}
