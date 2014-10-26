{
  'targets': [
    {
      'target_name': 'yajl',
      'product_extension': 'node',
      'type': 'shared_library',
      'include_dirs': [
        "<!(node -e \"require('nan')\")"
      ],
      'sources': [
        'src/version.cc',
      ],
      'dependencies': [
        './deps/libyajl.gyp:libyajl'
      ]
    }
  ]
}
