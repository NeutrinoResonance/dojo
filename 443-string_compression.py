class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """

        s = chars
        string_length = len(s)
        read_idx = 0

        last_char = None
        last_char_count = None

        while read_idx <= string_length:
            
            # Simulate an extra character at the end of the string so that
            # we do not have to duplicate the compression logic elsewhere
            if read_idx < string_length:
                current = s[read_idx]
            elif read_idx == string_length:
                current = 8888

            if last_char == None:
                last_char_count = 1
            else:
                if last_char != current:
                    if last_char_count == 1:
                        s[read_idx - 1] = last_char
                    elif last_char_count > 1:
                        # Stamp in the last character
                        s[read_idx - last_char_count] = last_char

                        # Write in the character count string
                        str_char_count = str(last_char_count)
                        start_length_idx = read_idx - last_char_count + 1
                        j = start_length_idx

                        while j < start_length_idx + len(str_char_count):
                            s[j] = str_char_count[j - start_length_idx]
                            j += 1

                        # Make the rest of the un-compressed string contiguous
                        # with the compressed string
                        k = start_length_idx + len(str_char_count)
                        copy_read_idx = read_idx
                        while copy_read_idx < string_length:
                            s[k] = s[copy_read_idx]
                            k += 1
                            copy_read_idx += 1

                        # Shorten the final string length
                        string_length -= last_char_count
                        string_length += len(str_char_count) + 1

                        # Zero out the parts of the old string
                        l = string_length
                        while l < len(s):
                            s[l] = None
                            l += 1

                        read_idx = j
                        last_char_count = 1
                    else:
                        raise Exception("last_char_count is not a positive number!")
                else:
                    last_char_count += 1

            last_char = current
            read_idx += 1

        return string_length
    
