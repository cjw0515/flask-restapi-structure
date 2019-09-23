def filter_query(query, filter_condition):
    '''
    Return filtered queryset based on condition.
    :param query: takes query
    :param filter_condition: Its a list, ie: [(key,operator,value)]
    operator list:
        eq for ==
        lt for <
        ge for >=
        in for in_
        like for like
        value could be list or a string
    :return: queryset

    '''

    if query is None:
        query = self.get_query()
    model_class = self.get_model_class()  # returns the query's Model
    for raw in filter_condition:
        try:
            key, op, value = raw
        except ValueError:
            raise Exception('Invalid filter: %s' % raw)
        column = getattr(model_class, key, None)
        if not column:
            raise Exception('Invalid filter column: %s' % key)
        if op == 'in':
            if isinstance(value, list):
                filt = column.in_(value)
            else:
                filt = column.in_(value.split(','))
        else:
            try:
                attr = list(filter(
                    lambda e: hasattr(column, e % op),
                    ['%s', '%s_', '__%s__']
                ))[0] % op
            except IndexError:
                raise Exception('Invalid filter operator: %s' % op)
            if value == 'null':
                value = None
            filt = getattr(column, attr)(value)
        query = query.filter(filt)
    return query