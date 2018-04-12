# s: "The quick, superduperlong brown fox jumped over the lazy dog."
# limit: 10
# output: [
#    "The quick,",
#    "superduperlong",
#    "brown fox",
#    "jumped",
#    "over the",
#    "lazy dog.",
# ]
#
# s: ""
# output: [""]
# if single word exceeds limit, count it as its own entry in the output.

abc = "The quick, superduperlong brown fox jumped over the lazy dog."
def text_chunker(text, limit):
    output = []
    text = text.split(" ")
    curr_limit = ''
    for word in text:
        if (len(word) + len(curr_limit)) > (limit - 1):
            output.append(curr_limit)
            curr_limit=word
        elif not curr_limit:
            curr_limit=word
        else:
            curr_limit = " ".join([curr_limit, word])

    if curr_limit:
        output.append(curr_limit)
    return output

print(text_chunker(abc, 10))
