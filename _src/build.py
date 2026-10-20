import json,os,html
B="/dizain-prompty"; SITE="https://ztim2008.github.io"+B
S=[
dict(slug="claymorphism",name="Claymorphism",ru="Клейморфизм — мягкий «пластилиновый» объём",
 desc="Пухлые формы, большие скругления, двойные мягкие тени и пастельные цвета. Интерфейс выглядит как игрушка из пластилина.",
 when="Детские и семейные сервисы, бытовые услуги, приложения, лендинги с дружелюбным тоном.",
 pal=[("#F4EEFF","фон"),("#7C5CFF","акцент"),("#FFB86B","второй акцент"),("#2B2140","текст")],
 fonts="Nunito, Manrope, Montserrat Alternates (все с кириллицей)",
 rules="фон #F4EEFF; карточки с border-radius 28–36px, фон светлее фона, двойная тень: внешняя мягкая снизу-справа (rgba(124,92,255,.25)) и внутренняя светлая сверху-слева; кнопки «надутые», с inset-тенью и лёгким увеличением при наведении; шрифт Nunito 800 для заголовков; иконки объёмные, пастельные"),
dict(slug="neo-brutalism",name="Neo-brutalism",ru="Необрутализм — смело, контрастно, с толстой обводкой",
 desc="Толстые чёрные рамки, жёсткие смещённые тени без размытия, кислотные плоские цвета и крупная типографика.",
 when="Стартапы, креативные агентства, молодёжные бренды, продукты, которым нужно выделиться.",
 pal=[("#FFF4D6","фон"),("#FF5C8A","акцент"),("#3DDC97","второй акцент"),("#111111","обводка/текст")],
 fonts="Unbounded, Rubik, Space Grotesk (кириллица есть у Unbounded и Rubik)",
 rules="рамки 3px solid #111; тени box-shadow 6px 6px 0 #111 без размытия; скругления 0–12px; плоские яркие заливки; при наведении кнопка смещается на тень (translate 3px,3px); заголовки Unbounded 800 крупно, капс допустим"),
dict(slug="glassmorphism",name="Glassmorphism",ru="Гласморфизм — матовое стекло поверх градиента",
 desc="Полупрозрачные панели с размытием фона, тонкой светлой рамкой и яркими градиентными пятнами позади.",
 when="Финтех, SaaS-дашборды, музыкальные и IT-продукты, премиальные лендинги.",
 pal=[("#0F1B4C","фон"),("#7F5AF0","пятно 1"),("#2CB1FF","пятно 2"),("#FFFFFF","текст/стекло")],
 fonts="Inter, Manrope, Golos Text",
 rules="фон тёмно-синий с 2–3 размытыми градиентными кругами; панели background rgba(255,255,255,.12), backdrop-filter blur(16px), border 1px rgba(255,255,255,.3), radius 20px; текст белый; кнопка — светлое стекло или градиент; соблюдать контраст текста не ниже 4.5:1"),
dict(slug="swiss-minimalizm",name="Swiss / минимализм",ru="Швейцарский стиль — сетка, воздух и типографика",
 desc="Строгая модульная сетка, много белого пространства, одна акцентная краска и крупный гротеск.",
 when="Архитектура, юристы, консалтинг, B2B, портфолио, медицина премиум-класса.",
 pal=[("#FFFFFF","фон"),("#E30613","акцент"),("#111111","текст"),("#EDEDED","линии")],
 fonts="Golos Text, Inter, PT Sans, IBM Plex Sans",
 rules="12-колоночная сетка, выравнивание по левому краю; заголовки 56–96px, жирный гротеск, плотный межстрочный; тонкие линии 1px вместо теней; один акцентный красный; без скруглений или 2px; фото чёрно-белые или без фото"),
dict(slug="bento-grid",name="Bento grid",ru="Бенто-сетка — плитки разного размера",
 desc="Контент разложен по прямоугольным плиткам разного размера, как в коробке бенто. Каждая плитка — одна мысль.",
 when="Продуктовые лендинги, презентация возможностей, личные сайты, SaaS.",
 pal=[("#F5F5F7","фон"),("#1D1D1F","текст"),("#0A84FF","акцент"),("#FFD60A","плитка-акцент")],
 fonts="Inter, Manrope, Onest",
 rules="CSS grid с плитками 1x1, 2x1, 1x2, 2x2; gap 16px; radius 24px; плитки белые на светло-сером фоне, 1–2 плитки цветные; в каждой плитке заголовок, короткий факт или цифра и иконка/визуал; на мобильном одна колонка"),
dict(slug="dark-tech-neon",name="Dark tech / неон",ru="Тёмный тех-стиль с неоновым свечением",
 desc="Почти чёрный фон, неоновые акценты со свечением, моноширинные подписи и ощущение кода или киберпанка.",
 when="IT, ИИ-продукты, геймдев, крипто, кибербезопасность, ночные заведения.",
 pal=[("#07080D","фон"),("#00F5D4","неон 1"),("#F15BB5","неон 2"),("#C9D1E0","текст")],
 fonts="JetBrains Mono, Onest, Unbounded",
 rules="фон #07080D с тонкой сеткой или шумом; акценты с text-shadow/box-shadow свечением 0 0 20px цвета; рамки 1px полупрозрачные неоновые; подписи и метки моноширинным шрифтом; кнопка с неоновой обводкой и заливкой при наведении; анимации плавные, уважать prefers-reduced-motion"),
]
# preview CSS per style (scoped .pv-<slug>)
PV={
"claymorphism":""".pv{background:#F4EEFF;color:#2B2140;font-family:Nunito,'Trebuchet MS',system-ui,sans-serif}
.pv .card,.pv .hero{background:#FBF8FF;border-radius:32px;box-shadow:12px 12px 24px rgba(124,92,255,.22),-8px -8px 18px #fff,inset 2px 2px 6px #fff}
.pv h3{font-weight:900}.pv .btn{background:#7C5CFF;color:#fff;border-radius:999px;box-shadow:inset -3px -4px 8px rgba(0,0,0,.18),inset 3px 3px 8px rgba(255,255,255,.45),6px 8px 16px rgba(124,92,255,.35)}
.pv .card:nth-child(2) .ic{background:#FFB86B}.pv .ic{background:#7C5CFF;border-radius:16px}""",
"neo-brutalism":""".pv{background:#FFF4D6;color:#111;font-family:'Arial Black',Impact,system-ui,sans-serif}
.pv .card,.pv .hero{background:#fff;border:3px solid #111;box-shadow:6px 6px 0 #111;border-radius:8px}
.pv .hero{background:#3DDC97}.pv h3{text-transform:uppercase}.pv .btn{background:#FF5C8A;color:#111;border:3px solid #111;box-shadow:4px 4px 0 #111;border-radius:6px}
.pv .ic{background:#FF5C8A;border:3px solid #111}""",
"glassmorphism":""".pv{color:#fff;font-family:system-ui,sans-serif;background:radial-gradient(circle at 15% 20%,#7F5AF0 0,transparent 40%),radial-gradient(circle at 85% 80%,#2CB1FF 0,transparent 40%),#0F1B4C}
.pv .card,.pv .hero{background:rgba(255,255,255,.12);backdrop-filter:blur(14px);-webkit-backdrop-filter:blur(14px);border:1px solid rgba(255,255,255,.3);border-radius:20px}
.pv .btn{background:linear-gradient(90deg,#7F5AF0,#2CB1FF);color:#fff;border-radius:12px}.pv .ic{background:rgba(255,255,255,.35);border-radius:50%}""",
"swiss-minimalizm":""".pv{background:#fff;color:#111;font-family:Helvetica,Arial,system-ui,sans-serif}
.pv .hero{border-top:6px solid #E30613;border-radius:0;padding-left:0}.pv .hero h3{font-size:2em;letter-spacing:-.03em;line-height:1}
.pv .card{border-top:1px solid #111;border-radius:0}.pv .btn{background:#111;color:#fff;border-radius:0}.pv .ic{background:#E30613;border-radius:0}""",
"bento-grid":""".pv{background:#F5F5F7;color:#1D1D1F;font-family:system-ui,sans-serif}
.pv .card,.pv .hero{background:#fff;border-radius:24px}.pv .cards{grid-template-columns:2fr 1fr 1fr}.pv .card:nth-child(1){background:#FFD60A}
.pv .btn{background:#0A84FF;color:#fff;border-radius:999px}.pv .ic{background:#0A84FF;border-radius:10px}""",
"dark-tech-neon":""".pv{background:#07080D;color:#C9D1E0;font-family:ui-monospace,'JetBrains Mono',Consolas,monospace;background-image:linear-gradient(rgba(0,245,212,.06) 1px,transparent 1px),linear-gradient(90deg,rgba(0,245,212,.06) 1px,transparent 1px);background-size:24px 24px}
.pv .card,.pv .hero{background:rgba(7,8,13,.8);border:1px solid rgba(0,245,212,.4);border-radius:10px;box-shadow:0 0 18px rgba(0,245,212,.15)}
.pv h3{color:#00F5D4;text-shadow:0 0 12px rgba(0,245,212,.7)}.pv .btn{background:transparent;color:#F15BB5;border:1px solid #F15BB5;box-shadow:0 0 14px rgba(241,91,181,.5);border-radius:8px}.pv .ic{background:#F15BB5;box-shadow:0 0 12px #F15BB5;border-radius:4px}""",
}
PVBASE=""".pv{padding:18px;border-radius:18px;overflow:hidden}.pv .hero{padding:22px;margin-bottom:14px}.pv h3{margin:0 0 6px;font-size:1.5em}.pv p{margin:0 0 14px;opacity:.85}
.pv .btn{display:inline-block;padding:10px 18px;font-weight:700;text-decoration:none;border:0;cursor:pointer;font:inherit;font-weight:700}
.pv .cards{display:grid;grid-template-columns:repeat(3,1fr);gap:14px}.pv .card{padding:14px}.pv .ic{width:32px;height:32px;margin-bottom:8px}.pv b{display:block}.pv small{opacity:.75}
@media(max-width:560px){.pv .cards{grid-template-columns:1fr!important}}"""
def scope(css,slug): return css.replace(".pv",".pv-"+slug)
def preview(slug,mini=False):
    if mini:
        return f'<div class="pv pv-{slug} mini" aria-hidden="true"><div class="hero"><h3>Заголовок</h3><span class="btn">Кнопка</span></div><div class="cards"><div class="card"><div class="ic"></div></div><div class="card"><div class="ic"></div></div><div class="card"><div class="ic"></div></div></div></div>'
    return f'''<div class="pv pv-{slug}"><div class="hero"><h3>Баня на дровах за городом</h3><p>Парная, купель и чан. Бронь онлайн за 1 минуту.</p><button class="btn" type="button">Забронировать</button></div>
<div class="cards"><div class="card"><div class="ic"></div><b>Парная</b><small>до 8 гостей</small></div><div class="card"><div class="ic"></div><b>Купель</b><small>ледяная вода</small></div><div class="card"><div class="ic"></div><b>Чан</b><small>с травами</small></div></div></div>'''
def prompts(s):
    pal=", ".join(f"{h} ({n})" for h,n in s["pal"])
    u=f"""Ты опытный веб-дизайнер и фронтенд-разработчик. Сверстай адаптивный лендинг в стиле «{s['name']}».

Стиль: {s['desc']}
Палитра: {pal}.
Шрифты: {s['fonts']}. Подключи шрифты локально (woff2) с поддержкой кириллицы.
Правила стиля: {s['rules']}.

Структура страницы:
1. Шапка: логотип, меню из 4 пунктов, кнопка действия.
2. Первый экран: заголовок H1 до 8 слов, подзаголовок, основная и вторичная кнопки, визуал.
3. Преимущества: 3–6 карточек с иконкой, заголовком и одной строкой текста.
4. Услуги или тарифы с ценами.
5. Отзывы или кейсы.
6. Частые вопросы (аккордеон).
7. Форма заявки: имя, телефон, согласие на обработку персональных данных (152-ФЗ).
8. Подвал с контактами.

Требования: семантичный HTML5, mobile-first, контраст по WCAG AA, состояния :hover и :focus-visible, без внешних CDN, все тексты на русском. Выдай один файл index.html со встроенными CSS и JS."""
    t=f"""Сделай код для HTML-блока Тильды (блок T123) в стиле «{s['name']}».

Палитра: {pal}. Шрифты: {s['fonts']} (если шрифта нет в Тильде, используй системный аналог).
Правила стиля: {s['rules']}.

Ограничения Тильды:
- весь CSS внутри <style>, все классы с префиксом .dp- чтобы не конфликтовать со стилями Тильды;
- не используй глобальные селекторы body, html, *, h1;
- JS только чистый, внутри <script>, обёрнутый в IIFE;
- ширина блока 100%, контент по центру до 1200px; адаптив под 980, 640 и 480px;
- ссылки на кнопках оставь как # с комментарием, куда подставить попап Тильды (#popup:form).

Блок: первый экран с заголовком, подзаголовком, кнопкой и тремя карточками преимуществ. Тексты на русском."""
    f=f"""Создай в Figma дизайн лендинга в стиле «{s['name']}» (десктоп 1440 и мобайл 390).

1. Сначала заведи Local Styles: цвета {pal}; текстовые стили H1/H2/H3/Body/Caption на шрифтах {s['fonts']}.
2. Эффекты: {s['rules']}.
3. Сетка: 12 колонок, поля 120 px на десктопе; 4 колонки, поля 16 px на мобайле.
4. Компоненты с вариантами: Button (primary/secondary, default/hover/disabled), Card, Input, Header.
5. Все фреймы на Auto Layout, отступы кратны 8.
6. Экраны: первый экран, преимущества, услуги с ценами, отзывы, FAQ, форма, подвал.
Тексты на русском, без lorem ipsum."""
    return [("Универсальный",u),("Для Тильды (HTML-блок)",t),("Для Figma",f)]
