import sys
from playwright.sync_api import sync_playwright
base=sys.argv[1]
with sync_playwright() as p:
    b=p.chromium.launch()
    for name,url,w,h,full in [("home-desktop",base+"/",1280,800,True),("home-mobile",base+"/",390,844,True),("style-glassmorphism",base+"/stil/glassmorphism/",1280,800,True)]:
        pg=b.new_page(viewport={"width":w,"height":h});errs=[];pg.on("pageerror",lambda e:errs.append(str(e)))
        r=pg.goto(url);pg.wait_for_timeout(400);pg.screenshot(path=f"shots/{name}.png",full_page=full);print(name,r.status,errs)
    pg=b.new_page(viewport={"width":1200,"height":630});pg.goto(base+"/");pg.screenshot(path="dist/og.png")
    b.close()
