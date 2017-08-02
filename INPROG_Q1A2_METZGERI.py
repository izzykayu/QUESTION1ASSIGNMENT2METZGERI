from datetime import datetime
from functools import reduce
import csv
import pprint
import operator


def taxon_date_items(list1):
    return [list1[1], list1[22]]


def map_dict(lis):
    data = dict(zip(taxon_name_keys, lis))
    return data

# def filter_func(dict):
#     for dict in mapped_results:
#         if key == 'date':
#             start_date = datetime.strptime(date, '2010:06:{}:{}:{}:{}')
#             end_date = datetime.strptime(date, '2010:09:{}:{}:{}:{}')
#             return start_date <= date <= end_date


with open('cleaned_GPMDB_table.tsv', 'r') as tsvfile:
    tsv_reader = csv.reader(tsvfile, delimiter='\t', quotechar='"')
    keys_list = list(next(tsv_reader))  # keys list are headings
    list_values = list([line.rstrip().split('\t') for line in tsvfile])


# print(len(list_values))     # 324217 rows
taxon_name_keys = taxon_date_items(keys_list)
# print(taxon_name_keys)    ['date', 'taxon']
mapped_list_values = list(map(taxon_date_items, list_values))
mapped_list_dictionaries = list(map(map_dict, mapped_list_values))
pprint.pprint(mapped_list_dictionaries[0:2])
print(len(mapped_list_dictionaries))


# list_fil = list(filter(lambda x: datetime.strptime(2010:06,  '2010:06:{}:{}:{}:{}') <= x < datetime.strptime(2010, 10, '2010:10:{}:{}:{}:{}'), list_important))
# print(list_fil)
# #mapped_list = list(map(lambda x: x**2, list_values))]
             #mapped_dict = dict(map
        #filter(lambda x['date']:  , gpmdp_list_dictionary)

    #             #fil = filter(filter_func, gpmdp_list_dictionary)

reduced_dict = {}


# def counter_fxn(list1):
#     return [v for k, v in reduced_dict.values()]
#
# map(counter_fxn, )

#results = []
#fpr ote, om ;ost:
#results.append(f(item))
#map(f, list)
#
# taxon_list_values =[d['taxon'] for d in .__getitem__() if 'taxon' in d]
#
#
# def taxon_count(a1, a2):        # a1 and a2 stand for different arguments
#     a1 = {}
#     d[a1] = [d.__setitem__(item, 1+d.get(item, 0)) for item in lis]
#     return a1


# make list for

# reduced_dict = reduce(taxon_count, list_fil, {})
# print(list(reduced_dict))
# most_common_taxon = max(reduced_dict.iteritems(), key=operator.itemgetter(1))[0]
# print('The most common taxon is', most_common_taxon)

li_dictionaries_of_taxon = list(map(lambda x: [v for k, v in x.items() if k == 'taxon'], mapped_list_dictionaries))
print(list(li_dictionaries_of_taxon[0:2]))