NICHES={"banya":("Баня","загородная баня / банный комплекс","Первый экран с фото парной и кнопкой «Забронировать»; виды парных и вместимость; цены за час с минимальным временем; доп. услуги (веники, чан, купель, парильщик); галерея; правила и как добраться (карта); отзывы; онлайн-бронь с датой и временем; FAQ"),
"stoma":("Стоматология","стоматологическая клиника","Первый экран с УТП и записью; услуги с ценами «от» (лечение, имплантация, брекеты, гигиена); врачи с опытом и фото; лицензия и оборудование; акции; до/после (с согласия пациентов); отзывы; форма записи; адрес и часы работы. Не обещать результат лечения, учесть требования к рекламе медуслуг"),
"kotly":("Ремонт котлов","ремонт и обслуживание газовых котлов","Первый экран «выезд мастера сегодня» с телефоном и кнопкой звонка; бренды котлов; неисправности и цены «от»; как мы работаем по шагам; гарантия; мастера; отзывы; районы выезда; форма «опишите проблему»; плавающая кнопка звонка/мессенджера на мобильном"),
"shop":("Интернет-магазин","интернет-магазин","Шапка с поиском, корзиной и каталогом; баннер-акция; категории плитками; хиты продаж (карточки: фото, цена, старая цена, кнопка «В корзину»); преимущества (доставка, оплата, возврат); отзывы; подписка; подвал с реквизитами и офертой"),
"mp":("Карточки Ozon/WB","инфографика для карточек Ozon и Wildberries","Слайды карточки 900x1200 (3:4): 1) главное фото товара + УТП крупно до 5 слов; 2) 3–4 ключевых преимущества с иконками; 3) размеры/габариты; 4) состав и материал; 5) сценарии использования; 6) комплектация; 7) сравнение с аналогом без упоминания брендов. Текст крупный, читаемый на телефоне, не больше 7 строк на слайд, соблюдать правила площадок (без контактов и ссылок)"),
"coffee":("Кофейня","кофейня","Первый экран с атмосферным фото и кнопкой «Меню»; меню с ценами по категориям; зёрна и обжарщик; завтраки; фото интерьера; бронь столика или предзаказ; программа лояльности; адрес на карте и часы; отзывы")}
CSS=open("src.css").read()
def page(path,title,desc,body,extra_css="",ld=None):
    url=SITE+path
    ldj=f'<script type="application/ld+json">{json.dumps(ld,ensure_ascii=False)}</script>' if ld else ""
    return f'''<!doctype html><html lang="ru"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title><meta name="description" content="{desc}"><link rel="canonical" href="{url}">
<meta property="og:type" content="website"><meta property="og:title" content="{title}"><meta property="og:description" content="{desc}"><meta property="og:url" content="{url}"><meta property="og:locale" content="ru_RU"><meta property="og:image" content="{SITE}/og.png">
<link rel="icon" href="{B}/favicon.svg" type="image/svg+xml"><style>{CSS}{PVBASE}{extra_css}</style>{ldj}</head><body>
<header class="top"><div class="wrap nav"><a class="logo" href="{B}/"><span>◆</span> Дизайн-промпты</a><nav><a href="{B}/#stili">Стили</a><a href="{B}/#generator">Генератор</a></nav></div></header>
<main>{body}</main><footer class="foot"><div class="wrap">© 2026 Дизайн-промпты · готовые промпты для нейросетей на русском</div></footer>
<script>{open("src.js").read()}</script></body></html>'''
allcss="".join(scope(PV[s["slug"]],s["slug"]) for s in S)
os.makedirs("dist",exist_ok=True)
cards="".join(f'''<a class="scard" href="{B}/stil/{s['slug']}/" data-q="{html.escape((s['name']+' '+s['ru']+' '+s['when']).lower())}">{preview(s['slug'],True)}<h3>{s['name']}</h3><p>{s['when']}</p></a>''' for s in S)
gen_data={"styles":{s["slug"]:dict(name=s["name"],rules=s["rules"],fonts=s["fonts"],pal=", ".join(f"{h} ({n})" for h,n in s["pal"])) for s in S},"niches":{k:dict(name=v[0],full=v[1],blocks=v[2]) for k,v in NICHES.items()}}
opt=lambda d:"".join(f'<option value="{k}">{v}</option>' for k,v in d)
home=f'''<section class="hero wrap"><p class="kicker">Каталог стилей · промпты на русском</p><h1>Готовые промпты для нейросетей: сайт в нужном стиле за минуту</h1>
<p class="lead">Выберите стиль, посмотрите живое превью и скопируйте подробный промпт. Подходит для Cursor, Claude, GigaChat, YandexGPT, Bolt, Lovable, а также Тильды и Figma.</p>
<div class="tools">{"".join(f"<span>{t}</span>" for t in ["Cursor","Claude","GigaChat","YandexGPT","Bolt","Lovable","Тильда","Figma"])}</div></section>
<section id="stili" class="wrap"><div class="sechead"><h2>Стили</h2><input id="q" type="search" placeholder="Поиск: стекло, тёмный, B2B…" aria-label="Поиск стилей"></div>
<div class="chips" id="chips"><button class="on" data-f="">Все</button><button data-f="светл">Светлые</button><button data-f="тёмн">Тёмные</button><button data-f="b2b">B2B</button><button data-f="it">IT</button></div>
<div class="grid" id="grid">{cards}</div><p id="empty" hidden>Ничего не нашлось.</p></section>
<section id="generator" class="wrap gen"><h2>Генератор промпта</h2><p>Ниша + стиль + акцентный цвет → один промпт со структурой блоков.</p>
<div class="genrow"><label>Ниша<select id="gn">{opt((k,v[0]) for k,v in NICHES.items())}</select></label><label>Стиль<select id="gs">{opt((s["slug"],s["name"]) for s in S)}</select></label><label>Акцент<input id="gc" type="color" value="#7c5cff"></label></div>
<div class="pbox"><button class="copy" data-t="gout">Скопировать</button><pre id="gout"></pre></div>
<script>window.GEN={json.dumps(gen_data,ensure_ascii=False)}</script></section>'''
# tag hints for filter
light={"claymorphism","neo-brutalism","swiss-minimalizm","bento-grid"}
for s in S:
    s["tags"]=("светл" if s["slug"] in light else "тёмн")
