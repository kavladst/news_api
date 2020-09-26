import requests
from typing import List, Dict, Optional
from datetime import datetime


class InstagramScrapper:

    @staticmethod
    def get_posts(user_name: str) -> Optional[List[Dict]]:
        """
        :return: Dictionaries of posts info or None, if can't retrieve posts
        """
        response = requests.get(f'https://www.instagram.com/{user_name}/?__a=1')
        try:
            response.raise_for_status()
            posts = response.json()['graphql']['user']['edge_owner_to_timeline_media']['edges']
        except (requests.exceptions.HTTPError, KeyError):
            return None
        posts = [
            {
                'instagram_id': post['node']['id'],
                'owner': user_name,
                'text': post['node']['edge_media_to_caption']['edges'][0]['node']['text'],
                'publish_date': datetime.fromtimestamp(post['node']['taken_at_timestamp']),
            }
            for post in posts
        ]
        return posts


if __name__ == '__main__':
    print(InstagramScrapper.get_posts('bbcnews'))
