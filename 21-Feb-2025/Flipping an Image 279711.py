# Problem: Flipping an Image - https://leetcode.com/problems/flipping-an-image/description/

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        # Get the number of columns in the image
        num_columns = len(image)
      
        # Traverse each row of the image
        for row in image:
            # Set two pointers, starting from the beginning and the end of the row respectively
            left, right = 0, num_columns - 1
          
            # Continue swapping pixels until the pointers meet or cross
            while left < right:
                # If the values at the current pixels are the same, invert them
                if row[left] == row[right]:
                    row[left] = 1 - row[left]    # flip the pixel value
                    row[right] = 1 - row[right]  # flip the pixel value
              
                # Move the pointers towards the center
                left += 1
                right -= 1
          
            # If the number of columns is odd, flip the central pixel
            if left == right:
                row[left] = 1 - row[left]
      
        # Return the modified image
        return image