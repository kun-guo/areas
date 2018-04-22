# _*_ coding: utf-8 _*_
import requests
from bs4 import BeautifulSoup
import threading
import time
import sys
import json

reload(sys)
sys.setdefaultencoding('utf-8')

base_url = "http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2016/"
dest = "E:\\data.json"
# url = "https://baidu.com"

extra = [{"name": "台湾省", "children": [{"name": "台北市", "children": [{"name": "中正区"}, {"name": "大同区"}, {"name": "中山区"}, {"name": "松山区"}, {"name": "大安区"}, {"name": "万华区"}, {"name": "信义区"}, {"name": "士林区"}, {"name": "北投区"}, {"name": "内湖区"}, {"name": "南港区"}, {"name": "文山区"}]}, {"name": "高雄市", "children": [{"name": "新兴区"}, {"name": "前金区"}, {"name": "芩雅区"}, {"name": "盐埕区"}, {"name": "鼓山区"}, {"name": "旗津区"}, {"name": "前镇区"}, {"name": "三民区"}, {"name": "左营区"}, {"name": "楠梓区"}, {"name": "小港区"}, {"name": "苓雅区"}, {"name": "仁武区"}, {"name": "大社区"}, {"name": "冈山区"}, {"name": "路竹区"}, {"name": "阿莲区"}, {"name": "田寮区"}, {"name": "燕巢区"}, {"name": "桥头区"}, {"name": "梓官区"}, {"name": "弥陀区"}, {"name": "永安区"}, {"name": "湖内区"}, {"name": "凤山区"}, {"name": "大寮区"}, {"name": "林园区"}, {"name": "鸟松区"}, {"name": "大树区"}, {"name": "旗山区"}, {"name": "美浓区"}, {"name": "六龟区"}, {"name": "内门区"}, {"name": "杉林区"}, {"name": "甲仙区"}, {"name": "桃源区"}, {"name": "那玛夏区"}, {"name": "茂林区"}, {"name": "茄萣区"}]}, {"name": "台南市", "children": [{"name": "中西区"}, {"name": "东区"}, {"name": "南区"}, {"name": "北区"}, {"name": "安平区"}, {"name": "安南区"}, {"name": "永康区"}, {"name": "归仁区"}, {"name": "新化区"}, {"name": "左镇区"}, {"name": "玉井区"}, {"name": "楠西区"}, {"name": "南化区"}, {"name": "仁德区"}, {"name": "关庙区"}, {"name": "龙崎区"}, {"name": "官田区"}, {"name": "麻豆区"}, {"name": "佳里区"}, {"name": "西港区"}, {"name": "七股区"}, {"name": "将军区"}, {"name": "学甲区"}, {"name": "北门区"}, {"name": "新营区"}, {"name": "后壁区"}, {"name": "白河区"}, {"name": "东山区"}, {"name": "六甲区"}, {"name": "下营区"}, {"name": "柳营区"}, {"name": "盐水区"}, {"name": "善化区"}, {"name": "大内区"}, {"name": "山上区"}, {"name": "新市区"}, {"name": "安定区"}]}, {"name": "台中市", "children": [{"name": "中区"}, {"name": "东区"}, {"name": "南区"}, {"name": "西区"}, {"name": "北区"}, {"name": "北屯区"}, {"name": "西屯区"}, {"name": "南屯区"}, {"name": "太平区"}, {"name": "大里区"}, {"name": "雾峰区"}, {"name": "乌日区"}, {"name": "丰原区"}, {"name": "后里区"}, {"name": "石冈区"}, {"name": "东势区"}, {"name": "和平区"}, {"name": "新社区"}, {"name": "潭子区"}, {"name": "大雅区"}, {"name": "神冈区"}, {"name": "大肚区"}, {"name": "沙鹿区"}, {"name": "龙井区"}, {"name": "梧栖区"}, {"name": "清水区"}, {"name": "大甲区"}, {"name": "外埔区"}, {"name": "大安区"}]}, {"name": "金门县", "children": [{"name": "金沙镇"}, {"name": "金湖镇"}, {"name": "金宁乡"}, {"name": "金城镇"}, {"name": "烈屿乡"}, {"name": "乌坵乡"}]}, {"name": "南投县", "children": [{"name": "南投市"}, {"name": "中寮乡"}, {"name": "草屯镇"}, {"name": "国姓乡"}, {"name": "埔里镇"}, {"name": "仁爱乡"}, {"name": "名间乡"}, {"name": "集集镇"}, {"name": "水里乡"}, {"name": "鱼池乡"}, {"name": "信义乡"}, {"name": "竹山镇"}, {"name": "鹿谷乡"}]}, {"name": "基隆市", "children": [{"name": "仁爱区"}, {"name": "信义区"}, {"name": "中正区"}, {"name": "中山区"}, {"name": "安乐区"}, {"name": "暖暖区"}, {"name": "七堵区"}]}, {"name": "新竹市", "children": [{"name": "东区"}, {"name": "北区"}, {"name": "香山区"}]}, {"name": "嘉义市", "children": [{"name": "东区"}, {"name": "西区"}]}, {"name": "新北市", "children": [{"name": "万里区"}, {"name": "金山区"}, {"name": "板桥区"}, {"name": "汐止区"}, {"name": "深坑区"}, {"name": "石碇区"}, {"name": "瑞芳区"}, {"name": "平溪区"}, {"name": "双溪区"}, {"name": "贡寮区"}, {"name": "新店区"}, {"name": "坪林区"}, {"name": "乌来区"}, {"name": "永和区"}, {"name": "中和区"}, {"name": "土城区"}, {"name": "三峡区"}, {"name": "树林区"}, {"name": "莺歌区"}, {"name": "三重区"}, {"name": "新庄区"}, {"name": "泰山区"}, {"name": "林口区"}, {"name": "芦洲区"}, {"name": "五股区"}, {"name": "八里区"}, {"name": "淡水区"}, {"name": "三芝区"}, {"name": "石门区"}]}, {"name": "宜兰县", "children": [{"name": "宜兰市"}, {"name": "头城镇"}, {"name": "礁溪乡"}, {"name": "壮围乡"}, {"name": "员山乡"}, {"name": "罗东镇"}, {"name": "三星乡"}, {"name": "大同乡"}, {"name": "五结乡"}, {"name": "冬山乡"}, {"name": "苏澳镇"}, {"name": "南澳乡"}, {"name": "钓鱼台"}]}, {"name": "新竹县", "children": [{"name": "竹北市"}, {"name": "湖口乡"}, {"name": "新丰乡"}, {"name": "新埔镇"}, {"name": "关西镇"}, {"name": "芎林乡"}, {"name": "宝山乡"}, {"name": "竹东镇"}, {"name": "五峰乡"}, {
    "name": "横山乡"}, {"name": "尖石乡"}, {"name": "北埔乡"}, {"name": "峨眉乡"}]}, {"name": "桃园县", "children": [{"name": "中坜市"}, {"name": "平镇市"}, {"name": "龙潭乡"}, {"name": "杨梅市"}, {"name": "新屋乡"}, {"name": "观音乡"}, {"name": "桃园市"}, {"name": "龟山乡"}, {"name": "八德市"}, {"name": "大溪镇"}, {"name": "复兴乡"}, {"name": "大园乡"}, {"name": "芦竹乡"}]}, {"name": "苗栗县", "children": [{"name": "竹南镇"}, {"name": "头份镇"}, {"name": "三湾乡"}, {"name": "南庄乡"}, {"name": "狮潭乡"}, {"name": "后龙镇"}, {"name": "通霄镇"}, {"name": "苑里镇"}, {"name": "苗栗市"}, {"name": "造桥乡"}, {"name": "头屋乡"}, {"name": "公馆乡"}, {"name": "大湖乡"}, {"name": "泰安乡"}, {"name": "铜锣乡"}, {"name": "三义乡"}, {"name": "西湖乡"}, {"name": "卓兰镇"}]}, {"name": "彰化县", "children": [{"name": "彰化市"}, {"name": "芬园乡"}, {"name": "花坛乡"}, {"name": "秀水乡"}, {"name": "鹿港镇"}, {"name": "福兴乡"}, {"name": "线西乡"}, {"name": "和美镇"}, {"name": "伸港乡"}, {"name": "员林镇"}, {"name": "社头乡"}, {"name": "永靖乡"}, {"name": "埔心乡"}, {"name": "溪湖镇"}, {"name": "大村乡"}, {"name": "埔盐乡"}, {"name": "田中镇"}, {"name": "北斗镇"}, {"name": "田尾乡"}, {"name": "埤头乡"}, {"name": "溪州乡"}, {"name": "竹塘乡"}, {"name": "二林镇"}, {"name": "大城乡"}, {"name": "芳苑乡"}, {"name": "二水乡"}]}, {"name": "嘉义县", "children": [{"name": "番路乡"}, {"name": "梅山乡"}, {"name": "竹崎乡"}, {"name": "阿里山乡"}, {"name": "中埔乡"}, {"name": "大埔乡"}, {"name": "水上乡"}, {"name": "鹿草乡"}, {"name": "太保市"}, {"name": "朴子市"}, {"name": "东石乡"}, {"name": "六脚乡"}, {"name": "新港乡"}, {"name": "民雄乡"}, {"name": "大林镇"}, {"name": "溪口乡"}, {"name": "义竹乡"}, {"name": "布袋镇"}]}, {"name": "云林县", "children": [{"name": "斗南镇"}, {"name": "大埤乡"}, {"name": "虎尾镇"}, {"name": "土库镇"}, {"name": "褒忠乡"}, {"name": "东势乡"}, {"name": "台西乡"}, {"name": "仑背乡"}, {"name": "麦寮乡"}, {"name": "斗六市"}, {"name": "林内乡"}, {"name": "古坑乡"}, {"name": "莿桐乡"}, {"name": "西螺镇"}, {"name": "二仑乡"}, {"name": "北港镇"}, {"name": "水林乡"}, {"name": "口湖乡"}, {"name": "四湖乡"}, {"name": "元长乡"}]}, {"name": "屏东县", "children": [{"name": "屏东市"}, {"name": "三地门乡"}, {"name": "雾台乡"}, {"name": "玛家乡"}, {"name": "九如乡"}, {"name": "里港乡"}, {"name": "高树乡"}, {"name": "盐埔乡"}, {"name": "长治乡"}, {"name": "麟洛乡"}, {"name": "竹田乡"}, {"name": "内埔乡"}, {"name": "万丹乡"}, {"name": "潮州镇"}, {"name": "泰武乡"}, {"name": "来义乡"}, {"name": "万峦乡"}, {"name": "崁顶乡"}, {"name": "新埤乡"}, {"name": "南州乡"}, {"name": "林边乡"}, {"name": "东港镇"}, {"name": "琉球乡"}, {"name": "佳冬乡"}, {"name": "新园乡"}, {"name": "枋寮乡"}, {"name": "枋山乡"}, {"name": "春日乡"}, {"name": "狮子乡"}, {"name": "车城乡"}, {"name": "牡丹乡"}, {"name": "恒春镇"}, {"name": "满州乡"}]}, {"name": "台东县", "children": [{"name": "台东市"}, {"name": "绿岛乡"}, {"name": "兰屿乡"}, {"name": "延平乡"}, {"name": "卑南乡"}, {"name": "鹿野乡"}, {"name": "关山镇"}, {"name": "海端乡"}, {"name": "池上乡"}, {"name": "东河乡"}, {"name": "成功镇"}, {"name": "长滨乡"}, {"name": "金峰乡"}, {"name": "大武乡"}, {"name": "达仁乡"}, {"name": "太麻里乡"}]}, {"name": "花莲县", "children": [{"name": "花莲市"}, {"name": "新城乡"}, {"name": "太鲁阁"}, {"name": "秀林乡"}, {"name": "吉安乡"}, {"name": "寿丰乡"}, {"name": "凤林镇"}, {"name": "光复乡"}, {"name": "丰滨乡"}, {"name": "瑞穗乡"}, {"name": "万荣乡"}, {"name": "玉里镇"}, {"name": "卓溪乡"}, {"name": "富里乡"}]}, {"name": "澎湖县", "children": [{"name": "马公市"}, {"name": "西屿乡"}, {"name": "望安乡"}, {"name": "七美乡"}, {"name": "白沙乡"}, {"name": "湖西乡"}]}, {"name": "连江县", "children": [{"name": "南竿乡"}, {"name": "北竿乡"}, {"name": "莒光乡"}, {"name": "东引乡"}]}]}, {"name": "香港特别行政区", "children": [{"name": "香港岛", "children": [{"name": "中西区"}, {"name": "湾仔"}, {"name": "东区"}, {"name": "南区"}]}, {"name": "九龙", "children": [{"name": "九龙城区"}, {"name": "油尖旺区"}, {"name": "深水埗区"}, {"name": "黄大仙区"}, {"name": "观塘区"}]}, {"name": "新界", "children": [{"name": "北区"}, {"name": "大埔区"}, {"name": "沙田区"}, {"name": "西贡区"}, {"name": "元朗区"}, {"name": "屯门区"}, {"name": "荃湾区"}, {"name": "葵青区"}, {"name": "离岛区"}]}]}, {"name": "澳门特别行政区", "children": [{"name": "澳门半岛", "children": []}, {"name": "离岛", "children": []}]}]

