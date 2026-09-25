def vectorize(seq: str, part: int) -> dict:
    domains = {}
    seq = seq.replace("\n", "").replace(" ", "").replace("\t", "")
    for t in range(part):
        for i in range(len(seq) // part + 1):
            batch = seq[i * part + t:i * part + part + t]
            domains[batch] = domains.get(batch, 0) + 1
            if len(batch) < part:
                break
    return domains