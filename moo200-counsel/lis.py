import re,sys,urllib.request,html
def get(sec):
    url=f"https://law.lis.virginia.gov/vacode/title51.1/chapter1/section{sec}/"
    r=urllib.request.Request(url,headers={"User-Agent":"Mozilla/5.0"})
    b=urllib.request.urlopen(r,timeout=30).read().decode("utf-8","replace")
    m=re.search(r'<div class="row">\s*<div class="[^"]*">(.*?)</div>\s*</div>',b,re.S)
    # fallback: take everything, strip tags
    t=b
    t=re.sub(r'(?s)<script.*?</script>','',t)
    t=re.sub(r'(?s)<style.*?</style>','',t)
    t=re.sub(r'(?s)<head.*?</head>','',t)
    t=re.sub(r'<br\s*/?>','\n',t)
    t=re.sub(r'</p>','\n\n',t)
    t=re.sub(r'<[^>]+>','',t)
    t=html.unescape(t)
    t=re.sub(r'\n{3,}','\n\n',t)
    return t
for s in sys.argv[1:]:
    open(f"lis-{s}.txt","w").write(get(s))
    print("wrote",s)
