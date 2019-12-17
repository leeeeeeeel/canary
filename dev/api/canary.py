""" """

def suggest(history):
    possibles = []
    # possibles is an array of
    # ["music_id":<str>, "relevance":<float>]

    # for each music in history get from database music entry as A
    # music entry loock like:
    # [music:["name":<str>, "band":<str>], "relations":[]]
    # where "relations" is a 1000 length list of:
    # ["music_id":<str>, "relevance":<float>]
    # from entry get all relations and throw in  possibles \
    # multiplying its relevance by A relevance, if a entry of \
    # this music already exist in possibles add its relevance multiplyed \
    # by A music relevance to possibles entry

    # return 100 most relevant possibles entrys

    return "cu"
