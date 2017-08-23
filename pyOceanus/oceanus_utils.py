def get_NN_compounds(oc_data):
    words = [[y[0] for y in x] for x in oc_data.tokens]
    poses = [[y[1] for y in x] for x in oc_data.tokens]
    
    nn_list = get_NNs(poses, words)
    nn_compounds = get_compounds(nn_list) 
    return nn_compounds


def get_NNs(pos_seqs, words_seqs):    
    return [get_tags_seq(x, y, "NN") for x, y in 
            zip(pos_seqs, words_seqs)]

def get_tags_seq(pos_list, word_list, tag):
    idx_list = []
    start_i = 0
    for i in range(len(pos_list)-1):        
        if pos_list[i] == tag and pos_list[i+1] != tag:
            start_i = i if start_i < 0 else start_i
            idx_list.append({
                "word": [word_list[wi] for wi in range(start_i, i+1)],
                "idx": list(range(start_i, i+1))
                })
            start_i = i+1
        elif pos_list[i] == tag:
            start_i = i
        else:
            start_i = -1
    return idx_list

def get_PNs(pos_seqs, words_seqs):
    return [get_tags_seq(x, y, "PN") for x, y in 
            zip(pos_seqs, words_seqs)]

def get_compounds(nns_list):
    com_buf = []
    for seq_x in nns_list:
        for nns in seq_x:
            com_buf.append("".join(nns["word"]))
    return com_buf
