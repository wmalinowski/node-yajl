{
  'configurations': {
    'Debug': {
      'defines': [ 'DEBUG', '_DEBUG' ]
    },
    'Release': {
      'defines': [ 'NDEBUG' ]
    }
  },
  'conditions': [
    ['OS == "win"', {
      'defines': [
        'WIN32'
      ],
      'cflags':[
        '/wd4996',
        '/wd4255',
        '/wd4130',
        '/wd4100',
        '/wd4711',
        '/O2'
      ]
    }],
    ['OS != "win"', {
      'cflags':[
        '-Wall',
        '-fvisibility=hidden',
        '-std=c99',
        '-pedantic',
        '-Wpointer-arith',
        '-Wno-format-y2k',
        '-Wstrict-prototypes',
        '-Wmissing-declarations',
        '-Wnested-externs',
        '-Wextra',
        '-Wundef',
        '-Wwrite-strings',
        '-Wold-style-definition',
        '-Wredundant-decls',
        '-Wno-unused-parameter',
        '-Wno-sign-compare',
        '-Wmissing-prototypes',
        '-O2',
        '-Wuninitialized'
      ],
    }]
  ],
  'targets': [
    {
      'target_name': 'copy_includes',
      'type': 'none',
      'copies': [
          {
            'files': [
              'yajl/src/api/yajl_common.h',
              'yajl/src/api/yajl_gen.h',
              'yajl/src/api/yajl_parse.h',
              'yajl/src/api/yajl_tree.h',
              'yajl/src/api/yajl_version.h.cmake'
            ],
            'destination': '<(SHARED_INTERMEDIATE_DIR)/includes/yajl'
          }
      ],
      'actions': [
        {
          'action_name': 'generate_version_h',
          'inputs': [
            '<(SHARED_INTERMEDIATE_DIR)/includes/yajl/yajl_version.h.cmake'
          ],
          'outputs': [
            '<(SHARED_INTERMEDIATE_DIR)/includes/yajl/yajl_version.h'
          ],
          'action': ['python',
                     'generate_version_h.py',
                     '<(RULE_INPUT_PATH)',
                     'yajl/CMakeLists.txt',
                     '<(SHARED_INTERMEDIATE_DIR)/includes/yajl/yajl_version.h'
                     ]
        }
      ]
    },
    {
      'target_name': 'libyajl',
      'type': 'static_library',
      'dependencies': [
        'copy_includes'
      ],
      'sources': [
        'yajl/src/yajl.c',
        'yajl/src/yajl_lex.c',
        'yajl/src/yajl_parser.c',
        'yajl/src/yajl_buf.c',
        'yajl/src/yajl_encode.c',
        'yajl/src/yajl_gen.c',
        'yajl/src/yajl_alloc.c',
        'yajl/src/yajl_tree.c',
        'yajl/src/yajl_version.c'
      ],
      'include_dirs': [
        '<(SHARED_INTERMEDIATE_DIR)/includes/'
      ],
      'direct_dependent_settings': {
        'include_dirs': [
          '<(SHARED_INTERMEDIATE_DIR)/includes/'
        ],
      }
    }
  ]
}