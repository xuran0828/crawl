import requests
from lxml import etree

def get_page(i):
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Connection': 'keep-alive',
        'Cookie': 'kztoken=nJail6zJp6iXaJqWl3BlYGFwaZaV; his=a%3A10%3A%7Bi%3A0%3Bs%3A28%3A%22nJail6zJp6iXaJqWl3BlYGFwZZOW%22%3Bi%3A1%3Bs%3A28%3A%22nJail6zJp6iXaJqWl3BlYGFwZZyU%22%3Bi%3A2%3Bs%3A28%3A%22nJail6zJp6iXaJqWl3BlYGFwZpSZ%22%3Bi%3A3%3Bs%3A28%3A%22nJail6zJp6iXaJqWl3BlYGFwZpya%22%3Bi%3A4%3Bs%3A28%3A%22nJail6zJp6iXaJqWl3BlYGFwZ5OT%22%3Bi%3A5%3Bs%3A28%3A%22nJail6zJp6iXaJqWl3BlYGFwZ5mY%22%3Bi%3A6%3Bs%3A28%3A%22nJail6zJp6iXaJqWl3BlYGFwaJSS%22%3Bi%3A7%3Bs%3A28%3A%22nJail6zJp6iXaJqWl3BlYGFwaJWU%22%3Bi%3A8%3Bs%3A28%3A%22nJail6zJp6iXaJqWl3BlYGFwaJiY%22%3Bi%3A9%3Bs%3A28%3A%22nJail6zJp6iXaJqWl3BlYGFwaZaV%22%3B%7D; acw_tc=707c9f9415730082259622365e4f58ea115862da5acc46bff21259d9f0c8ef; think_language=zh-CN; PHPSESSID=lrar70jh1ig5gt3jpsj6lne304; hmap_show=true; _ga=GA1.2.1853614770.1573008278; _gid=GA1.2.10628983.1573008278; Hm_lvt_65968db3ac154c3089d7f9a4cbb98c94=1573008278; linchuangshiyan_show=true; kztoken=nJail6zJp6iXaJqWl3BlYGFwaZiS; his=a%3A10%3A%7Bi%3A0%3Bs%3A28%3A%22nJail6zJp6iXaJqWl3BlYGFwZZyU%22%3Bi%3A1%3Bs%3A28%3A%22nJail6zJp6iXaJqWl3BlYGFwZpSZ%22%3Bi%3A2%3Bs%3A28%3A%22nJail6zJp6iXaJqWl3BlYGFwZpya%22%3Bi%3A3%3Bs%3A28%3A%22nJail6zJp6iXaJqWl3BlYGFwZ5OT%22%3Bi%3A4%3Bs%3A28%3A%22nJail6zJp6iXaJqWl3BlYGFwZ5mY%22%3Bi%3A5%3Bs%3A28%3A%22nJail6zJp6iXaJqWl3BlYGFwaJSS%22%3Bi%3A6%3Bs%3A28%3A%22nJail6zJp6iXaJqWl3BlYGFwaJWU%22%3Bi%3A7%3Bs%3A28%3A%22nJail6zJp6iXaJqWl3BlYGFwaJiY%22%3Bi%3A8%3Bs%3A28%3A%22nJail6zJp6iXaJqWl3BlYGFwaZaV%22%3Bi%3A9%3Bs%3A28%3A%22nJail6zJp6iXaJqWl3BlYGFwaZiS%22%3B%7D; Hm_lpvt_65968db3ac154c3089d7f9a4cbb98c94=1573008898',
        'Host': 'db.yaozh.com',
        'Referer': 'https://db.yaozh.com/hmap',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'
    }
    url = 'https://db.yaozh.com/hmap/{}.html'.format(str(i))
    response = requests.get(url=url, headers=headers)
    if response.status_code == 200:
        return response.content
    else:
        return None
