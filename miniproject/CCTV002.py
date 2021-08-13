import pandas as pd

SDFP = pd.read_excel('seoulPopulation.xls',
                     header= 2,
                     usecols= 'B, D, G, J, N')
                     # encoding = 'UTF-8')
SDFP.head()

# 열 이름 변경
SDFP.rename(columns={SDFP.columns[0] : '구별',
                     SDFP.columns[1]: '인구수',
                     SDFP.columns[2]: '한국인',
                     SDFP.columns[3]: '외국인',
                     SDFP.columns[4]: '고령자'}, inplace=True)
SDFP.head()

# 합계 행 삭제
SDFP.drop([0], inplace= True)
SDFP.head()

# 구별 열의 unique 정보 확인
SDFP['구별'].unique()

# NaN정보 확인
SDFP[SDFP['구별'].isnull()]

SDFP.tail()

# NaN행 삭제
SDFP.drop([26], inplace=True)
SDFP.tail()

# 외국인비율과 고령자비율 열을 계산 후 추가
SDFP['외국인비율'] = SDFP['외국인'] / SDFP['인구수'] * 100
SDFP['고령자비율'] = SDFP['고령자'] / SDFP['인구수'] * 100

SDFP.head()

# 인구수 내림차순 정렬
SDFP.sort_values(by = '인구수', ascending=False).head(7)

# 외국인 내림차순 정렬
SDFP.sort_values(by='외국인', ascending=False).head(7)

# 외국인비율 내림차순 정렬
SDFP.sort_values(by= '외국인비율', ascending=False).head(7)

# 고령자 내림차순 정렬
SDFP.sort_values(by='고령자', ascending=False).head(7)

# 고령자비율 내림차순 정렬
SDFP.sort_values(by='고령자비율', ascending=False).head(7)