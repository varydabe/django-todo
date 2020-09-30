def single_transform(values):
    return {
        'task': values.task,
        'user_id': values.user_id
    }


def transform(values):
    arr = []

    for item in values:
        arr.append(single_transform(item))

    return arr
