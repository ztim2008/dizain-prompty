import re,urllib.request,os
UA={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120 Safari/537.36"}
fams=["Nunito:wght@800","Unbounded:wght@700","Manrope:wght@400;700","Inter:wght@400;700","PT+Serif:wght@400;700","JetBrains+Mono:wght@400;700","Russo+One"]
out=[]
for f in fams:
    css=urllib.request.urlopen(urllib.request.Request(f"https://fonts.googleapis.com/css2?family={f}&display=swap",headers=UA)).read().decode()
    for sub,body in re.findall(r"/\* ([\w-]+) \*/\s*(@font-face\s*{[^}]+})",css):
        if sub not in("cyrillic","latin"):continue
        fam=re.search(r"font-family: '([^']+)'",body).group(1);w=re.search(r"font-weight: (\d+)",body).group(1)
        url=re.search(r"url\((\S+?)\)",body).group(1);fn=f"{fam.replace(' ','')}-{w}-{sub}.woff2"
        if not os.path.exists("dist/fonts/"+fn): open("dist/fonts/"+fn,"wb").write(urllib.request.urlopen(url).read())
        out.append(re.sub(r"url\(\S+?\)",f"url(/dizain-prompty/fonts/{fn})",body))
open("fonts.css","w").write("\n".join(out))
print(len(out))
