from dotenv import load_dotenv
import os
from pyairtable import Api

load_dotenv()


# print(table.all()[0]['fields']['Anime'])

class AnimeReview:

    def __init__(self):
        self.api = Api("patPQ7j4UBWhnOGAQ.7118b20ff871f854239a35d076f5f1d13eb970a1e201e2b0292d5b5b31108785")
        self.table = self.api.table('app3z413YGXNaYspL', 'tblbWDqffynJFJLoI') 



    def get_anime_ratings(self,sort="ASC",max_records=10):
        rating = ["Rating"]
        if sort=="DESC":
             rating = ["-Rating"]
        table = self.table.all(sort = rating,max_records=max_records)

        return table


    def add_anime_ratings(self,anime_title,anime_rating,remark = None):
        fields = {'Anime':anime_title,'Rating':anime_rating,'Remark':remark}
        self.table.create(fields=fields)



if __name__ == '__main__':
        ar = AnimeReview()
        # ar.add_anime_ratings('COTE',7,remark='Tryhard MC but a good anime overall!!')
        print(ar.get_anime_ratings(sort="ASC",max_records=2))
