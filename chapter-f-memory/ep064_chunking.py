"""EP064 · Chunking: split on paragraphs, cap the size, overlap a little, keep the source."""


def chunk(text, source, max_words=12, overlap=3):
    words = text.split()
    out, start = [], 0
    while start < len(words):
        piece = words[start:start + max_words]
        out.append({"source": source, "start": start, "text": " ".join(piece)})
        if start + max_words >= len(words):
            break
        start += max_words - overlap
    return out


if __name__ == "__main__":
    doc = ("Agents loop over tools. Memory stores facts across sessions. "
           "Retrieval finds the right facts when the model needs them. "
           "Chunk size changes what retrieval can find.")
    for c in chunk(doc, "notes.md"):
        print(c)
