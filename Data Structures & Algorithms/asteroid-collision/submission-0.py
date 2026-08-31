class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        
        for ast in asteroids:
            # Collision happens only if stack has a positive asteroid 
            # and the current asteroid is negative (moving left)
            while stack and stack[-1] > 0 and ast < 0:
                diff = stack[-1] + ast
                
                if diff < 0:
                    # Top of stack is smaller, so it explodes
                    stack.pop()
                elif diff > 0:
                    # Current asteroid is smaller, so it explodes
                    ast = 0
                    break
                else:
                    # Both are equal in size, both explode
                    stack.pop()
                    ast = 0
                    break
            
            # If the current asteroid survived all collisions, add it to the stack
            if ast != 0:
                stack.append(ast)
                
        return stack