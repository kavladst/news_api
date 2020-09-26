from django.db import models
from .news_scrappers.instagram_scrapper import InstagramScrapper


class News(models.Model):
    instagram_id = models.CharField(max_length=50)
    text = models.TextField()
    owner = models.CharField(max_length=20)
    publish_date = models.DateTimeField(editable=True)

    def __str__(self):
        return f'Inst_id: {self.instagram_id}, Owner: {self.owner}, Text: {self.text[:10]}'

    @staticmethod
    def load_news_from_instagram():
        instagram_users = ['bbcnews']
        curr_instagram_posts_ids = set(map(lambda x: x[0], News.objects.values_list('instagram_id')))
        for user in instagram_users:
            posts = InstagramScrapper.get_posts(user)
            if posts is None:
                continue
            for post in posts:
                post_instagram_id = post['instagram_id']
                if post_instagram_id not in curr_instagram_posts_ids:
                    News(
                        instagram_id=post_instagram_id,
                        owner=post['owner'],
                        text=post['text'],
                        publish_date=post['publish_date'],
                    ).save()
                    curr_instagram_posts_ids.add(post_instagram_id)
