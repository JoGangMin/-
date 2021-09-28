from src import *
from src.Browser import cycle_products, get_product_info

move_target_page("https://dkgagu.co.kr/?ca=product&page=list&c_id=781")
waite_element("#bottom_div > tbody > tr > td > table > tbody > tr > td > table:nth-child(2) > tbody > tr > td:nth-child(1) > img")
cycle_products(get_product_info)