from org.konghiran.lesson._12_advanced_modules._07_more_example._04_create_re_function_test_patterns import \
    multi_re_find

test_phrase = 'sdsd..sssddd...sdddsddd...dsds...dsssss...sdddd'

test_patterns = ['sd*',  # s followed by zero or more d's
                 'sd+',  # s followed by one or more d's
                 'sd?',  # s followed by zero or one d's
                 'sd{3}',  # s followed by three d's
                 'sd{2,3}',  # s followed by two to three d's
                 ]

multi_re_find(test_patterns, test_phrase)