def get_parse(html):
    data={}
    items=etree.HTML(html)
    # hosp_name=items.xpath('//tr[1]/td/span/text()')
    # print(hosp_name)
    # if items.xpath('//tr[2]/th[@class="detail-table-th"]'):
    #     hosp_alias=items.xpath('//tr[2]/td/span/text()')
    #     print(hosp_alias)
    # else:
    #     hosp_grade=items.xpath('//tr[2]/td/span/text()')
    #     print(hosp_grade)
    # # hosp_alias=items.xpath('//tr[2]/td/span/text()')
    # # if hosp_alias:
    # #     print(hosp_alias)
    # # else:
    # #     return None
    # hosp_grade=items.xpath('//tr[3]/td/span/text()')
    # print(hosp_grade)
    # hosp_type=items.xpath('//tr[4]/td/span/text()')
    # print(hosp_type)
    # hops_pr=items.xpath('//tr[10]/td/span/text()')
    # print(hops_pr)
    # hosp_city=items.xpath('//tr[11]/td/span/text()')
    # print(hosp_city)
    # hosp_addr = items.xpath('//tr[18]/td/span/text()')
    # print(hosp_addr)
    # hosp_web = items.xpath('//tr[20]/td/span/a/@href')
    # print(hosp_web)

    for item in items.xpath('//html/body/div[5]/div[2]'):
        hosp_name=item.xpath('normalize-space(//tr[1]/td/span/text())')
        if (item.xpath('normalize-space(//table/tbody/tr[2]/th/text())')=='医院别名'):
            hosp_alias=item.xpath('normalize-space(//tr[2]/td/span/text())')
            hosp_grade = item.xpath('normalize-space(//tr[3]/td/span/text())')
            hosp_type = item.xpath('normalize-space(//tr[4]/td/span/text())')
            hosp_pr=item.xpath('normalize-space(//tr[10]/td/span/text())')
            hosp_city=item.xpath('normalize-space(//tr[11]/td/span/text())')
            hosp_addr=item.xpath('normalize-space(//tr[17]/td/span/text())')
            hosp_web=item.xpath('normalize-space(//tr[19]/td/span/a/text())')
        elif(item.xpath('normalize-space(//table/tbody/tr[4]/th/text())')=='建院年份'):
            hosp_alias=None
            hosp_grade=item.xpath('normalize-space(//tr[2]/td/span/text())')
            hosp_type=item.xpath('normalize-space(//tr[3]/td/span/text())')
            hosp_pr = item.xpath('normalize-space(//tr[9]/td/span/text())')
            hosp_city = item.xpath('normalize-space(//tr[10]/td/span/text())')
            hosp_addr = item.xpath('normalize-space(//tr[16]/td/span/text())')
            hosp_web = item.xpath('normalize-space(//tr[19]/td/span/a/text())')
        elif(item.xpath('normalize-space(//table/tbody/tr[17]/th/text())') == '邮箱'):
            hosp_alias = None
            hosp_grade = item.xpath('normalize-space(//tr[2]/td/span/text())')
            hosp_type = item.xpath('normalize-space(//tr[3]/td/span/text())')
            hosp_pr = item.xpath('normalize-space(//tr[9]/td/span/text())')
            hosp_city = item.xpath('normalize-space(//tr[10]/td/span/text())')
            hosp_addr = item.xpath('normalize-space(//tr[18]/td/span/text())')
            hosp_web = item.xpath('normalize-space(//tr[20]/td/span/a/text())')
        else:
            hosp_alias = None
            hosp_grade = item.xpath('normalize-space(//tr[2]/td/span/text())')
            hosp_type = item.xpath('normalize-space(//tr[3]/td/span/text())')
            hosp_pr = item.xpath('normalize-space(//tr[8]/td/span/text())')
            hosp_city = item.xpath('normalize-space(//tr[9]/td/span/text())')
            hosp_addr = item.xpath('normalize-space(//tr[16]/td/span/text())')
            hosp_web = item.xpath('normalize-space(//tr[19]/td/span/a/text())')
        data={
            '医院名称':hosp_name,
            '医院别名':hosp_alias,
            '医院等级':hosp_grade,
            '医院类型':hosp_type,
            '省':hosp_pr,
            '市':hosp_city,
            '医院地址':hosp_addr,
            '医院网址':hosp_web
        }
        print(data)

    # with open('hosp.txt','a+',encoding='utf-8')as file:
    #     file.write(''.join(data))

if __name__=='__main__':
    for i in range(83221,83260):
        html=get_page(i)
        get_parse(html)