headers = {
    "Host": "www.stats.gov.cn",
    "Connection": "keep-alive",
    "Cache-Control": "max-age=0",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
    "Upgrade-Insecure-Requests": "1",
    "Content-Type": "text/html;charset=utf-8",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Cookie": "AD_RS_COOKIE=20080918; _trs_uv=jg8wz8bi_6_1rzx",
    "If-None-Match": "GZIP133f-54ec1ba6ad412",
    "If-Modified-Since": "Fri, 05 May 2017 07:20:46 GMT"
}


def fetchData():
    url = base_url + "index.html"
    r = requests.get(url=url, headers=headers)
    print r.apparent_encoding
    r.encoding = 'GB2312'
    html_doc = r.text
    # print html_doc

    sp = BeautifulSoup(html_doc, "html.parser")
    trs = sp.find_all("tr", {'class': 'provincetr'})
    # print trs

    # 行政区域数据
    datas = []

    for i in range(len(trs)):
        for td in trs[i].children:
            # 省份名
            print td
            name = td.a.get_text("", strip=True)
            city_href = td.a.get("href")

            province = {}
            province["name"] = name
            # 城市
            province["children"] = fetch_city(city_href)
            # 县区

            datas.append(province)
            pass

    datas.extend(extra)

    print "省份长度：" + str(len(datas))
    write2file(datas)

    return


