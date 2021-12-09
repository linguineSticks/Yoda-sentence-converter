import nltk

from nltk.corpus import treebank


def get_productions(parsed_sents):
    """
    Get all production rules from a parsed corpus

    Args:
        parsed_sents [nltk.tree.Tree]: parsed sentences
    Returns:
        [nltk.grammar.Production]: list of productions
    """

    productions = []

    for tree in parsed_sents:
        # Turn the productions into Chomsky Normal Form
        tree.collapse_unary(collapsePOS=False)  # Remove unary nodes except for leaves
        tree.chomsky_normal_form(horzMarkov=2)  # Remove ternary nodes
        productions += tree.productions()
    return productions

def parse(in_grammar, sent):
    """
    Get the list of parse trees of the given sentence
    conforming the grammar

    Args:
        grammar (str): name of the grammar file (CFG)
        sent (str): sentence

    Returns:
        (list): list of trees
    """

    #my_grammar = nltk.data.load(f"file:{grammar}.cfg")
    my_sent = nltk.word_tokenize(sent)
    my_parser = nltk.ChartParser(in_grammar)

    my_trees = my_parser.parse(my_sent)
    return list(my_trees)


def get_sbj(sent):
    """
    Get the subject of the given sentence

    Args:
        sent (str): sentence

    Returns:
        (str): subject
    """

    my_trees = parse("my_grammar", sent)
    my_tree = my_trees[0]

    sbj_tree = my_tree[0]
    return " ".join(sbj_tree.leaves())

def getObj(in_grammar,sent):
    """
    Get the obj of the given sentence

    Args:
        sent (str): sentence

    Returns:
        (str): subject
    """

    my_trees = parse(in_grammar, sent)
    my_tree = my_trees[0]
    obj_tree = my_tree[1][1]
    vp_tree = my_tree[1]
    vp = " ".join(vp_tree.leaves())
    #vp = vp.split()
    #vp.remove(vp[0])
    obj = " ".join(obj_tree.leaves())
    return obj

def getOSV(in_grammar, sent):
    mytrees = parse(in_grammar, sent)
    mytree = mytrees[0]
    obj_tree = mytree[1][1]
    sbj_tree = mytree[0]
    vp_tree = mytree[1]
    subj = " ".join(sbj_tree.leaves())
    #vp = vp_tree.split()
    v1 = vp_tree[0]
    v = " ".join(v1.leaves())
    obj = " ".join(obj_tree.leaves())
    return obj, subj, v





def main():
    productions = get_productions(nltk.corpus.treebank.parsed_sents())
    #print(len(productions))
    my_grammar = nltk.CFG(nltk.Nonterminal("S"), productions)
    sent = input("Enter a transitive sentence given the lexicon: ")
    ob, sub, vb = getOSV(my_grammar,sent)
    print("Yoda would say, {:s} {:s} {:s}".format(ob, sub, vb))




main()


