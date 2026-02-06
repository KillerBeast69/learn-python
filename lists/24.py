def filter_messages(messages):
    no_dang = []
    dang_count = []
    for message in messages:
        words = []
        words = message.split(" ")
        good_words = []
        dangs = []
        for word in words:
            if word == "dang":
                dangs.append(word)
            else:
                good_words.append(word)
            good_string = good_words.join()
            no_dang.append(good_string)
            count_dang = len(dangs)
            dang_count.append(count_dang)
    return no_dang, dang_count