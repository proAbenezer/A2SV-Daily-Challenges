# Problem: Remove Comments - https://leetcode.com/problems/remove-comments/

class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        final_output = []
        in_block_comment = False
        current_line = []

        for line in source:
            index, line_length = 0, len(line)

            if not in_block_comment:
                current_line = []

            while index < line_length:
                if in_block_comment:
                    if index + 1 < line_length and line[index: index + 2] == "*/":
                        in_block_comment = False
                        index += 1
                else:
                    if index + 1 < line_length and line[index: index + 2] == "/*":
                        in_block_comment = True
                        index += 1
                    elif index + 1 < line_length and line[index: index + 2] == "//":
                        break
                    else:
                        current_line.append(line[index])
                index += 1
                
            if current_line and not in_block_comment:
                    final_output.append("".join(current_line))
        return final_output
                        
                
        