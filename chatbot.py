import re

pairs = []
input_docs = []
target_docs = []


def __create_pairs():
    # Creating pairs
    data_path = "human_text.txt"
    data_path2 = "robot_text.txt"
    # Defining lines as a list of each line
    with open(data_path, 'r', encoding='utf-8') as f:
        lines = f.read().split('\n')
    with open(data_path2, 'r', encoding='utf-8') as f:
        lines2 = f.read().split('\n')
    lines = [re.sub(r"\[\w+\]", 'hi', line) for line in lines]
    lines = [" ".join(re.findall(r"\w+", line)) for line in lines]
    lines2 = [re.sub(r"\[\w+\]", '', line) for line in lines2]
    lines2 = [" ".join(re.findall(r"\w+", line)) for line in lines2]
    # grouping lines by response pair
    pairs = list(zip(lines, lines2))
    # random.shuffle(pairs)
    return pairs


def __create_tokens():
    # input_docs = []
    # target_docs = []
    input_tokens = set()
    target_tokens = set()
    for line in pairs[:400]:
        input_doc, target_doc = line[0], line[1]
        # Appending each input sentence to input_docs
        input_docs.append(input_doc)
        # Splitting words from punctuation
        target_doc = " ".join(re.findall(r"[\w']+|[^\s\w]", target_doc))
        # Redefine target_doc below and append it to target_docs
        target_doc = '<START> ' + target_doc + ' <END>'
        target_docs.append(target_doc)

        # Now we split up each sentence into words and add each unique word to our vocabulary set
        for token in re.findall(r"[\w']+|[^\s\w]", input_doc):
            if token not in input_tokens:
                input_tokens.add(token)
        for token in target_doc.split():
            if token not in target_tokens:
                target_tokens.add(token)

    input_tokens = sorted(list(input_tokens))
    target_tokens = sorted(list(target_tokens))
    num_encoder_tokens = len(input_tokens)
    num_decoder_tokens = len(target_tokens)

    # features dictionary is used to encode sentences into one-hote vectors; key is word, value is index
    input_features_dict = dict(
        [(token, i) for i, token in enumerate(input_tokens)])
    target_features_dict = dict(
        [(token, i) for i, token in enumerate(target_tokens)])
    # reverse features dictionary is used to decode sentences into one-hote vectors; key is index, value is word
    reverse_input_features_dict = dict(
        (i, token) for token, i in input_features_dict.items())
    reverse_target_features_dict = dict(
        (i, token) for token, i in target_features_dict.items())


# def __setup_training():


def get_output():
    __create_pairs()
    __create_tokens()
    # __setup_training()
