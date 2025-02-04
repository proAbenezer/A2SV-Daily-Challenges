# Problem: Masking Personal Information - https://leetcode.com/problems/masking-personal-information/description/?envType=problem-list-v2&envId=string

class Solution:
    def maskPII(self, s: str) -> str:
        def mask_email(s):
            name, domain = s.split("@")
            return name[0] + ("*" * 5) + name[-1] + "@" + domain

        def mask_phone(s):
            separaters = ['+', '-', '(', ')', ' ']
            for char in s:
                if char in separaters:
                    s = s.replace(char, "")
            country_code, local_number = [s[:len(s) - 10], s[len(s) - 10:]]
            length_of_country_code = len(country_code)
            if length_of_country_code == 0:
                return "***-***-" + local_number[6:]
            elif length_of_country_code == 1:
                return "+*-***-***-" + local_number[6:]
            elif length_of_country_code == 2:
                return "+**-***-***-" + local_number[6:]
            elif length_of_country_code == 3:
                return "+***-***-***-" + local_number[6:]


        if '.' in s:
            s = s.lower()
            return mask_email(s)
        else:
            return mask_phone(s)
        