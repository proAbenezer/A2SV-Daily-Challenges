# Problem: Divide Players Into Teams of Equal Skill - https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        commulative_product = 0
        target_value = skill[-1] + skill[0]
        n = len(skill)
        left = 0
        right = n - 1
        while left < right:
            if skill[left] + skill[right] != target_value:
                return -1
            commulative_product += skill[left] * skill[right]
            left += 1
            right -= 1
        return commulative_product

        