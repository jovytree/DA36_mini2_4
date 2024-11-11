import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import sys
sys.path.append('C:\\Workspaces\\DA36-mini-4\\test2_mini2')

from menu1 import *
from menu2 import *
from menu3 import *
from menu4 import *
from menu5 import *
from intro import *
import functions as fun

# fun.data_load()

fun.pickle_load()

# df = fun.sephora_df
intro = st.Page("intro.py", title ='HOME', icon=":material/home:")
menu1_page = st.Page("menu1.py", title="좋아요❤️ TOP3", icon=":material/search:")
menu2_page = st.Page("menu2.py", title="브랜드별 TOP3👑", icon=":material/search:")
menu3_page = st.Page("menu3.py", title="리뷰 & 평점", icon=":material/favorite:")
menu4_page = st.Page("menu4.py", title="화장품 추천 1", icon=":material/star:")
menu5_page = st.Page("menu5.py", title="화장품 추천 2", icon=":material/star:")


# pg = st.navigation([manu0_page, manu1_page, manu2_page, manu3_page])
pg = st.navigation([intro, menu1_page, menu2_page, menu3_page, menu4_page, menu5_page])
pg.run()
