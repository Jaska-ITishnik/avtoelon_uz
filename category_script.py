from bs4 import BeautifulSoup
from httpx import get

html_avto = '<select class="" name="category" id="change-category-select" data-original-name="category" data-parameter-name="category" onchange="" size="10"><option value="auto.car">Yengil avtomobillar</option><option value="auto.moto">Mototexnika</option><option value="auto.water">Suv transporti</option></select>'
html_ehtiyot = '<select class="" name="category" id="change-category-select" data-original-name="category" data-parameter-name="category" onchange="" size="10"><option value="spare.parts">Ehtiyot qismlar</option><option value="spare.consumables">Moy va rasxodniklar</option><option value="spare.accessory.main">Aksessuarlar va elektronika</option><option value="spare.wheel.tire">Shinalar</option><option value="spare.wheel.disc">Disklar</option><option value="spare.carsforparts">Avtomobil ehtiyot qismlar uchun</option></select>'
html_maxsus = '<select class="" name="category" id="change-category-select" data-original-name="category" data-parameter-name="category" onchange="" size="10"><option value="auto.truck">Yuk mashinalari</option><option value="auto.bus">Avtobuslar</option><option value="auto.spec">Maxsus texnika</option><option value="spare.special.parts">Maxsus texnika ehtiyot qismlari</option><option value="service.special.rent">Maxsus texnika ijarasi</option><option value="service.special">Tijorat xizmatlari</option><option value="spare.special.tiredisc">Shinalar va disklar</option></select>'
html_tamirlash = """ <select class="" name="category" id="change-category-select" data-original-name="category" data-parameter-name="category" onchange="" size="10"><option value="service.repair">Ta'mirlash</option><option value="service.services">Xizmatlar</option><option value="service.tuning">Tyuning</option><option value="service.other">Boshqalar</option></select> """

sub = [html_avto,
       html_ehtiyot,
       html_maxsus,
       html_tamirlash]

link = 'https://avtoelon.uz/uz/a/new/?cat=service.tuning&id=5363229&uuid=7ed1f8a8-601c-4a96-a8c8-dc3e7d315a0d'
html = get(link)
soup = BeautifulSoup(html, 'html.parser')
categories_name = soup.find('select', {'id': 'change-section-select'}).find_all('option')
categories = [i.text.strip() for i in categories_name]
d = {}
for i, cat in enumerate(categories):
    soup = BeautifulSoup(sub[i], 'html.parser')
    categories_name = soup.find('select', {'id': 'change-category-select'}).find_all('option')
    d[cat] = [i.text.strip() for i in categories_name]
print(d)