home=home.replace('data-q="','data-q="',1)
for s in S:
    home=home.replace(f'href="{B}/stil/{s["slug"]}/" data-q="',f'href="{B}/stil/{s["slug"]}/" data-q="{s["tags"]} ')
open("dist/index.html","w").write(page("/","Дизайн-промпты — готовые промпты для нейросетей по стилям дизайна","Каталог стилей дизайна с живым превью и готовыми промптами на русском для Cursor, Claude, GigaChat, YandexGPT, Тильды и Figma. Генератор промпта под нишу.",home,allcss,
 {"@context":"https://schema.org","@type":"WebSite","name":"Дизайн-промпты","url":SITE+"/","inLanguage":"ru"}))
for s in S:
    ps=prompts(s)
    tabs="".join(f'<button role="tab" class="{"on" if i==0 else ""}" data-tab="p{i}">{n}</button>' for i,(n,_) in enumerate(ps))
    panes="".join(f'<div class="pbox" id="w{i}" {"" if i==0 else "hidden"}><button class="copy" data-t="p{i}">Скопировать</button><pre id="p{i}">{html.escape(t)}</pre></div>' for i,(_,t) in enumerate(ps))
    sw="".join(f'<li><span style="background:{h}"></span><code>{h}</code> {n}</li>' for h,n in s["pal"])
    body=f'''<article class="wrap style"><nav class="crumbs"><a href="{B}/">Главная</a> / <a href="{B}/#stili">Стили</a> / {s['name']}</nav>
<h1>Стиль {s['name']}: промпт и живой пример</h1><p class="lead">{s['ru']}. {s['desc']}</p>
<div class="two"><div><h2>Превью</h2>{preview(s['slug'])}</div><div class="info"><h2>Когда подходит</h2><p>{s['when']}</p><h2>Палитра</h2><ul class="sw">{sw}</ul><h2>Шрифты с кириллицей</h2><p>{s['fonts']}</p></div></div>
<h2>Промпт</h2><div class="tabs" role="tablist">{tabs}</div>{panes}
<p class="next">Другие стили: {" · ".join(f'<a href="{B}/stil/{o["slug"]}/">{o["name"]}</a>' for o in S if o is not s)}</p></article>'''
    d=f"dist/stil/{s['slug']}"; os.makedirs(d,exist_ok=True)
    open(d+"/index.html","w").write(page(f"/stil/{s['slug']}/",f"Стиль {s['name']} для сайта — промпт для нейросети и пример | Дизайн-промпты",f"{s['desc']} Палитра, шрифты с кириллицей и готовый промпт на русском для Cursor, Claude, Тильды и Figma.",body,scope(PV[s['slug']],s['slug']),
     {"@context":"https://schema.org","@type":"HowTo","name":f"Как сделать сайт в стиле {s['name']} с помощью нейросети","inLanguage":"ru","step":[{"@type":"HowToStep","text":"Скопируйте промпт"},{"@type":"HowToStep","text":"Вставьте его в нейросеть (Cursor, Claude, GigaChat и др.)"},{"@type":"HowToStep","text":"Замените тексты на свои и опубликуйте"}]}))
urls=["/"]+[f"/stil/{s['slug']}/" for s in S]
open("dist/sitemap.xml","w").write('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+"".join(f"<url><loc>{SITE}{u}</loc><lastmod>2026-10-20</lastmod></url>" for u in urls)+"</urlset>")
open("dist/robots.txt","w").write(f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n")
open("dist/favicon.svg","w").write('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect width="32" height="32" rx="8" fill="#5b3df5"/><path d="M16 6l10 10-10 10L6 16z" fill="#fff"/></svg>')
open("dist/404.html","w").write(page("/404.html","Страница не найдена — Дизайн-промпты","Страница не найдена",f'<section class="wrap hero"><h1>Страница не найдена</h1><p><a href="{B}/">На главную</a></p></section>'))
open("dist/.nojekyll","w").write("")
