from django.db import models


class News(models.Model):
    netease_reference_id = models.CharField(max_length=100, unique=True)
    title = models.CharField(max_length=255)
    source = models.CharField(max_length=255)
    sourcelink = models.URLField()
    content = models.TextField()
    netease_link = models.URLField()
    tie_channel = models.CharField(max_length=50)
    thread_id = models.CharField(max_length=100)
    board_id = models.CharField(max_length=100)

    def comment_yield_urls(self):
        i = 1
        template = "http://comment.$tie_channel.163.com/cache/newlist/$board_id/${thread_id}_${i}.html"
        while True:
            url = template.safe_substitute({
                "tie_channel": self.tie_channel,
                "board_id": self.board_id,
                "thread_id": self.thread_id,
                "i": i
                })
            yield url
            i += 1



