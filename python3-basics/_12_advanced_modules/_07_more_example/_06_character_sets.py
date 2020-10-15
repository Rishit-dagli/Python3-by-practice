from org.konghiran.lesson._12_advanced_modules._07_more_example._04_create_re_function_test_patterns import \
    multi_re_find

test_phrase = 'sdsd..sssddd...sdddsddd...dsds...dsssss...sdddd'

test_patterns = ['[sd]',  # either s or d
                 's[sd]+']  # s followed by one or more s or d

multi_re_find(test_patterns, test_phrase)