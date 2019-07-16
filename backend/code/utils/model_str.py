def str_for_model(model):
    """
    更改默认打印，更可读
    """
    t = None
    if hasattr(model, 'title'):
        t = model.title
    elif hasattr(model, 'name'):
        t = model.name
    elif hasattr(model, 'username'):
        t = model.username
    elif hasattr(model, 'website_name'):
        t = model.website_name
    return '{} object (pk:{}): <{}>'.format(model.__class__.__name__, model.pk, t)
