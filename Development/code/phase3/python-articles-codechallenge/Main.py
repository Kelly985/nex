from Author import Author
from Magazine import Magazine
from Article import Article

kelly = Author("kelly mwiti")
ronny = Author("ronny koome")

nairobian = Magazine("The Nairobian", "full focus")
pulse = Magazine("The pulse", "entertainment")

kelly.add_article(nairobian, "wash wash")
kelly.add_article(pulse, "music billboard")
ronny.add_article(pulse, "the kardashians")
kelly.add_article(nairobian, "nabii scandals")

print(kelly.articles())
print(kelly.magazines())
print(kelly.topic_areas())
print(nairobian.contributors())
print(Magazine.find_by_name("The pulse"))
print(nairobian.contributing_authors())
