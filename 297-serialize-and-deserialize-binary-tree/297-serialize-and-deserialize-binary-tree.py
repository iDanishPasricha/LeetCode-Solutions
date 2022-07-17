# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        ans=[];
        def dfs(root):
            if root is None:
                ans.append("N");
                return
            
            ans.append(str(root.val))
            dfs(root.left);
            dfs(root.right);
        dfs(root);
        return ",".join(ans)
                
        
        
        
        

    def deserialize(self, data):
        nums = data.split(",");
        print(nums)
        self.i=0;
        def dfs():
            if nums[self.i]=="N":
                self.i+=1;
                return None

            node = TreeNode(int(nums[self.i]))
            self.i+=1;
            node.left = dfs();
            node.right = dfs();
            return node
        return dfs()
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))