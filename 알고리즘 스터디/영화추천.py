import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from numpy import array
from ast import literal_eval
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

pd.set_option('display.max_rows', 100) # 행을 최대 100개까지 출력
pd.set_option('display.max_columns', 100) # 열을 최대 100개 까지 출력
pd.set_option('display.width', 1000) #출력 창 넓이 설정

data=pd.read_csv('tmdb_5000_movies.csv',encoding='euc-kr') #영화 정보가 담긴 엑셀파일을 불러온다

#데이터 전처리
data=data[['영화번호','제목','장르','평점','평점투표 수','인기도','키워드']] #사용할 데이터를 뽑아온다

'''
투표수가 많을 수록 많은 사람들이 평가를 했기 때문에 투표 수가 낮을 수 밖에 없다.
이러한 불공정을 처리하기 위해 weighed rating 방법을 이용한다. 참고: https://www.quora.com/How-does-IMDbs-rating-system-work
R: 개별 영화 평점
v: 개별 영화에 평점을 투표한 횟수
m: 순위안에 들어야 하는 최소 투표 (정하기 나름)
c: 전체 영화에 대한 평균 평점
투표수의 상위 90프로 이상이면 500위 안으로 들어오게 된다. 
이 코드에서는 m=500이라고 가정했다
'''

m=data['평점투표 수'].quantile(0.9)
data=data.loc[data['평점투표 수']>=m]
C=data['평점'].mean() #평점의 평균을 구한다

def weighted_rating(x,m=m,C=C):
    v=x['평점투표 수']
    R=x['평점']
    return (v/(v+m)*R)+(m/(m+v)*C)

data['추천점수']=data.apply(weighted_rating,axis=1)


data['장르']=data['장르'].apply(literal_eval) #list와와 dictionary 형태로 변경
data['키워드']=data['키워드'].apply(literal_eval)
data['장르']=data['장르'].apply(lambda x : [d['name'] for d in x]).apply(lambda x: " ".join(x)) # dict 형태 -> list 형태 -> 띄어쓰기로 이루어진 str로 변경
data['키워드']=data['키워드'].apply(lambda x : [d['name'] for d in x]).apply(lambda x: " ".join(x))


count_vector=CountVectorizer(ngram_range=(1,3))
c_vector_genres=count_vector.fit_transform(data['장르'])

gerne_c_sim=cosine_similarity(c_vector_genres,c_vector_genres).argsort()[:,::-1]    #코사인 유사도를 구한 벡터를 미리 저장

def get_recommed_movie_list(df,movie_title,top=30): #특정영화와 비슷한 영화를 추천해주는 함수
    target_movie_index=df[df['제목']==movie_title].index.values #특정 영화와 비슷한 영화를 추천해야 하기 때문에 '특정 영화' 정보를 뽑아내는 함수
    sim_index=gerne_c_sim[target_movie_index,:top].reshape(-1) # 코사인 유사도 중 비슷한 코사인 유사도를 가진 정보를 뽑아낸다
    sim_index=sim_index[sim_index!=target_movie_index] # 본인은 제외
    result=df.iloc[sim_index].sort_values('추천점수',ascending=False)[:10] #data frame 으로 만든 뒤 추천점수로 정렬 한 뒤 return
    return result



print("마음에 들었던 영화를 조건에 맞게 입력하세요:")
movie=input()
temp=get_recommed_movie_list(data,movie_title=movie)
ans=[]
ans=temp.values.tolist()
ans=array(ans)



for i in range(10):
        if i==0:
            print('%50s %40s %35s %20s %14s %20s' % ('제목','장르','평점','평점투표 수','인기도','추천 점수'))
        else:
            print('%60s %50s %20s %20s %20.4s %20.4s' % (ans[i][1],ans[i][2],ans[i][3],ans[i][4],ans[i][5],ans[i][7]))
            #ans[0]=영화번호, [1]=제목,[2]=장르,[3]=평점,[4]=평점투표 수,[5]=인기도,[6]=키워드,[7]=추천 점수