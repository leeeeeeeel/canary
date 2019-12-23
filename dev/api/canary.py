""" """

def suggest(history):
    possibles = []
    # possibles is an array of
    # ["music_id":<str>, "relevance":<float>]

    #-for each music in history get from database music entry as [A]
    #   music entry looks like:
    #   [music:["name":<str>, "band":<str>], "relations":[]]
    #   where "relations" is a 1000 length list of:
    #   ["music_id":<str>, "relevance":<float>]
    #-from entry get all "relations" and throw in  [possibles] multiplying
    #   its relevance by [A]'s relevance, if a entry of this music already
    #   exists in [possibles] add its multiplyed relevance to existing
    #   [possibles] entry

    # return an array containing the 100 most relevant [possibles] entrys

    return "cu"
