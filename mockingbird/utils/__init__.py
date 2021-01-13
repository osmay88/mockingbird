
def hash_url(url: str):
    """
    return the hash of a string
    """
    from hashlib import sha1
    hash_ = sha1(url.encode())
    return hash_.hexdigest()


def extract_namespace_from_url(url: str):
    """
    Return the first part of a url path. This is used as namespace
    for stubs.
    """
    tokenized = url.split("/")
    if not len(tokenized):
        return ""
    else:
        return tokenized[1]
