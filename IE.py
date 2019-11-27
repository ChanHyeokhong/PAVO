#영어 사이트 읽어올 수 있는 것
from newspaper import Article
#크롤링할 url 주소 입력

def CU1(url):
    #언어가 한국어이므로 language='ko'로 설정
    a = Article(url, language='en')
    a.download()
    a.parse()
    #기사 제목 가져오기
    t=a.title
    sc=a.text
    return t,sc
