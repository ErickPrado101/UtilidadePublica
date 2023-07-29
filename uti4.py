import instaloader
from datetime import datetime

def bus(pch, nct=10, ca=None):
    ld = instaloader.Instaloader()
    eps = {
        "0-1000": {"rct": [], "ant": []},
        "1001-5000": {"rct": [], "ant": []},
        "5001-10000": {"rct": [], "ant": []},
        "10001-50000": {"rct": [], "ant": []},
        "50001-100000": {"rct": [], "ant": []},
        "100001+": {"rct": [], "ant": []}
    }
    ce = []
    if ca:
        ce.extend(ca)
    pcu = " ".join(pch)
    prs = instaloader.Profile.from_username(ld.context, pcu)
    pck = ["emp", "neg", "emp", "com"]
    for pr in prs.get_followees():
        if not pr.external_url and pr.biography:
            if pr.username not in ce:
                blw = pr.biography.lower()
                if any(p in blw for p in pck):
                    sg = pr.followers
                    dcr = datetime.fromtimestamp(pr.created_time)
                    dat = datetime.now()
                    dms = (dat.year - dcr.year) * 12 + dat.month - dcr.month

                    # Coleta de informações adicionais
                    ne = pr.full_name
                    dp = pr.biography
                    np = pr.mediacount
                    ht = pr.get_popular_tags()

                    if sg <= 1000:
                        if dms <= 6:
                            eps["0-1000"]["rct"].append({
                                "usr": pr.username,
                                "ne": ne,
                                "dp": dp,
                                "ns": sg,
                                "np": np,
                                "ht": ht
                            })
                        else:
                            eps["0-1000"]["ant"].append({
                                "usr": pr.username,
                                "ne": ne,
                                "dp": dp,
                                "ns": sg,
                                "np": np,
                                "ht": ht
                            })
                    elif sg <= 5000:
                        if dms <= 6:
                            eps["1001-5000"]["rct"].append({
                                "usr": pr.username,
                                "ne": ne,
                                "dp": dp,
                                "ns": sg,
                                "np": np,
                                "ht": ht
                            })
                        else:
                            eps["1001-5000"]["ant"].append({
                                "usr": pr.username,
                                "ne": ne,
                                "dp": dp,
                                "ns": sg,
                                "np": np,
                                "ht": ht
                            })
                    # Repetir o mesmo padrão para as outras faixas de seguidores

                    ce.append(pr.username)
                    if len(ce) >= nct:
                        return eps, ce
    return eps, ce

pch = ["empresas pequenas", "negócios locais", "pequenos negócios"]
espse, cenc = bus(pch, nct=20)
print(espse)