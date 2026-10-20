import sys
from playwright.sync_api import sync_playwright
base=sys.argv[1]
with sync_playwright() as p:
    b=p.chromium.launch()
    for name,url,w,h in [("home-desktop","/",1280,800),("home-mobile","/",390,844),("style-konstruktivizm","/stil/sovetskij-konstruktivizm/",1280,800),("style-marketplace","/stil/marketplace-infografika/",1280,800)]:
        pg=b.new_page(viewport={"width":w,"height":h});errs=[];pg.on("pageerror",lambda e:errs.append(str(e)))
        r=pg.goto(base+url);pg.wait_for_load_state("networkidle");pg.screenshot(path=f"shots/{name}.png",full_page=True)
        fl=pg.evaluate("document.fonts.check('16px Unbounded')&&document.fonts.check('16px \"Russo One\"')")
        print(name,r.status,errs,"fonts",fl)
    ctx=b.new_context(permissions=["clipboard-read","clipboard-write"]);pg=ctx.new_page();pg.goto(base+"/stil/sovetskij-konstruktivizm/")
    pg.click("[data-tab=p1]");pg.click("#w1 .copy");pg.wait_for_timeout(300)
    clip=pg.evaluate("navigator.clipboard.readText()");print("copy tilda ok",clip.startswith("Сделай код для HTML-блока"),pg.inner_text("#w1 .copy"))
    pg.goto(base+"/");pg.select_option("#gn","mp");pg.select_option("#gs","y2k");pg.click("#generator .copy");pg.wait_for_timeout(300)
    print("gen copy ok","Y2K" in pg.evaluate("navigator.clipboard.readText()"))
    pg.click("text=Российский рынок >> nth=0") if False else pg.click("#chips [data-f=rus]");print("rus filter",pg.locator(".scard:visible").count())
    b.close()
