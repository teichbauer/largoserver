data = {
    # --------------------------------------------------------
    # PS
    # --------------------------------------------------------
    'CS-PS001': {
        '_id': 'META-CS-PS001',
        'cat': 'PS001',
        'nick-name': 'single person',
        'properties': {
            'LS_name': {
                'descr': 'formal name in diff languages',
                'type': 'LS-dict of utf-8 str', 
                # value: {'en':'..','zh':'..',...}
                'required': True,
            },
            'sex': {    # male, female
                'descr': 'gender',
                'type': 'str',
                'value': ('male','female'),
                'required': True,
            },
            'mstatus': {    # unk, unm, mar, wdw, dvc
                'descr': 'marital status',
                'type': 'str',
                'value': (
                    'unk',  # unkown
                    'unm',  # unmarried
                    'mrd',  # maried
                    'wdw',  # widowed
                    'dvc',  # divorced   
                ),
                'required': False,
            },
            'dob': {
                'descr': 'date of birth',
                'type': 'date-str', 
                # value: 2022, 2022-04, 2022-01-30, 2022-02-13
                'required': False,
            },
            'dod': {
                'descr': 'date of death',
                'type': 'date-str', 
                # value: 2022, 2022-04, 2022-01-30, 2022-02-13
                'required': False,
            },
            'LS_pob': {
                'descr': 'place of birth',
                'type': 'LS-dict of utf-8 str', 
                # value: {'en':'..','zh':'..',...}
                'required': False,
            },
            'LS_pod': {
                'descr': 'place of death',
                'type': 'LS-dict of utf-8 str', 
                # value: {'en':'..','zh':'..',...}
                'required': False,
            },
            'LS_brp': {
                'descr': 'burial place',
                'type': 'LS-dict of utf-8 str', 
                # value: {'en':'..','zh':'..',...}
                'required': False,
            },
        },
        'relationships': {
            'possibles': (
                'R1001',    # child(this) has parents
                'R1011',    # has adopting parents
                'R0002',    # has marraige
                'R0003',    # has public keys
                'R0004',    # has synopsis
                'R0008',    # has documents
            )
        }
    }, # CPS001: single person
    'CS-PS002': {
        '_id': 'META-CS-PS002',
        'cat': 'PS002',
        'nick-name': 'a couple of persons, as a pair',
        'properties': {
            'male': {     # male in this family-union
                'descr': '_id of a PS001 - a male in this family-union',
                'type': 'str',      # _id of the male PS001
                'required': False,  # male / female: at least one present
            },
            'female': {    # female in this family-union
                'descr': '_id of a PS001 - a female in this family-union',
                'type': 'str',      # _id of the male PS001
                'required': False,  # male / female: at least one present
            },
            'pom': {
                'descr': 'place of marriage',
                'type': 'LS-str ',
                'required': False,
            },
            'dom': {
                'descr': 'date of marriage',
                'type': 'str - date str',
                'required': False,
            },
        },
        'relationships': (
            'R0006',    # marriage-has-male. PS002 -> PS0001:   str
            'R0007',    # marriage-has-female. PS002 -> PS0001: str
            'R0001',    # parent(s)->child. PS002 -> PS001:     []
            'R0008',    # has-document
        )
    },
    # --------------------------------------------------------
    # DS
    # --------------------------------------------------------
    'CS-DS001': {
        '_id': 'META-CS-DS001',
        'cat': 'DS001',
        'nick-name': 'txt-doc: synopsis: textual file, intro of a person',
        'properties': {
            'format': {
                'descr': 'keyword for type of document',
                'value': (
                    'txt',  # utf-8 text file
                    'pdf',  # PDF formatted file
                    'wrd',  # MS word forma
                    'unk',  # unknown
                ),
            },
            'type': 'txt',
            'date': 'date when it ihas been updated',
            'content': 'LS-str'
        },
        'relationships': (
            'R0005',        # has-owner
        )
    },
    'CS-DS002': {
        '_id': 'META-CS-DS002',
        'cat': 'DS002',
        'nick-name': 'folders',
        'properties': {
            'created': {
                'descr': 'when it has been created',
                'type': 'date str',
                'required': True
            },
        },
        'relationships': (
            'R0005',    # has-owner
            'R0009',    # containing
            'R0010',    # contained-by
        )
    },
    'CS-DS003': {
        '_id': 'META-CS-DS003',
        'cat': 'DS003',
        'nick-name': 'single document',
        'properties': {
            'keywords': {
                'location': 'LS-str',
                'vips': 'list of names',        # people's names
                'date-range': '2 date-strs',    # happened during
                'category': '[] str'            
                # category keywords:
                # -------------------
                # family, 
                # friend, 
                # encounter, 
                # scenery, 
                # artifacts, 
                # event, 
                # biz
            },
            'media-type': {
                'descr': 'type of media',
                'required': True,
                'value': (
                    'text',
                    'audio',
                    'image',
                    'video',
                ),
            },
            'source': {
                'descr': 'where this file is located',
                # this can be url, file-path on local machine, 
                'type': 'str',
                'required': True
            },
            'file-type': {
                'descr': 'file extension',
                'required': True,
                'value': (
                    'txt',
                    'pdf',
                    'doc',
                    'xdoc',
                    'jpg',
                    'png',
                    'gif',
                    'mp3', 
                    'avi',
                    'mp4',
                ),
            },
            'size': {
                'descr': 'size in bytes',
                'type': 'int',
                'required': True,
            },
            'signature': {
                'descr': 'sha-256 signature of this file',
                'type': 'str',
                'required': True,
            },
            'last-touched': {
                'descr': 'time stampe when this was lastly created, modified',
                'date': 'date-time str',
                'required': True,
            },
        },
        'relationships': (
            'R0010',    # contained-by
            'R0005',    # has owner
        )
    },
    # --------------------------------------------------------
    # CS
    # --------------------------------------------------------
    'CS-CS000': {
        '_id': 'META-CS-CS000',
        'cat': 'CS000',
        'nick-name': 'rsa-key',
        'properties': {
            'rsa-public-key': {
                'type': 'str',
                'required': True
            },
            'rsa-private-key': {
                'type': 'str',
                'required': True
            }
        },
        'relationships': (
            'R00005',   # PS001 owner id
        )
    },
    'CS-CS001': {
        '_id': 'META-CS-CS001',
        'cat': 'CS001',
        'nick-name': 'login acount',
        'properties': {
            'user-name': {
                'descr': 'user name',
                'type':'str',
                'required': True,
            },
            'email': {

            },
            'pwd': {
                'descr': 'password for logging in',
                'type': 'str',
                'content': 'str',
            }
        },
        'relationships': (

        )
    },
    'CS-CS002': {
        '_id': 'META-CS-CS002',
        'cat': 'CS002',
        'descr': 'bank account',
        'properties': {
        },
        'relationships': (

        )
    },
}