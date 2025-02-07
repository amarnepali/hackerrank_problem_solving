def count_substring(string, sub_string):
    list_string = list(string)
    len_substring = len(sub_string)

    new_pattern_list= [''.join(list_string[i:i+len_substring]) for i in range(len(list_string))]
    print(new_pattern_list)
    matched_string = list(filter (lambda a:a == sub_string, new_pattern_list))
    print(matched_string)
    return len(matched_string)

if __name__ == '__main__':
    string = input().strip()
    # print(type(string))
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)