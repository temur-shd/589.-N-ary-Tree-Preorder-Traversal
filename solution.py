class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        output=[]
        def call(root):
            if root==None:
                return
            output.append(root.val)
            for i in root.children:
                call(i)
        call(root)
        return output
