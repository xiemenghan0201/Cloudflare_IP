import pandas as pd

repo = "xiemenghan0201/Cloudflare_IP"
url = f"https://raw.githubusercontent.com/{repo}/main/result.csv"

try:
    df = pd.read_csv(url)
    ips = df.iloc[:,0].dropna().astype(str).unique()

    with open("v2rayn.txt", "w") as f:
        for ip in ips:
            f.write(f"IP-CIDR,{ip},DIRECT\n")

    print("OK:", len(ips))

except Exception as e:
    print("ERROR:", e)
