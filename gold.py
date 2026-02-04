import requests
import re

def get_price(symbol):
    url = f"https://hq.sinajs.cn/list={symbol}"
    headers = {'Referer': 'https://finance.sina.com.cn'}
    try:
        response = requests.get(url, headers=headers, timeout=10)
        data = re.search(r'"(.*)"', response.text).group(1)
        if not data: return None
        parts = data.split(',')
        # 国际金价(hf_XAU)当前价在索引 0，国内(gds_AU9999)在索引 0
        return parts[0]
    except:
        return None

if __name__ == "__main__":
    # 统一使用 gds 代码，数据更直观
    domestic = get_price("gds_AU9999")
    intl = get_price("hf_XAU")
    print(f"Domestic: {domestic}")
    print(f"International: {intl}")
