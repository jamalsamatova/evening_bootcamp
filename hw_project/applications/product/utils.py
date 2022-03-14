from transliterate import slugify


def slug_generator(title):
    slug = slugify(title.lower())
    return slug