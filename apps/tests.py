# import json
#
# with open('fixtures/districts.json', 'r') as f:
#     regions = json.load(f)
#     for i in regions:
#         # i['pk'] = i['id']
#         # del i['id']
#         i["model"] = "apps.district"
#         # i['fields'] = {'name': i['name'], 'region_id':i["region_id"]}
#         # del i['name']
#         # del i["region_id"]
#     with open('fixtures/districts.json', 'w') as f:
#         json.dump(regions, f, indent=2)
# import json
#
# from django.utils.text import slugify
#
# with open('fixtures/districts.json', 'r') as f:
#     data = json.load(f)
#     districts = [i['fields']['name'] for i in data]
#     slugified = [slugify(d) for d in districts]
#     for k, v in enumerate(data):
#         v['fields']['slug'] = slugified[k]
#     with open("fixtures/districts.json", 'w') as f:
#         json.dump(data, f, indent=2)
