import pandas as pd
import matplotlib.pyplot as plt
#matplotlib 패키지 한글 깨짐 처리 시작
import matplotlib as mpl
mpl.rc('font', family='Malgun Gothic') #윈도우, 구글 콜랩
#mpl.rc('font', family='AppleGothic') #맥
mpl.rcParams['axes.unicode_minus'] = False #한글 폰트 사용시 마이너스 폰트 깨짐 해결
#matplotlib 패키지 한글 깨짐 처리 끝