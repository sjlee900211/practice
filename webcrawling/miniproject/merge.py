# 크롤링 결과가 담긴 엑셀 파일 통합하기
import pandas as pd
excel_names = ['C:/Users/Celine/practice/webcrawling/miniproject/files/melon.xlsx', 'C:/Users/Celine/practice/webcrawling/miniproject/files/bugs.xlsx', 'C:/Users/Celine/practice/webcrawling/miniproject/files/genie.xlsx']
appended_data = pd.DataFrame()
for name in excel_names:
    pd_data = pd.read_excel(name)
    appended_data = appended_data.append(pd_data)

# 크롤링 결과 확인하기
appended_data.info()

# 통합한 크롤링 결과를 엑셀 파일로 저장
appended_data.to_excel('C:/Users/Celine/practice/webcrawling/miniproject/files/total.xlsx', index=False)