def fetch_city(href):
    url = base_url + href
    # print url
    r = requests.get(url=url, headers=headers)
    r.encoding = r.apparent_encoding
    html_doc = r.text

    sp = BeautifulSoup(html_doc, "html.parser")
    trs = sp.find_all("tr", {'class': 'citytr'})
    # print trs

    # 城市数据
    cities = []
    # 提取省份
    for i in range(len(trs)):
        # 每个tr对应一个城市
        it = iter(trs[i])
        while True:
            try:
                cell_code = next(it)
                cell_name = next(it)

                if cell_code.a is None:
                    code = cell_code.get_text("", strip=True)
                else:
                    code = cell_code.a.get_text("", strip=True)
                    href = cell_code.a.get("href")

                if cell_name.a == None:
                    name = cell_name.get_text("", strip=True)
                else:
                    name = cell_name.a.get_text("", strip=True)

                city = {}
                city["name"] = name
                city["children"] = fetch_district(href)
                cities.append(city)
                # print code, name
            except StopIteration:
                break

    return cities

'''
县区数据
'''


def fetch_district(href):
    url = base_url + href
    # print url
    r = requests.get(url=url, headers=headers)
    r.encoding = r.apparent_encoding
    html_doc = r.text

    sp = BeautifulSoup(html_doc, "html.parser")
    trs = sp.find_all("tr", {'class': 'countytr'})
    # print len(trs)

    # 城市数据
    districts = []
    # 提取县区
    for i in range(len(trs)):
        it = iter(trs[i])
        while True:
            try:
                cell_code = next(it)
                cell_name = next(it)

                if cell_code.a is None:
                    code = cell_code.get_text("", strip=True)
                else:
                    code = cell_code.a.get_text("", strip=True)

                if cell_name.a == None:
                    name = cell_name.get_text("", strip=True)
                else:
                    name = cell_name.a.get_text("", strip=True)

                district = {}
                district["name"] = name
                districts.append(district)
                # print code, name
            except StopIteration:
                break

    return districts


def write2file(json_data):
    json_str = json.dumps(json_data, ensure_ascii=False)
    fp = open(dest, "w")
    fp.write(json_str)
    fp.close()
    return

'''
多线程
'''


def action(arg):
    time.sleep(1)
    print 'the arg is:%s\r' % arg


def multiThread():
    for i in range(1):
        thread = threading.Thread(target=fetchData, args=())
        thread.start()
    print "thread " + str(i) + " start"
    return

multiThread()
