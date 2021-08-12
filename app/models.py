class Articles:
    '''
    Articles class to define news objects
    '''
    
    def __init__(self, publishedAt, urlToImage,title,content,author,url):
      self.publishedAt = publishedAt
      self.urlToImage= urlToImage
      self.title = title
      self.content =content
      self.author = author
      self.url = url
      
class News:
    '''
    News class to define news objects
    '''

    def __init__(self, name, url, description, country, category, id):
        self.name = name
        self.url = url
        self.description = description
        self.country = country
        self.category = category
        self.id = id