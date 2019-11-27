#URL 파일 본문 제목 읽어오는 
from newspaper import Article
#크롤링할 url 주소 입력

def CU(url):
    #언어가 한국어이므로 language='ko'로 설정
    a = Article(url, language='ko')
    a.download()
    a.parse()
    #기사 제목 가져오기
    t=a.title
    sc=a.text
    return t,sc
