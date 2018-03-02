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

def wrap_words(s, limit):
    if not s:
        return []
    output_bank = []
    word_chunk=''
    word_chunks = s.split()
    for chunk in word_chunks:
        if limit > len(word_chunk + chunk):
            word_chunk = (word_chunk + " {0}".format(chunk)).strip()
        else:
            output_bank.append(word_chunk)
            word_chunk = chunk
    if word_chunk:
       output_bank.append(word_chunk)
    return output_bank

print (wrap_words("The quick, superduperlong brown fox jumped over the lazy dog.", 10))
