import requests as r
anime_sites_list=[]
working_sites=[]
print("Wait....finding the best sites")
with r.session() as req:
    req.headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0'}
    resp=req.get("https://piracy.moe/api/fetch/data/englishAnimeSites")
    count=0
    for site in resp.text.split(","):
        if "siteAddresses" in site:
            anime_sites_list.append(site[18:-2])
        count+=1
    for links in anime_sites_list:
        try:
            res=req.get(links)
            if(res.status_code==200):
                working_sites.append(links)
        except:
            pass
for sites in working_sites:
    print(sites)