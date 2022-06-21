data = {
    'R0001': {
        '_id': 'META-RS-R0001',
        'descr': 'parent(s)->child. PS002 -> PS001',
        'reverse': 'R1001',  # child->parent(s)
    },
    'R1001': {
        '_id': 'META-RS-R1001',
        'descr': 'child->parent(s). PS001 -> PS002',
        'reverse': 'R0001',
    },
    'R0002': {
        '_id': 'META-RS-R0002',
        'descr': 'has-marriage. PS001 -> PS002',
        'reverse': '',  # not reversable
    },
    'R0003': {
        '_id': 'META-RS-R0003',
        'descr': 'has-account. PS001 -> CSnnn',
        'reverse': 'R0005',  # not reversable
    },
    'R0004': {
        '_id': 'META-RS-R0004',
        'descr': 'has-synopsis. PS00x -> DS001'
    },
    'R0005': {
        '_id': 'META-RS-R0005',
        'descr': 'has-owner. x -> PS00x'
    },
    'R0006': {
        '_id': 'META-RS-R0006',
        'descr': 'marriage-has-male. PS002 -> PS0001',
        'reverse': '',  # not reversable
    },
    'R0007': {
        '_id': 'META-RS-R0007',
        'descr': 'marriage-has-female. PS002 -> PS0001',
        'reverse': '',  # not reversable
    },
    'R0008': {
        '_id': 'META-RS-R0008',
        'descr': 'has-document'
    },
    'R0009': {
        '_id': 'META-RS-R0009',
        'descr': 'containing'
    },
    'R0010': {
        '_id': 'META-RS-R0010',
        'descr': 'contained-by'
    },
    'R0011': {
        '_id': 'META-RS-R0011',
        'descr': 'parent(s)-(adopt)->child. PS002 -> PS001',
        'reverse': 'R1011',  # child->parent(s)
    },
    'R1011': {
        '_id': 'META-RS-R1011',
        'descr': 'child-(adopted by)->parent(s). PS001 -> PS002',
        'reverse': 'R0011',
    },
    'R0012': {
        '_id': 'META-RS-R0012',
        'descr': 'using',
        'reverse': 'R1012'
    },
    'R1012': {
        '_id': 'META-RS-R1012',
        'descr': 'used-by',
        'reverse': 'R0012'
    },
}
