document.addEventListener('click',e=>{const c=e.target.closest('.copy');if(c){navigator.clipboard.writeText(document.getElementById(c.dataset.t).textContent).then(()=>{c.textContent='Скопировано ✓';setTimeout(()=>c.textContent='Скопировать',1500)})}
const t=e.target.closest('[data-tab]');if(t){document.querySelectorAll('[data-tab]').forEach(b=>b.classList.toggle('on',b===t));document.querySelectorAll('.pbox[id^=w]').forEach(p=>p.hidden=p.id!=='w'+t.dataset.tab.slice(1))}});
const q=document.getElementById('q');if(q){let f='';const run=()=>{let n=0;document.querySelectorAll('.scard').forEach(c=>{const ok=c.dataset.q.includes(q.value.toLowerCase().trim())&&c.dataset.q.includes(f);c.hidden=!ok;n+=ok});document.getElementById('empty').hidden=n>0};q.oninput=run;
document.getElementById('chips').onclick=e=>{const b=e.target.closest('button');if(!b)return;f=b.dataset.f;document.querySelectorAll('#chips button').forEach(x=>x.classList.toggle('on',x===b));run()}}
if(window.GEN){const g=()=>{const n=GEN.niches[gn.value],s=GEN.styles[gs.value],c=gc.value.toUpperCase();
gout.textContent=`Ты опытный веб-дизайнер и фронтенд-разработчик. Сделай адаптивный лендинг для ниши «${n.name}» (${n.full}) в стиле «${s.name}».

Стиль: ${s.rules}.
Базовая палитра стиля: ${s.pal}. Акцентный цвет бренда: ${c} — используй его для кнопок, ссылок и ключевых акцентов, проверь контраст текста на нём (WCAG AA).
Шрифты: ${s.fonts}, с кириллицей, подключить локально.

Структура блоков:
${n.blocks.split('; ').map((b,i)=>(i+1)+'. '+b.charAt(0).toUpperCase()+b.slice(1)).join('\n')}

Тексты пиши на русском, конкретно и без воды, не выдумывай цифры, рейтинги и отзывы — ставь понятные заглушки в [квадратных скобках]. Mobile-first, семантичный HTML5, без внешних CDN, форма с согласием на обработку персональных данных (152-ФЗ). Выдай один файл index.html со встроенными CSS и JS.`};[gn,gs,gc].forEach(x=>x.oninput=g);g()}
